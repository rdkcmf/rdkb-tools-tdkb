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
#include "ssp_tdk_dhcp_hal_wrp.h"
#include "ssp_hal_logger.h"

/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_config_attempts
 ** Description          : This function will  Gets the E-Router Number of Attemts to Configure
 ** @param [in]          : pDhcpValue
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_config_attempts(int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ecm_config_attempts wrapper function\n");

	if(dhcpv4c_get_ecm_config_attempts(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ecm_config_attempts function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_dhcp_svr
 ** Description          : This function will  Gets the ECM DHCP Server IP Address
 ** @param [in]          : pDhcpValue
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_dhcp_svr(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ecm_dhcp_svr wrapper\n");

	if(dhcpv4c_get_ecm_dhcp_svr(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ecm_dhcp_svr function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_dns_svrs
 ** Description          : This function will Gets the ECM List of DNS Servers
 ** @param [in]          : pList - List of IP Addresses (of DNS Servers)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_dns_svrs(dhcpv4c_ip_list_t *pList)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ecm_dns_svrs wrapper\n");

	if(dhcpv4c_get_ecm_dns_svrs(pList) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ecm_dns_svrs function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_fsm_state
 ** Description          : This function will Gets the ECM DHCP State
 ** @param [in]          : pDhcpValue - State of the DHCP (RENEW/ACQUIRED etc)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_fsm_state(int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ecm_fsm_state wrapper\n");

	if(dhcpv4c_get_ecm_fsm_state(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ecm_fsm_state function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_gw
 ** Description          : This function will Gets the ECM Gateway IP Address
 ** @param [in]          : pDhcpValue - IP Address of Gateway
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_gw(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ecm_gw wrapper\n");

	if(dhcpv4c_get_ecm_gw(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR," dhcpv4c_get_ecm_gw function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_ifname
 ** Description          : This function will Gets the ECM Interface Name
 ** @param [in]          : pName - Name of the Interface
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_ifname(char *pName)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering ssp_get_ecm_ifname wrapper\n");

	if(dhcpv4c_get_ecm_ifname(pName) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR," dhcpv4c_get_ecm_ifname function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_ip_addr
 ** Description          : This function will Gets the ECM Interface IP Address
 ** @param [in]          : pDhcpValue - IP Address of the Interface.
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_ip_addr(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ecm_ip_addr wrapper\n");

	if(dhcpv4c_get_ecm_ip_addr(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ecm_ip_addr function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_lease_time
 ** Description          : This function will Gets the ECM Offered Lease Time.
 ** @param [in]          : pDhcpValue - Value in Seconds.
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_lease_time(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ecm_lease_time wrapper\n");

	if(dhcpv4c_get_ecm_lease_time(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ecm_lease_time function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_mask
 ** Description          : This function will Gets the ECM Interface Subnet Mask.
 ** @param [in]          : pDhcpValue - Subnet Mask (bitmask)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_mask(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ecm_mask wrapper\n");

	if(dhcpv4c_get_ecm_mask(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ecm_mask function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_remain_lease_time
 ** Description          : This function will Gets the ECM Remaining Lease Time
 ** @param [in]          : pDhcpValue - Value in Seconds.
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_remain_lease_time(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the dhcpv4c_get_ecm_remain_lease_time wrapper\n");

	if(dhcpv4c_get_ecm_remain_lease_time(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ecm_remain_lease_time function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_remain_rebind_time
 ** Description          : This function will Gets the ECM Interface Remaining time to Rebind.
 ** @param [in]          : pDhcpValue - Value in Seconds.
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_remain_rebind_time(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ecm_remain_rebind_time wrapper\n");

	if(dhcpv4c_get_ecm_remain_rebind_time(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ecm_remain_rebind_time function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ecm_remain_renew_time
 ** Description          : This function will Gets the ECM Interface Remaining time to Renew.
 ** @param [in]          : pDhcpValue - Value in Seconds.
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ecm_remain_renew_time(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the get_ecm_remain_renew_time wrapper\n");

	if(dhcpv4c_get_ecm_remain_renew_time(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ecm_remain_renew_time function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_emta_remain_lease_time
 ** Description          : This function will Gets the E-MTA interface Least Time
 ** @param [in]          : pDhcpValue - Value in Seconds
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_emta_remain_lease_time(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_emta_remain_lease_time wrapper\n");

	if(dhcpv4c_get_emta_remain_lease_time(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_emta_remain_lease_time function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_emta_remain_rebind_time
 ** Description          : This function will Gets the E-MTA interface Remaining Time to Rebind
 ** @param [in]          : pDhcpValue - Value in Seconds
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_emta_remain_rebind_time(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_emta_remain_rebind_time wrapper\n");

	if(dhcpv4c_get_emta_remain_rebind_time(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_emta_remain_rebind_time function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_emta_remain_renew_time
 ** Description          : This function will Gets the E-MTA interface Remaining Time to Renew
 ** @param [in]          : pDhcpValue - Value in Seconds.
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_emta_remain_renew_time(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_emta_remain_renew_time wrapper\n");

	if(dhcpv4c_get_emta_remain_renew_time(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_emta_remain_renew_time function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ert_config_attempts
 ** Description          : This function will Gets the E-Router Number of Attemts to Configure
 ** @param [in]          : pDhcpValue - Count.
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_config_attempts(int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ert_config_attempts wrapper\n");

	if(dhcpv4c_get_ert_config_attempts(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_config_attempts function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ert_dhcp_svr
 ** Description          : This function will Gets the E-Router DHCP Server IP Address
 ** @param [in]          : pDhcpValue - IP Address (of DHCP Server)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_dhcp_svr(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ert_dhcp_svr wrapper\n");

	if(dhcpv4c_get_ert_dhcp_svr(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_dhcp_svr function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ert_dns_svrs
 ** Description          : This function will Gets the E-Router List of DNS Servers
 ** @param [in]          : pList - List of IP Address (of DNS Servers)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_dns_svrs(dhcpv4c_ip_list_t *pList)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ert_dns_svrs wrapper\n");

	if(dhcpv4c_get_ert_dns_svrs(pList) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_dns_svrs function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ert_fsm_state
 ** Description          : This function will Gets the E-Router DHCP State
 ** @param [in]          : pDhcpValue - State of the DHCP (RENEW/ACQUIRED etc.)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_fsm_state(int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ert_fsm_state wrapper\n");

	if(dhcpv4c_get_ert_fsm_state(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_fsm_state function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ert_gw
 ** Description          : This function will Gets the E-Router Gateway IP Address
 ** @param [in]          : pDhcpValue - IP Address (of the Gateway)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_gw(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ert_gw wrapper\n");

	if(dhcpv4c_get_ert_gw(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_gw function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 ** Function Name       : ssp_get_ert_ifname
 ** Description         : This function will Gets the E-Router Interface Name.
 ** @param [in]         : pName - Interface Name (e.g. ert0)
 ** @param [out]        : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_ifname(char *pName)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering ssp_get_ert_ifname wrapper");
	if(dhcpv4c_get_ert_ifname(pName) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_ifname function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ert_ip_addr
 ** Description          : This function will Gets the E-Router Interface Name
 ** @param [in]          : pName - Interface Name (e.g. ert0)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_ip_addr(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ert_ip_addr wrapper\n");

	if(dhcpv4c_get_ert_ip_addr(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_ip_addr function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ert_lease_time
 ** Description          : This function will Gets the E-Router Offered Lease Time
 ** @param [in]          : pDhcpValue - Value in Seconds.
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_lease_time(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ert_lease_time wrapper\n");

	if(dhcpv4c_get_ert_lease_time(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_lease_time function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ert_mask
 ** Description          : This function will Gets the E-Router Subnet Mask
 ** @param [in]          : pDhcpValue - Subnet Mask (bitmask)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_mask(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ert_mask wrapper\n");

	if(dhcpv4c_get_ert_mask(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_mask function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ert_remain_lease_time
 ** Description          : This function will Gets the E-Router Remaining Lease Time
 ** @param [in]          : pDhcpValue - Value in Seconds
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_remain_lease_time(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ert_remain_lease_time wrapper\n");

	if(dhcpv4c_get_ert_remain_lease_time(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_remain_lease_time functiion returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ert_remain_rebind_time
 ** Description          : This function will Gets the E-Router Remaining Lease Time
 ** @param [in]          : pDhcpValue - Value in Seconds.
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_remain_rebind_time(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ert_remain_rebind_time wrapper\n");

	if(dhcpv4c_get_ert_remain_rebind_time(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_remain_rebind_time function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_get_ert_remain_renew_time
 ** Description          : This function will Gets the E-Router Interface Remaining Time to Renew
 ** @param [in]          : pDhcpValue - Value in Seconds
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_get_ert_remain_renew_time(unsigned int *pDhcpValue)
{
	DEBUG_PRINT(DEBUG_TRACE,"Entering the ssp_get_ert_remain_renew_time wrapper\n");

	if(dhcpv4c_get_ert_remain_renew_time(pDhcpValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR,"dhcpv4c_get_ert_remain_renew_time function returns failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}
