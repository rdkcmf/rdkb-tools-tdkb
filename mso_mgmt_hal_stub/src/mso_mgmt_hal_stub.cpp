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

#include "mso_mgmt_hal_stub.h"

/********************************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for registering TDK with the CR
 *@param [in]   : None
 *@param [out]  : Return string "SUCCESS" in case of success else return string "FAILURE"
 **********************************************************************************************/
std::string mso_mgmt_hal::testmodulepre_requisites()
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
bool mso_mgmt_hal::testmodulepost_requisites()
{
        /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
        return TEST_SUCCESS;
}

/***************************************************************************************
 *Function name :  mso_mgmt_hal::initialize
 *Description   : This function is used to register all the msomgmt_hal methods.
 *param [in]    : szVersion - version, ptrAgentObj - Agent obhect
 *@param [out]  : Return TEST_SUCCESS or TEST_FAILURE
 ***************************************************************************************/
bool mso_mgmt_hal::initialize(IN const char* szVersion)

{
        DEBUG_PRINT(DEBUG_TRACE, "mso_mgmt_hal Initialize----->Entry\n");
        return TEST_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name    : mso_mgmt_hal_GetMsoPodSeed
 * Description      : This will get the MSO POD Seed value
 *

 * @param [in]  req - paramType : Holds NULL in the case of negative scenario and empty otherwise
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void mso_mgmt_hal::mso_mgmt_hal_GetMsoPodSeed(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n mso_mgmt_hal_GetMsoPodSeed  --->Entry \n");

    int returnValue = 0;
    char Details[800] = {'\0'};
    char value[700] = {'\0'};
    char paramType[10] = {'\0'};
	
    strcpy(paramType, req["paramType"].asCString());

    //For negative scenario, "NULL" will be passed as the paramType argument
    if(strcmp(paramType, "NULL"))
        returnValue = ssp_mso_mgmt_hal_GetMsoPodSeed(value);
    else
       returnValue = ssp_mso_mgmt_hal_GetMsoPodSeed(NULL);
    if(0 == returnValue)
    {
       sprintf(Details,"%s", value);
       DEBUG_PRINT(DEBUG_TRACE,"\n MSOPODSeed: %s\n",value);
       response["result"]="SUCCESS";
       response["details"]=Details;
    }
    else
    {
       response["result"]="FAILURE";
       DEBUG_PRINT(DEBUG_TRACE,"\n MSOPODSeed: %s\n",value);
       response["details"]="Failed to get the value";
       DEBUG_PRINT(DEBUG_TRACE,"\n mso_mgmt_hal_GetMsoPodSeed --->Exit\n");
       return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n mso_mgmt_hal_GetMsoPodSeed --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : mso_mgmt_hal_SetPodSeed
 * Description      : This will set the MSO POD Seed value
 *

 * @param [in]  req - paramValue : Value of Pod seed to be set
                      paramType : Holds NULL in the case of negative scenario and empty otherwise
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void mso_mgmt_hal::mso_mgmt_hal_SetMsoPodSeed(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n mso_set_pod_seed  --->Entry \n");

    int returnValue = 0;
    char paramValue[10] = {'\0'};
    char paramType[10] = {'\0'};

    /* Validate the input arguments */
    strcpy(paramType, req["paramType"].asCString());
    strcpy(paramValue, req["paramValue"].asCString());

    //For negative scenario, "NULL" will be passed as the paramType argument
    if(strcmp(paramType, "NULL"))
       returnValue = ssp_mso_mgmt_hal_SetMsoPodSeed(paramValue);
    else
       returnValue = ssp_mso_mgmt_hal_SetMsoPodSeed(NULL);
    if(0 == returnValue)
    {
       DEBUG_PRINT(DEBUG_TRACE,"Mso POD Seed set Validation successful");
       response["result"]="SUCCESS";
       response["details"]="Mso POD Seed set Validation successful";
    }
    else
    {
       response["result"]="FAILURE";
       response["details"]="Failed to validate the POD seed";
       DEBUG_PRINT(DEBUG_TRACE,"MSO POD seed validation failed");
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n mso_set_pod_seed --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : mso_mgmt_hal_MsoValidatePwd
 * Description      : This will validate the password
 *

 * @param [in]  req - paramValue: Holds the password 
                      paramType : Holds NULL in the case of negative scenario and empty otherwise
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void mso_mgmt_hal::mso_mgmt_hal_MsoValidatePwd(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n mso_mgmt_hal_MsoValidatePwd  --->Entry \n");

    int returnValue = 0;
    char Details[100] = {'\0'};
    char paramValue[10] = {'\0'};
    char paramType[10] = {'\0'};
    char output[20] = {'\0'};

    /* Validate the input arguments */
    strcpy(paramType, req["paramType"].asCString());
    strcpy(paramValue, req["paramValue"].asCString());


    //For negative scenario, "NULL" will be passed as the paramType argument
    if(strcmp(paramType, "NULL"))
        returnValue = ssp_mso_mgmt_hal_MsoValidatePwd(paramValue,output);
    else
       returnValue = ssp_mso_mgmt_hal_MsoValidatePwd(NULL,output);
    if(0 == returnValue)
    {
       sprintf(Details,"%s", output);
       DEBUG_PRINT(DEBUG_TRACE,"MSO Password validation value is %s\n",output);
       response["result"]="SUCCESS";
       response["details"]=Details;
    }
    else
    {
       response["result"]="FAILURE";
       response["details"]="Failed to validate the password";
       DEBUG_PRINT(DEBUG_TRACE,"MSO Password validation value is %s\n",output);      
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n mso_mgmt_hal_MsoValidatePwd --->Exit\n");
    return;

}

/***************************************************************************************************
 *Function Name   : CreateObject
 *Description     : This function is used to create a new object of the class "msomgmthal".
 *@param [in]     : None
 ***************************************************************************************************/
extern "C" mso_mgmt_hal* CreateObject(TcpSocketServer &ptrtcpServer)
{
        return new mso_mgmt_hal(ptrtcpServer);
}

/*************************************************************************************
 *Function Name : cleanup
 *Description   : This function will be used to the close things cleanly.
 *@param [in]   : szVersion - version, ptrAgentObj - Agent object
 *@param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 **************************************************************************************/
bool mso_mgmt_hal::cleanup(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "cleaning up\n");
        return TEST_SUCCESS;
}

/**********************************************************************************
 *Function Name : DestroyObject
 *Description   : This function will be used to destroy the mso_mgmt_hal object.
 *@param [in]   : Input argument is mso_mgmt_hal Object
 **********************************************************************************/
extern "C" void DestroyObject(mso_mgmt_hal *stubobj)
{
        DEBUG_PRINT(DEBUG_TRACE, "Destroying mso_mgmt_hal object\n");
        delete stubobj;
}



