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

#ifndef __TELCOVOICEMGR_STUB_HAL_H__
#define __TELCOVOICEMGR_STUB_HAL_H__

#include "rdkteststubintf.h"
#include "rdktestagentintf.h"

#include "jsonhal_lib_wrp.h"
#include "telcovoicemgrhal_lib_wrp.h"
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

#define MAX_BUFFER_SIZE_TO_SEND 500
#define MAX_PARAMETER_SIZE 500
#define DETAILS_BUFFER_SIZE 2048
#define RETURN_SUCCESS 0
#define RETURN_FAILURE 1
#define TELCO_CONF_FILE "/etc/rdk/conf/telcovoice_manager_conf.json"

using namespace std;

/* RDKTestAgent : This Class provides interface for the module to enable RPC mechanism. */
class RDKTestAgent;
/* RDKTestStubInterface : This Class provides provides interface for the modules.  */
class TELCOVOICEMgrHal : public RDKTestStubInterface, public AbstractServer<TELCOVOICEMgrHal>
{
        public:
                TELCOVOICEMgrHal(TcpSocketServer &ptrRpcServer) : AbstractServer <TELCOVOICEMgrHal>(ptrRpcServer)
                {
                    this->bindAndAddMethod(Procedure("TELCOVOICEMgrHal_Init", PARAMS_BY_NAME, JSON_STRING, NULL), &TELCOVOICEMgrHal::TELCOVOICEMgrHal_Init);
                    this->bindAndAddMethod(Procedure("TELCOVOICEMgrHal_InitData", PARAMS_BY_NAME, JSON_STRING, "bStatus", JSON_INTEGER, NULL), &TELCOVOICEMgrHal::TELCOVOICEMgrHal_InitData);
                    this->bindAndAddMethod(Procedure("TELCOVOICEMgrHal_GetParamValue", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &TELCOVOICEMgrHal::TELCOVOICEMgrHal_GetParamValue);
                    this->bindAndAddMethod(Procedure("TELCOVOICEMgrHal_SetParamValue", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "paramType", JSON_STRING,"paramValue", JSON_STRING, NULL), &TELCOVOICEMgrHal::TELCOVOICEMgrHal_SetParamValue);
                    this->bindAndAddMethod(Procedure("TELCOVOICEMgrHal_GetLineStats", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "flag", JSON_INTEGER, NULL), &TELCOVOICEMgrHal::TELCOVOICEMgrHal_GetLineStats);
                    this->bindAndAddMethod(Procedure("TELCOVOICEMgrHal_GetCapabilities", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, "paramName", JSON_STRING, NULL), &TELCOVOICEMgrHal::TELCOVOICEMgrHal_GetCapabilities);
                    this->bindAndAddMethod(Procedure("TELCOVOICEMgrHal_GetVoiceProfile", PARAMS_BY_NAME, JSON_STRING, "index", JSON_INTEGER, "flag", JSON_INTEGER, "paramName", JSON_STRING, NULL), &TELCOVOICEMgrHal::TELCOVOICEMgrHal_GetVoiceProfile);
                    this->bindAndAddMethod(Procedure("TELCOVOICEMgrHal_GetPhyInterface", PARAMS_BY_NAME, JSON_STRING, "index", JSON_INTEGER, "flag", JSON_INTEGER, "paramName", JSON_STRING, NULL), &TELCOVOICEMgrHal::TELCOVOICEMgrHal_GetPhyInterface);

                }

                bool initialize(IN const char* szVersion);
                bool cleanup(const char*);
                std::string testmodulepre_requisites();
                bool testmodulepost_requisites();

                void TELCOVOICEMgrHal_Init(IN const Json::Value& req, OUT Json::Value& response);
                void TELCOVOICEMgrHal_InitData(IN const Json::Value& req, OUT Json::Value& response);
                void TELCOVOICEMgrHal_GetParamValue(IN const Json::Value& req, OUT Json::Value& response);
                void TELCOVOICEMgrHal_SetParamValue(IN const Json::Value& req, OUT Json::Value& response);
                void TELCOVOICEMgrHal_GetLineStats(IN const Json::Value& req, OUT Json::Value& response);
                void TELCOVOICEMgrHal_GetCapabilities(IN const Json::Value& req, OUT Json::Value& response);
                void TELCOVOICEMgrHal_GetVoiceProfile(IN const Json::Value& req, OUT Json::Value& response);
                void TELCOVOICEMgrHal_GetPhyInterface(IN const Json::Value& req, OUT Json::Value& response);
};
#endif

