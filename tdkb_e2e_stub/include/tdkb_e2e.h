/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2017 RDK Management
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
#ifndef __TDKB_E2E_STUB_H__
#define __TDKB_E2E_STUB_H__
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
#include "ssp_tdk_wrp.h"
#define IN
#define OUT
#define TEST_SUCCESS true
#define TEST_FAILURE false
#define MAX_PARAM_SIZE  100
#define MAX_PARAM_NAMES_ARRAY   1000

/* To provide external linkage to C Functions defined in TDKB Component folder */
extern "C"
{
    int ssp_register(bool);
    GETPARAMVALUES* ssp_getParameterValue(char *pParamName,int *pParamsize);
    int ssp_setParameterValue(char *pParamName,char *pParamValue,char *pParamType,int commit);
    int ssp_setMultipleParameterValue(char **paramList, int size);
};

class RDKTestAgent;
class TDKB_E2E : public RDKTestStubInterface, public AbstractServer<TDKB_E2E>
{
    public:

		TDKB_E2E(TcpSocketServer &ptrRpcServer) : AbstractServer <TDKB_E2E>(ptrRpcServer)
		{
			this->bindAndAddMethod(Procedure("tdkb_e2e_Get", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &TDKB_E2E::tdkb_e2e_Get);
			this->bindAndAddMethod(Procedure("tdkb_e2e_Set", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "paramValue", JSON_STRING, "paramType", JSON_STRING, NULL), &TDKB_E2E::tdkb_e2e_Set);
			this->bindAndAddMethod(Procedure("tdkb_e2e_SetMultipleParams", PARAMS_BY_NAME, JSON_STRING, "paramList", JSON_STRING, NULL), &TDKB_E2E::tdkb_e2e_SetMultipleParams);
		}

        /*inherited functions*/
        bool initialize(IN const char* szVersion);
        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

        /*TDKB_E2E Stub Wrapper functions*/
        void tdkb_e2e_Get(IN const Json::Value& req, OUT Json::Value& response);
        void tdkb_e2e_Set(IN const Json::Value& req, OUT Json::Value& response);
        void tdkb_e2e_SetMultipleParams(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__TDKB_E2E_STUB_H__
