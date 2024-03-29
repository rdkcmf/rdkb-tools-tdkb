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
#ifndef __PLATFORM_STUB_HAL_H__
#define __PLATFORM_STUB_HAL_H__

#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include "ssp_tdk_platform_hal_wrp.h"
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>

/* for reference added it,(IN) indicates accepting the request from 
   Test Manager and (OUT) indicates sending the response for the request back to the Manager */
#ifndef IN
#define IN
#endif

#ifndef OUT
#define OUT
#endif

using namespace std;
/* RDKTestAgent   : This Class provides interface for the module to enable RPC mechanism. */
class RDKTestAgent;
/*  RDKTestStubInterface   : This Class provides provides interface for the modules.  */
class platform_stub_hal : public RDKTestStubInterface, public AbstractServer<platform_stub_hal>
{
	public:
                platform_stub_hal(TcpSocketServer &ptrRpcServer) : AbstractServer <platform_stub_hal>(ptrRpcServer)
                {
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetBaseMacAddress", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetBaseMacAddress);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_DocsisParamsDBInit", PARAMS_BY_NAME, JSON_STRING, NULL), &platform_stub_hal::platform_stub_hal_DocsisParamsDBInit);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetBootLoaderVersion", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetBootLoaderVersion);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetDeviceConfigStatus", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetDeviceConfigStatus);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_getFactoryPartnerId", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_getFactoryPartnerId);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetFreeMemorySize", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetFreeMemorySize);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetHardware", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetHardware);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetFirmwareName", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetFirmwareName);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetHardwareFree", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetHardwareFree);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetHardwareMemUsed", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetHardwareMemUsed);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetHardwareVersion", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetHardwareVersion);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetSerialNumber", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetSerialNumber);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetSNMPEnable", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetSNMPEnable);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetModelName", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetModelName);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetSoftwareVersion", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetSoftwareVersion);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetSSHEnable", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetSSHEnable);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetTelnetEnable", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetTelnetEnable);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetTotalMemorySize", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetTotalMemorySize);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetUsedMemorySize", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetUsedMemorySize);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetWebUITimeout", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetWebUITimeout);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_PandMDBInit", PARAMS_BY_NAME, JSON_STRING, NULL), &platform_stub_hal::platform_stub_hal_PandMDBInit);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_SetSNMPEnable", PARAMS_BY_NAME, JSON_STRING, "index", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_SetSNMPEnable);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_SetSSHEnable", PARAMS_BY_NAME, JSON_STRING, "index", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_SetSSHEnable);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_SetTelnetEnable", PARAMS_BY_NAME, JSON_STRING, "index", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_SetTelnetEnable);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_SetWebUITimeout", PARAMS_BY_NAME, JSON_STRING, "index", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_SetWebUITimeout);
			this->bindAndAddMethod(Procedure("platform_stub_hal_GetFactoryResetCount", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetFactoryResetCount);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_ClearResetCount", PARAMS_BY_NAME, JSON_STRING, "index", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_ClearResetCount);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetTimeOffSet", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetTimeOffSet);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetCMTSMac", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetCMTSMac);
			this->bindAndAddMethod(Procedure("platform_stub_hal_GetChipTemperature", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER,"chipIndex", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetChipTemperature);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetFanSpeed", PARAMS_BY_NAME, JSON_STRING, "fanIndex", JSON_INTEGER, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetFanSpeed);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_SetFanSpeed", PARAMS_BY_NAME, JSON_STRING, "index", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_SetFanSpeed);	
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetMACsecEnable", PARAMS_BY_NAME, JSON_STRING, "ethPort", JSON_INTEGER, "index", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetMACsecEnable);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_SetMACsecEnable", PARAMS_BY_NAME, JSON_STRING, "ethPort", JSON_INTEGER, "index", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_SetMACsecEnable);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetMACsecOperationalStatus", PARAMS_BY_NAME, JSON_STRING, "ethPort", JSON_INTEGER, "index", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetMACsecOperationalStatus);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_getFactoryCmVariant", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_getFactoryCmVariant);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_setFactoryCmVariant", PARAMS_BY_NAME, JSON_STRING, "CmVarient", JSON_STRING, NULL), &platform_stub_hal::platform_stub_hal_setFactoryCmVariant);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_getRPM", PARAMS_BY_NAME, JSON_STRING, "fanIndex", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_getRPM);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_getRotorLock", PARAMS_BY_NAME, JSON_STRING, "fanIndex", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_getRotorLock);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_getFanStatus", PARAMS_BY_NAME, JSON_STRING, "fanIndex", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_getFanStatus);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_setFanMaxOverride", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, "fanIndex", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_setFanMaxOverride);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_SetSNMPOnboardRebootEnable", PARAMS_BY_NAME, JSON_STRING, "SNMPonboard", JSON_STRING, NULL), &platform_stub_hal::platform_stub_hal_SetSNMPOnboardRebootEnable);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetRouterRegion", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetRouterRegion);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetMemoryPaths", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, "cpus", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetMemoryPaths);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_SetLowPowerModeState", PARAMS_BY_NAME, JSON_STRING, "state", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_SetLowPowerModeState);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_StartMACsec", PARAMS_BY_NAME, JSON_STRING, "ethPort", JSON_INTEGER, "timeoutSec", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_StartMACsec);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_StopMACsec", PARAMS_BY_NAME, JSON_STRING, "ethPort", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_StopMACsec);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetWebAccessLevel", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, "userIndex", JSON_INTEGER, "ifIndex", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetWebAccessLevel);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_SetDscp", PARAMS_BY_NAME, JSON_STRING, "interfaceType", JSON_INTEGER, "cmd", JSON_INTEGER, "isDscpValNull", JSON_INTEGER, "dscpVal", JSON_STRING, NULL), &platform_stub_hal::platform_stub_hal_SetDscp);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_ResetDscpCounts", PARAMS_BY_NAME, JSON_STRING, "interfaceType", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_ResetDscpCounts);
                        this->bindAndAddMethod(Procedure("platform_stub_hal_GetDscpClientList", PARAMS_BY_NAME, JSON_STRING, "interfaceType", JSON_INTEGER, "isClientListNull", JSON_INTEGER, NULL), &platform_stub_hal::platform_stub_hal_GetDscpClientList);
                 }

                bool initialize(IN const char* szVersion);
                bool cleanup(const char*);
                std::string testmodulepre_requisites();
                bool testmodulepost_requisites();

		void platform_stub_hal_GetBaseMacAddress(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_DocsisParamsDBInit(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetBootLoaderVersion(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetDeviceConfigStatus(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_getFactoryPartnerId(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetFreeMemorySize(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetHardware(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetFirmwareName(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetHardwareFree(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetHardwareMemUsed(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetHardwareVersion(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetSerialNumber(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetSNMPEnable(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetModelName(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetSoftwareVersion(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetSSHEnable(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetTelnetEnable(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetTotalMemorySize(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetUsedMemorySize(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetWebAccessLevel(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetWebUITimeout(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_PandMDBInit(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_SetSNMPEnable(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_SetSSHEnable(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_SetWebAccessLevel(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_SetTelnetEnable(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_SetWebUITimeout(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetFactoryResetCount(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_ClearResetCount(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_GetTimeOffSet(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_GetCMTSMac(IN const Json::Value& req, OUT Json::Value& response);
		void platform_stub_hal_GetChipTemperature(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_GetFanSpeed(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_SetFanSpeed(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_SetMACsecEnable(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_GetMACsecEnable(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_GetMACsecOperationalStatus(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_getFactoryCmVariant(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_setFactoryCmVariant(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_getRPM(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_getRotorLock(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_getFanStatus(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_setFanMaxOverride(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_SetSNMPOnboardRebootEnable(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_GetRouterRegion(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_GetMemoryPaths(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_SetLowPowerModeState(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_StartMACsec(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_StopMACsec(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_SetDscp(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_ResetDscpCounts(IN const Json::Value& req, OUT Json::Value& response);
                void platform_stub_hal_GetDscpClientList(IN const Json::Value& req, OUT Json::Value& response);
};
#endif
