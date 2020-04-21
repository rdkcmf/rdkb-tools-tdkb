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
                        this->bindAndAddMethod(Procedure("EPONHAL_GetFirmwareInfo", PARAMS_BY_NAME, JSON_STRING, NULL), &EPONHAL::EPONHAL_GetFirmwareInfo);
                        this->bindAndAddMethod(Procedure("EPONHAL_GetEponChipInfo", PARAMS_BY_NAME, JSON_STRING, NULL), &EPONHAL::EPONHAL_GetEponChipInfo);
                        this->bindAndAddMethod(Procedure("EPONHAL_GetManufacturerInfo", PARAMS_BY_NAME, JSON_STRING, NULL), &EPONHAL::EPONHAL_GetManufacturerInfo);
                        this->bindAndAddMethod(Procedure("EPONHAL_GetOnuPacketBufferCapabilities", PARAMS_BY_NAME, JSON_STRING, NULL), &EPONHAL::EPONHAL_GetOnuPacketBufferCapabilities);
                        this->bindAndAddMethod(Procedure("EPONHAL_GetOnuId", PARAMS_BY_NAME, JSON_STRING, NULL), &EPONHAL::EPONHAL_GetOnuId);
                        this->bindAndAddMethod(Procedure("EPONHAL_GetMaxLogicalLinks", PARAMS_BY_NAME, JSON_STRING, NULL), &EPONHAL::EPONHAL_GetMaxLogicalLinks);
                        this->bindAndAddMethod(Procedure("EPONHAL_GetDeviceSysDescrInfo", PARAMS_BY_NAME, JSON_STRING, NULL), &EPONHAL::EPONHAL_GetDeviceSysDescrInfo);
                        this->bindAndAddMethod(Procedure("EPONHAL_GetLlidForwardingState", PARAMS_BY_NAME, JSON_STRING,"numEntries",JSON_INTEGER, NULL), &EPONHAL::EPONHAL_GetLlidForwardingState);
                        this->bindAndAddMethod(Procedure("EPONHAL_GetOamFrameRate", PARAMS_BY_NAME, JSON_STRING,"numEntries",JSON_INTEGER, NULL), &EPONHAL::EPONHAL_GetOamFrameRate);
                        this->bindAndAddMethod(Procedure("EPONHAL_GetDynamicMacTable", PARAMS_BY_NAME, JSON_STRING,"numEntries",JSON_INTEGER, NULL), &EPONHAL::EPONHAL_GetDynamicMacTable);
                        this->bindAndAddMethod(Procedure("EPONHAL_GetOnuLinkStatistics", PARAMS_BY_NAME, JSON_STRING,"numEntries",JSON_INTEGER,NULL), &EPONHAL::EPONHAL_GetOnuLinkStatistics);
                        this->bindAndAddMethod(Procedure("EPONHAL_GetStaticMacTable", PARAMS_BY_NAME, JSON_STRING,"numEntries",JSON_INTEGER, NULL), &EPONHAL::EPONHAL_GetStaticMacTable);
                        this->bindAndAddMethod(Procedure("EPONHAL_SetClearOnuLinkStatistics", PARAMS_BY_NAME, JSON_STRING, NULL), &EPONHAL::EPONHAL_SetClearOnuLinkStatistics);
                        this->bindAndAddMethod(Procedure("EPONHAL_SetResetOnu", PARAMS_BY_NAME, JSON_STRING, NULL), &EPONHAL::EPONHAL_SetResetOnu);
                }

                bool initialize(IN const char* szVersion);
                bool cleanup(const char*);
                std::string testmodulepre_requisites();
                bool testmodulepost_requisites();

                void EPONHAL_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetFirmwareInfo(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetEponChipInfo(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetManufacturerInfo(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetOnuPacketBufferCapabilities(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetOnuId(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetMaxLogicalLinks(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetDeviceSysDescrInfo(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetLlidForwardingState(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetOamFrameRate(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetDynamicMacTable(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetOnuLinkStatistics(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_GetStaticMacTable(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_SetClearOnuLinkStatistics(IN const Json::Value& req, OUT Json::Value& response);
                void EPONHAL_SetResetOnu(IN const Json::Value& req, OUT Json::Value& response);
};
#endif
