/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2021 RDK Management
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

#include "FWUpgradeHAL_Stub.h"

/***************************************************************************
 *Function name : initialize
 *Description   : Initialize Function will be used for registering the wrapper method
 *                        with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/
bool FWUPGRADEHAL::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE, "FWUPGRADEHAL Initialize----->Entry\n");
    return TEST_SUCCESS;
}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string FWUPGRADEHAL::testmodulepre_requisites()
{

    /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
    return "SUCCESS";
}

/***************************************************************************
 *Function name : testmodulepost_requisites
 *Description   : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/
bool FWUPGRADEHAL::testmodulepost_requisites()
{
    /*Dummy function required as it is pure virtual. No need to register with CCSP bus for HAL*/
    return TEST_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name    : FWUPGRADEHAL_GetParamUlongValue
 * Description      : This will get the Ulong values
 * @param [in]  req - paramName : Holds the name of api
 *  		      paramType  : Holds NULL in the case of negative scenario and empty otherwise
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void FWUPGRADEHAL::FWUPGRADEHAL_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_GetParamUlongValue  --->Entry \n");
    int returnValue = 0;
    char paramName[100];
    char Details[64] = {'\0'};
    unsigned long value = 0;
    char paramType[10] = {'\0'};

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(paramName,req["paramName"].asCString());
    strcpy(paramType, req["paramType"].asCString());

    //For negative scenario, "NULL" will be passed as the paramType argument
    if(strcmp(paramType, "NULL"))
    {
        returnValue = ssp_FWUPGRADEHAL_GetParamUlongValue(paramName,&value);
    }
    else
    {
        returnValue = ssp_FWUPGRADEHAL_GetParamUlongValue(paramName,NULL);
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
        DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_GetParamUlongValue failed--->Exit\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_GetParamUlongValue --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : FWUPGRADEHAL_Set_Download_Interface
 * Description          : This function will invoke the SSP  HAL wrapper to set the Download_Interface
 *
 * @param [in] req-     : interface - The value of download interface
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void FWUPGRADEHAL::FWUPGRADEHAL_Set_Download_Interface(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Set_Download_Interface --->Entry \n");
    int returnValue = 0;
    unsigned int interface =0;
    char Details[64] = {'\0'};

    /* Validate the input arguments */
    if(&req["interface"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    interface =req["interface"].asInt();
    returnValue = ssp_FWUPGRADEHAL_Set_Download_Interface(interface);

    if(0 == returnValue)
    {
        sprintf(Details,"FWUPGRADEHAL_Set_Download_Interface set interface successfully");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set download interface";
        DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Set_Download_Interface failed--->Exit\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Set_Download_Interface --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : FWUPGRADEHAL_Download
 * Description          :This function will invoke the SSP  HAL wrapper to Download
 *
 * @param [in] req-     : None
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void FWUPGRADEHAL::FWUPGRADEHAL_Download(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_HTTP_Download --->Entry \n");
    int returnValue = 0;
    char Details[64] = {'\0'};
    returnValue = ssp_FWUPGRADEHAL_Download();

    if(0 == returnValue)
    {
        sprintf(Details,"FWUPGRADEHAL_Download: success");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to download ";
        DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Download failed--->Exit\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Download --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : FWUPGRADEHAL_Reboot_Now
 * Description          :This function will invoke the SSP  HAL wrapper to Reboot
 *
 * @param [in] req-     : None
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void FWUPGRADEHAL::FWUPGRADEHAL_Reboot_Now(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Reboot_Now --->Entry \n");
    int returnValue = 0;
    char Details[64] = {'\0'};
    returnValue = ssp_FWUPGRADEHAL_Reboot_Now();

    if(0 == returnValue)
    {
        sprintf(Details,"FWUPGRADEHAL_Reboot_Now: success");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to reboot ";
        DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Reboot_Now failed--->Exit\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Reboot_Now --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : FWUPGRADEHAL_Get_Download_Url
 * Description      : This will get the Download_Url and filename
 *
 * @param [in]      : URL : To save the URL
 *                  : filename : To save the filename
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void FWUPGRADEHAL::FWUPGRADEHAL_Get_Download_Url(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_HTTP_Download_Url  --->Entry \n");
    int returnValue = 0;
    char URL[200]={'\0'};
    char Details[800] = {'\0'};
    char filename[200]= {'\0'};
    char paramType[10] = {'\0'};
    strcpy(paramType, req["paramType"].asCString());

    if(strcmp(paramType, "NULL"))
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Executing Positive Sceanrio\n");
        returnValue = ssp_FWUPGRADEHAL_Get_Download_Url(URL,filename);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Executing Negative Scenario\n");
        returnValue = ssp_FWUPGRADEHAL_Get_Download_Url(NULL,NULL);
    }

    if(0 == returnValue)
    {
        sprintf(Details,"url is %s, filename is %s",URL,filename);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value of URL and file";
        DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Get_Download_Url failed--->Exit\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Get_Download_Url --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : FWUPGRADEHAL_Set_Download_Url
 * Description          : This function will invoke the SSP  HAL wrapper to set the Download_Url
 *
 * @param [in] req-     : URL : The URL of the site from which the file is to be downloaded
 *                        filename : The name of the file to be downloaded
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void FWUPGRADEHAL::FWUPGRADEHAL_Set_Download_Url(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Set_Download_Url --->Entry \n");
    int returnValue = 0;
    char URL[60] = {'\0'};
    char filename[60] = {'\0'};
    char Details[64] = {'\0'};

    /* Validate the input arguments */
    if((&req["URL"]==NULL) || (&req["filename"]==NULL))
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(URL,req["URL"].asCString());
    strcpy(filename,req["filename"].asCString());
    returnValue = ssp_FWUPGRADEHAL_Set_Download_Url(URL,filename);

    if(0 == returnValue)
    {
        sprintf(Details,"FWUPGRADEHAL_Set_Download_Url:set function success");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set Download_Url";
        DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Set_Download_Url failed--->Exit\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Set_Download_Url --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : FWUPGRADEHAL_Update_And_FactoryReset
 * Description          : This function will invoke the SSP  HAL wrapper to UpdateAndFactoryReset
 *
 * @param [in] req-     : URL - Image URL
                        : imageName - Name of the image
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void FWUPGRADEHAL::FWUPGRADEHAL_Update_And_FactoryReset(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Update_And_FactoryReset --->Entry \n");
    int returnValue = 0;
    char Details[64] = {'\0'};
    char url[1024] = {'\0'};
    char imagename[1024] = {'\0'};

    if((&req["URL"]==NULL) || (&req["imageName"]==NULL))
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(url, req["URL"].asCString());
    strcpy(imagename, req["imageName"].asCString());
    returnValue = ssp_FWUPGRADEHAL_UpdateAndFactoryReset(url,imagename);

    if(0 == returnValue)
    {
        sprintf(Details,"FWUPGRADEHAL_Update_And_FactoryReset: success");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to UpdateAndFactoryReset ";
        DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Update_And_FactoryReset failed--->Exit\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n FWUPGRADEHAL_Update_And_FactoryReset --->Exit\n");
    return;
}

/**************************************************************************
 * Function Name        : CreateObject
 * Description  : This function will be used to create a new object for the
 *                      class "FWUPGRADEHAL".
 *
 **************************************************************************/
extern "C" FWUPGRADEHAL* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new FWUPGRADEHAL(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/
bool FWUPGRADEHAL::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"FWUPGRADEHAL shutting down\n");
    return TEST_SUCCESS;
}

/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object
 *
 **************************************************************************/
extern "C" void DestroyObject(FWUPGRADEHAL *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying FWUPGRADEHAL object\n");
    delete stubobj;
}

