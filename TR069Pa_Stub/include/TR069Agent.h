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

#ifndef __TR069_STUB_H__
#define __TR069_STUB_H__

#include <json/json.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <sys/sysinfo.h>
#include <sys/utsname.h>
#include <ifaddrs.h>
#include <arpa/inet.h>
#include <net/if.h>


#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>

#define IN
#define OUT

#define TEST_SUCCESS true
#define TEST_FAILURE false


using namespace std;

class RDKTestAgent;
class TR069Agent : public RDKTestStubInterface, public AbstractServer<TR069Agent>
{
        public:

		TR069Agent(TcpSocketServer &ptrRpcServer) : AbstractServer <TR069Agent>(ptrRpcServer)
		{
			this->bindAndAddMethod(Procedure("TR069Agent_Init", PARAMS_BY_NAME, JSON_STRING,NULL), &TR069Agent::TR069Agent_Init);
			this->bindAndAddMethod(Procedure("TR069Agent_Terminate", PARAMS_BY_NAME, JSON_STRING,NULL), &TR069Agent::TR069Agent_Terminate);
			this->bindAndAddMethod(Procedure("TR069Agent_GetParameterNames", PARAMS_BY_NAME, JSON_STRING, "ParamName", JSON_STRING, "ParamList", JSON_STRING, NULL), &TR069Agent::TR069Agent_GetParameterNames);
			this->bindAndAddMethod(Procedure("TR069Agent_SetParameterValues", PARAMS_BY_NAME, JSON_STRING, "ParamName", JSON_STRING, "ParamValue", JSON_STRING, "Type", JSON_STRING,NULL), &TR069Agent::TR069Agent_SetParameterValues);
			this->bindAndAddMethod(Procedure("TR069Agent_GetParameterValues", PARAMS_BY_NAME, JSON_STRING, "ParamName", JSON_STRING, NULL), &TR069Agent::TR069Agent_GetParameterValues);
			this->bindAndAddMethod(Procedure("TR069Agent_GetParameterAttr", PARAMS_BY_NAME, JSON_STRING, "ParamName", JSON_STRING, NULL), &TR069Agent::TR069Agent_GetParameterAttr);
			this->bindAndAddMethod(Procedure("TR069Agent_SetParameterAttr", PARAMS_BY_NAME, JSON_STRING, "ParamName", JSON_STRING, "AccessControl", JSON_STRING, "Notify", JSON_STRING, NULL), &TR069Agent::TR069Agent_SetParameterAttr);
		}

        /*Inherited functions*/
        bool initialize(IN const char* szVersion);
        bool cleanup(const char*);
		std::string testmodulepre_requisites();
		bool testmodulepost_requisites();

		void TR069Agent_Init(IN const Json::Value& req, OUT Json::Value& response);
		void TR069Agent_Terminate(IN const Json::Value& req, OUT Json::Value& response);
		void TR069Agent_GetParameterNames(IN const Json::Value& req, OUT Json::Value& response);
		void TR069Agent_SetParameterValues(IN const Json::Value& req, OUT Json::Value& response);
		void TR069Agent_GetParameterValues(IN const Json::Value& req, OUT Json::Value& response);
		void TR069Agent_GetParameterAttr(IN const Json::Value& req, OUT Json::Value& response);
	    void TR069Agent_SetParameterAttr(IN const Json::Value& req, OUT Json::Value& response);
};

#endif
