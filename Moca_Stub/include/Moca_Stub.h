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
#ifndef __MOCA_STUB_H__
#define __MOCA_STUB_H__
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
#define MAX_PARAM_SIZE  100
#define MAX_PARAM_NAMES_ARRAY   1000
class RDKTestAgent;
class Mocastub : public RDKTestStubInterface, public AbstractServer<Mocastub>
{
    public:

		Mocastub(TcpSocketServer &ptrRpcServer) : AbstractServer <Mocastub>(ptrRpcServer)
		{
			this->bindAndAddMethod(Procedure("Mocastub_Get", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &Mocastub::Mocastub_Get);
			this->bindAndAddMethod(Procedure("Mocastub_Set", PARAMS_BY_NAME, JSON_STRING, "ParamName", JSON_STRING, "ParamValue", JSON_STRING, "Type", JSON_STRING, NULL), &Mocastub::Mocastub_Set);
			this->bindAndAddMethod(Procedure("Mocastub_SetKeypassphrase", PARAMS_BY_NAME, JSON_STRING, "ParamName", JSON_STRING, "ParamValue", JSON_STRING, "Type", JSON_STRING, NULL), &Mocastub::Mocastub_SetKeypassphrase);
		}

        /*inherited functions*/
        bool initialize(IN const char* szVersion);
        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

        /*Moca stub Wrapper functions*/
        void Mocastub_Get(IN const Json::Value& req, OUT Json::Value& response);
        void Mocastub_Set(IN const Json::Value& req, OUT Json::Value& response);
	void Mocastub_SetKeypassphrase(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__MOCA_STUB_H__

