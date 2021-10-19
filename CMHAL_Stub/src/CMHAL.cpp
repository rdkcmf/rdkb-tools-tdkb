/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2016 RDK Management
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

#include "CMHAL.h"

/***************************************************************************
 *Function name : initialize
 *Description   : Initialize Function will be used for registering the wrapper method
 *                        with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/

bool CMHAL::initialize(IN const char* szVersion)
{
    return TEST_SUCCESS;
}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string CMHAL::testmodulepre_requisites()
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_testmodulepre_requisites  --->Entry \n");

    DEBUG_PRINT(DEBUG_TRACE,"\n Initialising DB \n");
    int DBInitStatus = ssp_CMHAL_Init((char *)"InitDB");

    DEBUG_PRINT(DEBUG_TRACE,"\n Initialising DS \n");
    int DSInitStatus = ssp_CMHAL_Init((char *)"InitDS");

    DEBUG_PRINT(DEBUG_TRACE,"\n Initialising DB \n");
    int USInitStatus = ssp_CMHAL_Init((char *)"InitUS");

    if(DBInitStatus == 0 && DSInitStatus ==0 && USInitStatus==0)
    {
       DEBUG_PRINT(DEBUG_TRACE,"\n Initialised CMHAL ---> Exit\n");
        return "SUCCESS";
    }
    else
    {
       DEBUG_PRINT(DEBUG_TRACE,"\n Failed to initialise CMHAL --->Exit \n");
       return "FAILURE"; 
    }
}


/***************************************************************************
 *Function name : testmodulepost_requisites
 *Description   : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/
bool CMHAL::testmodulepost_requisites()
{
    DEBUG_PRINT(DEBUG_LOG,"DBG:CMHAL:testmodulepost_requisites() \n");
    return 0;
}


/*******************************************************************************************
 *
 * Function Name    : CMHAL_GetParamCharValue
 * Description      : This will get the char values
 *

 * @param [in]  req - paramName : Holds the name of api
                      paramType : Holds NULL in the case of negative scenario and empty otherwise
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CMHAL::CMHAL_GetParamCharValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetParamCharValue  --->Entry \n");

    int returnValue = 0;
    char paramName[100];
    char Details[800] = {'\0'};
    char value[700];
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
        returnValue = ssp_CMHAL_GetParamCharValue(paramName,value);
    else
       returnValue = ssp_CMHAL_GetParamCharValue(paramName,NULL);
    if(0 == returnValue)
    {
       sprintf(Details,"%s", value);
       response["result"]="SUCCESS";
       response["details"]=Details;
    }
    else
    {
       response["result"]="FAILURE";
       response["details"]="Failed to get the value";
       DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetParamCharValue --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetParamCharValue --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CMHAL_GetParamUlongValue
 * Description      : This will get the Ulong values
 * @param [in]  req - paramName : Holds the name of api
  		      paramType  :Holds NULL in the case of negative scenario and empty otherwise
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
*
 *******************************************************************************************/
void CMHAL::CMHAL_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetParamUlongValue  --->Entry \n");
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
        returnValue = ssp_CMHAL_GetParamUlongValue(paramName,&value);
    else
       returnValue = ssp_CMHAL_GetParamUlongValue(paramName,NULL);

    if(0 == returnValue)
    {
        sprintf(Details,"%d", value);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetParamUlongValue --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetParamUlongValue --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : CMHAL_GetErrorCodeWords
 * Description          :This function will invoke the SSP  HAL wrapper to get the ErrorCodeWords
 *
 * @param [in] req-    : flag: To handle negative scenario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void CMHAL::CMHAL_GetErrorCodeWords(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function CMHAL_GetErrorCodeWords stub\n");
    int isNegativeScenario = 0;
    char details[800] = {'\0'};
    char value[800] = {'\0'};

    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }

    if(ssp_CMHAL_GetErrorCodeWords(value,isNegativeScenario) == 0)
        {
                sprintf(details, "Value returned successfully\n");
                DEBUG_PRINT(DEBUG_TRACE, "Successfully retrieved the ErrorCodeWords status\n");
                response["result"] = "SUCCESS";
                response["details"] = details;
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "CMHAL_GetErrorCodeWords function has failed.Please check logs";
                return;
        }
}

