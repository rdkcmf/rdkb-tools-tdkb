/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
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

#include "moca_hal.h"
#define SSP_SUCCESS       0
#define SSP_FAILURE       1

#ifdef __cplusplus
extern "C"
{
#endif
    int ssp_MoCAHAL_GetIfConfig(unsigned long ifIndex, moca_cfg_t *pmoca_config);
    int ssp_MoCAHAL_SetIfConfig(unsigned long ifIndex, moca_cfg_t *pmoca_config);
    int ssp_MoCAHAL_IfGetDynamicInfo(unsigned long ifIndex, moca_dynamic_info_t *pdynamic_info);
    int ssp_MoCAHAL_IfGetStaticInfo(unsigned long ifIndex, moca_static_info_t *pstatic_info);
    int ssp_MoCAHAL_IfGetStats(unsigned long ifIndex, moca_stats_t *pmoca_stats);
    int ssp_MoCAHAL_GetNumAssociatedDevices(unsigned long ifIndex, unsigned long *pulCount);
    int ssp_MoCAHAL_IfGetExtCounter(unsigned long ifIndex, moca_mac_counters_t *pmoca_mac_counters);
    int ssp_MoCAHAL_IfGetExtAggrCounter(unsigned long ifIndex, moca_aggregate_counters_t *pmoca_aggregate_counts);
    int ssp_MoCAHAL_GetMocaCPEs(unsigned long ifIndex, moca_cpe_t *cpes, INT *pnum_cpes);
    int ssp_MoCAHAL_GetAssociatedDevices(unsigned long ifIndex, moca_associated_device_t **ppdevice_array);
    int ssp_MoCAHAL_FreqMaskToValue(unsigned char* mask);
    int ssp_MoCAHAL_HardwareEquipped();
    int ssp_MoCAHAL_GetFullMeshRates(unsigned long ifIndex, moca_mesh_table_t *pDeviceArray, unsigned long *pulCount);
    int ssp_MoCAHAL_GetFlowStatistics(unsigned long ifIndex, moca_flow_table_t *pDeviceArray, unsigned long *pulCount);
    int ssp_MoCAHAL_GetResetCount(unsigned long *resetcnt);
    int ssp_MoCAHAL_GetIfAcaConfig(int ifIndex, moca_aca_cfg_t *acaCfg);
    int ssp_MoCAHAL_SetIfAcaConfig(int ifIndex, moca_aca_cfg_t acaCfg);
    int ssp_MoCAHAL_GetIfAcaStatus(int ifIndex, moca_aca_stat_t *pAcaStat);
    int ssp_MoCAHAL_CancelIfAca(int ifIndex);
    int ssp_MoCAHAL_GetIfScmod(int ifIndex, int *pNumOfEntries, moca_scmod_stat_t **ppscmodStat);
#ifdef __cplusplus
}
#endif
