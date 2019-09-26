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
int ssp_GetFanSpeed(unsigned long int* pSpeedValue)
{
        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_GetFanSpeed wrapper\n");
//      CHECK_PARAM_AND_RET(pSpeedValue);
        if(platform_hal_GetFanSpeed(pSpeedValue) != RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_ERROR, "platform_hal_GetFanSpeed function failure\n");
                return RETURN_ERR;
        }
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
