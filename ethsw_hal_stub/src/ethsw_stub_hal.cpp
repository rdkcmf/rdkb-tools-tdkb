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
#include "ethsw_stub_hal.h"

#define WAIT_TIME 5
#define MAX_BUFFER_SIZE 128
#define MAX_STRING_SIZE 64
#define MAX_BUFFER_SIZE_TO_SEND 512
#define MAXBITRATE_10    10
#define MAXBITRATE_100   100
#define MAXBITRATE_1000  1000
#define MAXBITRATE_10000 10000
#define RETURN_SUCCESS 0
#define RETURN_FAILURE 1
#define TEST_SUCCESS true
#define TEST_FAILURE false

#define CHECK_PARAM_AND_RET(x) if ((x) == NULL) \
{ \
      DEBUG_PRINT(DEBUG_ERROR,"!!!NULL Pointer!!! :: %s:%d\n", __func__, __LINE__); \
      return TEST_FAILURE; \
}

/********************************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for registering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return string "SUCCESS" in case of success else return string "FAILURE"
 **********************************************************************************************/
std::string ethsw_stub_hal::testmodulepre_requisites()
{
	/*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
	return "SUCCESS";

}

/**********************************************************************************************
 *Function name : testmodulepost_requisites
 *Description   : testmodulepost_requisites will be used for unregistering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE based on the return value
 **********************************************************************************************/
bool ethsw_stub_hal::testmodulepost_requisites()
{
	/*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
	return TEST_SUCCESS;
}

/***************************************************************************************
 *Function name : ethsw_stub_hal_Init
 *Description   : This function is used to register all the ethsw_stub_hal methods.
 *param [in]    : szVersion - version, ptrAgentObj - Agent obhect
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE
 ***************************************************************************************/
bool ethsw_stub_hal::initialize(IN const char* szVersion)
{
	DEBUG_PRINT(DEBUG_TRACE, "ethsw_stub_hal Initialize----->Entry\n");
	return TEST_SUCCESS;
}

/*****************************************************************************************************
 *Function name : ethsw_stub_hal_Get_Port_Admin_Status
 *Description   : This function will invoke the SSP  HAL wrapper to get the ethsw port admin status
 *@param [in]   : req - It will give port id (port number) and flag(for negative scenario)
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *******************************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_Get_Port_Admin_Status(IN const Json::Value& req, OUT Json::Value& response)
{
	int portID = 0;
	char getAdminStatus[MAX_STRING_SIZE] = {0};
	int isNegativeScenario = 0;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_Get_Port_Admin_Status stub\n");
	if(&req["PortID"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	portID = req["PortID"].asInt();

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(ssp_ethsw_stub_hal_GetAdminPortStatus(portID, getAdminStatus, isNegativeScenario) == RETURN_SUCCESS)
	{
		DEBUG_PRINT(DEBUG_TRACE, "Successfully retrieved the admin status\n");
		response["result"] = "SUCCESS";
		response["details"] = getAdminStatus;
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "ethsw_stub_hal_Get_Port_Admin_Status function has failed.Please check logs";
		return;
	}
}


/*********************************************************************************************
 *Function name : ethsw_stub_hal_Get_Port_Cfg
 *Description   : This function will invoke the SSP  HAL wrapper to get the ethsw port cfg
 *@param [in]   : req - It will give port id (port number) and flag(for negative scenario)
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_Get_Port_Cfg(IN const Json::Value& req, OUT Json::Value& response)
{
	int portID = 0;
	char duplexMode[MAX_STRING_SIZE] = {0};
	int maxBitRate = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int  isNegativeScenario = 0;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_Get_Port_Cfg stub \n");
	if(&req["PortID"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	portID = req["PortID"].asInt();
	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(ssp_ethsw_stub_hal_GetPortCfg(portID, duplexMode, &maxBitRate, isNegativeScenario) == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "/%d/%s/", maxBitRate, duplexMode);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "ethsw_stub_hal_Get_Port_Cfg function has failed.Please check logs";
		return;
	}
}

/*********************************************************************************************
 *Function name : ethsw_stub_hal_Get_Port_Status
 *Description   : This function will invoke the SSP  HAL wrapper to get the ethsw port status
 *@param [in]   : req - It will give port id (port number) and flag(for negative scenario)
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_Get_Port_Status(IN const Json::Value& req, OUT Json::Value& response)
{
	int portID = 0;
	char linkStatus[MAX_STRING_SIZE] = {0};
	int bitRate = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int isNegativeScenario = 0;
        char duplexMode[MAX_STRING_SIZE] = {0};

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_Get_Port_Status stub \n");

	if(&req["PortID"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	portID = req["PortID"].asInt();

	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(ssp_ethsw_stub_hal_GetPort_Status(portID, linkStatus, &bitRate, duplexMode, isNegativeScenario) == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "/%d/%s/%s/", bitRate, linkStatus, duplexMode);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "ethsw_stub_hal_Get_Port_Status function has failed.Please check logs";
		return;
	}
}

/********************************************************************************************************
 *Function name : ethsw_stub_hal_Init
 *Description   : This function will invoke the SSP  HAL wrapper to intialize the ethsw_stub_hal HAL
 *@param [in]   : req - request sent by Test Manager
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_Init(IN const Json::Value& req, OUT Json::Value& response)
{
	DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_Init stub\n");
	if(ssp_ethsw_stub_hal_Init() == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = "ethsw_stub_hal_Init function has been intailized successfully";
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "ethsw_stub_hal_Init function has failed.Please check logs";
		return;
	}
}


/****************************************************************************************************************
 *Function name : ethsw_stub_hal_LocatePort_By_MacAddress
 *Description   : This function will invoke the SSP  HAL wrapper to Locate Port By MacAddress
 *@param [in]   : req - It will give MAC Address(MAC of associated device) and flag(for negative scenario)
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ****************************************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_LocatePort_By_MacAddress(IN const Json::Value& req, OUT Json::Value& response)
{
	char macID[MAX_STRING_SIZE] = {0};
	int portId = 0;
	char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
	int isNegativeScenario = 0;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_LocatePort_By_MacAddress stub\n");

	if(macID == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	strncpy(macID,req["macID"].asCString(), MAX_STRING_SIZE);
	if(&req["flag"])
	{
		isNegativeScenario = req["flag"].asInt();
	}

	if(ssp_ethsw_stub_hal_LocatePort_By_MacAddress(macID, &portId, isNegativeScenario) == RETURN_SUCCESS)
	{
		snprintf(resultDetails, MAX_BUFFER_SIZE_TO_SEND, "%d", portId);
		response["result"] = "SUCCESS";
		response["details"] = resultDetails;
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "ethsw_stub_hal_LocatePort_By_MacAddress function has failed.Please check logs";
		return;
	}
}

/***************************************************************************************
 *Function name : ethsw_stub_hal_SetAgingSpeed
 *Description   : This function will invoke the SSP  HAL wrapper to Set Aging Speed
 *@param [in]   : req - It will give port id and aging speed to be set
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_SetAgingSpeed(IN const Json::Value& req, OUT Json::Value& response)
{
	int portID = 0;
	int agingSpeed = 0;

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_SetAgingSpeed stub\n");

	if(&req["PortID"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	if(&req["AgingSpeed"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}

	portID = req["PortID"].asInt();
	agingSpeed = req["AgingSpeed"].asInt();

	DEBUG_PRINT(DEBUG_TRACE, "PortID = %d, AgingSpeed = %d\n", portID, agingSpeed);

	if(ssp_ethsw_stub_hal_SetAgingSpeed(portID, agingSpeed) == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = "ethsw_stub_hal_SetAgingSpeed function has passed";
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "ethsw_stub_hal_SetAgingSpeed function has failed.Please check logs";
		return;
	}
}

/******************************************************************************************
 *Function name : ethsw_stub_hal_SetPortAdminStatus
 *Description   : This function will invoke the SSP  HAL wrapper to Set Port Admin Status
 *@param [in]   : req - It will give port id and admin status to be set
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *******************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_SetPortAdminStatus(IN const Json::Value& req, OUT Json::Value& response)
{
	int portID = 0;
	char adminStatus[MAX_STRING_SIZE] = {0};

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_SetPortAdminStatus stub\n");

	if(&req["PortID"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}

	if(&req["adminstatus"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}

	portID = req["PortID"].asInt();
	strncpy(adminStatus, req["adminstatus"].asCString(), MAX_STRING_SIZE);

	if(ssp_ethsw_stub_hal_SetPortAdminStatus(portID, adminStatus) == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = "ethsw_stub_hal_SetPortAdminStatus function has been executed successfully";
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "ethsw_stub_hal_SetPortAdminStatus function has been failed";
		return;
	}
}

/******************************************************************************************
 *Function name : ethsw_stub_hal_SetPortCfg
 *Description   : This function will invoke the SSP  HAL wrapper to Set Port Cfg
 *@param [in]   : req - It will give port id, linkrate and duplex mode to be set
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ********************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_SetPortCfg(IN const Json::Value& req, OUT Json::Value& response)
{
	int portID = 0;
	int linkRate = 0;
	char duplexMode[MAX_STRING_SIZE] = {0};

	DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_SetPortCfg stub\n");

	if(&req["PortID"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	if(&req["linkrate"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}
	if(&req["mode"] == NULL)
	{
		response["result"] = "FAILURE";
		response["details"] = "NULL parameter as input argument";
		return;
	}

	portID = req["PortID"].asInt();
	linkRate = req["linkrate"].asInt();
	strncpy(duplexMode, req["mode"].asCString(), MAX_STRING_SIZE);

	if(ssp_ethsw_stub_hal_SetPortCfg(portID, linkRate, duplexMode) == RETURN_SUCCESS)
	{
		response["result"] = "SUCCESS";
		response["details"] = "ethsw_stub_hal_SetPortCfg function has been executed successfully";
		return;
	}
	else
	{
		response["result"] = "FAILURE";
		response["details"] = "ethsw_stub_hal_SetPortCfg function has been failed";
		return;
	}
}

/*******************************************************************************************
 *
 * Function Name        : ethsw_stub_hal_Get_AssociatedDevice
 * Description          :This function will invoke the SSP  HAL wrapper to get the ethsw assocoated device
 *
 * @param [in] req-    :
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_Get_AssociatedDevice(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_Get_AssociatedDevice stub\n");
    int isNegativeScenario = 0;
    char details[120] = {'\0'};
    eth_device_t eth_device_conf;
    unsigned long int array_size = 0;

    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }

    if(ssp_ethsw_stub_hal_Get_AssociatedDevice(&array_size,&eth_device_conf,isNegativeScenario) == RETURN_SUCCESS)
        {
                sprintf(details, "port: %d, mac address : %s, status: %d, lanid: %d, devTxRate: %d, devRxRate: %d",eth_device_conf.eth_port,eth_device_conf.eth_devMacAddress,eth_device_conf.eth_Active,eth_device_conf.eth_vlanid,eth_device_conf.eth_devTxRate,eth_device_conf.eth_devRxRate);
                DEBUG_PRINT(DEBUG_TRACE, "Successfully retrieved the associated device status status\n");
                response["result"] = "SUCCESS";
                response["details"] = details;
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "ethsw_stub_hal_Get_AssociatedDevice function has failed.Please check logs";
                return;
        }
}


/*********************************************************************************************
 *Function name : ethsw_stub_hal_Get_EthWanInterfaceName
 *Description   : This function will invoke the SSP  HAL wrapper to get the ethwan interface name
 *@param [in]   : req - flag(for negative scenario)
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_Get_EthWanInterfaceName(IN const Json::Value& req, OUT Json::Value& response)
{
        char interface[MAX_STRING_SIZE] = {0};
        char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
        int isNegativeScenario = 0;

        DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_Get_EthWanInterfaceName stub \n");

        if(&req["flag"])
        {
                isNegativeScenario = req["flag"].asInt();
        }

        if(ssp_ethsw_stub_hal_Get_EthWanInterfaceName(interface, isNegativeScenario) == RETURN_SUCCESS)
        {
                sprintf(resultDetails, "%s", interface);
                response["result"] = "SUCCESS";
                response["details"] = resultDetails;
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "ethsw_stub_hal_Get_EthWanInterfaceName function has failed.Please check logs";
                return;
        }
}


/*********************************************************************************************
 *Function name : ethsw_stub_hal_Get_EthWanEnable
 *Description   : This function will invoke the SSP  HAL wrapper to get the ethwan enable status
 *@param [in]   : req - flag(for negative scenario)
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_Get_EthWanEnable(IN const Json::Value& req, OUT Json::Value& response)
{
        unsigned char enableState = 0;
        char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
        int isNegativeScenario = 0;

        DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_Get_EthWanEnable stub \n");

        if(&req["flag"])
        {
                isNegativeScenario = req["flag"].asInt();
        }

        if(ssp_ethsw_stub_hal_Get_EthWanEnable(&enableState, isNegativeScenario) == RETURN_SUCCESS)
        {
                sprintf(resultDetails, "%d", enableState);
                response["result"] = "SUCCESS";
                response["details"] = resultDetails;
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "ethsw_stub_hal_Get_EthWanEnable function has failed.Please check logs";
                return;
        }
}


/***************************************************************************************
 *Function name : ethsw_stub_hal_Set_EthWanEnable
 *Description   : This function will invoke the SSP HAL wrapper to Set EthWanEnable state
 *@param [in]   : req - It will give the eth wan enable state to be set
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_Set_EthWanEnable(IN const Json::Value& req, OUT Json::Value& response)
{
        unsigned char enableState = 0;

        DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_Set_EthWanEnable stub\n");

        if(&req["enable"] == NULL)
        {
                response["result"] = "FAILURE";
                response["details"] = "NULL parameter as input argument";
                return;
        }

        enableState = req["enable"].asInt();

        DEBUG_PRINT(DEBUG_TRACE, "enableState = %d\n", enableState);

        if(ssp_ethsw_stub_hal_Set_EthWanEnable(enableState) == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                response["details"] = "ethsw_stub_hal_Set_EthWanEnable function has passed";
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "ethsw_stub_hal_Set_EthWanEnable function has failed.Please check logs";
                return;
        }
}


/*********************************************************************************************
 *Function name : ethsw_stub_hal_Get_EthWanPort
 *Description   : This function will invoke the SSP  HAL wrapper to get the ethwan port number
 *@param [in]   : req - flag(for negative scenario)
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_Get_EthWanPort(IN const Json::Value& req, OUT Json::Value& response)
{
        unsigned int portNum = 0;
        char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};
        int isNegativeScenario = 0;

        DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_Get_EthWanPort stub \n");

        if(&req["flag"])
        {
                isNegativeScenario = req["flag"].asInt();
        }

        if(ssp_ethsw_stub_hal_Get_EthWanPort(&portNum, isNegativeScenario) == RETURN_SUCCESS)
        {
                sprintf(resultDetails, "%u", portNum);
                response["result"] = "SUCCESS";
                response["details"] = resultDetails;
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "ethsw_stub_hal_Get_EthWanPort function has failed.Please check logs";
                return;
        }
}


/***************************************************************************************
 *Function name : ethsw_stub_hal_Set_EthWanPort
 *Description   : This function will invoke the SSP HAL wrapper to Set EthWanPort number
 *@param [in]   : req - It will give the eth wan port number to be set
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ******************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_Set_EthWanPort(IN const Json::Value& req, OUT Json::Value& response)
{
        unsigned int portNum = 0;

        DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_Set_EthWanPort stub\n");

        if(&req["port"] == NULL)
        {
                response["result"] = "FAILURE";
                response["details"] = "NULL parameter as input argument";
                return;
        }

        portNum = req["port"].asInt();

        DEBUG_PRINT(DEBUG_TRACE, "portNum = %d\n", portNum);

        if(ssp_ethsw_stub_hal_Set_EthWanPort(portNum) == RETURN_SUCCESS)
        {
                response["result"] = "SUCCESS";
                response["details"] = "ethsw_stub_hal_Set_EthWanPort function has passed";
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "ethsw_stub_hal_Set_EthWanPort function has failed.Please check logs";
                return;
        }
}


/*********************************************************************************************
 *Function name : ethsw_stub_hal_Get_EthWanLinkStatus
 *Description   : This function will invoke the SSP  HAL wrapper to get the ethwan link status
 *@param [in]   :
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 ************************************************************************************************/
void ethsw_stub_hal::ethsw_stub_hal_Get_EthWanLinkStatus(IN const Json::Value& req, OUT Json::Value& response)
{
        int linkStatus = 0;
        char resultDetails[MAX_BUFFER_SIZE_TO_SEND] = {0};

        DEBUG_PRINT(DEBUG_TRACE,"Inside Function ethsw_stub_hal_Get_EthLinkStatus stub \n");

        if(ssp_ethsw_stub_hal_Get_EthWanLinkStatus(&linkStatus) == RETURN_SUCCESS)
        {
                sprintf(resultDetails, "%d", linkStatus);
                response["result"] = "SUCCESS";
                response["details"] = resultDetails;
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "ethsw_stub_hal_Get_EthWanLinkStatus function has failed.Please check logs";
                return;
        }
}

/***************************************************************************************************
 *Function Name   : CreateObject
 *Description     : This function is used to create a new object of the class "ethsw_stub_hal".
 *@param [in]     : None
 ***************************************************************************************************/
extern "C" ethsw_stub_hal* CreateObject(TcpSocketServer &ptrtcpServer)
{
	return new ethsw_stub_hal(ptrtcpServer);
}

/*************************************************************************************
 *Function Name : cleanup
 *Description   : This function will be used to the close things cleanly.
 *@param [in]   : szVersion - version, ptrAgentObj - Agent object
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
bool ethsw_stub_hal::cleanup(IN const char* szVersion)
{
	DEBUG_PRINT(DEBUG_TRACE, "cleaning up\n");
	return TEST_SUCCESS;
}

/**********************************************************************************
 *Function Name : DestroyObject
 *Description   : This function will be used to destroy the ethsw_stub_hal object.
 *@param [in]   : Input argument is ethsw_stub_hal Object
 **********************************************************************************/
extern "C" void DestroyObject(ethsw_stub_hal *stubobj)
{
	DEBUG_PRINT(DEBUG_TRACE, "Destroying ethsw_stub_hal object\n");
	delete stubobj;
}
