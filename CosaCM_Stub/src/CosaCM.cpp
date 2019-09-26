/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2016 RDK Management
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

#include "CosaCM.h"
#include "ssp_tdk_wrp.h"

/* To provide external linkage to C Functions defined in TDKB Component folder */

extern "C"
{
int ssp_register(bool);
int ssp_terminate();
int ssp_CosaDmlCMGetResetCount(int handleType, int bufferType, char *pResetType);
int ssp_CosaDmlCMGetLockedUpstreamChID(int handleType);
int ssp_CosaDmlCMSetLockedUpstreamChID(int handleType, int channelId);
int ssp_CosaDmlCMGetStartDSFrequency(int handleType);
int ssp_CosaDmlCMSetStartDSFrequency(int handleType, int frequency);
int ssp_CosaDmlCMGetProvType(int handleType, int bufferType);
int ssp_CosaDmlCMGetIPv6DHCPInfo(int handleType, int bufferType);
int ssp_cosacm_getcpelist();
int ssp_cosacm_getcertstatus();
int ssp_cosacm_getcmerrorcodewords();
int ssp_cosacm_getcert();
int ssp_cosacm_getmddipoverride(char *value);
int ssp_cosacm_setmddipoverride(char *value);
int ssp_cosacm_getmarket();
int ssp_cosacm_getmarket_memory_unalloc();
int ssp_cosacm_setmddipoverride_memory_unalloc();
int ssp_cosacm_getmddipoverride_memory_unalloc();
int ssp_cosacm_getcert_memory_unalloc();
int ssp_cosacm_getcmerrorcodewords_invalid_arg();
int ssp_cosacm_getcertstatus_invalid_arg();
int ssp_cosacm_getcpelist_invalid_arg();
int ssp_CosaDmlCMGetStatus(int handleType, int Value);
int ssp_CosaCMGetLoopDiagnosticsStart(int handleType, int boolValue);
int ssp_CosaDmlCMGetLoopDiagnosticsDetails(int handleType, int Value);
int ssp_CosaDmlCMGetTelephonyRegistrationStatus(int handleType, int Value);
int ssp_CosaDmlCMGetTelephonyDHCPStatus(int handleType, int Value);
int ssp_CosaDmlCMGetTelephonyTftpStatus(int handleType, int Value);
int ssp_CosaDmlCMSetLoopDiagnosticsStart(int handleType, int boolValue);
int ssp_cosacm_GetDHCPInfo(int handleType, int bufferType);
int ssp_cosacm_GetDOCSISInfo(int handleType, int bufferType);
int ssp_cosacm_GetLog(int handleType, int bufferType);
int ssp_cosacm_SetLog(int handleType, int bufferType);
int ssp_cosacm_GetDocsisLog(int handleType, int bufferType);
int ssp_cosacm_GetDownstreamChannel(int handleType, int bufferType);
int ssp_cosacm_GetUpstreamChannel(int handleType, int bufferType);
int ssp_CosaCableModemCreate();
int ssp_CosaCableModemInitialize(int handleType);
int ssp_CosaCableModemRemove(int handleType);

int ssp_CMHal_GetCharValues(char* paramName, char* value);
int ssp_CMHal_GetUlongValues(char* paramName, unsigned long* value);
int ssp_CMHal_GetStructValues(char*, void*);
};

