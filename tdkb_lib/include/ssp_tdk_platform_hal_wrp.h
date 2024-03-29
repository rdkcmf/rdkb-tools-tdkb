/****************************************************************************
  Copyright 2016-2018 Intel Corporation

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
 ******************************************************************************/
#ifndef __SSP_TDK_HAL_WRP_H__
#define __SSP_TDK_HAL_WRP_H__
#include "platform_hal.h"    
#ifdef __cplusplus
extern "C"
{
#endif
        int ssp_register(BOOLEAN);
        int ssp_terminate();
        int ssp_DocsisParamsDBInit();
        int ssp_GetBaseMacAddress(char*);
        int ssp_GetBootloaderVersion(char*,unsigned long int);
        int ssp_GetDeviceConfigStatus(char*);
        int ssp_getFactoryPartnerId(char*);
        int ssp_GetFreeMemorySize(unsigned long int*);
        int ssp_GetFirmwareName(char*,unsigned long int);
        int ssp_GetHardware(char*);
        int ssp_GetHardwareMemFree(char*);
        int ssp_GetHardwareMemUsed(char*);
        int ssp_GetHardwareVersion(char *);
        int ssp_GetModelName(char*);
        int ssp_GetSerialNumber(char*);
        int ssp_GetSNMPEnable(char*);
        int ssp_GetSoftwareVersion(char*,unsigned long int);
        int ssp_GetSSHEnable(BOOLEAN*);
        int ssp_GetTelEnable(BOOLEAN*);
        int ssp_GetTotalMemorySize(unsigned long int*);
        int ssp_GetUsedMemorySize(unsigned long int*);
        int ssp_GetWebAccessLevel(int,int,unsigned long int*);
        int ssp_GetWebUITimeout(unsigned long int*);
        int ssp_PandMDBInit();
        int ssp_SetSNMPEnable(char *);
        int ssp_SetSSHEnable(BOOLEAN);
        int ssp_SetTelnetEnable(BOOLEAN);
        int ssp_SetWebAccessLevel(int,int,int);
        int ssp_SetWebUITimeout(unsigned long int);
	int ssp_GetFactoryResetCount(unsigned long int*);
        int ssp_ClearResetCount(BOOLEAN);
        int ssp_GetTimeOffSet(char*);
        int ssp_GetCMTSMac(char*);
	int ssp_GetChipTemperature(unsigned int,unsigned long int*);
        int ssp_GetFanSpeed(unsigned int,unsigned long int*);
        int ssp_SetFanSpeed(unsigned long int);
        int ssp_SetMACsecEnable(int,BOOLEAN);
        int ssp_GetMACsecEnable(int,BOOLEAN*);
        int ssp_GetMACsecOperationalStatus(int,BOOLEAN*);
        int ssp_getFactoryCmVariant(char*);
        int ssp_setFactoryCmVariant(char*);
        int ssp_getRPM(unsigned int,unsigned int*);
        int ssp_getRotorLock(unsigned int,int*);
        int ssp_getFanStatus(unsigned int,int*);
        int ssp_setFanMaxOverride(BOOLEAN, unsigned int);
        int ssp_SetSNMPOnboardRebootEnable(char*);
        int ssp_GetRouterRegion(char*);
        int ssp_GetMemoryPaths(RDK_CPUS, PPLAT_PROC_MEM_INFO*);
        int ssp_SetLowPowerModeState(PSM_STATE);
        int ssp_StartMACsec(int, int);
        int ssp_StopMACsec(int);
        int ssp_setDscp(WAN_INTERFACE interfaceType , TRAFFIC_CNT_COMMAND cmd , char* dscpVal);
        int ssp_resetDscpCounts(WAN_INTERFACE interfaceType);
        int ssp_getDscpClientList(WAN_INTERFACE interfaceType , pDSCP_list_t DSCP_List);
#ifdef __cplusplus
}
#endif
#endif
