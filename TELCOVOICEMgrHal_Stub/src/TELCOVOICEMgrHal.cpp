/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
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

#include "TELCOVOICEMgrHal.h"
#define GET_PARAMETER_METHOD "getParameters"
#define SET_PARAMETER_METHOD "setParameters"

/********************************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for registering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return string "SUCCESS" in case of success else return string "FAILURE"
 **********************************************************************************************/
std::string TELCOVOICEMgrHal::testmodulepre_requisites()
{
    return "SUCCESS";

}

/**********************************************************************************************
 *Function name : testmodulepost_requisites
 *Description   : testmodulepost_requisites will be used for unregistering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE based on the return value
 **********************************************************************************************/
bool TELCOVOICEMgrHal::testmodulepost_requisites()
{
    /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
    return TEST_SUCCESS;
}

/***************************************************************************************
 *Function name :  TELCOVOICEMgrHal::initialize
 *Description   : This function is used to register all the TELCOVOICEMgrHal methods.
 *param [in]    : szVersion - version
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE
 ***************************************************************************************/
bool TELCOVOICEMgrHal::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE, "TELCOVOICEMgrHal Initialize----->Entry\n");
    return TEST_SUCCESS;
}

/*************************************************************************************
 *Function Name : TELCOVOICEMgrHal_Init
 *Description   : This function will be used to initialize the TELCOVOICEMgr HAL
 *@param [in]   : None
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void TELCOVOICEMgrHal::TELCOVOICEMgrHal_Init(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_Init----->Entry\n");
    int returnValue = RETURN_FAILURE;

    DEBUG_PRINT(DEBUG_TRACE,"\n TELCO_CONF_FILE : %s", TELCO_CONF_FILE);
    returnValue = jsonhal_init(TELCO_CONF_FILE);

    DEBUG_PRINT(DEBUG_TRACE,"\n return value from telcovoicemgrhal_init : %d", returnValue);
    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="TELCOVOICEMgrHal_Init function was Successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="TELCOVOICEMgrHal_Init function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_Init --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : TELCOVOICEMgrHal_InitData
 *Description   : This function will be used to initialize the TELCOVOICEMgr HAL
 *@param [in]   : bStatus : 0/1
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void TELCOVOICEMgrHal::TELCOVOICEMgrHal_InitData(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_InitData----->Entry\n");
    int returnValue = RETURN_FAILURE;
    int bStatus = 0;

    if(&req["bStatus"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    bStatus = req["bStatus"].asInt();

    returnValue = telcovoicemgrhal_initdata(bStatus);
    DEBUG_PRINT(DEBUG_TRACE,"\n return value from telcovoicemgrhal_initdata : %d", returnValue);

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="TELCOVOICEMgrHal_InitData function was Successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="TELCOVOICEMgrHal_InitData function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_InitData --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : TELCOVOICEMgrHal_GetParamValue
 *Description   : This function will be used to get the TELCOVOICEMgr parameter values through JSON HAL
 *@param [in]   : paramName
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void TELCOVOICEMgrHal::TELCOVOICEMgrHal_GetParamValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_GetParamValue --->Entry\n");
    int returnValue = RETURN_FAILURE;
    char details[MAX_BUFFER_SIZE_TO_SEND] = {'\0'};

    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    char parameter_value[MAX_PARAMETER_SIZE]  = {'\0'};

    if(&req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }
    strcpy(parameter_name,req["paramName"].asCString());

    returnValue = jsonhal_getparam(parameter_name, parameter_value);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "%s", parameter_value);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="TELCOVOICEMgrHal_GetParamValue function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_GetParamValue --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : TELCOVOICEMgrHal_SetParamValue
 *Description   : This function will be used to Set the TELCOVOICEMgr parameter values through JSON HAL
 *@param [in]   : paramName, paramType, paramValue
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void TELCOVOICEMgrHal::TELCOVOICEMgrHal_SetParamValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_SetParamValue --->Entry\n");
    int returnValue = RETURN_FAILURE;

    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    char parameter_type[MAX_PARAMETER_SIZE]  = {'\0'};
    char parameter_value[MAX_PARAMETER_SIZE]  = {'\0'};
    eParamType  eType = PARAM_STRING;

    if((&req["paramName"] == NULL) || (&req["paramType"] == NULL) || (&req["paramValue"] == NULL))
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }
    strcpy(parameter_name,req["paramName"].asCString());
    strcpy(parameter_type,req["paramType"].asCString());
    strcpy(parameter_value,req["paramValue"].asCString());

    if (strcmp (parameter_type,"BOOL") == 0)
    {
        eType = PARAM_BOOLEAN;
    }

    returnValue = jsonhal_setparam(parameter_name, eType, parameter_value);

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="TELCOVOICEMgrHal_SetParamValue SET Operation Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="TELCOVOICEMgrHal_SetParamValue function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_SetParamValue --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : TELCOVOICEMgrHal_GetLineStats
 *Description   : This function will be used to get the statistics value of TELCOVOICEMgr Line
 *@param [in]   : paramName - Parameter Name
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void TELCOVOICEMgrHal::TELCOVOICEMgrHal_GetLineStats(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_GetLineStats --->Entry\n");
    int returnValue = RETURN_FAILURE;
    char details[DETAILS_BUFFER_SIZE] = {'\0'};
    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    int isNegativeScenario = 0;
    TELCOVOICEMGR_DML_VOICESERVICE_STATS pLineStats;

    if(&req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    strcpy(parameter_name,req["paramName"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\n parameter name passed to telcovoicemgrhal_getlinestats : %s", parameter_name);

    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
        DEBUG_PRINT(DEBUG_TRACE, "\nExecuting negative scenario\n");
      	returnValue = telcovoicemgrhal_getlinestats(parameter_name,NULL);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE, "\nExecuting positive scenario\n");
        returnValue = telcovoicemgrhal_getlinestats(parameter_name,&pLineStats);
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n return value from telcovoicemgrhal_getlinestats : %d", returnValue);
    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "Average Far End Interarrival Jitter=%u Average Receive Interarrival Jitter=%u Average Round Trip Delay=%u Bytes Received=%u Bytes Sent=%u Far End Interarrival Jitter=%u Far End Packet Loss Rate=%u Incoming Calls Answered=%u Incoming Calls Connected=%u Incoming Calls Failed=%u Incoming Calls Received=%u Outgoing Calls Answered=%u Outgoing Calls Attempted=%u Outgoing Calls Connected=%u Outgoing Calls Failed=%u Packets Lost=%u Packets Received=%u Packets Sent=%u Receive Interarrival Jitter=%u Receive Packet Loss Rate=%u Round Trip Delay=%u Overruns=%u Underruns=%u Calls Dropped=%u Total Call Time=%u", pLineStats.AverageFarEndInterarrivalJitter, pLineStats.AverageReceiveInterarrivalJitter, pLineStats.AverageRoundTripDelay, pLineStats.BytesReceived, pLineStats.BytesSent, pLineStats.FarEndInterarrivalJitter, pLineStats.FarEndPacketLossRate, pLineStats.IncomingCallsAnswered, pLineStats.IncomingCallsConnected, pLineStats.IncomingCallsFailed, pLineStats.IncomingCallsReceived, pLineStats.OutgoingCallsAnswered, pLineStats.OutgoingCallsAttempted, pLineStats.OutgoingCallsConnected, pLineStats.OutgoingCallsFailed, pLineStats.PacketsLost, pLineStats.PacketsReceived, pLineStats.PacketsSent,pLineStats.ReceiveInterarrivalJitter,pLineStats.ReceivePacketLossRate, pLineStats.RoundTripDelay, pLineStats.Overruns, pLineStats.Underruns,pLineStats.CallsDropped, pLineStats.TotalCallTime);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="TELCOVOICEMgrHal_GetLineStats function has failed";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_GetLineStats --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : TELCOVOICEMgrHal_GetCapabilities
 *Description   : This function will be used to get the information of TELCOVOICEMgr Capabilities
 *@param [in]   : index, paramName - Parameter Name
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *************************************************************************************/
void TELCOVOICEMgrHal::TELCOVOICEMgrHal_GetCapabilities(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_GetCapabilities --->Entry\n");
    int returnValue = RETURN_FAILURE;
    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    char details[DETAILS_BUFFER_SIZE] = {'\0'};
    int isNegativeScenario = 0;
    PTELCOVOICEMGR_DML_CAPABILITIES pCapabilities = PTELCOVOICEMGR_DML_CAPABILITIES(malloc(sizeof(TELCOVOICEMGR_DML_CAPABILITIES)));

    if(&req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }
    strcpy(parameter_name,req["paramName"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\n parameter name passed to telcovoicemgrhal_getcapabilities : %s", parameter_name);

    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
        DEBUG_PRINT(DEBUG_TRACE, "\nExecuting negative scenario\n");
        returnValue = telcovoicemgrhal_getcapabilities(NULL, parameter_name);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE, "\nExecuting positive scenario\n");
        returnValue = telcovoicemgrhal_getcapabilities(pCapabilities, parameter_name);
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n return value from telcovoicemgrhal_getcapabilities : %d", returnValue);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "Max Profile Count=%lu, Max Line Count=%lu, Max Sessions Per Line=%lu, Max Session Count=%lu, SIP Role=%d", pCapabilities->MaxProfileCount, pCapabilities->MaxLineCount, pCapabilities->MaxSessionsPerLine, pCapabilities->MaxSessionCount, pCapabilities->CapabilitiesSIPObj.Role);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="TELCOVOICEMgrHal_GetCapabilities function has failed";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_GetCapabilities --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : TELCOVOICEMgrHal_GetVoiceProfile
 *Description   : This function will be used to get the statistics values of Voice Profile
 *@param [in]   : index, paramName - Parameter Name
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void TELCOVOICEMgrHal::TELCOVOICEMgrHal_GetVoiceProfile(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_GetVoiceProfile --->Entry\n");
    int returnValue = RETURN_FAILURE;
    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    char details[DETAILS_BUFFER_SIZE] = {'\0'};
    int index = 0;
    int isNegativeScenario = 0;
    DML_PROFILE_LIST_T pVoiceProfileList;

    if(&req["index"] == NULL || &req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    index = req["index"].asInt();
    strcpy(parameter_name,req["paramName"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\n parameter name passed to telcovoicemgrhal_getvoiceprofile : %s", parameter_name);
    DEBUG_PRINT(DEBUG_TRACE,"\n index value sent to telcovoicemgrhal_getvoiceprofile : %d", index);

    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
        DEBUG_PRINT(DEBUG_TRACE, "\nExecuting negative scenario\n");
        returnValue = telcovoicemgrhal_getvoiceprofile(NULL, index, parameter_name);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE, "\nExecuting positive scenario\n");
        returnValue = telcovoicemgrhal_getvoiceprofile(&pVoiceProfileList, index, parameter_name);
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n return value from telcovoicemgrhal_getvoiceprofile : %d", returnValue);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "TELCOVOICEMgrHal_GetVoiceProfile function is success");
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="TELCOVOICEMgrHal_GetVoiceProfile function has failed";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_GetVoiceProfile --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : TELCOVOICEMgrHal_GetPhyInterface
 *Description   : This function will be used to get Physical Interafce values of the voice manager
 *@param [in]   : index, paramName - Parameter Name
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void TELCOVOICEMgrHal::TELCOVOICEMgrHal_GetPhyInterface(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_GetPhyInterface --->Entry\n");
    int returnValue = RETURN_FAILURE;
    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    char details[DETAILS_BUFFER_SIZE] = {'\0'};
    int index = 0;
    int isNegativeScenario = 0;
    DML_PHYINTERFACE_LIST_T pPhyInterfaceList;

    if(&req["index"] == NULL || &req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    index = req["index"].asInt();
    strcpy(parameter_name,req["paramName"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\n parameter name passed to telcovoicemgrhal_getphyinterface : %s", parameter_name);
    DEBUG_PRINT(DEBUG_TRACE,"\n index value sent to telcovoicemgrhal_getphyinterface : %d", index);

    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
        DEBUG_PRINT(DEBUG_TRACE, "\nExecuting negative scenario\n");
        returnValue = telcovoicemgrhal_getphyinterface(NULL, index, parameter_name);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE, "\nExecuting positive scenario\n");
        returnValue = telcovoicemgrhal_getphyinterface(&pPhyInterfaceList, index, parameter_name);
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n return value from telcovoicemgrhal_getphyinterface : %d", returnValue);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "TELCOVOICEMgrHal_GetPhyInterface function is success");
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="TELCOVOICEMgrHal_GetPhyInterface function has failed";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n TELCOVOICEMgrHal_GetPhyInterface --->Exit\n");
    return;
}

/***************************************************************************************************
 *Function Name   : CreateObject
 *Description     : This function is used to create a new object of the class "TELCOVOICEMgrHal".
 *@param [in]     : None
 ***************************************************************************************************/
extern "C" TELCOVOICEMgrHal* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new TELCOVOICEMgrHal(ptrtcpServer);
}

/*************************************************************************************
 *Function Name : cleanup
 *Description   : This function will be used to the close things cleanly.
 *@param [in]   : szVersion - version, ptrAgentObj - Agent object
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
bool TELCOVOICEMgrHal::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE, "cleaning up\n");
    return TEST_SUCCESS;
}

/**********************************************************************************
 *Function Name : DestroyObject
 *Description   : This function will be used to destroy the TELCOVOICEMgrHal object.
 *@param [in]   : Input argument is TELCOVOICEMgrHal Object
 **********************************************************************************/
extern "C" void DestroyObject(TELCOVOICEMgrHal *stubobj)
{
    DEBUG_PRINT(DEBUG_TRACE, "Destroying TELCOVOICEMgrHal object\n");
    delete stubobj;
}

