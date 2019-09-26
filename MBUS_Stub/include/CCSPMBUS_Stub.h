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
#ifndef __CCSPMBUSSTUB_STUB_H__
#define __CCSPMBUSSTUB_STUB_H__
#include <json/json.h>
#include <unistd.h>
#include <string.h>
#include <dlfcn.h>
#include <stdlib.h>
#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include <sys/types.h>
#include <sys/wait.h>
#include <fstream>
#include <sstream>
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>
#define IN
#define OUT

#define TEST_SUCCESS true
#define TEST_FAILURE false
#define MAX_PARAM_SIZE	100
#define MAX_PARAM_NAMES_ARRAY	1000

using namespace std;
class RDKTestAgent;

class CCSPMBUS : public RDKTestStubInterface, public AbstractServer<CCSPMBUS>
{
    public:

               CCSPMBUS(TcpSocketServer &ptrRpcServer) : AbstractServer <CCSPMBUS>(ptrRpcServer)
                {
                  this->bindAndAddMethod(Procedure("CCSPMBUS_GetParamValues", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_GetParamValues);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_SetParamValues", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,"paramValue", JSON_STRING,"paramType",JSON_STRING,"commit", JSON_INTEGER,NULL), &CCSPMBUS::CCSPMBUS_SetParamValues);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_Init", PARAMS_BY_NAME, JSON_STRING,"cfgfileName", JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_Init);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_Exit", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_Exit);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_RegisterEvent", PARAMS_BY_NAME, JSON_STRING,"eventName", JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_RegisterEvent);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_UnRegisterEvent", PARAMS_BY_NAME, JSON_STRING,"eventName", JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_UnRegisterEvent);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_LoadCfg", PARAMS_BY_NAME, JSON_STRING,"cmpCfgFile", JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_LoadCfg);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_LoadDmXml", PARAMS_BY_NAME, JSON_STRING,"xmlfileName", JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_LoadDmXml);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_RegisterPath", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_RegisterPath);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_QueryStatus", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_QueryStatus);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_GetAllocMemory", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_GetAllocMemory);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_GetMaxMemory", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_GetMaxMemory);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_RegisterCapabilities", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_RegisterCapabilities);
                  this->bindAndAddMethod(Procedure("CCSPMBUS_RegisterBase", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_RegisterBase);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_UnRegisterNamespace", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_UnRegisterNamespace);
 		  this->bindAndAddMethod(Procedure("CCSPMBUS_UnRegisterComponent", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_UnRegisterComponent);
 		  this->bindAndAddMethod(Procedure("CCSPMBUS_DiskNamespaceSupportedByComponent", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_DiskNamespaceSupportedByComponent);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_DiskComponentSupportingDynamicTbl", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_DiskComponentSupportingDynamicTbl);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_GetRegisteredComponents", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_GetRegisteredComponents);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_GetHealth", PARAMS_BY_NAME, JSON_STRING,"cmpId", JSON_STRING,"cmpPath", JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_GetHealth);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_DumpComponentRegistry", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_DumpComponentRegistry);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_IsSystemReady", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_IsSystemReady);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_SendSignal", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_SendSignal);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_ReqSessionId", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_ReqSessionId);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_InformEndSession", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_InformEndSession);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_BusCheck", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_BusCheck);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_CheckNamespaceDataType", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_CheckNamespaceDataType);
		  this->bindAndAddMethod(Procedure("CCSPMBUS_UnloadCfg", PARAMS_BY_NAME, JSON_STRING,NULL), &CCSPMBUS::CCSPMBUS_UnloadCfg);
               }

        /*inherited functions*/
        bool initialize(IN const char* szVersion);
        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

        void CCSPMBUS_GetParamValues(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_SetParamValues(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_Init(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_Exit(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_RegisterEvent(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_UnRegisterEvent(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_LoadCfg(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_LoadDmXml(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_RegisterPath(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_QueryStatus(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_GetAllocMemory(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_GetMaxMemory(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_RegisterCapabilities(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_UnRegisterNamespace(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_UnRegisterComponent(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_DiskNamespaceSupportedByComponent(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_DiskComponentSupportingDynamicTbl(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_GetRegisteredComponents(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_GetHealth(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_DumpComponentRegistry(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_IsSystemReady(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_SendSignal(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_ReqSessionId(const Json::Value&, Json::Value&);
        void CCSPMBUS_InformEndSession(const Json::Value&, Json::Value&);
        void CCSPMBUS_BusCheck(const Json::Value&, Json::Value&);
        void CCSPMBUS_CheckNamespaceDataType(const Json::Value&, Json::Value&);
        void CCSPMBUS_RegisterBase(IN const Json::Value& req, OUT Json::Value& response);
        void CCSPMBUS_UnloadCfg(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__CCSPMBUS_STUB_H__
