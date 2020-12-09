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

#include "ssp_tdk_eponhal_wrp.h"
#include "ssp_hal_logger.h"
#define DummyValue 500
/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetParamUlongValue
 * Description          : This function will invoke the hal api of epon to get the ulong values
 *
 * @param [in]          : paramName: specifies the name of the API
 *                        value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_EPONHAL_GetParamUlongValue(char* paramName, unsigned long* value)
{
    int return_status = RETURN_ERR;
    unsigned short llidEntry = 0;

    DEBUG_PRINT(DEBUG_TRACE,"\n ssp_EPONHAL_GetParamUlongValue ----> Entry\n");

    if( !(strcmp(paramName, "NumberOfNetworkPorts")) )
    {
        return_status = dpoe_getNumberOfNetworkPorts(value);
        DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_getNumberOfNetworkPorts %d", return_status);

        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the EPON NumberOfNetworkPorts\n");
        }
    }
    else if( !(strcmp(paramName, "NumberOfS1Interfaces")) )
    {
        return_status = dpoe_getNumberOfS1Interfaces(value);
        DEBUG_PRINT(DEBUG_TRACE, "Return status of dpoe_getNumberOfS1Interfaces %d", return_status);
        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the Number Of S1 Interfaces\n");
        }
    }
    else if( !(strcmp(paramName, "LlidForwardingStateGetEntryCount")) )
    {
        return_status = dpoe_LlidForwardingStateGetEntryCount(&llidEntry);
        *value = llidEntry;
        DEBUG_PRINT(DEBUG_TRACE, "Return status of dpoe_LlidForwardingStateGetEntryCount %d, llidEntry: %u, output:%lu", return_status, llidEntry, *value);
        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get LlidForwardingStateGetEntryCount\n");
        }
    }
    else if( !(strcmp(paramName, "GetErouterResetCount")) )
    {
       return_status = dpoe_hal_Get_ErouterResetCount(value);
       DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_hal_Get_ErouterResetCount %d,value : %lu", return_status,*value);
       if ( return_status != RETURN_OK)
       {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the Erouter Reset Count \n");
       }
    }
    else if( !(strcmp(paramName, "GetLocalResetCount")) )
    {
       return_status = dpoe_hal_LocalResetCount(value);
       DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_hal_LocalResetCount %d ,value : %lu", return_status,*value);
       if ( return_status != RETURN_OK)
       {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the Local Reset count\n");
       }
    }
    else if( !(strcmp(paramName, "GetEponResetCount")) )
    {
       return_status = dpoe_hal_Get_eponResetCount(value);
       DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_hal_Get_eponResetCount %d,value : %lu", return_status,*value);
       if ( return_status != RETURN_OK)
       {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the Epon Reset count\n");
       }
    }
    else if( !(strcmp(paramName, "OnuLinkStatisticsGetEntryCount")) )
    {
        return_status = dpoe_OnuLinkStatisticsGetEntryCount(&llidEntry);
        *value = llidEntry;
        DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_OnuLinkStatisticsGetEntryCount: %d llidEntry:%u  value:%lu ", return_status,llidEntry, *value);
        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the count of Onu Link Statstics\n");
        }
    }
    else if( !(strcmp(paramName, "OamFrameRateGetEntryCount")) )
    {
        return_status = dpoe_OamFrameRateGetEntryCount(&llidEntry);
        *value = llidEntry;
        DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_OamFrameRateGetEntryCount : %d  llidEntry:%u value:%lu", return_status,llidEntry, *value);
        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the count of  Frame Rate Entry\n");
        }
    }
    else if( !(strcmp(paramName, "getMacLearningAggregateLimit")) )
    {
        return_status = dpoe_getMacLearningAggregateLimit(&llidEntry);
        *value = llidEntry;
        DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_getMacLearningAggregateLimit : %d llidEntry:%u value:%lu", return_status,llidEntry, *value);
        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the count of  Frame Rate Entry\n");
        }
    }
    else if( !(strcmp(paramName, "hal_Reboot_Ready")) )
    {
        return_status = dpoe_hal_Reboot_Ready(value);
        if (value)
             DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_hal_Reboot_Ready  %d,value : %lu\n", return_status,*value);
        else
             DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_hal_Reboot_Ready  %d\n", return_status);
        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the hal_Reboot_Ready status\n");
        }
    }
    else if( !(strcmp(paramName, "DynamicMacAddressAgeLimit")) )
    {
        return_status = dpoe_getDynamicMacAddressAgeLimit(&llidEntry);
        *value = llidEntry;
        DEBUG_PRINT(DEBUG_TRACE, "Return status of dpoe_getDynamicMacAddressAgeLimit %d, llidEntry: %u, output:%lu", return_status, llidEntry, *value);
        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get DynamicMacAddressAgeLimit\n");
        }
    }
    else if( !(strcmp(paramName, "DynamicMacLearningTableSize")) )
    {
        return_status = dpoe_getDynamicMacLearningTableSize(&llidEntry);
        *value = llidEntry;
        DEBUG_PRINT(DEBUG_TRACE, "Return status of dpoe_getDynamicMacLearningTableSize %d, llidEntry: %u, output:%lu", return_status, llidEntry, *value);
        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get dpoe_getDynamicMacLearningTableSize\n");
        }
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR,"Invalid parameter name");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n ssp_EPONHAL_GetParamUlongValue ----> Exit\n");

    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetManufacturerInfo
 * Description          : This function invokes WiFi hal api dpoe_getManufacturerInfo()
 * @param [in]          : NIL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_EPONHAL_GetManufacturerInfo(dpoe_manufacturer_t *pManufacturerInfo)
{
    printf("\n ssp_EPONHAL_GetManufacturerInfo ----> Entry\n");
    int return_status = 0;
    return_status = dpoe_getManufacturerInfo(pManufacturerInfo);
    printf("return value from ssp_EPONHAL_GetManufacturerInfo  is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_EPONHAL_GetManufacturerInfo::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\nssp_EPONHAL_GetManufacturerInfo::Success\n");
     return return_status;
    }
    printf("\n ssp_EPONHAL_GetManufacturerInfo ----> Exit\n");
}


