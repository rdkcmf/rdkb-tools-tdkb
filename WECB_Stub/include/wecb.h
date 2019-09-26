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

#ifndef __WECB_STUB_H__
#define __WECB_STUB_H__
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

class WECB : public RDKTestStubInterface, public AbstractServer<WECB>
{
    public:

		WECB(TcpSocketServer &ptrRpcServer) : AbstractServer <WECB>(ptrRpcServer)
		{
			this->bindAndAddMethod(Procedure("WECB_GetParamNames", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "paramList", JSON_STRING, "recursive", JSON_INTEGER, NULL), &WECB::WECB_GetParamNames);
			this->bindAndAddMethod(Procedure("WECB_GetParamValues", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &WECB::WECB_GetParamValues);
			this->bindAndAddMethod(Procedure("WECB_GetParamAttributes", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &WECB::WECB_GetParamAttributes);
			this->bindAndAddMethod(Procedure("WECB_SetParamValues", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "paramValue", JSON_STRING, "paramName", JSON_STRING, "commit", JSON_INTEGER,NULL), &WECB::WECB_SetParamValues);
			this->bindAndAddMethod(Procedure("WECB_SetParamAttribute", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING,"notify", JSON_STRING, "accessControl", JSON_STRING,NULL), &WECB::WECB_SetParamAttribute);
			this->bindAndAddMethod(Procedure("WECB_SetSessionId", PARAMS_BY_NAME, JSON_STRING, "sessionId", JSON_INTEGER, NULL), &WECB::WECB_SetSessionId);
			this->bindAndAddMethod(Procedure("WECB_AddObject", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &WECB::WECB_AddObject);
			this->bindAndAddMethod(Procedure("WECB_DelObject", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &WECB::WECB_DelObject);
			this->bindAndAddMethod(Procedure("WECB_SetCommit", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &WECB::WECB_SetCommit);
		}

        /*inherited functions*/
        bool initialize(IN const char* szVersion);
        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

        /*WECB Wrapper functions*/
        void WECB_GetParamNames(IN const Json::Value& req, OUT Json::Value& response);
        void WECB_GetParamValues(IN const Json::Value& req, OUT Json::Value& response);
        void WECB_GetParamAttributes(IN const Json::Value& req, OUT Json::Value& response);
        void WECB_SetParamValues(IN const Json::Value& req, OUT Json::Value& response);
        void WECB_SetParamAttribute(IN const Json::Value& req, OUT Json::Value& response);
        void WECB_SetSessionId(IN const Json::Value& req, OUT Json::Value& response);
        void WECB_AddObject(IN const Json::Value& req, OUT Json::Value& response);
        void WECB_DelObject(IN const Json::Value& req, OUT Json::Value& response);
        void WECB_SetCommit(IN const Json::Value& req, OUT Json::Value& response);

};
#endif //__WECB_STUB_H__
