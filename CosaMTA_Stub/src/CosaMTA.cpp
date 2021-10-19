/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
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

#include "CosaMTA.h"
#include "ssp_tdk_wrp.h"

/* To provide external linkage to C Functions defined in TDKB Component folder */

extern "C"
{
    int ssp_register(bool);
    int ssp_CosaDmlMtaGetResetCount(int handleType, int bufferType, char *pResetType, unsigned long* ResetCount);
    int ssp_CosaDmlMTAGetDHCPInfo(int handleType, int bufferType, void* DHCPInfo);
    int ssp_CosaDmlMTATriggerDiagnostics();

    int ssp_CosaDmlMtaBatteryGetInfo(int handleType, int bufferType, char* BatteryInfo);
    int ssp_CosaDmlMtaBatteryGetStatus(int handleType, int bufferType, char* BatteryStatus);
    int ssp_CosaDmlMtaBatteryGetPowerStatus(int handleType, int bufferType, char* Power);
    int ssp_CosaDmlMtaLineTableGetNumberOfEntries(int handleType, unsigned long* lineTableNumOfEntries);
    int ssp_CosaDmlMtaLineTableGetEntry(int handleType, int bufferType, unsigned long* TableEntry);

    int ssp_CosaDmlMTAGetServiceClass(int handleType, void* SerClass);
    int ssp_CosaDmlMTADectGetEnable(int handleType,int Value);
    int ssp_CosaDmlMTADectSetEnable(int handleType,int Value);
    int ssp_CosaDmlMTADectGetRegistrationMode(int handleType,int Value);
    int ssp_CosaDmlMTADectSetRegistrationMode(int handleType,int Value);

    int ssp_CosaDmlMTAGetDect(int handleType,int bufferType, void* DectInfo);
    int ssp_CosaDmlMTAGetDectPIN(int handleType,int bufferType,char *pin);
    int ssp_CosaDmlMTASetDectPIN(int handleType,int bufferType, char *pin);
    int ssp_CosaDmlMTAGetDSXLogEnable(int handleType,int Value, int *Bool);

    int ssp_CosaDmlMTASetDSXLogEnable(int handleType,int Value);
    int ssp_CosaDmlMTAClearDSXLog(int handleType,int Value);
    int ssp_CosaDmlMTAGetCallSignallingLogEnable(int handleType,int Value,int *Bool);
    int ssp_CosaDmlMTASetCallSignallingLogEnable(int handleType,int Value);
    int ssp_CosaDmlMTAClearCallSignallingLog(int handleType,int Value);
    int ssp_CosaDmlMtaBatteryGetNumberofCycles(int handleType, unsigned long* Num);
    int ssp_CosaDmlMtaBatteryGetRemainingTime(int handleType, unsigned long* Num);
    int ssp_CosaDmlMtaBatteryGetLife(int handleType, int bufferType, char *Life);
    int ssp_CosaDmlMtaBatteryGetCondition(int handleType, int bufferType, char *Cond);
    int ssp_terminate();
    int ssp_CosaDmlMtaInit(void);
    int ssp_CosaDmlMTAGetServiceFlow(int handleType, unsigned long* count, PMTA_SERVICE_FLOW *ppCfg);
    int ssp_CosaDmlMTAGetDSXLogs(int handleType, unsigned long* count, PMTA_DSXLOG *ppLog);
    int ssp_CosaDmlMTAGetMtaLog(int handleType, unsigned long* count, PDML_MTALOG_FULL *ppConf);
    int ssp_CosaDmlMTAGetDhcpStatus(unsigned long* output_pIpv4status, unsigned long* output_pIpv6status);
    int ssp_CosaDmlMTAGetConfigFileStatus(unsigned long* poutput_status);
    int ssp_CosaDmlMTAGetLineRegisterStatus(char* pcLineRegisterStatus);
    int ssp_CosaDmlMTAGetParamUlongValue(int handleType, char* paramName, unsigned long* value); 
    int ssp_CosaDmlMTAGetCalls(int handleType, unsigned long, unsigned long*, PMTA_CALLS *);
    int ssp_CosaDmlMTAGetHandsets(int handleType, unsigned long* count, PMTA_HANDSETS_INFO *ppHandsets);
};

