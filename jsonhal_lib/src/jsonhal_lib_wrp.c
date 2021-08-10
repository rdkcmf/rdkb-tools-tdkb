/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2021 RDK Management
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/
#include <unistd.h>
#include "json_hal_logger.h"
#include "jsonhal_wrp.h"
#include "jsonhal_lib_wrp.h"
#include "json_schema_validator_wrapper.h"
#include "telcovoicemgrhal_lib_wrp.h"

/*****************************************************************************************************************
 * Function Name : jsonhal_init
 * Description   : This function will invoke the json_client to connect to json hal server
 * @param [in]   : CONF_FILE
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int jsonhal_init(const char * CONF_FILE)
{
    int rc = RETURN_OK;

    if (!strcmp(CONF_FILE, XDSL_JSON_CONF_PATH))
    {
        rc = json_hal_client_init(XDSL_JSON_CONF_PATH);
    }
    else if (!strcmp(CONF_FILE, TELCOVOICEMGR_CONF_FILE))
    {
        rc = json_hal_client_init(TELCOVOICEMGR_CONF_FILE);
    }
    if (rc != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s-%d Failed to initialize hal client. \n",__FUNCTION__,__LINE__);
        return RETURN_ERR;
    }

    rc = json_hal_client_run();
    if (rc != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s-%d Failed to start hal client. \n", __FUNCTION__,__LINE__);
        return RETURN_ERR;
    }

    int retry_count = 0;
    int is_client_connected = 0;
    while (retry_count < HAL_CONNECTION_RETRY_MAX_COUNT)
    {
        if (!json_hal_is_client_connected())
        {
            sleep(1);
            retry_count++;
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s-%d Hal-client connected to the hal server \n", __FUNCTION__, __LINE__);
            is_client_connected = TRUE;
            break;
        }
    }

    if (is_client_connected != TRUE)
    {
        DEBUG_PRINT(DEBUG_TRACE,"Failed to connect to the hal server. \n");
        return RETURN_ERR;
    }
    if (!strcmp(CONF_FILE, TELCOVOICEMGR_CONF_FILE))
    {
        int bStatus = 1;
        if(telcovoicemgrhal_initdata(bStatus) !=  RETURN_OK)
        {
           DEBUG_PRINT(DEBUG_TRACE, "Failed to initialise data\n");
           rc = RETURN_ERR;
        }
    }
    return rc;
}

/*****************************************************************************************************************
 * Function Name : create_json_request_message
 * Description   : This function will be used to create a JSON messge for GET/SET operations
 * @param [in]   : request_type  - GET/SET request type
                 : param_name - Parameter Name
                 : eParamType - Parameter Type
                 : param_val - Parameter Value
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
json_object *create_json_request_message(eActionType request_type, char *param_name, eParamType type, char *param_val)
{
    json_object *jrequest = NULL;
    hal_param_t stParam;
    memset(&stParam, 0, sizeof(stParam));
    switch (request_type)
    {
        case SET_REQUEST_MESSAGE:
            jrequest = json_hal_client_get_request_header(RPC_SET_PARAMETERS_REQUEST);
            strncpy(stParam.name, param_name, sizeof(stParam.name)-1);
            stParam.type = type;
            switch (type)
            {
                case PARAM_BOOLEAN:
                case PARAM_INTEGER:
                case PARAM_UNSIGNED_INTEGER:
                case PARAM_STRING:
                {
                    strncpy(stParam.value,param_val,sizeof(stParam.value)-1);
                    json_hal_add_param(jrequest, SET_REQUEST_MESSAGE, &stParam);
                    break;
                }
                default:
                {
                    fprintf(stderr,"Invalid input\n");
                    break;
                }
            }
        break;
        case GET_REQUEST_MESSAGE:
            jrequest = json_hal_client_get_request_header(RPC_GET_PARAMETERS_REQUEST);
            strncpy(stParam.name, param_name, sizeof(stParam.name)-1);
            json_hal_add_param(jrequest, GET_REQUEST_MESSAGE, &stParam);
            break;
	default:
            break;
    }
    return jrequest;
}

/*****************************************************************************************************************
 * Function Name : jsonhal_getparam
 * Description   : This function will be used to get the parameter value using JSON HAL
 * @param [in]   : param_name  - Parameter Name
                 : param_value - Parameter Value
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int jsonhal_getparam(char *param_name, char* param_value)
{
    FILE *file_jr;
    int rc = RETURN_OK;
    int total_param_count = 0;
    int length = 0;
    char *buffer = NULL;

    json_object *jreply_msg = NULL;
    json_object *jparams = NULL;
    hal_param_t resp_param;

    json_object *jrequest = create_json_request_message(GET_REQUEST_MESSAGE, param_name, 0 , NULL);
    CHECK(jrequest != NULL);

    if (json_hal_client_send_and_get_reply(jrequest, &jreply_msg) == RETURN_ERR)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get reply for the json request \n", __FUNCTION__, __LINE__);
        return RETURN_ERR;
    }

    if (json_object_object_get_ex(jreply_msg, JSON_RPC_FIELD_PARAMS, &jparams))
    {
        total_param_count = json_object_array_length(jparams);
    }

    if (json_hal_get_param(jreply_msg, 0, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get required params from the response message \n", __FUNCTION__, __LINE__);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }

    file_jr = fopen("/nvram/TDK/tdkb_json_Response.json","w");
    fprintf(file_jr,"%s", json_object_to_json_string_ext(jreply_msg, JSON_C_TO_STRING_PRETTY));
    fclose(file_jr);

    /* JSON_SCHEMA_VALIDATION STARTS */
    rc = json_validator_init(XDSL_JSON_SCHEMA_PATH);

    file_jr = fopen("/nvram/TDK/tdkb_json_Response.json","rb");
    if (file_jr)
    {
        fseek(file_jr, 0, SEEK_END);
        length = ftell(file_jr);
        fseek(file_jr, 0, SEEK_SET);
        buffer = (char *)malloc(length);
        if (buffer)
        {
            fread(buffer, 1, length, file_jr);
        }
        fclose(file_jr);
    }

    if (buffer)
    {
        rc = json_validator_validate_request(buffer);
        if (rc !=0)
        {
            DEBUG_PRINT(DEBUG_TRACE,"Validating json Response against schema is Failed \n");
            return RETURN_ERR;
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"Validating json Response against schema is Successful \n");
        }
        free(buffer);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Failed to get the json message from file \n");
        return RETURN_ERR;
    }

    json_validator_terminate();
    /* JSON_SCHEMA_VALIDATION ENDS */

    for (int i = 0; i < total_param_count; ++i)
    {
        if (json_hal_get_param(jreply_msg, i, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get the param from response message [index = %d] \n", __FUNCTION__, __LINE__, i);
            continue;
        }

        if (strcmp (param_name,"Device.DSL.Line.1.Enable") == 0)
        {
            if (strstr (resp_param.name, "Enable"))
            {
                strcpy(param_value, resp_param.value);
                break;
            }
        }
        else if (strcmp (param_name,"Device.DSL.Line.1.LinkStatus") == 0)
        {
            if (strstr (resp_param.name, "LinkStatus"))
            {
                strcpy(param_value, resp_param.value);
                break;
            }
        }
        else if (strcmp (param_name,"Device.DSL.Line.1.EnableDataGathering") == 0)
        {
            if (strstr (resp_param.name, "EnableDataGathering"))
            {
                strcpy(param_value, resp_param.value);
                break;
            }
        }
    }

    if (rc != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get statistics data  \n", __FUNCTION__, __LINE__);
    }

    if (jrequest)
    {
        json_object_put(jrequest);
        jrequest = NULL;
    }

    if (jreply_msg)
    {
        json_object_put(jreply_msg);
        jreply_msg = NULL;
    }
    return rc;
}

