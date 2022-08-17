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
#include "platform_stub_hal.h"

#define MAX_STRING_SIZE 64
#define RETURN_SUCCESS 0
#define RETURN_FAILURE 1
#define TEST_SUCCESS true
#define TEST_FAILURE false

#define CHECK_PARAM_AND_RET(x) if ((x) == NULL) \
{ \
      DEBUG_PRINT(DEBUG_ERROR,"!!!NULL Pointer!!! :: %s:%d\n", __func__, __LINE__); \
      return RETURN_FAILURE; \
}

/*****************************************************************************************
 * Function name : testmodulepre_requisites
 * Description   : testmodulepre_requisites will  be used for setting the
 *                 pre-requisites that are necessary for this component
 * @param [in]   : None
 * @param [out]  : Return string "SUCCESS" in case of success else return string "FAILURE"
 ******************************************************************************************/
std::string platform_stub_hal::testmodulepre_requisites()
{
        /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
        return "SUCCESS";
}

/*********************************************************************************
 *Function name : testmodulepost_requisites
 *Description   : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *@param [in]   : None
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE based on the return value
 **********************************************************************************/
bool platform_stub_hal::testmodulepost_requisites()
{
        /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
        return TEST_SUCCESS;
}

/************************************************************************************
 *Function name : platform_stub_hal_Init
 *Description   : platform_stub_hal_Init will be used for initiating in CCSP module
 *@param [in]   : szVersion - version, ptrAgentObj - Agent obhect
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE
 ************************************************************************************/

bool platform_stub_hal::initialize(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "platform_stub_hal Initialize\n");
        return TEST_SUCCESS;
}


/*******************************************************************************************
 ** Function name : platform_stub_hal_DocsisParamsDBInit
 ** Description   : This function will invoke the SSP  HAL wrapper to intialize Docsis DB
 ** @param [in]   : req - ParamName : Holds the name of the parameter
 ** @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *******************************************************************************************/
void platform_stub_hal::platform_stub_hal_DocsisParamsDBInit(IN const Json::Value& req, OUT Json::Value& response)
{
	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_DocsisParamsDBInit \n");

	if(ssp_DocsisParamsDBInit() == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = "Docsis Params Init has been success";
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Docsis Params Init has been failure";
		return;
	}
}


