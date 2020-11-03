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

#ifndef __SSP_TDK_RBUS_WRP_H__
#define __SSP_TDK_RBUS_WRP_H__
#include "rbus.h"
#define SSP_SUCCESS       0
#define SSP_FAILURE       1
#ifdef __cplusplus
extern "C"
{
#endif
        int ssp_rbus_checkStatus( rbusStatus_t *status);
        int ssp_rbus_open();
        int ssp_rbus_close();
#ifdef __cplusplus
}
#endif
#endif