/*****************************************************************************************************************
 * Function Name : jsonhal_setparam
 * Description   : This function will be used to set the parameter value using JSON HAL
 * @param [in]   : pName  - Parameter Name
                 : pType - Parameter Type
                 : pValue - Parameter Value
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int jsonhal_setparam(char *pName, eParamType pType, char *pValue)
{
    json_object *jreply_msg;
    json_object *jrequest;
    int rc = RETURN_ERR;
    json_bool status = FALSE;
    jrequest = create_json_request_message(SET_REQUEST_MESSAGE, pName, pType, pValue);
    CHECK(jrequest != NULL);

    if (json_hal_client_send_and_get_reply(jrequest, &jreply_msg) == RETURN_ERR)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get reply for the json request \n", __FUNCTION__, __LINE__);
        return rc;
    }

    if (json_hal_get_result_status(jreply_msg, &status) == RETURN_OK)
    {
        if (status)
        {
            rc = RETURN_OK;
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s - %d Set request for [%s] is failed\n", __FUNCTION__, __LINE__, pName);
        }
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get result status from json response, something wrong happened!!! \n", __FUNCTION__, __LINE__);
    }

    if (jrequest)
    {
        json_object_put(jrequest);
        jrequest = NULL;
    }

    if (jreply_msg)
    {
        json_object_put(jreply_msg);
        jreply_msg = NULL;
    }
    return rc;
}

