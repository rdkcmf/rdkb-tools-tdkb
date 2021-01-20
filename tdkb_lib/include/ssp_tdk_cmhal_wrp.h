/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
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

#include "cm_hal.h"
#define SSP_SUCCESS       0
#define SSP_FAILURE       1

#ifdef __cplusplus
extern "C"
{
#endif
    int ssp_CMHAL_GetParamCharValue(char* paramName, char* value);
    int ssp_CMHAL_GetParamUlongValue(char* paramName, unsigned long* value);
    int ssp_CMHAL_GetErrorCodeWords(char *value, int isNegativeScenario);
    int ssp_CMHAL_Init(char* paramName);
    int ssp_CMHAL_GetDocsisEventLogItems(CMMGMT_CM_EventLogEntry_t *entryArray,int len,int isNegativeScenario);
    int ssp_CMHAL_SetLEDFlashStatus(BOOLEAN LEDFlash);
    int ssp_CMHAL_ClearDocsisEventLog(void);
    int ssp_CMHAL_GetCPEList(unsigned long int *InstanceNum, char *cpeList,char *lanMode,int isNegativeScenario);
    int ssp_CMHAL_SetMddIpModeOverride(char* Value);
    int ssp_CMHAL_SetStartFreq(unsigned long int Value);
    int ssp_CMHAL_SetUSChannelId(int Value);
    int ssp_CMHAL_SetHTTP_Download_Interface(unsigned int interface);
    int ssp_CMHAL_Download();
    int ssp_CMHAL_Reboot_Now();
    int ssp_CMHAL_GetHTTP_Download_Url(char* httpURL, char* filename);
    int ssp_CMHAL_SetHTTP_Download_Url(char* httpURL, char* filename);
    int ssp_CMHAL_FWupdateAndFactoryReset(char* url, char* name);
    int ssp_CMHAL_GetDsOfdmChanTable(char* paramName, char* value, int *numberofEntries);
    int ssp_CMHAL_GetUsOfdmChanTable(char* paramName, char* value, int *numberofEntries);
    int ssp_CMHAL_GetStatusOfdmaUsTable(char* paramName, char* value, int *numberofEntries);
    int ssp_CMHAL_IsEnergyDetected(char* energyDetected);
#ifdef __cplusplus
}
#endif
