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
#ifndef __CMAGENT_STUB_H__
#define __CMAGENT_STUB_H__
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

class TADstub : public RDKTestStubInterface, public AbstractServer<TADstub>
{
    public:

		TADstub(TcpSocketServer &ptrRpcServer) : AbstractServer <TADstub>(ptrRpcServer)
		{
			this->bindAndAddMethod(Procedure("TADstub_Get", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &TADstub::TADstub_Get);
			this->bindAndAddMethod(Procedure("TADstub_Set", PARAMS_BY_NAME, JSON_STRING, "ParamName", JSON_STRING, "ParamValue", JSON_STRING, "Type", JSON_STRING, NULL), &TADstub::TADstub_Set);
			this->bindAndAddMethod(Procedure("TADstub_SetDiagnosticsState", PARAMS_BY_NAME, JSON_STRING, "ParamName", JSON_STRING, "ParamValue", JSON_STRING, "Type", JSON_STRING, NULL), &TADstub::TADstub_SetDiagnosticsState);
			this->bindAndAddMethod(Procedure("TADstub_Init", PARAMS_BY_NAME, JSON_STRING,NULL), &TADstub::TADstub_Init);
			this->bindAndAddMethod(Procedure("TADstub_Start", PARAMS_BY_NAME, JSON_STRING, "mode", JSON_INTEGER, NULL), &TADstub::TADstub_Start);
			this->bindAndAddMethod(Procedure("TADstub_Stop", PARAMS_BY_NAME, JSON_STRING, "mode", JSON_INTEGER, NULL), &TADstub::TADstub_Stop);
			this->bindAndAddMethod(Procedure("TADstub_SetCfg", PARAMS_BY_NAME, JSON_STRING, "mode", JSON_INTEGER, "host", JSON_STRING, NULL), &TADstub::TADstub_SetCfg);
			this->bindAndAddMethod(Procedure("TADstub_GetCfg", PARAMS_BY_NAME, JSON_STRING, "mode", JSON_INTEGER, NULL), &TADstub::TADstub_GetCfg);
			this->bindAndAddMethod(Procedure("TADstub_GetState", PARAMS_BY_NAME, JSON_STRING, "mode", JSON_INTEGER, NULL), &TADstub::TADstub_GetState);
		}

        /*inherited functions*/
        bool initialize(IN const char* szVersion);
        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

        /*TAD Stub Wrapper functions*/
        void TADstub_Get(IN const Json::Value& req, OUT Json::Value& response);
        void TADstub_Set(IN const Json::Value& req, OUT Json::Value& response);
        void TADstub_SetDiagnosticsState(IN const Json::Value& req, OUT Json::Value& response);
        void TADstub_Init(IN const Json::Value& req, OUT Json::Value& response);
        void TADstub_Start(IN const Json::Value& req, OUT Json::Value& response);
        void TADstub_Stop(IN const Json::Value& req, OUT Json::Value& response);
        void TADstub_SetCfg(IN const Json::Value& req, OUT Json::Value& response);
        void TADstub_GetCfg(IN const Json::Value& req, OUT Json::Value& response);
        void TADstub_GetState(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__TAD_STUB_H__
