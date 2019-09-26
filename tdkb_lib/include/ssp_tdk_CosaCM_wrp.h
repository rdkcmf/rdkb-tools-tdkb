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

#ifndef __SSP_TDK_COSACM_WRP_H__
#define __SSP_TDK_COSACM_WRP_H__


#define SSP_SUCCESS       0

#define SSP_FAILURE   	  1

int ssp_CosaDmlCMGetResetCount(int handleType, int bufferType, char *pResetType);
int ssp_CosaDmlCMGetLockedUpstreamChID(int handleType);
int ssp_CosaDmlCMSetLockedUpstreamChID(int handleType, int channelId);
int ssp_CosaDmlCMGetStartDSFrequency(int handleType);
int ssp_CosaDmlCMSetStartDSFrequency(int handleType, int frequency);
int ssp_CosaDmlCMGetProvType(int handleType, int bufferType);
int ssp_CosaDmlCMGetIPv6DHCPInfo(int handleType, int bufferType);
int ssp_CosaDmlCMGetStatus(int handleType, int Value);
int ssp_CosaCMGetLoopDiagnosticsStart(int handleType, int boolValue);
int ssp_CosaDmlCMGetLoopDiagnosticsDetails(int handleType, int Value);
int ssp_CosaDmlCMGetTelephonyRegistrationStatus(int handleType, int Value);
int ssp_CosaDmlCMGetTelephonyDHCPStatus(int handleType, int Value);
int ssp_CosaDmlCMGetTelephonyTftpStatus(int handleType, int Value);
int ssp_CosaDmlCMSetLoopDiagnosticsStart(int handleType, int boolValue);
int ssp_cosacm_GetDHCPInfo(int handleType, int bufferType);
int ssp_cosacm_GetDOCSISInfo(int handleType, int bufferType);
int ssp_cosacm_GetLog(int handleType, int bufferType);
int ssp_cosacm_SetLog(int handleType, int bufferType);
int ssp_cosacm_GetDocsisLog(int handleType, int bufferType);
int ssp_cosacm_GetDownstreamChannel(int handleType, int bufferType);
int ssp_cosacm_GetUpstreamChannel(int handleType, int bufferType);
int ssp_CosaCableModemCreate();
int ssp_CosaCableModemInitialize(int handleType);
int ssp_CosaCableModemRemove(int handleType);

#endif
