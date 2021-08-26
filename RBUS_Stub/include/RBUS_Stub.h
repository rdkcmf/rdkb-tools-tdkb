/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2020 RDK Management
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

#ifndef __RBUS_STUB_H__
#define __RBUS_STUB_H__

#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include "ssp_tdk_rbus_wrp.h"
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>

/* for reference added it,(IN) indicates accepting the request from Test Manager and (OUT)
   indicates sending the response for the request back to the Manager */
#ifndef IN
#define IN
#endif

#ifndef OUT
#define OUT
#endif

#define TEST_SUCCESS true
#define TEST_FAILURE false

using namespace std;

/* RDKTestAgent : This Class provides interface for the module to enable RPC mechanism. */
class RDKTestAgent;
/* RDKTestStubInterface : This Class provides provides interface for the modules.  */
class RBUS : public RDKTestStubInterface, public AbstractServer<RBUS>
{
    public:

        RBUS(TcpSocketServer &ptrRpcServer) : AbstractServer <RBUS>(ptrRpcServer)
        {
            this->bindAndAddMethod(Procedure("RBUS_CheckStatus", PARAMS_BY_NAME, JSON_STRING, NULL), &RBUS::RBUS_CheckStatus);
            this->bindAndAddMethod(Procedure("RBUS_Open", PARAMS_BY_NAME, JSON_STRING, NULL), &RBUS::RBUS_Open);
            this->bindAndAddMethod(Procedure("RBUS_Close", PARAMS_BY_NAME, JSON_STRING, NULL), &RBUS::RBUS_Close);
            this->bindAndAddMethod(Procedure("RBUS_DataElements", PARAMS_BY_NAME, JSON_STRING, "element1",JSON_STRING, "element2" , JSON_STRING, "operation", JSON_STRING, NULL), &RBUS::RBUS_DataElements);
            this->bindAndAddMethod(Procedure("RBUS_Session", PARAMS_BY_NAME, JSON_STRING,"operation", JSON_STRING, NULL), &RBUS::RBUS_Session);
            this->bindAndAddMethod(Procedure("RBUS_CloseSession", PARAMS_BY_NAME, JSON_STRING, "sessionid", JSON_INTEGER, NULL), &RBUS::RBUS_CloseSession);
            this->bindAndAddMethod(Procedure("RBUS_DiscoverComponentDataElements", PARAMS_BY_NAME, JSON_STRING, "componentName", JSON_STRING, NULL), &RBUS::RBUS_DiscoverComponentDataElements);
            this->bindAndAddMethod(Procedure("RBUS_Get", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &RBUS::RBUS_Get);
            this->bindAndAddMethod(Procedure("RBUS_GetValue", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "paramType", JSON_STRING, NULL), &RBUS::RBUS_GetValue);
            this->bindAndAddMethod(Procedure("RBUS_SetValue", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "paramType", JSON_STRING, "paramValue", JSON_STRING, NULL), &RBUS::RBUS_SetValue);
            this->bindAndAddMethod(Procedure("RBUS_RegisterOperation", PARAMS_BY_NAME, JSON_STRING, "operation", JSON_STRING, "objectName", JSON_STRING, "methodName", JSON_STRING, NULL), &RBUS::RBUS_RegisterOperation);
            this->bindAndAddMethod(Procedure("RBUS_PropertyCommands", PARAMS_BY_NAME, JSON_STRING, "operation", JSON_STRING, "prop_count",JSON_INTEGER,  "property_name", JSON_STRING, NULL), &RBUS::RBUS_PropertyCommands);
            this->bindAndAddMethod(Procedure("RBUS_ObjectCommands", PARAMS_BY_NAME, JSON_STRING, "operation", JSON_STRING, "obj_count",JSON_INTEGER,  "object_name", JSON_STRING, NULL), &RBUS::RBUS_ObjectCommands);
            this->bindAndAddMethod(Procedure("RBUS_TableRowCommands", PARAMS_BY_NAME, JSON_STRING, "operation", JSON_STRING, "table_row", JSON_STRING, NULL), &RBUS::RBUS_TableRowCommands);
            this->bindAndAddMethod(Procedure("RBUS_SetLogLevel", PARAMS_BY_NAME, JSON_STRING, "level", JSON_INTEGER, NULL), &RBUS::RBUS_SetLogLevel);
        }

        bool initialize(IN const char* szVersion);
        bool cleanup(const char*);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();
        void RBUS_CheckStatus(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_Open(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_Close(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_DataElements(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_Session(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_CloseSession(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_DiscoverComponentDataElements(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_Get(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_GetValue(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_SetValue(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_RegisterOperation(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_PropertyCommands(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_ObjectCommands(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_TableRowCommands(IN const Json::Value& req, OUT Json::Value& response);
        void RBUS_SetLogLevel(IN const Json::Value& req, OUT Json::Value& response);
};
#endif