/***************************************************************************
 *Function name	: initialize
 *Description	: Initialize Function will be used for registering the wrapper method
 *        	  	  with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/

bool CosaCM::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE,"TDK::CosaCM Initialize\n");
    return TEST_SUCCESS;
}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string CosaCM::testmodulepre_requisites()
{
    int returnValue;
    returnValue = ssp_register(1);

    if(0 != returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepre_requisites: Failed to initialize \n");
        return "TEST_FAILURE";
    }

    return "SUCCESS";
}

/***************************************************************************
 *Function name : testmodulepost_requisites
 *Description   : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/
bool CosaCM::testmodulepost_requisites()
{
    DEBUG_PRINT(DEBUG_LOG,"DBG:CosaCM:testmodulepost_requisites() \n");
    return 0;
}

/*******************************************************************************************
 *
 * Function Name    : CosaCM_GetResetCount
 * Description      : This function is used to retrieve the reset count of docsis, erouter
 *                    cable modem and local reset count
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType: Holds whether buffer passed is valid or NULL
 * @param [in]  req - resetType: Holds whether reset type is docsis, cable modem, erouter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_GetResetCount(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetResetCount --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;
    char resetType[MAX_PARAM_SIZE];

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }
    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }
    if(&req["resetType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();
    strcpy(resetType,req["resetType"].asCString());

    /* Invoke the wrapper function to get the reset count */
    returnValue = ssp_CosaDmlCMGetResetCount(handleType,bufferType,resetType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the reset count";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the reset count";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetResetCount --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetResetCount  --->Exit\n");
    return;
}


