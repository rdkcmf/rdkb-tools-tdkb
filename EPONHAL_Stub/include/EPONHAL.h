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

#ifndef __EPON_STUB_HAL_H__
#define __EPON_STUB_HAL_H__

#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include "ssp_tdk_eponhal_wrp.h"
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
class EPONHAL : public RDKTestStubInterface, public AbstractServer<EPONHAL>
{
        public:

                EPONHAL(TcpSocketServer &ptrRpcServer) : AbstractServer <EPONHAL>(ptrRpcServer)
                {
                        this->bindAndAddMethod(Procedure("EPONHAL_GetParamUlongValue", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "paramType", JSON_STRING,  NULL), &EPONHAL::EPONHAL_GetParamUlongValue);
                }

                bool initialize(IN const char* szVersion);
                bool cleanup(const char*);
                std::string testmodulepre_requisites();
                bool testmodulepost_requisites();

                void EPONHAL_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response);
};
#endif
