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
#define MAX_PARAM_SIZE 1024
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
 * Function Name        : RBUS_CheckStatus
 * Description          : This function invokes RBUS api rbus_checkStatus()
 * @param [in] req-     : None
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void RBUS::RBUS_CheckStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_CheckStatus  --->Entry \n");

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
        response["details"]="RBUS_CheckStatus function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_CheckStatus --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : RBUS_Open
 * Description          : This function invokes RBUS api rbus_open()
 * @param [in] req-     : None
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void RBUS::RBUS_Open(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_Open  --->Entry \n");

    int returnValue = RETURN_FAILURE;

    returnValue = ssp_rbus_open();

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="RBUS_Open function was Successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_Open function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_Open --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : RBUS_Close
 * Description          : This function invokes RBUS api rbus_close()
 * @param [in] req-     : None
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 *******************************************************************************************/
void RBUS::RBUS_Close(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_Close  --->Entry \n");

    int returnValue = RETURN_FAILURE;

    returnValue = ssp_rbus_close();

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="RBUS_Close function was Successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_Close function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_Close --->Exit\n");
    return;
}

/*****************************************************************************************************************
 * Function Name : RBUS_DataElements
 * Description   : This function will invoke the wrapper function ssp_rbus_dataElements
 * @param [in]   : element1 - Data Element 1 (Parameter Name)
                 : element2 - Data Element 2 (Parameter Name)
                 : operation - To Specify Register / UnRegister
 * @param [out]  : Filled with SUCCESS or FAILURE based on the output status of operation
 **************************************************************************************************************/
void RBUS::RBUS_DataElements(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_DataElements  --->Entry \n");

    int returnValue = RETURN_FAILURE;
    char element1[MAX_PARAM_SIZE] = {'\0'};
    char element2[MAX_PARAM_SIZE] = {'\0'};
    char operation[MAX_PARAM_SIZE] = {'\0'};

    if((&req["element1"]==NULL) || (&req["element2"]==NULL) ||(&req["operation"]==NULL) )
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(element1, req["element1"].asCString());
    strcpy(element2, req["element2"].asCString());
    strcpy(operation, req["operation"].asCString());

    returnValue = ssp_rbus_dataElements(element1, element2,operation);

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="RBUS_DataElements function was Successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_DataElements function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_DataElements --->Exit\n");
    return;
}

/*****************************************************************************************************************
 * Function Name : RBUS_Session
 * Description   : This function will invoke the wrapper function ssp_rbus_session
 * @param [in]   : operation - To Specify Create / Get
 * @param [out]  : Filled with SUCCESS or FAILURE based on the output status of operation
 **************************************************************************************************************/
