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
#ifndef __WIFIAGENT_STUB_H__
#define __WIFIAGENT_STUB_H__
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

class WIFIAgent :  public RDKTestStubInterface, public AbstractServer<WIFIAgent>
{
    public:

                 WIFIAgent(TcpSocketServer &ptrRpcServer) : AbstractServer <WIFIAgent>(ptrRpcServer)
                {
                  this->bindAndAddMethod(Procedure("WIFIAgent_Start", PARAMS_BY_NAME, JSON_STRING,NULL), &WIFIAgent::WIFIAgent_Start);
                  this->bindAndAddMethod(Procedure("WIFIAgent_Get", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &WIFIAgent::WIFIAgent_Get);
                  this->bindAndAddMethod(Procedure("WIFIAgent_GetAttr", PARAMS_BY_NAME, JSON_STRING,"paramname", JSON_STRING,NULL), &WIFIAgent::WIFIAgent_GetAttr);
                  this->bindAndAddMethod(Procedure("WIFIAgent_GetNames", PARAMS_BY_NAME, JSON_STRING,"pathname",JSON_STRING ,"brecursive", JSON_INTEGER,NULL), &WIFIAgent::WIFIAgent_GetNames);
                  this->bindAndAddMethod(Procedure("WIFIAgent_SetAttr", PARAMS_BY_NAME, JSON_STRING,"paramname", JSON_STRING,"notification", JSON_STRING,"accessControlChanged", JSON_STRING,NULL), &WIFIAgent::WIFIAgent_SetAttr);
                  this->bindAndAddMethod(Procedure("WIFIAgent_Set", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,"paramValue", JSON_STRING,"paramType", JSON_STRING,NULL), &WIFIAgent::WIFIAgent_Set);
                  this->bindAndAddMethod(Procedure("WIFIAgent_Set_Get", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,"paramValue", JSON_STRING,"paramType", JSON_STRING,NULL), &WIFIAgent::WIFIAgent_Set_Get);
                  this->bindAndAddMethod(Procedure("WIFIAgent_AddObject", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &WIFIAgent::WIFIAgent_AddObject);
                  this->bindAndAddMethod(Procedure("WIFIAgent_DelObject", PARAMS_BY_NAME, JSON_STRING,"paramName",JSON_STRING ,"apiTest", JSON_INTEGER,NULL), &WIFIAgent::WIFIAgent_DelObject);
                  this->bindAndAddMethod(Procedure("WIFIAgent_SetCommit", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &WIFIAgent::WIFIAgent_SetCommit);
                  this->bindAndAddMethod(Procedure("WIFIAgent_GetHealth", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &WIFIAgent::WIFIAgent_GetHealth);
                  this->bindAndAddMethod(Procedure("WIFIAgent_SetSessionId", PARAMS_BY_NAME, JSON_STRING,"pathname",JSON_STRING,"priority", JSON_INTEGER,"sessionId", JSON_INTEGER,"override", JSON_INTEGER,NULL), &WIFIAgent::WIFIAgent_SetSessionId);
                  this->bindAndAddMethod(Procedure("WIFIAgent_Stop", PARAMS_BY_NAME, JSON_STRING,NULL), &WIFIAgent::WIFIAgent_Stop);
                  this->bindAndAddMethod(Procedure("WIFIAgent_SetMultiple", PARAMS_BY_NAME, JSON_STRING,"paramList", JSON_STRING,NULL), &WIFIAgent::WIFIAgent_SetMultiple);
               }

        /*inherited functions*/
        bool initialize(IN const char* szVersion);

        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();
        /*WIFI Stub Wrapper functions*/
        void WIFIAgent_Start(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_Get(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_GetAttr(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_SetAttr(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_GetNames(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_Set(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_Set_Get(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_AddObject(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_DelObject(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_SetCommit(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_GetHealth(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_SetSessionId(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_Stop(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIAgent_SetMultiple(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__WIFIAGENT_STUB_H__
