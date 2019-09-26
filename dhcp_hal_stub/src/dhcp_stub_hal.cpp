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
 ******************************************************************************/
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include "dhcp_stub_hal.h"

#define MAX_BUFFER_SIZE 128
#define MAX_STRING_SIZE 64
#define MAX_BUFFER_SIZE_TO_SEND 512
#define RETURN_SUCCESS 0
#define RETURN_FAILURE 1
#define TEST_SUCCESS true
#define TEST_FAILURE false
#define free_tdk(arg) if(arg != NULL) \
{ \
	free(arg); \
	arg = NULL; \
}

#define CHECK_PARAM_AND_RET(x) if ((x) == NULL) \
{ \
      DEBUG_PRINT(DEBUG_ERROR,"!!!NULL Pointer!!! :: %s:%d\n", __func__, __LINE__); \
      return TEST_FAILURE; \
}

struct in_addr ip_addr1;

/****************************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for registering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return string "SUCCESS" in case of success else return string "FAILURE"
 ******************************************************************************************/
std::string dhcp_stub_hal::testmodulepre_requisites()
{
	/*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
	return "SUCCESS";
}

/*********************************************************************************************
 *Function name : testmodulepost_requisites
 *Description   : testmodulepost_requisites will be used for unregistering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return TEST_SUCCESS in case of success else return TEST_FAILURE
 *********************************************************************************************/
bool dhcp_stub_hal::testmodulepost_requisites()
{
	/*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
	return TEST_SUCCESS;
}

/************************************************************************************
 *Function name : dhcp_stub_hal_Init
 *Description   : This function is used to register all the dhcp_stub_hal methods.
 *@param [in]   : szVersion - version, ptrAgentObj - Agent obhect
 *@param [out]  : response - filled with SUCCESS or FAILURE(if any error is detected)
 ************************************************************************************/
bool dhcp_stub_hal::initialize(IN const char* szVersion)
{
	DEBUG_PRINT(DEBUG_TRACE, "dhcp_stub_hal Initialize\n");
	return TEST_SUCCESS;
}

/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_config_attempts
 * Description   : This function calls the wrapper function(ssp_get_ecm_config_attempts) to retrieve the ECM Offered Lease Time
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_config_attempts(IN const Json::Value& req, OUT Json::Value& response)
{
	int dhcp_pVal = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ecm_config_attempts stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_config_attempts(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_config_attempts(&dhcp_pVal);
	}
	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%d", dhcp_pVal);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_config_attempts has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_dhcp_svr
 * Description   : This function calls the wrapper function(ssp_get_ecm_dhcp_svr) to retrieve the ECM DHCP Server IP Address
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_dhcp_svr(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ecm_dhcp_svr stub\n");
	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_dhcp_svr(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_dhcp_svr(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		ip_addr1.s_addr = dhcpValue;
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%s", inet_ntoa(ip_addr1));
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_dhcp_svr has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_dns_svrs
 * Description   : This function calls the wrapper function(ssp_get_ecm_dns_svrs) to retrieve the ECM List of DNS Servers
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_dns_svrs(IN const Json::Value& req, OUT Json::Value& response)
{
	int i = 0;
	int isNegativeScenario = 0;
	dhcpv4c_ip_list_t ipList = {0};
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ecm_dns_svrs stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_dns_svrs(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_dns_svrs(&ipList);
	}

	if(result == RETURN_SUCCESS)
	{
		for(i = 0; i < ipList.number; i++)
		{
			ip_addr1.s_addr = ipList.addrs[i];
			snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "/%s/%d/", inet_ntoa(ip_addr1), ipList.number);
		}

		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_dns_svrs has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_fsm_state
 * Description   : This function calls the wrapper function(ssp_get_ecm_fsm_state) to retrieve the ECM DHCP State(RENEW/ACQUIRED  etc)
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_fsm_state(IN const Json::Value& req, OUT Json::Value& response)
{
	int dhcp_pVal = -1;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ecm_fsm_state stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_fsm_state(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_fsm_state(&dhcp_pVal);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%d", dhcp_pVal);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_fsm_state has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_gw
 * Description   : This function calls the wrapper function(ssp_get_ecm_gw) to retrieve the ECM Gateway IP Address
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_gw(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ecm_gw stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_gw(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_gw(&dhcpValue);
	}
	if(result == RETURN_SUCCESS)
	{
		ip_addr1.s_addr = dhcpValue;
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%s", inet_ntoa(ip_addr1));
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_gw has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_ifname
 * Description   : This function calls the wrapper function(ssp_get_ecm_ifname) to retrieve the ECM Interface Name (e.g doc0)
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_ifname(IN const Json::Value& req, OUT Json::Value& response)
{
	char ifName[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ecm_ifname stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_ifname(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_ifname(ifName);
	}

	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = ifName;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, ifName);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_ifname has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_ip_addr
 * Description   : This function calls the wrapper function(ssp_get_ecm_ip_addr) to retrieve the ECM Interface IP Address
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_ip_addr(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ecm_ip_addr stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_ip_addr(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_ip_addr(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		ip_addr1.s_addr = dhcpValue;
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%s", inet_ntoa(ip_addr1));
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_ip_addr has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_lease_time
 * Description   : This function calls the wrapper function(ssp_get_ecm_lease_time) to
		   retrieve the ECM Offered Lease Time value in Seconds
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_lease_time(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ecm_lease_time stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_lease_time(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_lease_time(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%u", dhcpValue);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_lease_time has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_mask
 * Description   : This function calls the wrapper function(ssp_get_ecm_mask) to retrieve the ECM Interface Subnet Mask
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_mask(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ecm_mask stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_mask(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_mask(&dhcpValue);
	}
	if(result == RETURN_SUCCESS)
	{
		ip_addr1.s_addr = dhcpValue;
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%s", inet_ntoa(ip_addr1));
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_mask has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_remain_lease_time
 * Description   : This function calls the wrapper function(ssp_get_ecm_remain_lease_time) to
		   retrieve the ECM Remaining Lease Time value in seconds
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_remain_lease_time(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ecm_remain_lease_time stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_remain_lease_time(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_remain_lease_time(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%u", dhcpValue);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_remain_lease_time has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_remain_rebind_time
 * Description   : This function calls the wrapper function(ssp_get_ecm_remain_rebind_time) to
		   retrieve the ECM Interface Remaining time to Rebind value in seconds.
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_remain_rebind_time(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function get_ecm_remain_rebind_time stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_remain_rebind_time(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_remain_rebind_time(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%u", dhcpValue);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_remain_rebind_time has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ecm_remain_renew_time
 * Description   : This function calls the wrapper function(ssp_get_ecm_remain_renew_time) to
		   retrieve the ECM Interface Remaining time to Renew value in seconds
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ecm_remain_renew_time(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ecm_remain_renew_time stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ecm_remain_renew_time(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ecm_remain_renew_time(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%u", dhcpValue);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ecm_remain_renew_time has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_emta_remain_lease_time
 * Description   : This function calls the wrapper function(ssp_get_emta_remain_lease_time)
		   to retrieve the E-MTA interface Least Time value in seconds
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_emta_remain_lease_time(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_emta_remain_lease_time stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_emta_remain_lease_time(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_emta_remain_lease_time(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%u", dhcpValue);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_emta_remain_lease_time has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/******************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_emta_remain_rebind_time
 * Description   : This function calls the wrapper function(ssp_get_emta_remain_rebind_time) to
		   retrieve the E-MTA interface Remaining Time to Rebind value in seconds
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_emta_remain_rebind_time(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_emta_remain_rebind_time stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_emta_remain_rebind_time(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_emta_remain_rebind_time(&dhcpValue);
	}
	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%u", dhcpValue);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_emta_remain_rebind_time has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/*****************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_emta_remain_renew_time
 * Description   : This function calls the wrapper function(ssp_get_emta_remain_renew_time) to
		   retrieve the E-MTA interface Remaining Time to Renew value in seconds
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_emta_remain_renew_time(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_emta_remain_renew_time stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_emta_remain_renew_time(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_emta_remain_renew_time(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%u", dhcpValue);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_emta_remain_renew_time has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/*************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ert_config_attempts
 * Description   : This function calls the wrapper function(ssp_get_ert_config_attempts) to
		   retrieve the E-Router Number of Attemts to Configure
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_config_attempts(IN const Json::Value& req, OUT Json::Value& response)
{
	int dhcp_pVal = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ert_config_attempts stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_config_attempts(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_config_attempts(&dhcp_pVal);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%d", dhcp_pVal);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_config_attempts has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ert_dhcp_svr
 * Description   : This function calls the wrapper function(ssp_get_ert_dhcp_svr) to retrieve the E-Router DHCP Server IP Address
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_dhcp_svr(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function get_ert_dhcp_svr stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_dhcp_svr(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_dhcp_svr(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		ip_addr1.s_addr = dhcpValue;
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%s", inet_ntoa(ip_addr1));
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_dhcp_svr has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/******************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ert_dns_svrs
 * Description   : This function calls the wrapper function(ssp_get_ert_dns_svrs) to
		   retrieve the E-Router List of DNS Servers(List of IP Address (of DNS Servers))
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *******************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_dns_svrs(IN const Json::Value& req, OUT Json::Value& response)
{
	int i = 0;
	dhcpv4c_ip_list_t ipList = {0};
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ert_dns_svrs stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_dns_svrs(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_dns_svrs(&ipList);
	}

	if(result == RETURN_SUCCESS)
	{
		for(i = 0; i< ipList.number; i++)
		{
			ip_addr1.s_addr = ipList.addrs[i];
			snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "/%s/%d/", inet_ntoa(ip_addr1), ipList.number);
		}
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_dns_svrs has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/*******************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ert_fsm_state
 * Description   : This function calls the wrapper function(ssp_get_ert_fsm_state) to
		   retrieve the E-Router DHCP State (State of the DHCP (RENEW/ACQUIRED etc.))
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ********************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_fsm_state(IN const Json::Value& req, OUT Json::Value& response)
{
	int dhcp_pVal = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ert_fsm_state stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_fsm_state(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_fsm_state(&dhcp_pVal);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%d", dhcp_pVal);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_fsm_state has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ert_gw
 * Description   : This function calls the wrapper function(ssp_get_ert_gw) to
		   retrieve the E-Router Gateway IP Address (IP Address (of the Gateway))
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_gw(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ert_gw stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_gw(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_gw(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		ip_addr1.s_addr = dhcpValue;
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%s", inet_ntoa(ip_addr1));

		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_gw has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ert_ifname
 * Description   : This function calls the wrapper function(ssp_get_ert_ifname) to retrieve the E-Router Interface Name(e.g. ert0).
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_ifname(IN const Json::Value& req, OUT Json::Value& response)
{
	char ifName[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ert_ifname stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_ifname(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_ifname(ifName);
	}

	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = ifName;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, ifName);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_ifname has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/*****************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ert_ip_addr
 * Description   : This function calls the wrapper function(ssp_get_ert_ip_addr) to
		   retrieve the E-Router Interface IP Address (IP Address (of the Interface)).
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_ip_addr(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ert_ip_addr stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_ip_addr(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_ip_addr(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		ip_addr1.s_addr = dhcpValue;
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%s", inet_ntoa(ip_addr1));
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_ip_addr has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/********************************************************************************************************
 * Function Name : dhcp_stub_hal_get_ert_lease_time
 * Description   : This function calls the wrapper function(ssp_get_ert_lease_time) to
		   retrieve the E-Router Offered Lease Time value is seconds
 * @param [in]   : req - request sent by Test Manager
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *********************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_lease_time(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ert_lease_time stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_lease_time(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_lease_time(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%u", dhcpValue);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_lease_time has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/********************************************************************************************************************
 * Function Name    : dhcp_stub_hal_get_ert_mask
 * Description      : This function calls the wrapper function(ssp_get_ert_mask) to retrieve the E-Router Subnet Mask
 * @param [in]      : req - request sent by Test Manager
 * @param [out]     : response - filled with SUCCESS or FAILURE based on the return value
 ********************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_mask(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ert_mask stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_mask(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_mask(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		ip_addr1.s_addr = dhcpValue;
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%s", inet_ntoa(ip_addr1));
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_mask has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/****************************************************************************************************************
 * Function Name    : dhcp_stub_hal_get_ert_remain_lease_time
 * Description      : This function calls the wrapper function(ssp_get_ert_remain_lease_time) to
		      retrieve the E-Router Remaining Lease Time value in seconds
 * @param [in]      : req - request sent by Test Manager
 * @param [out]     : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_remain_lease_time(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ert_remain_lease_time stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_remain_lease_time(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_remain_lease_time(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%u", dhcpValue);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_remain_lease_time has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/*****************************************************************************************************************
 * Function Name    : dhcp_stub_hal_get_ert_remain_rebind_time
 * Description      : This function calls the wrapper function(ssp_get_ert_remain_rebind_time) to
		      retrieve the E-Router Interface Remaining Time to Rebind value in seconds
 * @param [in]      : req - request sent by Test Manager
 * @param [out]     : response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_remain_rebind_time(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function get_ert_remain_rebind_time stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_remain_rebind_time(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_remain_rebind_time(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%u", dhcpValue);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_remain_rebind_time has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***************************************************************************************************************
 * Function Name    : dhcp_stub_hal_get_ert_remain_renew_time
 * Description      : This function calls the wrapper function(ssp_get_ert_remain_renew_time)
		      to retrieve the E-Router Interface Remaining Time to Renew value in seconds
 * @param [in]      : req - request sent by Test Manager
 * @param [out]     : response - filled with SUCCESS or FAILURE based on the return value
****************************************************************************************************************/
void dhcp_stub_hal::dhcp_stub_hal_get_ert_remain_renew_time(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned int dhcpValue = 0;
	int isNegativeScenario = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function  get_ert_remain_renew_time stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_get_ert_remain_renew_time(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_get_ert_remain_renew_time(&dhcpValue);
	}

	if(result == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%u", dhcpValue);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, resultDetails);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "get_ert_remain_renew_time has been failure";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/*******************************************************************************************
 * Function Name    : erouter_ip_stub_get_ip_address
 * Description      : This function is used to retrieve IP address of the erouter interface
 * @param [in]      : req - request sent by Test Manager
 * @param [out]     : response - filled with SUCCESS or FAILURE(if any error is detected)
 *******************************************************************************************/
void dhcp_stub_hal::erouter_ip_stub_get_ip_address(IN const Json::Value& req, OUT Json::Value& response)
{
	int fd;
	struct ifreq ifrequest;
	char interface[] = "erouter0";
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};

	DEBUG_PRINT(DEBUG_TRACE, "Inside Function erouter_ip_stub_get_ip_address\n");

	fd = socket(AF_INET, SOCK_DGRAM, 0);

	ifrequest.ifr_addr.sa_family = AF_INET;

	strncpy(ifrequest.ifr_name, interface, IFNAMSIZ - 1);
	ioctl(fd, SIOCGIFADDR, &ifrequest);
	snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND,
			"%s", inet_ntoa(((struct sockaddr_in *)&ifrequest.ifr_addr )->sin_addr));

	response["result"] = "SUCCESS";
	response["details"] = resultDetails;
	return;
}


/**********************************************************************************************
 *Function Name : CreateObject
 *Description   : This function is used to create a new object of the class "dhcp_stub_hal".
 *@param [in]   : None
 ********************************************************************************************/
extern "C" dhcp_stub_hal* CreateObject(TcpSocketServer &ptrtcpServer)
{
	return new dhcp_stub_hal(ptrtcpServer);
}


/**************************************************************************************
 *Function Name : cleanup
 *Description   : This function will be used to unregister the methods of dhcp_stub_hal
 *@param [in]   : szVersion - version, ptrAgentObj - Agent object
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
bool dhcp_stub_hal::cleanup(IN const char* szVersion)
{
	DEBUG_PRINT(DEBUG_TRACE, "cleaning up\n");
	return TEST_SUCCESS;
}

/*********************************************************************************
 *Function Name : DestroyObject
 *Description   : This function will be used to destory the dhcp_stub_hal object.
 *@param [in]   : dhcp_stub_hal Object
 **********************************************************************************/
extern "C" void DestroyObject(dhcp_stub_hal *stubobj)
{
	DEBUG_PRINT(DEBUG_TRACE, "Destroying HAL object\n");
	delete stubobj;
}
