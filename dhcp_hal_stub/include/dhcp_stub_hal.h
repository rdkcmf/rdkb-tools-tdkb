/****************************************************************************
  Copyright 2016-2017 Intel Corporation

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*******************************************************************************/

#ifndef __DHCP_STUB_HAL_STUB_H__
#define __DHCP_STUB_HAL_STUB_H__
#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include "ssp_tdk_dhcp_hal_wrp.h"
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>

/* for reference added it,(IN) indicates accepting the request from Test Manager
   and (OUT) indicates sending the response for the request back to the Manager
*/
#ifndef IN
#define IN
#endif

#ifndef OUT
#define OUT
#endif

using namespace std;
/* RDKTestAgent : This Class provides interface for the module to enable RPC mechanism. */
class RDKTestAgent;
/* RDKTestStubInterface : This Class provides provides interface for the modules. */
class dhcp_stub_hal : public RDKTestStubInterface, public AbstractServer<dhcp_stub_hal>
{
	public:
		dhcp_stub_hal(TcpSocketServer &ptrRpcServer) : AbstractServer <dhcp_stub_hal>(ptrRpcServer)
		{
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_config_attempts", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_config_attempts);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_dhcp_svr", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER,NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_dhcp_svr);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_dns_svrs", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_dns_svrs);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_fsm_state", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_fsm_state);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_gw", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_gw);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_ifname", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_ifname);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_ip_addr", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_ip_addr);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_lease_time", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_lease_time);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_mask", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_mask);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_remain_lease_time", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_remain_lease_time);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_remain_rebind_time", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_remain_rebind_time);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ecm_remain_renew_time", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ecm_remain_renew_time);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_emta_remain_lease_time", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_emta_remain_lease_time);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_emta_remain_rebind_time", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_emta_remain_rebind_time);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_emta_remain_renew_time", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_emta_remain_renew_time);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_config_attempts", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_config_attempts);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_dhcp_svr", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_dhcp_svr);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_dns_svrs", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_dns_svrs);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_fsm_state", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_fsm_state);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_gw", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_gw);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_ifname", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_ifname);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_ip_addr", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_ip_addr);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_lease_time", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_lease_time);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_mask", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_mask);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_remain_lease_time", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_remain_lease_time);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_remain_rebind_time", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_remain_rebind_time);
			this->bindAndAddMethod(Procedure("dhcp_stub_hal_get_ert_remain_renew_time", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::dhcp_stub_hal_get_ert_remain_renew_time);
			this->bindAndAddMethod(Procedure("erouter_ip_stub_get_ip_address", PARAMS_BY_NAME, JSON_STRING, "flag", JSON_INTEGER, NULL), &dhcp_stub_hal::erouter_ip_stub_get_ip_address);
		}

		bool initialize(IN const char* szVersion);
		bool cleanup(const char*);
		std::string testmodulepre_requisites();
		bool testmodulepost_requisites();

		void dhcp_stub_hal_get_ecm_config_attempts(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ecm_dhcp_svr(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ecm_dns_svrs(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ecm_fsm_state(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ecm_gw(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ecm_ifname(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ecm_ip_addr(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ecm_lease_time(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ecm_mask(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ecm_remain_lease_time(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ecm_remain_rebind_time(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ecm_remain_renew_time(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_emta_remain_lease_time(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_emta_remain_rebind_time(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_emta_remain_renew_time(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_config_attempts(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_dhcp_svr(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_dns_svrs(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_fsm_state(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_gw(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_ifname(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_ip_addr(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_lease_time(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_mask(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_remain_lease_time(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_remain_rebind_time(IN const Json::Value& req, OUT Json::Value& response);
		void dhcp_stub_hal_get_ert_remain_renew_time(IN const Json::Value& req, OUT Json::Value& response);
		void erouter_ip_stub_get_ip_address(IN const Json::Value& req, OUT Json::Value& response);
};
#endif
