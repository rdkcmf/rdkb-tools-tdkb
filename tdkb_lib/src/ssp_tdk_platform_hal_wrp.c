/****************************************************************************
  Copyright 2016-2018 Intel Corporation

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
#include "ssp_tdk_platform_hal_wrp.h"
#include "ssp_hal_logger.h"

INT platform_hal_getCMTSMac(CHAR *pValue);
int platform_hal_SetFanSpeed(unsigned long int Value);
int platform_hal_GetChipTemperature(unsigned int chipIndex, unsigned long int* pTempValue);

/*******************************************************************************************
 * * Function Name       : ssp_DocsisParamsDBInit
 ** Description          : This function will invoke the HAL api to intialize Docsis DB
 ** @param [in]          : void funtion
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_DocsisParamsDBInit()
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_DocsisParamsDBInit wrapper\n");
	if (platform_hal_DocsisParamsDBInit() != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "platform_hal_DocsisParamsDBInit function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}

/******************************************************************************************
 * * Function Name       : ssp_GetBaseMacAddress
 ** Description          : This function will invoke the HAL API to get the MAC AddressB
 **
 ** @param [in]          : String to fetch the MAC ID
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetBaseMacAddress(char* pValue)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetBaseMacAddress wrapper\n");

	if (platform_hal_GetBaseMacAddress(pValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "platform_hal_GetBaseMacAddress function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}
/*******************************************************************************************
 * *
 * * Function Name       : ssp_GetBootloaderVersion
 ** Description          : This function will invoke the HAL API to get the Boot loader version
 **
 ** @param [in]          : String to fetch the Boot Loader Version
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetBootloaderVersion(char* pValue, unsigned long int maxSize)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetBootloaderVersion wrapper\n");

	if (platform_hal_GetBootloaderVersion(pValue, maxSize) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "platform_hal_GetBootloaderVersion function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_GetDeviceConfigStatus
 ** Description          : This function will invoke the HAL API to get the Device config status
 ** @param [in]          : String to fetch the Boot Loader Version
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetDeviceConfigStatus(char* pValue)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetDeviceConfigStatus wrapper\n");

	if(platform_hal_GetDeviceConfigStatus(pValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, " platform_hal_GetDeviceConfigStatus function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_getFactoryPartnerId
 ** Description          : This function will invoke the HAL API to get the factory partner ID
 ** @param [in]          : String to fetch the Boot Loader Version
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_getFactoryPartnerId(char* pValue)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_getFactoryPartnerId wrapper\n");

	if(platform_hal_getFactoryPartnerId(pValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, " platform_hal_getFactoryPartnerId function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_GetFirmwareName
 ** Description          : This function will invoke the HAL API to get the Firmware Name
 ** @param [in]          : String to fetch the Fetch the Firmware Name
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetFirmwareName(char* pValue,unsigned long int maxSize)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetFirmwareName wrapper\n");

	if(platform_hal_GetFirmwareName(pValue,maxSize) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, " platform_hal_GetBaseMacAddress function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_GetFreeMemorySize
 ** Description          : This function will invoke the HAL API to get the free memory size
 ** @param [in]          : String to fetch Free memory size
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetFreeMemorySize(unsigned long int* pulSize)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetFreeMemorySize wrapper\n");

	if(platform_hal_GetFreeMemorySize(pulSize) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "platform_hal_GetFreeMemorySize function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_GetHardware
 ** Description          : This function will invoke the HAL API to get the Hardware
 **
 ** @param [in]          : String to fetch the Hardware
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetHardware(char* pValue)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetHardware wrapper\n");

	if (platform_hal_GetHardware(pValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, " ssp_GetHardware function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_GetHardwareMemFree
 ** Description          : This function will invoke the HAL API to get the Hardware memory free
 **
 ** @param [in]          : String to fetch the Hardware memory free
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/

int ssp_GetHardwareMemFree(char* pValue)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetHardwareMemFree wrapper\n");

	if (platform_hal_GetHardware_MemFree(pValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_GetHardwareMemFree function failure\n");
		return RETURN_ERR;
	}

	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_GetHardwareVersion
 ** Description          : This function will invoke the HAL API to get the Hardware version
 **
 ** @param [in]          : String to fetch the Hardware version
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetHardwareVersion(char *rx_test)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetHardwareVersion wrapper\n");

	if (platform_hal_GetHardwareVersion(rx_test) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_GetHardwareVersion function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}



/*******************************************************************************************
 * * Function Name       : ssp_GetHardwareMemUsed
 ** Description          : This function will invoke the HAL API to get the Hardware memory used
 **
 ** @param [in]          : String to fetch the Hardware memory used
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetHardwareMemUsed(char* pValue)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetHardwareMemUsed wrapper\n");

	if(platform_hal_GetHardware_MemUsed(pValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_GetHardwareMemUsed function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_GetModelName
 ** Description          : This function will invoke the HAL API to get the Model Name
 ** @param [in]          : String to fetch the Model Name
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetModelName(char* pValue)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetModelName wrapper\n");

	if(platform_hal_GetModelName(pValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, " ssp_GetModelName function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_GetSerialNumber
 ** Description          : This function will invoke the HAL API to get the Serial Number
 ** @param [in]          : String to fetch the Serial Number
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetSerialNumber(char* pValue)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the SerialNumber wrapper\n");

	if(platform_hal_GetSerialNumber(pValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "ssp_GetSerialNumber function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 * * Function Name       : ssp_GetSNMPEnable
 ** Description          : This function will invoke the HAL API to get the SNMP details
 **
 ** @param [in]          : String to fetch the SNMP details
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetSNMPEnable(char* pValue)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetSNMPEnable wrapper\n");

	if (platform_hal_GetSNMPEnable(pValue) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, " ssp_GetSNMPEnable function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 **Function Name       : ssp_GetSoftwareVersion
 ** Description        : This function will invoke the HAL API to Get Software Version
 ** @param [in]        : String to fetch the Software version
 ** @param [out]       : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_GetSoftwareVersion(char* pValue,unsigned long int maxSize)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetSoftwareVersion wrapper\n");

	if(platform_hal_GetSoftwareVersion(pValue,maxSize) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "platform_hal_GetSoftwareVersion function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}

/*******************************************************************************************
 * *Function Name        : ssp_GetSSHEnable
 ** Description          : This function will invoke the HAL API to Get SSH Enable
 ** @param [in]          : BOOLEAN
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_GetSSHEnable(BOOLEAN* pflag)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetSSHEnable wrapper\n");

	if (platform_hal_GetSSHEnable(pflag) != RETURN_OK )
	{
		DEBUG_PRINT(DEBUG_ERROR, "Platform funtion returns failure\n");
		return RETURN_ERR;
	}
	DEBUG_PRINT(DEBUG_TRACE, "Platform function returns success\n");
	return RETURN_OK;

}
/*******************************************************************************************
 ** Function Name : ssp_GetTelnetEnable
 ** Description   : This function will invoke the HAL API to Get Telnet Enable status
 ** @param [in]   : Boolean
 ** @param [out]  : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_GetTelEnable(BOOLEAN* pflag)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetTelnetEnable wrapper\n");

	if (platform_hal_GetTelnetEnable(pflag) != RETURN_OK )
	{
		DEBUG_PRINT(DEBUG_ERROR, "Platform funtion returns failure\n");
		return RETURN_ERR;
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Platform funtion returns sucess\n");
		return RETURN_OK;
	}

}
/*******************************************************************************************
 ** Function Name        : ssp_GetTotalMemorySize
 ** Description          : This function will invoke the HAL API to Get the total memory size
 ** @param [in]          : String to fetch the total memory size
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_GetTotalMemorySize(unsigned long int* pulSize)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetTotalMemorySize wrapper\n");
	CHECK_PARAM_AND_RET(pulSize);

	if(platform_hal_GetTotalMemorySize(pulSize) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "platform_hal_GetTotalMemorySize function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 ** Function Name        : ssp_GetUsedMemorySize
 ** Description          : This function will invoke the HAL API to Get Used memory size
 ** @param [in]          : String to fetch the used memory size
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_GetUsedMemorySize(unsigned long int* pulSize)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetUsedMemorySize wrapper\n");
	CHECK_PARAM_AND_RET(pulSize);

	if(platform_hal_GetUsedMemorySize(pulSize) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "platform_hal_GetUsedMemorySize function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 **Function Name         : ssp_GetWebUITimeout
 ** Description          : This function will invoke the HAL API to Get web UI Timeout
 ** @param [in]          : String to fetch UIT timeout
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_GetWebUITimeout(unsigned long int* pulSize)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetWebUITimeout wrapper\n");
	CHECK_PARAM_AND_RET(pulSize);

	if(platform_hal_GetWebUITimeout(pulSize) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "platform_hal_GetWebUITimeout function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 ** Function Name        : ssp_PandMDBInit
 ** Description          : This function will invoke the HAL API to initiate pandMDB
 ** @param [in]          : void
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_PandMDBInit()
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_PandMDBInit wrapper\n");
	if (platform_hal_PandMDBInit() != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "platform_hal_PandMDBInit function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 ** Function Name        : ssp_SetSNMPEnable
 ** Description          : This function will invoke the HAL API to Set SNMP Enable
 ** @param [in]          : pointer to char
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_SetSNMPEnable(char *pEnable)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_SetSNMPEnable wrapper\n");
	CHECK_PARAM_AND_RET(pEnable);

	if (platform_hal_SetSNMPEnable(pEnable) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "platform_hal_SetSNMPEnable function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}


/*******************************************************************************************
 ** Function Name        : ssp_SetSSHEnable
 ** Description          : This function will invoke the HAL API to Set SSH Enable
 ** @param [in]          : Boolean value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_SetSSHEnable(BOOLEAN flag)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_SetSSHEnable wrapper\n");

	if (platform_hal_SetSSHEnable(flag) != RETURN_OK )
	{
		DEBUG_PRINT(DEBUG_ERROR, "SetSSH enable returns failure of funtion\n");
		return RETURN_ERR;
	}
	DEBUG_PRINT(DEBUG_TRACE, "SetSSH enable returns success\n");
	return RETURN_OK;

}

/*******************************************************************************************
 ** Function Name        : ssp_SetTelnetEnable
 ** Description          : This function will invoke the HAL API to set Telnet Enable
 ** @param [in]          : boolean value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_SetTelnetEnable(BOOLEAN flag)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_SetTelnetEnable wrapper\n");

	if (platform_hal_SetTelnetEnable(flag) != RETURN_OK )
	{
		DEBUG_PRINT(DEBUG_ERROR, "HAL funtion returns failure\n");
		return RETURN_ERR;
	}
	DEBUG_PRINT(DEBUG_TRACE, "HAL function returns success\n");
	return RETURN_OK;

}

/*******************************************************************************************
 ** Function Name        : ssp_SetWebUITimeout
 ** Description          : This function will invoke the HAL API to set the WebUI Timeout
 ** @param [in]          : unsigned integer value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *****************************************************************************************/