/*******************************************************************************************
 *
 * Function Name        : CMHAL_Init
 * Description          :This function will invoke the SSP  HAL wrapper to init the CM
 *
 * @param [in] req-     :ParamName : Name of the api
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void CMHAL::CMHAL_Init(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function CMHAL_Init stub\n");
    char details[64] = {'\0'};
    char paramName[64] = {'\0'};

    strcpy(paramName,req["paramName"].asCString());

    if(ssp_CMHAL_Init(paramName) == 0)
        {
                sprintf(details, "CM  has initiated successfully\n");
                DEBUG_PRINT(DEBUG_TRACE, "Successfully initiated the CM \n");
                response["result"] = "SUCCESS";
                response["details"] = details;
                return;
        }
        else
        {
                response["result"] = "FAILURE";
                response["details"] = "CMHAL_Init function has failed.Please check logs";
                return;
        }
}

/*******************************************************************************************
 *
 * Function Name        : CMHAL_GetDocsisEventLogItems
 * Description          :This function will invoke the SSP  HAL wrapper to get the DocsisEventLogItems
 *
 * @param [in] req-    :flag- to execute negative scenarios
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void CMHAL::CMHAL_GetDocsisEventLogItems(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function CMHAL_GetDocsisEventLogItems stub\n");
    int isNegativeScenario = 0;
    char details[120] = {'\0'};
    CMMGMT_CM_EventLogEntry_t entries[DOCSIS_EVENT_LOG_SIZE];

    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }

    if(ssp_CMHAL_GetDocsisEventLogItems(entries, DOCSIS_EVENT_LOG_SIZE,isNegativeScenario) == 0)
    {
        sprintf(details, "Retrieved the event log items  successfully");
        DEBUG_PRINT(DEBUG_TRACE, "Successfully retrieved the event log items\n");
        response["result"] = "SUCCESS";
        response["details"] = details;
        return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "CMHAL_GetDocsisEventLogItems function has failed.Please check logs";
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : CMHAL_SetLEDFlashStatus
 * Description          :This function will invoke the SSP  HAL wrapper to set the LEDFlashStatus
 *
 * @param [in] req-    :LEDFlash - to enable LEDFlash status
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void CMHAL::CMHAL_SetLEDFlashStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetLEDFlashStatus --->Entry \n");
    int returnValue = 0;
    unsigned char* LEDFlash;
    char Details[64] = {'\0'};

    LEDFlash=(unsigned char*)req["LEDFlash"].asCString();
    returnValue = ssp_CMHAL_SetLEDFlashStatus(*LEDFlash);
    if(0 == returnValue)
    {
        sprintf(Details,"CMHAL_SetLEDFlashStatus enabled successfully");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set enable status";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetLEDFlashStatus failed--->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetLEDFlashStatus --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : CMHAL_ClearDocsisEventLog
 * Description          :This function will invoke the SSP  HAL wrapper to clear the docsis event logs
 *
 * @param [in] req-    :
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void CMHAL::CMHAL_ClearDocsisEventLog(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function CMHAL_ClearDocsisEventLog stub\n");
    char details[120] = {'\0'};
    int return_status = 0;
    return_status=ssp_CMHAL_ClearDocsisEventLog();
    if(return_status== 0)
    {
        sprintf(details, "Cleared the docsis log successfully\n");
        response["result"] = "SUCCESS";
        response["details"] = details;
        return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "CMHAL_ClearDocsisEventLog function has failed.Please check logs";
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : CMHAL_GetCPEList
 * Description          : This function will invoke the SSP  HAL wrapper to get the CPE List
 *
 * @param [in] req-     : flag- to execute negative scenarios
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 * @param [in] req-     : lanMode - to know lan operational mode of device 
 ********************************************************************************************/