/****************************************************************************************
 *Function name : platform_stub_hal_GetBaseMacAddress
 *Description   : This function will invoke the SSP  HAL wrapper to get the MAC Address
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetBaseMacAddress(IN const Json::Value& req, OUT Json::Value& response)
{
	char getMacAddress[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetBaseMacAddress stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetBaseMacAddress(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetBaseMacAddress(getMacAddress);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"]= getMacAddress;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getMacAddress);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "GetBaseMacAddress has been failed";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/************************************************************************************************
 *Function name : platform_stub_hal_GetBootLoaderVersion
 *Description   : This function will invoke the SSP  HAL wrapper to get the GetBootLoaderVersion
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetBootLoaderVersion(IN const Json::Value& req, OUT Json::Value& response)
{
	char getVersion[MAX_STRING_SIZE] = {0};
	int maxSize = MAX_STRING_SIZE;
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetBootLoaderVersion \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetBootloaderVersion(NULL, 0);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetBootloaderVersion(getVersion, maxSize);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getVersion;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getVersion);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Boot Loader Version not  fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/*************************************************************************************************
 *Function name : platform_stub_hal_GetDeviceConfigStatus
 *Description   : This function will invoke the SSP  HAL wrapper to get the GetDeviceConfigStatus
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetDeviceConfigStatus(IN const Json::Value& req, OUT Json::Value& response)
{
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetDeviceConfigStatus stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetDeviceConfigStatus(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetDeviceConfigStatus(getResult);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Config Status not fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}
/*************************************************************************************************
 *Function name : platform_stub_hal_getFactoryPartnerId
 *Description   : This function will invoke the SSP  HAL wrapper to get the getFactoryPartnerId
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************************/
void platform_stub_hal::platform_stub_hal_getFactoryPartnerId(IN const Json::Value& req, OUT Json::Value& response)
{
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_getFactoryPartnerId stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_getFactoryPartnerId(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_getFactoryPartnerId(getResult);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Factory partner ID not fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}
/*************************************************************************************************
 *Function name : platform_stub_hal_GetFirmwareName
 *Description   : This function will invoke the SSP  HAL wrapper to get the GetFirmwareName
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
**************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetFirmwareName(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned long int maxSize = MAX_STRING_SIZE;
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetFirmwareName stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetFirmwareName(NULL, 0);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetFirmwareName(getResult, maxSize);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Firmaware version not  fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/***********************************************************************************************
 *Function name : platform_stub_hal_GetFreeMemorySize
 *Description   : This function will invoke the SSP  HAL wrapper to get the GetFreeMemorySize
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ***********************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetFreeMemorySize(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned long int memSize = 0;
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetFreeMemorySize stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetFreeMemorySize(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetFreeMemorySize(&memSize);
	}
	if(result == RETURN_SUCCESS)
	{
		snprintf(getResult, MAX_STRING_SIZE, "%lu", memSize);
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Memory size staus not fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***************************************************************************
 *Function name : platform_stub_hal_GetHardware
 *Description   : This function will invoke the SSP  HAL wrapper to get the GetHardware
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void platform_stub_hal::platform_stub_hal_GetHardware(IN const Json::Value& req, OUT Json::Value& response)
{
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetHardware stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetHardware(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetHardware(getResult);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Hardware details is not fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/***************************************************************************
 *Function name : platform_stub_hal_GetHardwareFree
 *Description   : This function will invoke the SSP  HAL wrapper to get the GetHardware free memory
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void platform_stub_hal::platform_stub_hal_GetHardwareFree(IN const Json::Value& req, OUT Json::Value& response)
{
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetHardwareFree stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetHardwareMemFree(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetHardwareMemFree(getResult);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Hardware free memory details is not fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***************************************************************************
 *Function name : platform_stub_hal_GetHardwareMemUsed
 *Description   : This function will invoke the SSP  HAL wrapper to get the GetHardware memory used
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void platform_stub_hal::platform_stub_hal_GetHardwareMemUsed(IN const Json::Value& req, OUT Json::Value& response)
{
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetHardwareMemUsed stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetHardwareMemUsed(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetHardwareMemUsed(getResult);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Hardware used memory details is not fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/***************************************************************************
 *Function name : platform_stub_hal_GetHardwareVersion
 *Description   : This function will invoke the SSP  HAL wrapper to get the GetHardware version
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void platform_stub_hal::platform_stub_hal_GetHardwareVersion(IN const Json::Value& req, OUT Json::Value& response)
{
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetHardwareVersion stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetHardwareVersion(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetHardwareVersion(getResult);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Hardware version details is not fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/***************************************************************************
 *Function name : platform_stub_hal_GetModelName
 *Description   : This function will invoke the SSP  HAL wrapper to get the Get Model Name
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void platform_stub_hal::platform_stub_hal_GetModelName(IN const Json::Value& req, OUT Json::Value& response)
{
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetModelName stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetModelName(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetModelName(getResult);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Model Name details is not fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/************************************************************************************************
 *Function name : platform_stub_hal_GetSerialNumber
 *Description   : This function will invoke the SSP  HAL wrapper to get the Get Serail Number
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetSerialNumber(IN const Json::Value& req, OUT Json::Value& response)
{
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetSerialNumber stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetSerialNumber(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetSerialNumber(getResult);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Serial Number details is not fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/********************************************************************************************
 *Function name : platform_stub_hal_GetSNMPEnable
 *Description   : This function will invoke the SSP  HAL wrapper to get the Get SNMP details
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *********************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetSNMPEnable(IN const Json::Value& req, OUT Json::Value& response)
{
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetSNMPEnable stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetSNMPEnable(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetSNMPEnable(getResult);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "SNMP status details is not fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/**************************************************************************************************
 *Function name : platform_stub_hal_GetSoftwareVersion
 *Description   : This function will invoke the SSP  HAL wrapper to get the Get software version
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ***************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetSoftwareVersion(IN const Json::Value& req, OUT Json::Value& response)
{
	char getResult[MAX_STRING_SIZE] = {0};
	unsigned long int maxSize = MAX_STRING_SIZE;
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetSoftwareVersion stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetSoftwareVersion(NULL, 0);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetSoftwareVersion(getResult, maxSize);
	}
	if(result == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Software Version not  fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/*****************************************************************************************************
 *Function name : platform_stub_hal_GetSSHEnable
 *Description   : This function will invoke the SSP  HAL wrapper to get the Get SSH Enable status
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetSSHEnable(IN const Json::Value& req, OUT Json::Value& response)
{
	BOOLEAN flag = 0;
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetSSHEnable stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetSSHEnable(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetSSHEnable(&flag);
	}
	if(result == RETURN_SUCCESS)
	{
		snprintf(getResult, MAX_STRING_SIZE, "%d", flag);
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "SSH Enable not  fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}

/**********************************************************************************************************
 *Function name : platform_stub_hal_GetTelnetEnable
 *Description   : This function will invoke the SSP  HAL wrapper to get the Get Telnet Enable status
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ***********************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetTelnetEnable(IN const Json::Value& req, OUT Json::Value& response)
{
	BOOLEAN flag = 0;
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetTelnetEnable stub \n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetTelEnable(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetTelEnable(&flag);
	}
	if(result == RETURN_SUCCESS)
	{
		snprintf(getResult, MAX_STRING_SIZE, "%d", flag);
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Telnet Enable not fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}



/**************************************************************************************************
 *Function name : platform_stub_hal_GetTotalMemorySize
 *Description   : This function will invoke the SSP  HAL wrapper to get the Get Total memory size
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetTotalMemorySize(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned long int memSize = 0;
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetTotalMemorySize stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetTotalMemorySize(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetTotalMemorySize(&memSize);
	}
	if(result == RETURN_SUCCESS)
	{
		snprintf(getResult, MAX_STRING_SIZE, "%lu", memSize);
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Memory size not  fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************
 *Function name : platform_stub_hal_GetUsedMemorySize
 *Description   : This function will invoke the SSP  HAL wrapper to get the Get Used Memory Size
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetUsedMemorySize(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned long int memSize = 0;
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetUsedMemorySize stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetUsedMemorySize(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetUsedMemorySize(&memSize);
	}
	if(result == RETURN_SUCCESS)
	{
		snprintf(getResult, MAX_STRING_SIZE, "%lu", memSize);
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Used Memory size not  fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************
 *Function name : platform_stub_hal_GetWebUITimeout
 *Description   : This function will invoke the SSP HAL wrapper to Get the Web UI Timeout
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetWebUITimeout(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned long int ulSize = 0;
	char getResult[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;
	int result = RETURN_FAILURE;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetWebUITimeout stub\n");

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(isNegativeScenario)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
		result = ssp_GetWebUITimeout(NULL);
	}
	else
	{
		DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
		result = ssp_GetWebUITimeout(&ulSize);
	}
	if(result == RETURN_SUCCESS)
	{
		snprintf(getResult, MAX_STRING_SIZE, "%lu", ulSize);
		response["result"] = "SUCCESS";
		response["details"] = getResult;

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "WebUI Timeout value not  fetched successfully";

		DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
		return;
	}
}


/***********************************************************************************************
 *Function name : platform_stub_hal_PandMDBInit
 *Description   : This function will invoke the SSP HAL wrapper to Get the PandMDB Init
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/
void platform_stub_hal::platform_stub_hal_PandMDBInit(IN const Json::Value& req, OUT Json::Value& response)
{
	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_PandMDBInit stub\n");
	if(ssp_PandMDBInit() == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = "PandMDBInit fetched successfully";;
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "PandMDBInit not  fetched successfully";
		return;
	}
}


/***************************************************************************************************
 *Function name : platform_stub_hal_SetSNMPEnable
 *Description   : This function will invoke the SSP HAL wrapper to set the SNMP Enable
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/

void platform_stub_hal::platform_stub_hal_SetSNMPEnable(IN const Json::Value& req, OUT Json::Value& response)
{
	int flag = 0;
	char setFlag[MAX_STRING_SIZE] = {0};

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_SetSNMPEnable stub\n");
	if(&req["index"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	flag = req["index"].asInt();

	if(flag < 0 || flag > 1)
	{
		response["result"] = "FAILURE";
		response["details"] = "Invalid parameter";
		return;
	}

	if(flag == 0)
	{
		strncpy(setFlag,"stopped", MAX_STRING_SIZE);
	}
	else
	{
		strncpy(setFlag,"started", MAX_STRING_SIZE);
	}

	if(ssp_SetSNMPEnable(setFlag) == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = "Set SNMP Enable fetched successfully";
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Set SNMP Enable not  fetched successfully";
		return;
	}
}

/***********************************************************************************************
 *Function name : platform_stub_hal_SetSSHEnable
 *Description   : This function will invoke the SSP HAL wrapper to set the SSH Enable
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/
void platform_stub_hal::platform_stub_hal_SetSSHEnable(IN const Json::Value& req, OUT Json::Value& response)
{
	int flag = 0;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_SetSSHEnable stub\n");
	if(&req["index"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	flag = req["index"].asInt();
	if(flag < 0 || flag > 1)
	{
		response["result"] = "FAILURE";
		response["details"] = "Invalid parameter";
		return;
	}

	if(ssp_SetSSHEnable(flag) == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = "Set SSH Enable fetched successfully";
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Set SSH Enable not fetched successfully";
		return;
	}
}


/***************************************************************************************************
 *Function name : platform_stub_hal_SetTelnetEnable
 *Description   : This function will invoke the SSP HAL wrapper to set the Telnet Enable
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/
void platform_stub_hal::platform_stub_hal_SetTelnetEnable(IN const Json::Value& req, OUT Json::Value& response)
{

	int index = 0;
	bool setTelnet = 0;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_SetTelnetEnable stub\n");
	if(&req["index"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	index = req["index"].asInt();
	if(index == 0)
	{
		setTelnet = 0;
	}
	else if(index == 1)
	{
		setTelnet = 1;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Invalid parameter";
		return;
	}

	if(ssp_SetTelnetEnable(setTelnet) == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = "Set Telnet Enable fetched successfully";
		return;

	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Set Telnet Enable not fetched successfully";
		return;
	}
}


/***********************************************************************************************
 *Function name : platform_stub_hal_SetWebUITimeout
 *Description   : This function will invoke the SSP HAL wrapper to Set WebUIT imeout
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/
void platform_stub_hal::platform_stub_hal_SetWebUITimeout(IN const Json::Value& req, OUT Json::Value& response)
{
	unsigned long int timeOut = 0;

	if(&req["index"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	timeOut = req["index"].asInt();

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_SetWebUITimeout stub\n");

	if(ssp_SetWebUITimeout(timeOut) == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = "Set WebUI Timeout fetched successfully";
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "Set WebUI Timeout not  fetched successfully";
		return;
	}
}

/***********************************************************************************************
 *Function name : platform_stub_hal_GetFactoryResetCount
 *Description   : This function will invoke the SSP  HAL wrapper to get the Get Factory Reset Count
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetFactoryResetCount(IN const Json::Value& req, OUT Json::Value& response)
{
       unsigned long int resetCount = 0;
       char getResult[MAX_STRING_SIZE] = {0};
       int isNegativeScenario = 0;
       int result = RETURN_FAILURE;
       DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetFactoryResetCount\n");
       if(&req["flag"])
       {
               isNegativeScenario = req["flag"].asInt();
       }
       if(isNegativeScenario)
       {
               DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
               result = ssp_GetFactoryResetCount(NULL);
       }
       else
       {
               DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
               result = ssp_GetFactoryResetCount(&resetCount);
       }
       if(result == RETURN_SUCCESS)
       {
               snprintf(getResult, MAX_STRING_SIZE, "%lu", resetCount);
               response["result"] = "SUCCESS";
               response["details"] = getResult;
               DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
               return;
       }
       else
       {
               response["result"] = "FAILURE";
               response["details"] = "Factory Reset count not  fetched successfully";
               DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
               return;
       }
}

/***************************************************************************************************
 *Function name : platform_stub_hal_ClearResetCount
 *Description   : This function will invoke the SSP HAL wrapper to clear the reset count
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/
void platform_stub_hal::platform_stub_hal_ClearResetCount(IN const Json::Value& req, OUT Json::Value& response)
{
        int index = 0;
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_ClearResetCount stub\n");
        if(&req["index"] == NULL)
        {
                response["result"] = "FAILURE";
                response["details"] = "NULL parameter as input argument";
                return;
        }
        index = req["index"].asInt();
        if(ssp_ClearResetCount(index) == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                response["details"] = "Cleared reset count successfully";
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "Failed to clear the reset count";
                return;
        }
}

/***************************************************************************
 *Function name : platform_stub_hal_GetTimeOffSet
 *Description   : This function will invoke the SSP  HAL wrapper to get the GetTimeOffSet
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void platform_stub_hal::platform_stub_hal_GetTimeOffSet(IN const Json::Value& req, OUT Json::Value& response)
{
        char getResult[MAX_STRING_SIZE] = {0};
        int isNegativeScenario = 0;
        int result = RETURN_FAILURE;
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetTimeOffSet stub \n");
        if(&req["flag"])
        {
                isNegativeScenario = req["flag"].asInt();
        }
        if(isNegativeScenario)
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
                result = ssp_GetTimeOffSet(NULL);
        }
        else
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
                result = ssp_GetTimeOffSet(getResult);
        }
        if(result == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                response["details"] = getResult;
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "TimeOffSet details is not fetched successfully";
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
                return;
        }
}

/***************************************************************************
 *Function name : platform_stub_hal_GetCMTSMac
 *Description   : This function will invoke the SSP  HAL wrapper to get the GetCMTSMac
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void platform_stub_hal::platform_stub_hal_GetCMTSMac(IN const Json::Value& req, OUT Json::Value& response)
{
        char getResult[MAX_STRING_SIZE] = {0};
        int isNegativeScenario = 0;
        int result = RETURN_FAILURE;
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetCMTSMac stub \n");
        if(&req["flag"])
        {
                isNegativeScenario = req["flag"].asInt();
        }
        if(isNegativeScenario)
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
                result = ssp_GetCMTSMac(NULL);
        }
        else
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
                result = ssp_GetCMTSMac(getResult);
        }
        if(result == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                response["details"] = getResult;
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "CMTSMac details is not fetched successfully";
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
                return;
        }
}

/*************************************************************************************************
 *Function name : platform_stub_hal_GetChipTemperature
 *Description   : This function will invoke the SSP  HAL wrapper to get the ChipTemperature
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
**************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetChipTemperature(IN const Json::Value& req, OUT Json::Value& response)
{
        unsigned int chipIndex = 0;
        unsigned long int TempValue = 0;
        char getResult[MAX_STRING_SIZE] = {0};
        int isNegativeScenario = 0;
        int result = RETURN_FAILURE;
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetChipTemperature stub \n");
        chipIndex = req["chipIndex"].asInt();
        if(&req["flag"])
        {
                isNegativeScenario = req["flag"].asInt();
        }
        if(isNegativeScenario)
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
                result = ssp_GetChipTemperature(0, NULL);
        }
        else
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
                result = ssp_GetChipTemperature(chipIndex, &TempValue);
        }
        if(result == RETURN_SUCCESS)
        {
                snprintf(getResult, MAX_STRING_SIZE, "%lu", TempValue);
                response["result"] = "SUCCESS";
                response["details"] = getResult;
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "ChipTemperature not fetched successfully";
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
                return;
        }
}

/***********************************************************************************************
 *Function name : platform_stub_hal_GetFanSpeed
 *Description   : This function will invoke the SSP HAL wrapper to Get the FanSpeed
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetFanSpeed(IN const Json::Value& req, OUT Json::Value& response)
{
        unsigned long int SpeedValue = 0;
        char getResult[MAX_STRING_SIZE] = {0};
        int isNegativeScenario = 0;
        int result = RETURN_FAILURE;
        unsigned int fanIndex = 0;
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetFanSpeed stub\n");
        if(&req["flag"])
        {
                isNegativeScenario = req["flag"].asInt();
        }
        fanIndex = req["fanIndex"].asInt();
        if(isNegativeScenario)
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
                result = ssp_GetFanSpeed(fanIndex,NULL);
        }
        else
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
                result = ssp_GetFanSpeed(fanIndex,&SpeedValue);
        }
        if(result == RETURN_SUCCESS)
        {
                snprintf(getResult, MAX_STRING_SIZE, "%lu", SpeedValue);
                response["result"] = "SUCCESS";
                response["details"] = getResult;
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "FanSpeed not  fetched successfully";
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
                return;
        }
}

/***********************************************************************************************
 *Function name : platform_stub_hal_SetFanSpeed
 *Description   : This function will invoke the SSP HAL wrapper to Set FanSpeed
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/
void platform_stub_hal::platform_stub_hal_SetFanSpeed(IN const Json::Value& req, OUT Json::Value& response)
{
        unsigned long int SpeeddInRpms = 0;
        if(&req["index"] == NULL)
        {
                response["result"] = "FAILURE";
                response["details"] = "NULL parameter as input argument";
                return;
        }
        SpeeddInRpms = req["index"].asInt();
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_SetFanSpeed stub\n");
        if(ssp_SetFanSpeed(SpeeddInRpms) == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                response["details"] = "Set fan speed successfully";
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "Failed to set fan speed";
                return;
        }
}


/***********************************************************************************************
 *Function name : platform_stub_hal_SetMACsecEnable
 *Description   : This function will invoke the SSP HAL wrapper to set the MACsec Enable
 *@param [in]   : req - ethPort: Ethernet Port Number index: To enable/Disable the MACsec
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************/
void platform_stub_hal::platform_stub_hal_SetMACsecEnable(IN const Json::Value& req, OUT Json::Value& response)
{
        int ethPort = 0, flag = 0;

        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_SetSSHEnable stub\n");
        if(&req["ethPort"] == NULL || &req["index"] == NULL)
        {
                response["result"] = "FAILURE";
                response["details"] = "NULL parameter as input argument";
                return;
        }
        ethPort = req["ethPort"].asInt();
        flag = req["index"].asInt();
        if(ethPort < 1 || ethPort > 4 || flag < 0 || flag > 1)
        {
                response["result"] = "FAILURE";
                response["details"] = "Invalid parameter";
                return;
        }

        if(ssp_SetMACsecEnable(ethPort,flag) == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                response["details"] = "Set MACsec Enable fetched successfully";
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "Set MACsec Enable not fetched successfully";
                return;
        }
}

/*****************************************************************************************************
 *Function name : platform_stub_hal_GetMACsecEnable
 *Description   : This function will invoke the SSP HAL wrapper to get the Get MACsec Enable status
 *@param [in]   : req - ethPort: Ethernet Port Number , flag: To set Postitive or Negative Scenario
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetMACsecEnable(IN const Json::Value& req, OUT Json::Value& response)
{
        BOOLEAN index = 0;
	int ethPort = 0;
        char getResult[MAX_STRING_SIZE] = {0};
        int isNegativeScenario = 0;
        int result = RETURN_FAILURE;

        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetMACsecEnable stub \n");

	if(&req["ethPort"] == NULL)
	{
                response["result"] = "FAILURE";
                response["details"] = "NULL parameter as input argument";
                return;
	}
	ethPort = req["ethPort"].asInt();

        if(&req["index"])
        {
                isNegativeScenario = req["index"].asInt();
        }

        if(isNegativeScenario)
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
                result = ssp_GetMACsecEnable(ethPort,NULL);
        }
        else
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
                result = ssp_GetMACsecEnable(ethPort,&index);
        }
        if(result == RETURN_SUCCESS)
        {
                snprintf(getResult, MAX_STRING_SIZE, "%d", index);
                response["result"] = "SUCCESS";
                response["details"] = getResult;

                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "MACsec Enable not  fetched successfully";

                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
                return;
        }
}


/*****************************************************************************************************
 *Function name : platform_stub_hal_GetMACsecOperationalStatus
 *Description   : This function will invoke the HAL wrapper to get the Get MACsec Operation status
 *@param [in]   : req - ethPort: Ethernet Port Number, index: To set negative or positive scenario
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetMACsecOperationalStatus(IN const Json::Value& req, OUT Json::Value& response)
{
        BOOLEAN index = 0;
	int ethPort = 0;
        char getResult[MAX_STRING_SIZE] = {0};
        int isNegativeScenario = 0;
        int result = RETURN_FAILURE;
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetMACsecOperationalStatus stub \n");

        if(&req["ethPort"] == NULL  || &req["index"] == NULL )
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	ethPort = req["ethPort"].asInt();

        if(&req["index"])
        {
                isNegativeScenario = req["index"].asInt();
        }

        if(isNegativeScenario)
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
                result = ssp_GetMACsecOperationalStatus(ethPort,NULL);
        }
        else
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
                result = ssp_GetMACsecOperationalStatus(ethPort,&index);
        }
        if(result == RETURN_SUCCESS)
        {
                snprintf(getResult, MAX_STRING_SIZE, "%d", index);
                response["result"] = "SUCCESS";
                response["details"] = getResult;

                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "MACsec Operational Status not  fetched successfully";

                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
                return;
        }
}

/*****************************************************************************************************
 *Function name : platform_stub_hal_getFactoryCmVariant
 *Description   : This function will invoke the HAL wrapper to get the Factory CM Variant value
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void platform_stub_hal::platform_stub_hal_getFactoryCmVariant(IN const Json::Value& req, OUT Json::Value& response)
{
        char getResult[MAX_STRING_SIZE] = {0};
        int result = RETURN_FAILURE;
        int isNegativeScenario = 0;

        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_getFactoryCmVariant stub\n");

        if(&req["flag"])
        {
                isNegativeScenario = req["flag"].asInt();
        }

        if(isNegativeScenario)
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
                result = ssp_getFactoryCmVariant(NULL);
        }
        else
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
                result = ssp_getFactoryCmVariant(getResult);
        }
        if(result == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                response["details"] = getResult;
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "Get Factory Cm varient details is not fetched successfully";
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
                return;
        }
}

/*****************************************************************************************************
 *Function name : platform_stub_hal_setFactoryCmVariant
 *Description   : This function will invoke the HAL wrapper to set the Factory CM Variant value
 *@param [in]   : req - CmVarient: Holds the value of CmVarient
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void platform_stub_hal::platform_stub_hal_setFactoryCmVariant(IN const Json::Value& req, OUT Json::Value& response)
{
        char getResult[MAX_STRING_SIZE] = {0};
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_setFactoryCmVariant stub\n");
        if(&req["CmVarient"] == NULL)
        {
                response["result"] = "FAILURE";
                response["details"] = "NULL parameter as input argument";
                return;
        }
        strcpy(getResult, req["CmVarient"].asCString());

        if(ssp_setFactoryCmVariant(getResult) == RETURN_SUCCESS )
        {
                response["result"] = "SUCCESS";
                response["details"] = "Set Factory CmVarient fetched successfully";
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "Set Factory CmVarient not  fetched successfully";
                return;
        }
}

/*****************************************************************************************************
 *Function name : platform_stub_hal_getRPM
 *Description   : This function will invoke the HAL wrapper to get the RPM value
 *@param [in]   : fanIndex - the index of the fan for which RPM is to be retrieved
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void platform_stub_hal::platform_stub_hal_getRPM(IN const Json::Value& req, OUT Json::Value& response)
{
        unsigned int rpmValue = 0;
        char details[MAX_STRING_SIZE] = {0};
        unsigned int fanIndex = 0;
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_getRPM stub\n");
        fanIndex = req["fanIndex"].asInt();

        if(ssp_getRPM(fanIndex,&rpmValue) == RETURN_SUCCESS)
        {
                sprintf(details, "RPM value is :%u", rpmValue);
                response["result"] = "SUCCESS";
                response["details"] = details;
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %u\n", __func__, rpmValue);
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "RPM details is not fetched successfully";
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
                return;
        }
}

/*****************************************************************************************************
 *Function name : platform_stub_hal_getRotorLock
 *Description   : This function will invoke the HAL wrapper to get the Rotor Lock value
 *@param [in]   : fanIndex - the index of the fan for which the Rotor Lock value needs to be retrieved
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void platform_stub_hal::platform_stub_hal_getRotorLock(IN const Json::Value& req, OUT Json::Value& response)
{
        int rotorLock = 0;
        unsigned int fanIndex = 0;
        char details[MAX_STRING_SIZE] = {0};
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_getRotorLock stub\n");
        fanIndex = req["fanIndex"].asInt();
        if(ssp_getRotorLock(fanIndex,&rotorLock) == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                sprintf(details,"Rotor Lock value is :%d",rotorLock);
                response["details"] = details;
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %d\n", __func__, rotorLock);
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "Rotor Lock details is not fetched successfully";
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
                return;
        }
}

/*****************************************************************************************************
 *Function name : platform_stub_hal_getFanStatus
 *Description   : This function will invoke the HAL wrapper to get the Fan status value
 *@param [in]   : fanIndex - the index of the fan for which status is to be retrieved
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void platform_stub_hal::platform_stub_hal_getFanStatus(IN const Json::Value& req, OUT Json::Value& response)
{
        int fanstatus = 0;
        unsigned int fanIndex = 0;
        char details[MAX_STRING_SIZE] = {0};
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_getFanStatus stub\n");
        fanIndex = req["fanIndex"].asInt();
        if(ssp_getFanStatus(fanIndex,&fanstatus) == RETURN_SUCCESS)
	{
                response["result"] = "SUCCESS";
                sprintf(details,"Fan Status is :%d",fanstatus);
                response["details"] = details;
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, details);
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "Get Fan Status details is not fetched successfully";
                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
                return;
        }
}

/*****************************************************************************************************
 *Function name : platform_stub_hal_ssp_setFanMaxOverride
 *Description   : This function will invoke the HAL wrapper to set the Fan Max override
 *@param [in]   : req - flag : To set the Fan Max override
 *@param [in]   : req - fanIndex : Fan index starting from 0
 *param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void platform_stub_hal::platform_stub_hal_setFanMaxOverride(IN const Json::Value& req, OUT Json::Value& response)
{
        int flag = 0;
        unsigned int fanIndex = 0;
        BOOLEAN setFlag = 0;
        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_SetFanMaxOverride stub\n");
        if(&req["flag"] == NULL)
        {
                response["result"] = "FAILURE";
                response["details"] = "NULL parameter as input argument";
                return;
        }
        if(&req["fanIndex"] == NULL)
        {
                response["result"] = "FAILURE";
                response["details"] = "NULL parameter as input argument";
                return;
        }
        flag = req["flag"].asInt();
        fanIndex = (unsigned int)req["fanIndex"].asInt();
        if(flag == 0)
        {
                setFlag = 0;
        }
        else if(flag == 1)
        {
                setFlag = 1;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "Invalid parameter";
                return;
        }

        if(ssp_setFanMaxOverride(setFlag, fanIndex) == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                response["details"] = "Set FanMaxOverride fetched successfully";
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "Set FanMaxOverride not fetched successfully";
                return;
        }
}

/*****************************************************************************************************
 *Function name : platform_stub_hal_SetSNMPOnboardRebootEnable
 *Description   : This function will invoke the HAL wrapper to set the SNMP Onboard Reboot Enable
 *@param [in]   : req - SNMPonboard: Holds the  enable or disable value for SNMP onboard Reboot
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void platform_stub_hal::platform_stub_hal_SetSNMPOnboardRebootEnable(IN const Json::Value& req, OUT Json::Value& response)
{
        char setFlag[MAX_STRING_SIZE] = {'\0'};

        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_SetSNMPOnboardRebootEnable stub\n");
        if(&req["SNMPonboard"] == NULL)
        {
                response["result"] = "FAILURE";
                response["details"] = "NULL parameter as input argument";
                return;
        }
        strcpy(setFlag, req["SNMPonboard"].asCString());

        if(ssp_SetSNMPOnboardRebootEnable(setFlag) == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                response["details"] = "Set SNMP onboard Reboot Enable fetched successfully";
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "Set SNMP  onboard Reboot Enable not  fetched successfully";
                return;
        }
}


/*************************************************************************************************
 *Function name : platform_stub_hal_GetGetRouterRegion
 *Description   : This function will invoke the SSP  HAL wrapper to get the RouterRegion
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetRouterRegion(IN const Json::Value& req, OUT Json::Value& response)
{
        char getResult[MAX_STRING_SIZE] = {0};
        int isNegativeScenario = 0;
        int result = RETURN_FAILURE;

        DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetRouterRegion stub\n");

        if(&req["flag"])
        {
                isNegativeScenario = req["flag"].asInt();
        }

        if(isNegativeScenario)
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
                result = ssp_GetRouterRegion(NULL);
        }
        else
        {
                DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
                result = ssp_GetRouterRegion(getResult);
        }
        if(result == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                response["details"] = getResult;

                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "RouterRegion not fetched successfully";

                DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
                return;
        }
}

/************************************************************************************************
 *Function name : platform_hal_GetMemoryPaths
 *Description   : This function will invoke the SSP  HAL wrapper to get the GetMemoryPaths
 *@param [in]   : cpus  : Holds the value of CPUS
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetMemoryPaths(IN const Json::Value& req, OUT Json::Value& response)
{
    char details[1024] = {0};
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_hal_GetMemoryPaths stub\n");

    RDK_CPUS cpus = HOST_CPU;
    int cpus_1 = 0;
    int isNegativeScenario = 0;
    int result = RETURN_FAILURE;

    PLAT_PROC_MEM_INFO *PPLAT_PROC_MEM_INFO =  NULL;
    PPLAT_PROC_MEM_INFO = (PLAT_PROC_MEM_INFO*)malloc(sizeof(PLAT_PROC_MEM_INFO));
    if (PPLAT_PROC_MEM_INFO != NULL) {
        memset(PPLAT_PROC_MEM_INFO, 0, sizeof(PLAT_PROC_MEM_INFO));
    }

    if(&req["cpus"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }
    cpus_1 = req["cpus"].asInt();
    cpus = (RDK_CPUS)cpus_1;

    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }

    if(isNegativeScenario)
    {
        DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
        result = ssp_GetMemoryPaths(cpus,NULL);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
        result = ssp_GetMemoryPaths(cpus,&PPLAT_PROC_MEM_INFO);
    }

    if(result == RETURN_SUCCESS)
    {
        response["result"] = "SUCCESS";
        sprintf(details,"dramPath=%s emmcPath1=%s and emmcPath2=%s ",(*PPLAT_PROC_MEM_INFO).dramPath,(*PPLAT_PROC_MEM_INFO).emmcPath1,(*PPLAT_PROC_MEM_INFO).emmcPath2);
        response["details"] = details;
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, details);
        return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "GetMemoryPaths details is not fetched successfully";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
        return;
    }
}

/************************************************************************************************
 *Function name : platform_hal_SetLowPowerModeState
 *Description   : This function will invoke the SSP  HAL wrapper to set the LowPowerModeState
 *@param [in]   : state  : Holds the value of Power State
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void platform_stub_hal::platform_stub_hal_SetLowPowerModeState(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_hal_SetLowPowerModeState stub\n");
    PSM_STATE  state = PSM_AC;
    int state1 = 1;
    if(&req["state"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }
    state1 = req["state"].asInt();
    state = (PSM_STATE)state1;

    if(ssp_SetLowPowerModeState(state) == RETURN_SUCCESS)
    {
        response["result"] = "SUCCESS";
        response["details"] = "SetLowPowerModeState function was successful";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful", __func__);
        return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "SetLowPowerModeState function was NOT successful, Please check logs";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
        return;
    }
}

/************************************************************************************************
 *Function name : platform_hal_StartMACsec
 *Description   : This function will invoke the SSP  HAL wrapper to Start MAC security
 *@param [in]   : state  : Holds the value of Power State
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void platform_stub_hal::platform_stub_hal_StartMACsec(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_hal_StartMACsec stub\n");
    int ethPort = 1;
    int timeoutSec = 1;

    if(&req["ethPort"] == NULL && &req["timeoutSec"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    ethPort = req["ethPort"].asInt();
    timeoutSec = req["timeoutSec"].asInt();

    if(ssp_StartMACsec(ethPort,timeoutSec) == RETURN_SUCCESS)
    {
        response["result"] = "SUCCESS";
        response["details"] = "StartMACsec function was successful";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful\n", __func__);
        return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "StartMACsec function was NOT successful, Please check logs";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
        return;
    }
}

/************************************************************************************************
 *Function name : platform_hal_StopMACsec
 *Description   : This function will invoke the SSP  HAL wrapper to set the LowPowerModeState
 *@param [in]   : state  : Holds the value of Power State
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void platform_stub_hal::platform_stub_hal_StopMACsec(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_hal_StartMACsec stub\n");
    int ethPort = 1;

    if(&req["ethPort"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    ethPort = req["ethPort"].asInt();

    if(ssp_StopMACsec(ethPort) == RETURN_SUCCESS)
    {
        response["result"] = "SUCCESS";
        response["details"] = "StartMACsec function was successful";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful\n", __func__);
        return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "StartMACsec function was NOT successful, Please check logs";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
        return;
    }
}
/*****************************************************************************************************
 *Function name : platform_stub_hal_GetWebAccessLevel
 *Description   : This function will invoke the HAL wrapper to get the Web Access Level value
 *@param [in]   : req - ParamName : Holds the name of the parameter
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetWebAccessLevel(IN const Json::Value& req, OUT Json::Value& response)
{
    unsigned long int level = 0;
    char getResult[MAX_STRING_SIZE] = {0};
    int isNegativeScenario = 0;
    int user_index = 0;
    int if_index = 0;
    int result = RETURN_FAILURE;
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetWebAccessLevel stub\n");
    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }
    if(&req["userIndex"])
    {
        user_index = req["userIndex"].asInt();
    }
    if(&req["ifIndex"])
    {
        if_index = req["ifIndex"].asInt();
    }
    if(isNegativeScenario)
    {
        DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
        result = ssp_GetWebAccessLevel(user_index, if_index, NULL);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE, "Executing positive scenario\n");
        result = ssp_GetWebAccessLevel(user_index, if_index, &level);
    }
    if(result == RETURN_SUCCESS)
    {
        snprintf(getResult, MAX_STRING_SIZE, "%lu", level);
        response["result"] = "SUCCESS";
        response["details"] = getResult;
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful:: result = %s\n", __func__, getResult);
        return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "Level not fetched successfully";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
        return;
    }
}


/************************************************************************************************
 *Function name : platform_stub_hal_SetDscp
 *Description   : This function will invoke the SSP  HAL wrapper to Control/Set traffic counting based on Dscp value
 *@param [in]   : interfaceType - 1 for DOCSIS , 2 for EWAN
 *@param [in]   : cmd - START/STOP
 *@param [in]   : dscpVal - comma seperated string , e.g. "10,0" , NULL
 *@param [in]   : isDscpValNull - whether the dscpVal is Null or not
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void platform_stub_hal::platform_stub_hal_SetDscp(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_SetDscp\n");
    WAN_INTERFACE  interfaceType = DOCSIS;
    TRAFFIC_CNT_COMMAND cmd = TRAFFIC_CNT_START;
    int nullFlag = 0;
    char dscpVal[100] = {'\0'};
    int returnValue = RETURN_FAILURE;

    if(&req["interfaceType"] == NULL || &req["cmd"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameters as input argument";
        return;
    }

    interfaceType = (WAN_INTERFACE)req["interfaceType"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\nInterface Type : %s", (interfaceType == DOCSIS) ? "DOCSIS" :  "EWAN");

    cmd = (TRAFFIC_CNT_COMMAND)req["cmd"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\nTraffic count command : %s", (cmd == TRAFFIC_CNT_START) ? "TRAFFIC_CNT_START" :  "TRAFFIC_CNT_STOP");

    if(&req["isDscpValNull"])
    {
        nullFlag = req["isDscpValNull"].asInt();
    }

    if(nullFlag)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\nDSCP Values to be set is Null");
        returnValue = ssp_setDscp(interfaceType, cmd, NULL);
    }
    else
    {
        if(&req["dscpVal"] == NULL)
        {
            response["result"] = "FAILURE";
            response["details"] = "NULL dscpVal parameter as input argument";
            return;
        }
        strcpy(dscpVal, req["dscpVal"].asCString());
        DEBUG_PRINT(DEBUG_TRACE,"\nDSCP Values : %s", dscpVal);

        returnValue = ssp_setDscp(interfaceType, cmd, dscpVal);
    }

    DEBUG_PRINT(DEBUG_TRACE,"\nReturn status from ssp_setDscp: %d", returnValue);

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"] = "SUCCESS";
        response["details"] = "platform_hal_setDscp() function invocation was successful";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful", __func__);
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "platform_hal_setDscp() function invocation was NOT successful, Please check logs";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
    }

    DEBUG_PRINT(DEBUG_TRACE,"\nplatform_stub_hal_SetDscp ---->Exiting\n");
    return;
}


/************************************************************************************************
 *Function name : platform_stub_hal_ResetDscpCounts
 *Description   : This function will invoke the SSP  HAL wrapper to reset Dscp Counter values
 *@param [in]   : interfaceType - 1 for DOCSIS , 2 for EWAN
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void platform_stub_hal::platform_stub_hal_ResetDscpCounts(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_ResetDscpCounts\n");
    WAN_INTERFACE  interfaceType = DOCSIS;
    int returnValue = RETURN_FAILURE;

    if(&req["interfaceType"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL interfaceType parameter as input argument";
        return;
    }
    interfaceType = (WAN_INTERFACE)req["interfaceType"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\nInterface Type : %s", (interfaceType == DOCSIS) ? "DOCSIS" :  "EWAN");

    returnValue = ssp_resetDscpCounts(interfaceType);
    DEBUG_PRINT(DEBUG_TRACE,"\nReturn status from ssp_resetDscpCounts: %d", returnValue);

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"] = "SUCCESS";
        response["details"] = "platform_hal_resetDscpCounts() function invocation was successful";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful", __func__);
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "platform_hal_resetDscpCounts() function invocation was NOT successful, Please check logs";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
    }

    DEBUG_PRINT(DEBUG_TRACE,"\nplatform_stub_hal_ResetDscpCounts ---->Exiting\n");
    return;
}


/************************************************************************************************
 *Function name : platform_stub_hal_GetDscpClientList
 *Description   : This function will invoke the SSP  HAL wrapper to get the counter data
 *@param [in]   : interfaceType - 1 for DOCSIS , 2 for EWAN
 *@param [in]   : isClientListNull - whether the clientList buffer is NULL or not
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void platform_stub_hal::platform_stub_hal_GetDscpClientList(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function platform_stub_hal_GetDscpClientList\n");
    WAN_INTERFACE  interfaceType = DOCSIS;
    DSCP_list_t clientList;
    int returnValue = RETURN_FAILURE;
    int isNegativeScenario = 0;
    unsigned int iteration = 0;
    unsigned int client = 0;
    char output[2000] = {'\0'};
    char details[4000] = {'\0'};

    if(&req["interfaceType"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL interfaceType parameter as input argument";
        return;
    }
    interfaceType = (WAN_INTERFACE)req["interfaceType"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\nInterface Type : %s", (interfaceType == DOCSIS) ? "DOCSIS" :  "EWAN");

    if(&req["isClientListNull"])
    {
        isNegativeScenario = req["isClientListNull"].asInt();
    }

    if(isNegativeScenario)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\nExecuting Negative Scenario by passing Null Buffer input");
        returnValue = ssp_getDscpClientList(interfaceType, NULL);
    }
    else
    {
        returnValue = ssp_getDscpClientList(interfaceType, &clientList);
    }

    DEBUG_PRINT(DEBUG_TRACE,"\nReturn status from ssp_getDscpClientList: %d", returnValue);

    if(returnValue == RETURN_SUCCESS)
    {
        DEBUG_PRINT(DEBUG_TRACE,"platform_hal_getDscpClientList() function invocation was successful; Total DSCP number of elements = %d", clientList.numElements);
        sprintf(output, "platform_hal_getDscpClientList() function invocation was successful; Total DSCP number of elements = %d", clientList.numElements);
        strcat(details, output);

        for (iteration = 0; iteration < clientList.numElements; iteration++)
        {
            DEBUG_PRINT(DEBUG_TRACE,"For DSCP element[%d], DSCP value[%d], DSCP numClients[%d] :", iteration, clientList.DSCP_Element[iteration].dscp_value, clientList.DSCP_Element[iteration].numClients);
            sprintf(output, "; For DSCP element[%d], DSCP value[%d], DSCP numClients[%d] :", iteration, clientList.DSCP_Element[iteration].dscp_value, clientList.DSCP_Element[iteration].numClients);
            strcat(details, output);

            for (client = 0; client < clientList.DSCP_Element[iteration].numClients; client++)
            {
                DEBUG_PRINT(DEBUG_TRACE,"DSCP client num[%d] :- ", client);
                DEBUG_PRINT(DEBUG_TRACE,"mac - %s", clientList.DSCP_Element[iteration].Client[client].mac);
                DEBUG_PRINT(DEBUG_TRACE,"rxBytes - %ld", clientList.DSCP_Element[iteration].Client[client].rxBytes);
                DEBUG_PRINT(DEBUG_TRACE,"txBytes - %ld", clientList.DSCP_Element[iteration].Client[client].txBytes);

                sprintf(output, " DSCP client num[%d]:- mac - %s, rxBytes - %ld, txBytes - %ld", client, clientList.DSCP_Element[iteration].Client[client].mac, clientList.DSCP_Element[iteration].Client[client].rxBytes, clientList.DSCP_Element[iteration].Client[client].txBytes);
                strcat(details, output);
            }
        }

        response["result"] = "SUCCESS";
        response["details"] = details;
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution successful", __func__);
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "platform_hal_getDscpClientList() function invocation was NOT successful, Please check logs";
        DEBUG_PRINT(DEBUG_TRACE, "%s:: Test execution failed\n", __func__);
    }

    DEBUG_PRINT(DEBUG_TRACE,"\nplatform_stub_hal_GetDscpClientList ---->Exiting\n");
    return;
}


/********************************************************************************************
 *Function Name   : CreateObject
 *Description     : This function is used to create a new object of the class "TR069Agent".
 *@param [in]     : None
 ********************************************************************************************/

extern "C" platform_stub_hal* CreateObject(TcpSocketServer &ptrtcpServer)
{
        return new platform_stub_hal(ptrtcpServer);
}

/**************************************************************************************
 *Function Name : cleanup
 *Description   : This function will be used to the close things cleanly.
 *@param [in]   : szVersion - version, ptrAgentObj - Agent object
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
bool platform_stub_hal::cleanup(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "cleaning up\n");
        return TEST_SUCCESS;
}

/**************************************************************************
 *Function Name : DestroyObject
 *Description   : This function will be used to destory the TR069Agent object.
 *@param [in]   : Input argument is TR069Agent Object
 **************************************************************************/
extern "C" void DestroyObject(platform_stub_hal *stubobj)
{
	DEBUG_PRINT(DEBUG_TRACE, "Destroying HAL object\n");
	delete stubobj;
}