void RBUS::RBUS_Session(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_Session  --->Entry \n");

    int returnValue = RETURN_FAILURE;
    unsigned int sessionid = 0;
    char details[MAX_BUFFER_SIZE_TO_SEND] = {'\0'};
    char operation[MAX_PARAM_SIZE] = {'\0'};

    if(&req["operation"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(operation, req["operation"].asCString());
    returnValue = ssp_rbus_session(operation,&sessionid);

    if(returnValue == RETURN_SUCCESS)
    {
        sprintf(details, "%d", sessionid);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_Session function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_Session --->Exit\n");
    return;
}

/*****************************************************************************************************************
 * Function Name : RBUS_CloseSession
 * Description   : This function will invoke the wrapper function ssp_rbus_closeSession
 * @param [in]   : sessionid - Session ID value
 * @param [out]  : Filled with SUCCESS or FAILURE based on the output status of operation
 **************************************************************************************************************/
void RBUS::RBUS_CloseSession(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_CloseSession  --->Entry \n");

    int returnValue = RETURN_FAILURE;
    unsigned int sessionid = 0;

    if(&req["sessionid"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    sessionid = req["sessionid"].asUInt();

    returnValue = ssp_rbus_closeSession(sessionid);

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="RBUS_CloseSession function was successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_CloseSession function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_CloseSession --->Exit\n");
    return;
}

/*****************************************************************************************************************
 * Function Name : RBUS_DiscoverComponentDataElements
 * Description   : This function will invoke the wrapper function  ssp_rbus_discoverComponentDataElements
 * @param [in]   : componentName - Component Name to get the available Data Elements
 * @param [out]  : Filled with SUCCESS or FAILURE based on the output status of operation
 **************************************************************************************************************/
void RBUS::RBUS_DiscoverComponentDataElements(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_DiscoverComponentDataElements  --->Entry \n");

    int returnValue = RETURN_FAILURE;
    char component_name[MAX_PARAM_SIZE] = {'\0'};

    if(&req["componentName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(component_name, req["componentName"].asCString());

    returnValue = ssp_rbus_discoverComponentDataElements(component_name);

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="RBUS_DiscoverComponentDataElements function was Successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_DiscoverComponentDataElements function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_DiscoverComponentDataElements --->Exit\n");
    return;
}

/*****************************************************************************************************************
 * Function Name : RBUS_Get
 * Description   : This function will invokes the wrapper function ssp_rbus_get
 * @param [in]   : paramName - Parameter Name
 * @param [out]  : Filled with SUCCESS or FAILURE based on the output status of operation
 **************************************************************************************************************/
void RBUS::RBUS_Get(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_Get  --->Entry \n");

    int returnValue = RETURN_FAILURE;
    char paramname[1024] = "NULL";

    strcpy(paramname, req["paramName"].asCString());

    returnValue = ssp_rbus_get(paramname);

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="RBUS_Get function was Successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_Get function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_Get --->Exit\n");
    return;
}

/*****************************************************************************************************************
 * Function Name : RBUS_GetValue
 * Description   : This function will invokes the wrapper function ssp_rbus_getValue
 * @param [in]   : paramName - Parameter Name
                 : paramtype - Parameter Type
 * @param [out]  : Filled with SUCCESS or FAILURE based on the output status of operation
 **************************************************************************************************************/
void RBUS::RBUS_GetValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_GetValue  --->Entry \n");

    int returnValue = RETURN_FAILURE;
    char paramname[MAX_PARAM_SIZE] = {'\0'};
    char paramtype[MAX_PARAM_SIZE] = {'\0'};
    char details[MAX_BUFFER_SIZE_TO_SEND] = {'\0'};
    const char* getvalue = "";
    int* getvalue_i = 0;

    if((&req["paramName"]==NULL) || (&req["paramType"]==NULL))
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(paramname, req["paramName"].asCString());
    strcpy(paramtype, req["paramType"].asCString());

    returnValue = ssp_rbus_getValue(paramtype, paramname, &getvalue, &getvalue_i);

    if(returnValue == RETURN_SUCCESS)
    {
        if ((strcmp(paramtype,"String") == 0) || (strcmp(paramtype,"Boolean") == 0))
            sprintf(details, "%s", getvalue);
        else
            sprintf(details, "%d", getvalue_i);

        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_GetValue function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_GetValue --->Exit\n");
    return;
}

/*****************************************************************************************************************
 * Function Name : RBUS_SetValue
 * Description   : This function will invokes the wrapper function ssp_rbus_setValue
 * @param [in]   : paramName - Parameter Name
                 : paramtype - Parameter Type
 * @param [out]  : Filled with SUCCESS or FAILURE based on the output status of operation
 **************************************************************************************************************/
void RBUS::RBUS_SetValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_SetValue  --->Entry \n");

    int returnValue = RETURN_FAILURE;
    char paramname[MAX_PARAM_SIZE] = {'\0'};
    char paramtype[MAX_PARAM_SIZE] = {'\0'};
    char paramvalue[MAX_PARAM_SIZE] = {'\0'};

    if((&req["paramName"]==NULL) || (&req["paramType"]==NULL) ||(&req["paramValue"]==NULL) )
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(paramname, req["paramName"].asCString());
    strcpy(paramtype, req["paramType"].asCString());
    strcpy(paramvalue, req["paramValue"].asCString());

    returnValue = ssp_rbus_setValue(paramtype, paramname, paramvalue);

    if(returnValue == RETURN_SUCCESS)
    {
        response["result"]="SUCCESS";
        response["details"]="RBUS_SetValue function was Successful";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="RBUS_SetValue function has failed.Please check logs";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n RBUS_SetValue --->Exit\n");
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
