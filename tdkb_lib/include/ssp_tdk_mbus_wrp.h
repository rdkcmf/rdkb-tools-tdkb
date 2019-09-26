/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
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

#ifndef __SSP_TDK_MBUS_WRP_H__
#define __SSP_TDK_MBUS_WRP_H__

#define SSP_MBUS_TRUE       	1

#define SSP_MBUS_SUCCESS	0

#define SSP_MBUS_FAILURE	-1

#define SSP_MBUS_EXEC_ERROR 	-2

#define  CCSP_NAME_PREFIX      	""

#if eRT
    #define CCSP_CR_NAME "eRT.com.cisco.spvtg.ccsp.CR"
    #define CCSP_PAM_NAME "eRT.com.cisco.spvtg.ccsp.pam"
    #define CCSP_TDKB_NAMESPACE "eRT.com.cisco.spvtg.ccsp.tdkb.Name"
#else
    #define CCSP_CR_NAME "com.cisco.spvtg.ccsp.CR"
    #define CCSP_PAM_NAME "com.cisco.spvtg.ccsp.pam"
    #define CCSP_TDKB_NAMESPACE "com.cisco.spvtg.ccsp.tdkb.Name"
#endif

#endif
