/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2020 RDK Management
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

#include "BLEHAL.h"
#define MAX_BUFFER_SIZE_TO_SEND 500
#define RETURN_SUCCESS 0
#define RETURN_FAILURE 1
/********************************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for registering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return string "SUCCESS" in case of success else return string "FAILURE"
 **********************************************************************************************/
std::string BLEHAL::testmodulepre_requisites()
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
bool BLEHAL::testmodulepost_requisites()
{
        /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
        return TEST_SUCCESS;
}

/***************************************************************************************
 *Function name :  BLEHAL::initialize
 *Description   : This function is used to register all the ble_hal methods.
 *param [in]    : szVersion - version, ptrAgentObj - Agent obhect
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE
 ***************************************************************************************/
bool BLEHAL::initialize(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "BLEHAL Initialize----->Entry\n");
        return TEST_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : BLEHAL_GetStatus
 * Description          : This function invokes BLE  hal api ble_GetStatus()
 * @param [in] req-     : req - flag(for negative scenario)
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void BLEHAL::BLEHAL_GetStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n BLEHAL_GetStatus----->Entry\n");
    int returnValue = RETURN_FAILURE;
    char details[MAX_BUFFER_SIZE_TO_SEND] = {'\0'};
    BLE_Status_e status = BLE_DISABLE;
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }
    returnValue = ssp_BLEHAL_GetStatus(&status, isNegativeScenario);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "%d", status);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="BLEHAL_GetStatus function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n BLEHAL_GetStatus --->Exit\n");
    return;
}


/*******************************************************************************************
 *
* Function Name        : BLEHAL_Enable
 * Description          : This function invokes BLE  hal api ble_Enable()
 * @param [in] req-     : req - It will give the ble enable state to be set
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void BLEHAL::BLEHAL_Enable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n BLEHAL_Enable----->Entry\n");
    int returnValue = RETURN_FAILURE;
    BLE_Status_e status = BLE_DISABLE;

    if(&req["enable"] == NULL)
    {
            response["result"] = "FAILURE";
            response["details"] = "NULL parameter as input argument";
            return;
    }
    status = (BLE_Status_e)(req["enable"].asInt());

    DEBUG_PRINT(DEBUG_TRACE, "enableState = %d\n", status);
    returnValue = ssp_BLEHAL_Enable(status);
    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="BLEHAL_Enable function has passed";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="BLEHAL_Enable function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n BLEHAL_Enable --->Exit\n");
    return;
}


/***************************************************************************************************
 *Function Name   : CreateObject
 *Description     : This function is used to create a new object of the class "BLEHAL".
 *@param [in]     : None
 ***************************************************************************************************/
extern "C" BLEHAL* CreateObject(TcpSocketServer &ptrtcpServer)
{
        return new BLEHAL(ptrtcpServer);
}

/*************************************************************************************
 *Function Name : cleanup
 *Description   : This function will be used to the close things cleanly.
 *@param [in]   : szVersion - version, ptrAgentObj - Agent object
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
bool BLEHAL::cleanup(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "cleaning up\n");
        return TEST_SUCCESS;
}

/**********************************************************************************
 *Function Name : DestroyObject
 *Description   : This function will be used to destroy the BLEHAL object.
 *@param [in]   : Input argument is BLEHAL Object
 **********************************************************************************/
extern "C" void DestroyObject(BLEHAL *stubobj)
{
        DEBUG_PRINT(DEBUG_TRACE, "Destroying BLEHAL object\n");
        delete stubobj;
}