/***************************************************************************
 *Function name : initialize
 *Description  : Initialize Function will be used for registering the wrapper method
 *          with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/

bool CosaMTA::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE,"TDK::CosaMTA Initialize\n");
    return TEST_SUCCESS;
}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string CosaMTA::testmodulepre_requisites()
{
    int returnValue;
    returnValue = ssp_register(1);

    if(0 != returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepre_requisites: Failed to initialize \n");
        return "TEST_FAILURE";
    }

    returnValue = ssp_CosaDmlMtaInit();
    if(0 != returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepre_requisites: Failed to initialize the COSA MTA DML\n");
        return "TEST_FAILURE";
    }

    return "SUCCESS";
}

/***************************************************************************
 *Function name : testmodulepost_requisites
 *Description    : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/
bool CosaMTA::testmodulepost_requisites()
{
    return 0;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetResetCount
 * Description      : This function is used to retrieve the reset count of MTAResetCount, LineResetCount
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType: Holds whether buffer passed is valid or NULL
 * @param [in]  req - resetType: Holds whether reset type is MTAResetCount, LineResetCount or invalid
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_GetResetCount(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetResetCount --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;
    char resetType[MAX_PARAM_SIZE];
    unsigned long ResetCount=0;
    char Details[64] = {'\0'};

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    if(&req["resetType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();
    strcpy(resetType,req["resetType"].asCString());

    /* Invoke the wrapper function to get the reset count */
  returnValue = ssp_CosaDmlMtaGetResetCount(handleType,bufferType,resetType,&ResetCount);
    if(0 == returnValue)
    {
	sprintf(Details,"Reset count retrieved is: %lu", ResetCount);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the reset count";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetResetCount --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetResetCount  --->Exit\n");
    return;
}
/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetDHCPInfo
 * Description      : This function will retrieve the DHCP information
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaMTA::CosaMTA_GetDHCPInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDHCPInfo --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;
    void* DHCPInfo;
    char Details[64] = {'\0'};

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();
    returnValue = ssp_CosaDmlMTAGetDHCPInfo(handleType,bufferType,DHCPInfo);
    if(0 == returnValue)
    {
	sprintf(Details,"DHCP Info retrieved is: %s", DHCPInfo);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the DHCP information";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDHCPInfo --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDHCPInfo  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_TriggerDiagnostics
 * Description      : This function will check the index value
 *
 * @param [in]  req - index - 0
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaMTA::CosaMTA_Triggerdiagnostics(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_TriggerDiagnostics --->Entry \n");

    int returnValue = 0;
    returnValue = ssp_CosaDmlMTATriggerDiagnostics();
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully checked the index value of Trigger diagnostics";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to check the index value of trigger diagnostics";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_TriggerDiagnostics --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_TriggerDiagnostics  --->Exit\n");
    return;
}
/*******************************************************************************************
 *
 * Function Name    : CosaMTA_BatteryGetInfo
 * Description      : This function is used to retrieve the battery info
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType: Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaMTA::CosaMTA_BatteryGetInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetInfo --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;
    char BatteryInfo[50]={'\0'};
    char Details[64] = {'\0'};


    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }


    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();


    returnValue = ssp_CosaDmlMtaBatteryGetInfo(handleType,bufferType,BatteryInfo);
    if(0 == returnValue)
    {
	sprintf(Details,"Battery Info is retrieved is: %s", BatteryInfo);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the Battery info";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetInfo --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetResetCount  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_BatteryGetStatus
 * Description      : This function is used to retrieve the battery status
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType: Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_BatteryGetStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetStatus --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;
    char BatteryStatus[50];
    char Details[64] = {'\0'};

    // Validate the input arguments
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();

    returnValue = ssp_CosaDmlMtaBatteryGetStatus(handleType,bufferType,BatteryStatus);
    if(0 == returnValue)
    {
	sprintf(Details,"Battery Status retrieved is: %s", BatteryStatus);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the Battery Status";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetStatus --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetStatus  --->Exit\n");
    return;
}



/*******************************************************************************************
 *
 * Function Name    : CosaMTA_BatteryGetPowerStatus
 * Description      : This function is used to retrieve the battery power status
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType: Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaMTA::CosaMTA_BatteryGetPowerStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetPowerStatus --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;
    char Power[20];
    char Details[64] = {'\0'};


    // Validate the input arguments
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();
    returnValue = ssp_CosaDmlMtaBatteryGetPowerStatus(handleType,bufferType,Power);
    if(0 == returnValue)
    {
	sprintf(Details,"Power Status retrieved is: %s",Power);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the battery power status";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetPowerStatus --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetPowerStatus  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_LineTableGetNumberOfEntries
 * Description      : This function is used to retrieve the number of entries in line table
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_LineTableGetNumberOfEntries(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_LineTableGetNumberOfEntries --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    unsigned long lineTableNumOfEntries = 0;
    char Details[64] = {'\0'};

    // Validate the input arguments
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    handleType = req["handleType"].asInt();
    returnValue = ssp_CosaDmlMtaLineTableGetNumberOfEntries(handleType, &lineTableNumOfEntries);

    if(0 == returnValue)
    {
	sprintf(Details,"No of Line table entries retrieved is: %lu", lineTableNumOfEntries);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the Line Table Entries";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_LineTableGetNumberOfEntries --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_LineTableGetNumberOfEntries  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_LineTableGetEntry
 * Description      : This function is used to retrieve the number of entries in line table
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaMTA::CosaMTA_LineTableGetEntry(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_LineTableGetEntry --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;
    unsigned long TableEntry=0;
    char Details[64] = {'\0'};


    // Validate the input arguments
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    if(&req["bufferType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    handleType = req["handleType"].asInt();
    bufferType = req["bufferType"].asInt();
    returnValue = ssp_CosaDmlMtaLineTableGetEntry(handleType, bufferType, &TableEntry);
    if(0 == returnValue)
    {
	sprintf(Details,"TableEntry retrieved is: %lu", TableEntry);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the Line Table Entries";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_LineTableGetEntry --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_LineTableGetEntry  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetServiceClass
 * Description      : This function will get the service class
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_GetServiceClass(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetServiceClass --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    void *SerClass;
    char Details[64] = {'\0'};

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();

    returnValue = ssp_CosaDmlMTAGetServiceClass(handleType, SerClass);
    if(0 == returnValue)
    {
	sprintf(Details,"Service Class is retrieved is: %s", SerClass);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the Service class";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetServiceClass --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetServiceClass  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_DectGetEnable
 * Description      : This function will get the dect value
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - Value : Holds whether the value is 0 or 1
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_DectGetEnable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectGetEnable --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;
    char Details[64] = {'\0'};

    int isNegativeScenario = 0;

    if(&req["flag"])
    {
       isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
       DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
       returnValue = ssp_CosaDmlMTADectGetEnable(0,0);
    }
    else
    {
        /* Validate the input arguments */
        if(&req["handleType"]==NULL)
        {
           response["result"]="FAILURE";
           response["details"]="NULL parameter as input argument";
           return;
        }

        if(&req["Value"]==NULL)
        {
           response["result"]="FAILURE";
           response["details"]="NULL parameter as input argument";
           return;
        }

        handleType = req["handleType"].asInt();
        Value = req["Value"].asInt();

        returnValue = ssp_CosaDmlMTADectGetEnable(handleType,Value);
     }
     printf("return value is %d\n",returnValue);
     if(0 == returnValue)
     {
	sprintf(Details,"Enable value of Dect is :%d",returnValue);
        response["result"]="SUCCESS";
        response["details"]=Details;
     }
     else
     {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the Enable value of Dect";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectGetEnable --->Exit\n");
        return;
     }
     DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectGetEnable  --->Exit\n");
     return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_DectSetEnable
 * Description      : This function will set the Dect Enable value
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - boolType : Holds whether boolvalue is 0 or 1
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_DectSetEnable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectSetEnable --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
       isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
       DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
       returnValue = ssp_CosaDmlMTADectSetEnable(0,0);
    }
    else
    {
        /* Validate the input arguments */
        if(&req["handleType"]==NULL)
        {
          response["result"]="FAILURE";
          response["details"]="NULL parameter as input argument";
          return;
        }

        if(&req["Value"]==NULL)
        {
           response["result"]="FAILURE";
           response["details"]="NULL parameter as input argument";
           return;
        }

        handleType = req["handleType"].asInt();
        Value = req["Value"].asInt();

        returnValue = ssp_CosaDmlMTADectSetEnable(handleType,Value);
    }
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully set the Dect enable";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set the Dect enable";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectSetEnable --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectSetEnable  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_DectGetRegistrationMode
 * Description      : This function will get the dect registration mode
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - Value : Holds whether boolvalue as 0 or 1
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_DectGetRegistrationMode(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectGetRegistrationMode --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;
    char Details[64]={'\0'};
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
       isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
       DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
       returnValue = ssp_CosaDmlMTADectGetRegistrationMode(0,0);
    }
    else
    {
        /* Validate the input arguments */
        if(&req["handleType"]==NULL)
        {
           response["result"]="FAILURE";
           response["details"]="NULL parameter as input argument";
           return;
        }

        if(&req["Value"]==NULL)
        {
          response["result"]="FAILURE";
          response["details"]="NULL parameter as input argument";
          return;
        }

        handleType = req["handleType"].asInt();
        Value    = req["Value"].asInt();

        returnValue = ssp_CosaDmlMTADectGetRegistrationMode(handleType,Value);
    }
    if(0 == returnValue)
    {
	sprintf(Details,"Registration mode is :%d",returnValue);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the dect registration mode";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectGetRegistrationMode --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectGetRegistrationMode  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_DectSetRegistrationMode
 * Description      : This function will set the dect registration mode
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - Value : Holds the Value as 0 or 1
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_DectSetRegistrationMode(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectSetRegistrationMode --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
       isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
       DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
       returnValue = ssp_CosaDmlMTADectSetRegistrationMode(0,0);
    }
    else
    {
      /* Validate the input arguments */
      if(&req["handleType"]==NULL)
      {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
      }

      if(&req["Value"]==NULL)
      {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
      }

      handleType = req["handleType"].asInt();
      Value = req["Value"].asInt();

      returnValue = ssp_CosaDmlMTADectSetRegistrationMode(handleType,Value);
    }
    printf("return value is %d\n",returnValue);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully set the dect registration mode";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set the dect registration mode";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectSetRegistrationMode --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_DectSetRegistrationMode  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetDect
 * Description      : This function will get the Dect value
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_GetDect(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDect --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;
    void* DectInfo;
    char Details[64] = {'\0'};
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
       isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
       DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
       returnValue = ssp_CosaDmlMTAGetDect(0,0,NULL);
    }
    else
    {
       /* Validate the input arguments */
       if(&req["handleType"]==NULL)
       {
         response["result"]="FAILURE";
         response["details"]="NULL parameter as input argument";
         return;
       }

       if(&req["bufferType"]==NULL)
       {
         response["result"]="FAILURE";
         response["details"]="NULL parameter as input argument";
         return;
       }

       handleType = req["handleType"].asInt();
       bufferType = req["bufferType"].asInt();
       printf("handleType %d\nbufferType %d\n",handleType,bufferType);

       returnValue = ssp_CosaDmlMTAGetDect(handleType,bufferType, DectInfo);
    }
    printf("return value is %d\n",returnValue);
    if(0 == returnValue)
    {
	sprintf(Details,"Dect Info retrieved is: %s", DectInfo);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the Dect information";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDect --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDect  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetDectPIN
 * Description      : This function will get the Dect pin information
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_GetDectPIN(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDectPIN --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;
    char pin[64] = {0};
    char Details[64] = {'\0'};
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
       isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
       DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
       returnValue = ssp_CosaDmlMTAGetDectPIN(0,0,NULL);
    }
    else
    {
      /* Validate the input arguments */
      if(&req["handleType"]==NULL)
      {
         response["result"]="FAILURE";
         response["details"]="NULL parameter as input argument";
         return;
      }

      if(&req["bufferType"]==NULL)
      {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
      }

      handleType = req["handleType"].asInt();
      bufferType = req["bufferType"].asInt();
    
      returnValue = ssp_CosaDmlMTAGetDectPIN(handleType,bufferType,pin);
    }
    if(0 == returnValue)
    {
	sprintf(Details,"Dect pin retrieved is: %s",pin);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the Dect pin information";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDectPIN --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDectPIN  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_SetDectPIN
 * Description      : This function will set the Dect pin information
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType : Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_SetDectPIN(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_SetDectPIN --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int bufferType = 0;
    char pin[64] = {0};
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
       isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
       DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
       returnValue = ssp_CosaDmlMTASetDectPIN(0,0,NULL);
    }
    else
    {
      /* Validate the input arguments */
      if(&req["handleType"]==NULL)
      {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
      }

      if(&req["bufferType"]==NULL)
      {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
      }

      if(&req["value"]==NULL)
      {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
      }

      handleType = req["handleType"].asInt();
      bufferType = req["bufferType"].asInt();
      strcpy(pin,req["value"].asCString());

      returnValue = ssp_CosaDmlMTASetDectPIN(handleType,bufferType,pin);
    }
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully set the Dect pin information";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set the Dect pin information";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_SetDectPIN --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_SetDectPIN  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_BatteryGetNumberofCycles
 * Description      : This function will retrive the number of cycles in battery
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaMTA::CosaMTA_BatteryGetNumberofCycles(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetNumberofCycles --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    unsigned long Num=0;
    char Details[64] = {'\0'};

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }


    handleType = req["handleType"].asInt();

    returnValue = ssp_CosaDmlMtaBatteryGetNumberofCycles(handleType, &Num);
    if(0 == returnValue)
    {
	sprintf(Details,"Number of cycles retrieved is: %lu", Num);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the number of cycles in battery";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetNumberofCycles --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetNumberofCycles  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetDSXLogEnable
 * Description      : This function will retrieve the enabled DSX log
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - Value : Holds whether Value passed is 0 or 1
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_GetDSXLogEnable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDSXLogEnable --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;
    int Bool=0;
    char Details[64] = {'\0'};

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["Value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();
    Value = req["Value"].asInt();

    returnValue = ssp_CosaDmlMTAGetDSXLogEnable(handleType,Value, &Bool);
    printf("return value is %d\n",returnValue);
    if(0 == returnValue)
    {
	sprintf(Details,"DSX logs retrieved is: %d", Bool);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the enabled DSX log information";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDSXLogEnable --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDSXLogEnable  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_SetDSXLogEnable
 * Description      : This function will enable the DSX Log
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - Value : Holds whether boolvalue passed is 0 or 1
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_SetDSXLogEnable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_SetDSXLogEnable --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["Value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();
    Value = req["Value"].asInt();

    returnValue = ssp_CosaDmlMTASetDSXLogEnable(handleType,Value);
    printf("return value is %d\n",returnValue);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully enabled the DSX Log";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to enable the DSX Log";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_SetDSXLogEnable --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_SetDSXLogEnable  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_ClearDSXLog
 * Description      : This function will clear the DSX Log
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - Value : Holds whether boolvalue passed is 0 or 1
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_ClearDSXLog(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_ClearDSXLog --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["Value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();
    Value = req["Value"].asInt();

    returnValue = ssp_CosaDmlMTAClearDSXLog(handleType,Value);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully cleared the DSX Log";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to clear the DSX Log";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_ClearDSXLog --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_ClearDSXLog  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetCallSignallingLogEnable
 * Description      : This function will get the enable value for call signalling log
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - Value : Holds whether Value passed is 0 or 1
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_GetCallSignallingLogEnable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetCallSignallingLogEnable --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;
    int Bool=0;
    char Details[64] = {'\0'};

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["Value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();
    Value = req["Value"].asInt();

    returnValue = ssp_CosaDmlMTAGetCallSignallingLogEnable(handleType,Value, &Bool);
    printf("return value is %d\n",returnValue);
    if(0 == returnValue)
    {
	sprintf(Details,"Call signal log retrieved is: %d", Bool);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the enable value for call signalling log";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetCallSignallingLogEnable --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetCallSignallingLogEnable  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_SetCallSignallingLogEnable
 * Description      : This function will enable the call signalling log
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - Value : Holds whether Value passed is 0 or 1
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_SetCallSignallingLogEnable(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_SetCallSignallingLogEnable --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["Value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();
    Value = req["Value"].asInt();

    returnValue = ssp_CosaDmlMTASetCallSignallingLogEnable(handleType,Value);
    printf("return value is %d\n",returnValue);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully enabled the call signalling log";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to enable the call signalling log";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_SetCallSignallingLogEnable --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_SetCallSignallingLogEnable  --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_ClearCallSignallingLog
 * Description      : This function will clear the call signalling log
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - boolvalue : Holds whether Value passed is 0 or 1
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/


void CosaMTA::CosaMTA_ClearCallSignallingLog(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_ClearCallSignallingLog --->Entry \n");

    int returnValue = 0;
    int handleType = 0;
    int Value = 0;

    /* Validate the input arguments */
    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["Value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();
    Value = req["Value"].asInt();

    returnValue = ssp_CosaDmlMTAClearCallSignallingLog(handleType,Value);
    printf("return value is %d\n",returnValue);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully cleared the call signalling log";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to clear the call signalling log";
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_ClearCallSignallingLog --->Exit\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_ClearCallSignallingLog  --->Exit\n");
    return;
}


/*******************************************************************************************
 *
 * Function Name    : CosaMTA_BatteryGetRemainingTime
 * Description      : This function will get the battery Remaining time
 *
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaMTA::CosaMTA_BatteryGetRemainingTime(IN const Json::Value& req, OUT Json::Value& response)
{
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetRemainingTime --->Entry \n");

        int returnValue = 0;

        int handleType = 0;
	unsigned long Num=0;
	char Details[64] = {'\0'};

                    /* Validate the input arguments */

        if(&req["handleType"]==NULL)
        {
            response["result"]="FAILURE";
            response["details"]="NULL parameter as input argument";
            return;
        }


        handleType = req["handleType"].asInt();

        returnValue = ssp_CosaDmlMtaBatteryGetRemainingTime(handleType, &Num);
        if(0 == returnValue)
        {
	    sprintf(Details,"Remaining time retrieved is: %lu", Num);
            response["result"]="SUCCESS";
            response["details"]=Details;
        }
        else
        {
            response["result"]="FAILURE";
            response["details"]="Failed to retrieve the battery remaining time";
            DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetRemainingTime --->Exit\n");
            return;
        }
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetRemainingTime --->Exit\n");
        return;
}


/*******************************************************************************************
 *
 * Function Name    : CosaMTA_BatteryGetCondition
 * Description      : This function is used to retrieve the battery Condition
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType: Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaMTA::CosaMTA_BatteryGetCondition(IN const Json::Value& req, OUT Json::Value& response)
{
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetCondition --->Entry \n");

        int returnValue = 0;
        int handleType = 0;
        int bufferType = 0;
	char Cond[20];
	char Details[64] = {'\0'};

        //Validate the input arguments
            if(&req["handleType"]==NULL)
            {
                response["result"]="FAILURE";
                response["details"]="NULL parameter as input argument";
                return;
            }
        if(&req["bufferType"]==NULL)
        {
            response["result"]="FAILURE";
            response["details"]="NULL parameter as input argument";
            return;
        }

        handleType = req["handleType"].asInt();
        bufferType = req["bufferType"].asInt();

        returnValue = ssp_CosaDmlMtaBatteryGetCondition(handleType,bufferType,Cond);
        if(0 == returnValue)
        {
	    sprintf(Details,"Battery condition retrieved is: %s",Cond);
            response["result"]="SUCCESS";
            response["details"]=Details;
        }
        else
        {
            response["result"]="FAILURE";
            response["details"]="Failed to retrieve the Battery Condition";
            DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetCondition --->Exit\n");
            return;
        }
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetCondition  --->Exit\n");
        return;
}


/*******************************************************************************************
 *
 * Function Name    : CosaMTA_BatteryGetLife
 * Description      : This function is used to retrieve the battery life
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [in]  req - bufferType: Holds whether buffer passed is valid or NULL
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void CosaMTA::CosaMTA_BatteryGetLife(IN const Json::Value& req, OUT Json::Value& response)
{
            DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetLife --->Entry \n");

            int returnValue = 0;
            int handleType = 0;
            int bufferType = 0;
	    char Life[20];
	    char Details[64] = {'\0'};

          //  Validate the input arguments
                if(&req["handleType"]==NULL)
                {
                    response["result"]="FAILURE";
                    response["details"]="NULL parameter as input argument";
                    return;
                }
            if(&req["bufferType"]==NULL)
            {
                response["result"]="FAILURE";
                response["details"]="NULL parameter as input argument";
                return;
            }

            handleType = req["handleType"].asInt();
            bufferType = req["bufferType"].asInt();


            returnValue = ssp_CosaDmlMtaBatteryGetLife(handleType,bufferType,Life);
            if(0 == returnValue)
            {
				sprintf(Details,"Battery life retrieved is: %s",Life);
                response["result"]="SUCCESS";
                response["details"]=Details;
            }
            else
            {
                response["result"]="FAILURE";
                response["details"]="Failed to retrieve the Battery Life";
                DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetLife --->Exit\n");
                return;
            }
            DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_BatteryGetLife  --->Exit\n");
            return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetServiceFlow
 * Description      : This function is used to retrieve ServiceFlo
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_GetServiceFlow(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetServiceFlow --->Entry \n");
    int returnValue = 0;
    int handleType = 0;
    char details[1024] = {'\0'}, *d;
    unsigned long count = 0;
    PMTA_SERVICE_FLOW pFlow = NULL, p;
    int i;

    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();

    returnValue = ssp_CosaDmlMTAGetServiceFlow(handleType, &count, &pFlow);
    if(0 == returnValue)
    {
        if (pFlow)
        {
            p = pFlow;
            d = details;
            for (i=0; i<count; i++)
            {
                sprintf(d,"FLOW=%u;SFID=%u;ServiceClassName=%s;Direction=%s;ScheduleType=%u;DefaultFlow=%d;NomGrantInterval=%u;UnsolicitGrantSize=%u;TolGrantJitter=%u;NomPollInterval=%u;MinReservedPkt=%u;MaxTrafficRate=%u;MinReservedRate=%u;MaxTrafficBurst=%u;TrafficType=%s;NumberOfPackets=%u;",
                        i,p->SFID,p->ServiceClassName,p->Direction,p->ScheduleType,p->DefaultFlow,p->NomGrantInterval,p->UnsolicitGrantSize,p->TolGrantJitter,p->NomPollInterval,p->MinReservedPkt,p->MaxTrafficRate,p->MinReservedRate,p->MaxTrafficBurst,p->TrafficType,p->NumberOfPackets);
                if (strlen(details) < 512)
                {
                    d = details + strlen(details);
                    p++;
                }
                else break;
            }
            free(pFlow);
        }
        else
        {
            sprintf(details, "There is no ServiceFlow data to display");
        }
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
	sprintf(details, "Failed to get the value");
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetServiceFlow execution details: %s", details);
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetServiceFlow --->Exit\n");
    return;
}


/**************************************************************************
n Name    : CosaMTA_GetDSXLogs
 * Description      : This function is used to retrieve DSXLogs
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_GetDSXLogs(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDSXLogs --->Entry \n");
    int returnValue = 0;
    int handleType = 0;
    char details[1024] = {'\0'}, *d;
    unsigned long count = 0;
    PMTA_DSXLOG pLog = NULL, p;
    int i;

    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();

    returnValue = ssp_CosaDmlMTAGetDSXLogs(handleType, &count, &pLog);
    if(0 == returnValue)
    {
        if (pLog)
        {
            p = pLog;
            d = details;
            sprintf(d, "COUNT=%u;",count);
            d = details + strlen(details);
            for (i=0; i<count; i++)
            {
                sprintf(d, "Time=%s;Description=%s;ID=%u;Level=%u;",p->Time,p->Description,p->ID,p->Level);
                if (strlen(details) < 512)
                {
                    d = details + strlen(details);
                    p++;
                }
                else break;
            }
            free(pLog);
        }
        else
        {
            sprintf(details, "There is no log available");
        }
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
	sprintf(details, "Failed to get the value");
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDSXLogs execution details: %s", details);
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDSXLogs --->Exit\n");
    return;
}


/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetMtaLog
 * Description      : This function is used to retrieve MTA Log
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_GetMtaLog(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetMtaLog --->Entry \n");
    int returnValue = 0;
    int handleType = 0;
    char details[1024] = {'\0'}, *d, desc[100];
    unsigned long count = 0;
    PDML_MTALOG_FULL pLog = NULL, p;
    int i;

    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();

    returnValue = ssp_CosaDmlMTAGetMtaLog(handleType, &count, &pLog);
    if(0 == returnValue)
    {
        if (pLog)
        {
            p = pLog;
            d = details;
            sprintf(d, "COUNT=%u;",count);
            d = details + strlen(details);
            for (i=0; i<count; i++)
            {
                memset(desc, '\0', 100);
                if (p->pDescription)
                {
                    strncpy(desc, p->pDescription, 99);
                }
                sprintf(d, "Index=%u;EventID=%u;EventLevel=%s;Time=%s;Description=%s;",
                        p->Index,p->EventID,p->EventLevel,p->Time,desc);
                if (strlen(details) < 512)
                {
                    d = details + strlen(details);
                    p++;
                }
                else break;
            }
            p = pLog;
            for (i=0; i<count; i++)
            {
                free(p->pDescription);
                p++;
            }
            free(pLog);
        }
        else
        {
            sprintf(details, "There is no log available");
        }
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
	sprintf(details, "Failed to get the value");
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetMtaLog execution details: %s", details);
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetMtaLog--->Exit\n");
    return;
}
  

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetDhcpStatus
 * Description      : This function is used to retrieve MTA Log
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_GetDhcpStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDhcpStatus --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'};
    unsigned long output_pIpv4status = 0;
    unsigned long output_pIpv6status = 0;
    char const *status_string[4] = { "MTA_INIT", "MTA_START", "MTA_COMPLETE", "MTA_ERROR" };

    returnValue = ssp_CosaDmlMTAGetDhcpStatus(&output_pIpv4status, &output_pIpv4status);
    if(0 == returnValue)
    {
        sprintf(details, "Ipv4 status=%s;Ipv6 status=%s", status_string[output_pIpv4status], status_string[output_pIpv6status]);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
	sprintf(details, "Failed to get the value");
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDhcpStatus execution details: %s", details);
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetDhcpStatus --->Exit\n");
    return;
}


/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetConfigFileStatus
 * Description      : This function is used to retrieve MTA Log
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_GetConfigFileStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetConfigFileStatus --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'};
    unsigned long output_status = 0;
    char const *status_string[4] = { "MTA_INIT", "MTA_START", "MTA_COMPLETE", "MTA_ERROR" };

    returnValue = ssp_CosaDmlMTAGetConfigFileStatus(&output_status);
    if(0 == returnValue)
    {
        sprintf(details, "Config File Status=%s", status_string[output_status]);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
	sprintf(details, "Failed to get the value");
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetConfigFileStatus execution details: %s", details);
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetConfigFileStatus --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name    : CosaMTA_GetLineRegisterStatus
 * Description      : This function is used to retrieve MTA Log
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_GetLineRegisterStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetLineRegisterStatus --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'};
    char lineRegisterStatus[128] = {'\0'};

    returnValue = ssp_CosaDmlMTAGetLineRegisterStatus(lineRegisterStatus);
    if(0 == returnValue)
    {
        sprintf(details, "Line Register status=%s", lineRegisterStatus);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
	sprintf(details, "Failed to get the value");
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetLineRegisterStatus execution details: %s", details);
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetLineRegisterStatus --->Exit\n");
    return;
}


/*******************************************************************************************
 *
 * Function Name : CosaMTA_GetParamUlongValue
 * Description   : This will get the Ulong values
 * @param [in]   : req - paramName : Holds the name of api
 *                 req - handleType : Holds the message bus handle
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
*
 *******************************************************************************************/
void CosaMTA::CosaMTA_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetParamUlongValue---> Entry \n");
    int returnValue = 0;
    int handleType = 0;
    char paramName[100] = {'\0'};
    char Details[64] = {'\0'};
    unsigned long value = 0;
    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    strcpy(paramName,req["paramName"].asCString());

    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    handleType = req["handleType"].asInt();

    returnValue =  ssp_CosaDmlMTAGetParamUlongValue(handleType,paramName,&value);
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
	DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetParamUlongValue: Failed to get the value\n");
        DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetParamUlongValue---> Exit\n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetParamUlongValue execution details: %s\n", Details);
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetParamUlongValue---> Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : CosaMTA_GetCalls
 * Description   : This will get all call info for the given instance number of LineTable
 * @param [in]   : req - value : instance number
 *                 req - count : Holds the line number of Call
 *                 req - pCfg  : Holds the MTA call info
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_GetCalls(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetCalls --->Entry \n");
    int handleType = 0;
    int returnValue = 0;
    char details[1024] = {'\0'}, *d;
    unsigned long value = 0;
    unsigned long count = 0;
    PMTA_CALLS pCfg = NULL, p;
    int i;

    if(&req["value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    value = req["value"].asInt();

    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    handleType = req["handleType"].asInt();

    returnValue = ssp_CosaDmlMTAGetCalls(handleType, value, &count, &pCfg);

    if(0 == returnValue)
    {
        if (pCfg)
        {
            p = pCfg;
            d = details;
            for (i=0; i<count; i++)
            {
                sprintf(d,"COUNT=%u;Codec=%s;RemoteCodec=%s;CallStartTime=%s;CallEndTime=%s;CWErrorRate=%s;PktLossConcealment=%s;JitterBufferAdaptive=%d;Originator=%d;RemoteIPAddress=%X;CallDuration=%u;CWErrors=%s;SNR=%s;MicroReflections=%s;DownstreamPower=%s;UpstreamPower=%s;EQIAverage=%s;EQIMinimum=%s;EQIMaximum=%s;EQIInstantaneous=%s;MOS_LQ=%s;MOS_CQ=%s;EchoReturnLoss=%s;SignalLevel=%s;NoiseLevel=%s;LossRate=%s;DiscardRate=%s;BurstDensity=%s;GapDensity=%s;BurstDuration=%s;GapDuration=%s;RoundTripDelay=%s;Gmin=%s;RFactor=%s;ExternalRFactor=%s;JitterBufRate=%s;JBNominalDelay=%s;JBMaxDelay=%s;JBAbsMaxDelay=%s;TxPackets=%s;TxOctets=%s;RxPackets=%s;RxOctets=%s;PacketLoss=%s;IntervalJitter=%s;",
                        i+1,p->Codec,p->RemoteCodec,p->CallStartTime,p->CallEndTime,p->CWErrorRate,p->PktLossConcealment,p->JitterBufferAdaptive,p->Originator,p->RemoteIPAddress.Value,p->CallDuration,p->CWErrors,p->SNR,p->MicroReflections,p->DownstreamPower,p->UpstreamPower,p->EQIAverage,p->EQIMinimum,p->EQIMaximum,p->EQIInstantaneous,p->MOS_LQ,p->MOS_CQ,p->EchoReturnLoss,p->SignalLevel,p->NoiseLevel,p->LossRate,p->DiscardRate,p->BurstDensity,p->GapDensity,p->BurstDuration,p->GapDuration,p->RoundTripDelay,p->Gmin,p->RFactor,p->ExternalRFactor,p->JitterBufRate,p->JBNominalDelay,p->JBMaxDelay,p->JBAbsMaxDelay,p->TxPackets,p->TxOctets,p->RxPackets,p->RxOctets,p->PacketLoss,p->IntervalJitter);
                if (strlen(details) < 512)
                {
                    d = details + strlen(details);
                    p++;
                }
                else break;
            }
            free(pCfg);
        }
        else
        {
            sprintf(details, "There is no data to display for Line %d", value+1);
        }
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
	sprintf(details, "Failed to get the value");
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetCalls execution details: %s", details);
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetCalls--->Exit\n");
    return;
}

/**************************************************************************
n Name    : CosaMTA_GetHandsets
 * Description      : This function is used to retrieve Handsets details
 * @param [in]  req - handleType : Holds the message bus handle
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void CosaMTA::CosaMTA_GetHandsets(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetHandsets --->Entry \n");
    int returnValue = 0;
    int handleType = 0;
    char details[1024] = {'\0'}, *d;
    unsigned long count = 0;
    PMTA_HANDSETS_INFO pHandsets = NULL, p;
    int i;

    if(&req["handleType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    handleType = req["handleType"].asInt();

    returnValue = ssp_CosaDmlMTAGetHandsets(handleType, &count, &pHandsets);
    if(0 == returnValue)
    {
        if (pHandsets)
        {
            p = pHandsets;
            d = details;
            sprintf(d, "COUNT=%u;",count);
            d = details + strlen(details);
            for (i=0; i<count; i++)
            {
                sprintf(d, "InstanceNumber=%lu;Status=%d;LastActiveTime=%s;HandsetName=%s,HandsetFirmware=%s,OperatingTN=%s,SupportedTN=%s;",p->InstanceNumber,p->Status,p->LastActiveTime,p->HandsetName,p->HandsetFirmware,p->OperatingTN,p->SupportedTN);
                if (strlen(details) < 512)
                {
                    d = details + strlen(details);
                    p++;
                }
                else break;
            }
            free(pHandsets);
        }
        else
        {
            sprintf(details, "There is no handset info available");
        }
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "Failed to get the value");
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetHandsets execution details: %s", details);
    DEBUG_PRINT(DEBUG_TRACE,"\n CosaMTA_GetHandsets--->Exit\n");
    return;
}

/**************************************************************************
 * Function Name    : CreateObject
 * Description : This function will be used to create a new object for the
 *          class "CosaMTA".
 *
 **************************************************************************/

extern "C" CosaMTA* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new CosaMTA(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/

bool CosaMTA::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"CosaMTA shutting down\n");
    return TEST_SUCCESS;
}

/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(CosaMTA *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying CosaMTA object\n");
    delete stubobj;
}






