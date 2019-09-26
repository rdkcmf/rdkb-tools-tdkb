/*
 * Copyright 2016-2017 Intel Corporation
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
#ifndef __ETHSW_STUB_HAL_H__
#define __ETHSW_STUB_HAL_H__

#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include "ssp_tdk_Ethsw_wrp.h"
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>

/* for reference added it,(IN) indicates accepting the request from Test Manager and (OUT)
   indicates sending the response for the request back to the Manager */
#ifndef IN
#define IN
#endif

#ifndef OUT
#define OUT
#endif

using namespace std;
/* RDKTestAgent : This Class provides interface for the module to enable RPC mechanism. */
class RDKTestAgent;
/* RDKTestStubInterface : This Class provides provides interface for the modules.  */
class ethsw_stub_hal : public RDKTestStubInterface, public AbstractServer<ethsw_stub_hal>
{
	public:

		ethsw_stub_hal(TcpSocketServer &ptrRpcServer) : AbstractServer <ethsw_stub_hal>(ptrRpcServer)
		{
			this->bindAndAddMethod(Procedure("ethsw_stub_hal_Get_Port_Admin_Status", PARAMS_BY_NAME, JSON_STRING, "PortID", JSON_INTEGER, "flag", JSON_INTEGER, NULL), &ethsw_stub_hal::ethsw_stub_hal_Get_Port_Admin_Status);
			this->bindAndAddMethod(Procedure("ethsw_stub_hal_Get_Port_Cfg", PARAMS_BY_NAME, JSON_STRING, "PortID", JSON_INTEGER, "flag", JSON_INTEGER, NULL), &ethsw_stub_hal::ethsw_stub_hal_Get_Port_Cfg);
			this->bindAndAddMethod(Procedure("ethsw_stub_hal_Get_Port_Status", PARAMS_BY_NAME, JSON_STRING, "PortID", JSON_INTEGER, "flag", JSON_INTEGER, NULL), &ethsw_stub_hal::ethsw_stub_hal_Get_Port_Status);
			this->bindAndAddMethod(Procedure("ethsw_stub_hal_Init", PARAMS_BY_NAME, JSON_STRING,NULL), &ethsw_stub_hal::ethsw_stub_hal_Init);
			this->bindAndAddMethod(Procedure("ethsw_stub_hal_LocatePort_By_MacAddress", PARAMS_BY_NAME, JSON_STRING, "macID", JSON_STRING, "flag", JSON_INTEGER, NULL), &ethsw_stub_hal::ethsw_stub_hal_LocatePort_By_MacAddress);
			this->bindAndAddMethod(Procedure("ethsw_stub_hal_SetAgingSpeed", PARAMS_BY_NAME, JSON_STRING, "PortID", JSON_INTEGER, "AgingSpeed", JSON_INTEGER, NULL), &ethsw_stub_hal::ethsw_stub_hal_SetAgingSpeed);
			this->bindAndAddMethod(Procedure("ethsw_stub_hal_SetPortAdminStatus", PARAMS_BY_NAME, JSON_STRING, "PortID", JSON_INTEGER, "adminstatus", JSON_STRING, NULL), &ethsw_stub_hal::ethsw_stub_hal_SetPortAdminStatus);
			this->bindAndAddMethod(Procedure("ethsw_stub_hal_SetPortCfg", PARAMS_BY_NAME, JSON_STRING, "PortID", JSON_INTEGER, "linkrate", JSON_INTEGER, "mode", JSON_STRING, NULL), &ethsw_stub_hal::ethsw_stub_hal_SetPortCfg);
			this->bindAndAddMethod(Procedure("ethsw_stub_hal_Get_AssociatedDevice", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER,  NULL), &ethsw_stub_hal::ethsw_stub_hal_Get_AssociatedDevice);
		}

		bool initialize(IN const char* szVersion);
		bool cleanup(const char*);
		std::string testmodulepre_requisites();
		bool testmodulepost_requisites();

		void ethsw_stub_hal_Get_Port_Admin_Status(const Json::Value&, Json::Value&);
		void ethsw_stub_hal_Get_Port_Cfg(const Json::Value&, Json::Value&);
		void ethsw_stub_hal_Get_Port_Status(const Json::Value&, Json::Value&);
		void ethsw_stub_hal_Init(IN const Json::Value& req, OUT Json::Value& response);
		void ethsw_stub_hal_LocatePort_By_MacAddress(IN const Json::Value& req, OUT Json::Value& response);
		void ethsw_stub_hal_SetAgingSpeed(IN const Json::Value& req, OUT Json::Value& response);
		void ethsw_stub_hal_SetPortAdminStatus(IN const Json::Value& req, OUT Json::Value& response);
		void ethsw_stub_hal_SetPortCfg(IN const Json::Value& req, OUT Json::Value& response);
		void ethsw_stub_hal_Get_AssociatedDevice(IN const Json::Value& req, OUT Json::Value& response);
};
#endif
