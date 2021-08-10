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
#include "json_hal_logger.h"
#include "jsonhal_wrp.h"
#include "jsonhal_lib_wrp.h"
#include "json_schema_validator_wrapper.h"

int voice_process_get_info(hal_param_t *get_param);
int get_voice_line_stats(json_object *reply_msg, TELCOVOICEMGR_DML_VOICESERVICE_STATS *stVoiceStats);
int Map_hal_dml_capabilities(PTELCOVOICEMGR_DML_CAPABILITIES pCapabilities, char* ParamName, char* pValue);
int Map_hal_dml_voiceProfile(DML_PROFILE_LIST_T* pVoiceProfileList, char* ParamName, char* pValue);
int Map_hal_dml_phyInterface(DML_PHYINTERFACE_LIST_T* pPhyInterfaceList, char* ParamName, char* pValue);
int telcovoicemgr_hal_get_second_index(char* ParamName, char* Pattern,  int* hal_index);
int telcovoicemgr_hal_get_first_index(char* ParamName, char* Pattern, int* hal_index);

/*****************************************************************************************************************
 * Function Name : telcovoicemgrhal_initdata
 * Description   : This function will invoke the telco voice manager API to get the init data according to the bStatus
 * @param [in]   : bStatus - 0 or 1
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int telcovoicemgrhal_initdata(int bStatus)
{
    int rc = RETURN_OK;
    char strValue[JSON_MAX_VAL_ARR_SIZE]={0};
    char strName[JSON_MAX_STR_ARR_SIZE]={0};

    snprintf(strName,JSON_MAX_STR_ARR_SIZE, "%s", HALINIT);
    if(bStatus)
    {
       snprintf(strValue,JSON_MAX_VAL_ARR_SIZE,"%s","true");
    }
    else
    {
        snprintf(strValue,JSON_MAX_VAL_ARR_SIZE,"%s","false");
    }
    if (jsonhal_setparam(strName,PARAM_BOOLEAN,strValue) != rc)
    {
       return RETURN_ERR;
    }
    return rc;
}

/*****************************************************************************************************************
 * Function Name : telcovoicemgrhal_getlinestats
 * Description   : This function will invoke the telco voice manager line stats API to get the details of line statistics
 * @param [in]   : param_name, pLineStats : to retrieve the line statistics info
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int telcovoicemgrhal_getlinestats(char *param_name, TELCOVOICEMGR_DML_VOICESERVICE_STATS *pLineStats)
{
    CHECK(param_name != NULL);
    CHECK(pLineStats != NULL);

    int rc = RETURN_OK;

    json_object *jreply_msg = NULL;
    json_object *jrequest = create_json_request_message(GET_REQUEST_MESSAGE, param_name, NULL_TYPE , NULL);
    CHECK(jrequest != NULL);

    if (json_hal_client_send_and_get_reply(jrequest, &jreply_msg) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get reply for the json request \n", __FUNCTION__, __LINE__);
        FREE_JSON_OBJECT(jrequest);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }

    rc = get_voice_line_stats(jreply_msg, pLineStats);
    if (rc != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get statistics data  \n", __FUNCTION__, __LINE__);
    }

    // Free json objects.
    FREE_JSON_OBJECT(jrequest);
    FREE_JSON_OBJECT(jreply_msg);
    return rc;
}

/*****************************************************************************************************************
 * Function Name : voice_process_get_info
 * Description   : This function will retrieve the voice process info
 * @param [in]   : get_param
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int voice_process_get_info(hal_param_t *get_param)
{
    CHECK(get_param != NULL);

    json_object *jreply_msg;
    json_object *jrequest;
    hal_param_t resp_param;
    int rc = RETURN_ERR;

    jrequest = create_json_request_message(GET_REQUEST_MESSAGE, get_param->name, NULL_TYPE , NULL);
    CHECK(jrequest != NULL);

    DEBUG_PRINT(DEBUG_TRACE,"%s - %d Json request message = %s \n", __FUNCTION__, __LINE__, json_object_to_json_string_ext(jrequest, JSON_C_TO_STRING_PRETTY));

    if (json_hal_client_send_and_get_reply(jrequest, &jreply_msg) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get reply for the json request \n", __FUNCTION__, __LINE__);
        FREE_JSON_OBJECT(jrequest);
        FREE_JSON_OBJECT(jreply_msg);
        return rc;
    }

    CHECK(jreply_msg != NULL);
    DEBUG_PRINT(DEBUG_TRACE,"Got Json response \n = %s \n", json_object_to_json_string_ext(jreply_msg, JSON_C_TO_STRING_PRETTY));

    if (json_hal_get_param(jreply_msg, JSON_RPC_PARAM_ARR_INDEX, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get required params from the response message \n", __FUNCTION__, __LINE__);
        return rc;
    }

    strncpy(get_param->value, resp_param.value, sizeof(resp_param.value));

    // Free json objects.
    FREE_JSON_OBJECT(jrequest);
    FREE_JSON_OBJECT(jreply_msg);
    return RETURN_OK;
}

/*****************************************************************************************************************
 * Function Name : get_voice_line_stats
 * Description   : This function will retrieve the voice line statistics
 * @param [in]   : stVoiceStats - structure to retrieve the Voice statistics
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int get_voice_line_stats(json_object *reply_msg, TELCOVOICEMGR_DML_VOICESERVICE_STATS *stVoiceStats)
{
    int rc = RETURN_OK;
    int total_param_count = 0;

    total_param_count = json_hal_get_total_param_count(reply_msg);
    hal_param_t resp_param;

    /**
     * Traverse through each index and retrieve value.
     */
    for (int i = 0; i < total_param_count; ++i)
    {
        if (json_hal_get_param(reply_msg, i, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get the param from response message [index = %d] \n", __FUNCTION__, __LINE__, i);
            continue;
        }
        if( strstr(resp_param.name, "AverageFarEndInterarrivalJitter") )
        {
            stVoiceStats->AverageFarEndInterarrivalJitter = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "AverageReceiveInterarrivalJitter") )
        {
            stVoiceStats->AverageReceiveInterarrivalJitter = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "AverageRoundTripDelay") )
        {
            stVoiceStats->AverageRoundTripDelay = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "BytesReceived") )
        {
            stVoiceStats->BytesReceived = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "BytesSent") )
        {
            stVoiceStats->BytesSent = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "FarEndInterarrivalJitter") )
        {
            stVoiceStats->FarEndInterarrivalJitter = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "FarEndPacketLossRate") )
        {
            stVoiceStats->FarEndPacketLossRate = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "IncomingCallsAnswered") )
        {
            stVoiceStats->IncomingCallsAnswered= atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "IncomingCallsConnected") )
        {
            stVoiceStats->IncomingCallsConnected = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "IncomingCallsFailed") )
        {
            stVoiceStats->IncomingCallsFailed = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "IncomingCallsReceived") )
        {
            stVoiceStats->IncomingCallsReceived= atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "OutgoingCallsAnswered") )
        {
            stVoiceStats->OutgoingCallsAnswered = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "OutgoingCallsAttempted") )
        {
            stVoiceStats->OutgoingCallsAttempted = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "OutgoingCallsConnected") )
        {
            stVoiceStats->OutgoingCallsConnected = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "OutgoingCallsFailed") )
        {
            stVoiceStats->OutgoingCallsFailed = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "PacketsLost") )
        {
            stVoiceStats->PacketsLost = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "PacketsReceived") )
        {
            stVoiceStats->PacketsReceived = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "PacketsSent") )
        {
            stVoiceStats->PacketsSent = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "ReceiveInterarrivalJitter") )
        {
            stVoiceStats->ReceiveInterarrivalJitter = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "ReceivePacketLossRate") )
        {
            stVoiceStats->ReceivePacketLossRate = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "RoundTripDelay") )
        {
            stVoiceStats->RoundTripDelay = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "Overruns") )
        {
            stVoiceStats->Overruns = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "Underruns") )
        {
            stVoiceStats->Underruns = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "CallsDropped") )
        {
            stVoiceStats->CallsDropped = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "TotalCallTime") )
        {
            stVoiceStats->TotalCallTime = atol(resp_param.value);
        }
        else if( strstr(resp_param.name, "ServerDownTime") )
        {
            stVoiceStats->ServerDownTime = atol(resp_param.value);
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE, "%s::Unknown ParamName:%s\n", __FUNCTION__, resp_param.name);
        }
    }

    return rc;
}