/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetEponChipInfo
 * Description          : This function invokes WiFi hal api dpoe_getEponChipInfo()
 * @param [in]          : NIL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_EPONHAL_GetEponChipInfo(dpoe_epon_chip_info_t *pEponChipInfo)
{
    printf("\n ssp_EPONHAL_GetEponChipInfo----> Entry\n");
    int return_status = 0;
    return_status = dpoe_getEponChipInfo(pEponChipInfo);
    printf("return value from ssp_EPONHAL_GetEponChipInfo  is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_EPONHAL_GetEponChipInfo::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_EPONHAL_GetEponChipInfo::Success\n");
     return return_status;
    }
    printf("\n ssp_EPONHAL_GetEponChipInfo ----> Exit\n");
}



/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetFirmwareInfo
 * Description          : This function invokes WiFi hal api dpoe_getFirmwareInfo()
 * @param [in]          : NIL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_EPONHAL_GetFirmwareInfo(dpoe_firmware_info_t *pFirmwareInfo)
{
    printf("\n ssp_EPONHAL_GetFirmwareInfo----> Entry\n");
    int return_status = 0;
    return_status = dpoe_getFirmwareInfo(pFirmwareInfo);
    printf("return value from ssp_EPONHAL_GetFirmwareInfo  is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_EPONHAL_GetFirmwareInfo::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_EPONHAL_GetFirmwareInfo::Success\n");
     return return_status;
    }
    printf("\n ssp_EPONHAL_GetFirmwareInfo ----> Exit\n");
}


