/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
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

#include "EPONHAL.h"

/********************************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for registering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return string "SUCCESS" in case of success else return string "FAILURE"
 **********************************************************************************************/
std::string EPONHAL::testmodulepre_requisites()
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
bool EPONHAL::testmodulepost_requisites()
{
        /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
        return TEST_SUCCESS;
}

/***************************************************************************************
 *Function name :  EPONHAL::initialize
 *Description   : This function is used to register all the epon_hal methods.
 *param [in]    : szVersion - version, ptrAgentObj - Agent obhect
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE
 ***************************************************************************************/
bool EPONHAL::initialize(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "EPONHAL Initialize----->Entry\n");
        return TEST_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name : EPONHAL_GetParamUlongValue
 * Description   : This will get the Ulong values
 * @param [in]   : req - paramName : Holds the name of api
 *                 req - paramType : NULL value indicates negative test
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
*
 *******************************************************************************************/
void EPONHAL::EPONHAL_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetParamUlongValue ---> Entry \n");
    int returnValue = 0;
    char paramName[100] = {'\0'};
    char Details[100] = {'\0'};
    unsigned long value = 0;
    char paramType[10] = {'\0'};


    /* Validate the input arguments */
    if(&req["paramName"]==NULL || &req["paramType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(paramName,req["paramName"].asCString());
    strcpy(paramType, req["paramType"].asCString());

    if(strcmp(paramType, "NULL"))
    {
        returnValue = ssp_EPONHAL_GetParamUlongValue(paramName,&value);
    }
    else
    {
        returnValue = ssp_EPONHAL_GetParamUlongValue(paramName,NULL);
    }

    if(0 == returnValue)
    {
        sprintf(Details,"%lu", value);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
        DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetParamUlongValue ---> Exit\n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetParamUlongValue ---> Exit\n");
    return;
}
/*******************************************************************************************
 *
 * Function Name        : EPONHAL_GetFirmwareInfo
 * Description          : This function invokes EPON  hal api dpoe_getFirmwareInfo()
 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void EPONHAL::EPONHAL_GetFirmwareInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetFirmwareInfo----->Entry\n");
    int returnValue;
    char details[200] = {'\0'};
    dpoe_firmware_info_t pFirmwareInfo;
    returnValue = ssp_EPONHAL_GetFirmwareInfo(&pFirmwareInfo);
    if(0 == returnValue)
       {
            sprintf(details, "Value returned is : info_bootVersion : %d,info_bootCrc32 :%lu,info_appVersion :%d ,info_appCrc32 : %lu",pFirmwareInfo.info_bootVersion,pFirmwareInfo.info_bootCrc32,pFirmwareInfo.info_appVersion,pFirmwareInfo.info_appCrc32);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
    else
       {
            sprintf(details, "EPONHAL_GetFirmwareInfo failure");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
       }
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetFirmwareInfo --->Exit\n");
}



/*******************************************************************************************
 *
 * Function Name        : EPON_GetEponChipInfo
 * Description          : This function invokes EPON  hal api dpoe_getEponChipInfo()
 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void EPONHAL::EPONHAL_GetEponChipInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPON_GetEponChipInfo----->Entry\n");
    int returnValue;
    char details[200] = {'\0'};
    dpoe_epon_chip_info_t pEponChipInfo;
    returnValue = ssp_EPONHAL_GetEponChipInfo(& pEponChipInfo);
    if(0 == returnValue)
       {
            sprintf(details, "Value returned is : info_JedecId :%d ,info_ChipModel :%lu,info_ChipVersion :%lu",pEponChipInfo.info_JedecId,pEponChipInfo.info_ChipModel,pEponChipInfo.info_ChipVersion);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
    else
       {
            sprintf(details, "EPONHAL_GetEponChipInfo failure");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
       }
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetEponChipInfo --->Exit\n");
}


/*******************************************************************************************
 *
 * Function Name        : EPON_GetManufacturerInfo
 * Description          : This function invokes EPON  hal api dpoe_getManufacturerInfo()
 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void EPONHAL::EPONHAL_GetManufacturerInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPON_GetManufacturerInfo----->Entry\n");
    int returnValue;
    char details[200] = {'\0'};
    dpoe_manufacturer_t pManufacturerInfo;
    returnValue = ssp_EPONHAL_GetManufacturerInfo(&pManufacturerInfo);
    if(0 == returnValue)
       {
            sprintf(details, "Value returned is : manufacturer_Info :%s ,manufacturer_OrganizationName :%s",pManufacturerInfo.manufacturer_Info,pManufacturerInfo.manufacturer_OrganizationName );
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
    else
       {
            sprintf(details, "EPONHAL_GetManufacturerInfo  failure");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
       }
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetManufacturerInfo --->Exit\n");
}



/*****************************************************************************************************
 *Function name : EPONHAL_GetOnuId
 *Description   : This function will invoke the SSP  HAL wrapper to get the ONU ID
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *******************************************************************************************************/
void EPONHAL::EPONHAL_GetOnuId(IN const Json::Value& req, OUT Json::Value& response)
{

    char macAddress[18] = {0};

    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetOnuId ---> Entry \n");

    if(ssp_EPONHAL_GetOnuId(macAddress) == 0)
    {
        DEBUG_PRINT(DEBUG_TRACE, "Successfully retrieved the ONUID MAC as %s\n", macAddress);
        response["result"] = "SUCCESS";
        response["details"] = macAddress;
        return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "EPONHAL_GetOnuId failed.Please check logs";
        DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetOnuId failed. EPONHAL_GetOnuId ---> Exit\n");
        return;
    }
}

/*****************************************************************************************************
 *Function name : EPONHAL_GetMaxLogicalLinks
 *Description   : This function will invoke the SSP  HAL wrapper to get the MaxLogicalLinks
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *******************************************************************************************************/
void EPONHAL::EPONHAL_GetMaxLogicalLinks(IN const Json::Value& req, OUT Json::Value& response)
{
    char details[120] = {'\0'};
    dpoe_onu_max_logical_links_t maxLogicalLinks;

    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetMaxLogicalLinks ---> Entry \n");

    if(ssp_EPONHAL_GetMaxLogicalLinks(&maxLogicalLinks) == 0)
    {
        sprintf(details, "lnks_bidirectional: %u, links_downstreamonly: %u", maxLogicalLinks.links_bidirectional, maxLogicalLinks.links_downstreamonly);
        DEBUG_PRINT(DEBUG_TRACE, "Successfully retrieved the maxLogicalLinks as %s: \n", details);
        response["result"] = "SUCCESS";
        response["details"] = details;
        return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "EPONHAL_GetMaxLogicalLinks failed.Please check logs";
        DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetMaxLogicalLinks failed. EPONHAL_GetMaxLogicalLinks ---> Exit\n");
        return;
    }
}

/*****************************************************************************************************
 *Function name : EPONHAL_DeviceSysDescrInfo
 *Description   : This function will invoke the SSP  HAL wrapper to get the DeviceSysDescrInfo
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *******************************************************************************************************/
void EPONHAL::EPONHAL_GetDeviceSysDescrInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    char details[120] = {'\0'};
    dpoe_device_sys_descr_info_t devSysDescrInfo;

    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_DeviceSysDescrInfo ---> Entry \n");

    if(ssp_EPONHAL_GetDeviceSysDescrInfo(&devSysDescrInfo) == 0)
    {
        sprintf(details, "VendorName: %s, ModelNumber: %s, HardwareVersion: %s", devSysDescrInfo.info_VendorName, devSysDescrInfo.info_ModelNumber, devSysDescrInfo.info_HardwareVersion);
        DEBUG_PRINT(DEBUG_TRACE, "Successfully retrieved the DeviceSysDescrInfo as %s: \n", details);
        response["result"] = "SUCCESS";
        response["details"] = details;
        return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "EPONHAL_GetDeviceSysDescrInfo failed.Please check logs";
        DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetDeviceSysDescrInfo failed. EPONHAL_GetGetDeviceSysDescrInfo ---> Exit\n");
        return;
    }
}

/***************************************************************************************************
 *Function Name   : CreateObject
 *Description     : This function is used to create a new object of the class "EPONHAL".
 *@param [in]     : None
 ***************************************************************************************************/
extern "C" EPONHAL* CreateObject(TcpSocketServer &ptrtcpServer)
{
        return new EPONHAL(ptrtcpServer);
}

/*************************************************************************************
 *Function Name : cleanup
 *Description   : This function will be used to the close things cleanly.
 *@param [in]   : szVersion - version, ptrAgentObj - Agent object
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
bool EPONHAL::cleanup(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "cleaning up\n");
        return TEST_SUCCESS;
}

/**********************************************************************************
 *Function Name : DestroyObject
 *Description   : This function will be used to destroy the EPONHAL object.
 *@param [in]   : Input argument is EPONHAL Object
 **********************************************************************************/
extern "C" void DestroyObject(EPONHAL *stubobj)
{
        DEBUG_PRINT(DEBUG_TRACE, "Destroying EPONHAL object\n");
        delete stubobj;
}

/*******************************************************************************************
 *
 * Function Name        : EPON_GetOnuPacketBufferCapabilities
 * Description          : This function invokes EPON  hal api dpoe_getOnuPacketBufferCapabilities()
 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void EPONHAL::EPONHAL_GetOnuPacketBufferCapabilities(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetOnuPacketBufferCapabilities----->Entry\n");
    int returnValue = 0;
    char details[200] = {'\0'};
    dpoe_onu_packet_buffer_capabilities_t pCapabilities;
    returnValue = ssp_EPONHAL_GetOnuPacketBufferCapabilities(&pCapabilities);
    if(0 == returnValue)
       {
            sprintf(details, "Value returned is : UpstreamQueues:%c ,UpQueuesMaxPerLink:%c ,UpQueueIncrement:%c ,DownstreamQueues: %c,DnQueuesMaxPerPort:%c ,DnQueueIncrement: %c ,TotalPacketBuffer: %d , UpPacketBuffer: %d ,DnPacketBuffer: %d ",pCapabilities.capabilities_UpstreamQueues,pCapabilities.capabilities_UpQueuesMaxPerLink,pCapabilities.capabilities_UpQueueIncrement,pCapabilities.capabilities_DownstreamQueues,pCapabilities.capabilities_DnQueuesMaxPerPort,pCapabilities.capabilities_DnQueueIncrement,pCapabilities.capabilities_TotalPacketBuffer,pCapabilities.capabilities_UpPacketBuffer,pCapabilities.capabilities_DnPacketBuffer );
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
    else
       {
            sprintf(details, "EPONHAL_GetOnuPacketBufferCapabilities failure");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
       }
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetOnuPacketBufferCapabilities --->Exit\n");
}