int ssp_SetWebUITimeout(unsigned long int Value)
{
	DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_SetWebUITimeout wrapper\n");
	if (platform_hal_SetWebUITimeout(Value) != RETURN_OK)
	{
		DEBUG_PRINT(DEBUG_ERROR, "platform_hal_SetWebUITimeout function failure\n");
		return RETURN_ERR;
	}
	return RETURN_OK;
}

/*******************************************************************************************
 ** Function Name        : ssp_GetFactoryResetCount
 ** Description          : This function will invoke the HAL API to GetFactory reset count
 ** @param [in]          : String to fetch the factory reset count
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_GetFactoryResetCount(unsigned long int* pulSize)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetFactoryResetCount wrapper\n");
        CHECK_PARAM_AND_RET(pulSize);

        if(platform_hal_GetFactoryResetCount(pulSize) != RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, "platform_hal_GetFactoryResetCount function failure\n");
                return RETURN_ERR;
        }
        return RETURN_OK;
}

/*******************************************************************************************
 ** Function Name        : ssp_ClearResetCount
 ** Description          : This function will invoke the HAL API to clear the reset count
 ** @param [in]          : boolean value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_ClearResetCount(BOOLEAN flag)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_ClearResetCount wrapper\n");

        if (platform_hal_ClearResetCount(flag) != RETURN_OK )
        {
                DEBUG_PRINT(DEBUG_ERROR, "HAL funtion returns failure\n");
                return RETURN_ERR;
        }
        DEBUG_PRINT(DEBUG_TRACE, "HAL function returns success\n");
        return RETURN_OK;

}

/*******************************************************************************************
 * * Function Name       : ssp_GetTimeOffSet
 ** Description          : This function will invoke the HAL API to get the TimeOffSet
 **
 ** @param [in]          : String to fetch the TimeOffSet
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetTimeOffSet(char* pValue)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetTimeOffSet wrapper\n");

        if (platform_hal_getTimeOffSet(pValue) != RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, " ssp_GetTimeOffSet function failure\n");
                return RETURN_ERR;
        }
        return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_GetCMTSMac
 ** Description          : This function will invoke the HAL API to get the CMTSMac
 **
 ** @param [in]          : String to fetch the CMTSMac
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetCMTSMac(char* pValue)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetCMTSMac wrapper\n");

        if (platform_hal_getCMTSMac(pValue) != RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, " ssp_GetCMTSMac function failure\n");
                return RETURN_ERR;
        }
        return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_GetChipTemperature
 ** Description          : This function will invoke the HAL API to get the ChipTemperature
 ** @param [in]          : String to fetch the Fetch the ChipTemperature
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetChipTemperature(unsigned int chipIndex,unsigned long int* pTempValue)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetChipTemperature wrapper\n");
        if(platform_hal_GetChipTemperature(chipIndex,pTempValue) != RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, " platform_hal_GetChipTemperature function failure\n");
                return RETURN_ERR;
        }
        return RETURN_OK;
}

/*******************************************************************************************
 **Function Name         : ssp_GetFanSpeed
 ** Description          : This function will invoke the HAL API to Get FanSpeed
 ** @param [in]          : String to fetch FanSpeed
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_GetFanSpeed(unsigned int fanIndex,unsigned long int* pSpeedValue)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetFanSpeed wrapper\n");
        unsigned int speedValue = 0;
        speedValue = platform_hal_getFanSpeed(fanIndex);
        *pSpeedValue = speedValue;
        DEBUG_PRINT(DEBUG_TRACE, "Value of Fan Speed is %d\n",speedValue);

        if ((signed)speedValue < 0 )
        {
                DEBUG_PRINT(DEBUG_ERROR, "Platform funtion returns failure\n");
                return RETURN_ERR;
        }
        DEBUG_PRINT(DEBUG_TRACE, "Platform function returns success\n");
        return RETURN_OK;

}

/*******************************************************************************************
 ** Function Name        : ssp_SetFanSpeed
 ** Description          : This function will invoke the HAL API to set the WebUI Timeout
 ** @param [in]          : unsigned integer value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *****************************************************************************************/