/*****************************************************************************************************************
 * Function Name : telcovoicemgrhal_getcapabilities
 * Description   : This function will invoke the telco voice manager capabilities API
 * @param [in]   : pCapabilities : to retrieve the capabilities info
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/

int telcovoicemgrhal_getcapabilities(PTELCOVOICEMGR_DML_CAPABILITIES pCapabilities, char *param_name)
{
    CHECK(param_name != NULL);
    int rc = RETURN_OK;

    if (pCapabilities == NULL)
    {
        DEBUG_PRINT(DEBUG_TRACE, "%s - %d Invalid argument \n", __FUNCTION__, __LINE__);
        return RETURN_ERR;
    }

    int total_param_count = 0;
    hal_param_t resp_param;
    json_object *jreply_msg = NULL;
    memset(&resp_param, 0, sizeof(resp_param));

    json_object *jrequest = create_json_request_message(GET_REQUEST_MESSAGE, param_name, NULL_TYPE , NULL);

    CHECK(jrequest != NULL);

    if (json_hal_client_send_and_get_reply(jrequest, &jreply_msg) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE, "%s - %d Failed to get reply for the json request \n", __FUNCTION__, __LINE__);
        // Free json objects.
        FREE_JSON_OBJECT(jrequest);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }

    total_param_count = json_hal_get_total_param_count(jreply_msg);

    for (int i = 0; i < total_param_count; ++i)
    {
        if (json_hal_get_param(jreply_msg, i, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_TRACE, "%s - %d Failed to get the param from response message [index = %d] \n", __FUNCTION__, __LINE__, i);
            continue;
        }
        rc = Map_hal_dml_capabilities(pCapabilities,resp_param.name,resp_param.value);
    }
    if (rc != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE, "%s - %d Failed to get data  \n", __FUNCTION__, __LINE__);
    }

    // Free json objects.
    FREE_JSON_OBJECT(jrequest);
    FREE_JSON_OBJECT(jreply_msg);
    return rc;
}

/*****************************************************************************************************************
 * Function Name : telcovoicemgrhal_getphyinterface
 * Description   : This function will invoke the telco voice manager physical interface API
 * @param [in]   : index, pPhyInterfaceList : to retrieve the physical interface info
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int telcovoicemgrhal_getphyinterface(DML_PHYINTERFACE_LIST_T* pPhyInterfaceList, int vsIndex, char *param_name)
{
    int rc = RETURN_OK;
    int total_param_count = 0;
    char paramName[JSON_MAX_STR_ARR_SIZE] = { 0 };

    hal_param_t resp_param;
    json_object *jreply_msg = NULL;
    memset(&resp_param, 0, sizeof(resp_param));

    if ((pPhyInterfaceList == NULL) || (vsIndex <=0))
    {
        DEBUG_PRINT(DEBUG_TRACE, "%s - %d Invalid argument \n", __FUNCTION__, __LINE__);
        return RETURN_ERR;
    }

    snprintf(paramName, JSON_MAX_STR_ARR_SIZE, param_name, vsIndex);
    json_object *jrequest = create_json_request_message(GET_REQUEST_MESSAGE, paramName, NULL_TYPE , NULL);

    CHECK(jrequest != NULL);

    if (json_hal_client_send_and_get_reply(jrequest, &jreply_msg) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE, "%s - %d Failed to get reply for the json request \n", __FUNCTION__, __LINE__);
        // Free json objects.
        FREE_JSON_OBJECT(jrequest);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }

    //check all messages
    total_param_count = json_hal_get_total_param_count(jreply_msg);

    for (int i = 0; i < total_param_count; ++i)
    {
        if (json_hal_get_param(jreply_msg, i, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_TRACE, "%s - %d Failed to get the param from response message [index = %d] \n", __FUNCTION__, __LINE__, i);
            continue;
        }
        rc = Map_hal_dml_phyInterface(pPhyInterfaceList, resp_param.name, resp_param.value);
    }

    if (rc != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE, "%s - %d Failed to get data  \n", __FUNCTION__, __LINE__);
    }
    // Free json objects.
    FREE_JSON_OBJECT(jrequest);
    FREE_JSON_OBJECT(jreply_msg);

    return rc;
}

/*****************************************************************************************************************
 * Function Name : telcovoicemgrhal_getvoiceprofile
 * Description   : This function will get the voice profile details for the given index
 * @param [in]   : index, pVoiceProfileList : buffer to retrieve the voice profile info
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int telcovoicemgrhal_getvoiceprofile(DML_PROFILE_LIST_T* pVoiceProfileList, int vsIndex, char *param_name)
{
    int rc = RETURN_OK;
    int total_param_count = 0;
    hal_param_t resp_param;
    char paramName[JSON_MAX_STR_ARR_SIZE] = { 0 };

    json_object *jreply_msg = NULL;
    memset(&resp_param, 0, sizeof(resp_param));

    if ((pVoiceProfileList == NULL ) || (vsIndex <=0))
    {
        fprintf(stderr,"%s - %d Invalid argument \n", __FUNCTION__, __LINE__);
        return RETURN_ERR;
    }

    snprintf(paramName, JSON_MAX_STR_ARR_SIZE, param_name, vsIndex);
    json_object *jrequest = create_json_request_message(GET_REQUEST_MESSAGE, paramName, NULL_TYPE , NULL);

    CHECK(jrequest != NULL);

    if (json_hal_client_send_and_get_reply(jrequest, &jreply_msg) != RETURN_OK)
    {
        fprintf(stderr,"%s - %d Failed to get reply for the json request \n", __FUNCTION__, __LINE__);
        // Free json objects.
        FREE_JSON_OBJECT(jrequest);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }
    total_param_count = json_hal_get_total_param_count(jreply_msg);


    for (int i = 0; i < total_param_count; ++i)
    {
        if (json_hal_get_param(jreply_msg, i, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
        {
            fprintf(stderr,"%s - %d Failed to get the param from response message [index = %d] \n", __FUNCTION__, __LINE__, i);
            continue;
        }
        rc = Map_hal_dml_voiceProfile(pVoiceProfileList, resp_param.name, resp_param.value);
    }
    if (rc != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE, "%s - %d Failed to get data  \n", __FUNCTION__, __LINE__);
    }
    // Free json objects.
    FREE_JSON_OBJECT(jrequest);
    FREE_JSON_OBJECT(jreply_msg);

    return rc;
}


/*****************************************************************************************************************
 * Function Name : telcovoicemgr_hal_get_first_index
 * Description   : This function will voice service index
 * @param [in]   : ParamName, Pattern, buffer to fetch the hal_index
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int telcovoicemgr_hal_get_first_index(char* ParamName, char* Pattern, int* hal_index)
{
    if(sscanf(ParamName, Pattern, hal_index) != FIRST_INDEX)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n%s:%d:: \nInvalid index ParamName[%s]\nPattern[%s]\n", __FUNCTION__, __LINE__, ParamName,Pattern);
        return RETURN_ERR;
    }
    if( *hal_index <= 0 )
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n%s:%d:: \nInvalid index ParamName[%s]\nPattern[%s]\n", __FUNCTION__, __LINE__, ParamName,Pattern);
        return RETURN_ERR;
    }
    return RETURN_OK;
}

/*****************************************************************************************************************
 * Function Name : telcovoicemgr_hal_get_second_index
 * Description   : This function will physical interface index
 * @param [in]   : ParamName, Pattern, buffer to fetch the hal_index
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int telcovoicemgr_hal_get_second_index(char* ParamName, char* Pattern,  int* hal_index)
{
    int tmp_index1;
    if(sscanf(ParamName, Pattern, &tmp_index1, hal_index) != SECOND_INDEX)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n%s:%d:: \nInvalid index ParamName[%s]\nPattern[%s]\n", __FUNCTION__, __LINE__, ParamName,Pattern);
        return RETURN_ERR;
    }
    if( *hal_index <= 0 || tmp_index1 <= 0 )
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n%s:%d:: \nInvalid index ParamName[%s]\nPattern[%s]\n", __FUNCTION__, __LINE__, ParamName,Pattern);
        return RETURN_ERR;
    }
    return RETURN_OK;
}

/*****************************************************************************************************************
 * Function Name : Map_hal_dml_phyInterface
 * Description   : This function will retrieve the structure parameters of Physical Interface
 * @param [in]   : ParamName, pValue, buffer to fetch the Physical Interface details : pPhyInterfaceList
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int Map_hal_dml_phyInterface(DML_PHYINTERFACE_LIST_T* pPhyInterfaceList, char* ParamName, char* pValue)
{
    int uVsIndex = 0;
    int uPhyIndex = 0;
    char *err;

    if(RETURN_ERR == telcovoicemgr_hal_get_voiceService_index(ParamName, DML_VOICESERVICE, &uVsIndex))
    {
        return RETURN_ERR;
    }
    if(RETURN_ERR == telcovoicemgr_hal_get_phyInterface_index(ParamName, DML_VOICESERVICE_PHYIFACE, &uPhyIndex))
    {
        return RETURN_ERR;
    }

    if( uVsIndex <= 0  || uPhyIndex <= 0 )
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s:%d:: Invalid index ParamName[%s]\n", __FUNCTION__, __LINE__, ParamName);
        return RETURN_ERR;
    }
    DML_PHYINTERFACE_CTRL_T* pPhyInterfaceData = pPhyInterfaceList->pdata[uPhyIndex - 1];

    TELCOVOICEMGR_DML_PHYINTERFACE* pPhyInterface = &(pPhyInterfaceData->dml);
    if(pPhyInterface)
    {
        pPhyInterface->InstanceNumber = uPhyIndex;

        if( strstr(ParamName, "PhyPort"))
        {
            strncpy(pPhyInterface->PhyPort, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "InterfaceID"))
        {
            pPhyInterface->InterfaceID = strtoul(pValue,&err,10);
        }
        else if( strstr(ParamName, "Description"))
        {
            strncpy(pPhyInterface->Description, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "Tests"))
        {
            //VoiceService.{i}.PhyInterface.{i}.Tests.
            PTELCOVOICEMGR_DML_PHYINTERFACE_TESTS pPhyInterface_Tests= &(pPhyInterface->PhyInterfaceTestsObj);

            if( strstr(ParamName, "TestState"))
            {
                if(strstr(pValue, "None"))
                {
                    pPhyInterface_Tests->TestState = PHYINTERFACE_TESTSTATE_NONE;
                }
                else if(strstr(pValue, "Requested"))
                {
                    pPhyInterface_Tests->TestState = PHYINTERFACE_TESTSTATE_REQUESTED;
                }
                else if(strstr(pValue, "Complete"))
                {
                    pPhyInterface_Tests->TestState = PHYINTERFACE_TESTSTATE_COMPLETE;
                }
                else if(strstr(pValue, "Error_TestNotSupported"))
                {
                    pPhyInterface_Tests->TestState = PHYINTERFACE_TESTSTATE_ERROR_TESTNOTSUPPORTED;
                }
            }
            else if( strstr(ParamName, "TestSelector"))
            {
                if(strstr(pValue, "PhoneConnectivityTest"))
                {
                    pPhyInterface_Tests->TestSelector = PHYINTERFACE_TESTSELECTOR_PHONE_CONNECTIVITY_TEST;
                }
                else if(strstr(pValue, "Hazard Potential"))
                {
                    pPhyInterface_Tests->TestSelector = PHYINTERFACE_TESTSELECTOR_HAZARD_POTENTIAL;
                }
                else if(strstr(pValue, "Foreign Voltage"))
                {
                    pPhyInterface_Tests->TestSelector = PHYINTERFACE_TESTSELECTOR_FOREIGN_VOLTAGE;
                }
                else if(strstr(pValue, "Resistive Faults"))
                {
                    pPhyInterface_Tests->TestSelector = PHYINTERFACE_TESTSELECTOR_RESISTIVE_FAULTS;
                }
                else if(strstr(pValue, "Off-hook"))
                {
                    pPhyInterface_Tests->TestSelector = PHYINTERFACE_TESTSELECTOR_OFF_HOOK;
                }
                else if(strstr(pValue, "REN"))
                {
                    pPhyInterface_Tests->TestSelector = PHYINTERFACE_TESTSELECTOR_REN;
                }
            }
            else if( strstr(ParamName, "X_RDK_TestResult"))
            {
                strncpy(pPhyInterface_Tests->X_RDK_TestResult, pValue,strlen(pValue)+1);
            }
            else
            {
                DEBUG_PRINT(DEBUG_TRACE,"%s:%d:: Invalid ParamName[%s] paramValue[%s].\n", __FUNCTION__, __LINE__, ParamName, pValue);
            }
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s:%d:: Invalid ParamName[%s] paramValue[%s].\n", __FUNCTION__, __LINE__, ParamName, pValue);
        }
    }
    return RETURN_OK;
}


/*****************************************************************************************************************
 * Function Name : Map_hal_dml_voiceProfile
 * Description   : This function will retrieve the structure parameters of voice profile
 * @param [in]   : ParamName, pValue, buffer to fetch the voice profile details : pVoiceProfileList
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int Map_hal_dml_voiceProfile(DML_PROFILE_LIST_T* pVoiceProfileList, char* ParamName, char* pValue)
{
    char *err;
    int uVsIndex = 0;
    int uVpIndex = 0;

    if(RETURN_ERR == telcovoicemgr_hal_get_voiceService_index(ParamName, DML_VOICESERVICE, &uVsIndex))
    {
        return RETURN_ERR;
    }
    if(RETURN_ERR == telcovoicemgr_hal_get_voiceProfile_index(ParamName, DML_VOICESERVICE_VOICEPROF, &uVpIndex))
    {
        return RETURN_ERR;
    }
    if( uVsIndex <= 0  || uVpIndex <= 0 )
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n%s:%d:: \nInvalid index ParamName[%s]", __FUNCTION__, __LINE__, ParamName);
        return RETURN_ERR;
    }
    DML_PROFILE_CTRL_T* pVoiceProfile = pVoiceProfileList->pdata[uVpIndex - 1];

    TELCOVOICEMGR_DML_VOICEPROFILE* pVoiceProf = &(pVoiceProfile->dml);
    if (pVoiceProf)
    {
        if( strstr(ParamName, "SIP"))
        {
            //VoiceService.{i}.VoiceProfile.{i}.SIP.
            PTELCOVOICEMGR_DML_SIP pVoiceProf_SIP = &(pVoiceProf->SIPObj);
            if( strstr(ParamName, "ProxyServerPort"))
            {
                pVoiceProf_SIP->ProxyServerPort = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "ProxyServerTransport"))
            {
                strncpy(pVoiceProf_SIP->ProxyServerTransport, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "ProxyServer"))
            {
                strncpy(pVoiceProf_SIP->ProxyServer, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "RegistrarServerPort"))
            {
                pVoiceProf_SIP->RegistrarServerPort = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "RegistrarServerTransport"))
            {
                strncpy(pVoiceProf_SIP->RegistrarServerTransport, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "RegistrarServer"))
            {
                strncpy(pVoiceProf_SIP->RegistrarServer, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "UserAgentDomain"))
            {
                strncpy(pVoiceProf_SIP->UserAgentDomain, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "UserAgentPort"))
            {
                pVoiceProf_SIP->UserAgentPort = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "UserAgentTransport"))
            {
                strncpy(pVoiceProf_SIP->UserAgentTransport, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "OutboundProxyPort"))
            {
                pVoiceProf_SIP->OutboundProxyPort = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "OutboundProxy"))
            {
                strncpy(pVoiceProf_SIP->OutboundProxy, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "Organization"))
            {
                strncpy(pVoiceProf_SIP->Organization, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "RegistrationPeriod"))
            {
                pVoiceProf_SIP->RegistrationPeriod = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerT1"))
            {
                pVoiceProf_SIP->TimerT1 = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerT2"))
            {
                pVoiceProf_SIP->TimerT2 = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerT4"))
            {
                pVoiceProf_SIP->TimerT4 = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerA"))
            {
                pVoiceProf_SIP->TimerA = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerB"))
            {
                pVoiceProf_SIP->TimerB = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerC"))
            {
                pVoiceProf_SIP->TimerC = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerD"))
            {
                pVoiceProf_SIP->TimerD = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerE"))
            {
                pVoiceProf_SIP->TimerE = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerF"))
            {
                pVoiceProf_SIP->TimerF = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerG"))
            {
                pVoiceProf_SIP->TimerG = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerH"))
            {
                pVoiceProf_SIP->TimerH = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerI"))
            {
                pVoiceProf_SIP->TimerI = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerJ"))
            {
                pVoiceProf_SIP->TimerJ = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TimerK"))
            {
                pVoiceProf_SIP->TimerK = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "InviteExpires"))
            {
                pVoiceProf_SIP->InviteExpires = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "ReInviteExpires"))
            {
                pVoiceProf_SIP->ReInviteExpires = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "RegisterExpires"))
            {
                pVoiceProf_SIP->RegisterExpires = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "RegistersMinExpires"))
            {
                pVoiceProf_SIP->RegistersMinExpires = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "InboundAuthUsername"))
            {
                strncpy(pVoiceProf_SIP->InboundAuthUsername, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "InboundAuthPassword"))
            {
                strncpy(pVoiceProf_SIP->InboundAuthPassword, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "InboundAuth"))
            {
                if(strstr(pValue, "None"))
                {
                    pVoiceProf_SIP->InboundAuth = SIP_INBOUNDAUTH_NONE;
                }
                else if(strstr(pValue, "Digest"))
                {
                    pVoiceProf_SIP->InboundAuth = SIP_INBOUNDAUTH_DIGEST;
                }
            }
            else if( strstr(ParamName, "DSCPMark"))
            {
                pVoiceProf_SIP->DSCPMark = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "VLANIDMark"))
            {
                pVoiceProf_SIP->VLANIDMark = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "EthernetPriorityMark"))
            {
                pVoiceProf_SIP->EthernetPriorityMark = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "X_RDK_Firewall_Rule_Data"))
            {
                strncpy(pVoiceProf_SIP->X_RDK_Firewall_Rule_Data, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "X_RDK_SKBMark"))
            {
                pVoiceProf_SIP->X_RDK_SKBMark = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "X_RDK-Central_COM_ConferencingURI"))
            {
                strncpy(pVoiceProf_SIP->ConferencingURI, pValue,strlen(pValue)+1);
            }
        }  // END_OF_SIP
        else if( strstr(ParamName, "MGCP"))
        {
            //VoiceService.{i}.VoiceProfile.{i}.MGCP.
            TELCOVOICEMGR_DML_MGCP* pVoiceProfile_MGCP = &(pVoiceProf->MGCPObj);
            if( strstr(ParamName, "CallAgent1"))
            {
            strncpy(pVoiceProfile_MGCP->CallAgent1, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "CallAgentPort1"))
            {
                pVoiceProfile_MGCP->CallAgentPort1 = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "CallAgent2"))
            {
            strncpy(pVoiceProfile_MGCP->CallAgent2, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "CallAgentPort2"))
            {
                pVoiceProfile_MGCP->CallAgentPort2 = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "MaxRetranCount"))
            {
                pVoiceProfile_MGCP->MaxRetranCount = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "RegisterMode"))
            {
                if(strstr(pValue, "WildCard"))
                {
                    pVoiceProfile_MGCP->RegisterMode = MGCP_REGISTERMODE_WILDCARD;
                }
                else if(strstr(pValue, "Individual"))
                {
                    pVoiceProfile_MGCP->RegisterMode = MGCP_REGISTERMODE_INDIVIDUAL;
                }
            }
            else if( strstr(ParamName, "LocalPort"))
            {
                pVoiceProfile_MGCP->LocalPort = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "Domain"))
            {
                strncpy(pVoiceProfile_MGCP->Domain, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "User"))
            {
                strncpy(pVoiceProfile_MGCP->User, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "DSCPMark"))
            {
                pVoiceProfile_MGCP->DSCPMark = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "VLANIDMark"))
            {
                pVoiceProfile_MGCP->VLANIDMark = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "EthernetPriorityMark"))
            {
                pVoiceProfile_MGCP->EthernetPriorityMark = strtoul(pValue,&err,10);
            }
            else
            {
                DEBUG_PRINT(DEBUG_TRACE,"%s:%d:: Invalid ParamName[%s] paramValue[%s].\n", __FUNCTION__, __LINE__, ParamName, pValue);
            }
        }
        else if( strstr(ParamName, "H323"))
        {
            //VoiceService.{i}.VoiceProfile.{i}.H323.
            TELCOVOICEMGR_DML_H323* pVoiceProfile_H323 = &(pVoiceProf->H323Obj);
            if( strstr(ParamName, "Gatekeeper"))
            {
                strncpy(pVoiceProfile_H323->Gatekeeper, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "GatekeeperPort"))
            {
                pVoiceProfile_H323->GatekeeperPort = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "GatekeeperID"))
            {
                strncpy(pVoiceProfile_H323->GatekeeperID, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "TimeToLive"))
            {
                pVoiceProfile_H323->TimeToLive = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "AuthPassword"))
            {
            strncpy(pVoiceProfile_H323->AuthPassword, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "SendersID"))
            {
            strncpy(pVoiceProfile_H323->SendersID, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "DSCPMark"))
            {
                pVoiceProfile_H323->DSCPMark = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "VLANIDMark"))
            {
                pVoiceProfile_H323->VLANIDMark = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "EthernetPriorityMark"))
            {
                pVoiceProfile_H323->EthernetPriorityMark = strtoul(pValue,&err,10);
            }
            else
            {
                DEBUG_PRINT(DEBUG_TRACE,"\n%s:%d:: \nInvalid ParamName[%s] \nparamValue[%s].", __FUNCTION__, __LINE__, ParamName, pValue);
            }
        }
        else if( strstr(ParamName, "RTP"))
        {
            //VoiceService.{i}.VoiceProfile.{i}.RTP.
            TELCOVOICEMGR_DML_RTP* pVoiceProfile_RTP = &(pVoiceProf->RTPObj);
            if( strstr(ParamName, "LocalPortMin"))
            {
                pVoiceProfile_RTP->LocalPortMin = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "LocalPortMax"))
            {
                pVoiceProfile_RTP->LocalPortMax = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "DSCPMark"))
            {
                pVoiceProfile_RTP->DSCPMark = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "VLANIDMark"))
            {
                pVoiceProfile_RTP->VLANIDMark = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "EthernetPriorityMark"))
            {
                pVoiceProfile_RTP->EthernetPriorityMark = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TelephoneEventPayloadType"))
            {
                pVoiceProfile_RTP->TelephoneEventPayloadType = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "X_RDK_Firewall_Rule_Data"))
            {
                strncpy(pVoiceProfile_RTP->X_RDK_Firewall_Rule_Data, pValue,strlen(pValue)+1);
            }
            else if( strstr(ParamName, "X_RDK_SKBMark"))
            {
                pVoiceProfile_RTP->X_RDK_SKBMark = strtoul(pValue,&err,10);
            }
        }
        else if( strstr(ParamName, "NumberingPlan"))
        {
            //VoiceService.{i}.VoiceProfile.{i}.NumberingPlan.
            TELCOVOICEMGR_DML_NUMBERINGPLAN* pVoiceProfile_NumberingPlan = &(pVoiceProf->NumberingPlanObj);
            if( strstr(ParamName, "MinimumNumberOfDigits"))
            {
                pVoiceProfile_NumberingPlan->MinimumNumberOfDigits = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "MaximumNumberOfDigits"))
            {
                pVoiceProfile_NumberingPlan->MaximumNumberOfDigits = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "InvalidNumberTone"))
            {
                pVoiceProfile_NumberingPlan->InvalidNumberTone = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "PrefixInfoMaxEntries"))
            {
                pVoiceProfile_NumberingPlan->PrefixInfoMaxEntries = strtoul(pValue,&err,10);
            }
        }
        else if( strstr(ParamName, "FaxT38"))
        {
            //VoiceService.{i}.VoiceProfile.{i}.FaxT38.
            TELCOVOICEMGR_DML_FAXT38* pVoiceProfile_FaxT38 = &(pVoiceProf->Fax38Obj);
            if( strstr(ParamName, "BitRate"))
            {
                pVoiceProfile_FaxT38->BitRate = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "HighSpeedPacketRate"))
            {
                pVoiceProfile_FaxT38->HighSpeedPacketRate = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "HighSpeedRedundancy"))
            {
                pVoiceProfile_FaxT38->HighSpeedRedundancy = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "LowSpeedRedundancy"))
            {
                pVoiceProfile_FaxT38->LowSpeedRedundancy = strtoul(pValue,&err,10);
            }
            else if( strstr(ParamName, "TCFMethod"))
            {
                if(strstr(pValue, "Local"))
                {
                    pVoiceProfile_FaxT38->TCFMethod = TCFMETHOD_LOCAL;
                }
                else if( strstr(ParamName, "Network"))
                {
                    pVoiceProfile_FaxT38->TCFMethod = TCFMETHOD_NETWORK;
                }
            }
            else
            {
                DEBUG_PRINT(DEBUG_TRACE,"%s:%d:: Invalid ParamName[%s] paramValue[%s].\n", __FUNCTION__, __LINE__, ParamName, pValue);
            }
        }
        else if( strstr(ParamName, "NumberOfLines"))
        {
            pVoiceProf->NumberOfLines = strtoul(pValue,&err,10);
        }
        else if( strstr(ParamName, "Name"))
        {
            strncpy(pVoiceProf->Name, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "SignalingProtocol"))
        {
            strncpy(pVoiceProf->SignalingProtocol, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "MaxSessions"))
        {
            pVoiceProf->MaxSessions = strtoul(pValue,&err,10);
        }
        else if( strstr(ParamName, "Region"))
        {
            strncpy(pVoiceProf->Region, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "X_RDK-Central_COM_DigitMap"))
        {
            strncpy(pVoiceProf->X_RDK_DigitMap, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "X_RDK-Central_COM_EmergencyDigitMap"))
        {
            strncpy(pVoiceProf->EmergencyDigitMap, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "X_RDK-Central_COM_SDigitTimer"))
        {
            pVoiceProf->SDigitTimer = strtoul(pValue,&err,10);
        }
        else if( strstr(ParamName, "X_RDK-Central_COM_ZDigitTimer"))
        {
            pVoiceProf->ZDigitTimer = strtoul(pValue,&err,10);
        }
        else if( strstr(ParamName, "STUNServer"))
        {
            strncpy(pVoiceProf->STUNServer, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "NonVoiceBandwidthReservedUpstream"))
        {
            pVoiceProf->NonVoiceBandwidthReservedUpstream = strtoul(pValue,&err,10);
        }
        else if( strstr(ParamName, "NonVoiceBandwidthReservedDownstream"))
        {
            pVoiceProf->NonVoiceBandwidthReservedDownstream = strtoul(pValue,&err,10);
        }
        else if( strstr(ParamName, "FaxPassThrough"))
        {
            if(strstr(pValue, "Disable"))
            {
                pVoiceProf->FaxPassThrough = VOICE_PROFILE_FAXPASSTHROUGH_DISABLE;
            }
            else if(strstr(pValue, "Auto"))
            {
                pVoiceProf->FaxPassThrough = VOICE_PROFILE_FAXPASSTHROUGH_AUTO;
            }
            else if(strstr(pValue, "Force"))
            {
                pVoiceProf->FaxPassThrough = VOICE_PROFILE_FAXPASSTHROUGH_FORCE;
            }
        }
        else if( strstr(ParamName, "ModemPassThrough"))
        {
            if(strstr(pValue, "Disable"))
            {
                pVoiceProf->FaxPassThrough = VOICE_PROFILE_MODEMPASSTHROUGH_DISABLE;
            }
            else if(strstr(pValue, "Auto"))
            {
                pVoiceProf->FaxPassThrough = VOICE_PROFILE_MODEMPASSTHROUGH_AUTO;
            }
            else if(strstr(pValue, "Force"))
            {
                pVoiceProf->FaxPassThrough = VOICE_PROFILE_MODEMPASSTHROUGH_FORCE;
            }
        }
    }
    return RETURN_OK;
}


/*****************************************************************************************************************
 * Function Name : Map_hal_dml_capabilities
 * Description   : This function will retrieve the structure parameters of voice capabilities
 * @param [in]   : ParamName, pValue, buffer to fetch the voice capabilities details : pCapabilities
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int Map_hal_dml_capabilities(PTELCOVOICEMGR_DML_CAPABILITIES pCapabilities, char* ParamName, char* pValue)
{
    char *err;

    if( strstr(ParamName, "MaxProfileCount"))
    {
       pCapabilities->MaxProfileCount = strtoul(pValue,&err,10);
    }
    else if( strstr(ParamName, "MaxLineCount"))
    {
       pCapabilities->MaxLineCount = strtoul(pValue,&err,10);
    }
    else if( strstr(ParamName, "MaxSessionsPerLine"))
    {
       pCapabilities->MaxSessionsPerLine = strtoul(pValue,&err,10);
    }
    else if( strstr(ParamName, "MaxSessionCount"))
    {
       pCapabilities->MaxSessionCount = strtoul(pValue,&err,10);
    }
    else if( strstr(ParamName, "SignalingProtocols"))
    {
       strncpy(pCapabilities->SignalingProtocols, pValue,strlen(pValue)+1);
    }
    else if( strstr(ParamName, "Regions"))
    {
       strncpy(pCapabilities->Regions, pValue,strlen(pValue)+1);
    }
    else if( strstr(ParamName, "SRTPKeyingMethods"))
    {
       strncpy(pCapabilities->SRTPKeyingMethods, pValue,strlen(pValue)+1);
    }
    else if( strstr(ParamName, "SRTPEncryptionKeySizes"))
    {
       strncpy(pCapabilities->SRTPEncryptionKeySizes, pValue,strlen(pValue)+1);
    }
    else if( strstr(ParamName, "RingFileFormats"))
    {
       strncpy(pCapabilities->RingFileFormats, pValue,strlen(pValue)+1);
    }
    else if( strstr(ParamName, "SIP"))
    {
        //VoiceService.{i}.Capabilities.SIP.
        PTELCOVOICEMGR_DML_CAPABILITIES_SIP pCapabilities_SIP= &(pCapabilities->CapabilitiesSIPObj);
        if( strstr(ParamName, "Role"))
        {
            if(strstr(pValue, "UserAgent"))
            {
               pCapabilities_SIP->Role = SIP_ROLE_USER_AGENT;
            }
            else if(strstr(pValue, "BackToBackUserAgents"))
            {
               pCapabilities_SIP->Role = SIP_ROLE_B2B_USER_AGENT;
            }
            else if(strstr(pValue, "OutboundProxy"))
            {
               pCapabilities_SIP->Role = SIP_ROLE_OUTBOUND_PROXY;
            }
        }
        else if( strstr(ParamName, "Extensions"))
        {
            strncpy(pCapabilities_SIP->Extensions, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "Transports"))
        {
            strncpy(pCapabilities_SIP->Transports, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "URISchemes"))
        {
            strncpy(pCapabilities_SIP->URISchemes, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "TLSAuthenticationProtocols"))
        {
            strncpy(pCapabilities_SIP->TLSAuthenticationProtocols, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "TLSAuthenticationKeySizes"))
        {
            strncpy(pCapabilities_SIP->TLSAuthenticationKeySizes, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "TLSEncryptionProtocols"))
        {
            strncpy(pCapabilities_SIP->TLSEncryptionProtocols, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "TLSEncryptionKeySizes"))
        {
            strncpy(pCapabilities_SIP->TLSEncryptionKeySizes, pValue,strlen(pValue)+1);
        }
        else if( strstr(ParamName, "TLSKeyExchangeProtocols"))
        {
            strncpy(pCapabilities_SIP->TLSKeyExchangeProtocols, pValue,strlen(pValue)+1);
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s:%d:: Invalid ParamName[%s] paramValue[%s].\n", __FUNCTION__, __LINE__, ParamName, pValue);
        }
    }
    else if( strstr(ParamName, "MGCP"))
    {
        //VoiceService.{i}.Capabilities.MGCP.
        PTELCOVOICEMGR_DML_CAPABILITIES_MGCP pCapabilities_MGCP= &(pCapabilities->CapabilitiesMGCPObj);
        if( strstr(ParamName, "Extensions"))
        {
            strncpy(pCapabilities_MGCP->Extensions, pValue,strlen(pValue)+1);
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s:%d:: Invalid ParamName[%s] paramValue[%s].\n", __FUNCTION__, __LINE__, ParamName, pValue);
        }
    }
    else if( strstr(ParamName, "H323"))
    {
        //VoiceService.{i}.Capabilities.H323.
        PTELCOVOICEMGR_DML_CAPABILITIES_H323 pCapabilities_H323= &(pCapabilities->CapabilitiesH323Obj);
        if( strstr(ParamName, "H235AuthenticationMethods"))
        {
            strncpy(pCapabilities_H323->H235AuthenticationMethods, pValue,strlen(pValue)+1);
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s:%d:: Invalid ParamName[%s] paramValue[%s].\n", __FUNCTION__, __LINE__, ParamName, pValue);
        }
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s:%d:: Invalid ParamName[%s] paramValue[%s].\n", __FUNCTION__, __LINE__, ParamName, pValue);
    }
    return RETURN_OK;
}