void CMHAL::CMHAL_GetCPEList(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function CMHAL_GetCPEList stub\n");
    int isNegativeScenario = 0;
    char details[120] = {'\0'};
    unsigned long int InstanceNum =0;
    char cpeList[120] = {'\0'};
    char lanMode[60]  = {'\0'};
    strcpy(lanMode,req["lanMode"].asCString());
    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }
    if(ssp_CMHAL_GetCPEList(&InstanceNum,cpeList,lanMode,isNegativeScenario) == 0)
    {
        sprintf(details, "%s InstNum :%d ", cpeList, InstanceNum);
        DEBUG_PRINT(DEBUG_TRACE, "Successfully retrieved cpe list\n");
        response["result"] = "SUCCESS";
        response["details"] = details;
        return;
    }
    else
    {sprintf(details, "Failed to get the cpe List, InstNum :%d ",InstanceNum);
        response["result"] = "FAILURE";
        response["details"] = details;
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : CMHAL_SetMddIpModeOverride
 * Description          : This function will invoke the SSP  HAL wrapper to set the MddIpModeOverride
 *
 * @param [in] req-     : Value - To set the MddIpModeOverride
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void CMHAL::CMHAL_SetMddIpModeOverride(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetMddIpModeOverride --->Entry \n");
    int returnValue = 0;
    char Value[60];
    char Details[64] = {'\0'};
    strcpy(Value,req["value"].asCString());
    returnValue = ssp_CMHAL_SetMddIpModeOverride(Value);
    if(0 == returnValue)
    {
        sprintf(Details,"CMHAL_SetMddIpModeOverride:set function success");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set MddIpModeOverride";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetMddIpModeOverride failed--->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetMddIpModeOverride --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CMHAL_SetStartFreq
 * Description      : This function will set the StartFreq
 *
 * @param [in] req-    : Value - Value to set the StartFreq
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CMHAL::CMHAL_SetStartFreq(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetStartFreq --->Entry \n");
    int returnValue = 0;
    int Value = 0;
    /* Validate the input arguments */
    if(&req["Value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    Value = req["Value"].asInt();
    returnValue = ssp_CMHAL_SetStartFreq(Value);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully set the StartFreq";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set the StartFreq";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetStartFreq --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetStartFreq  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CMHAL_SetUSChannelId
 * Description      : This function will set the USChannelId
 *
 * @param [in] req-    : Value - Value to set the UDChannelId
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CMHAL::CMHAL_SetUSChannelId(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetUSChannelId --->Entry \n");
    int returnValue = 0;
    int Value = 0;
    /* Validate the input arguments */
    if(&req["Value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    Value = req["Value"].asInt();
    returnValue = ssp_CMHAL_SetUSChannelId(Value);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="US Channel ID is set successfully";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set the US Channel ID";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetUSChannelId --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetUSChannelId  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : CMHAL_SetHTTP_Download_Interface
 * Description          : This function will invoke the SSP  HAL wrapper to set the HTTP_Download_Interface
 *
 * @param [in] req-     : interface - The value of download interface
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void CMHAL::CMHAL_SetHTTP_Download_Interface(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetHTTP_Download_Interface --->Entry \n");
    int returnValue = 0;
    unsigned int interface =0;
    char Details[64] = {'\0'};
    interface =req["interface"].asInt();
    returnValue = ssp_CMHAL_SetHTTP_Download_Interface(interface);
    if(0 == returnValue)
    {
        sprintf(Details,"CMHAL_SetHTTP_Download_Interface set interface successfully");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set download interface";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetHTTP_Download_Interface failed--->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetHTTP_Download_Interface --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : CMHAL_HTTP_Download
 * Description          :This function will invoke the SSP  HAL wrapper to Download
 *
 * @param [in] req-     : None
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void CMHAL::CMHAL_HTTP_Download(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_HTTP_Download --->Entry \n");
    int returnValue = 0;
    char Details[64] = {'\0'};

    returnValue = ssp_CMHAL_Download();
    if(0 == returnValue)
    {
        sprintf(Details,"CMHAL_HTTP_Download: success");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to download ";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_HTTP_Download failed--->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_HTTP_Download --->Exit\n");
    return;
}
/*******************************************************************************************
 *
 * Function Name        : CMHAL_Reboot_Now
 * Description          :This function will invoke the SSP  HAL wrapper to Reboot
 *
 * @param [in] req-     : None
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void CMHAL::CMHAL_Reboot_Now(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_Reboot_Now --->Entry \n");
    int returnValue = 0;
    char Details[64] = {'\0'};

    returnValue = ssp_CMHAL_Reboot_Now();
    if(0 == returnValue)
    {
        sprintf(Details,"CMHAL_Reboot_Now: success");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to reboot ";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_Reboot_Now failed--->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_Reboot_Now --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CMHAL_GetHTTP_Download_Url
 * Description      : This will get the HTTP_Download_Url and filename
 *
 * @param [in]      : httpURL : To save the URL
 *					: filename : To save the filename

 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CMHAL::CMHAL_GetHTTP_Download_Url(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetHTTP_Download_Url  --->Entry \n");
    int returnValue = 0;
    char httpURL[200]={'\0'};
    char Details[800] = {'\0'};
    char filename[200]= {'\0'};
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());

    if(strcmp(paramType, "NULL"))
    {
      DEBUG_PRINT(DEBUG_TRACE,"\n Executing Positive Sceanrio\n");
      returnValue = ssp_CMHAL_GetHTTP_Download_Url(httpURL,filename);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Executing Negative Scenario\n");
        returnValue = ssp_CMHAL_GetHTTP_Download_Url(NULL,NULL);
    }
    if(0 == returnValue)
    {
       sprintf(Details,"url is %s, filename is %s",httpURL,filename);
       response["result"]="SUCCESS";
       response["details"]=Details;
    }
    else
    {
       response["result"]="FAILURE";
       response["details"]="Failed to get the value of URL and file";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetHTTP_Download_Url --->Exit\n");
    return;
}
/*******************************************************************************************
 *
 * Function Name        : CMHAL_SetHTTP_Download_Url
 * Description          : This function will invoke the SSP  HAL wrapper to set the HTTP_Download_Url
 *
 * @param [in] req-     : httpURL : The URL of the site from which the file is to be downloaded
 *                        filename : The name of the file to be downloaded
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void CMHAL::CMHAL_SetHTTP_Download_Url(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetHTTP_Download_Url --->Entry \n");
    int returnValue = 0;
    char httpURL[60] = {'\0'};
    char filename[60] = {'\0'};
    char Details[64] = {'\0'};

    strcpy(httpURL,req["httpURL"].asCString());
    strcpy(filename,req["filename"].asCString());

    returnValue = ssp_CMHAL_SetHTTP_Download_Url(httpURL,filename);
    if(0 == returnValue)
    {
        sprintf(Details,"CMHAL_SetHTTP_Download_Url:set function success");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set HTTP_Download_Url";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetHTTP_Download_Url failed--->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_SetHTTP_Download_Url --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : CMHAL_FWupdateAndFactoryReset
 * Description          : This function will invoke the SSP  HAL wrapper to FWupdateAndFactoryReset
 *
 * @param [in] req-     : URL - Image URL
                        : imageName - Name of the image
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void CMHAL::CMHAL_FWupdateAndFactoryReset(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_FWupdateAndFactoryReset --->Entry \n");
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

    returnValue = ssp_CMHAL_FWupdateAndFactoryReset(url,imagename);
    if(0 == returnValue)
    {
        sprintf(Details,"CMHAL_FWupdateAndFactoryReset: success");
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to FWupdateAndFactoryReset ";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_FWupdateAndFactoryReset failed--->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_FWupdateAndFactoryReset --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CMHAL_GetDsOfdmChanTable
 * Description      : This will get the values in DS OFDM channel table
 *
 * @param [in]  req - paramName : Holds the name of api
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CMHAL::CMHAL_GetDsOfdmChanTable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetDsOfdmChanTable --->Entry \n");

    int returnValue = 0;
    char paramName[100];
    char Details[800] = {'\0'};
    char value[700];
    int NoOfEntries = 0;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    strcpy(paramName,req["paramName"].asCString());
    if (strcmp(paramType, "NULL"))
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Executing Positive Sceanrio\n");
        returnValue = ssp_CMHAL_GetDsOfdmChanTable(paramName,value,&NoOfEntries);
    }
    else
    {
         DEBUG_PRINT(DEBUG_TRACE,"\n Executing Negative Scenario\n");
         returnValue = ssp_CMHAL_GetDsOfdmChanTable(paramName,value,NULL);
    }
    if(0 == returnValue)
    {
       sprintf(Details,"No of Entries in table:%d; Value:%s", NoOfEntries,value);
       response["result"]="SUCCESS";
       response["details"]=Details;
    }
    else
    {
       response["result"]="FAILURE";
       response["details"]="Failed to get the value from docsis_GetDsOfdmChanTable()";
       DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetDsOfdmChanTable --->Exit\n");
       return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetDsOfdmChanTable --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CMHAL_GetUsOfdmChanTable
 * Description      : This will get the values in US OFDM channel table
 *
 * @param [in]  req - paramName : Holds the name of api
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CMHAL::CMHAL_GetUsOfdmChanTable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetUsOfdmChanTable --->Entry \n");

    int returnValue = 0;
    char paramName[100];
    char Details[800] = {'\0'};
    char value[700];
    int NoOfEntries = 0;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    strcpy(paramName,req["paramName"].asCString());
    if(strcmp(paramType, "NULL"))
    {
       DEBUG_PRINT(DEBUG_TRACE,"\n Executing Positive Sceanrio\n");
       returnValue = ssp_CMHAL_GetUsOfdmChanTable(paramName,value,&NoOfEntries);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Executing Negative Scenario\n");
        returnValue = ssp_CMHAL_GetUsOfdmChanTable(paramName,value,NULL);
    }
    if(0 == returnValue)
    {
       sprintf(Details,"No of Entries in table:%d; Value:%s", NoOfEntries,value);
       response["result"]="SUCCESS";
       response["details"]=Details;
    }
    else
    {
       response["result"]="FAILURE";
       response["details"]="Failed to get the value from docsis_GetUsOfdmChanTable()";
       DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetUsOfdmChanTable --->Exit\n");
       return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetUsOfdmChanTable --->Exit\n");
    return;
}
/*******************************************************************************************
 *
 * Function Name    : CMHAL_GetStatusOfdmaUsTable
 * Description      : This will get the status of dmaUsTable
 *
 * @param [in]  req - paramName : Holds the name of api
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CMHAL::CMHAL_GetStatusOfdmaUsTable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetStatusOfdmaUsTable --->Entry \n");

    int returnValue = 0;
    char paramName[100];
    char Details[800] = {'\0'};
    char value[700];
    int NoOfEntries = 0;
    char paramType[10] = {'\0'};
    strcpy(paramType, req["paramType"].asCString());

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    strcpy(paramName,req["paramName"].asCString());

    if(strcmp(paramType, "NULL"))
    {
       DEBUG_PRINT(DEBUG_TRACE,"\n Executing Positive Sceanrio\n");
       returnValue = ssp_CMHAL_GetStatusOfdmaUsTable(paramName,value,&NoOfEntries);
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Executing Negative Scenario\n");
        returnValue = ssp_CMHAL_GetStatusOfdmaUsTable(paramName,value,NULL);
    }
    if(0 == returnValue)
    {
       sprintf(Details,"No of Entries in table:%d; Value:%s", NoOfEntries,value);
       response["result"]="SUCCESS";
       response["details"]=Details;
    }
    else
    {
       response["result"]="FAILURE";
       response["details"]="Failed to get the value from docsis_GetStatusOfdmaUsTable()";
       DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetDsOfdmChanTable --->Exit\n");
       return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_GetStatusOfdmaUsTable --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CMHAL_IsEnergyDetected
 * Description      : This will get the Energy Detected status from HAL
 
 * @param [in]  req - none
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CMHAL::CMHAL_IsEnergyDetected(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_IsEnergyDetected --->Entry \n");
    int returnValue = 0;
    char* energyDetected = 0;
    char Details[800] = {'\0'};
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    if(strcmp(paramType, "NULL"))
    {
       DEBUG_PRINT(DEBUG_TRACE,"\n Executing Positive Sceanrio\n");
       returnValue = ssp_CMHAL_IsEnergyDetected(energyDetected);
    }
    else
    {
       DEBUG_PRINT(DEBUG_TRACE,"\n Executing Negative Sceanrio\n");
       returnValue = ssp_CMHAL_IsEnergyDetected(NULL);
    }
    if(0 == returnValue)
    {
       if(energyDetected != NULL)
       {
           sprintf(Details,"CMHAL_IsEnergyDetected:%d", energyDetected);
           response["result"]="SUCCESS";
           response["details"]=Details;
       }
    }
    else
    {
       response["result"]="FAILURE";
       response["details"]="Failed to get the value from docsis_IsEnergyDetected()";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CMHAL_IsEnergyDetected --->Exit\n");
    return;
}

/**************************************************************************
 * Function Name        : CreateObject
* Description  : This function will be used to create a new object for the
 *                      class "CMHAL".
*
+ **************************************************************************/

extern "C" CMHAL* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new CMHAL(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/

bool CMHAL::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"CMHAL shutting down\n");
    return TEST_SUCCESS;
}

/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object
 *
 **************************************************************************/
extern "C" void DestroyObject(CMHAL *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying CMHAL object\n");
    delete stubobj;
}