/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetOnuPacketBufferCapabilities
 * Description          : This function invokes WiFi hal api dpoe_getOnuPacketBufferCapabilities()
 * @param [in]          : NIL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_EPONHAL_GetOnuPacketBufferCapabilities(dpoe_onu_packet_buffer_capabilities_t *pCapabilities)
{
    printf("\n ssp_EPONHAL_GetOnuPacketBufferCapabilities----> Entry\n");
    int return_status = 0;
    return_status = dpoe_getOnuPacketBufferCapabilities(pCapabilities);
    printf("return value from ssp_EPONHAL_GetOnuPacketBufferCapabilities  is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_EPONHAL_GetOnuPacketBufferCapabilities::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_EPONHAL_GetOnuPacketBufferCapabilities::Success\n");
     return return_status;
    }
    printf("\n ssp_EPONHAL_GetOnuPacketBufferCapabilities----> Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetOnuId
 * Description          : This function will invoke the hal api dpoe_getOnuId to get the onuid
 *
 * @param [in]          : macAddress : returns the value of onu id mac
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_EPONHAL_GetOnuId(char* macAddress)
{
    int return_status = RETURN_ERR;
    dpoe_mac_address_t dpoe_mac;

    DEBUG_PRINT(DEBUG_TRACE,"\n ssp_EPONHAL_GetOnuId ----> Entry\n");
    CHECK_PARAM_AND_RET(macAddress);

    return_status = dpoe_getOnuId(&dpoe_mac);
    DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_getOnuId %d", return_status);

    if ( return_status == RETURN_OK)
    {
        sprintf(macAddress, "%02x:%02x:%02x:%02x:%02x:%02x",dpoe_mac.macAddress[0], dpoe_mac.macAddress[1], dpoe_mac.macAddress[2], dpoe_mac.macAddress[3], dpoe_mac.macAddress[4],dpoe_mac.macAddress[5]);
        DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetOnuId : Successfully got the ONU ID dpoe_mac.macAddress=%s macAddress=%s\n", dpoe_mac.macAddress, macAddress);
        return return_status;
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the EPON NumberOfNetworkPorts\n");
         return return_status;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetMaxLogicalLinks
 * Description          : This function will invoke the hal api dpoe_getMaxLogicalLinks to get the onuid
 *
 * @param [in]          : pMaxLogicalLinks : buffer to hold the pMaxLogicalLinks values
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_EPONHAL_GetMaxLogicalLinks(dpoe_onu_max_logical_links_t *pMaxLogicalLinks)
{
    int return_status = RETURN_ERR;

    DEBUG_PRINT(DEBUG_TRACE,"\n ssp_EPONHAL_GetMaxLogicalLinks ----> Entry\n");
    CHECK_PARAM_AND_RET(pMaxLogicalLinks);

    return_status = dpoe_getMaxLogicalLinks(pMaxLogicalLinks);
    DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_getMaxLogicalLinks %d", return_status);

    if ( return_status == RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetMaxLogicalLinks : Successfully got the MaxLogicalLinks\n");
        return return_status;
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetMaxLogicalLinks : Failed to get the MaxLogicalLinks\n");
         return return_status;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetDeviceSysDescrInfo
 * Description          : This function will invoke the hal api dpoe_getDeviceSysDescrInfo to get the onuid
 *
 * @param [in]          : pdevSysDescrInfo : buffer to hold the DeviceSysDescrInfo values
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_EPONHAL_GetDeviceSysDescrInfo(dpoe_device_sys_descr_info_t *pdevSysDescrInfo)
{
    int return_status = RETURN_ERR;

    DEBUG_PRINT(DEBUG_TRACE,"\n ssp_EPONHAL_GetDeviceSysDescrInfo ----> Entry\n");
    CHECK_PARAM_AND_RET(pdevSysDescrInfo);

    return_status = dpoe_getDeviceSysDescrInfo(pdevSysDescrInfo);
    DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_getDeviceSysDescrInfo %d", return_status);

    if ( return_status == RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetDeviceSysDescrInfo : Successfully got the DeviceSysDescrInfo\n");
        return return_status;
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetDeviceSysDescrInfo : Failed to get the DeviceSysDescrInfo\n");
         return return_status;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetLlidForwardingState
 * Description          : This function invokes EPON  hal api dpoe_getLlidForwardingState()
 * @param [in]          : NILL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
** ********************************************************************************************/
int ssp_EPONHAL_GetLlidForwardingState(dpoe_link_forwarding_state_t linkForwardingState[], unsigned short numEntries)
{
    printf("\n ssp_EPONHAL_GetLlidForwardingState----> Entry\n");
    int return_status = 0;
    return_status = dpoe_getLlidForwardingState(linkForwardingState,numEntries);
    printf("return value from ssp_EPON_GetLlidForwardingState  is %d\n",return_status);
    printf("num entries : %d",numEntries);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_EPONHAL_GetLlidForwardingState::Failed\n");
     printf("\n ssp_EPONHAL_GetLlidForwardingState ----> Exit\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_EPONHAL_GetLlidForwardingState::Success\n");
      printf("\n ssp_EPONHAL_GetLlidForwardingState ----> Exit\n");
     return return_status;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetOamFrameRate
 * Description          : This function invokes EPON  hal api dpoe_getOamFrameRate()
 * @param [in]          : NILL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
** ********************************************************************************************/
int ssp_EPONHAL_GetOamFrameRate(dpoe_link_oam_frame_rate_t linkOamFrameRate[], unsigned short numEntries)
{
    printf("\n ssp_EPONHAL_GetOamFrameRate----> Entry\n");
    int return_status = 0;
    return_status = dpoe_getOamFrameRate(linkOamFrameRate,numEntries);
    printf("return value from ssp_EPONHAL_GetOamFrameRate  is %d\n",return_status);
    printf("num entries : %d",numEntries);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_EPONHAL_GetOamFrameRate::Failed\n");
     printf("\n ssp_EPONHAL_GetOamFrameRate ----> Exit\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_EPONHAL_GetOamFrameRate::Success\n");
      printf("\n ssp_EPONHAL_GetOamFrameRate ----> Exit\n");
     return return_status;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetDynamicMacTable
 * Description          : This function invokes EPON  hal api dpoe_getDynamicMacTable()
 * @param [in]          : NILL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
** ********************************************************************************************/
int ssp_EPONHAL_GetDynamicMacTable(dpoe_link_mac_address_t linkDynamicMacTable[], unsigned short numEntries)
{
    printf("\n ssp_EPONHAL_GetDynamicMacTable----> Entry\n");
    int return_status = 0;
    return_status = dpoe_getDynamicMacTable(linkDynamicMacTable,numEntries);
    printf("return value from ssp_EPONHAL_GetDynamicMacTable  is %d\n",return_status);
    printf("num entries : %d",numEntries);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_EPONHAL_GetDynamicMacTable::Failed\n");
     printf("\n ssp_EPONHAL_GetDynamicMacTable ----> Exit\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_EPONHAL_GetDynamicMacTable::Success\n");
     printf("\n ssp_EPONHAL_GetDynamicMacTable ----> Exit\n");
     return return_status;
    }
}
/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetOnuLinkStatistics
 * Description          : This function invokes EPON  hal api dpoe_getOnuLinkStatistics()
 * @param [in]          : NILL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
** ********************************************************************************************/
int ssp_EPONHAL_GetOnuLinkStatistics(dpoe_link_traffic_stats_t onuLinkTrafficStats[], unsigned short *numEntries)
{
    printf("\n ssp_EPONHAL_GetOnuLinkStatistics----> Entry\n");
    int return_status = -1 ,loop =0,count=1;
    dpoe_onu_max_logical_links_t  MaxLogicalLinks = {0};
    //for max logical links
    if (DummyValue  == *numEntries)
    {
       *numEntries  = dpoe_getMaxLogicalLinks(&MaxLogicalLinks);
       printf("\n numEntries form dpoe_getMaxLogicalLinks :%d,",*numEntries);
       if (*numEntries != return_status && *numEntries != 0 && *numEntries > 0)
       {
          onuLinkTrafficStats  = (dpoe_link_traffic_stats_t *)malloc((sizeof(dpoe_link_traffic_stats_t)*(*numEntries)));
          if(onuLinkTrafficStats != NULL)
          {
             memset((char *)onuLinkTrafficStats, 0x00, (sizeof(dpoe_link_traffic_stats_t)*(*numEntries)));
             for (loop = 0; loop< *numEntries;loop++)
             {
                onuLinkTrafficStats[loop].link_Id = count++;
             }
             return_status = dpoe_getOnuLinkStatistics(onuLinkTrafficStats,*numEntries);
          }
          else
          {
            printf("Memory allocation failed");
          }

       }
       else
       {
          printf("\n dpoe_getMaxLogicalLinks::Failed\n");
       }
   }
   //for min logical links
    else
    {
       return_status = dpoe_getOnuLinkStatistics(onuLinkTrafficStats,*numEntries);
    }
    printf("return value from ssp_EPONHAL_GetOnuLinkStatistics  is %d\n",return_status);
    printf("num entries at the ssp_EPONHAL_GetOnuLinkStatistics exit is  : %d",*numEntries);
    if(return_status == -1)
    {
         printf("\n ssp_EPONHAL_GetOnuLinkStatistics::Failed\n");
         printf("\n ssp_EPONHAL_GetOnuLinkStatistics----> Exit\n");
         return return_status;
    }
    else
    {

         printf("\n ssp_EPONHAL_GetOnuLinkStatistics::Success\n");
         printf("\n ssp_EPONHAL_GetOnuLinkStatistics----> Exit\n");
         return SSP_SUCCESS;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetStaticMacTable
 * Description          : This function invokes EPON  hal api dpoe_getStaticMacTable()
 * @param [in]          : linkStaticMacTable - buffer to hold MAC details
 * @param [in]          : numEntries - numEntries in StaticMACTable
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
** ********************************************************************************************/
int ssp_EPONHAL_GetStaticMacTable(dpoe_link_mac_address_t linkStaticMacTable[], unsigned short numEntries)
{
    printf("\n ssp_EPONHAL_GetStaticMacTable----> Entry\n");
    int return_status = 0;

    return_status = dpoe_getStaticMacTable(linkStaticMacTable,numEntries);
    printf("return value from ssp_EPONHAL_GetStaticMacTable  is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_EPONHAL_GetStaticMacTable::Failed\n");
     printf("\n ssp_EPONHAL_GetStaticMacTable ----> Exit\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_EPONHAL_GetStaticMacTable::Success\n");
     printf("\n ssp_EPONHAL_GetStaticMacTable ----> Exit\n");
     return return_status;
    }
}


/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_SetClearOnuLinkStatistics
 * Description          : This function invokes EPON  hal api dpoe_setClearOnuLinkStatistics()
 * @param [in]          : NILL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
** ********************************************************************************************/
int ssp_EPONHAL_SetClearOnuLinkStatistics()
{
    printf("\n ssp_EPONHAL_SetClearOnuLinkStatistics----> Entry\n");
    int return_status = 0;

    return_status = dpoe_setClearOnuLinkStatistics();
    printf("return value from ssp_EPONHAL_SetClearOnuLinkStatistics is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_EPONHAL_SetClearOnuLinkStatistics::Failed\n");
     printf("\n ssp_EPONHAL_SetClearOnuLinkStatistics ----> Exit\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_EPONHAL_SetClearOnuLinkStatistics::Success\n");
     printf("\n ssp_EPONHAL_SetClearOnuLinkStatistics ----> Exit\n");
     return return_status;
    }
}


/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_SetResetOnu
 * Description          : This function invokes EPON hal api dpoe_SetResetOnu()
 * @param [in]          : NILL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
** ********************************************************************************************/
int ssp_EPONHAL_SetResetOnu()
{
    printf("\n ssp_EPONHAL_SetResetOnu----> Entry\n");
    int return_status = 0;

    return_status = dpoe_setResetOnu();
    printf("return value from ssp_EPONHAL_SetResetOnu is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_EPONHAL_SetResetOnu::Failed\n");
     printf("\n ssp_EPONHAL_SetResetOnu ----> Exit\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_EPONHAL_SetResetOnu::Success\n");
     printf("\n ssp_EPONHAL_SetResetOnu ----> Exit\n");
     return return_status;
    }
}
