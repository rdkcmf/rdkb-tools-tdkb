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
#include "ssp_tdk_Ethsw_wrp.h"
#include "ssp_hal_logger.h"

#define MAX_STRING_SIZE 64
#define MAXBITRATE_10    10
#define MAXBITRATE_100   100
#define MAXBITRATE_1000  1000
#define MAXBITRATE_2500  2500
#define MAXBITRATE_5000  5000
#define MAXBITRATE_10000 10000
#define MAXBITRATE_AUTO  1
#define INVALID_VALUE -1
#define ETH_WAN_LINK_UP 1
#define ETH_WAN_LINK_DOWN 0

/************************************************************************************************************
 * Function Name : ssp_ethsw_stub_hal_GetAdminPortStatus
 * Description   : This function will Retrieve the current port admin status
 * @param [in]   : portId - port id, pAdminStatus - Admin status, isNegativeScenario - for negative scenario
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ************************************************************************************************************/
int ssp_ethsw_stub_hal_GetAdminPortStatus(int portId, char *pAdminStatus, int isNegativeScenario)
{
	#if defined(INTEL_PUMA7)
        if(portId ==1)
           portId = 2;
        else if(portId ==2)
           portId =1;
        #endif
	CCSP_HAL_ETHSW_PORT port = INVALID_VALUE;
	CCSP_HAL_ETHSW_ADMIN_STATUS getAdminStatus = INVALID_VALUE;
	int result = RETURN_ERR;

	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_Port_Admin_Status wrapper\n");
	CHECK_PARAM_AND_RET(pAdminStatus);

	port = (CCSP_HAL_ETHSW_PORT)portId;

	if(isNegativeScenario)
	{
		result = CcspHalEthSwGetPortAdminStatus(port, NULL);
	}
	else
	{
		result = CcspHalEthSwGetPortAdminStatus(port, &getAdminStatus);
	}

	if(result == RETURN_OK)
	{
		switch(getAdminStatus)
		{
			case CCSP_HAL_ETHSW_AdminUp:
				{
					strncpy(pAdminStatus, "CCSP_HAL_ETHSW_AdminUp", MAX_STRING_SIZE);
					break;
				}
			case CCSP_HAL_ETHSW_AdminDown:
				{
					strncpy(pAdminStatus, "CCSP_HAL_ETHSW_AdminDown", MAX_STRING_SIZE);
					break;
				}
			case CCSP_HAL_ETHSW_AdminTest:
				{
					strncpy(pAdminStatus, "CCSP_HAL_ETHSW_AdminTest", MAX_STRING_SIZE);
					break;
				}
			default:
				{
					DEBUG_PRINT(DEBUG_TRACE, "Invalid port status");
					strncpy(pAdminStatus, "CCSP_HAL_ETHSW_AdminInvalid", MAX_STRING_SIZE);
					break;
				}
		}
	}
	else
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_Port_Admin_Status function returns failure\n");
	}

	return result;
}


/********************************************************************************************************
 * Function Name : ssp_ethsw_stub_hal_GetPortCfg
 * Description   : This function will Retrieve the current port config -- link speed, duplex mode, etc
 * @param [in]   : PortId - Port ID as defined in CCSP_HAL_ETHSW_PORT
		   pLinkRate - Receives the current link rate, as in CCSP_HAL_ETHSW_LINK_RATE
		   pDuplexMode -- Receives the current duplex mode, as in CCSP_HAL_ETHSW_DUPLEX_MODE
		   isNegativeScenario - for negative scenario
 * @param [out]  : return status an integer value 0-success and 1-Failure
 *********************************************************************************************************/