/*******************************************************************************************
 *
 * Function Name    : CosaCM_GetUpstreamChannelId
 * Description      : This function will retrieve the currently locked upstream channel Id
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_GetUpstreamChannelId(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetUpstreamChannelId --->Entry \n");

    int returnValue = 0;
    int handleType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();

    returnValue = ssp_CosaDmlCMGetLockedUpstreamChID(handleType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the upstream channel Id";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the upstream channel Id";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetUpstreamChannelId --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetUpstreamChannelId  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaCM_SetUpstreamChannelId
 * Description      : This function will lock channel for the specified upstream channel Id.
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_SetUpstreamChannelId(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_SetUpstreamChannelId --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int channelId = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["channelId"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    channelId = req["channelId"].asInt();

    returnValue = ssp_CosaDmlCMSetLockedUpstreamChID(handleType,channelId);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully locked the channel for the upstream channel Id";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to lock channel for the upstream channel Id";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_SetUpstreamChannelId --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_SetUpstreamChannelId  --->Exit\n");
    return;
}


/*******************************************************************************************
 *
 * Function Name    : CosaCM_GetStartDSFrequency
 * Description      : This function will retrieve the current downstream frequency
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_GetStartDSFrequency(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetStartDSFrequency --->Entry \n");

    int returnValue = 0;
    int handleType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();

    returnValue = ssp_CosaDmlCMGetStartDSFrequency(handleType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the downstream frequency";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the downstream ferquency";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetStartDSFrequency --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetStartDSFrequency  --->Exit\n");
    return;
}


/*******************************************************************************************
 *
 * Function Name    : CosaCM_SetStartDSFrequency
 * Description      : This function will set the specified downstream frequency
 *
 * @param [in]  req - handleType : Holds the message bus handl
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_SetStartDSFrequency(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_SetStartDSFrequency --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int frequency = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["frequency"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    frequency = req["frequency"].asInt();

    returnValue = ssp_CosaDmlCMSetStartDSFrequency(handleType,frequency);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully set the downstream frequency";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set the downstream frequency";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_SetStartDSFrequency --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_SetStartDSFrequency  --->Exit\n");
    return;
}


/*******************************************************************************************
 *
 * Function Name    : CosaCM_GetProvType
 * Description      : This function will retrieve the provisioning type
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_GetProvType(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetProvType --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();

    returnValue = ssp_CosaDmlCMGetProvType(handleType,bufferType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the provisioning type";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the provisioning type";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetProvType --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetProvType  --->Exit\n");
    return;
}

/*******************************************************************************************
*
* Function Name    : CosaCM_GetIPv6DHCPInfo
* Description      : This function will retrieve the DHCP information of IPv6
*
* @param [in]  req - handleType : Holds the message bus handle
* @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::CosaCM_GetIPv6DHCPInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetIPv6DHCPInfo --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();

    returnValue = ssp_CosaDmlCMGetIPv6DHCPInfo(handleType,bufferType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the DHCP information of IPv6";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the DHCP information of IPv6";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetIPv6DHCPInfo --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetIPv6DHCPInfo  --->Exit\n");
    return;
}


/*******************************************************************************************
*
* Function Name    : COSACM_GetMarket
* Description      : This function will invoke COSACM_GetMarket API Function and obtain
*                    its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetMarket(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMarket--->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_getmarket();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the DUT Market Information";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the DUT Market Information";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMarket --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMarket --->Exit\n");

    return;
}

/*******************************************************************************************
*
* Function Name    : CosaDmlCMSetMDDIPOverride
* Description      : This function will invoke the CosaDmlCMSetMDDIPOverride API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_SetMDDIPOverride(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_SetMDDIPOverride --->Entry \n");

    int returnValue = 0;
    char value[10] = {0};

    if(&req["value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    strcpy(value,req["value"].asCString());

    printf("MDD value to be set is:%s\n",value);
    returnValue = ssp_cosacm_setmddipoverride(value);

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully Set the MDD IP Override Function";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to Set the MDD IP Override Function";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_SetMDDIPOverride --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_SetMDDIPOverride --->Exit\n");

    return;
}

/*******************************************************************************************
*
* Function Name    : COSACM_GetMDDIPOverride
* Description      : This function will invoke the COSACM_GetMDDIPOverride API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetMDDIPOverride(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMDDIPOverride --->Entry \n");

    int returnValue = 0;
    char mdd_value[10] = {0};
    char paramDetails[30] = {0};

    returnValue = ssp_cosacm_getmddipoverride(mdd_value);

    if(0 == returnValue)
    {
        sprintf(paramDetails,"MDD Override Value is:%s",mdd_value);
        response["result"]="SUCCESS";
        response["details"]=paramDetails;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to Get the MDD IP Override Function";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMDDIPOverride --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMDDIPOverride --->Exit\n");

    return;
}

/*******************************************************************************************
*
* Function Name    : COSACM_GetCMCert
* Description      : This function will invoke the COSACM_GetCMCert API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetCMCert(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCert --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_getcert();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully Executed and Get the CM Certificate";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to Get the CM Certificate";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCert --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCert --->Exit\n");

    return;
}

/*******************************************************************************************
*
* Function Name    : COSACM_GetCMCertStatus
* Description      : This function will invoke the COSACM_GetCMCertStatus API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetCMCertStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCertStatus --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_getcertstatus();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully Executed and Get the CM Certificate Status Info";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to Get the CM Certificate Status Information";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCertStatus --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCertStatus --->Exit\n");

    return;
}

/*******************************************************************************************
*
* Function Name    : COSACM_GetCMErrorCodewords
* Description      : This function will invoke the COSACM_GetCMErrorCodewords API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetCMErrorCodewords(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMErrorCodewords --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_getcmerrorcodewords();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully Get the CM Error Code Words Info";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to Get the CM Error Code Words Info";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMErrorCodewords --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMErrorCodewords --->Exit\n");

    return;
}


/*******************************************************************************************
*
* Function Name    : COSACM_GetCPEList
* Description      : This function will invoke the COSACM_GetCPEList API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetCPEList(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCPEList --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_getcpelist();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully Get the CPE List information";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to Get the CPE List Information";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCPEList --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCPEList --->Exit\n");

    return;
}



/*******************************************************************************************
*
* Function Name    : COSACM_GetMarket_ArgMemory_unalloc
* Description      : This function will invoke COSACM_GetMarket API Function and obtain
*                    its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetMarket_ArgMemory_unalloc(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMarket_ArgMemory_unalloc --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_getmarket_memory_unalloc();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully handled the input memory unallocated case";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to handle the input memory unallocated case";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMarket_ArgMemory_unalloc --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMarket_ArgMemory_unalloc --->Exit\n");

    return;
}

/*******************************************************************************************
*
* Function Name    : COSACM_SetMDDIPOverride_ArgMemory_unalloc
* Description      : This function will invoke the COSACM_SetMDDIPOverride API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_SetMDDIPOverride_ArgMemory_unalloc(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_SetMDDIPOverride_ArgMemory_unalloc --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_setmddipoverride_memory_unalloc();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully handled the input memory unallocated case";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to handle the input memory unallocated case";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_SetMDDIPOverride_ArgMemory_unalloc --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_SetMDDIPOverride_ArgMemory_unalloc --->Exit\n");

    return;
}

/*******************************************************************************************
*
* Function Name    : COSACM_GetMDDIPOverride_ArgMemory_unalloc
* Description      : This function will invoke the COSACM_GetMDDIPOverride API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetMDDIPOverride_ArgMemory_unalloc(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMDDIPOverride --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_getmddipoverride_memory_unalloc();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully handled the input memory unallocated case";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to handle the input memory unallocated case";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMDDIPOverride_ArgMemory_unalloc --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetMDDIPOverride_ArgMemory_unalloc --->Exit\n");

    return;
}

/*******************************************************************************************
*
* Function Name    : COSACM_GetCMCert_ArgMemory_unalloc
* Description      : This function will invoke the COSACM_GetCMCert API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetCMCert_ArgMemory_unalloc(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCert_ArgMemory_unalloc --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_getcert_memory_unalloc();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully handled the input memory unallocated case";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to handle the input memory unallocated case";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCert_ArgMemory_unalloc --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCert_ArgMemory_unalloc --->Exit\n");

    return;
}

/*******************************************************************************************
*
* Function Name    : COSACM_GetCMCertStatus_InvalidArg
* Description      : This function will invoke the COSACM_GetCMCertStatus API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetCMCertStatus_InvalidArg(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCertStatus_InvalidArg--->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_getcertstatus_invalid_arg();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully handled the invalid input argument";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to handle the invalid input argument";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCertStatus_InvalidArg --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMCertStatus_InvalidArg--->Exit\n");

    return;
}

/*******************************************************************************************
*
* Function Name    : COSACM_GetCMErrorCodewords_InvalidArg
* Description      : This function will invoke the COSACM_GetCMErrorCodewords API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetCMErrorCodewords_InvalidArg(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMErrorCodewords_InvalidArg --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_getcmerrorcodewords_invalid_arg();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully handled the invalid input argument";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to handle the invalid input argument";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMErrorCodewords_InvalidArg --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCMErrorCodewords_InvalidArg --->Exit\n");

    return;
}


/*******************************************************************************************
*
* Function Name    : COSACM_GetCPEList_InvalidArg
* Description      : This function will invoke the COSACM_GetCPEList API Function
*                    and obtain its response
* @param [in]  req - Nil
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetCPEList_InvalidArg(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCPEList_InvalidArg --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_cosacm_getcpelist_invalid_arg();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully handled the invalid input argument";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to handle the invalid input argument";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCPEList_InvalidArg --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetCPEList_InvalidArg --->Exit\n");

    return;
}

/*******************************************************************************************
*
* Function Name    : CosaCM_GetStatus
* Description      : This function will retrieve the DHCP information of IPv6
*
* @param [in]  req - handleType : Holds the message bus handle
* @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::CosaCM_GetStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetStatus --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["Value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    Value = req["Value"].asInt();

    returnValue =ssp_CosaDmlCMGetStatus(handleType,Value);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully got CM Status";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get CM Status";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetStatus --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetStatus  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaCM_GetLoopDiagnosticsStart
 * Description      : This function will get the Loop Diagnostics Start
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - boolValue : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_GetLoopDiagnosticsStart(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetLoopDiagnosticsStart --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int boolValue = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["boolValue"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    boolValue = req["boolValue"].asInt();

    returnValue =ssp_CosaCMGetLoopDiagnosticsStart(handleType,boolValue);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully got the Loop Diagnostics Start";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the Loop Diagnostics Start";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetLoopDiagnosticsStart --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetLoopDiagnosticsStart  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaCM_GetLoopDiagnosticsDetails
 * Description      : This function will get the Loop Diagnostics Details
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_GetLoopDiagnosticsDetails(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetLoopDiagnosticsDetails --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }
    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();

    returnValue =ssp_CosaDmlCMGetLoopDiagnosticsDetails(handleType,bufferType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully got the Loop Diagnostics Details";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the Loop Diagnostics Details";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetLoopDiagnosticsDetails --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetLoopDiagnosticsDetails  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaCM_GetTelephonyRegistrationStatus
 * Description      : This function will get Telephony Registration Status.
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_GetTelephonyRegistrationStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetTelephonyRegistrationStatus --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }
    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();

    returnValue =ssp_CosaDmlCMGetTelephonyRegistrationStatus(handleType,bufferType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully got Telephony Registration Status";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get Telephony Registration Status";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetTelephonyRegistrationStatus --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetTelephonyRegistrationStatus  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaCM_GetTelephonyTftpStatus
 * Description      : This function will get Telephony Tftp Status.
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_GetTelephonyTftpStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetTelephonyTftpStatus --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }
    if(&req["Value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    Value = req["Value"].asInt();

    returnValue =ssp_CosaDmlCMGetTelephonyTftpStatus(handleType,Value);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully got Telephony Tftp Status";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get Telephony Tftp Status";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetTelephonyTftpStatus --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetTelephonyTftpStatus  --->Exit\n");
    return;
}

/*******************************************************************************************
 * Function Name    : CosaCM_GetTelephonyDHCPStatus
 * Description      : This function will get Telephony DHCP Status.
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_GetTelephonyDHCPStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetTelephonyDHCPStatus --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }
    if(&req["Value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    Value = req["Value"].asInt();

    returnValue =ssp_CosaDmlCMGetTelephonyDHCPStatus(handleType,Value);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully got Telephony DHCP Status";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get Telephony DHCP Status";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetTelephonyDHCPStatus --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_GetTelephonyDHCPStatus  --->Exit\n");
    return;
}

/*******************************************************************************************
 * Function Name    : CosaCM_SetLoopDiagnosticsStart
 * Description      : This function will set Loop Diagnostics Start.
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - boolValue :
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CosaCM_SetLoopDiagnosticsStart(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_SetLoopDiagnosticsStart --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int boolValue = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }
    if(&req["boolValue"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    boolValue = req["boolValue"].asInt();

    returnValue =ssp_CosaDmlCMSetLoopDiagnosticsStart(handleType,boolValue);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully Set Loop Diagnostics Start value";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to Set Loop Diagnostics Start value";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_SetLoopDiagnosticsStart --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaCM_SetLoopDiagnosticsStart  --->Exit\n");
    return;
}

/*******************************************************************************************
*
* Function Name    : COSACM_GetDHCPInfo
* Description      : This function will retrieve the DHCP information
*
* @param [in]  req - handleType : Holds the message bus handle
* @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetDHCPInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDHCPInfo --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();
    returnValue = ssp_cosacm_GetDHCPInfo(handleType,bufferType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the DHCP information";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the DHCP information";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDHCPInfo --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDHCPInfo  --->Exit\n");
    return;
}

/*******************************************************************************************
*
* Function Name    : COSACM_GetDOCSISInfo
* Description      : This function will retrieve the DOCSIS information
*
* @param [in]  req - handleType : Holds the message bus handle
* @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
* @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
*******************************************************************************************/

