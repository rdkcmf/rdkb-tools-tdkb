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

#ifndef __SSP_TDK_MSOMGMTHAL_WRP_H__
#define __SSP_TDK_MSOMGMTHAL_WRP_H__
#include "dpoe_hal.h"

#ifdef __cplusplus
extern "C"
{
#endif
        int ssp_mso_mgmt_hal_GetMsoPodSeed(char* value);
        int ssp_mso_mgmt_hal_SetMsoPodSeed(char* value);
        int ssp_mso_mgmt_hal_MsoValidatePwd(char* paramValue,char* output);
#ifdef __cplusplus
}
#endif
#endif

