
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

#ifndef __DSLHAL_LIB_WRP_H__
#define __DSLHAL_LIB_WRP_H__

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
    int dslhal_getlinestats(char *param_name,PDML_XDSL_LINE_STATS pstLineStats) ;
    int dslhal_getXRdk_Nlm( char *param_name,PDML_XDSL_X_RDK_NLNM pstNlmInfo );
    int dslhal_getlineinfo(char *param_name, PDML_XDSL_LINE pstLineInfo);
    int xtm_hal_getLinkStats(char *param_name, PDML_PTM_STATS link_stats);
    int atm_hal_getLinkStats(char *param_name, PDML_ATM_STATS link_stats);
    int xdsl_hal_dslGetChannelInfo(char *param_name,PDML_XDSL_CHANNEL pstChannelInfo);
    int xdsl_hal_dslGetChannelStats(char *param_name, PDML_XDSL_CHANNEL_STATS pstChannelStats);
#ifdef __cplusplus
}
#endif
#endif