void CosaCM::COSACM_GetDOCSISInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDOCSISInfo --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();

    returnValue = ssp_cosacm_GetDOCSISInfo(handleType,bufferType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the DOCSIS information";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the DOCSIS information";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDOCSISInfo --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDOCSISInfo  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : COSACM_GetLog
 * Description      : This function will retrieve the Log information
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::COSACM_GetLog(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetLog --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();
    returnValue = ssp_cosacm_GetLog(handleType,bufferType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the Log information";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the Log information";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetLog --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetLog  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : COSACM_SetLog
 * Description      : This function will set the log information
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::COSACM_SetLog(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_SetLog --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();

    returnValue = ssp_cosacm_SetLog(handleType,bufferType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully set the log information";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set the log information";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_SetLog --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_SetLog  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : COSACM_GetDocsisLog
 * Description      : This function will get the DOCSIS log information
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::COSACM_GetDocsisLog(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDocsisLog --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;
    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();

    returnValue = ssp_cosacm_GetDocsisLog(handleType,bufferType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the DOCSIS Log information";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the DOCSIS Log information";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDocsisLog --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDocsisLog  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : COSACM_GetDownstreamChannel
 * Description      : This function will get the Downstream channel information
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::COSACM_GetDownstreamChannel(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDownstreamChannel --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();
    printf("handleType %d\nbufferType %d\n",handleType,bufferType);

    returnValue = ssp_cosacm_GetDownstreamChannel(handleType,bufferType);
    printf("return value is %d\n",returnValue);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the Downstream channel information";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the Downstream channel information";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDownstreamChannel --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetDownstreamChannel  --->Exit\n");
    return;
}
/*******************************************************************************************
 *
 * Function Name    : COSACM_GetUpstreamChannel
 * Description      : This function will get the Upstream channel information
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaCM::COSACM_GetUpstreamChannel(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetUpstreamChannel --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();

    returnValue = ssp_cosacm_GetUpstreamChannel(handleType,bufferType);
    if(0 == returnValue)
    {
        printf("Successfully retrieved the Upstream channel information\n");
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the Upstream channel information";
    }
    else
    {
        printf("Failed to retrieve the Upstream channel information\n");
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the Upstream channel information";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetUpstreamChannel --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_GetUpstreamChannel  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : COSACM_CableModemCreate
 * Description      : This function will execute cable modem create
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::COSACM_CableModemCreate(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_CableModemCreate --->Entry \n");

    int returnValue = 0;
    returnValue = ssp_CosaCableModemCreate();
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully executed Cable Modem Create";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to execute Cable Modem Create";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_CableModemCreate --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_CableModemCreate  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaCableModemInitialize
 * Description      : This function will execute the cable modem initialize

 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::COSACM_CableModemInitialize(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_CableModemInitialize --->Entry \n");

    int returnValue = 0;
    int handleType = 0;

    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    handleType = req["handleType"].asInt();

    returnValue = ssp_CosaCableModemInitialize(handleType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully executed Cable Modem Initialize";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to execute Cable Modem Initialize";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_CableModemInitialize --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_CableModemInitialize  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : COSACM_CableModemRemove
 * Description      : This will execute cable modem remove
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::COSACM_CableModemRemove(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_CableModemRemove  --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    handleType = req["handleType"].asInt();

    returnValue = ssp_CosaCableModemRemove(handleType);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully executed Cable Modem Remove";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to execute Cable Modem Remove";
        DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_CableModemRemove --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n COSACM_CableModemRemove --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CMHal_GetCharValues
 * Description      : This will get the char values
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CMHal_GetCharValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHal_GetCharValues  --->Entry \n");

    int returnValue = 0;
    char paramName[100];
    char Details[64] = {'\0'};
    char value[60];
    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }
    strcpy(paramName,req["paramName"].asCString());

    returnValue = ssp_CMHal_GetCharValues(paramName,value);
    if(0 == returnValue)
    {
       sprintf(Details,"%s", value);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHal_GetCharValues --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHal_GetCharValues --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CMHal_GetUlongValues
 * Description      : This will get the Ulong values
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaCM::CMHal_GetUlongValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHal_GetUlongValues  --->Entry \n");

    int returnValue = 0;
    char paramName[100];
    char Details[64] = {'\0'};
    unsigned long value = 0;
    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }
    strcpy(paramName,req["paramName"].asCString());

    returnValue = ssp_CMHal_GetUlongValues(paramName,&value);
    if(0 == returnValue)
    {
        sprintf(Details,"%d", value);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHal_GetUlongValues --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHal_GetUlongValues --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CMHal_GetStructValues
 * Description      : This function is used to retrieve value of structure
 *
 * @param [in]  req - MethodName : Holds the name of api
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaCM::CMHal_GetStructValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n  CMHal_GetStructValues--->Entry \n");
    int returnValue = 0;
    DOCSIS docsis = {0};
    DS_CHANNEL ds_channel = {0};
    US_CHANNEL us_channel = {0};
    IPV6DHCP ipv6dhcp = {0};
    IPV4DHCP ipv4dhcp = {0};
    char value[400];
    char Details[200]= {'\0'};
    char paramName[100] = {'\0'};
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }
    strcpy(paramName,req["paramName"].asCString());
    printf("paramName received as %s\n", paramName);
    /* Invoke the wrapper function to get the config */
    if( !(strcmp(paramName, "version")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,&docsis);
        if(0 == returnValue)
        {
        sprintf(Details,"%s",docsis.version);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else if( !(strcmp(paramName, "ConfigFileName")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,&docsis);
        if(0 == returnValue)
        {
        sprintf(Details,"%s",docsis.ConfigFileName);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else if( !(strcmp(paramName, "Ipv6DhcpBootFileName")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,&ipv6dhcp);
        if(0 == returnValue)
        {
        sprintf(Details,"%s",ipv6dhcp.IPv6BootFileName);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else if( !(strcmp(paramName, "Ipv4DhcpBootFileName")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,&ipv4dhcp);
        if(0 == returnValue)
        {
        sprintf(Details,"%s",ipv4dhcp.BootFileName);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else if( !(strcmp(paramName, "Ipv6DhcpIPAddress")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,&ipv6dhcp);
        if(0 == returnValue)
        {
        sprintf(Details,"%s",ipv6dhcp.IPv6Address);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else if( !(strcmp(paramName, "Ipv4DhcpIPAddress")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,&ipv4dhcp);
        if(0 == returnValue)
        {
        sprintf(Details,"%s",ipv4dhcp.IPAddress);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else if( !(strcmp(paramName, "DS_Frequency")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,value);
        if(0 == returnValue)
        {
	sprintf(Details,"%s", value);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else if( !(strcmp(paramName, "US_Frequency")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,value);
        if(0 == returnValue)
        {
        sprintf(Details,"%s", value);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else if( !(strcmp(paramName, "ModulationAndSNRLevel")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,value);
        if(0 == returnValue)
        {
        sprintf(Details,"%s", value);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else if( !(strcmp(paramName, "DS_DataRate")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,&docsis);
        if(0 == returnValue)
        {
        sprintf(Details,"%s",docsis.DownstreamDataRate);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else if( !(strcmp(paramName, "US_DataRate")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,&docsis);
        if(0 == returnValue)
        {
        sprintf(Details,"%s",docsis.UpstreamDataRate);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else if( !(strcmp(paramName, "LockStatusAndChannelID")) )
    {
        returnValue = ssp_CMHal_GetStructValues(paramName,value);
        if(0 == returnValue)
        {
        sprintf(Details,"%s", value);
        response["result"]="SUCCESS";
        response["details"]=Details;
        }
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="invalid parameter as input argument";
	return;
    }
    if (0 != returnValue)
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the value";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHal_GetStructValues --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHal_GetStructValues --->Exit\n");
    return;
}
/**************************************************************************
 * Function Name	: CreateObject
 * Description	: This function will be used to create a new object for the
 *	                class "CosaCM".
 *
 **************************************************************************/

extern "C" CosaCM* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new CosaCM(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/

bool CosaCM::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"CosaCM shutting down\n");
    return TEST_SUCCESS;
}

/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(CosaCM *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying CosaCM object\n");
    delete stubobj;
}