int ssp_SetFanSpeed(unsigned long int Value)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_SetFanSpeed wrapper\n");
        if (platform_hal_SetFanSpeed(Value) != RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, "platform_hal_SetFanSpeed function failure\n");
                return RETURN_ERR;
        }
        return RETURN_OK;
}
/*******************************************************************************************
 ** Function Name        : ssp_SetMACsecEnable
 ** Description          : This function will invoke the HAL API to Set MACsec Enable
 ** @param [in]          : Integer Port Number and Boolean value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_SetMACsecEnable(int ethPort, BOOLEAN flag)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_SetMACsecEnable wrapper\n");

        if (platform_hal_SetMACsecEnable(ethPort,flag) != RETURN_OK )
        {
                DEBUG_PRINT(DEBUG_ERROR, "SetMACsecEnable returns failure of funtion\n");
                return RETURN_ERR;
        }
        DEBUG_PRINT(DEBUG_TRACE, "SetMACsecEnable returns success\n");
        return RETURN_OK;
}

/*******************************************************************************************
 * *Function Name        : ssp_GetMACsecEnable
 ** Description          : This function will invoke the HAL API to Get MACsec Enable
 ** @param [in]          : Integer Port Number and Boolean value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_GetMACsecEnable(int ethPort, BOOLEAN* pflag)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetMACsecEnable wrapper\n");
        if(pflag == NULL)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Sending NULL pointer to the flag\n");
	}

        if (platform_hal_GetMACsecEnable(ethPort,pflag) != RETURN_OK )
        {
                DEBUG_PRINT(DEBUG_ERROR, "Platform funtion returns failure\n");
                return RETURN_ERR;
        }
        DEBUG_PRINT(DEBUG_TRACE, "Platform function returns success\n");
        return RETURN_OK;
}

/*******************************************************************************************
 * *Function Name        : ssp_GetMACsecOperationalStatus
 ** Description          : This function will invoke the HAL API to Get MACsec Operational status
 ** @param [in]          : Integer Port Number and Boolean value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_GetMACsecOperationalStatus(int ethPort, BOOLEAN* pflag)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetMACsecOperationalStatus wrapper\n");

        if (platform_hal_GetMACsecOperationalStatus(ethPort,pflag) != RETURN_OK )
        {
                DEBUG_PRINT(DEBUG_ERROR, "Platform funtion returns failure\n");
                return RETURN_ERR;
        }
        DEBUG_PRINT(DEBUG_TRACE, "Platform function returns success\n");
        return RETURN_OK;
}

/*******************************************************************************************
 **
 ** Function Name       : ssp_getFactoryCmVariant
 ** Description          : This function will invoke the HAL API to get the FactoryCM varient
 ** @param [in]          : String to fetch the Cm varient value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_getFactoryCmVariant(char *pValue)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_getFactoryCmVariant wrapper\n");

        if (platform_hal_getFactoryCmVariant(pValue) != RETURN_OK )
        {
                DEBUG_PRINT(DEBUG_ERROR, "Platform funtion returns failure\n");
                return RETURN_ERR;
        }
        DEBUG_PRINT(DEBUG_TRACE, "Platform function returns success\n");
        return RETURN_OK;
}

/*******************************************************************************************
 * *
 ** Function Name       : ssp_setFactoryCmVariant
 ** Description          : This function will invoke the HAL API to set the Factory CM varient
 **
 ** @param [in]          : String  value to set the CM varient value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_setFactoryCmVariant(char *pValue)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_setFactoryCmVariant wrapper\n");

        if (platform_hal_setFactoryCmVariant(pValue) != RETURN_OK )
        {
                DEBUG_PRINT(DEBUG_ERROR, "Platform funtion returns failure\n");
                return RETURN_ERR;
        }
        DEBUG_PRINT(DEBUG_TRACE, "Platform function returns success\n");
        return RETURN_OK;
}

/*******************************************************************************************
 **
 ** Function Name       : ssp_getRPM
 ** Description          : This function will invoke the HAL API to get RPM value
 **
 ** @param [in]          : boolean to fetch the RPM value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_getRPM(unsigned int fanIndex,unsigned int *rpmbuf)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_getRPM wrapper\n");
        unsigned int rpmValue = 0;
        rpmValue = platform_hal_getRPM(fanIndex);
        *rpmbuf = rpmValue;
        DEBUG_PRINT(DEBUG_TRACE, "Value of RPM is %d\n",rpmValue);

        DEBUG_PRINT(DEBUG_TRACE, "Platform function returns success\n");
        return RETURN_OK;
}

/*******************************************************************************************
 **
 ** Function Name       : ssp_getRotorLock
 ** Description          : This function will invoke the HAL API to get the Rotor Lock
 **
 ** @param [in]          : integer to fetch the Rotot Lock Value
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_getRotorLock(unsigned int fanIndex,int *rotorLockbuf)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_getRotorLock wrapper\n");
        int rotorLockValue = 0;
        rotorLockValue = platform_hal_getRotorLock(fanIndex);
        *rotorLockbuf = rotorLockValue;
        DEBUG_PRINT(DEBUG_ERROR, "Value of RotorLock is %d\n",rotorLockValue);

        if (rotorLockValue < -1 || rotorLockValue > 1)
        {
                DEBUG_PRINT(DEBUG_ERROR, "Platform funtion returns failure\n");
                return RETURN_ERR;
        }
        DEBUG_PRINT(DEBUG_TRACE, "Platform function returns success\n");
        return RETURN_OK;
}

/*******************************************************************************************
 **
 ** Function Name       : ssp_getFanStatus
 ** Description          : This function will invoke the HAL API to get the Fan status
 **
 ** @param [in]          : String to fetch the Fan status
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_getFanStatus(unsigned int fanIndex,int *flag)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_getFanStatus wrapper\n");
        BOOLEAN fanStatus = 0;
        fanStatus = platform_hal_getFanStatus(fanIndex);
        *flag = (int)fanStatus;
        DEBUG_PRINT(DEBUG_TRACE, "Value of FanStatus is %d\n",fanStatus);
        if (fanStatus == 1)
	{
                DEBUG_PRINT(DEBUG_ERROR, "Platform function  success and returns Fanstatus TRUE \n");
		return RETURN_OK;
	}
	else if (fanStatus == 0)
	{
		DEBUG_PRINT(DEBUG_ERROR, "Platform function  success and returns Fanstatus FALSE \n");
		return RETURN_OK;
	}
	else
	{
	        DEBUG_PRINT(DEBUG_ERROR, "Platform function failed to get a value \n");
		return RETURN_ERR;
	}
}

/*******************************************************************************************
 **
 ** Function Name       : ssp_setFanMaxOverride
 ** Description          : This function will invoke the HAL API to set the Fan Max Override
 **
 ** @param [in]          : Boolean value to enable or disable
 ** @param fanIndex      : Fan index starting from 0
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_setFanMaxOverride(BOOLEAN flag, unsigned int fanIndex)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_setFanMaxOverride wrapper\n");
	if (platform_hal_setFanMaxOverride(flag, fanIndex) != RETURN_OK )
        {
                DEBUG_PRINT(DEBUG_ERROR, "Platform funtion returns failure\n");
                return RETURN_ERR;
        }
        DEBUG_PRINT(DEBUG_TRACE, "Platform function returns success\n");
        return RETURN_OK;
}

/*******************************************************************************************
 **
 ** Function Name        : ssp_setSNMMOnboardRebootEnable
 ** Description          : This function will invoke the HAL API to set the SNMP Onboard Reboot Enable
 **
 ** @param [in]          : String value to enable or disable
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_SetSNMPOnboardRebootEnable(char *pEnable)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_SetSNMPOnboardRebootEnable wrapper\n");

        if (platform_hal_SetSNMPOnboardRebootEnable(pEnable) != RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, "platform_hal_SetSNMPEnable function failure\n");
                return RETURN_ERR;
        }
        return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_GetRouterRegion
 ** Description          : This function will invoke the HAL API to get the RouterRegion
 ** @param [in]          : String to fetch the RouterRegion
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetRouterRegion(char* pValue)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetRouterRegion wrapper\n");

        if(platform_hal_GetRouterRegion(pValue) != RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, " platform_hal_GetRouterRegion function failure\n");
                return RETURN_ERR;
        }

        DEBUG_PRINT(DEBUG_TRACE, "platform_hal_GetRouterRegion call was success\n");
        if(pValue)
            DEBUG_PRINT(DEBUG_TRACE, "platform_hal_GetRouterRegion returns value: %s\n", pValue);
        return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_GetMemoryPaths
 ** Description          : This function will invoke the HAL API to get the platform_hal_GetMemoryPaths
 ** @param [in]          : index - Index value of RDK_CPUS
                         : ppinfo - Structure value of PPLAT_PROC_MEM_INFO
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetMemoryPaths(RDK_CPUS index, PPLAT_PROC_MEM_INFO *ppinfo)
{
    DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetMemoryPaths wrapper\n");
    DEBUG_PRINT(DEBUG_TRACE, "RDK_CPUS index value is %d\n",(int)index);

    if(platform_hal_GetMemoryPaths(index, ppinfo) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_ERROR, " platform_hal_GetMemoryPaths function failure\n");
        return RETURN_ERR;
    }
    DEBUG_PRINT(DEBUG_TRACE, "Value of dramPath is %s",(*ppinfo)->dramPath);
    DEBUG_PRINT(DEBUG_TRACE, "Value of emmcPath1 is %s",(*ppinfo)->emmcPath1);
    DEBUG_PRINT(DEBUG_TRACE, "Value of emmcPath2 is %s",(*ppinfo)->emmcPath2);

    DEBUG_PRINT(DEBUG_TRACE, "platform_hal_GetMemoryPaths call was success\n");
    return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_SetLowPowerModeState
 ** Description          : This function will invoke the HAL API to set the platform_hal_SetLowPowerModeState
 ** @param [in]          : state - Power Mode value (AC, Battery, etc.,)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_SetLowPowerModeState(PSM_STATE state)
{
    DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_SetLowPowerModeState wrapper\n");
    DEBUG_PRINT(DEBUG_TRACE, "Value to be set on LowPowerModeState is %d \n",(int)state);

    if(platform_hal_SetLowPowerModeState(&state) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_ERROR, "Platform_hal_SetLowPowerModeState function failure\n");
        return RETURN_ERR;
    }

    DEBUG_PRINT(DEBUG_TRACE, "platform_hal_SetLowPowerModeState call was success\n");
    return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_StartMACsec
 ** Description          : This function will invoke the HAL API platform_hal_StartMACsec
 ** @param [in]          : state - Power Mode value (AC, Battery, etc.,)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_StartMACsec(int ethPort, int timeout)
{
    DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_StartMACsec wrapper\n");
    DEBUG_PRINT(DEBUG_TRACE, "ethPort value is %d and timeout value is %d \n",ethPort,timeout);

    if(platform_hal_StartMACsec(ethPort,timeout) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_ERROR, "platform_hal_StartMACsec function failure\n");
        return RETURN_ERR;
    }

    DEBUG_PRINT(DEBUG_TRACE, "platform_hal_StartMACsec call was success\n");
    return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_StopMACsec
 ** Description          : This function will invoke the HAL API platform_hal_StopMACsec
 ** @param [in]          : state - Power Mode value (AC, Battery, etc.,)
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_StopMACsec(int ethPort)
{
    DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_StopMACsec wrapper\n");
    DEBUG_PRINT(DEBUG_TRACE, "ethPort value is %d \n",ethPort);

    if(platform_hal_StopMACsec(ethPort) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_ERROR, "platform_hal_StopMACsec function failure\n");
        return RETURN_ERR;
    }

    DEBUG_PRINT(DEBUG_TRACE, "platform_hal_StopMACsec call was success\n");
    return RETURN_OK;
}

/*******************************************************************************************
 * * Function Name       : ssp_GetWebAccessLevel
 ** Description          : This function will invoke the HAL API to get the WebAccessLevel
 ** @param [in]          : String to fetch the WebAccessLevel
 ** @param [out]         : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_GetWebAccessLevel(int user, int index, unsigned long int* pulValue)
{
    DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetWebAccessLevel wrapper\n");
    DEBUG_PRINT(DEBUG_TRACE, "User Value is :%d and Interface Index Value is :%d \n",user,index);
    if(platform_hal_GetWebAccessLevel(user, index, pulValue) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_ERROR, " platform_hal_GetWebAccessLevel function failure\n");
        return RETURN_ERR;
    }
    DEBUG_PRINT(DEBUG_TRACE, "platform_hal_GetWebAccessLevel call was success\n");
    DEBUG_PRINT(DEBUG_TRACE, "The WebAccessLevel Value is :%lu\n",*pulValue);
    return RETURN_OK;
}

/*******************************************************************************************
 * Function Name       : ssp_setDscp
 * Description         : This function will invoke the HAL API platform_hal_setDscp() to Control/Set traffic counting based on Dscp value
 * @param [in]         : interfaceType - 1 for DOCSIS , 2 for EWAN
 * @param [in]         : cmd - START/STOP
 * @param [in]         : dscpVal - comma seperated string , e.g. "10,0" , NULL
 * @param [out]        : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_setDscp(WAN_INTERFACE interfaceType , TRAFFIC_CNT_COMMAND cmd , char* dscpVal)
{
    int returnValue = RETURN_OK;
    DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_setDscp wrapper\n");
    DEBUG_PRINT(DEBUG_TRACE, "Interface Type is %d \n",(int)interfaceType);
    DEBUG_PRINT(DEBUG_TRACE, "Traffic Count Command is %d \n",(int)cmd);

    if(dscpVal)
    {
        DEBUG_PRINT(DEBUG_TRACE, "DSCP Value is %s \n", dscpVal);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE, "DSCP Value is Null\n");
    }

    returnValue = platform_hal_setDscp(interfaceType, cmd, dscpVal);

    if(returnValue == RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE, "platform_hal_setDscp call was success::return value : %d\n", returnValue);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE, "platform_hal_setDscp call failed::return value : %d\n", returnValue);
    }

    DEBUG_PRINT(DEBUG_TRACE, "ssp_setDscp -----> Exiting\n");
    return returnValue;
}


/*******************************************************************************************
 * Function Name       : ssp_resetDscpCounts
 * Description         : This function will invoke the HAL API platform_hal_resetDscpCounts() to reset Dscp Counter values
 * @param [in]         : interfaceType - 1 for DOCSIS , 2 for EWAN
 * @param [out]        : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_resetDscpCounts(WAN_INTERFACE interfaceType)
{
    int returnValue = RETURN_OK;
    DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_resetDscpCounts wrapper\n");
    DEBUG_PRINT(DEBUG_TRACE, "Interface Type is %d \n",(int)interfaceType);

    returnValue = platform_hal_resetDscpCounts(interfaceType);

    if(returnValue == RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE, "platform_hal_resetDscpCounts call was success::return value : %d\n", returnValue);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE, "platform_hal_resetDscpCounts call failed::return value : %d\n", returnValue);
    }

    DEBUG_PRINT(DEBUG_TRACE, "ssp_resetDscpCounts -----> Exiting\n");
    return returnValue;
}


/*******************************************************************************************
 * Function Name       : ssp_getDscpClientList
 * Description         : This function will invoke the HAL API platform_hal_getDscpClientList() to get the counter data
 * @param [in]         : interfaceType - 1 for DOCSIS , 2 for EWAN
 * @param [in]         : DSCP_List - List of client structure to be filled by hal
 * @param [out]        : return status an integer value 0-success and 1-Failure
 *********************************************************************************************/
int ssp_getDscpClientList(WAN_INTERFACE interfaceType , pDSCP_list_t DSCP_List)
{
    int returnValue = RETURN_OK;
    DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_getDscpClientList wrapper\n");
    DEBUG_PRINT(DEBUG_TRACE, "Interface Type is %d \n",(int)interfaceType);

    returnValue = platform_hal_getDscpClientList(interfaceType, DSCP_List);

    if(returnValue == RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE, "platform_hal_getDscpClientList call was success::return value : %d\n", returnValue);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE, "platform_hal_getDscpClientList call failed::return value : %d\n", returnValue);
    }

    DEBUG_PRINT(DEBUG_TRACE, "ssp_getDscpClientList -----> Exiting\n");
    return returnValue;
}
