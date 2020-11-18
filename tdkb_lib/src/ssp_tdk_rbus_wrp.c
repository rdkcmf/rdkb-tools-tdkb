/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2020 RDK Management
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
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
#include <inttypes.h>
#include <rbus/rbus.h>
#include "ssp_tdk_rbus_wrp.h"
#include "ssp_hal_logger.h"

#define DEFAULT_BUFFERSIZE 128

static rbusHandle_t bus_handle;

/*****************************************************************************************************************
 * Function Name : ssp_rbus_checkStatus
 * Description   : This function will Retrieve the RBUS status
 * @param [in]   : status - buffer to hold RBUS status value
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_checkStatus( rbusStatus_t *status) {

    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_checkStatus wrapper\n");

    int result = RETURN_ERR;
    rbusStatus_t rbus_status = RBUS_DISABLED;
    rbus_status = rbus_checkStatus();

    DEBUG_PRINT(DEBUG_ERROR, "RBUS Status is %d\n",rbus_status);

    *status = rbus_status;

    if(rbus_status == RBUS_ENABLED || rbus_status == RBUS_ENABLE_PENDING || rbus_status == RBUS_DISABLE_PENDING || rbus_status == RBUS_DISABLED )
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_checkStatus function returns value : %d\n", rbus_status);
        result = RETURN_OK;
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_checkStatus function returns failure, %d\n", rbus_status);
        result = RETURN_ERR;
    }

    DEBUG_PRINT(DEBUG_ERROR, "Exiting ssp_rbus_checkStatus wrapper\n");
    return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_rbus_open
 * Description   : This function will open the RBUS connection
 * @param [in]   : none
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_open() {

    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_open wrapper\n");

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;

    if (bus_handle)
    {
        rbus_close(bus_handle);
    }

    ret = rbus_open(&bus_handle, "tdk_b");

    if(ret != RBUS_ERROR_SUCCESS)
    {
        DEBUG_PRINT(DEBUG_ERROR, "rbus_open failed with error code %d \n", ret);
        result = RETURN_ERR;
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "rbus_open was successful, return value is %d \n",ret);
        result = RETURN_OK;
    }

    return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_rbus_close
 * Description   : This function will close the rbus connection
 * @param [in]   : None
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_close( ) {

    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_close wrapper\n");

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;

    if (bus_handle)
    {
        ret = rbus_close(bus_handle);

        if(ret != RBUS_ERROR_SUCCESS)
        {
            DEBUG_PRINT(DEBUG_ERROR, "rbus_close failed with error code %d \n", ret);
            result = RETURN_ERR;
        }
        else
        {
            DEBUG_PRINT(DEBUG_ERROR, "rbus_close was successful, return value is %d \n",ret);
            result = RETURN_OK;
        }
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "rbus was not opened properly, bus_handle was null");
        result = RETURN_ERR;
    }
    return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_rbus_dataElements
 * Description   : This function will invoke rbus_regDataElements / rbus_unregDataElements RBUS APIs
                 : rbus_regDataElements - To register one or more Data Elements that will be accessible/subscribable by other components
                 : rbus_unregDataElements - To unregister one or more previously registered Data Elements that will no longer be accessible
 * @param [in]   : element1 - Data Element name (Parameter Name)
                 : element2 - Data Element name (Parameter Name)
                 : operation - To specify, Regsister / UnRegister operation
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_dataElements (char* element1, char* element2,char* operation) {

    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_dataElements wrapper\n");

    DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_dataElements Element 1: %s, Element 2: %s  and Operation %s \n", element1,element2, operation);

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;

    if (bus_handle != NULL)
    {
        rbusDataElement_t dataElements[2] = {
        {element1, RBUS_ELEMENT_TYPE_EVENT, {NULL, NULL, NULL, NULL, NULL}},
        {element2, RBUS_ELEMENT_TYPE_EVENT, {NULL, NULL, NULL, NULL, NULL}}
        };

        if (strcmp(operation, "Register") == 0)
            ret = rbus_regDataElements(bus_handle, 2, dataElements);
        else if(strcmp(operation , "UnRegister") == 0)
            ret = rbus_unregDataElements(bus_handle, 2, dataElements);
        else
        {
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_dataElements Invalid operation name ");
            return RETURN_ERR;
        }

        if(ret != RBUS_ERROR_SUCCESS)
        {
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_dataElements operation %s Failed: %d\n",operation, ret);
            result = RETURN_ERR;
        }
        else
        {
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_dataElements operation %s Success: %d\n",operation, ret);
            result = RETURN_OK;
        }
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_dataElements bus_handle was null\n");
        result = RETURN_ERR;
    }

    DEBUG_PRINT(DEBUG_ERROR, "Exit from ssp_rbus_dataElements wrapper\n");
    return result;
}


/*****************************************************************************************************************
 * Function Name : ssp_rbus_session
 * Description   : This function will invoke rbus_createSession / rbus_getCurrentSession RBUS APIs to open new session
                 : and get the session ID
 * @param [in]   : operation - To specify Create Session or Get Current Session ID
                 : sessionID - To get the Session ID value
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_session(char* operation, unsigned int *sessionID) {

    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_session wrapper\n");

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;

    if (bus_handle != NULL)
    {
        if (strcmp(operation,"CreateSession") == 0)
        {
            ret = rbus_createSession(bus_handle,sessionID);
        }
        else if (strcmp(operation,"GetSession") == 0)
        {
            ret = rbus_getCurrentSession(bus_handle,sessionID);
        }
        else
        {
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_session Invalid Operation Name\n");
            return RETURN_ERR;
        }

        if(ret != RBUS_ERROR_SUCCESS)
        {
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_session Operation %s Failed: %d\n",operation, ret);
            result = RETURN_ERR;
        }
        else
        {
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_session Operation %s Success: %d\n",operation, ret);
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_session Session ID is: %d\n", sessionID);
            result = RETURN_OK;
        }
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_session bus_handle was NULL");
        result = RETURN_ERR;
    }

    DEBUG_PRINT(DEBUG_ERROR, "Exit from ssp_rbus_session wrapper\n");
    return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_rbus_closeSession
 * Description   : This function will invoke the rbus api rbus_closeSession to close the current session
 * @param [in]   : sessionID - Session to be closed
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_closeSession(unsigned int sessionID) {

    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_closeSession wrapper\n");

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;

    if (bus_handle != NULL)
    {
        ret = rbus_closeSession(bus_handle,sessionID);

        if(ret != RBUS_ERROR_SUCCESS)
        {
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_closeSession failed: %d\n", ret);
            result = RETURN_ERR;
        }
        else
        {
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_closeSession success: %d\n", ret);
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_closeSession Session ID is: %d\n", sessionID);
            result = RETURN_OK;
        }
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_closeSession bus_handle was NULL \n");
        result = RETURN_ERR;
    }

    DEBUG_PRINT(DEBUG_ERROR, "Exit from ssp_rbus_close wrapper\n");
    return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_rbus_discoverComponentDataElements
 * Description   : This function will invoke the rbus api rbus_discoverComponentDataElements which enables a component
                 : to get a list of all data elements provided by a component.
 * @param [in]   : component_name - Name of the Component
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
 int ssp_rbus_discoverComponentDataElements(char* component_name) {

    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_discoverComponentDataElements wrapper\n");

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;
    int numElements = 0;
    char** elementNames = NULL;
    int i;

    ret =  rbus_discoverComponentDataElements(bus_handle,component_name,false,&numElements,&elementNames);
    if(RBUS_ERROR_SUCCESS == ret)
    {
        DEBUG_PRINT(DEBUG_ERROR, "Discovered elements are,\n");
        for(i=0;i<numElements;i++)
        {
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_discoverComponentDataElements %d: %s\n", i,elementNames[i]);
            free(elementNames[i]);
        }
        free(elementNames);
        result = RETURN_OK;
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "Failed to discover element array. Error Code = %s\n", "");
        result = RETURN_ERR;
    }

    DEBUG_PRINT(DEBUG_ERROR, "Exit from ssp_rbus_discoverComponentDataElements wrapper\n");
    return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_rbus_get
 * Description   : This function will invoke the rbus api rbus_get which returns rbusValue_t structure value
 * @param [in]   : parameter_name - Parameter Name to get values
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_get(char* parameter_name){

    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_get wrapper\n");

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;

    rbusValue_t value;
    ret = rbus_get(bus_handle, parameter_name ,&value);

    if(RBUS_ERROR_SUCCESS != ret)
    {
        DEBUG_PRINT(DEBUG_ERROR, "Failed to get the Data \n");
        result = RETURN_ERR;
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "rbus_get function was success \n");
        result = RETURN_OK;
    }

    DEBUG_PRINT(DEBUG_ERROR, "rbus_get calling rbusValue_Release function to release the structure value \n");
    rbusValue_Release(value);

    DEBUG_PRINT(DEBUG_ERROR, "Exit from ssp_rbus_get wrapper\n");
    return result;
}


/*****************************************************************************************************************
 * Function Name : ssp_rbus_getValue
 * Description   : This function will invoke the RBUS APIs to get Boolean, string, Interger or UnsignedInt parameter values
 * @param [in]   : parameter_name - Parameter Name to get values
                 : parameter_type - Boolean , String, Integer or UnsignedInt
                 : getvalue - TO Store the Parameter value
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_getValue(char* parameter_type,char* parameter_name, const char** getvalue, int** getvalue_i) {

    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_getValue wrapper\n");
    DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_getValue calling for Method %s with Parameter %s \n", parameter_type, parameter_name);

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;
    rbusValue_t value;

    ret = rbus_get(bus_handle, parameter_name ,&value);

    if(ret == RBUS_ERROR_SUCCESS)
    {
        if (strcmp(parameter_type,"Boolean") == 0)
        {
            if (rbusValue_GetBoolean(value))
                *getvalue = "true";
            else
                *getvalue = "false";

            if (getvalue != NULL)
            {
                DEBUG_PRINT(DEBUG_ERROR, "Value Received on Boolean is %s",*getvalue);
                result = RETURN_OK;
            }
            else
            {
                DEBUG_PRINT(DEBUG_ERROR, "Value Received is NULL");
                result = RETURN_ERR;
            }
        }
        else if (strcmp(parameter_type,"String") == 0)
        {
            *getvalue = rbusValue_GetString(value, NULL);
            if (getvalue != NULL)
            {
                DEBUG_PRINT(DEBUG_ERROR, "Value Received on String is %s",*getvalue);
                result = RETURN_OK;
            }
            else
            {
                DEBUG_PRINT(DEBUG_ERROR, "Value Received is NULL");
                result = RETURN_ERR;
            }
        }
        else if (strcmp(parameter_type, "Integer") == 0)
        {
            *getvalue_i = rbusValue_GetInt32(value);

            if (getvalue_i != NULL)
            {
                DEBUG_PRINT(DEBUG_ERROR, "Value Received on Integer is %d",*getvalue_i);
                result = RETURN_OK;
            }
            else
            {
                DEBUG_PRINT(DEBUG_ERROR, "Value Received is NULL");
                result = RETURN_ERR;
            }
        }
        else if (strcmp(parameter_type, "UnsignedInt") == 0)
        {
            unsigned int getv = 0;
            getv = rbusValue_GetUInt32(value);
            *getvalue_i = (int)getv;

            if (getvalue_i != NULL)
            {
                DEBUG_PRINT(DEBUG_ERROR, "Value Received on UnsignedInt is %d",*getvalue_i);
                result = RETURN_OK;
            }
            else
            {
                DEBUG_PRINT(DEBUG_ERROR, "Value Received is NULL");
                result = RETURN_ERR;
            }
        }
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "Failed to get the Data\n");
        result = RETURN_ERR;
    }

    DEBUG_PRINT(DEBUG_ERROR, "Exit from ssp_rbus_getValue wrapper\n");
    return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_rbus_setValue
 * Description   : This function will invoke RBUS APIs to Set Boolean, string, Interger or UnsignedInt parameter values
 * @param [in]   : parameter_name - Parameter Name to get values
                 : parameter_type - Boolean , String, Integer or UnsignedInt
                 : set_value - The value to be set
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_setValue(char* parameter_type,char* param_name, char* set_value) {

    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_setValue wrapper\n");
    DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_setValue calling for Method %s with Parameter %s and Value %s\n", parameter_type, param_name,set_value);

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;
    rbusValue_t value;

    DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_setValue calling rbusValue_Init to initialize rbus structure value");
    rbusValue_Init(&value);

    if (strcmp(parameter_type,"Boolean") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_setValue calling rbusValue_SetBoolean with value %s", set_value);
        rbusValue_SetBoolean(value, (bool)set_value);
    }
    else if (strcmp(parameter_type,"String") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_setValue calling rbusValue_SetString with value %s", set_value);
        rbusValue_SetString(value, (char const*)set_value);
    }
    else if (strcmp(parameter_type, "Integer") == 0)
    {
        int set_value1 = 0;
        set_value1 = atoi(set_value);

        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_setValue calling rbusValue_SetInt32 with value %d", set_value1);
        rbusValue_SetInt32(value, set_value1);
    }
    else if (strcmp(parameter_type, "UnsignedInt") == 0)
    {
        unsigned int set_value1 = 0;
        set_value1 = atoi(set_value);

        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_setValue calling rbusValue_SetUInt32 with value %d", set_value1);
        rbusValue_SetUInt32(value, set_value1);
    }

    ret = rbus_set(bus_handle, param_name, value, NULL);

    if (ret == RBUS_ERROR_SUCCESS)
    {
        DEBUG_PRINT(DEBUG_ERROR, "rbus_set success for [%s] with error [%d]\n", param_name, ret);
        result = RETURN_OK;
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "rbus_set Failed for [%s] with error [%d]\n", param_name, ret);
        result = RETURN_ERR;
    }

    DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_setValue calling rbusValue_Release to release the structure value");
    rbusValue_Release(value);

    DEBUG_PRINT(DEBUG_ERROR, "Exit from ssp_rbus_setValue wrapper\n");
    return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_rbus_registerOperation
 * Description   : This function will invoke the different RBUS Register operations
 * @param [in]   : Operation : Operation to be Performed
                 : object_name : Name of the object / Component name
                 : method_name : Method Name
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_registerOperation(char* operation, char* object_name,char* method_name)
{
    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_registerOperation wrapper\n");

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;
    char object_buffer[DEFAULT_BUFFERSIZE] = {'\0'};;
    char method_buffer[DEFAULT_BUFFERSIZE] = {'\0'};;

    DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_registerOperation - Operation is %s object_name is %s method_name is %s \n",operation,object_name,method_name);

    if (strcmp(operation,"openBrokerConnection") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_registerOperation --> openBrokerConnection Invoked...! \n");
        //Object_name parameter carries value for Component name
        //method_name parameter carries value for deciding the connection to close before open
        if (strcmp(method_name,"CloseConnectionBeforeOpen") == 0)
        {
            rbus_closeBrokerConnection(); // Closing the Broker Connection to avoid duplicate connection
        }

        char component_name[DEFAULT_BUFFERSIZE] = {'\0'};;
        memset(component_name, 0, DEFAULT_BUFFERSIZE );
        snprintf(component_name, (sizeof(component_name) - 1), "%s", object_name);

        ret = rbus_openBrokerConnection(component_name);

        DEBUG_PRINT(DEBUG_ERROR, "openBrokerConnection Return value is %d \n",ret);
    }
    else if (strcmp(operation,"closeBrokerConnection") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_registerOperation --> closeBrokerConnection Invoked...! \n");

        ret = rbus_closeBrokerConnection();

        DEBUG_PRINT(DEBUG_ERROR, "closeBrokerConnection Return value is %d \n",ret);
    }
    else if (strcmp(operation,"registerObj") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_registerOperation --> registerObj Invoked...! \n");

        memset( object_buffer, 0, DEFAULT_BUFFERSIZE );
        snprintf(object_buffer, (sizeof(object_buffer) - 1), "%s", object_name);

	ret = rbus_registerObj(object_buffer, NULL, NULL);

        DEBUG_PRINT(DEBUG_ERROR, "registerObj Return value is %d \n",ret);
    }
    else if (strcmp(operation,"unregisterObj") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_registerOperation --> unregisterObj Invoked...! \n");

        ret = rbus_unregisterObj(object_name);

        DEBUG_PRINT(DEBUG_ERROR, "rbus_unregisterObj Return value is %d \n",ret);
    }
    else if (strcmp(operation,"registerMethod") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_registerOperation --> registerMethod Invoked...! \n");

        memset(object_buffer, 0, DEFAULT_BUFFERSIZE );
        snprintf(object_buffer, (sizeof(object_buffer) - 1), "%s", object_name);
        memset(method_buffer, 0, DEFAULT_BUFFERSIZE );
        snprintf(method_buffer, (sizeof(method_buffer) - 1), "%s", method_name);

        ret = rbus_registerMethod(object_name, method_buffer, NULL, NULL);

        DEBUG_PRINT(DEBUG_ERROR, "registerMethod Return value is %d \n",ret);
    }
    else if (strcmp(operation,"unregisterMethod") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_registerOperation --> unregisterMethod Invoked...! \n");

        ret = rbus_unregisterMethod(object_name, method_name);

        DEBUG_PRINT(DEBUG_ERROR, "unregisterMethod Return value is %d \n",ret);
    }
    else if (strcmp(operation,"registerEvent") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_registerOperation --> registerEvent Invoked...! \n");
        char data[] = "data";

        ret = rbus_registerEvent(object_name,method_name,NULL,data); // Methodname parameter holds value for Event Name

        DEBUG_PRINT(DEBUG_ERROR, "registerEvent Return value is %d \n",ret);
    }
    else if (strcmp(operation,"unregisterEvent") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_registerOperation --> unregisterEvent Invoked...! \n");

        ret = rbus_unregisterEvent(object_name,method_name); // Methodname parameter holds value for Event Name

        DEBUG_PRINT(DEBUG_ERROR, "unregisterEvent Return value is %d \n",ret);
    }
    else if (strcmp(operation,"addElement") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_registerOperation --> addElement Invoked...! \n");

        memset( method_buffer, 0, DEFAULT_BUFFERSIZE);
        snprintf(method_buffer, (sizeof(method_buffer) - 1), "%s", method_name);  // Method_name parameter holds value for Element Name
        ret =  rbus_addElement(object_name, method_buffer);

        DEBUG_PRINT(DEBUG_ERROR, "addElement Return value is %d \n",ret);
    }
    else if (strcmp(operation,"removeElement") == 0)
    {
        DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_registerOperation --> removeElement Invoked...! \n");

        memset( method_buffer, 0, DEFAULT_BUFFERSIZE);
        snprintf(method_buffer, (sizeof(method_buffer) - 1), "%s", method_name);  // Method_name parameter holds value for Element Name
        ret =  rbus_removeElement(object_name, method_buffer);

        DEBUG_PRINT(DEBUG_ERROR, "removeElement Return value is %d \n",ret);
    }
    if(ret != RBUS_ERROR_SUCCESS)
    {
        DEBUG_PRINT(DEBUG_ERROR, "%s failed with error code %d \n", operation,ret);
        result = RETURN_ERR;
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "%s was successful, return value is %d \n",operation,ret);
        result = RETURN_OK;
    }

    return result;
}
