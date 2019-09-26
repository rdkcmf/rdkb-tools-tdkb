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

#ifndef __MTA_agent_STUB_H__
#define __MTA_agent_STUB_H__

#include <json/json.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <unistd.h>
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>
#include <sys/sysinfo.h>
#include <sys/utsname.h>
#include <ifaddrs.h>
#include <arpa/inet.h>
#include <net/if.h>


#include "rdkteststubintf.h"
#include "rdktestagentintf.h"

#define IN
#define OUT

#define TEST_SUCCESS true
#define TEST_FAILURE false


using namespace std;

class RDKTestAgent;
class MTA_Agent : public RDKTestStubInterface, public AbstractServer<MTA_Agent>
{
    public:

                 MTA_Agent(TcpSocketServer &ptrRpcServer) : AbstractServer <MTA_Agent>(ptrRpcServer)
                {
                  this->bindAndAddMethod(Procedure("MTA_agent_Init", PARAMS_BY_NAME, JSON_STRING,NULL), &MTA_Agent::MTA_agent_Init);
                  this->bindAndAddMethod(Procedure("MTA_agent_Terminate", PARAMS_BY_NAME, JSON_STRING,NULL), &MTA_Agent::MTA_agent_Terminate);
                  this->bindAndAddMethod(Procedure("MTA_agent_GetParameterNames", PARAMS_BY_NAME, JSON_STRING,"ParamName", JSON_STRING,"ParamList", JSON_STRING,NULL), &MTA_Agent::MTA_agent_GetParameterNames);
                  this->bindAndAddMethod(Procedure("MTA_agent_SetParameterValues", PARAMS_BY_NAME, JSON_STRING,"ParamName", JSON_STRING,"ParamValue", JSON_STRING,"Type", JSON_STRING,NULL), &MTA_Agent::MTA_agent_SetParameterValues);
                  this->bindAndAddMethod(Procedure("MTA_agent_GetParameterValues", PARAMS_BY_NAME, JSON_STRING,"ParamName", JSON_STRING,NULL), &MTA_Agent::MTA_agent_GetParameterValues);
                  this->bindAndAddMethod(Procedure("MTA_agent_GetParameterAttr", PARAMS_BY_NAME, JSON_STRING,"ParamName", JSON_STRING,NULL), &MTA_Agent::MTA_agent_GetParameterAttr);
                  this->bindAndAddMethod(Procedure("MTA_agent_SetParameterAttr", PARAMS_BY_NAME,  JSON_STRING,"ParamName", JSON_STRING,"AccessControl", JSON_STRING,"Notify", JSON_STRING,NULL), &MTA_Agent::MTA_agent_SetParameterAttr);
                  this->bindAndAddMethod(Procedure("MTA_agent_Commit", PARAMS_BY_NAME, JSON_STRING,"ParamName", JSON_STRING,"ParamValue", JSON_STRING,"Type", JSON_STRING,NULL), &MTA_Agent::MTA_agent_Commit);
                  this->bindAndAddMethod(Procedure("MTA_agent_GetParameterNames_NextLevel", PARAMS_BY_NAME, JSON_STRING,"ParamName", JSON_STRING,NULL), &MTA_Agent::MTA_agent_GetParameterNames_NextLevel);
                  this->bindAndAddMethod(Procedure("MTA_agent_DelTble", PARAMS_BY_NAME, JSON_STRING,"ParamName", JSON_STRING,NULL), &MTA_Agent::MTA_agent_DelTble);
                  this->bindAndAddMethod(Procedure("MTA_agent_AddTbl", PARAMS_BY_NAME, JSON_STRING,"ParamName", JSON_STRING,NULL), &MTA_Agent::MTA_agent_AddTbl);
                  this->bindAndAddMethod(Procedure("MTA_agent_SetSessionId", PARAMS_BY_NAME, JSON_STRING,"pathname",JSON_STRING,"priority", JSON_INTEGER,"sessionId", JSON_INTEGER,"override",JSON_INTEGER,NULL), &MTA_Agent::MTA_agent_SetSessionId);
                  this->bindAndAddMethod(Procedure("MTA_agent_GetHealth", PARAMS_BY_NAME, JSON_STRING,"ParamName", JSON_STRING,NULL), &MTA_Agent::MTA_agent_GetHealth);
		}

        /*Inherited functions*/
        bool initialize(IN const char* szVersion);
        bool cleanup(const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

        void MTA_agent_Init(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_Terminate(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_GetParameterNames(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_SetParameterValues(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_GetParameterValues(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_GetParameterAttr(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_SetParameterAttr(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_Commit(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_GetParameterNames_NextLevel(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_AddTbl(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_DelTble(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_SetSessionId(IN const Json::Value& req, OUT Json::Value& response);
        void MTA_agent_GetHealth(IN const Json::Value& req, OUT Json::Value& response);

};

#endif
