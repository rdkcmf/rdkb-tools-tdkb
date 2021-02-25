/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2021 RDK Management
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

#ifndef __DSL_STUB_HAL_H__
#define __DSL_STUB_HAL_H__

#include "rdkteststubintf.h"
#include "rdktestagentintf.h"

#include "jsonhal_lib_wrp.h"
#include "dslhal_lib_wrp.h"
#include "json_hal_client.h"
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
class DSLHAL : public RDKTestStubInterface, public AbstractServer<DSLHAL>
{
        public:
                DSLHAL(TcpSocketServer &ptrRpcServer) : AbstractServer <DSLHAL>(ptrRpcServer)
                {
                    this->bindAndAddMethod(Procedure("DSLHAL_Init", PARAMS_BY_NAME, JSON_STRING, NULL), &DSLHAL::DSLHAL_Init);
                    this->bindAndAddMethod(Procedure("DSLHAL_GetParamValue", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &DSLHAL::DSLHAL_GetParamValue);
                    this->bindAndAddMethod(Procedure("DSLHAL_SetParamValue", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "paramType", JSON_STRING,"paramValue", JSON_STRING, NULL), &DSLHAL::DSLHAL_SetParamValue);
                    this->bindAndAddMethod(Procedure("DSLHAL_GetLineStats", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &DSLHAL::DSLHAL_GetLineStats);

                    this->bindAndAddMethod(Procedure("DSLHAL_GetXRdk_Nlm", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &DSLHAL::DSLHAL_GetXRdk_Nlm);
                    this->bindAndAddMethod(Procedure("DSLHAL_GetLineInfo", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &DSLHAL::DSLHAL_GetLineInfo);
                    this->bindAndAddMethod(Procedure("DSLHAL_XtmGetLinkStats", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &DSLHAL::DSLHAL_XtmGetLinkStats);
                    this->bindAndAddMethod(Procedure("DSLHAL_AtmGetLinkStats", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &DSLHAL::DSLHAL_AtmGetLinkStats);
                    this->bindAndAddMethod(Procedure("DSLHAL_GetChannelInfo", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &DSLHAL::DSLHAL_GetChannelInfo);
                    this->bindAndAddMethod(Procedure("DSLHAL_GetChannelStats", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &DSLHAL::DSLHAL_GetChannelStats);

                }

                bool initialize(IN const char* szVersion);
                bool cleanup(const char*);
                std::string testmodulepre_requisites();
                bool testmodulepost_requisites();

                void DSLHAL_Init(IN const Json::Value& req, OUT Json::Value& response);
                void DSLHAL_GetParamValue(IN const Json::Value& req, OUT Json::Value& response);
                void DSLHAL_SetParamValue(IN const Json::Value& req, OUT Json::Value& response);
                void DSLHAL_GetLineStats(IN const Json::Value& req, OUT Json::Value& response);
                void DSLHAL_GetXRdk_Nlm(IN const Json::Value& req, OUT Json::Value& response);
                void DSLHAL_GetLineInfo(IN const Json::Value& req, OUT Json::Value& response);
                void DSLHAL_XtmGetLinkStats(IN const Json::Value& req, OUT Json::Value& response);
                void DSLHAL_AtmGetLinkStats(IN const Json::Value& req, OUT Json::Value& response);
                void DSLHAL_GetChannelInfo(IN const Json::Value& req, OUT Json::Value& response);
                void DSLHAL_GetChannelStats(IN const Json::Value& req, OUT Json::Value& response);
};
#endif

