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

#include "DSLHAL.h"
#define GET_PARAMETER_METHOD "getParameters"
#define SET_PARAMETER_METHOD "setParameters"

#define MAX_BUFFER_SIZE_TO_SEND 500
#define MAX_PARAMETER_SIZE 500
#define RETURN_SUCCESS 0
#define RETURN_FAILURE 1
#define DSL_CONF_FILE "/etc/rdk/conf/xdsl_manager_conf.json"

/********************************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for registering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return string "SUCCESS" in case of success else return string "FAILURE"
 **********************************************************************************************/
std::string DSLHAL::testmodulepre_requisites()
{
    /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
    return "SUCCESS";

}

/**********************************************************************************************
 *Function name : testmodulepost_requisites
 *Description   : testmodulepost_requisites will be used for unregistering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE based on the return value
 **********************************************************************************************/
bool DSLHAL::testmodulepost_requisites()
{
    /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
    return TEST_SUCCESS;
}

/***************************************************************************************
 *Function name :  DSLHAL::initialize
 *Description   : This function is used to register all the ble_hal methods.
 *param [in]    : szVersion - version, ptrAgentObj - Agent obhect
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE
 ***************************************************************************************/
bool DSLHAL::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE, "DSLHAL Initialize----->Entry\n");
    return TEST_SUCCESS;
}

