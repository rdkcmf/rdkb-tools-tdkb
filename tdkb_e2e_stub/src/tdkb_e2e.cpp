/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2017 RDK Management
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
#include <sstream>
#include "tdkb_e2e.h"

/***************************************************************************
 *Function name : initialize
 *Description   : Initialize Function will be used for registering the wrapper method
 *                        with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/
bool TDKB_E2E::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE,"TDK::TDKB_E2E Initialize\n");
    return TEST_SUCCESS;
}
/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string TDKB_E2E::testmodulepre_requisites()
{
    int returnValue;
    int bStart = 1;
    DEBUG_PRINT(DEBUG_TRACE,"\n TDKB_E2E::testmodulepre_requisites");
    returnValue = ssp_register(bStart);
    if(0 != returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepre_requisites --->Error invoking WIFI Agent in DUT !!! \n");
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
bool TDKB_E2E::testmodulepost_requisites()
{
    int returnValue;
    int bStart = 0;
    returnValue = ssp_register(bStart);
    if(1 != returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepost_requisites --->Error invoking WIFI Agent in DUT !!! \n");
        return TEST_FAILURE;
    }
    return TEST_SUCCESS;
}
/*******************************************************************************************
 *
 * Function Name        : tdkb_e2e_Get
 * Description          : This function will invoke TDK Component GET Value wrapper
 *                                function to get parameter value
 *
 * @param [in] req- This holds Path name for Parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                                 ssp_getParameterValue
 ********************************************************************************************/
