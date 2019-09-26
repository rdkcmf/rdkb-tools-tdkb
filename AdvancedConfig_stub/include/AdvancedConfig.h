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

#ifndef __ADVANCEDCONFIG_STUB_H__
#define __ADVANCEDCONFIG_STUB_H__

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

class AdvancedConfig : public RDKTestStubInterface, public AbstractServer<AdvancedConfig>
{
	public:

		AdvancedConfig(TcpSocketServer &ptrRpcServer) : AbstractServer <AdvancedConfig>(ptrRpcServer)
		{
			this->bindAndAddMethod(Procedure("AdvancedConfig_Start", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_Start);
			this->bindAndAddMethod(Procedure("AdvancedConfig_Get", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_Get);
			this->bindAndAddMethod(Procedure("AdvancedConfig_GetAttr", PARAMS_BY_NAME, JSON_STRING, "paramname", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_GetAttr);
			this->bindAndAddMethod(Procedure("AdvancedConfig_SetAttr", PARAMS_BY_NAME, JSON_STRING, "paramname", JSON_STRING, "notification", JSON_STRING, "accessControlChanged", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_SetAttr);
			this->bindAndAddMethod(Procedure("AdvancedConfig_GetNames", PARAMS_BY_NAME, JSON_STRING, "pathname", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_GetNames);
			this->bindAndAddMethod(Procedure("AdvancedConfig_Set", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "paramValue", JSON_STRING, "paramType", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_Set);
			this->bindAndAddMethod(Procedure("AdvancedConfig_Set_Get", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "paramValue", JSON_STRING, "paramType", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_Set_Get);
			this->bindAndAddMethod(Procedure("AdvancedConfig_AddObject", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_AddObject);
			this->bindAndAddMethod(Procedure("AdvancedConfig_DelObject", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_DelObject);
			this->bindAndAddMethod(Procedure("AdvancedConfig_SetCommit", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_SetCommit);
			this->bindAndAddMethod(Procedure("AdvancedConfig_GetHealth", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_GetHealth);
			this->bindAndAddMethod(Procedure("AdvancedConfig_SetSessionId", PARAMS_BY_NAME, JSON_STRING, "priority", JSON_INTEGER, "sessionId", JSON_INTEGER, NULL), &AdvancedConfig::AdvancedConfig_SetSessionId);
			this->bindAndAddMethod(Procedure("AdvancedConfig_Stop", PARAMS_BY_NAME, JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_Stop);
			this->bindAndAddMethod(Procedure("AdvancedConfig_SetMultiple", PARAMS_BY_NAME, JSON_STRING, "paramList", JSON_STRING, NULL), &AdvancedConfig::AdvancedConfig_SetMultiple);
		}

		/*inherited functions*/
		bool initialize(IN const char* szVersion);
        bool cleanup(IN const char* szVersion);
		std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

		/*Advance Config Stub Wrapper functions*/
		void AdvancedConfig_Start(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_Get(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_GetAttr(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_SetAttr(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_GetNames(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_Set(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_Set_Get(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_AddObject(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_DelObject(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_SetCommit(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_GetHealth(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_SetSessionId(IN const Json::Value& req, OUT Json::Value& response);
		void AdvancedConfig_Stop(IN const Json::Value& req, OUT Json::Value& response);
        void AdvancedConfig_SetMultiple(IN const Json::Value& req, OUT Json::Value& response);
};

#endif
