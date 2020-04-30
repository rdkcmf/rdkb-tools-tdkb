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

#ifndef __MSOMGMT_STUB_HAL_H__
#define __MSOMGMT_STUB_HAL_H__

#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include "ssp_tdk_mso_mgmt_hal_wrp.h"
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
class mso_mgmt_hal : public RDKTestStubInterface, public AbstractServer<mso_mgmt_hal>
{
        public:

                mso_mgmt_hal(TcpSocketServer &ptrRpcServer) : AbstractServer <mso_mgmt_hal>(ptrRpcServer)
                {
                  this->bindAndAddMethod(Procedure("mso_mgmt_hal_GetMsoPodSeed", PARAMS_BY_NAME, JSON_STRING,"paramType", JSON_STRING,NULL), &mso_mgmt_hal::mso_mgmt_hal_GetMsoPodSeed);                
                  this->bindAndAddMethod(Procedure("mso_mgmt_hal_SetMsoPodSeed", PARAMS_BY_NAME,JSON_STRING,"paramValue",JSON_STRING,"paramType",JSON_STRING,NULL), &mso_mgmt_hal::mso_mgmt_hal_SetMsoPodSeed);
		  this->bindAndAddMethod(Procedure("mso_mgmt_hal_MsoValidatePwd", PARAMS_BY_NAME,JSON_STRING,"paramValue",JSON_STRING,"paramType",JSON_STRING,NULL), &mso_mgmt_hal::mso_mgmt_hal_MsoValidatePwd);
                }                
                bool initialize(IN const char* szVersion);
                bool cleanup(const char*);
                std::string testmodulepre_requisites();
                bool testmodulepost_requisites();

                void mso_mgmt_hal_GetMsoPodSeed(IN const Json::Value& req, OUT Json::Value& response);
		void mso_mgmt_hal_SetMsoPodSeed(IN const Json::Value& req, OUT Json::Value& response);
                void mso_mgmt_hal_MsoValidatePwd(IN const Json::Value& req, OUT Json::Value& response);

};
#endif