void TDKB_E2E::tdkb_e2e_Get(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n tdkb_e2e_Get --->Entry\n");
    bool bReturn = TEST_FAILURE;
    char ParamNames[MAX_PARAM_SIZE];
    GETPARAMVALUES *resultDetails;
    int paramsize=0;
    char paramDetails[200] = {0};
    strcpy(ParamNames,req["paramName"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\n ParamNames input is %s",ParamNames);
    resultDetails = ssp_getParameterValue(&ParamNames[0],&paramsize);
    if(resultDetails == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="Get Parameter Value API Validation Failure";
    }
    else
    {
        sprintf(paramDetails, "NAME:%s VALUE:%s TYPE:%d",resultDetails[0].pParamNames,resultDetails[0].pParamValues,resultDetails[0].pParamType);
        response["result"]="SUCCESS";
        response["details"]=paramDetails;
        bReturn = TEST_SUCCESS;
        for(int i=0; i < paramsize; i++)
        {
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Id is %d\n",i);
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Name retrieved is: %s\n",resultDetails[i].pParamNames);
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Value retrieved is: %s",resultDetails[i].pParamValues);
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Type retrieved is: %d\n",resultDetails[i].pParamType);
            free(resultDetails[i].pParamValues);
        }
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n tdkb_e2e_Get --->Exit\n");
    return;
}
/*******************************************************************************************
 *
 * Function Name        : tdkb_e2e_Set
 * Description          : This function will invoke TDK Component SET Value wrapper
 *                                function
 *
 * @param [in] req-        This holds Path name, Value to set and its type
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                                 ssp_setParameterValue
 ********************************************************************************************/
void TDKB_E2E::tdkb_e2e_Set(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n tdkb_e2e_Set --->Entry\n");
    bool bReturn = TEST_FAILURE;
    int returnValue = 0;
    int retVal = 0;
    char ParamName[MAX_PARAM_SIZE];
    char ParamValue[MAX_PARAM_SIZE];
    char ParamType[MAX_PARAM_SIZE];
    int commit = 1;
    strcpy(ParamName,req["paramName"].asCString());
    strcpy(ParamValue,req["paramValue"].asCString());
    strcpy(ParamType,req["paramType"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\ntdkb_e2e_Set:: ParamName input is %s",ParamName);
    DEBUG_PRINT(DEBUG_TRACE,"\ntdkb_e2e_Set:: ParamValue input is %s",ParamValue);
    DEBUG_PRINT(DEBUG_TRACE,"\ntdkb_e2e_Set:: ParamType input is %s",ParamType);
    returnValue = ssp_setParameterValue(&ParamName[0],&ParamValue[0],&ParamType[0],commit);
    if(0 == returnValue)
    {
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="SET API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="tdkb_e2e_Set::SET API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdkb_e2e_Set --->Error in Set API Validation of WIFI Agent in DUT !!! \n");
    }
    if ((!strncmp(ParamName, "Device.WiFi.Radio.1.", 20)) || (!strncmp(ParamName, "Device.WiFi.AccessPoint.1.", 26)) || (!strncmp(ParamName, "Device.WiFi.SSID.1.", 19)))
    {
        printf("Apply the wifi settings for 2.4GHZ\n");
        retVal = ssp_setParameterValue("Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting","true","boolean",commit);
    }
    else if ((!strncmp(ParamName, "Device.WiFi.Radio.2.", 20)) || (!strncmp(ParamName, "Device.WiFi.AccessPoint.2.", 26)) || (!strncmp(ParamName, "Device.WiFi.SSID.2.", 19)))
    {
        printf("Apply the wifi settings for 5GHZ\n");
        retVal = ssp_setParameterValue("Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting","true","boolean",commit);
    }
    if((0 == returnValue) && (0 == retVal))
    {
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="SET API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="tdkb_e2e_Set::SET API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdkb_e2e_Set --->Error in Set API Validation in DUT !!! \n");
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n tdkb_e2e_Set --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : tdkb_e2e_SetMultipleParams
 * Description          : This function will set multiple parameter value at one shot
 *
 * @param [in] req-        ParamList will hold the entire list to be set.
 *
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                         ssp_setMultipleParameterValue
********************************************************************************************/
void TDKB_E2E::tdkb_e2e_SetMultipleParams(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n tdkb_e2e_SetMultipleParams --->Entry\n");
    int returnValue = 0;
    int retVal = 0;
    char params[1000] = {'\0'};
    char **paramlist  = NULL;
    int num_spaces = 0;
    int index = 0;
    int size = 0;
    int commit = 1;
    strcpy(params,req["paramList"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\ntdkb_e2e_SetMultipleParams:: ParamList input is %s\n",params);
    char *list = strtok (params, "|");
    while (list) {
    paramlist = (char **) realloc (paramlist, ++num_spaces * sizeof(char *));
    if (paramlist == NULL)
    {
       return; /* memory allocation failed */
    }
    paramlist[num_spaces-1] = list;
    list = strtok (NULL, "|");
   }
   /* realloc one extra element for the last NULL */
   paramlist = (char **) realloc (paramlist, (num_spaces+1) * sizeof(char *));
   paramlist[num_spaces] = 0;
   for (index = 0; index < (num_spaces); index++)
   {
     printf ("\nparamlist[%d] = %s\n", index, paramlist[index]);
   }
   printf("Index Count:%d\n",index);
   size = index/3;
   printf("ParamCount:%d\n",size);
   printf("Invoking ssp_setMultipleParameterValue function\n");
   returnValue = ssp_setMultipleParameterValue(paramlist,size);
   if(0 == returnValue)
   {
       response["result"]="SUCCESS";
       response["details"]="SET API Validation is Success";
   }
   else
   {
       response["result"]="FAILURE";
       response["details"]="tdkb_e2e_SetMultipleParams::SET API Validation is Failure";
       DEBUG_PRINT(DEBUG_TRACE,"\n tdkb_e2e_SetMultipleParams: Failed to set multiple parameters !!! \n");
   }
   if ((!strncmp(paramlist[0], "Device.WiFi.Radio.1.", 20)) || (!strncmp(paramlist[0], "Device.WiFi.AccessPoint.1.", 26)) || (!strncmp(paramlist[0], "Device.WiFi.SSID.1.", 19)))
    {
        printf("Apply the wifi settings for 2.4GHZ\n");
        retVal = ssp_setParameterValue("Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting","true","boolean",commit);
    }
    else if ((!strncmp(paramlist[0], "Device.WiFi.Radio.2.", 20)) || (!strncmp(paramlist[0], "Device.WiFi.AccessPoint.2.", 26)) || (!strncmp(paramlist[0], "Device.WiFi.SSID.2.", 19)))
    {
        printf("Apply the wifi settings for 5GHZ\n");
        retVal = ssp_setParameterValue("Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting","true","boolean",commit);
    }
    if((0 == returnValue) && (0 == retVal))
    {
        response["result"]="SUCCESS";
        response["details"]="SET API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="tdkb_e2e_SetMultipleParams::SET API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdkb_e2e_SetMultipleParams --->Error in Set API Validation in DUT !!! \n");
    }
    /* free the memory allocated */
   free(paramlist);
   DEBUG_PRINT(DEBUG_TRACE,"\n tdkb_e2e_SetMultipleParams --->Exit\n");
   return;
}
/**************************************************************************
 * Function Name        : CreateObject
 * Description  : This function will be used to create a new object for the
 *                class "TDKB_E2E".
 *
 **************************************************************************/
extern "C" TDKB_E2E* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new TDKB_E2E(ptrtcpServer);
}
/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/
bool TDKB_E2E::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"TDKB_E2E shutting down\n");
    return TEST_SUCCESS;
}
/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(TDKB_E2E *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying TDKB_E2E object\n");
    delete stubobj;
}
