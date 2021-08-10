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

#ifndef __TELCOVOICEMGR_LIB_WRP_H__
#define __TELCOVOICEMGR_LIB_WRP_H__

#include "jsonhal_wrp.h"

#include <json-c/json.h>
#include "json_hal_common.h"
#include "json_hal_client.h"

#define SSP_SUCCESS       0
#define SSP_FAILURE       1
#ifdef __cplusplus
extern "C"
{
#endif
    int telcovoicemgrhal_initdata(int bStatus);
    int telcovoicemgrhal_getlinestats(char *param_name, TELCOVOICEMGR_DML_VOICESERVICE_STATS *pLineStats);
    int telcovoicemgrhal_getcapabilities(PTELCOVOICEMGR_DML_CAPABILITIES pCapabilities, char *param_name);
    int telcovoicemgrhal_getvoiceprofile(DML_PROFILE_LIST_T* pVoiceProfileList, int vsIndex, char *param_name);
    int telcovoicemgrhal_getphyinterface(DML_PHYINTERFACE_LIST_T* pPhyInterfaceList, int vsIndex, char *param_name);
#ifdef __cplusplus
}
#endif
#endif

