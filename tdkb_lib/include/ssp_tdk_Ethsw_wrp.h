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
#ifndef __SSP_TDK_ETHSW_WRP_H__
#define __SSP_TDK_ETHSW_WRP_H__
#include "ccsp_hal_ethsw.h"

#ifdef __cplusplus
extern "C"
{
#endif
	int ssp_ethsw_stub_hal_Init(void);
	int ssp_ethsw_stub_hal_GetAdminPortStatus(int portId, char *pAdminStatus, int isNegativeScenario);
	int ssp_ethsw_stub_hal_GetPortCfg(int portID, char *pDuplexMode, int *pBitRate, int isNegativeScenario);
	int ssp_ethsw_stub_hal_GetPort_Status(int portId, char *pLinkStatus, int *pBitRate, int isNegativeScenario);
	int ssp_ethsw_stub_hal_LocatePort_By_MacAddress(char *pmacAddr, int *pPortId, int isNegativeScenario);
	int ssp_ethsw_stub_hal_SetPortCfg(int portId, int linkRate, char *pDuplexmode);
	int ssp_ethsw_stub_hal_SetPortAdminStatus(int portId, char *pAdminStatus);
	int ssp_ethsw_stub_hal_SetAgingSpeed(int portId, int agingSpeed);
	int ssp_ethsw_stub_hal_Get_AssociatedDevice(unsigned long int *array_size,eth_device_t *eth_device_conf, int isNegativeScenario);
#ifdef __cplusplus
}
#endif
#endif
