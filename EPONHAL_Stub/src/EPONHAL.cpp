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

#include "EPONHAL.h"

/********************************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for registering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return string "SUCCESS" in case of success else return string "FAILURE"
 **********************************************************************************************/
std::string EPONHAL::testmodulepre_requisites()
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
bool EPONHAL::testmodulepost_requisites()
{
        /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
        return TEST_SUCCESS;
}

/***************************************************************************************
 *Function name :  EPONHAL::initialize
 *Description   : This function is used to register all the epon_hal methods.
 *param [in]    : szVersion - version, ptrAgentObj - Agent obhect
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE
 ***************************************************************************************/
bool EPONHAL::initialize(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "EPONHAL Initialize----->Entry\n");
        return TEST_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name : EPONHAL_GetParamUlongValue
 * Description   : This will get the Ulong values
 * @param [in]   : req - paramName : Holds the name of api
 *                 req - paramType : NULL value indicates negative test
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
*
 *******************************************************************************************/
void EPONHAL::EPONHAL_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetParamUlongValue ---> Entry \n");
    int returnValue = 0;
    char paramName[100] = {'\0'};
    char Details[100] = {'\0'};
    unsigned long value = 0;
    char paramType[10] = {'\0'};


    /* Validate the input arguments */
    if(&req["paramName"]==NULL || &req["paramType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(paramName,req["paramName"].asCString());
    strcpy(paramType, req["paramType"].asCString());

    if(strcmp(paramType, "NULL"))
    {
        returnValue = ssp_EPONHAL_GetParamUlongValue(paramName,&value);
    }
    else
    {
        returnValue = ssp_EPONHAL_GetParamUlongValue(paramName,NULL);
    }

    if(0 == returnValue)
    {
        sprintf(Details,"%lu", value);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
        DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetParamUlongValue ---> Exit\n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n EPONHAL_GetParamUlongValue ---> Exit\n");
    return;
}

/***************************************************************************************************
 *Function Name   : CreateObject
 *Description     : This function is used to create a new object of the class "EPONHAL".
 *@param [in]     : None
 ***************************************************************************************************/
extern "C" EPONHAL* CreateObject(TcpSocketServer &ptrtcpServer)
{
        return new EPONHAL(ptrtcpServer);
}

/*************************************************************************************
 *Function Name : cleanup
 *Description   : This function will be used to the close things cleanly.
 *@param [in]   : szVersion - version, ptrAgentObj - Agent object
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
bool EPONHAL::cleanup(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "cleaning up\n");
        return TEST_SUCCESS;
}

/**********************************************************************************
 *Function Name : DestroyObject
 *Description   : This function will be used to destroy the EPONHAL object.
 *@param [in]   : Input argument is EPONHAL Object
 **********************************************************************************/
extern "C" void DestroyObject(EPONHAL *stubobj)
{
        DEBUG_PRINT(DEBUG_TRACE, "Destroying EPONHAL object\n");
        delete stubobj;
}
