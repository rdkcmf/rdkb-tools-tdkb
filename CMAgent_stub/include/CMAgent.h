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
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>
#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
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

class CMAgent : public RDKTestStubInterface, public AbstractServer<CMAgent>
{
    public:

                 CMAgent(TcpSocketServer &ptrRpcServer) : AbstractServer <CMAgent>(ptrRpcServer)
                {
                  this->bindAndAddMethod(Procedure("CMAgent_Get", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CMAgent::CMAgent_Get);
                  this->bindAndAddMethod(Procedure("CMAgent_GetAttr", PARAMS_BY_NAME, JSON_STRING,"paramname", JSON_STRING,NULL), &CMAgent::CMAgent_GetAttr);
                  this->bindAndAddMethod(Procedure("CMAgent_GetNames", PARAMS_BY_NAME, JSON_STRING,"pathname",JSON_STRING, "brecursive",JSON_INTEGER,NULL), &CMAgent::CMAgent_GetNames);
                  this->bindAndAddMethod(Procedure("CMAgent_SetAttr", PARAMS_BY_NAME, JSON_STRING,"paramname", JSON_STRING,"notification", JSON_STRING,"accessControlChanged", JSON_STRING,NULL), &CMAgent::CMAgent_SetAttr);
                  this->bindAndAddMethod(Procedure("CMAgent_Set", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,"paramValue", JSON_STRING,"paramType", JSON_STRING,NULL), &CMAgent::CMAgent_Set);
                  this->bindAndAddMethod(Procedure("CMAgent_AddObject", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CMAgent::CMAgent_AddObject);
                  this->bindAndAddMethod(Procedure("CMAgent_DelObject", PARAMS_BY_NAME, JSON_STRING,"paramName",JSON_STRING ,"apiTest", JSON_INTEGER,NULL), &CMAgent::CMAgent_DelObject);
                  this->bindAndAddMethod(Procedure("CMAgent_SetCommit", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CMAgent::CMAgent_SetCommit);
                  this->bindAndAddMethod(Procedure("CMAgent_GetHealth", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CMAgent::CMAgent_GetHealth);
                  this->bindAndAddMethod(Procedure("CMAgent_SetSessionId", PARAMS_BY_NAME, JSON_STRING,"pathname",JSON_STRING, "priority",JSON_INTEGER,"sessionId", JSON_INTEGER,"override", JSON_INTEGER,NULL), &CMAgent::CMAgent_SetSessionId);
                  this->bindAndAddMethod(Procedure("CMAgent_Set_Get", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,"paramValue", JSON_STRING,"paramType", JSON_STRING,NULL), &CMAgent::CMAgent_Set_Get);
		}

        /*inherited functions*/
        bool initialize(IN const char* szVersion);

        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();
        /*CM Agent Stub Wrapper functions*/
        void CMAgent_Get(IN const Json::Value& req, OUT Json::Value& response);
        void CMAgent_GetAttr(IN const Json::Value& req, OUT Json::Value& response);
        void CMAgent_SetAttr(IN const Json::Value& req, OUT Json::Value& response);
        void CMAgent_GetNames(IN const Json::Value& req, OUT Json::Value& response);
        void CMAgent_Set(IN const Json::Value& req, OUT Json::Value& response);
        void CMAgent_Set_Get(IN const Json::Value& req, OUT Json::Value& response);
        void CMAgent_AddObject(IN const Json::Value& req, OUT Json::Value& response);
        void CMAgent_DelObject(IN const Json::Value& req, OUT Json::Value& response);
        void CMAgent_SetCommit(IN const Json::Value& req, OUT Json::Value& response);
        void CMAgent_GetHealth(IN const Json::Value& req, OUT Json::Value& response);
        void CMAgent_SetSessionId(IN const Json::Value& req, OUT Json::Value& response);

};
#endif //__CMAGENT_STUB_H__
