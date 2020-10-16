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

#include "RBUS_Stub.h"
#define MAX_BUFFER_SIZE_TO_SEND 500
#define RETURN_SUCCESS 0
#define RETURN_FAILURE 1
/********************************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for registering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return string "SUCCESS" in case of success else return string "FAILURE"
 **********************************************************************************************/
std::string RBUS::testmodulepre_requisites()
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
bool RBUS::testmodulepost_requisites()
{
        /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
        return TEST_SUCCESS;
}

/***************************************************************************************
 *Function name :  RBUS::initialize
 *Description   : This function is used to register all the ble_hal methods.
 *param [in]    : szVersion - version, ptrAgentObj - Agent obhect
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE
 ***************************************************************************************/
bool RBUS::initialize(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "RBUS Initialize----->Entry\n");
        return TEST_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : RBUS_checkStatus
 * Description          : This function invokes RBUS api rbus_checkStatus()
 * @param [in] req-     : None
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void RBUS::RBUS_checkStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_checkStatus  --->Entry \n");

    int returnValue = RETURN_FAILURE;
    char details[MAX_BUFFER_SIZE_TO_SEND] = {'\0'};
    rbusStatus_t status = RBUS_DISABLED;

    returnValue = ssp_rbus_checkStatus(&status);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "%d", status);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_checkStatus function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_checkStatus --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : RBUS_open
 * Description          : This function invokes RBUS api rbus_open()
 * @param [in] req-     : None
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void RBUS::RBUS_open(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_open  --->Entry \n");

    int returnValue = RETURN_FAILURE;

    returnValue = ssp_rbus_open();

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="RBUS_open function was Successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_open function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_open --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : RBUS_close
 * Description          : This function invokes RBUS api rbus_close()
 * @param [in] req-     : None
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void RBUS::RBUS_close(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_close  --->Entry \n");

    int returnValue = RETURN_FAILURE;

    returnValue = ssp_rbus_close();

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="RBUS_close function was Successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_close function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_close --->Exit\n");
    return;
}

/***************************************************************************************************
 *Function Name   : CreateObject
 *Description     : This function is used to create a new object of the class "RBUS".
 *@param [in]     : None
 ***************************************************************************************************/
extern "C" RBUS* CreateObject(TcpSocketServer &ptrtcpServer)
{
        return new RBUS(ptrtcpServer);
}

/*************************************************************************************
 *Function Name : cleanup
 *Description   : This function will be used to the close things cleanly.
 *@param [in]   : szVersion - version, ptrAgentObj - Agent object
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
bool RBUS::cleanup(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "cleaning up\n");
        return TEST_SUCCESS;
}

/**********************************************************************************
 *Function Name : DestroyObject
 *Description   : This function will be used to destroy the RBUS object.
 *@param [in]   : Input argument is RBUS Object
 **********************************************************************************/
extern "C" void DestroyObject(RBUS *stubobj)
{
        DEBUG_PRINT(DEBUG_TRACE, "Destroying RBUS object\n");
        delete stubobj;
}
