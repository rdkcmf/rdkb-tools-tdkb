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

#ifndef __CosaMTA_STUB_H__
#define __CosaMTA_STUB_H__
#include <json/json.h>
#include <unistd.h>
#include <string.h>
#include <dlfcn.h>
#include <stdlib.h>
#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fstream>
#include <sstream>
#define IN
#define OUT

#define TEST_SUCCESS true
#define TEST_FAILURE false
#define MAX_PARAM_SIZE	100
#define MAX_PARAM_NAMES_ARRAY	1000


class RDKTestAgent;

class CosaMTA : public RDKTestStubInterface, public AbstractServer<CosaMTA>
{
	public:

        CosaMTA(TcpSocketServer &ptrRpcServer) : AbstractServer <CosaMTA>(ptrRpcServer)
		{
			this->bindAndAddMethod(Procedure("CosaMTA_GetResetCount", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "bufferType", JSON_INTEGER, "resetType", JSON_STRING, NULL), &CosaMTA::CosaMTA_GetResetCount);
			this->bindAndAddMethod(Procedure("CosaMTA_GetDHCPInfo", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "bufferType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_GetDHCPInfo);
			this->bindAndAddMethod(Procedure("CosaMTA_Triggerdiagnostics", PARAMS_BY_NAME, JSON_STRING, NULL), &CosaMTA::CosaMTA_Triggerdiagnostics);
			this->bindAndAddMethod(Procedure("CosaMTA_BatteryGetInfo", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "bufferType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_BatteryGetInfo);
			this->bindAndAddMethod(Procedure("CosaMTA_BatteryGetStatus", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "bufferType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_BatteryGetStatus);
			this->bindAndAddMethod(Procedure("CosaMTA_BatteryGetPowerStatus", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "bufferType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_BatteryGetPowerStatus);
			this->bindAndAddMethod(Procedure("CosaMTA_LineTableGetNumberOfEntries", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_LineTableGetNumberOfEntries);
			this->bindAndAddMethod(Procedure("CosaMTA_LineTableGetEntry", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "bufferType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_LineTableGetEntry);
			this->bindAndAddMethod(Procedure("CosaMTA_GetServiceClass", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_GetServiceClass);
			this->bindAndAddMethod(Procedure("CosaMTA_DectGetEnable", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "Value", JSON_INTEGER,"flag",JSON_INTEGER, NULL), &CosaMTA::CosaMTA_DectGetEnable);
			this->bindAndAddMethod(Procedure("CosaMTA_DectSetEnable", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "Value", JSON_INTEGER, "flag",JSON_INTEGER,NULL), &CosaMTA::CosaMTA_DectSetEnable);
			this->bindAndAddMethod(Procedure("CosaMTA_DectGetRegistrationMode", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "Value", JSON_INTEGER, "flag",JSON_INTEGER,NULL), &CosaMTA::CosaMTA_DectGetRegistrationMode);
			this->bindAndAddMethod(Procedure("CosaMTA_DectSetRegistrationMode", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "Value", JSON_INTEGER, "flag",JSON_INTEGER,NULL), &CosaMTA::CosaMTA_DectSetRegistrationMode);
			this->bindAndAddMethod(Procedure("CosaMTA_GetDect", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "bufferType", JSON_INTEGER, "flag",JSON_INTEGER,NULL), &CosaMTA::CosaMTA_GetDect);
			this->bindAndAddMethod(Procedure("CosaMTA_GetDectPIN", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "bufferType", JSON_INTEGER,"flag",JSON_INTEGER, NULL), &CosaMTA::CosaMTA_GetDectPIN);
			this->bindAndAddMethod(Procedure("CosaMTA_SetDectPIN", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "bufferType", JSON_INTEGER, "value", JSON_STRING,"flag",JSON_INTEGER, NULL), &CosaMTA::CosaMTA_SetDectPIN);
			this->bindAndAddMethod(Procedure("CosaMTA_GetDSXLogEnable", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "Value", JSON_INTEGER,NULL), &CosaMTA::CosaMTA_GetDSXLogEnable);
			this->bindAndAddMethod(Procedure("CosaMTA_SetDSXLogEnable", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "Value", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_SetDSXLogEnable);
			this->bindAndAddMethod(Procedure("CosaMTA_ClearDSXLog", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "Value", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_ClearDSXLog);
			this->bindAndAddMethod(Procedure("CosaMTA_GetCallSignallingLogEnable", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "Value", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_GetCallSignallingLogEnable);
			this->bindAndAddMethod(Procedure("CosaMTA_SetCallSignallingLogEnable", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "Value", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_SetCallSignallingLogEnable);
			this->bindAndAddMethod(Procedure("CosaMTA_ClearCallSignallingLog", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "Value", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_ClearCallSignallingLog);
			this->bindAndAddMethod(Procedure("CosaMTA_BatteryGetNumberofCycles", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_BatteryGetNumberofCycles);
			this->bindAndAddMethod(Procedure("CosaMTA_BatteryGetRemainingTime", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_BatteryGetRemainingTime);
			this->bindAndAddMethod(Procedure("CosaMTA_BatteryGetLife", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "bufferType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_BatteryGetLife);
			this->bindAndAddMethod(Procedure("CosaMTA_BatteryGetCondition", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "bufferType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_BatteryGetCondition);
			this->bindAndAddMethod(Procedure("CosaMTA_GetServiceFlow", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_GetServiceFlow);
                        this->bindAndAddMethod(Procedure("CosaMTA_GetDSXLogs", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_GetDSXLogs);
                        this->bindAndAddMethod(Procedure("CosaMTA_GetMtaLog", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_GetMtaLog);
                        this->bindAndAddMethod(Procedure("CosaMTA_GetDhcpStatus", PARAMS_BY_NAME, JSON_STRING, NULL), &CosaMTA::CosaMTA_GetDhcpStatus);
                        this->bindAndAddMethod(Procedure("CosaMTA_GetConfigFileStatus", PARAMS_BY_NAME, JSON_STRING, NULL), &CosaMTA::CosaMTA_GetConfigFileStatus);
                        this->bindAndAddMethod(Procedure("CosaMTA_GetLineRegisterStatus", PARAMS_BY_NAME, JSON_STRING, NULL), &CosaMTA::CosaMTA_GetLineRegisterStatus);
                        this->bindAndAddMethod(Procedure("CosaMTA_GetParamUlongValue", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "handleType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_GetParamUlongValue);
                        this->bindAndAddMethod(Procedure("CosaMTA_GetCalls", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, "value", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_GetCalls);
     		        this->bindAndAddMethod(Procedure("CosaMTA_GetHandsets", PARAMS_BY_NAME, JSON_STRING, "handleType", JSON_INTEGER, NULL), &CosaMTA::CosaMTA_GetHandsets);
		}

		/*inherited functions*/
		bool initialize(IN const char* szVersion);
		bool cleanup(IN const char* szVersion);
		std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

        /*CosaMTA Stub Wrapper functions*/
        void CosaMTA_GetResetCount(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_GetDHCPInfo(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_Triggerdiagnostics(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_BatteryGetInfo(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_BatteryGetStatus(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_BatteryGetPowerStatus(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_LineTableGetNumberOfEntries(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_LineTableGetEntry(IN const Json::Value& req, OUT Json::Value& response);

        void CosaMTA_GetServiceClass(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_DectGetEnable(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_DectSetEnable(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_DectGetRegistrationMode(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_DectSetRegistrationMode(IN const Json::Value& req, OUT Json::Value& response);

        void CosaMTA_GetDect(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_GetDectPIN(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_SetDectPIN(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_GetDSXLogEnable(IN const Json::Value& req, OUT Json::Value& response);

        void CosaMTA_SetDSXLogEnable(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_ClearDSXLog(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_GetCallSignallingLogEnable(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_SetCallSignallingLogEnable(IN const Json::Value& req, OUT Json::Value& response);

        void CosaMTA_ClearCallSignallingLog(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_BatteryGetNumberofCycles(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_BatteryGetRemainingTime(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_BatteryGetLife(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_BatteryGetCondition(IN const Json::Value& req, OUT Json::Value& response);
	void CosaMTA_GetServiceFlow(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_GetDSXLogs(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_GetMtaLog(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_GetDhcpStatus(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_GetConfigFileStatus(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_GetLineRegisterStatus(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response);
        void CosaMTA_GetCalls(IN const Json::Value& req, OUT Json::Value& response);
	void CosaMTA_GetHandsets(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__CosaMTA_STUB_H__
