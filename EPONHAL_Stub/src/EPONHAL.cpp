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
#define Dummy 500
#define MAX_STRING_SIZE 1024
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
        DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetParamUlongValue() %s NULL buffer validation\n", paramName);
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
        DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetParamUlongValue Failed\n");
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
    char details[582] = {'\0'};
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
    char details[152] = {'\0'};
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
 * Description          : This function invokes EPON wrapper ssp_EPONHAL_GetOnuPacketBufferCapabilities
 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void EPONHAL::EPONHAL_GetOnuPacketBufferCapabilities(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetOnuPacketBufferCapabilities----->Entry\n");
    int returnValue;
    char details[205] = {'\0'};
    dpoe_onu_packet_buffer_capabilities_t pCapabilities;
    unsigned long UpstreamQueues = 0,UpQueuesMaxPerLink =0,UpQueueIncrement =0,DownstreamQueues =0,DnQueuesMaxPerPort =0,DnQueueIncrement =0;
    returnValue = ssp_EPONHAL_GetOnuPacketBufferCapabilities(&pCapabilities);
    UpstreamQueues = (unsigned long)pCapabilities.capabilities_UpstreamQueues;
    UpQueuesMaxPerLink = (unsigned long)pCapabilities.capabilities_UpQueuesMaxPerLink;
    UpQueueIncrement = (unsigned long)pCapabilities.capabilities_UpQueueIncrement;
    DownstreamQueues = (unsigned long)pCapabilities.capabilities_DownstreamQueues;
    DnQueuesMaxPerPort = (unsigned long)pCapabilities.capabilities_DnQueuesMaxPerPort;
    DnQueueIncrement = (unsigned long)pCapabilities.capabilities_DnQueueIncrement;
    if(0 == returnValue)
       {
            sprintf(details, "Value returned is : UpstreamQueues: %lu,UpQueuesMaxPerLink:%lu ,UpQueueIncrement:%lu ,DownstreamQueues: %lu,DnQueuesMaxPerPort:%lu ,DnQueueIncrement: %lu ,TotalPacketBuffer: %d , UpPacketBuffer: %d",UpstreamQueues,UpQueuesMaxPerLink,UpQueueIncrement,DownstreamQueues,DnQueuesMaxPerPort,DnQueueIncrement,pCapabilities.capabilities_TotalPacketBuffer,pCapabilities.capabilities_UpPacketBuffer);
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

/*******************************************************************************************
 *
 * Function Name        : EPONHAL_GetLlidForwardingState
 * Description          : This function invokes epon wrapper ssp_EPONHAL_GetLlidForwardingState
 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
** *******************************************************************************************/
void EPONHAL::EPONHAL_GetLlidForwardingState(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetLlidForwardingState----->Entry\n");
    int returnValue = 0, loop= 0,num = 0,count = 1;
    char details[2000] = {'\0'};
    unsigned short numEntries =0;
    numEntries  = req["numEntries"].asInt();
    num = int(numEntries);
    dpoe_link_forwarding_state_t linkForwardingState[num];
    for (loop = 0; loop< num;loop++)
    {
      linkForwardingState[loop].link_Id = count++;
    }

    returnValue = ssp_EPONHAL_GetLlidForwardingState(linkForwardingState,numEntries);
    printf("\n return value:%d \n",returnValue);
    printf("\n numEntries : %d \n",num);
    if(0 == returnValue)
    {
            if ( num > 0)
            {
               for( loop = 0; loop < num;loop++)
               {
                 sprintf(details + strlen(details),"ForwardingState %d : %d ,",loop+1,linkForwardingState[loop].link_ForwardingState);
                 printf("\nForwardingState %d : %d ",loop,linkForwardingState[loop].link_ForwardingState);
               }
               response["result"]="SUCCESS";
               response["details"]=details;
               return;
            }
            else
            {
               sprintf(details, "EPONHAL_GetLlidForwardingState has not entries --> failure");
               response["result"]="FAILURE";
               response["details"]=details;
               return;
            }

    }
    else
    {
       sprintf(details, "EPONHAL_GetLlidForwardingState  failure");
       response["result"]="FAILURE";
       response["details"]=details;
       return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetLlidForwardingState --->Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : EPONHAL_GetOamFrameRate
 * Description          : This function invokes epon wrapper ssp_EPONHAL_GetOamFrameRate
 * @param [in] req-     : NILL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
** *******************************************************************************************/
void EPONHAL::EPONHAL_GetOamFrameRate(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetOamFrameRate----->Entry\n");
    int returnValue = 0,loop = 0,num = 0,count =1;
    char details[1024] = {'\0'};
    unsigned short numEntries = 0;
    numEntries  = req["numEntries"].asInt();
    num = int(numEntries);
    dpoe_link_oam_frame_rate_t linkOamFrameRate[num];
    for (loop = 0; loop< num;loop++)
    {
      linkOamFrameRate[loop].link_Id = count++;
    }
    returnValue = ssp_EPONHAL_GetOamFrameRate(linkOamFrameRate,numEntries);
    printf("\n return value:%d \n",returnValue);
    printf("\n numEntries : %d \n",num);
    if(0 == returnValue)
    {
            if ( num > 0)
            {
               for( loop = 0; loop < num ;loop++)
               {
                 if (strlen(details) < 512)
                 {
                  sprintf( details + strlen(details),",MaxRate %d : %d ,MinRate %d :%d",loop+1,linkOamFrameRate[loop].link_MaxRate,loop+1,linkOamFrameRate[loop].link_MinRate);
                 }
                 else break;
                 printf("\n link_MaxRate %d : %d",loop+1,linkOamFrameRate[loop].link_MaxRate);
                 printf("\n link_MinRate %d : %d",loop+1,linkOamFrameRate[loop].link_MinRate);
               }
               response["result"]="SUCCESS";
               response["details"]=details;
               return;
            }
            else
            {
               sprintf(details, "EPONHAL_GetOamFrameRate has no entries --> failure");
               response["result"]="FAILURE";
               response["details"]=details;
               return;
            }

    }
    else
    {
       sprintf(details, "EPONHAL_GetOamFrameRate  failure");
       response["result"]="FAILURE";
       response["details"]=details;
       return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetOamFrameRate --->Exit\n");
}
 /*******************************************************************************************
 *
 * Function Name        : EPONHAL_GetDynamicMacTable
 * Description          : This function invokes epon wrapper ssp_EPONHAL_GetDynamicMacTable
 * @param [in] req-     : NILL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
** *******************************************************************************************/
void EPONHAL::EPONHAL_GetDynamicMacTable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetDynamicMacTable----->Entry\n");
    int returnValue = 0,loop = 0,num = 0;
    char details[2000] = {'\0'};
    unsigned short numEntries = 0;
    numEntries  = req["numEntries"].asInt();
    num= int(numEntries);
    dpoe_link_mac_address_t linkDynamicMacTable[num];
    returnValue = ssp_EPONHAL_GetDynamicMacTable(linkDynamicMacTable,numEntries);
    printf("\n return value:%d \n",returnValue);
    printf("\n numEntries : %d \n",num);
    num  = int(linkDynamicMacTable ->numEntries);
    printf("\n linkDynamicMacTable ->numEntries : %d \n",num);
    if(0 == returnValue)
    {
            if ( num > 0)
            {
               for( loop = 0; loop < num ;loop++)
               {
                 if (strlen(details) < 512)
                 {
                   sprintf(details + strlen(details),"MAC %d: %x %x %x %x %x %x",loop+1,linkDynamicMacTable[loop].pMacAddress->macAddress[0],linkDynamicMacTable[loop].pMacAddress->macAddress[1],linkDynamicMacTable[loop].pMacAddress->macAddress[2],linkDynamicMacTable[loop].pMacAddress->macAddress[3],linkDynamicMacTable[loop].pMacAddress->macAddress[4],linkDynamicMacTable[loop].pMacAddress->macAddress[5]);
                 }
                else break;
               }
               response["result"]="SUCCESS";
               response["details"]=details;
               return;
            }
            else
            {
               sprintf(details, "EPONHAL_GetDynamicMacTable has not entries");
               response["result"]="FAILURE";
               response["details"]=details;
               return;
            }

    }
    else
    {
       sprintf(details, "EPONHAL_GetDynamicMacTable failure");
       response["result"]="FAILURE";
       response["details"]=details;
       return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetDynamicMacTable --->Exit\n");
}
/*******************************************************************************************
 *
 * Function Name        : EPONHAL_GetOnuLinkStatistics
 * Description          : This function invokes epon wrapper ssp_EPONHAL_GetOnuLinkStatistics
 * @param [in] req-     : NILL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
** *******************************************************************************************/
void EPONHAL::EPONHAL_GetOnuLinkStatistics(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetOnuLinkStatistics----->Entry\n");
    int returnValue = -1,loop = 0,count =1;
    char details[2000] = {'\0'};
    unsigned short *numEntries = NULL,num = 0;
    num = req["numEntries"].asInt();
    numEntries = &num;
    dpoe_link_traffic_stats_t onuLinkTrafficStats = {0};
    dpoe_link_traffic_stats_t *ptronuLinkTrafficStats = NULL;
    //for min logical link
    if (num != Dummy)
    {
       onuLinkTrafficStats.link_Id = count;
       returnValue = ssp_EPONHAL_GetOnuLinkStatistics(&onuLinkTrafficStats,numEntries);
       printf("\n return value:%d \n",returnValue);
       printf("\n numEntries : %d \n",num);
       if(0 == returnValue)
       {
                 printf("\nRxUnicastFrames : %llu",onuLinkTrafficStats.link_TrafficStats.port_RxUnicastFrames);
                 printf("\nTxUnicastFrames : %llu",onuLinkTrafficStats.link_TrafficStats.port_TxUnicastFrames);
                 printf("\nRxFrameTooShort  : %llu",onuLinkTrafficStats.link_TrafficStats.port_RxFrameTooShort);
                 printf("\nRxFrame64  : %llu",onuLinkTrafficStats.link_TrafficStats.port_RxFrame64);
                 printf("\n RxFrame65_127 : %llu",onuLinkTrafficStats.link_TrafficStats.port_RxFrame65_127);
                 printf("\nRxFrame128_255  : %llu",onuLinkTrafficStats.link_TrafficStats.port_RxFrame128_255);
                 printf("\nRxFrame256_511  : %llu",onuLinkTrafficStats.link_TrafficStats.port_RxFrame256_511);
                 printf("\nRxFrame512_1023  : %llu",onuLinkTrafficStats.link_TrafficStats.port_RxFrame512_1023);
                 printf("\nRxFrame1024_1518  : %llu",onuLinkTrafficStats.link_TrafficStats.port_RxFrame1024_1518);
                 printf("\nRxFrame1519_Plus  : %llu",onuLinkTrafficStats.link_TrafficStats.port_RxFrame1519_Plus);
                 printf("\nTxFrame64  : %llu",onuLinkTrafficStats.link_TrafficStats.port_TxFrame64);
                 printf("\nTxFrame65_127  : %llu",onuLinkTrafficStats.link_TrafficStats.port_TxFrame65_127);
                 printf("\nTxFrame128_255  : %llu",onuLinkTrafficStats.link_TrafficStats.port_TxFrame128_255);
                 printf("\nTxFrame256_511  : %llu",onuLinkTrafficStats.link_TrafficStats.port_TxFrame256_511);
                 printf("\nTxFrame512_1023 : %llu",onuLinkTrafficStats.link_TrafficStats.port_TxFrame512_1023);
                 printf("\nRxFrame1024_1518: %llu",onuLinkTrafficStats.link_TrafficStats.port_TxFrame_1024_1518);
                 printf("\nTxFrame_1519_Plus: %llu",onuLinkTrafficStats.link_TrafficStats.port_TxFrame_1519_Plus);
                 printf("\nFramesDropped : %llu",onuLinkTrafficStats.link_TrafficStats.port_FramesDropped);
                 printf("\nBytesDropped : %llu",onuLinkTrafficStats.link_TrafficStats.port_BytesDropped);
                 printf("\nOpticalMonVcc : %d",onuLinkTrafficStats.link_TrafficStats.port_OpticalMonVcc);
                 printf("\nOpticalMonTxBiasCurrent: %d",onuLinkTrafficStats.link_TrafficStats.port_OpticalMonTxBiasCurrent);
                 printf("\nOpticalMonTxPower: %d",onuLinkTrafficStats.link_TrafficStats.port_OpticalMonTxPower);
                 printf("\nOpticalMonRxPower: %d",onuLinkTrafficStats.link_TrafficStats.port_OpticalMonRxPower);


                sprintf(details," Value returned is : RxUnicastFrames: %llu,TxUnicastFrames :%llu,RxFrameTooShort : %llu,RxFrame64 :%llu,RxFrame65_127: %llu,RxFrame128_255:%llu,RxFrame256_511:%llu,RxFrame512_1023 :%llu,RxFrame1024_1518 :%llu,RxFrame1519_Plus :%llu,TxFrame64 :%llu,TxFrame65_127:%llu,TxFrame128_255:%llu,TxFrame256_511:%llu,TxFrame512_1023 :%llu,TxFrame_1024_1518:%llu,TxFrame_1519_Plus :%llu,FramesDropped:%llu,BytesDropped:%llu,OpticalMonVcc:%d,OpticalMonTxBiasCurrent:%d,OpticalMonTxPower:%d,OpticalMonRxPower:%d",onuLinkTrafficStats.link_TrafficStats.port_RxUnicastFrames,onuLinkTrafficStats.link_TrafficStats.port_TxUnicastFrames,onuLinkTrafficStats.link_TrafficStats.port_RxFrameTooShort,onuLinkTrafficStats.link_TrafficStats.port_RxFrame64,onuLinkTrafficStats.link_TrafficStats.port_RxFrame65_127,onuLinkTrafficStats.link_TrafficStats.port_RxFrame128_255,onuLinkTrafficStats.link_TrafficStats.port_RxFrame256_511,onuLinkTrafficStats.link_TrafficStats.port_RxFrame512_1023,onuLinkTrafficStats.link_TrafficStats.port_RxFrame1024_1518,onuLinkTrafficStats.link_TrafficStats.port_RxFrame1519_Plus, onuLinkTrafficStats.link_TrafficStats.port_TxFrame64,onuLinkTrafficStats.link_TrafficStats.port_TxFrame65_127,onuLinkTrafficStats.link_TrafficStats.port_TxFrame128_255,onuLinkTrafficStats.link_TrafficStats.port_TxFrame256_511,onuLinkTrafficStats.link_TrafficStats.port_TxFrame512_1023,onuLinkTrafficStats.link_TrafficStats.port_TxFrame_1024_1518,onuLinkTrafficStats.link_TrafficStats.port_TxFrame_1519_Plus,onuLinkTrafficStats.link_TrafficStats.port_FramesDropped,onuLinkTrafficStats.link_TrafficStats.port_BytesDropped, onuLinkTrafficStats.link_TrafficStats.port_OpticalMonVcc,onuLinkTrafficStats.link_TrafficStats.port_OpticalMonTxBiasCurrent,onuLinkTrafficStats.link_TrafficStats.port_OpticalMonTxPower, onuLinkTrafficStats.link_TrafficStats.port_OpticalMonRxPower);
               response["result"]="SUCCESS";
               response["details"]=details;
               return;

    }
    else
    {
      sprintf(details, "EPONHAL_GetOnuLinkStatistics failure");
      response["result"]="FAILURE";
      response["details"]=details;
      return;
    }
 }
 else
 {
   //for max logical link
   returnValue = ssp_EPONHAL_GetOnuLinkStatistics(ptronuLinkTrafficStats,numEntries);
   num = int(*numEntries);
   printf("\n return value:%d \n",returnValue);
   printf("\n numEntries : %d \n",num) ;
   if (0 == returnValue)
   {
      for( loop = 0; loop < num ;loop++)
      {
        printf("\nRxUnicastFrames %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_RxUnicastFrames);
        printf("\nTxUnicastFrames %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_TxUnicastFrames);
        printf("\nRxFrameTooShort %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_RxFrameTooShort);
        printf("\nRxFrame64 %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_RxFrame64);
        printf("\n RxFrame65_127%d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_RxFrame65_127);
        printf("\nRxFrame128_255 %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_RxFrame128_255);
        printf("\nRxFrame256_511 %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_RxFrame256_511);
        printf("\nRxFrame512_1023 %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_RxFrame512_1023);
        printf("\nRxFrame1024_1518 %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_RxFrame1024_1518);
        printf("\nRxFrame1519_Plus %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_RxFrame1519_Plus);
        printf("\nTxFrame64 %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_TxFrame64);
        printf("\nTxFrame65_127 %d : %llu",loop+1, ptronuLinkTrafficStats[loop].link_TrafficStats.port_TxFrame65_127);
        printf("\nTxFrame128_255 %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_TxFrame128_255);
        printf("\nTxFrame256_511 %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_TxFrame256_511);
        printf("\nTxFrame512_1023 %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_TxFrame512_1023);
        printf("\nRxFrame1024_1518 %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_TxFrame_1024_1518);
        printf("\nTxFrame_1519_Plus %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_TxFrame_1519_Plus);
        printf("\nFramesDropped %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_FramesDropped);
        printf("\nBytesDropped %d : %llu",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_BytesDropped);
        printf("\nOpticalMonVcc %d : %d",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_OpticalMonVcc);
        printf("\nOpticalMonTxBiasCurrent %d : %d",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_OpticalMonTxBiasCurrent);
        printf("\nOpticalMonTxPower %d : %d",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_OpticalMonTxPower);
        printf("\nOpticalMonRxPower %d : %d",loop+1,ptronuLinkTrafficStats[loop].link_TrafficStats.port_OpticalMonRxPower);

      }
      sprintf(details," Value returned is : RxUnicastFrames: %llu,TxUnicastFrames :%llu,RxFrameTooShort : %llu,RxFrame64 :%llu,RxFrame65_127: %llu,RxFrame128_255:%llu,RxFrame256_511:%llu,RxFrame512_1023 :%llu,RxFrame1024_1518 :%llu,RxFrame1519_Plus :%llu,TxFrame64 :%llu,TxFrame65_127:%llu,TxFrame128_255:%llu,TxFrame256_511:%llu,TxFrame512_1023 :%llu,TxFrame_1024_1518:%llu,TxFrame_1519_Plus :%llu,FramesDropped:%llu,BytesDropped:%llu,OpticalMonVcc:%d,OpticalMonTxBiasCurrent:%d,OpticalMonTxPower:%d,OpticalMonRxPower:%d",ptronuLinkTrafficStats[0].link_TrafficStats.port_RxUnicastFrames,ptronuLinkTrafficStats[0].link_TrafficStats.port_TxUnicastFrames,ptronuLinkTrafficStats[0].link_TrafficStats.port_RxFrameTooShort,ptronuLinkTrafficStats[0].link_TrafficStats.port_RxFrame64,ptronuLinkTrafficStats[0].link_TrafficStats.port_RxFrame65_127,ptronuLinkTrafficStats[0].link_TrafficStats.port_RxFrame128_255,ptronuLinkTrafficStats[0].link_TrafficStats.port_RxFrame256_511,ptronuLinkTrafficStats[0].link_TrafficStats.port_RxFrame512_1023,ptronuLinkTrafficStats[0].link_TrafficStats.port_RxFrame1024_1518,ptronuLinkTrafficStats[0].link_TrafficStats.port_RxFrame1519_Plus, ptronuLinkTrafficStats[0].link_TrafficStats.port_TxFrame64,ptronuLinkTrafficStats[0].link_TrafficStats.port_TxFrame65_127,ptronuLinkTrafficStats[0].link_TrafficStats.port_TxFrame128_255,ptronuLinkTrafficStats[0].link_TrafficStats.port_TxFrame256_511,ptronuLinkTrafficStats[0].link_TrafficStats.port_TxFrame512_1023,ptronuLinkTrafficStats[0].link_TrafficStats.port_TxFrame_1024_1518,ptronuLinkTrafficStats[0].link_TrafficStats.port_TxFrame_1519_Plus,ptronuLinkTrafficStats[0].link_TrafficStats.port_FramesDropped,ptronuLinkTrafficStats[0].link_TrafficStats.port_BytesDropped, ptronuLinkTrafficStats[0].link_TrafficStats.port_OpticalMonVcc,ptronuLinkTrafficStats[0].link_TrafficStats.port_OpticalMonTxBiasCurrent,ptronuLinkTrafficStats[0].link_TrafficStats.port_OpticalMonTxPower, ptronuLinkTrafficStats[0].link_TrafficStats.port_OpticalMonRxPower);

      response["result"]="SUCCESS";
      response["details"]=details;
      free(ptronuLinkTrafficStats);
      return;
    }
    else
    {
       sprintf(details, "EPONHAL_GetOnuLinkStatistics  failure");
       response["result"]="FAILURE";
       response["details"]=details;
       free(ptronuLinkTrafficStats);
       return;
    }
  }
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetOnuLinkStatistics --->Exit\n");
}

 /*******************************************************************************************
 *
 * Function Name        : EPONHAL_GetStaticMacTable
 * Description          : This function invokes epon wrapper ssp_EPONHAL_GetStaticMacTable
 * @param [in] req-     : numEntries - no: of entries in StaticMacTable
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
** *******************************************************************************************/
void EPONHAL::EPONHAL_GetStaticMacTable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetStaticMacTable----->Entry\n");
    int returnValue = 0,loop = 0,num = 0;
    char details[MAX_STRING_SIZE] = {'\0'};
    unsigned short numEntries = 0;
    numEntries  = req["numEntries"].asInt();
    num= int(numEntries);
    dpoe_link_mac_address_t linkStaticMacTable[num];

    //invoke ssp wrapper for dpoe_getStaticMacTable
    returnValue = ssp_EPONHAL_GetStaticMacTable(linkStaticMacTable, numEntries);
    printf("\n dpoe_getStaticMacTable return value:%d \n",returnValue);
    printf("\n dpoe_getStaticMacTable numEntries : %d \n",num);
    num  = int(linkStaticMacTable->numEntries);
    printf("\n linkStaticMacTable->numEntries : %d \n",num);
    if(0 == returnValue)
    {
            if ( num > 0)
            {
               for( loop = 0; loop < num ;loop++)
               {
                 if (strlen(details) < 512)
                 {
                   sprintf(details + strlen(details),"MAC %d: %x %x %x %x %x %x",loop+1,linkStaticMacTable[loop].pMacAddress->macAddress[0],linkStaticMacTable[loop].pMacAddress->macAddress[1],linkStaticMacTable[loop].pMacAddress->macAddress[2],linkStaticMacTable[loop].pMacAddress->macAddress[3],linkStaticMacTable[loop].pMacAddress->macAddress[4],linkStaticMacTable[loop].pMacAddress->macAddress[5]);
                 }
                else break;
               }
               response["result"]="SUCCESS";
               response["details"]=details;
               return;
            }
            else
            {
               sprintf(details, "EPONHAL_GetStaticMacTable has no entries");
               response["result"]="FAILURE";
               response["details"]=details;
               return;
            }
    }
    else
    {
       sprintf(details, "EPONHAL_GetStaticMacTable failure");
       response["result"]="FAILURE";
       response["details"]=details;
       return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetStaticMacTable --->Exit\n");
}

 /*******************************************************************************************
 *
 * Function Name        : EPONHAL_SetClearOnuLinkStatistics
 * Description          : This function invokes epon wrapper ssp_EPONHAL_SetClearOnuLinkStatistics
 * @param [in] req-     : NILL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
** *******************************************************************************************/
void EPONHAL::EPONHAL_SetClearOnuLinkStatistics(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_SetClearOnuLinkStatistics ----->Entry\n");
    int returnValue = 0;

    returnValue = ssp_EPONHAL_SetClearOnuLinkStatistics();
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="EPONHAL_SetClearOnuLinkStatistics api returned success";
    }
    else
    {
       response["result"]="FAILURE";
       response["details"]="EPONHAL_SetClearOnuLinkStatistics api returned failure";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_SetClearOnuLinkStatistics --->Exit\n");
    return;
}


 /*******************************************************************************************
 *
 * Function Name        : EPONHAL_SetResetOnu
 * Description          : This function invokes epon wrapper ssp_EPONHAL_SetResetOnu
 * @param [in] req-     : NILL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
** *******************************************************************************************/
void EPONHAL::EPONHAL_SetResetOnu(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_SetResetOnu ----->Entry\n");
    int returnValue = 0;

    returnValue = ssp_EPONHAL_SetResetOnu();
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="EPONHAL_SetResetOnu api returned success";
    }
    else
    {
       response["result"]="FAILURE";
       response["details"]="EPONHAL_SetResetOnu api returned failure";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_SetResetOnu --->Exit\n");
    return;
}
