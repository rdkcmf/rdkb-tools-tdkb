/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2018 RDK Management
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

#include "mta_hal.h"

#define SSP_SUCCESS       0
#define SSP_FAILURE       1

#ifdef __cplusplus
extern "C"
{
#endif
    int ssp_MTAHAL_GetParamCharValue(char* paramName, char* value);
    int ssp_MTAHAL_GetParamUlongValue(char* paramName, unsigned long* value);
    int ssp_MTAHAL_SetParamUlongValue(char* paramName, unsigned long value);
    int ssp_MTAHAL_GetDHCPInfo(PMTAMGMT_MTA_DHCP_INFO pInfo);
    int ssp_MTAHAL_GetLineTableGetEntry(unsigned long index, PMTAMGMT_MTA_LINETABLE_INFO pEntry);
    int ssp_MTAHAL_TriggerDiagnostics(unsigned long index);
    int ssp_MTAHAL_GetServiceFlow(unsigned long* count, PMTAMGMT_MTA_SERVICE_FLOW *ppCfg);
    int ssp_MTAHAL_GetCalls(unsigned long instanceNumber, unsigned long* count, PMTAMGMT_MTA_CALLS* ppCfg);
    int ssp_MTAHAL_GetCALLP(unsigned long lineNumber, PMTAMGMT_MTA_CALLP pCallp);
    int ssp_MTAHAL_GetDSXLogs(unsigned long* count, PMTAMGMT_MTA_DSXLOG* ppDSXLog);
    int ssp_MTAHAL_GetMtaLog(unsigned long* count, PMTAMGMT_MTA_MTALOG_FULL* ppConf);
    int ssp_MTAHAL_getDhcpStatus(MTAMGMT_MTA_STATUS *output_pIpv4status, MTAMGMT_MTA_STATUS *output_pIpv6status);
    int ssp_MTAHAL_getConfigFileStatus(MTAMGMT_MTA_STATUS *poutput_status);
    int ssp_MTAHAL_getLineRegisterStatus(MTAMGMT_MTA_STATUS *output_status_array, int array_size);
    int ssp_MTAHAL_GetHandsets(unsigned long* count, PMTAMGMT_MTA_HANDSETS_INFO* ppHandsets);
    int ssp_MTAHAL_InitDB(void);
    int ssp_MTAHAL_devResetNow(void);
    int ssp_MTAHAL_getMtaOperationalStatus(MTAMGMT_MTA_STATUS *operationalStatus);
    int ssp_MTAHAL_start_provisioning(int mtaIPMode, char* dhcpOption122Suboption1, char* dhcpOption122Suboption2, char* dhcpOption2171CccV6DssID1, char* dhcpOption2171CccV6DssID2);
    int ssp_MTAHAL_LineRegisterStatus_callback_register(void);
    int ssp_MTAHAL_getMtaProvisioningStatus(MTAMGMT_MTA_PROVISION_STATUS *status);
#ifdef __cplusplus
}
#endif