int ssp_ethsw_stub_hal_GetPortCfg(int portId, char *pDuplexMode, int *pLinkRate, int isNegativeScenario)
{
	#if defined(INTEL_PUMA7)
        if(portId ==1)
           portId = 2;
        else if(portId ==2)
           portId =1;
        #endif
	CCSP_HAL_ETHSW_PORT         port = INVALID_VALUE;
	CCSP_HAL_ETHSW_LINK_RATE    getLinkRate = INVALID_VALUE;
	CCSP_HAL_ETHSW_DUPLEX_MODE  getDuplexModeValue = INVALID_VALUE;
	int result = RETURN_ERR;

	port = (CCSP_HAL_ETHSW_PORT)portId;

	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_Port_Cfg wrapper\n");
	CHECK_PARAM_AND_RET(pDuplexMode);
	CHECK_PARAM_AND_RET(pLinkRate);

	if(isNegativeScenario)
	{
		result = CcspHalEthSwGetPortCfg(port, NULL, NULL);
	}
	else
	{
		result = CcspHalEthSwGetPortCfg(port, &getLinkRate, &getDuplexModeValue);
	}

	if(result == RETURN_OK)
	{
		switch(getLinkRate)
		{
			case CCSP_HAL_ETHSW_LINK_10Mbps:
				{
					*pLinkRate = MAXBITRATE_10;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_100Mbps:
				{
					*pLinkRate = MAXBITRATE_100;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_1Gbps:
				{
					*pLinkRate = MAXBITRATE_1000;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_2_5Gbps:
				{
					*pLinkRate = MAXBITRATE_2500;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_5Gbps:
				{
					*pLinkRate = MAXBITRATE_5000;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_10Gbps:
				{
					*pLinkRate = MAXBITRATE_10000;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_Auto:
				{
					*pLinkRate = MAXBITRATE_AUTO;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_NULL:
				{
					*pLinkRate = 0;
					break;
				}
			default:
				{
					DEBUG_PRINT(DEBUG_TRACE, "Invalid value provided\n");
					*pLinkRate = INVALID_VALUE; //Invalid value
					break;
				}
		}

		switch(getDuplexModeValue)
		{
			case CCSP_HAL_ETHSW_DUPLEX_Auto:
				{
					strncpy(pDuplexMode, "CCSP_HAL_ETHSW_DUPLEX_Auto", MAX_STRING_SIZE);
					break;
				}
			case CCSP_HAL_ETHSW_DUPLEX_Half:
				{
					strncpy(pDuplexMode, "CCSP_HAL_ETHSW_DUPLEX_Half", MAX_STRING_SIZE);
					break;
				}
			case CCSP_HAL_ETHSW_DUPLEX_Full:
				{
					strncpy(pDuplexMode, "CCSP_HAL_ETHSW_DUPLEX_Full", MAX_STRING_SIZE);
					break;
				}
			default:
				{
					DEBUG_PRINT(DEBUG_TRACE, "Invalid value provided\n");
					strncpy(pDuplexMode, "Invalid", MAX_STRING_SIZE);
					break;
				}
		}
		DEBUG_PRINT(DEBUG_TRACE, "DuplexMode = %s, MaxBitRate = %d\n", pDuplexMode, *pLinkRate);
	}
	else
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_Port_Cfg function returns failure\n");
	}

	return result;
}

/******************************************************************************************************
 * Function Name : ssp_ethsw_stub_hal_GetPort_Status
 * Description   : This function will Retrieve the current port status -- link speed, duplex mode, etc.
 * @param [in]   : portId     -- Port ID as defined in CCSP_HAL_ETHSW_PORT
		   pLinkRate   -- Receives the current link rate, as in CCSP_HAL_ETHSW_LINK_RATE
		   isNegativeScenario - for negative scenario
 *@param [out]   : return status an integer value 0-success and 1-Failure
 *******************************************************************************************************/
int ssp_ethsw_stub_hal_GetPort_Status(int portId, char *pLinkStatus, int *pLinkRate, char *pDuplexMode, int isNegativeScenario)
{
	#if defined(INTEL_PUMA7)
        if(portId ==1)
           portId = 2;
        else if(portId ==2)
           portId =1;
        #endif
	CCSP_HAL_ETHSW_PORT port = INVALID_VALUE;
	CCSP_HAL_ETHSW_LINK_RATE    getLinkRate = INVALID_VALUE;
	CCSP_HAL_ETHSW_DUPLEX_MODE  getDuplexMode = INVALID_VALUE;
	CCSP_HAL_ETHSW_LINK_STATUS  getLinkStatus = INVALID_VALUE;
	int result = RETURN_ERR;

	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_Port_Status wrapper\n");
	CHECK_PARAM_AND_RET(pLinkStatus);
	CHECK_PARAM_AND_RET(pLinkRate);
	CHECK_PARAM_AND_RET(pDuplexMode);

	port = (CCSP_HAL_ETHSW_PORT)portId;

	if(isNegativeScenario)
	{
		result = CcspHalEthSwGetPortStatus(port, NULL, NULL, NULL);
	}
	else
	{
		result = CcspHalEthSwGetPortStatus(port, &getLinkRate, &getDuplexMode, &getLinkStatus);
	}

	if(result == RETURN_OK)
	{
		switch(getLinkStatus)
		{
			case CCSP_HAL_ETHSW_LINK_Up:
				{
					strncpy(pLinkStatus, "CCSP_HAL_ETHSW_LINK_Up", MAX_STRING_SIZE);
					break;
				}
			case CCSP_HAL_ETHSW_LINK_Down:
				{
					strncpy(pLinkStatus, "CCSP_HAL_ETHSW_LINK_Down", MAX_STRING_SIZE);
					break;
				}
			case CCSP_HAL_ETHSW_LINK_Disconnected:
				{
					strncpy(pLinkStatus, "CCSP_HAL_ETHSW_LINK_Disconnected", MAX_STRING_SIZE);
					break;
				}
			default:
				{
					DEBUG_PRINT(DEBUG_TRACE, "Default value is given\n");
					strncpy(pLinkStatus, "Invalid", MAX_STRING_SIZE);
					break;
				}
		}

		switch(getLinkRate)
		{
			case CCSP_HAL_ETHSW_LINK_10Mbps:
				{
					*pLinkRate = MAXBITRATE_10;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_100Mbps:
				{
					*pLinkRate = MAXBITRATE_100;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_1Gbps:
				{
					*pLinkRate = MAXBITRATE_1000;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_2_5Gbps:
				{
					*pLinkRate = MAXBITRATE_2500;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_5Gbps:
				{
					*pLinkRate = MAXBITRATE_5000;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_10Gbps:
				{
					*pLinkRate = MAXBITRATE_10000;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_Auto:
				{
					*pLinkRate = 1;
					break;
				}
			case CCSP_HAL_ETHSW_LINK_NULL:
				{
					*pLinkRate = 0;
					break;
				}
			default:
				{
					*pLinkRate = INVALID_VALUE; //Invalid value
					break;
				}
		}

                switch(getDuplexMode)
                {
                        case CCSP_HAL_ETHSW_DUPLEX_Auto:
                                {
                                        strncpy(pDuplexMode, "CCSP_HAL_ETHSW_DUPLEX_Auto", MAX_STRING_SIZE);
                                        break;
                                }
                        case CCSP_HAL_ETHSW_DUPLEX_Half:
                                {
                                        strncpy(pDuplexMode, "CCSP_HAL_ETHSW_DUPLEX_Half", MAX_STRING_SIZE);
                                        break;
                                }
                        case CCSP_HAL_ETHSW_DUPLEX_Full:
                                {
                                        strncpy(pDuplexMode, "CCSP_HAL_ETHSW_DUPLEX_Full", MAX_STRING_SIZE);
                                        break;
                                }
                        default:
                                {
                                        DEBUG_PRINT(DEBUG_TRACE, "Invalid value provided\n");
                                        strncpy(pDuplexMode, "Invalid", MAX_STRING_SIZE);
                                        break;
                                }
                }

		DEBUG_PRINT(DEBUG_TRACE, "LinkRate = %d, LinkStatus = %s DuplexMode = %s\n", *pLinkRate, pLinkStatus, pDuplexMode);
	}
	else
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_Port_Status function returns failure\n");
	}
	return result;
}

/*******************************************************************************************
 * Function Name : ssp_ethsw_stub_hal_Init
 * Description   : This function will invoke the HAL api to intailize the Ethsw HAL
 * @param [in]   : no parameters
 * @param [out]  : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_ethsw_stub_hal_Init()
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_ethsw_stub_hal_Init wrapper\n");
	if(CcspHalEthSwInit() != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Init function returns failure\n");
		return RETURN_ERR;
	}

	return RETURN_OK;
}


/*****************************************************************************************************************
 * Function Name : ssp_EthSw_LocatePort_By_MacAddress
 * Description   : This function will Retrieve the port number that the specificed MAC address is associated with
 * @param [in]   : macAddr    -- Specifies the MAC address -- 6 bytes
		   pPortId    -- Receives the found port number that the MAC address is seen on
		   isNegativeScenario - for negative scenario
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_ethsw_stub_hal_LocatePort_By_MacAddress(char *pMacAddr, int *pPortId, int isNegativeScenario)
{
	int result = RETURN_ERR;

	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_EthSw_LocatePort_By_MacAddress wrapper\n");

	CHECK_PARAM_AND_RET(pMacAddr);
	CHECK_PARAM_AND_RET(pPortId);

	if(isNegativeScenario)
	{
		result = CcspHalEthSwLocatePortByMacAddress(NULL, NULL);
	}
	else
	{
		result = CcspHalEthSwLocatePortByMacAddress(pMacAddr, pPortId);
	}

	if(result == RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_EthSw_LocatePort_By_MacAddress function returns failure\n");
	}

	return result;
}


/******************************************************************************************************************
 * Function Name : ssp_EthSw_SetAgingSpeed
 * Description   : This function will Set the ethernet port configuration -- admin up/down, link speed, duplex mode
 * @param [in]   : PortId      -- Port ID as defined in CCSP_HAL_ETHSW_PORT
		   AgingSpeed  -- integer value of aging speed
 * @param [out]  : return status an integer value 0-success and 1-Failure
 *******************************************************************************************************************/
int ssp_ethsw_stub_hal_SetAgingSpeed(int portId, int agingSpeed)
{
	#if defined(INTEL_PUMA7)
        if(portId ==1)
           portId = 2;
        else if(portId ==2)
           portId =1;
        #endif
	CCSP_HAL_ETHSW_PORT port = INVALID_VALUE;

	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_EthSw_SetAgingSpeed wrapper\n");

	port = (CCSP_HAL_ETHSW_PORT)portId;
	if(CcspHalEthSwSetAgingSpeed(port, agingSpeed) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_EthSw_SetAgingSpeed function returns failure\n");
		return RETURN_ERR;
	}

	return RETURN_OK;
}


/************************************************************************************************
 * Function Name : ssp_EthSw_SetPortAdminStatus
 * Description   : This function will Set the ethernet port admin status
 * @param [in]   : portId -- Port ID as defined in CCSP_HAL_ETHSW_PORT
		   portAdminstatus -- set the admin status, as defined in CCSP_HAL_ETHSW_ADMIN_STATUS
 * @param [out]  : return status an integer value 0-success and 1-Failure
 *************************************************************************************************/
int ssp_ethsw_stub_hal_SetPortAdminStatus(int portId, char *portAdminstatus)
{
	#if defined(INTEL_PUMA7)
        if(portId ==1)
           portId = 2;
        else if(portId ==2)
           portId =1;
        #endif
	CCSP_HAL_ETHSW_PORT port  = (CCSP_HAL_ETHSW_PORT)portId;
	CCSP_HAL_ETHSW_ADMIN_STATUS setAdminStatus = (CCSP_HAL_ETHSW_ADMIN_STATUS) INVALID_VALUE;

	if(strcmp(portAdminstatus, "CCSP_HAL_ETHSW_AdminUp") == 0)
	{
		setAdminStatus = CCSP_HAL_ETHSW_AdminUp;
	}
	else if(strcmp(portAdminstatus, "CCSP_HAL_ETHSW_AdminDown") == 0)
	{
		setAdminStatus = CCSP_HAL_ETHSW_AdminDown;
	}
	else if(strcmp(portAdminstatus, "CCSP_HAL_ETHSW_AdminTest") == 0)
	{
		setAdminStatus = CCSP_HAL_ETHSW_AdminTest;
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Invalid value provided\n");
		setAdminStatus = (CCSP_HAL_ETHSW_DUPLEX_MODE) INVALID_VALUE;
	}

	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_EthSw_SetPortAdminStatus wrapper\n");
	if(CcspHalEthSwSetPortAdminStatus(port, setAdminStatus) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_EthSw_SetPortAdminStatus function returns failure\n");
		return RETURN_ERR;
	}

	return RETURN_OK;
}


/*******************************************************************************************
 * Function Name : ssp_EthSw_SetPortCfg
 * Description   : This function will Set the port configuration -- link speed, duplex mode
 * @param [in]   : portId -- Port ID as defined in CCSP_HAL_ETHSW_PORT
		   linkRate -- Set the link rate, as in CCSP_HAL_ETHSW_LINK_RATE
		   pDuplexMode -- Set the duplex mode, as in CCSP_HAL_ETHSW_DUPLEX_MODE
 * @param [out]  : return status an integer value 0-success and 1-Failure
 *******************************************************************************************/
int ssp_ethsw_stub_hal_SetPortCfg(int portId, int linkRate, char *pDuplexMode)
{
	#if defined(INTEL_PUMA7)
        if(portId ==1)
           portId = 2;
        else if(portId ==2)
           portId =1;
        #endif
	CCSP_HAL_ETHSW_PORT port = INVALID_VALUE;
	CCSP_HAL_ETHSW_LINK_RATE setLinkRate = INVALID_VALUE;
	CCSP_HAL_ETHSW_DUPLEX_MODE setDuplexmode = INVALID_VALUE;

	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_EthSw_SetPortCfg wrapper\n");

	switch(linkRate)
	{
		case MAXBITRATE_10:
			{
				setLinkRate = CCSP_HAL_ETHSW_LINK_10Mbps;
				break;
			}
		case MAXBITRATE_100:
			{
				setLinkRate = CCSP_HAL_ETHSW_LINK_100Mbps;
				break;
			}
		case MAXBITRATE_1000:
			{
				setLinkRate = CCSP_HAL_ETHSW_LINK_1Gbps;
				break;
			}
		case MAXBITRATE_2500:
			{
				setLinkRate = CCSP_HAL_ETHSW_LINK_2_5Gbps;
				break;
			}
		case MAXBITRATE_5000:
			{
				setLinkRate = CCSP_HAL_ETHSW_LINK_5Gbps;
				break;
			}
		case MAXBITRATE_10000:
			{
				setLinkRate = CCSP_HAL_ETHSW_LINK_10Gbps;
				break;
			}
		case MAXBITRATE_AUTO:
			{
				setLinkRate = CCSP_HAL_ETHSW_LINK_Auto;
				break;
			}
		default:
			{
				DEBUG_PRINT(DEBUG_TRACE, "Invalid value provided\n");
				setLinkRate = (CCSP_HAL_ETHSW_LINK_RATE) INVALID_VALUE; //Invalid value
				break;
			}
	}

	if(strcmp(pDuplexMode, "CCSP_HAL_ETHSW_DUPLEX_Auto") == 0)
	{
		setDuplexmode  = CCSP_HAL_ETHSW_DUPLEX_Auto;
	}
	else if(strcmp(pDuplexMode, "CCSP_HAL_ETHSW_DUPLEX_Half") == 0)
	{
		setDuplexmode  = CCSP_HAL_ETHSW_DUPLEX_Half;
	}
	else if(strcmp(pDuplexMode, "CCSP_HAL_ETHSW_DUPLEX_Full") == 0)
	{
		setDuplexmode  = CCSP_HAL_ETHSW_DUPLEX_Full;
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Invalid value provided\n");
		setDuplexmode  = (CCSP_HAL_ETHSW_DUPLEX_MODE) INVALID_VALUE;
	}

	port = (CCSP_HAL_ETHSW_PORT)portId;

	DEBUG_PRINT(DEBUG_TRACE, "Duplex mode to be set = %d and Link rate to be set =  %d\n", setDuplexmode, setLinkRate);

	if(CcspHalEthSwSetPortCfg(port, setLinkRate, setDuplexmode) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_EthSw_SetPortCfg function returns failure\n");
		return RETURN_ERR;
	}

	return RETURN_OK;
}
/*****************************************************************************************************************
 * Function Name : ssp_ethsw_stub_hal_Get_AssociatedDevice
 * Description   : This function will Retrieve the config of associated device
 * @param [in]   : array_size - size of the array
                   eth_device_conf - for getting the conf of associated devices
                   isNegativeScenario - for negative scenario
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_ethsw_stub_hal_Get_AssociatedDevice(unsigned long int *array_size,eth_device_t **eth_device_conf, int isNegativeScenario)
{
        int result = RETURN_ERR;

        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_ethsw_stub_hal_Get_AssociatedDevice wrapper\n");

        if(isNegativeScenario)
        {
                result = CcspHalExtSw_getAssociatedDevice(NULL, NULL);
        }
        else
        {
                result = CcspHalExtSw_getAssociatedDevice(array_size, eth_device_conf);
        }

        if(result != RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Get_AssociatedDevice function returns failure\n");
        }
        else
        {
                DEBUG_PRINT(DEBUG_TRACE, "ssp_ethsw_stub_hal_Get_AssociatedDevice function returns success\n");
        }

        return result;
}


/*****************************************************************************************************************
 * Function Name : ssp_ethsw_stub_hal_Get_EthWanInterfaceName
 * Description   : This function will Retrieve the interface name of ethwan
 * @param [in]   : interface - buffer to hold interface name
                   isNegativeScenario - for negative scenario
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_ethsw_stub_hal_Get_EthWanInterfaceName( char* interface, int isNegativeScenario)
{
        int result = RETURN_ERR;
        unsigned long max_size = MAX_STRING_SIZE;

        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_ethsw_stub_hal_Get_EthWanInterfaceName wrapper\n");

        if(isNegativeScenario)
        {
                result = GWP_GetEthWanInterfaceName(NULL,NULL);
        }
        else
        {
                result = GWP_GetEthWanInterfaceName(interface,max_size);
        }

        if(result == RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_TRACE, "ssp_ethsw_stub_hal_Get_EthWanInterfaceName function returns value : %s\n", interface);
        }
        else
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Get_EthWanInterfaceName function returns failure\n");
        }

        DEBUG_PRINT(DEBUG_TRACE, "Exiting ssp_ethsw_stub_hal_Get_EthWanInterfaceName wrapper\n");
        return result;
}


/*****************************************************************************************************************
 * Function Name : ssp_ethsw_stub_hal_Get_EthWanEnable
 * Description   : This function will Retrieve the ethwan enable status
 * @param [in]   : enableStatus - buffer to hold enable state
                   isNegativeScenario - for negative scenario
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_ethsw_stub_hal_Get_EthWanEnable( unsigned char* enableStatus, int isNegativeScenario)
{
        int result = RETURN_ERR;

        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_ethsw_stub_hal_Get_EthWanEnable wrapper\n");

        if(isNegativeScenario)
        {
                result = CcspHalExtSw_getEthWanEnable(NULL);
        }
        else
        {
                result = CcspHalExtSw_getEthWanEnable(enableStatus);
        }

        if(result == RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Get_EthWanEnable function returns enableStatus as %d\n", *enableStatus);
        }
        else
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Get_EthWanEnable function returns failure\n");
        }

        DEBUG_PRINT(DEBUG_TRACE, "Exiting ssp_ethsw_stub_hal_Get_EthWanEnable wrapper\n");
        return result;
}


/*****************************************************************************************************************
 * Function Name : ssp_ethsw_stub_hal_Set_EthWanEnable
 * Description   : This function will set the ethwan enable status
 * @param [in]   : enableStatus - enable state value to be set
                   isNegativeScenario - for negative scenario
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_ethsw_stub_hal_Set_EthWanEnable( unsigned char enableStatus)
{
        int result = RETURN_ERR;

        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_ethsw_stub_hal_Set_EthWanEnable wrapper\n");

        if(CcspHalExtSw_setEthWanEnable(enableStatus) == RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Set_EthWanEnable function returns success\n");
                result = RETURN_OK;
        }
        else
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Set_EthWanEnable function returns failure\n");
        }

        DEBUG_PRINT(DEBUG_TRACE, "Exiting ssp_ethsw_stub_hal_Set_EthWanEnable wrapper\n");
        return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_ethsw_stub_hal_Get_EthWanPort
 * Description   : This function will Retrieve the ethwan port number
 * @param [in]   : portNum - buffer to hold ethwan port number
                   isNegativeScenario - for negative scenario
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_ethsw_stub_hal_Get_EthWanPort( unsigned int* portNum, int isNegativeScenario)
{
        int result = RETURN_ERR;

        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_ethsw_stub_hal_Get_EthWanPort wrapper\n");

        if(isNegativeScenario)
        {
                result = CcspHalExtSw_getEthWanPort(NULL);
        }
        else
        {
                result = CcspHalExtSw_getEthWanPort(portNum);
        }

        if(result == RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Get_EthWanPort function returns port number as %lu\n", *portNum);
        }
        else
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Get_EthWanPort function returns failure\n");
        }

        DEBUG_PRINT(DEBUG_TRACE, "Exiting ssp_ethsw_stub_hal_Get_EthWanPort wrapper\n");
        return result;
}


/*****************************************************************************************************************
 * Function Name : ssp_ethsw_stub_hal_Set_EthWanPort
 * Description   : This function will set the ethwan port number
 * @param [in]   : portNum - ethwan port number value to be set
                   isNegativeScenario - for negative scenario
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_ethsw_stub_hal_Set_EthWanPort( unsigned int portNum)
{
        int result = RETURN_ERR;

        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_ethsw_stub_hal_Set_EthWanPort wrapper\n");

        if(CcspHalExtSw_setEthWanPort(portNum) == RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Set_EthWanPort function returns success\n");
                result = RETURN_OK;
        }
        else
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Set_EthWanPort function returns failure\n");
        }

        DEBUG_PRINT(DEBUG_TRACE, "Exiting ssp_ethsw_stub_hal_Set_EthWanPort wrapper\n");
        return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_ethsw_stub_hal_Get_EthWanLinkStatus
 * Description   : This function will Retrieve the ethwan link status
 * @param [in]   : linkstatus - buffer to hold ethwan link status
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_ethsw_stub_hal_Get_EthWanLinkStatus(int* linkStatus)
{
        int result = RETURN_ERR;

        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_ethsw_stub_hal_Get_EthWanLinkStatus wrapper\n");

        *linkStatus = GWP_GetEthWanLinkStatus();

        if (*linkStatus == ETH_WAN_LINK_UP)
        {
                DEBUG_PRINT(DEBUG_TRACE, "ssp_ethsw_stub_hal_Get_EthWanLinkStatus function returns status as ETH_WAN_LINK_UP \n");
                result = RETURN_OK;
        }
        else if (*linkStatus == ETH_WAN_LINK_DOWN)
        {
                DEBUG_PRINT(DEBUG_TRACE, "ssp_ethsw_stub_hal_Get_EthWanLinkStatus function returns status as ETH_WAN_LINK_DOWN \n");
                result = RETURN_OK;
        }
        else
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_ethsw_stub_hal_Get_EthWanLinkStatus function returns failure status: %d\n", *linkStatus);
        }

        DEBUG_PRINT(DEBUG_TRACE, "Exiting ssp_ethsw_stub_hal_Get_EthWanLinkStatus wrapper\n");
        return result;
}

