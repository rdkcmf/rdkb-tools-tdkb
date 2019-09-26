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
#ifndef __SSP_TDK_DHCP_HAL_WRP_H__
#define __SSP_TDK_DHCP_HAL_WRP_H__
#include "dhcpv4c_api.h"

#ifdef __cplusplus
extern "C"
{
#endif
	int ssp_get_ecm_config_attempts(int *pDhcpValue);
	int ssp_get_ecm_dhcp_svr(unsigned int *pDhcpValue);
	int ssp_get_ecm_dns_svrs(dhcpv4c_ip_list_t *pList);
	int ssp_get_ecm_fsm_state(int *pDhcpValue);
	int ssp_get_ecm_gw(unsigned int *pDhcpValue);
	int ssp_get_ecm_ifname(char *pName);
	int ssp_get_ecm_ip_addr(unsigned int *pDhcpValue);
	int ssp_get_ecm_lease_time(unsigned int *pDhcpValue);
	int ssp_get_ecm_mask(unsigned int *pDhcpValue);
	int ssp_get_ecm_remain_lease_time(unsigned int *pDhcpValue);
	int ssp_get_ecm_remain_rebind_time(unsigned int *pDhcpValue);
	int ssp_get_ecm_remain_renew_time(unsigned int *pDhcpValue);
	int ssp_get_emta_remain_lease_time(unsigned int *pDhcpValue);
	int ssp_get_emta_remain_rebind_time(unsigned int *pDhcpValue);
	int ssp_get_emta_remain_renew_time(unsigned int *pDhcpValue);
	int ssp_get_ert_config_attempts(int *pDhcpValue);
	int ssp_get_ert_dhcp_svr(unsigned int *pDhcpValue);
	int ssp_get_ert_dns_svrs(dhcpv4c_ip_list_t *pList);
	int ssp_get_ert_fsm_state(int *pDhcpValue);
	int ssp_get_ert_gw(unsigned int *pDhcpValue);
	int ssp_get_ert_ifname(char *pName);
	int ssp_get_ert_ip_addr(unsigned int *pDhcpValue);
	int ssp_get_ert_lease_time(unsigned int *pDhcpValue);
	int ssp_get_ert_mask(unsigned int *pDhcpValue);
	int ssp_get_ert_remain_lease_time(unsigned int *pDhcpValue);
	int ssp_get_ert_remain_rebind_time(unsigned int *pDhcpValue);
	int ssp_get_ert_remain_renew_time(unsigned int *pDhcpValue);
#ifdef __cplusplus
}
#endif
#endif
