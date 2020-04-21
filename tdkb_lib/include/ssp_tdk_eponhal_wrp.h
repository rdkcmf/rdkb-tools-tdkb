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

#ifndef __SSP_TDK_EPONHAL_WRP_H__
#define __SSP_TDK_EPONHAL_WRP_H__
#include "dpoe_hal.h"
#define SSP_SUCCESS       0
#define SSP_FAILURE       1
#ifdef __cplusplus
extern "C"
{
#endif
        int ssp_EPONHAL_GetParamUlongValue(char* paramName, unsigned long* value);
        int ssp_EPONHAL_GetFirmwareInfo(dpoe_firmware_info_t *pFirmwareInfo);
        int ssp_EPONHAL_GetEponChipInfo(dpoe_epon_chip_info_t *pEponChipInfo);
        int ssp_EPONHAL_GetManufacturerInfo(dpoe_manufacturer_t *pManufacturerInfo);
        int ssp_EPONHAL_GetOnuPacketBufferCapabilities(dpoe_onu_packet_buffer_capabilities_t *pCapabilities);
        int ssp_EPONHAL_GetOnuId(char* macAddress);
        int ssp_EPONHAL_GetMaxLogicalLinks(dpoe_onu_max_logical_links_t *pMaxLogicalLinks);
        int ssp_EPONHAL_GetDeviceSysDescrInfo(dpoe_device_sys_descr_info_t *pdevSysDescrInfo);
        int ssp_EPONHAL_GetLlidForwardingState(dpoe_link_forwarding_state_t linkForwardingState[], unsigned short numEntries);
        int ssp_EPONHAL_GetOamFrameRate(dpoe_link_oam_frame_rate_t linkOamFrameRate[], unsigned short numEntries);
        int ssp_EPONHAL_GetDynamicMacTable(dpoe_link_mac_address_t linkDynamicMacTable[], unsigned short numEntries);
        int ssp_EPONHAL_GetOnuLinkStatistics(dpoe_link_traffic_stats_t onuLinkTrafficStats[], unsigned short *numEntries);
        int ssp_EPONHAL_GetStaticMacTable(dpoe_link_mac_address_t linkStaticMacTable[], unsigned short numEntries);
        int ssp_EPONHAL_SetClearOnuLinkStatistics();
        int ssp_EPONHAL_SetResetOnu();
#ifdef __cplusplus
}
#endif
#endif
