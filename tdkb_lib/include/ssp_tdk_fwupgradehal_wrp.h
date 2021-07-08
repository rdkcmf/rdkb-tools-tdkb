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

#ifndef __SSP_TDK_FWUPGRADEHAL_WRP_H__
#define __SSP_TDK_FWUPGRADEHAL_WRP_H__
#include "fwupgrade_hal.h"
#define SSP_SUCCESS       0
#define SSP_FAILURE       1
#ifdef __cplusplus

extern "C"
{
#endif
    int ssp_FWUPGRADEHAL_GetParamUlongValue(char* paramName, unsigned long* value);
    int ssp_FWUPGRADEHAL_Set_Download_Interface(unsigned int interface);
    int ssp_FWUPGRADEHAL_Download();
    int ssp_FWUPGRADEHAL_Reboot_Now();
    int ssp_FWUPGRADEHAL_Get_Download_Url(char* URL, char* filename);
    int ssp_FWUPGRADEHAL_Set_Download_Url(char* URL, char* filename);
    int ssp_FWUPGRADEHAL_UpdateAndFactoryReset(char* url, char* name);
#ifdef __cplusplus
}
#endif
#endif