/*************************************************************************************
 *Function Name : DSLHAL_Init
 *Description   : This function will be used to initialize the DSL HAL
 *@param [in]   : None
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void DSLHAL::DSLHAL_Init(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_Init----->Entry\n");
    int returnValue = RETURN_FAILURE;

    DEBUG_PRINT(DEBUG_TRACE,"\n DSL_CONF_FILE : %s", DSL_CONF_FILE);
    returnValue = jsonhal_init(DSL_CONF_FILE);

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="DSLHAL_Init function was Successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="DSLHAL_Init function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_Init --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : DSLHAL_GetParamValue
 *Description   : This function will be used to get the DSL parameter values through JSON HAL
 *@param [in]   : None
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void DSLHAL::DSLHAL_GetParamValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetParamValue --->Entry\n");
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
        response["details"]="DSLHAL_GetParamValue function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetParamValue --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : DSLHAL_SetParamValue
 *Description   : This function will be used to Set the DSL parameter values through JSON HAL
 *@param [in]   : None
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void DSLHAL::DSLHAL_SetParamValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_SetParamValue --->Entry\n");
    int returnValue = RETURN_FAILURE;

    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    char parameter_type[MAX_PARAMETER_SIZE]  = {'\0'};
    char parameter_value[MAX_PARAMETER_SIZE]  = {'\0'};
    eParamType	eType = PARAM_STRING;

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
        response["details"]="DSLHAL_SetParamValue SET Operation Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="DSLHAL_SetParamValue function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_SetParamValue --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : DSLHAL_GetLineStats
 *Description   : This function will be used to get the statistics value of DSL Line
 *@param [in]   : paramName - Parameter Name
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void DSLHAL::DSLHAL_GetLineStats(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetLineStats --->Entry\n");
    int returnValue = RETURN_FAILURE;
    char details[2048] = {'\0'};
    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    DML_XDSL_LINE_STATS pLineStats;

    if(&req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    strcpy(parameter_name,req["paramName"].asCString());

    //Collect Line Statistics
    returnValue = dslhal_getlinestats(parameter_name,&pLineStats);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "BytesSent=%lu BytesReceived=%lu PacketsSent=%lu PacketsReceived=%lu ErrorsSent=%lu ErrorsReceived=%lu DiscardPacketsSent=%lu DiscardPacketsReceived=%lu TotalStart=%lu ShowtimeStart=%lu LastShowtimeStart=%d QuarterHourStart=%lu CurrentDayStart=%lu CurrentTime ErroredSecs=%d CurrentTime SeverelyErroredSecs=%d ShowTime ErroredSecs=%d ShowTime SeverelyErroredSecs=%d LastShowTime ErroredSecs=%d LastShowTime SeverelyErroredSecs=%d CurrentDay ErroredSecs=%d CurrentDay SeverelyErroredSecs=%d CurrentDay X_RDK_LinkRetrain=%d CurrentDay X_RDK_InitErrors=%d CurrentDay X_RDK_InitTimeouts=%d stQuarterHour X_RDK_LinkRetrain=%d stQuarterHour ErroredSecs=%d stQuarterHour SeverelyErroredSecs=%d ", pLineStats.BytesSent, pLineStats.BytesReceived, pLineStats.PacketsSent, pLineStats.PacketsReceived, pLineStats.ErrorsSent, pLineStats.ErrorsReceived, pLineStats.DiscardPacketsSent, pLineStats.DiscardPacketsReceived, pLineStats.TotalStart, pLineStats.ShowtimeStart, pLineStats.LastShowtimeStart, pLineStats.QuarterHourStart, pLineStats.CurrentDayStart, pLineStats.stTotal.ErroredSecs, pLineStats.stTotal.SeverelyErroredSecs, pLineStats.stShowTime.ErroredSecs, pLineStats.stShowTime.SeverelyErroredSecs, pLineStats.stLastShowTime.ErroredSecs, pLineStats.stLastShowTime.SeverelyErroredSecs, pLineStats.stCurrentDay.ErroredSecs,pLineStats.stCurrentDay.SeverelyErroredSecs, pLineStats.stCurrentDay.X_RDK_LinkRetrain, pLineStats.stCurrentDay.X_RDK_InitErrors, pLineStats.stCurrentDay.X_RDK_InitTimeouts,pLineStats.stQuarterHour.X_RDK_LinkRetrain, pLineStats.stQuarterHour.ErroredSecs, pLineStats.stQuarterHour.SeverelyErroredSecs );

        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="DSLHAL_GetLineStats function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetLineStats --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : DSLHAL_GetXRdk_Nlm
 *Description   : This function will be used to get the NLM value of DSL Line
 *@param [in]   : paramName - Parameter Name
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void DSLHAL::DSLHAL_GetXRdk_Nlm(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetXRdk_Nlm --->Entry\n");
    char details[1024] = {'\0'};
    int returnValue = RETURN_FAILURE;
    DML_XDSL_X_RDK_NLNM  pstXRdkNlm;
    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};

    if(&req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    strcpy(parameter_name,req["paramName"].asCString());

    returnValue = dslhal_getXRdk_Nlm(parameter_name,&pstXRdkNlm );

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details,"%d", pstXRdkNlm.echotonoiseratio);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="DSLHAL_GetXRdk_Nlm function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetXRdk_Nlm --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : DSLHAL_GetLineInfo
 *Description   : This function will be used to get the information of DSL Line
 *@param [in]   : paramName - Parameter Name
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *************************************************************************************/
void DSLHAL::DSLHAL_GetLineInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetLineInfo --->Entry\n");
    int returnValue = RETURN_FAILURE;
    char details[2048] = {'\0'};
    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    DML_XDSL_LINE pLineInfo;

    if(&req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    strcpy(parameter_name,req["paramName"].asCString());

    //Collect Line Statistics
    returnValue = dslhal_getlineinfo(parameter_name,&pLineInfo);

    if(returnValue == RETURN_SUCCESS)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n return value is SUCCESS \n");
        sprintf(details, " ulInstanceNumber =%lu LowerLayers=%s Name=%s LastChange=%i ",pLineInfo.ulInstanceNumber,pLineInfo.LowerLayers,pLineInfo.Name,pLineInfo.LastChange);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="DSLHAL_GetLineInfo function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetLineInfo --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : DSLHAL_XtmGetLinkStats
 *Description   : This function will be used to get the statistics value of xtm DSL Line
 *@param [in]   : paramName - Parameter Name
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void DSLHAL::DSLHAL_XtmGetLinkStats(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_XtmGetLinkStats --->Entry\n");
    int returnValue = RETURN_FAILURE;
    char details[2048] = {'\0'};
    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    DML_PTM_STATS link_stats;

    if(&req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    strcpy(parameter_name,req["paramName"].asCString());

    //Collect Line Statistics
    returnValue =   xtm_hal_getLinkStats(parameter_name,&link_stats);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "BytesSent = %ld BytesReceived = %ld ", link_stats.BytesSent,link_stats.BytesReceived);

        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="DSLHAL_XtmGetLinkStats function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_XtmGetLinkStats --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : DSLHAL_AtmGetLinkStats
 *Description   : This function will be used to get the statistics of ATM Link
 *@param [in]   : paramName - Parameter Name
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void DSLHAL::DSLHAL_AtmGetLinkStats(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_AtmGetLinkStats --->Entry\n");
    int returnValue = RETURN_FAILURE;
    char details[2048] = {'\0'};
    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    DML_ATM_STATS link_stats;

    if(&req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    strcpy(parameter_name,req["paramName"].asCString());

    //Collect Line Statistics
    returnValue = atm_hal_getLinkStats(parameter_name,&link_stats);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "BytesSent = %ld BytesReceived = %ld PacketsSent = %ld ", link_stats.BytesSent,link_stats.BytesReceived,link_stats.PacketsSent);

        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="DSLHAL_AtmGetLinkStats function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_AtmGetLinkStats --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : DSLHAL_GetChannelInfo
 *Description   : This function will be used to get channel Information
 *@param [in]   : paramName - Parameter Name
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void DSLHAL::DSLHAL_GetChannelInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetChannelInfo --->Entry\n");
    int returnValue = RETURN_FAILURE;
    char details[2048] = {'\0'};
    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    DML_XDSL_CHANNEL pstChannelInfo;

    if(&req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    strcpy(parameter_name,req["paramName"].asCString());

    //Collect Line Statistics
    returnValue =   xdsl_hal_dslGetChannelInfo(parameter_name,&pstChannelInfo);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "LastChange=%i LPATH=%i LinkEncapsulationSupported=%s LinkEncapsulationUsed=%s",pstChannelInfo.LastChange,pstChannelInfo.LPATH,pstChannelInfo.LinkEncapsulationSupported,pstChannelInfo.LinkEncapsulationUsed);

        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="DSLHAL_GetChannelInfo function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetChannelInfo --->Exit\n");
    return;
}

/*************************************************************************************
 *Function Name : DSLHAL_GetChannelStats
 *Description   : This function will be used to get the statistics of Channel
 *@param [in]   : paramName - Parameter Name
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
void DSLHAL::DSLHAL_GetChannelStats(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetChannelStats --->Entry\n");
    int returnValue = RETURN_FAILURE;
    char details[2048] = {'\0'};
    char parameter_name[MAX_PARAMETER_SIZE]  = {'\0'};
    DML_XDSL_CHANNEL_STATS pstChannelStats;

    if(&req["paramName"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    strcpy(parameter_name,req["paramName"].asCString());

    //Collect Line Statistics
    returnValue =   xdsl_hal_dslGetChannelStats(parameter_name,&pstChannelStats);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "BytesSent=%lu BytesReceived=%lu PacketsSent=%lu PacketsReceived=%lu",pstChannelStats.BytesSent,pstChannelStats.BytesReceived,pstChannelStats.PacketsSent,pstChannelStats.PacketsReceived);

        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="DSLHAL_GetChannelStats function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n DSLHAL_GetChannelStats --->Exit\n");
    return;
}

/***************************************************************************************************
 *Function Name   : CreateObject
 *Description     : This function is used to create a new object of the class "DSLHAL".
 *@param [in]     : None
 ***************************************************************************************************/
extern "C" DSLHAL* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new DSLHAL(ptrtcpServer);
}

/*************************************************************************************
 *Function Name : cleanup
 *Description   : This function will be used to the close things cleanly.
 *@param [in]   : szVersion - version, ptrAgentObj - Agent object
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
bool DSLHAL::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE, "cleaning up\n");
    return TEST_SUCCESS;
}

/**********************************************************************************
 *Function Name : DestroyObject
 *Description   : This function will be used to destroy the DSLHAL object.
 *@param [in]   : Input argument is DSLHAL Object
 **********************************************************************************/
extern "C" void DestroyObject(DSLHAL *stubobj)
{
    DEBUG_PRINT(DEBUG_TRACE, "Destroying DSLHAL object\n");
    delete stubobj;
}



