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

#include "WIFIHAL.h"

/***************************************************************************
 *Function name : initialize
 *Description   : Initialize Function will be used for registering the wrapper method
 *                        with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/
bool WIFIHAL::initialize(IN const char* szVersion)
{
    return TEST_SUCCESS;
}


/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string WIFIHAL::testmodulepre_requisites()
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL testmodulepre_requisites --->Entry\n");

    int return_value = 0;

    return_value = ssp_wifi_init();

    if(0 == return_value)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepre_requisites ---> Initialize SUCCESS !!! \n");
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL testmodulepre_requisites --->Exit\n");
        return "SUCCESS";
    }
    else
    {
       DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepre_requisites --->Failed to initialize !!! \n");
       DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL testmodulepre_requisites --->Exit\n");
       return "FAILURE";
    }
}


/***************************************************************************
 *Function name : testmodulepost_requisites
 *Description    : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/
bool WIFIHAL::testmodulepost_requisites()
{
    return TEST_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetParamBoolValue
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is BOOL
 *
 * @param [in] req-    : methodName - identifier for the hal api name
 			  radioIndex - radio index value of wifi
                          enable     - the bool value to be get/set
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetParamBoolValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamBoolValue --->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex;
    unsigned char enable;
    int returnValue;
    int retValue;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    enable = req["param"].asInt();
    strcpy(paramType, req["paramType"].asCString());

    if(!(strncmp(methodName, "set",3)&&strncmp(methodName, "push",4)&&strncmp(methodName, "create",6)))
    {
	printf("wifi_set operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetParamBoolValue(radioIndex, &enable, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap")||strstr(methodName, "BandSteering"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(0 == retValue)
                {
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    printf("applyRadioSettings operation failed\n");
                    return;
                }
            }
	    else
		return;
        }
    }
    else
    {
        printf("wifi_get operation to be done\n");
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            returnValue = ssp_WIFIHALGetOrSetParamBoolValue(radioIndex, &enable, methodName);
        else
            returnValue = ssp_WIFIHALGetOrSetParamBoolValue(radioIndex, NULL, methodName);
        if(0 == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",enable);
            sprintf(details, "Enable state : %s", int(enable)? "Enabled" : "Disabled");
            response["result"]="SUCCESS";
            response["details"]=details;
	    return;
        }
     }
     sprintf(details, "%s operation failed", methodName);
     response["result"]="FAILURE";
     response["details"]=details;
     DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForBool --->Error in execution\n");
     return;
}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetParamULongValue
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is Unsigned long
 *
 * @param [in] req-    : methodName - identifier for the hal api name
			 radioIndex - radio index value of wifi
                         param     - the ulong value to be get/set
                         paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetParamULongValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamULongValue------>Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    unsigned long uLongVar = 0;
    int returnValue;
    int retValue;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    uLongVar = (unsigned long)req["param"].asLargestUInt();
    strcpy(paramType, req["paramType"].asCString());

    if(!strncmp(methodName, "set",3))
    {
	printf("wifi_set operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetParamULongValue(radioIndex, &uLongVar, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(0 == retValue)
                {
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    printf("applyRadioSettings operation failed\n");
                    return;
                }
            }
	    else
		return;
        }
    }
    else
    {
       printf("wifi_get operation to be done\n");
       //paramType is set as NULL for negative test scenarios, for NULL pointer checks
       if(strcmp(paramType, "NULL"))
           returnValue = ssp_WIFIHALGetOrSetParamULongValue(radioIndex, &uLongVar, methodName);
       else
           returnValue = ssp_WIFIHALGetOrSetParamULongValue(radioIndex, NULL, methodName);
       if(0 == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %lu\n",uLongVar);
            sprintf(details, "Value returned is :%lu", uLongVar);
            response["result"]="SUCCESS";
            response["details"]=details;
	    return;
        }
     }
     sprintf(details, "%s operation failed", methodName);
     response["result"]="FAILURE";
     response["details"]=details;
     DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForULong --->Error in execution\n");
     return;

}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetParamStringValue
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is a string
 *
 * @param [in] req-    : methodName - identifier for the hal api name
 			  radioIndex - radio index value of wifi
                          param     - the string value to be get
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetParamStringValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamStringValue  ----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    char output[1000] = {'\0'};
    int returnValue;
    int retValue;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    char param[200] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());
    strcpy(param, req["param"].asCString());

    if(!(strncmp(methodName, "set",3)&&strncmp(methodName, "push",4)&&strncmp(methodName, "kick",4)))
    {
	printf("wifi_set operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetParamStringValue(radioIndex, param, methodName);
        if(0 == returnValue)
        {
            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(0 == retValue)
                {
                    sprintf(details, "%s operation success", methodName);
                    response["result"]="SUCCESS";
                    response["details"]=details;
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    sprintf(details, "%s operation failed", methodName);
                    response["result"]="FAILURE";
                    response["details"]=details;
                    printf("applyRadioSettings operation Failed\n");
                    return;
                }
            }
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForString --->Error in execution\n");
            return;
        }
    }
    else
    {
        printf("wifi_get operation to be done\n");
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            returnValue = ssp_WIFIHALGetOrSetParamStringValue(radioIndex, output, methodName);
        else
            returnValue = ssp_WIFIHALGetOrSetParamStringValue(radioIndex, NULL, methodName);

        if(0 == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %s\n",output);
            sprintf(details, "Value returned is :%s", output);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForString --->Error in execution\n");
            return;
        }
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetRadioStandard
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is a string
 *
 * @param [in] req-    : methodName - identifier for the hal api name
                          radioIndex - radio index value of wifi
                          param     - the string value to be get
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
			  gOnly, nOnly, acOnly - the bool values to be set/get
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetRadioStandard(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamRadioStandard ----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    char output[1000] = {'\0'};
    int returnValue;
    int retValue;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    char param[200] = {'\0'};
    unsigned char gOnly, nOnly, acOnly;

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());
    strcpy(param, req["param"].asCString());
    gOnly = req["gOnly"].asInt();
    nOnly = req["nOnly"].asInt();
    acOnly = req["acOnly"].asInt();

    if(!strncmp(methodName, "set",3))
    {
        printf("wifi_set operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetRadioStandard(radioIndex, param, methodName, &gOnly, &nOnly, &acOnly);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(0 == retValue)
                {
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    printf("applyRadioSettings operation failed\n");
                    return;
                }
            }
            else
                return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForRadioStandard --->Error in execution\n");
            return;
        }
    }
    else
    {
        printf("wifi_get operation to be done\n");
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            returnValue = ssp_WIFIHALGetOrSetRadioStandard(radioIndex, output, methodName, &gOnly, &nOnly, &acOnly);
        else
            returnValue = ssp_WIFIHALGetOrSetRadioStandard(radioIndex, NULL, methodName, &gOnly, &nOnly, &acOnly);

        if(0 == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %s\n",output);
            sprintf(details, "Value returned is :%s %d %d %d", output,gOnly,nOnly,acOnly);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForRadioStandard --->Error in execution\n");
            return;
        }
    }
}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetParamIntValue
 * Description          : This function invokes WiFi hal's get apis, when the value to be
                          get  is an integer
 *
 * @param [in] req-    : methodName - identifier for the hal api name
 			  radioIndex - radio index value of wifi
                          param     - the int value to be get
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetParamIntValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamIntValue----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    int intParam = 0;
    int returnValue;
    int retValue;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    intParam = req["param"].asInt();
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());

    if(!strncmp(methodName, "set",3))
    {
	printf("wifi_set operation to be done\n");
        printf("MethodName : %s\n",methodName);
        returnValue = ssp_WIFIHALGetOrSetParamIntValue(radioIndex, &intParam, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(0 == retValue)
                {
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    printf("applyRadioSettings operation failed\n");
                    return;
                }
            }
	    else
		return;
        }
    }
    else
    {
        printf("wifi_get operation to be done\n");
        printf("MethodName : %s\n",methodName);
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            //When the paramType is not equal to NULL
            returnValue = ssp_WIFIHALGetOrSetParamIntValue(radioIndex, &intParam, methodName);
        else
            //When the paramType is NULL i.e., negative scenario
            returnValue = ssp_WIFIHALGetOrSetParamIntValue(radioIndex, NULL, methodName);
        if(0 == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",intParam);
            sprintf(details, "Value returned is :%d", intParam);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
     }
     sprintf(details, "%s operation failed", methodName);
     response["result"]="FAILURE";
     response["details"]=details;
     DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForInt --->Error in execution\n");
     return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetParamUIntValue
 * Description          : This function invokes WiFi hal's get apis, when the value to be
                          get  is an unsigned integer
 *
 * @param [in] req-    : methodName - identifier for the hal api name
 			  radioIndex - radio index value of wifi
                          param     - the int value to be get
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetParamUIntValue (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamUIntValue----->Entry\n");

    char methodName[50] = {'\0'};
    int radioIndex = 0;
    unsigned int uintParam = 0;
    int returnValue;
    int retValue;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    uintParam = req["param"].asInt();
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());

    if(!strncmp(methodName, "set",3))
    {
	printf("wifi_set operation to be done\n");
        printf("MethodName : %s\n",methodName);
        returnValue = ssp_WIFIHALGetOrSetParamUIntValue(radioIndex, &uintParam, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(0 == retValue)
                {
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    printf("applyRadioSettings operation failed\n");
                    return;
                }
            }
	    else
		return;
        }
    }
    else
    {
        printf("wifi_get operation to be done\n");
        printf("MethodName : %s\n",methodName);
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            //When the paramType is not equal to NULL
            returnValue = ssp_WIFIHALGetOrSetParamUIntValue(radioIndex, &uintParam, methodName);
        else
            //When the paramType is NULL i.e., negative scenario
            returnValue = ssp_WIFIHALGetOrSetParamUIntValue(radioIndex, NULL, methodName);
        if(0 == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %u\n",uintParam);
            sprintf(details, "Value returned is :%u", uintParam);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
     }
     sprintf(details, "%s operation failed", methodName);
     response["result"]="FAILURE";
     response["details"]=details;
     DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForUInt --->Error in execution\n");
     return;
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetIndexFromName
 * Description          : This function invokes WiFi hal api wifi_getIndexFromName()

 * @param [in] req-     : param     - the ssid name to be passed
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetIndexFromName (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetIndexFromName ----->Entry\n");

    int returnValue;
    int output = 1;
    char ssidName[10] = {'\0'};
    char details[200] = {'\0'};

    strcpy(ssidName, req["param"].asCString());

    returnValue = ssp_WIFIHALGetIndexFromName(ssidName, &output);
    if(0 == returnValue)
       {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",output);
            sprintf(details, "Value returned is :%d", output);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
    else
       {
            sprintf(details, "GetIndexFromName operation failed");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
       }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetIndexFromName  --->Exit\n");
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_ClearRadioResetCount
 * Description          : This function invokes WiFi hal api wifi_clearRadioResetCount()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_ClearRadioResetCount (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ClearRadioResetCount ----->Entry\n");

    int returnValue;
    char details[200] = {'\0'};

    returnValue = ssp_WIFIHALClearRadioResetCount();
    if(0 == returnValue)
       {
            sprintf(details, "ClearRadioResetCount operation success");
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
    else
       {
            sprintf(details, "ClearRadioResetCount operation failed");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
       }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ClearRadioResetCount  --->Exit\n");
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_Reset
 * Description          : This function invokes WiFi hal api wifi_reset()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_Reset (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Reset ----->Entry\n");

    int returnValue;
    char details[200] = {'\0'};

    returnValue = ssp_WIFIHALReset();
    if(0 == returnValue)
       {
            sprintf(details, "wifi_reset operation success");
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
    else
       {
            sprintf(details, "wifi_reset operation failed");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
       }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Reset --->Exit\n");
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetSecurityRadiusServer
 * Description          : This function invokes WiFi hal's get/set api's which are
                          related to SecurityRadiusServer
 *
 * @param [in] req-    :  methodName - identifier for the hal api name
                          radioIndex - radio index value of wifi
                          IPAddress - IP Address of the RADIUS server used for WLAN security
			  port - port  number of the RADIUS server used for WLAN security
			  RadiusSecret - RadiusSecret of the RADIUS server used for WLAN security
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetSecurityRadiusServer(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetSecurityRadiusServer----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    int returnValue;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    unsigned int port = 0;
    char IPAddress[50] = {'\0'};
    char RadiusSecret[100] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    port = req["port"].asInt();
    strcpy(IPAddress, req["IPAddress"].asCString());
    strcpy(RadiusSecret, req["RadiusSecret"].asCString());
    strcpy(paramType, req["paramType"].asCString());

    if(!strncmp(methodName, "set",3))
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Set operation requested\n");
        printf("MethodName : %s\n",methodName);
        returnValue = ssp_WIFIHALGetOrSetSecurityRadiusServer(radioIndex, IPAddress, &port, RadiusSecret, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetSecurityRadiusServer ---->Error in execution\n");
            return;
       }
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Get operation requested\n");
        printf("MethodName : %s\n",methodName);
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            //When the paramType is not equal to NULL
            returnValue = ssp_WIFIHALGetOrSetSecurityRadiusServer(radioIndex, IPAddress, &port, RadiusSecret, methodName);
        else
            //When the paramType is NULL i.e., negative scenario
            returnValue = ssp_WIFIHALGetOrSetSecurityRadiusServer(radioIndex, NULL, NULL, NULL, methodName);
        if(0 == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %s\n%d\n%s\n",IPAddress,port,RadiusSecret);
            sprintf(details, "Value returned is :IPAddress=%s,Port=%u,RadiusSecret=%s",IPAddress, port, RadiusSecret);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %s\n%d\n%s\n",IPAddress,port,RadiusSecret);
            DEBUG_PRINT(DEBUG_TRACE,"\n%s returned failure", methodName);
            sprintf(details, "Value returned is :IPAddress=%s,Port=%u,RadiusSecret=%s",IPAddress, port, RadiusSecret);
            response["result"]="FAILURE";
            response["details"]=details;
            return;
        }
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetSecurityRadiusServer ---->Error in execution\n");
        return;
     }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetApBridgeInfo
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is related to ApBridgeInfo
 *
 * @param [in] req-    : methodName - identifier for the hal api name
                          radioIndex - radio index value of wifi
                          bridgeName,IP,subnet - the string value to be get/set
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetApBridgeInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetApBridgeInfo  ----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    char output[1000] = {'\0'};
    int returnValue;
    int retValue;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    char bridgeName[32] = {'\0'};
    char IP[20] = {'\0'};
    char subnet[50] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());
    strcpy(bridgeName, req["bridgeName"].asCString());
    strcpy(IP, req["IP"].asCString());
    strcpy(subnet, req["subnet"].asCString());

    if(!strncmp(methodName, "set",3))
    {
        printf("wifi_set operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetApBridgeInfo(radioIndex, bridgeName, IP, subnet, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
            if(0 == retValue)
            {
                printf("applyRadioSettings operation success\n");
                return;
            }
            else
            {
                printf("applyRadioSettings operation failed\n");
                return;
            }
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForApBridgeInfo --->Error in execution\n");
            return;
        }
    }
    else
    {
        printf("wifi_get operation to be done\n");
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            returnValue = ssp_WIFIHALGetOrSetApBridgeInfo(radioIndex, bridgeName, IP, subnet, methodName);
        else
            returnValue = ssp_WIFIHALGetOrSetApBridgeInfo(radioIndex, NULL, NULL, NULL, methodName);

        if(0 == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %s\n%s\n%s\n",bridgeName,IP,subnet);
            sprintf(details, "Value returned is :bridgeName=%s,IP=%s,subnet=%s",bridgeName,IP,subnet);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForApBridgeInfo --->Error in execution\n");
            return;
	}
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetRadioDCSScanTime
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is related to RadioDCSScanTime
 *
 * @param [in] req-    : methodName - identifier for the hal api name
                         radioIndex - radio index value of wifi
                         output_interval_seconds,output_dwell_milliseconds - the integer value to be get/set
                         paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetRadioDCSScanTime(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetRadioDCSScanTime----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    char output[1000] = {'\0'};
    int returnValue;
    int retValue;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    int output_interval_seconds = 0;
    int output_dwell_milliseconds = 0;

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());
    output_interval_seconds = req["output_interval_seconds"].asInt();
    output_dwell_milliseconds = req["output_dwell_milliseconds"].asInt();

    if(!strncmp(methodName, "set",3))
    {
        printf("wifi_set operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetRadioDCSScanTime(radioIndex, &output_interval_seconds, &output_dwell_milliseconds, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
            if(0 == retValue)
            {
                printf("applyRadioSettings operation success\n");
                return;
            }
            else
            {
                printf("applyRadioSettings operation failed\n");
                return;
            }
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForRadioDCSScanTime --->Error in execution\n");
            return;
        }
    }
    else
    {
        printf("wifi_get operation to be done\n");
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            returnValue = ssp_WIFIHALGetOrSetRadioDCSScanTime(radioIndex, &output_interval_seconds, &output_dwell_milliseconds, methodName);
        else
            returnValue = ssp_WIFIHALGetOrSetRadioDCSScanTime(radioIndex, NULL, NULL, methodName);

        if(0 == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n%d\n",output_interval_seconds,output_dwell_milliseconds);
            sprintf(details, "Value returned is :output_interval_seconds=%d,output_dwell_milliseconds=%d",output_interval_seconds,output_dwell_milliseconds);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForRadioDCSScanTime --->Error in execution\n");
            return;
        }
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_AddorDelApAclDevice
 * Description          : This function invokes WiFi hal's add/delete apis, when the value to be
                          added/deleted is related to ApAclDevice
 *
 * @param [in] req-    : methodName - identifier for the hal api name
                          apIndex - ap index value of wifi
                          DeviceMacAddress - the MacAddress(string)of the device to be added/deleted
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_AddorDelApAclDevice(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_AddorDelApAclDevice------>Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    char output[1000] = {'\0'};
    int returnValue;
    char details[200] = {'\0'};
    char DeviceMacAddress[64] = {'\0'};
    strcpy(methodName, req["methodName"].asCString());
    apIndex = req["apIndex"].asInt();
    strcpy(DeviceMacAddress, req["DeviceMacAddress"].asCString());
    if(!strncmp(methodName, "add",3))
    {
        printf("wifi_add operation to be done\n");
        returnValue = ssp_WIFIHALAddorDelApAclDevice(apIndex, DeviceMacAddress, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForAddApAclDevice --->Error in execution\n");
            return;
        }
    }
    else
    {
        printf("wifi_delete operation to be done\n");
	returnValue = ssp_WIFIHALAddorDelApAclDevice(apIndex, DeviceMacAddress, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForDelApAclDevice --->Error in execution\n");
            return;
	}
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_IfConfigUporDown
 * Description          : This function invokes WiFi hal api's wifi_ifConfigDown() or wifi_ifConfigUp()

 * @param [in] req-     :  apIndex - ap Index value of wifi
                           methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_IfConfigUporDown(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_IfConfigUporDown------>Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    char output[1000] = {'\0'};
    int returnValue;
    char details[200] = {'\0'};
    strcpy(methodName, req["methodName"].asCString());
    apIndex = req["apIndex"].asInt();
    if(!strcmp(methodName, "ifConfigUp"))
    {
        printf("wifi_IfConfigUp operation to be done\n");
        returnValue = ssp_WIFIHALIfConfigUporDown(apIndex, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
	    return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForIfConfigUp --->Error in execution\n");
            return;
        }
    }
    else
    {
        printf("wifi_IfConfigDown operation to be done\n");
	returnValue = ssp_WIFIHALIfConfigUporDown(apIndex, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForIfConfigDown --->Error in execution\n");
            return;
	}
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_ParamRadioIndex
 * Description          : This function invokes WiFi hal api's which require radioIndex as input
 * @param [in] req-     :  radioIndex - radio Index value of wifi
                           methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_ParamRadioIndex(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ParamRadioIndex------>Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    char output[1000] = {'\0'};
    int returnValue;
    char details[200] = {'\0'};
    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    if(strstr(methodName, "cancel")||strstr(methodName, "set")||strstr(methodName, "reset")||strstr(methodName, "disable")||strstr(methodName, "remove")||strstr(methodName, "init")||strstr(methodName, "factoryReset"))
    {
        returnValue = ssp_WIFIHALParamRadioIndex(radioIndex, methodName);
	if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForParamRadioIndex --->Error in execution\n");
            return;
	}
    }
    else
        return;
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ParamRadioIndex --->Exit\n");
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_StartorStopHostApd
 * Description          : This function invokes WiFi hal api's wifi_startHostApd() and wifi_stopHostApd()
 * @param [in] req-     : methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_StartorStopHostApd(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_StartorStopHostApd ----->Entry\n");
    int returnValue;
    char details[200] = {'\0'};
    char output[1000] = {'\0'};
    char methodName[50] = {'\0'};
    strcpy(methodName, req["methodName"].asCString());
    if(strstr(methodName, "start")||strstr(methodName, "stop"))
    {
        returnValue = ssp_WIFIHALStartorStopHostApd(methodName);
	if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForStartorStopHostApd --->Error in execution\n");
            return;
	}
    }
    else
        return;
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_StartorStopHostApd --->Exit\n");
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_FactoryReset
 * Description          : This function invokes WiFi hal api's wifi_factoryResetRadios() and wifi_factoryReset()
 * @param [in] req-     : methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_FactoryReset(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_FactoryReset ----->Entry\n");
    int returnValue;
    char details[200] = {'\0'};
    char output[1000] = {'\0'};
    char methodName[50] = {'\0'};
    strcpy(methodName, req["methodName"].asCString());
    if(strstr(methodName, "Reset")||strstr(methodName, "ResetRadios"))
    {
        returnValue = ssp_WIFIHALFactoryReset(methodName);
	if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForFactoryReset --->Error in execution\n");
            return;
	}
    }
    else
        return;
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_FactoryReset --->Exit\n");
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetSecurityRadiusSettings
 * Description          : This function invokes WiFi hal get/set api's which are
                          related to SecurityRadiusSettings()

 * @param [in] req-     : radioIndex - radio Index value of wifi
                          methodName - identifier for the hal api name
			  RadiusServerRetries - Number of retries for Radius requests
			  RadiusServerRequestTimeout - Radius request timeout in seconds after which the request must be retransmitted for the # of
                                                       retries available
			  PMKLifetime - Default time in seconds after which a Wi-Fi client is forced to ReAuthenticate (def 8 hrs)
			  PMKCaching - Time interval in seconds after which the PMKSA (Pairwise Master Key Security Association)cache is purged (def 5min)
			  MaxAuthenticationAttempts - Indicates the # of time, a client can attempt to login with incorrect credentials.
                                                      When this limit is reached, the client is blacklisted and not allowed to attempt loging
                                                      into the network. Settings this parameter to 0 (zero) disables the blacklisting feature.
			  BlacklistTableTimeout - Time interval in seconds for which a client will continue to be blacklisted once it is marked so
			  IdentityRequestRetryInterval - Time Interval in seconds between identity requests retries. A value of 0 (zero) disables it
			  QuietPeriodAfterFailedAuthentication - The enforced quiet period (time interval) in seconds following failed authentication.
                                                                 A value of 0 (zero) disables it
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetSecurityRadiusSettings (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetSecurityRadiusSettings ----->Entry\n");

    wifiRadiusSetting radiusSetting;
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    int returnValue;
    char details[500] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    radiusSetting.RadiusServerRetries = req["RadiusServerRetries"].asInt();
    radiusSetting.RadiusServerRequestTimeout = req["RadiusServerRequestTimeout"].asInt();
    radiusSetting.PMKLifetime = req["PMKLifetime"].asInt();
    radiusSetting.PMKCaching = req["PMKCaching"].asInt();
    radiusSetting.PMKCacheInterval = req["PMKCacheInterval"].asInt();
    radiusSetting.MaxAuthenticationAttempts = req["MaxAuthenticationAttempts"].asInt();
    radiusSetting.BlacklistTableTimeout = req["BlacklistTableTimeout"].asInt();
    radiusSetting.IdentityRequestRetryInterval = req["IdentityRequestRetryInterval"].asInt();
    radiusSetting.QuietPeriodAfterFailedAuthentication = req["QuietPeriodAfterFailedAuthentication"].asInt();

    if(!strncmp(methodName, "set",3))
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Set operation requested\n");
        printf("MethodName : %s\n",methodName);
        returnValue = ssp_WIFIHALGetOrSetSecurityRadiusSettings(radioIndex, &radiusSetting, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Get operation requested\n");
        printf("MethodName : %s\n",methodName);
        returnValue = ssp_WIFIHALGetOrSetSecurityRadiusSettings(radioIndex, &radiusSetting, methodName);
        if(0 == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: ");
            sprintf(details, "Value returned is :RadiusServerRetries=%d,RadiusServerRequestTimeout=%d,PMKLifetime=%d,PMKCaching=%d,PMKCacheInterval=%d,MaxAuthenticationAttempts=%d,BlacklistTableTimeout=%d,IdentityRequestRetryInterval=%d,QuietPeriodAfterFailedAuthentication=%d",radiusSetting.RadiusServerRetries,radiusSetting.RadiusServerRequestTimeout,radiusSetting.PMKLifetime,radiusSetting.PMKCaching,radiusSetting.PMKCacheInterval,radiusSetting.MaxAuthenticationAttempts,radiusSetting.BlacklistTableTimeout,radiusSetting.IdentityRequestRetryInterval,radiusSetting.QuietPeriodAfterFailedAuthentication);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
     }
     sprintf(details, "%s operation failed", methodName);
     response["result"]="FAILURE";
     response["details"]=details;
     DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetSecurityRadiusSettings ---->Error in execution\n");
     return;
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetSSIDTrafficStats2
 * Description          : This function invokes WiFi hal api wifi_getSSIDTrafficStats2

 * @param [in] req-     : radioIndex - radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetSSIDTrafficStats2(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetSSIDTrafficStats2 ----->Entry\n");

    wifi_ssidTrafficStats2_t ssidTrafficStats2;
    int radioIndex = 0;
    int returnValue;
    char details[1000] = {'\0'};

    radioIndex = req["radioIndex"].asInt();

    returnValue = ssp_WIFIHALGetSSIDTrafficStats2(radioIndex, &ssidTrafficStats2);
    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :ssid_BytesSent=%lu,ssid_BytesReceived=%lu,ssid_PacketsSent=%lu,ssid_PacketsReceived=%lu,ssid_RetransCount=%lu,ssid_FailedRetransCount=%lu,ssid_RetryCount=%lu,ssid_MultipleRetryCount=%lu,ssid_ACKFailureCount=%lu,ssid_AggregatedPacketCount=%lu,ssid_ErrorsSent=%lu,ssid_ErrorsReceived=%lu,ssid_UnicastPacketsSent=%lu,ssid_UnicastPacketsReceived=%lu,ssid_DiscardedPacketsSent=%lu,ssid_UnicastPacketsReceived=%lu,ssid_DiscardedPacketsSent%lu,ssid_DiscardedPacketsReceived=%lu,ssid_MulticastPacketsSent=%lu,ssid_MulticastPacketsReceived=%lu,ssid_BroadcastPacketsSent=%lu,ssid_BroadcastPacketsRecevied=%lu,ssid_UnknownPacketsReceived=%lu\n",ssidTrafficStats2.ssid_BytesSent,ssidTrafficStats2.ssid_BytesReceived,ssidTrafficStats2.ssid_PacketsSent,ssidTrafficStats2.ssid_PacketsReceived,ssidTrafficStats2.ssid_RetransCount,ssidTrafficStats2.ssid_FailedRetransCount,ssidTrafficStats2.ssid_RetryCount,ssidTrafficStats2.ssid_MultipleRetryCount,ssidTrafficStats2.ssid_ACKFailureCount,ssidTrafficStats2.ssid_AggregatedPacketCount,ssidTrafficStats2.ssid_ErrorsSent,ssidTrafficStats2.ssid_ErrorsReceived,ssidTrafficStats2.ssid_UnicastPacketsSent,ssidTrafficStats2.ssid_UnicastPacketsReceived,ssidTrafficStats2.ssid_DiscardedPacketsSent,ssidTrafficStats2.ssid_UnicastPacketsReceived,ssidTrafficStats2.ssid_DiscardedPacketsSent,ssidTrafficStats2.ssid_DiscardedPacketsReceived,ssidTrafficStats2.ssid_MulticastPacketsSent,ssidTrafficStats2.ssid_MulticastPacketsReceived,ssidTrafficStats2.ssid_BroadcastPacketsSent,ssidTrafficStats2.ssid_BroadcastPacketsRecevied,ssidTrafficStats2.ssid_UnknownPacketsReceived);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getSSIDTrafficStats2 operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetSSIDTrafficStats2 ---->Error in execution\n");
        return;
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRadioTrafficStats2
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getRadioTrafficStats2()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioTrafficStats2 (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioTrafficStats2 ----->Entry\n");
    GetRadioTrafficStats2 TrafficStats2;
    int radioIndex = 0;
    int returnValue;
    char details[1000] = {'\0'};
    radioIndex = req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Get operation requested\n");
    returnValue = ssp_WIFIHALGetRadioTrafficStats2(radioIndex, &TrafficStats2);
    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :radio_BytesSent=%lu,radio_BytesReceived=%lu,radio_PacketsSent=%lu,radio_ErrorsSent=%lu,radio_PacketsReceived=%lu,radio_ErrorsReceived=%lu,radio_DiscardPacketsSent=%lu,radio_DiscardPacketsReceived=%lu,radio_PLCPErrorCount=%lu,radio_FCSErrorCount=%lu,radio_InvalidMACCount=%lu,radio_PacketsOtherReceived=%lu,radio_NoiseFloor=%lu,radio_ChannelUtilization=%lu,radio_ActivityFactor=%lu,radio_CarrierSenseThreshold_Exceeded=%lu,radio_RetransmissionMetirc=%lu,radio_MaximumNoiseFloorOnChannel=%lu,radio_MinimumNoiseFloorOnChannel=%lu,radio_MedianNoiseFloorOnChannel=%lu,radio_StatisticsStartTime=%lu",TrafficStats2.radio_BytesSent,TrafficStats2.radio_BytesReceived,TrafficStats2.radio_PacketsSent,TrafficStats2.radio_ErrorsSent,TrafficStats2.radio_PacketsReceived,TrafficStats2.radio_ErrorsReceived,TrafficStats2.radio_DiscardPacketsSent,TrafficStats2.radio_DiscardPacketsReceived,TrafficStats2.radio_PLCPErrorCount,TrafficStats2.radio_FCSErrorCount,TrafficStats2.radio_InvalidMACCount,TrafficStats2.radio_PacketsOtherReceived,TrafficStats2.radio_NoiseFloor,TrafficStats2.radio_ChannelUtilization,TrafficStats2.radio_ActivityFactor,TrafficStats2.radio_CarrierSenseThreshold_Exceeded,TrafficStats2.radio_RetransmissionMetirc,TrafficStats2.radio_MaximumNoiseFloorOnChannel,TrafficStats2.radio_MinimumNoiseFloorOnChannel,TrafficStats2.radio_MedianNoiseFloorOnChannel,TrafficStats2.radio_StatisticsStartTime);
        response["result"]="SUCCESS";
        response["details"]=details;
	return;
    }
    else
    {
        sprintf(details, "wifi_getRadioTrafficStats2 operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetRadioTrafficStats2  --->Error in execution\n");
        return;
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedDeviceDiagnosticResult
 * Description          : This function invokes WiFi hal api wifi_getApAssociatedDeviceDiagnosticResult
 * @param [in] req-     : radioIndex - radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult ----->Entry\n");
    wifi_associated_dev_t *associated_dev = (wifi_associated_dev_t*)malloc(sizeof(wifi_associated_dev_t));
    unsigned int output_array_size;
    int radioIndex = 0;
    int returnValue;
    char details[2000] = {'\0'};
    radioIndex = req["radioIndex"].asInt();
    if (associated_dev != NULL)
    {
         DEBUG_PRINT(DEBUG_TRACE,"\n Memory Allocated Successfully");
    }
    else
    {
         DEBUG_PRINT(DEBUG_TRACE, "\n Memory Allocation Failed");
    }
    returnValue = ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult(radioIndex, &associated_dev, &output_array_size);
    if(0 == returnValue)
    {
        //sprintf(details, "Value returned is :cli_MACAddress=%s,cli_IPAddress=%s,cli_AuthenticationState=%d,cli_LastDataDownlinkRate=%d,cli_LastDataUplinkRate=%d,cli_SignalStrength=%d,cli_Retransmissions=%d,cli_Active=%d,cli_OperatingStandard=%s,cli_OperatingChannelBandwidth=%s,cli_SNR=%d,cli_InterferenceSources=%s,cli_DataFramesSentAck=%lu,cli_DataFramesSentNoAck=%lu,cli_BytesSent=%lu,cli_BytesReceived=%lu,cli_RSSI=%d,cli_MinRSSI=%d,cli_MaxRSSI=%d,cli_Disassociations=%d,cli_AuthenticationFailures=%d,output_array_size=%d",associated_dev->cli_MACAddress,associated_dev->cli_IPAddress,associated_dev->cli_AuthenticationState,associated_dev->cli_LastDataDownlinkRate,associated_dev->cli_LastDataUplinkRate,associated_dev->cli_SignalStrength,associated_dev->cli_Retransmissions,associated_dev->cli_Active,associated_dev->cli_OperatingStandard,associated_dev->cli_OperatingChannelBandwidth,associated_dev->cli_SNR,associated_dev->cli_InterferenceSources,associated_dev->cli_DataFramesSentAck,associated_dev->cli_DataFramesSentNoAck,associated_dev->cli_BytesSent,associated_dev->cli_BytesReceived,associated_dev->cli_RSSI,associated_dev->cli_MinRSSI,associated_dev->cli_MaxRSSI,associated_dev->cli_Disassociations,associated_dev->cli_AuthenticationFailures,output_array_size);
        sprintf(details,"Value returned is : output_array_size=%u",output_array_size);
        response["result"]="SUCCESS";
        response["details"]=details;
        free(associated_dev);
        return;
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceDiagnosticResult operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        free(associated_dev);
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult ---->Error in execution\n");
        return;
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetNeighboringWiFiDiagnosticResult2
 * Description          : This function invokes WiFi hal api wifi_getNeighboringWiFiDiagnosticResult2

 * @param [in] req-     : radioIndex - radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetNeighboringWiFiDiagnosticResult2(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetNeighboringWiFiDiagnosticResult2 ----->Entry\n");

    wifi_neighbor_ap2_t *neighbor_ap2 = NULL,*pt = NULL;
    unsigned int output_array_size = 0;
    int radioIndex = 0;
    int returnValue = 1;
    unsigned int i = 0;
    char details[1000] = {'\0'};

    radioIndex = req["radioIndex"].asInt();

    returnValue = ssp_WIFIHALGetNeighboringWiFiDiagnosticResult2(radioIndex, &neighbor_ap2, &output_array_size);
    if(0 == returnValue)
    {
        if(neighbor_ap2 != NULL and output_array_size > 0)
        {
	    for(i=0, pt=neighbor_ap2; i<output_array_size; i++, pt++)
	    {
	         if((pt->ap_SSID!="") and (strcmp(pt->ap_SSID,"OutOfService")!=0))
		     break;
	    }
	    if(i==output_array_size)
                sprintf(details, "Value returned is :ap_SSID=%s,ap_BSSID=%s,ap_Mode=%s,ap_Channel=%d,ap_SignalStrength=%d,ap_SecurityModeEnabled=%s,ap_EncryptionMode=%s,ap_OperatingFrequencyBand=%s,ap_SupportedStandards=%s,ap_OperatingStandards=%s,ap_OperatingChannelBandwidth=%s,ap_BeaconPeriod=%d,ap_Noise=%d,ap_BasicDataTransferRates=%s,ap_SupportedDataTransferRates=%s,ap_DTIMPeriod=%d,ap_ChannelUtilization=%d,output_array_size=%u",neighbor_ap2->ap_SSID,neighbor_ap2->ap_BSSID,neighbor_ap2->ap_Mode,neighbor_ap2->ap_Channel,neighbor_ap2->ap_SignalStrength,neighbor_ap2->ap_SecurityModeEnabled,neighbor_ap2->ap_EncryptionMode,neighbor_ap2->ap_OperatingFrequencyBand,neighbor_ap2->ap_SupportedStandards,neighbor_ap2->ap_OperatingStandards,neighbor_ap2->ap_OperatingChannelBandwidth,neighbor_ap2->ap_BeaconPeriod,neighbor_ap2->ap_Noise,neighbor_ap2->ap_BasicDataTransferRates,neighbor_ap2->ap_SupportedDataTransferRates,neighbor_ap2->ap_DTIMPeriod,neighbor_ap2->ap_ChannelUtilization,output_array_size);
           else
	       sprintf(details, "Value returned is :ap_SSID=%s,ap_BSSID=%s,ap_Mode=%s,ap_Channel=%d,ap_SignalStrength=%d,ap_SecurityModeEnabled=%s,ap_EncryptionMode=%s,ap_OperatingFrequencyBand=%s,ap_SupportedStandards=%s,ap_OperatingStandards=%s,ap_OperatingChannelBandwidth=%s,ap_BeaconPeriod=%d,ap_Noise=%d,ap_BasicDataTransferRates=%s,ap_SupportedDataTransferRates=%s,ap_DTIMPeriod=%d,ap_ChannelUtilization=%d,output_array_size=%u",pt->ap_SSID,pt->ap_BSSID,pt->ap_Mode,pt->ap_Channel,pt->ap_SignalStrength,pt->ap_SecurityModeEnabled,pt->ap_EncryptionMode,pt->ap_OperatingFrequencyBand,pt->ap_SupportedStandards,pt->ap_OperatingStandards,pt->ap_OperatingChannelBandwidth,pt->ap_BeaconPeriod,pt->ap_Noise,pt->ap_BasicDataTransferRates,pt->ap_SupportedDataTransferRates,pt->ap_DTIMPeriod,pt->ap_ChannelUtilization,output_array_size);
           response["result"]="SUCCESS";
           response["details"]=details;
           return;
      }
	 else
        {
            response["result"]="SUCCESS";
            response["details"]="No neighbouring Accesspoints found by wifi_getNeighboringWiFiDiagnosticResult2";
            return;
        }
    }
    else
    {
        sprintf(details, "wifi_getNeighboringWiFiDiagnosticResult2 operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetNeighboringWiFiDiagnosticResult2 ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_Down
 * Description          : This function invokes WiFi hal api wifi_down()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_Down (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Down ----->Entry\n");

    int returnValue;
    char details[200] = {'\0'};
    int retValue = 0;
    int radioIndex = 0;
    returnValue = ssp_WIFIHALDown();
    if(0 == returnValue)
       {
            sprintf(details, "wifi_down operation success");
            response["result"]="SUCCESS";
            response["details"]=details;
            retValue = ssp_WIFIHALApplySettings(radioIndex, (char *)"wifi_down");
            if(0 == retValue)
            {
                printf("applyRadioSettings operation success\n");
                return;
            }
            else
            {
                printf("applyRadioSettings operation failed\n");
                return;
            }
       }
    else
       {
            sprintf(details, "wifi_down operation failed");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
       }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Down --->Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_Init
 * Description          : This function invokes WiFi hal api wifi_init()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_Init (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Init ----->Entry\n");

    int returnValue;
    char details[200] = {'\0'};

    returnValue = ssp_wifi_init();
    if(0 == returnValue)
       {
            sprintf(details, "wifi_init operation success");
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
    else
       {
            sprintf(details, "wifi_init operation failed");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
       }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Init --->Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_CreateInitialConfigFiles
 * Description          : This function invokes WiFi hal api wifi_createInitialConfigFiles()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_CreateInitialConfigFiles (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_CreateInitialConfigFiles ----->Entry\n");

    int returnValue;
    char details[200] = {'\0'};
    returnValue = ssp_WIFIHALCreateInitialConfigFiles();
    if(0 == returnValue)
       {
            sprintf(details, "wifi_createInitialConfigFiles operation success");
            response["result"]="SUCCESS";
            response["details"]=details;
       }
    else
       {
            sprintf(details, "wifi_createInitialConfigFiles operation failed");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
       }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_CreateInitialConfigFiles --->Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_PushRadioChannel2
 * Description          : This function invokes WiFi hal api's wifi_pushRadioChannel2()
 * @param [in] req-     : methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_PushRadioChannel2(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushRadioChannel2 ----->Entry\n");
    int returnValue;
    char details[200] = {'\0'};
    char methodName[50] = {'\0'};
    int radioIndex;
    unsigned int channel;
    unsigned int channel_width_MHz;
    unsigned int csa_beacon_count;
    radioIndex = req["radioIndex"].asInt();
    channel = req["channel"].asInt();
    channel_width_MHz = req["channel_width_MHz"].asInt();
    csa_beacon_count = req["csa_beacon_count"].asInt();

    returnValue = ssp_WIFIHALPushRadioChannel2(radioIndex,channel,channel_width_MHz,csa_beacon_count);
    if(0 == returnValue)
    {
        sprintf(details, "%s operation success", methodName);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "%s operation failed", methodName);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForPushRadioChannel2 --->Error in execution\n");
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushRadioChannel2 --->Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetNeighboringWiFiStatus
 * Description          : This function invokes WiFi hal api wifi_getNeighboringWiFiStatus

 * @param [in] req-     : radioIndex - radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetNeighboringWiFiStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetNeighboringWiFiStatus ----->Entry\n");

    wifi_neighbor_ap2_t *neighbor_ap2 = NULL;
    unsigned int output_array_size = 0;
    int radioIndex = 0;
    int returnValue = 1;
    char details[1000] = {'\0'};

    radioIndex = req["radioIndex"].asInt();

    returnValue = ssp_WIFIHALGetNeighboringWiFiStatus(radioIndex, &neighbor_ap2, &output_array_size);
    if(0 == returnValue)
    {
        if(neighbor_ap2 != NULL and output_array_size > 0)
        {
            sprintf(details, "Value returned is :ap_SSID=%s,ap_BSSID=%s,ap_Mode=%s,ap_Channel=%d,ap_SignalStrength=%d,ap_SecurityModeEnabled=%s,ap_EncryptionMode=%s,ap_OperatingFrequencyBand=%s,ap_SupportedStandards=%s,ap_OperatingStandards=%s,ap_OperatingChannelBandwidth=%s,ap_BeaconPeriod=%d,ap_Noise=%d,ap_BasicDataTransferRates=%s,ap_SupportedDataTransferRates=%s,ap_DTIMPeriod=%d,ap_ChannelUtilization=%d,output_array_size=%u",neighbor_ap2->ap_SSID,neighbor_ap2->ap_BSSID,neighbor_ap2->ap_Mode,neighbor_ap2->ap_Channel,neighbor_ap2->ap_SignalStrength,neighbor_ap2->ap_SecurityModeEnabled,neighbor_ap2->ap_EncryptionMode,neighbor_ap2->ap_OperatingFrequencyBand,neighbor_ap2->ap_SupportedStandards,neighbor_ap2->ap_OperatingStandards,neighbor_ap2->ap_OperatingChannelBandwidth,neighbor_ap2->ap_BeaconPeriod,neighbor_ap2->ap_Noise,neighbor_ap2->ap_BasicDataTransferRates,neighbor_ap2->ap_SupportedDataTransferRates,neighbor_ap2->ap_DTIMPeriod,neighbor_ap2->ap_ChannelUtilization,output_array_size);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            response["result"]="SUCCESS";
            response["details"]="No neighbouring WiFi found by wifi_getNeighboringWiFiStatus";
            return;
        }
    }
    else
    {
        sprintf(details, "wifi_getNeighboringWiFiStatus operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetNeighboringWiFiStatus ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRadioChannelStats
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getRadioChannelStats()

 * @param [in] req-     : radioIndex : radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioChannelStats (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioChannelStats ----->Entry\n");
    wifi_channelStats_t channelStats;
    int array_size = 10;
    int radioIndex = 0;
    int returnValue;
    char details[1000] = {'\0'};
    radioIndex = req["radioIndex"].asInt();
    returnValue = ssp_WIFIHALGetRadioChannelStats(radioIndex, &channelStats, array_size);
    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :ch_number=%d,ch_in_pool=%d,ch_noise=%d,ch_radar_noise=%d,ch_max_80211_rssi=%d,ch_non_80211_noise=%d,ch_utilization=%d,ch_utilization_total=%llu,ch_utilization_busy=%llu,ch_utilization_busy_tx=%llu,ch_utilization_busy_rx=%llu,ch_utilization_busy_self=%llu,ch_utilization_busy_ext=%llu",channelStats.ch_number,channelStats.ch_in_pool,channelStats.ch_noise,channelStats.ch_radar_noise,channelStats.ch_max_80211_rssi,channelStats.ch_non_80211_noise,channelStats.ch_utilization,channelStats.ch_utilization_total,channelStats.ch_utilization_busy,channelStats.ch_utilization_busy_tx,channelStats.ch_utilization_busy_rx,channelStats.ch_utilization_busy_self,channelStats.ch_utilization_busy_ext);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getRadioChannelStats operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetRadioChannelStats  --->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_ParamApIndex
 * Description          : This function invokes WiFi hal api's which require apIndex as input
 * @param [in] req-     : apIndex -ap Index value of wifi
                           methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_ParamApIndex(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ParamApIndex------>Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    int returnValue;
    char details[200] = {'\0'};
    strcpy(methodName, req["methodName"].asCString());
    apIndex = req["apIndex"].asInt();
    if(strstr(methodName, "delete")||strstr(methodName, "factoryReset"))
    {
        returnValue = ssp_WIFIHALParamApIndex(apIndex, methodName);
        if(0 == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForParamApIndex --->Error in execution\n");
            return;
        }
    }
    else
        return;
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ParamApIndex --->Exit\n");
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_GetApAssociatedDevice
 * Description          : This function invokes WiFi hal api wifi_getApAssociatedDeviceDiagnosticResult
 * @param [in] req-     : radioIndex - radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDevice(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDevice ----->Entry\n");
    char associated_dev[1024]={0};
    unsigned int output_array_size=1024;
    int apIndex = 1;
    int returnValue;
    char details[2000] = {'\0'};
    apIndex = req["apIndex"].asInt();
    if (associated_dev != NULL)
    {
         DEBUG_PRINT(DEBUG_TRACE,"\n Memory Allocated Successfully");
    }
    else
    {
         DEBUG_PRINT(DEBUG_TRACE, "\n Memory Allocation Failed");
    }
    returnValue = ssp_WIFIHALGetApAssociatedDevice(apIndex, associated_dev, output_array_size);
    if(0 == returnValue)
    {
        sprintf(details,"List of Associated Device: Devices=%s:Value returned is : output_array_size=%d",associated_dev,strlen(associated_dev));
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDevice operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDevice ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_GetApDeviceRSSI
 * Description          : This function invokes WiFi hal api wifi_getApDeviceRSSI
 * @param [in] req-     : apIndex      Access Point index
                                                  MAC          Client MAC in upcase format
                                                  output_RSSI  RSSI is in dbm
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApDeviceRSSI(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApDeviceRSSI ----->Entry\n");
    char methodName[50] = {'\0'};
    int returnValue;
    int apIndex = 0;
    int output_RSSI = 0;
    char MAC[64] = {'\0'};
    char details[200] = {'\0'};
    apIndex = req["apIndex"].asInt();
    strcpy(MAC, req["MAC"].asCString());
    strcpy(methodName, req["methodName"].asCString());
    returnValue = ssp_WIFIHALGetApDeviceRSSI(apIndex, MAC, &output_RSSI, methodName);
    if(0 == returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",output_RSSI);
        sprintf(details, "Value returned is :%d", output_RSSI);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "GetApDeviceRSSI operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApDeviceRSSI  --->Exit\n");
}

/*******************************************************************************************
  *
 * Function Name        : WIFIHAL_DelApAclDevices
 * Description          : This function invokes WiFi hal's delete api Ap Acl Devices *
 * @param [in] req-    : methodName - identifier for the hal api name
                          apIndex - ap index value of wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_DelApAclDevices(IN const Json::Value& req, OUT Json::Value& response){
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_AddorDelApAclDevice------>Entry\n");
    int apIndex = 0;
    int returnValue;
    char details[200] = {'\0'};
    apIndex = req["apIndex"].asInt();
    printf("wifi_del operation to be done\n");
    returnValue = ssp_WIFIHALDelApAclDevices(apIndex);
    if(0 == returnValue)
    {
        sprintf(details, "%s operation success", __FUNCTION__);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "%s operation failed", __FUNCTION__);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForDelApAclDevices --->Error in execution\n");
        return;
    }
}



/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAclDevices
 * Description          : This function invokes WiFi hal api wifi_getApAclDevices
 * @param [in] req-     : apIndex - ap index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAclDevices(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAclDevices ----->Entry\n");
    char mac_addr[512]={'\0'};
    //unsigned int output_array_size;
    int apIndex = 0;
    int returnValue;
    char details[2000] = {'\0'};
    apIndex = req["apIndex"].asInt();
    if (mac_addr != NULL)
    {
         DEBUG_PRINT(DEBUG_TRACE,"\n Memory Allocated Successfully");
    }
    else
    {
         DEBUG_PRINT(DEBUG_TRACE, "\n Memory Allocation Failed");
    }
    returnValue = ssp_WIFIHALGetApAclDevices(apIndex, mac_addr, sizeof(mac_addr));
    if(0 == returnValue)
    {
        sprintf(details,"List of Mac Address; %s ;Value returned is ; output_array_size=%d",mac_addr,strlen(mac_addr));
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getApAclDevices operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAclDevices ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_GetApDeviceTxRxRate
 * Description          : This function invokes WiFi hal apis
 * @param [in] req-     : apIndex      Access Point index
                                                  MAC          Client MAC in upcase format
                                                  output_TxRx in Mbps
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApDeviceTxRxRate(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApDeviceTxRxRate ----->Entry\n");
    char methodName[50] = {'\0'};
    int returnValue;
    int apIndex = 0;
    int output_TxRx = 0;
    char MAC[64] = {'\0'};
    char details[200] = {'\0'};
    apIndex = req["apIndex"].asInt();
    strcpy(MAC, req["MAC"].asCString());
    strcpy(methodName, req["methodName"].asCString());
    returnValue = ssp_WIFIHALGetApDeviceTxRxRate(apIndex, MAC, &output_TxRx, methodName);
    if(0 == returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",output_TxRx);
        sprintf(details, "Value returned is :%d", output_TxRx);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "GetApDeviceTxRxRate operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApDeviceTxRxRate  --->Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_CreateAp
 * Description          : This function invokes WiFi hal api wifi_createAp
 * @param [in] req-     : apIndex     Access Point index
 * @param [in] req-     :  radioIndex  Radio index
 * @param [in] req-     :  essid       SSID Name
 * @param [in] req-     :  hideSsid    True/False, to SSID advertisement enable value

 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
*********************************************************************************************/
void WIFIHAL::WIFIHAL_CreateAp(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_CreateAp ----->Entry\n");
    int apIndex = 1;
    int radioIndex = 1;
    int returnValue;
    char details[1000] = {'\0'};
    char essid[20] = {'\0'};
    unsigned char hideSsid;
    apIndex = req["apIndex"].asInt();
    radioIndex = req["radioIndex"].asInt();
    strcpy(essid, req["essid"].asCString());
    hideSsid = req["hideSsid"].asInt();
    returnValue = ssp_WIFIHAL_CreateAp(apIndex, radioIndex, essid, hideSsid);
    if(0 == returnValue)
    {
        sprintf(details, "wifi_createAp operation SUCCESS");
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_createAp operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_CreateAp ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedDeviceDiagnosticResult3
 * Description          : This function invokes WiFi hal api wifi_getApAssociatedDeviceDiagnosticResult3
 * @param [in] req-     : apIndex - ap index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult3(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult3 ----->Entry\n");
    wifi_associated_dev3_t *associated_dev_array = NULL;
    unsigned int output_array_size = 0;
    int apIndex = 0;
    int returnValue;
    char details[2000] = {'\0'};
    apIndex = req["apIndex"].asInt();

    returnValue = ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult3(apIndex, &associated_dev_array, &output_array_size);
    if(0 == returnValue)
    {
       if(associated_dev_array and output_array_size > 0)
       {
            sprintf(details,"Value returned is : output_array_size=%u, MAC=%02x:%02x:%02x:%02x:%02x:%02x, IP=%s, AuthState=%d, LastDataDownlinkRate=%u, LastDataUplinkRate=%u, SignalStrength=%d, Retransmissions=%u, Active=%d, OperatingStd= %s, OperatingChBw=%s, SNR=%d, interferenceSources=%s, DataFramesSentAck=%lu, cli_DataFramesSentNoAck=%lu, cli_BytesSent=%lu, cli_BytesReceived=%lu, cli_RSSI=%d, cli_MinRSSI=%d, cli_MaxRSSI=%d, Disassociations=%u, AuthFailures=%u, cli_Associations=%llu, PacketsSent=%lu, PacketsReceived=%lu, ErrorsSent=%lu, RetransCount=%lu, FailedRetransCount=%lu, RetryCount=%lu, MultipleRetryCount=%lu, MaxDownlinkRate=%u, MaxUplinkRate=%u",output_array_size,associated_dev_array->cli_MACAddress[0],associated_dev_array->cli_MACAddress[1],associated_dev_array->cli_MACAddress[2],associated_dev_array->cli_MACAddress[3],associated_dev_array->cli_MACAddress[4],associated_dev_array->cli_MACAddress[5],associated_dev_array->cli_IPAddress,associated_dev_array->cli_AuthenticationState,associated_dev_array->cli_LastDataDownlinkRate,associated_dev_array->cli_LastDataUplinkRate,associated_dev_array->cli_SignalStrength,associated_dev_array->cli_Retransmissions,associated_dev_array->cli_Active,associated_dev_array->cli_OperatingStandard,associated_dev_array->cli_OperatingChannelBandwidth,associated_dev_array->cli_SNR,associated_dev_array->cli_InterferenceSources,associated_dev_array->cli_DataFramesSentAck,associated_dev_array->cli_DataFramesSentNoAck,associated_dev_array->cli_BytesSent,associated_dev_array->cli_BytesReceived,associated_dev_array->cli_RSSI,associated_dev_array->cli_MinRSSI,associated_dev_array->cli_MaxRSSI,associated_dev_array->cli_Disassociations,associated_dev_array->cli_AuthenticationFailures,associated_dev_array->cli_Associations,associated_dev_array->cli_PacketsSent,associated_dev_array->cli_PacketsReceived,associated_dev_array->cli_ErrorsSent,associated_dev_array->cli_RetransCount,associated_dev_array->cli_FailedRetransCount,associated_dev_array->cli_RetryCount,associated_dev_array->cli_MultipleRetryCount,associated_dev_array->cli_MaxDownlinkRate,associated_dev_array->cli_MaxUplinkRate);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
       else
       {
           sprintf(details, "wifi_getApAssociatedDeviceDiagnosticResult3 returned empty buffer");
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult3 ----> returned empty buffer\n");
            return;
        }
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceDiagnosticResult3 operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult3 ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_SetApScanFilter
 * Description          : This function invokes WiFi hal's set api, when the value to be set is related to ApScanFilter
 *
 * @param [in] req-    : methodName - identifier for the hal api name
 *                       apIndex - ap index value of wifi
 *                       mode - the mode value to be set
 *                       essid - the string value to be set
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 * ******************************************************************************************/
void WIFIHAL::WIFIHAL_SetApScanFilter(IN const Json::Value& req, OUT Json::Value& response)
{
       DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApScanFilter  ----->Entry\n");
       char methodName[50] = {'\0'};
       int apIndex = 1;
       int returnValue;
       int retValue;
       char details[200] = {'\0'};
       int mode = 0;
       char essid[20] = {'\0'};
       strcpy(methodName, req["methodName"].asCString());
       apIndex = req["apIndex"].asInt();
       mode = req["mode"].asInt();
       strcpy(essid, req["essid"].asCString());
       printf("wifi_set operation to be done\n");
       returnValue = ssp_WIFIHALSetApScanFilter(apIndex, mode, essid, methodName);
       if(0 == returnValue)
       {
               sprintf(details, "%s operation success", methodName);
               response["result"]="SUCCESS";
               response["details"]=details;
       }
       else
       {
               sprintf(details, "%s operation failed", methodName);
               response["result"]="FAILURE";
               response["details"]=details;
               DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForApScanFilter --->Error in execution\n");
               return;
       }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedDeviceStats
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getApAssociatedDeviceStats
 * @param [in] req-     : apIndex : apIndex value of wifi
                        : MAC : DeviceMacAddress - the MacAddress(string)of the device
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceStats(IN const Json::Value& req, OUT Json::Value& response)
{
       DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceStats----->Entry\n");
       wifi_associated_dev_stats_t associated_dev_stats;
       unsigned long long handle;
       int apIndex = 1;
       int i =0;
       char ClientAddress[64] = {'\0'};
       int returnValue;
       mac_address_t MAC;
       unsigned int tmp_MACConv[6];
       char details[2000] = {'\0'};
       apIndex = req["apIndex"].asInt();
       strcpy(ClientAddress, req["MAC"].asCString());
       sscanf(ClientAddress, "%02x:%02x:%02x:%02x:%02x:%02x",
                       &tmp_MACConv[0],
                       &tmp_MACConv[1],
                       &tmp_MACConv[2],
                       &tmp_MACConv[3],
                       &tmp_MACConv[4],
                       &tmp_MACConv[5]);

       for(i =0 ;i <6; i++)
               MAC[i]=(unsigned char)tmp_MACConv[i];

       returnValue = ssp_WIFIHALGetApAssociatedDeviceStats(apIndex, &MAC, &associated_dev_stats, &handle);
       if(0 == returnValue)
       {
               sprintf(details, "Value returned is :cli_rx_bytes=%llu,cli_tx_bytes=%llu,cli_rx_frames=%llu,cli_tx_frames=%llu,cli_rx_retries=%llu,cli_tx_retries=%llu,cli_rx_errors=%llu,cli_tx_errors=%llu,cli_rx_rate=%lf,cli_tx_rate=%lf,cli_rssi_bcn_rssi=%s,cli_rssi_bcn_time_s=%s,cli_rssi_bcn_count=%d,cli_rssi_ack_rssi=%s,cli_rssi_ack_time_s=%s,cli_rssi_ack_count=%d\n",associated_dev_stats.cli_rx_bytes,associated_dev_stats.cli_tx_bytes,associated_dev_stats.cli_rx_frames,associated_dev_stats.cli_tx_frames,associated_dev_stats.cli_rx_retries,associated_dev_stats.cli_tx_retries,associated_dev_stats.cli_rx_errors,associated_dev_stats.cli_tx_errors,associated_dev_stats.cli_rx_rate,associated_dev_stats.cli_tx_rate,associated_dev_stats.cli_rssi_bcn.rssi,associated_dev_stats.cli_rssi_bcn.time_s,associated_dev_stats.cli_rssi_bcn.count,associated_dev_stats.cli_rssi_ack.rssi,associated_dev_stats.cli_rssi_ack.time_s,associated_dev_stats.cli_rssi_ack.count);
               response["result"]="SUCCESS";
               response["details"]=details;
               return;
       }
       else
       {
               sprintf(details, "wifi_getApAssociatedDeviceStats operation failed");
               response["result"]="FAILURE";
               response["details"]=details;
               DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceStats ---->Error in execution\n");
               return;
       }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedDeviceTxStatsResult
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getApAssociatedDeviceTxStatsResult
 * @param [in] req-     : radioIndex : radio Index value of wifi
                        : MAC : DeviceMacAddress - the MacAddress(string)of the device
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceTxStatsResult(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceTxStatsResult ----->Entry\n");
//    wifi_associated_dev_rate_info_tx_stats_t *stats_array = (wifi_associated_dev_rate_info_tx_stats_t*)malloc(sizeof(wifi_associated_dev_rate_info_tx_stats_t));
    wifi_associated_dev_rate_info_tx_stats_t *tx_stats = NULL;
    unsigned int output_array_size = 0;
    unsigned long long handle = 0;
    int radioIndex = 1;
    int returnValue = 0;
    mac_address_t MAC;
    char details[2000] = {'\0'};
    int i =0;
    char ClientAddress[64] = {'\0'};
    unsigned char tmp_MACConv[6] = {0};
    radioIndex = req["radioIndex"].asInt();
    strcpy(ClientAddress, req["MAC"].asCString());
    sscanf(ClientAddress, "%02x:%02x:%02x:%02x:%02x:%02x",
                           &tmp_MACConv[0],
                           &tmp_MACConv[1],
                           &tmp_MACConv[2],
                           &tmp_MACConv[3],
                           &tmp_MACConv[4],
                           &tmp_MACConv[5]);

    for(i =0 ;i <6; i++)
        MAC[i]=(unsigned char)tmp_MACConv[i];

    //returnValue = ssp_WIFIHALGetApAssociatedDeviceTxStatsResult(radioIndex, &MAC, &stats_array, &output_array_size, &handle);
    returnValue = ssp_WIFIHALGetApAssociatedDeviceTxStatsResult(radioIndex, (mac_address_t *)tmp_MACConv, &tx_stats, &output_array_size, &handle);
    if(0 == returnValue)
    {
       if(tx_stats && output_array_size>0)
       {
            sprintf(details,"Value returned is : output_array_size=%d rate %1u/%02u/%1u (%08x) bytes %20llu   msdus %20llu    mpdus %20llu ppdus %20llu retries %20llu attempts %20llu",output_array_size,tx_stats[0].nss,tx_stats[0].mcs,tx_stats[0].bw,tx_stats[0].flags,tx_stats[0].bytes,tx_stats[0].msdus,tx_stats[0].mpdus,tx_stats[0].ppdus,tx_stats[0].retries,tx_stats[0].attempts);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
        else
        {
            sprintf(details,"wifi_getApAssociatedDeviceTxStatsResult returned empty buffer");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
        }
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceTxStatsResult operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceTxStatsResult ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedDeviceRxStatsResult
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getApAssociatedDeviceRxStatsResult
 * @param [in] req-     : radioIndex : radio Index value of wifi
                        : MAC : DeviceMacAddress - the MacAddress(string)of the device
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceRxStatsResult(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceRxStatsResult ----->Entry\n");
    wifi_associated_dev_rate_info_rx_stats_t *stats_array = NULL;
    unsigned int output_array_size = 0;
    unsigned long long handle = 0;
    int radioIndex = 1;
    int returnValue = 0;
    mac_address_t MAC;
    char details[2000] = {'\0'};
    int i =0;
    char ClientAddress[64] = {'\0'};
    unsigned char tmp_MACConv[6];
    radioIndex = req["radioIndex"].asInt();
    strcpy(ClientAddress, req["MAC"].asCString());
    sscanf(ClientAddress, "%02x:%02x:%02x:%02x:%02x:%02x",
                           &tmp_MACConv[0],
                           &tmp_MACConv[1],
                           &tmp_MACConv[2],
                           &tmp_MACConv[3],
                           &tmp_MACConv[4],
                           &tmp_MACConv[5]);

    for(i =0 ;i <6; i++)
        MAC[i]=(unsigned char)tmp_MACConv[i];

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceRxStatsResult MAC %02x:%02x:%02x:%02x:%02x:%02x\n",MAC[0],MAC[1],MAC[2],MAC[3],MAC[4],MAC[5]);
    returnValue = ssp_WIFIHALGetApAssociatedDeviceRxStatsResult(radioIndex, (mac_address_t *)tmp_MACConv, &stats_array, &output_array_size, &handle);
    if(0 == returnValue)
    {
       if(stats_array && output_array_size>0)
       {
            sprintf(details,"Value returned is : output_array_size=%d, rate %1u/%02u/%1u (%08llx)   bytes %20llu   msdus %20llu    mpdus %20llu ppdus %20llu retries %20llu     rssi %20u",output_array_size,stats_array->nss, stats_array->mcs, stats_array->bw, stats_array->flags,stats_array->bytes, stats_array->msdus, stats_array->mpdus, stats_array->ppdus, stats_array->retries, stats_array->rssi_combined);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
       else
       {
           sprintf(details,"wifi_getApAssociatedDeviceRxStatsResult returned empty buffer");
           response["result"]="FAILURE";
           response["details"]=details;
           return;
       }
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceRxStatsResult operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceRxStatsResult ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRadioChannelStats2
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getRadioChannelStats2()

 * @param [in] req-     : radioIndex : radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioChannelStats2 (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioChannelStats ----->Entry\n");
    wifi_channelStats2_t channelStats;
    int radioIndex = 0;
    int returnValue;
    char details[1000] = {'\0'};
    radioIndex = req["radioIndex"].asInt();
    returnValue = ssp_WIFIHALGetRadioChannelStats2(radioIndex, &channelStats);
    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :ch_Frequency=%d,ch_NoiseFloor=%d,ch_Non80211Noise=%d,ch_Max80211Rssi=%d,ch_ObssUtil=%d,ch_SelfBssUtil=%d",channelStats.ch_Frequency,channelStats.ch_NoiseFloor,channelStats.ch_Non80211Noise,channelStats.ch_Max80211Rssi,channelStats.ch_ObssUtil,channelStats.ch_SelfBssUtil);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getRadioChannelStats2 operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetRadioChannelStats2  --->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_StartNeighborScan
 * Description          : This function invokes WiFi hal api wifi_startNeighborScan
 * @param [in] req-     : apIndex - The index of access point array.
 * @param [out]         : scan_mode    - structure with the scan info
                        : dwell_time - Amount of time spent on each channel in the hopping sequence.
                        : chan_num - The channel number.
                        : chan_list - List of channels.
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_StartNeighborScan(IN const Json::Value& req, OUT Json::Value& response)
{
       DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_StartNeighborScan ----->Entry\n");
       wifi_neighborScanMode_t scan_mode = WIFI_RADIO_SCAN_MODE_NONE;;
       int scan_mode_tmp = 0;
       int dwell_time = 0;
       unsigned int chan_num = 0;
       unsigned int chan_list[100] = {0};
       int apIndex = 1;
       int returnValue = 1;
       char details[1000] = {'\0'};

        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_StartNeighborScan: getting param\n");
       apIndex = req["apIndex"].asInt();
       dwell_time = req["dwell_time"].asInt();
//     chan_num = req["chan_num"].asInt();
//     chan_list = req["chan_list"].asInt();
       scan_mode_tmp = req["scan_mode"].asInt();

       /*Setting the scan mode */
       if(scan_mode_tmp == WIFI_RADIO_SCAN_MODE_NONE)
               scan_mode = WIFI_RADIO_SCAN_MODE_NONE;
       else if (scan_mode_tmp == WIFI_RADIO_SCAN_MODE_FULL)
               scan_mode = WIFI_RADIO_SCAN_MODE_FULL;
       else if (scan_mode_tmp == WIFI_RADIO_SCAN_MODE_ONCHAN)
               scan_mode = WIFI_RADIO_SCAN_MODE_ONCHAN;
       else if (scan_mode_tmp ==  WIFI_RADIO_SCAN_MODE_OFFCHAN)
               scan_mode = WIFI_RADIO_SCAN_MODE_OFFCHAN;
       else if (scan_mode_tmp == WIFI_RADIO_SCAN_MODE_SURVEY)
               scan_mode = WIFI_RADIO_SCAN_MODE_SURVEY;
       else
               printf("\nScan_mode is not valid\n");

       returnValue = ssp_WIFIHALStartNeighborScan(apIndex, scan_mode, dwell_time, chan_num, chan_list);
       if(0 == returnValue)
       {
               sprintf(details, "wifi_startNeighborScan operation success");
               response["result"]="SUCCESS";
               response["details"]=details;
               return;
       }
       else
       {
               sprintf(details, "wifi_startNeighborScan operation failed");
               response["result"]="FAILURE";
               response["details"]=details;
               DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_StartNeighborScan ---->Error in execution\n");
               return;
       }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetBSSColorValue
 * Description          : This function invokes WiFi hal's wifi_getBSSColor() api
 * @param [in] req-    :  radioIndex - radio index value of wifi
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetBSSColorValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBSSColorValue --->Entry\n");
    int radioIndex = 0;
    unsigned char color = 0;
    int returnValue = 1;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());

    printf("wifi_getBSSColor operation to be done\n");
    //paramType is set as NULL for negative test scenarios, for NULL pointer checks
    if(strcmp(paramType, "NULL"))
        returnValue = ssp_WIFIHALGetBSSColorValue(radioIndex, &color);
    else
        returnValue = ssp_WIFIHALGetBSSColorValue(radioIndex, NULL);
    if(0 == returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",color);
        sprintf(details, "Value returned is :%d", color);
        response["result"]="SUCCESS";
        response["details"]=details;
	return;
    }
    else
    {
        sprintf(details, "WIFIHAL_GetBSSColorValue operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBSSColorValue --->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_ApplyGASConfiguration
 * Description          : This function invokes WiFi hal api wifi_applyGASConfiguration()
 * @param [in] req-     : Values correspond to the dot11GASAdvertisementEntry field definitions
                          AdvertisementID
			  PauseForServerResponse
			  ResponseTimeout
			  ComeBackDelay
			  ResponseBufferingTime
			  QueryResponseLengthLimit
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_ApplyGASConfiguration(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ApplyGASConfiguration ----->Entry\n");
    wifi_GASConfiguration_t GASConfiguration = {0};
    int returnValue = 1;
    char details[500] = {'\0'};
    GASConfiguration.AdvertisementID = req["advertisementID"].asInt();
    GASConfiguration.PauseForServerResponse = req["pauseForServerResponse"].asInt();
    GASConfiguration.ResponseTimeout = req["responseTimeout"].asInt();
    GASConfiguration.ComeBackDelay = req["comeBackDelay"].asInt();
    GASConfiguration.ResponseBufferingTime = req["responseBufferingTime"].asInt();
    GASConfiguration.QueryResponseLengthLimit = req["queryResponseLengthLimit"].asInt();
    returnValue = ssp_WIFIHALApplyGASConfiguration(&GASConfiguration);
    if(0 == returnValue)
    {
        sprintf(details, "WIFIHAL_ApplyGASConfiguration operation success");
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "WIFIHAL_ApplyGASConfiguration operation failure");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ApplyGASConfiguration ---->Error in execution\n");
        return;
    }
}

/**************************************************************************
 * Function Name        : CreateObject
 * Description  : This function will be used to create a new object for the
 *                class "WIFIHAL".
*
 **************************************************************************/
extern "C" WIFIHAL* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new WIFIHAL(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/
bool WIFIHAL::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"WIFIHAL shutting down\n");
    return TEST_SUCCESS;
}

/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(WIFIHAL *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying WIFIHAL object\n");
    delete stubobj;
}
/*********************************************************************************************
 * Function Name        :  WIFIHAL_GetApAssociatedDeviceTidStatsResult
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getApAssociatedDeviceTidStatsResult
 * @param [in] req-     : radioIndex : radio Index value of wifi
                        : MAC : DeviceMacAddress - the MacAddress(string)of the device
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceTidStatsResult(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceTidStatsResult ----->Entry\n");
    int i =0,n=0;
    int radioIndex = 1;
    wifi_associated_dev_tid_stats_t tid_stats;
    wifi_associated_dev_tid_entry_t *s = NULL;
    char ClientAddress[64] = {'\0'};
    unsigned char tmp_MACConv[6];
    radioIndex = req["radioIndex"].asInt();
    unsigned long long handle = 0;
    unsigned char ac =0 ,tid =0;
    unsigned long long ewma_time_ms = 0,sum_time_ms = 0,num_msdus = 0 ;
    int returnValue = 1;
    char details[1000] = {'\0'};
    mac_address_t MAC;
    strcpy(ClientAddress, req["MAC"].asCString());
    sscanf(ClientAddress, "%02x:%02x:%02x:%02x:%02x:%02x",
                           &tmp_MACConv[0],
                           &tmp_MACConv[1],
                           &tmp_MACConv[2],
                           &tmp_MACConv[3],
                           &tmp_MACConv[4],
                           &tmp_MACConv[5]);
    for(i =0 ;i <6; i++)
        MAC[i]=(unsigned char)tmp_MACConv[i];
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceTidStatsResult MAC %02x:%02x:%02x:%02x:%02x:%02x\n",MAC[0],MAC[1],MAC[2],MAC[3],MAC[4],MAC[5]);
    returnValue = ssp_WIFIHALGetApAssociatedDeviceTidStatsResult(radioIndex, (mac_address_t *)tmp_MACConv, & tid_stats, &handle);
    if(0 == returnValue)
    {

          n = (sizeof(tid_stats.tid_array)/sizeof(tid_stats.tid_array[0]));
          printf ("Size of array is %d ",n);
          if ( n > 0)
          {
              for (i=0; i< n; i++)
              {
                  s = &tid_stats.tid_array[i];
                  printf("ac : %s,tid:%s,ewma_time_ms:%llu,sum_time_ms:%llu,num_msdus:%llu",s->ac,s->tid,s->ewma_time_ms,s->sum_time_ms,s->num_msdus);
                  ac = s->ac;
                  tid = s->tid;
                  ewma_time_ms = s->ewma_time_ms;
                  sum_time_ms = s->sum_time_ms;
                  num_msdus = s->num_msdus;
              }
              sprintf(details," Value returned is : ac : %s,tid:%s,ewma_time_ms:%llu,sum_time_ms:%llu,num_msdus:%llu",ac,tid,ewma_time_ms,sum_time_ms,num_msdus);
              response["result"]="SUCCESS";
              response["details"]=details;

          }
          else
          {
             sprintf(details,"wifi_getApAssociatedDeviceTidStatsResult returned empty buffer");
             response["result"]="FAILURE";
             response["details"]=details;

          }
          return;

    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceTidStatsResult operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceTidStatsResult  ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetBandSteeringLog
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getBandSteeringLog
 * @param [in] req-     : record_index: index value of record
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation

 * @@param[out] pSteeringTime      Returns the UTC time in seconds
 * @param[out] pSteeringReason    Returns the predefined steering trigger reason
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetBandSteeringLog(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBandSteeringLog ----->Entry\n");
    char pClientMAC[64] = {'\0'};
    int  pSourceSSIDIndex = 0;
    int  pDestSSIDIndex = 0;
    int  pSteeringReason = 0 ;
    int  record_index;
    char details[1000] = {'\0'};
    int returnValue = 1;
    unsigned long pSteeringTime;
    record_index = req["record_index"].asInt();

    returnValue = ssp_WIFIHALGetBandSteeringLog(record_index,&pSteeringTime,pClientMAC,&pSourceSSIDIndex,&pDestSSIDIndex,&pSteeringReason);
    if(0 == returnValue)
    {
      sprintf(details,"Value returned is : pSteeringTime: %lu ,pSteeringReason : %d, pClientMAC :%s,pSourceSSIDIndex :%s ,pDestSSIDIndex :%s",pSteeringTime,pSteeringReason,pClientMAC,pSourceSSIDIndex,pDestSSIDIndex);
      response["result"]="SUCCESS";
      response["details"]=details;
      return;
    }
    else
    {
        sprintf(details, "wifi_getBandSteeringLog operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBandSteeringLog---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name                    : WIFIHAL_GetApAssociatedDeviceDiagnosticResult2
 * Description                      : This function invokes WiFi hal api wifi_getApAssociatedDeviceDiagnosticResult2
 * @param[in] apIndex               :Access Point index
 * @param [out] response            : filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult2(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult2 ----->Entry\n");
    int apIndex = 1;
    wifi_associated_dev2_t *associated_dev2 = NULL;
    unsigned int dev_cnt = 0;
    char details[2000] = {'\0'};
    int returnValue = 1;
    apIndex  = req["apIndex"].asInt();

    returnValue = ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult2(apIndex,&associated_dev2,&dev_cnt);
    if(0 == returnValue)
    {
        if(associated_dev2 && dev_cnt > 0)
        {
             sprintf(details, "Value returned is : dev count:%u,cli_IPAddress :%s",dev_cnt,associated_dev2->cli_IPAddress);
             response["result"]="SUCCESS";
             response["details"]=details;
        }
        else
        {
           sprintf(details,"wifi_getApAssociatedDeviceDiagnosticResult2 returned empty buffer");
           response["result"]="FAILURE";
           response["details"]=details;

        }

        if(associated_dev2)
           free(associated_dev2);

        return;
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceDiagnosticResult2 failed");
        response["result"]="FAILURE";
        response["details"]=details;
        free(associated_dev2);
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult2 ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name                    : WIFIHAL_GetRadioMode
 * Description                      : This function invokes WiFi HAL API wifi_getRadioMode()
 * @param[in] radioIndex            : WiFi Radio index
 * @param [out] response            : filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioMode(IN const Json::Value& req, OUT Json::Value& response)
{

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioMode ----->Entry\n");
    int returnValue = -1;
    int radioIndex = 1;
    char details[1000] = {'\0'};
    radioIndex  = req["radioIndex"].asInt();
    unsigned int puremode = 0;
    char opStandard[32] = {'\0'};

    returnValue = ssp_WIFIHALGetRadioMode(radioIndex,opStandard,&puremode);
    if(0 == returnValue)
    {
        sprintf(details, "Value returned is : puremode:%d, opStandard:%s",puremode,opStandard);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getRadioMode failed");
        response["result"]="FAILURE";
        response["details"]=details;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioMode ----->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name                    : WIFIHAL_SetRadioMode
 * Description                      : This function invokes WiFi HAL API wifi_setRadioMode()
 * @param[in] radioIndex            : WiFi Radio index
              chnmode               : Channel Mode
              pure mode             : Operation standard values
 * @param [out] response            : filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SetRadioMode(IN const Json::Value& req, OUT Json::Value& response)
{

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetRadioMode ----->Entry\n");
    int returnValue = -1;
    int radioIndex = 1;
    unsigned int puremode = 1;
    char chnMode[32] = {'\0'};
    radioIndex  = req["radioIndex"].asInt();
    strcpy(chnMode,req["chnmode"].asCString());
    puremode = req["puremode"].asInt();

    returnValue = ssp_WIFIHALSetRadioMode(radioIndex,chnMode,puremode);
    if(0 == returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n wifi_setRadioMode operation success\n");
        returnValue = ssp_WIFIHALApplySettings(radioIndex, (char *)"setRadioMode");
        if(0 == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\napplyRadioSettings operation success\n");
            response["result"]="SUCCESS";
            response["details"]="wifi_setRadioMode operation success";
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"\napplyRadioSettings operation failed\n");
            response["result"]="FAILURE";
            response["details"]="wifi_applyRadioSettings failed";
        }

    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n wifi_setRadioMode operation success\n");
        response["result"]="FAILURE";
        response["details"]="wifi_setRadioMode operation Failed";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetRadioMode ----->Exit\n");
    return;
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApIndexFromName
 * Description          : This function invokes WiFi hal api wifi_getApIndexFromName()
 * @param [in] req-     : param     - the ssid name to be passed
 * @param [out] response - Access Point index, to be returned
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApIndexFromName (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApIndexFromName ----->Entry\n");
    int returnValue;
    int output = 1;
    char ssidName[10] = {'\0'};
    char details[200] = {'\0'};
    strcpy(ssidName, req["param"].asCString());
    returnValue = ssp_WIFIHALGetApIndexFromName(ssidName, &output);
    if(0 == returnValue)
       {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",output);
            sprintf(details, "Value returned is :%d", output);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
    else
       {
            sprintf(details, "GetApIndexFromName operation failed");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
       }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApIndexFromName  --->Exit\n");
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_GetAssociatedDeviceDetail
 * Description          : This function invokes WiFi hal api wifi_getAssociatedDeviceDetail
 * @param [in] req-     : apIndex - access point index
                          devIndex - Index of associated device
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetAssociatedDeviceDetail(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAssociatedDeviceDetail ----->Entry\n");
    int apIndex = 0;
    int devIndex = 0;
    wifi_device_t dev;
    int returnValue = 1;
    char details[2000] = {'\0'};

    apIndex = req["apIndex"].asInt();
    devIndex = req["devIndex"].asInt();

    returnValue = ssp_WIFIHALGetAssociatedDeviceDetail(apIndex, devIndex, &dev);
    if(0 == returnValue)
    {
        sprintf(details,"Associated Device MAC Address : %02x:%02x:%02x:%02x:%02x:%02x Auth State : %d Rx Rate : %d Tx Rate : %d", dev.wifi_devMacAddress[0], dev.wifi_devMacAddress[1],
                        dev.wifi_devMacAddress[2], dev.wifi_devMacAddress[3], dev.wifi_devMacAddress[4], dev.wifi_devMacAddress[5],
                        dev.wifi_devAssociatedDeviceAuthentiationState, dev.wifi_devTxRate, dev.wifi_devRxRate);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getAssociatedDeviceDetail operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAssociatedDeviceDetail ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_GetBasicTrafficStats
 * Description          : This function invokes WiFi hal api wifi_getBasicTrafficStats
 * @param [in] req-     : apIndex - access point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetBasicTrafficStats(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBasicTrafficStats ----->Entry\n");
    int apIndex = 0;
    wifi_basicTrafficStats_t stats={0};
    int returnValue = 1;
    char details[2000] = {'\0'};

    apIndex = req["apIndex"].asInt();

    returnValue = ssp_WIFIHALGetBasicTrafficStats(apIndex, &stats);
    if(0 == returnValue)
    {
        sprintf(details,"BasicTrafficStats Details- wifi_BytesSent %lu, wifi_BytesReceived %lu, wifi_PacketsSent %lu, wifi_PacketsReceived %lu, wifi_Associations %lu", stats.wifi_BytesSent, stats.wifi_BytesReceived, stats.wifi_PacketsSent, stats.wifi_PacketsReceived, stats.wifi_Associations);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getBasicTrafficStats operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBasicTrafficStats ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_GetWifiTrafficStats
 * Description          : This function invokes WiFi hal api wifi_getWifiTrafficStats
 * @param [in] req-     : apIndex - access point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetWifiTrafficStats(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetWifiTrafficStats ----->Entry\n");
    int apIndex = 0;
    wifi_trafficStats_t stats={0};
    int returnValue = 1;
    char details[2000] = {'\0'};

    apIndex = req["apIndex"].asInt();

    returnValue = ssp_WIFIHALGetWifiTrafficStats(apIndex, &stats);
    if(0 == returnValue)
    {
        sprintf(details,"WifiTrafficStats Details- wifi_ErrorsSent %lu, wifi_ErrorsReceived %lu, wifi_UnicastPacketsSent %lu, wifi_UnicastPacketsReceived %lu, wifi_DiscardedPacketsSent %lu, wifi_DiscardedPacketsReceived %lu, wifi_MulticastPacketsSent %lu, wifi_MulticastPacketsReceived %lu", stats.wifi_ErrorsSent, stats.wifi_ErrorsReceived, stats.wifi_UnicastPacketsSent, stats.wifi_UnicastPacketsReceived, stats.wifi_DiscardedPacketsSent, stats.wifi_DiscardedPacketsReceived, stats.wifi_MulticastPacketsSent, stats.wifi_MulticastPacketsReceived);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getWifiTrafficStats operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetWifiTrafficStats ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_SteeringClientDisconnect
 * Description          : This function invokes WiFi hal api wifi_steering_clientDisconnect
 * @param [in] req-     : steeringgroupIndex - Wifi Steering Group index
			  apIndex - access point index
			  clientMAC - The Client's MAC address
			  disconnectType - Disconnect Type
			  reason - Reason code to provide in deauth/disassoc frame
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SteeringClientDisconnect(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientDisconnect ----->Entry\n");
    int apIndex = 0;
    unsigned int steeringgroupIndex = 0;
    char mac[20] = {'\0'};
    mac_address_t client_mac;
    unsigned int macInt[6];
    wifi_disconnectType_t type;
    unsigned int reason = 0;
    int returnValue = 1;
    char details[2000] = {'\0'};
    int k = 0;

    apIndex = req["apIndex"].asInt();
    steeringgroupIndex = req["steeringgroupIndex"].asInt();
    type = (wifi_disconnectType_t)req["disconnectType"].asInt();
    reason = (unsigned int)req["reason"].asInt();
    strcpy(mac, req["clientMAC"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &macInt[0], &macInt[1], &macInt[2], &macInt[3], &macInt[4], &macInt[5]);
    for (k = 0; k < 6; k++) {
         client_mac[k] = (unsigned char)macInt[k];
    }

    returnValue = ssp_WIFIHALSteeringClientDisconnect(steeringgroupIndex, apIndex, client_mac, type, reason);
    if(0 == returnValue)
    {
        sprintf(details, "wifi_steering_clientDisconnect operation is success");
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_steering_clientDisconnect operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientDisconnect ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_SteeringClientSet
 * Description          : This function invokes WiFi hal api wifi_steering_clientSet
 * @param [in] req-     : steeringgroupIndex - Wifi Steering Group index
                          apIndex - access point index
                          clientMAC - The Client's MAC address
                          rssiProbeHWM - Probe response RSSI high water mark
                          rssiProbeLWM - Probe response RSSI low water mark
                          rssiAuthHWM - Auth response RSSI high water mark
                          rssiAuthLWM - Auth response RSSI low water mark
                          rssiInactXing - Inactive RSSI crossing threshold
                          rssiHighXing - High RSSI crossing threshold
                          rssiLowXing - Low RSSI crossing threshold
                          authRejectReason - Inactive RSSI crossing threshold
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SteeringClientSet(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientSet ----->Entry\n");
    int apIndex = 0;
    unsigned int steeringgroupIndex = 0;
    char mac[20] = {'\0'};
    mac_address_t client_mac;
    unsigned int macInt[6];
    wifi_steering_clientConfig_t cli_cfg = {0};
    int returnValue = 1;
    char details[2000] = {'\0'};
    int k = 0;

    apIndex = req["apIndex"].asInt();
    steeringgroupIndex = req["steeringgroupIndex"].asInt();
    cli_cfg.rssiProbeHWM = req["rssiProbeHWM"].asInt();
    cli_cfg.rssiProbeLWM = req["rssiProbeLWM"].asInt();
    cli_cfg.rssiAuthHWM = req["rssiAuthHWM"].asInt();
    cli_cfg.rssiAuthLWM = req["rssiAuthLWM"].asInt();
    cli_cfg.rssiInactXing = req["rssiInactXing"].asInt();
    cli_cfg.rssiHighXing = req["rssiHighXing"].asInt();
    cli_cfg.rssiLowXing = req["rssiLowXing"].asInt();
    cli_cfg.authRejectReason = req["authRejectReason"].asInt();
    strcpy(mac, req["clientMAC"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &macInt[0], &macInt[1], &macInt[2], &macInt[3], &macInt[4], &macInt[5]);
    for (k = 0; k < 6; k++) {
         client_mac[k] = (unsigned char)macInt[k];
    }

    returnValue = ssp_WIFIHALSteeringClientSet(steeringgroupIndex, apIndex, client_mac, &cli_cfg);
    if(0 == returnValue)
    {
        sprintf(details, "wifi_steering_clientSet operation is success");
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_steering_clientSet operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientSet ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_SteeringClientRemove
 * Description          : This function invokes WiFi hal api wifi_steering_clientRemove
 * @param [in] req-     : steeringgroupIndex - Wifi Steering Group index
                          apIndex - access point index
                          clientMAC - The Client's MAC address
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SteeringClientRemove(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientRemove ----->Entry\n");
    int apIndex = 0;
    unsigned int steeringgroupIndex = 0;
    char mac[20] = {'\0'};
    mac_address_t client_mac;
    unsigned int macInt[6];
    int returnValue = 1;
    char details[2000] = {'\0'};
    int k = 0;

    apIndex = req["apIndex"].asInt();
    steeringgroupIndex = req["steeringgroupIndex"].asInt();
    strcpy(mac, req["clientMAC"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &macInt[0], &macInt[1], &macInt[2], &macInt[3], &macInt[4], &macInt[5]);
    for (k = 0; k < 6; k++) {
         client_mac[k] = (unsigned char)macInt[k];
    }

    returnValue = ssp_WIFIHALSteeringClientRemove(steeringgroupIndex, apIndex, client_mac);
    if(0 == returnValue)
    {
        sprintf(details, "wifi_steering_clientRemove operation is success");
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_steering_clientRemove operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientRemove ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_GetBTMClientCapabilityList
 * Description          : This function invokes WiFi hal api wifi_getBTMClientCapabilityList
 * @param [in] req-     : apIndex - access point index
                          count - no: of MAC entries being passed
                          clientMAC - The Client's MAC address
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetBTMClientCapabilityList(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBTMClientCapabilityList ----->Entry\n");
    int apIndex = 0;
    int count = 0;
    char mac[20] = {'\0'};
    mac_address_t client_mac;
    wifi_BTMCapabilities_t btm_caps;
    unsigned int macInt[6];
    int returnValue = 1;
    char details[2000] = {'\0'};
    int k = 0;

    apIndex = req["apIndex"].asInt();
    btm_caps.entries = req["count"].asInt();
    strcpy(mac, req["clientMAC"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &macInt[0], &macInt[1], &macInt[2], &macInt[3], &macInt[4], &macInt[5]);
    for (k = 0; k < 6; k++) {
         client_mac[k] = (unsigned char)macInt[k];
         btm_caps.peer[0][k] = client_mac[k];
    }

    returnValue = ssp_WIFIHALGetBTMClientCapabilityList(apIndex, &btm_caps);
    if(0 == returnValue)
    {
        sprintf(details, "wifi_getBTMClientCapabilityList output is: Entries %d, MAC %x:%x:%x:%x:%x:%x, Capability %d", btm_caps.entries, btm_caps.peer[0][0],  btm_caps.peer[0][1], btm_caps.peer[0][2], btm_caps.peer[0][3], btm_caps.peer[0][4], btm_caps.peer[0][5], btm_caps.capability[0]);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getBTMClientCapabilityList operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBTMClientCapabilityList ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_GetApRoamingConsortiumElement
 * Description          : This function invokes WiFi hal api wifi_getApRoamingConsortiumElement
 * @param [in] req-     : apIndex - access point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApRoamingConsortiumElement(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApRoamingConsortiumElement ----->Entry\n");

    wifi_roamingConsortiumElement_t roam = {0};
    int apIndex = 0;
    int returnValue = 1;
    char details[2000] = {'\0'};
    char tempstr[33] = {'\0'};
    int elemCount = 0;
    int index = 0;
    int len= 0;

    if(&req["apIndex"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();

    returnValue = ssp_WIFIHALGetApRoamingConsortiumElement(apIndex, &roam);
    if(0 == returnValue)
    {
        elemCount = (int)roam.wifiRoamingConsortiumCount;
        sprintf(details, "wifi_getApRoamingConsortiumElement output is: EntryCount %d", elemCount);
        for(index=0; index<3; ++index)
        {
                tempstr[0] = '\0';
                for(len=0; len<roam.wifiRoamingConsortiumLen[index] && len<16; ++len) {
                        sprintf(&tempstr[len*2], "%02x", roam.wifiRoamingConsortiumOui[index][len]);
                }
                sprintf(details + strlen(details), ", OUI[%d] %s, LenOfOUI[%d] %u", index, tempstr, index, roam.wifiRoamingConsortiumLen[index]);
        }
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getApRoamingConsortiumElement operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApRoamingConsortiumElement ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_PushApRoamingConsortiumElement
 * Description          : This function invokes WiFi hal api wifi_pushApRoamingConsortiumElement
 * @param [in] req-     : apIndex - access point index
                        : ouiCount - no: of OUIs to be set
                        : ouiList - OUI values to be est
                        : ouiLen - length of each OUI value
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_PushApRoamingConsortiumElement(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApRoamingConsortiumElement ----->Entry\n");

    wifi_roamingConsortiumElement_t roam = {0};
    int apIndex = 0;
    int returnValue = 1;
    char details[2000] = {'\0'};
    char tempOui[110] = {'\0'};
    char tempOuiLen[10] = {'\0'};
    char *token = NULL;
    int index = 0;
    int len = 0;
    unsigned int ouiInt = 0;

    if(&req["apIndex"]==NULL || &req["ouiList"]==NULL || &req["ouiCount"]==NULL || &req["ouiLen"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    apIndex = req["apIndex"].asInt();
    strcpy(tempOui, req["ouiList"].asCString());
    roam.wifiRoamingConsortiumCount = req["ouiCount"].asInt();
    strcpy(tempOuiLen, req["ouiLen"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\n tempOui = %s, ouiCount = %u, tempOuiLen = %s\n",tempOui, roam.wifiRoamingConsortiumCount, tempOuiLen);

    //split and save the input oui lengths' list
    token = strtok(tempOuiLen, ",");
    while (token != NULL && index < 3)
    {
        roam.wifiRoamingConsortiumLen[index]=atoi(token);
        DEBUG_PRINT(DEBUG_TRACE,"\n wifiRoamingConsortiumOuiLen[%d] = %u\n", index, roam.wifiRoamingConsortiumLen[index]);
        index++;
        token = strtok(NULL, ",");
    }

    //split and save the input oui list
    token = strtok(tempOui, ",");
    index = 0;
    while (token != NULL && index < 3)
    {
        len=0;
        while (sscanf(&token[len*2], "%2x", &ouiInt) != EOF and len<15)
        {
            roam.wifiRoamingConsortiumOui[index][len] = (unsigned char)ouiInt;
            DEBUG_PRINT(DEBUG_TRACE,"\n roam.wifiRoamingConsortiumOui[%d][%d] = %u\n", index, len, ouiInt);
            len++;
        }
        index++;
        token = strtok(NULL, ",");
    }

    returnValue = ssp_WIFIHALPushApRoamingConsortiumElement(apIndex, &roam);
    if(0 == returnValue)
    {
        sprintf(details, "wifi_pushApRoamingConsortiumElement operation is success");
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_pushApRoamingConsortiumElement operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApRoamingConsortiumElement ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
*
 * Function Name        : WIFIHAL_GetApInterworkingElement
 * Description          : This function invokes WiFi hal get api wifi_getApInterworkingElement()
 * @param [in] req-     : RadioIndex. 0 - 2.4GHz, 1 - 5GHz
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApInterworkingElement (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApInterworkingElement ----->Entry\n");
    wifi_InterworkingElement_t element;
    int radioIndex = 0;
    int returnValue;
    char details[1000] = {'\0'};
    if(&req["radioIndex"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    radioIndex = req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Get operation requested\n");
    returnValue = ssp_WIFIHALGetApInterworkingElement(radioIndex, &element);
    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :interworkingEnabled=%d, accessNetworkType=%d, internetAvailable=%d, asra=%d, esra=%d, uesa=%d, venueOptionPresent=%d, venueType=%d, venueGroup=%d, hessOptionPresent=%d, hessid=%s", element.interworkingEnabled, element.accessNetworkType, element.internetAvailable, element.asra, element.esra, element.uesa, element.venueOptionPresent, element.venueType, element.venueGroup, element.hessOptionPresent, element.hessid);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
	response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getApInterworkingElement operation failed");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetApInterworkingElement  --->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_PushApInterworkingElement
 * Description          : This function invokes WiFi hal push api wifi_pushApInterworkingElement()
 * @param [in] req-     : radioIndex - radio Index value of wifi
                          interworkingEnabled - if Interworking Service is enabled or disabled(0/1)
                          accessNetworkType - Network Type(0-15), specifies the type of network - Optional parameter
                          internetAvailable - Internet available or not - Optional parameter
                          asra - Optional parameter
                          esra - Optional parameter
                          uesa - Optional parameter
                          venueOptionPresent - Optional parameter - True when venue information has been provided
                          venueType - Optional parameter
                          venueGroup - Optional parameter
                          hessOptionPresent - Optional parameter - True when hessid is present
                          hessid - Optional parameter - Mac Address
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_PushApInterworkingElement (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApInterworkingElement ----->Entry\n");
    wifi_InterworkingElement_t element;
    int radioIndex = 0;
    int returnValue;
    char details[500] = {'\0'};
    if(&req["radioIndex"]== NULL || &req["interworkingEnabled"]== NULL || &req["accessNetworkType"]== NULL || &req["internetAvailable"]== NULL || &req["asra"]== NULL || &req["esra"]== NULL || &req["uesa"]== NULL || &req["venueOptionPresent"]== NULL || &req["venueType"]== NULL || &req["venueGroup"]== NULL &req["hessOptionPresent"]== NULL || &req["hessid"]== NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    radioIndex = req["radioIndex"].asInt();
    element.interworkingEnabled = req["interworkingEnabled"].asBool();
    element.accessNetworkType = req["accessNetworkType"].asUInt();
    element.internetAvailable = req["internetAvailable"].asBool();
    element.asra = req["asra"].asBool();
    element.esra = req["esra"].asBool();
    element.uesa = req["uesa"].asBool();
    element.venueOptionPresent = req["venueOptionPresent"].asBool();
    element.venueType = req["venueType"].asInt();
    element.venueGroup = req["venueGroup"].asInt();
    element.hessOptionPresent = req["hessOptionPresent"].asBool();
    strcpy(element.hessid, req["hessid"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n Invoking wifi_pushApInterworkingElement\n");
    returnValue = ssp_WIFIHALPushApInterworkingElement(radioIndex, &element);
    if(0 == returnValue)
    {
        sprintf(details, "wifi_pushApInterworkingElement was invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_pushApInterworkingElement was not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApInterworkingElement ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_EnableCSIEngine
 * Description          : This function invokes WiFi hal api wifi_enableCSIEngine()
 * @param [in] req-     : apIndex - WiFi Access Point Index value
                          MacAddress - Mac Address of client device connected
                          enable - Whether CSI data collection is enabled or not
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_EnableCSIEngine(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_EnableCSIEngine ----->Entry\n");
    int apIndex = 0;
    mac_address_t MAC;
    char mac[20] = {'\0'};
    unsigned int tmp_MACConv[6] = {0};
    unsigned char enable;
    int returnValue = 0;
    char details[500] = {'\0'};

    if(&req["apIndex"]==NULL || &req["MacAddress"]==NULL || &req["enable"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    enable = req["enable"].asInt();
    strcpy(mac, req["MacAddress"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &tmp_MACConv[0], &tmp_MACConv[1], &tmp_MACConv[2], &tmp_MACConv[3], &tmp_MACConv[4], &tmp_MACConv[5]);

    for(int index = 0 ; index <6; index++)
    {
        MAC[index]=(unsigned char)tmp_MACConv[index];
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d, MAC : %s, Enable : %d\n", apIndex, MAC, enable);
    returnValue = ssp_WIFIHALEnableCSIEngine(apIndex, MAC, &enable);

    if(0 == returnValue)
    {
        sprintf(details, "wifi_enableCSIEngine was invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_enableCSIEngine was not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_EnableCSIEngine ---->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_EnableCSIEngine ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_SendDataFrame
 * Description          : This function invokes WiFi hal api wifi_sendDataFrame()
 * @param [in] req-     : apIndex - Index of VAP
 *                        MacAddress - MAC address of the station associated in this VAP
 *                        length - length of data
 *                        insert_llc - whether LLC header should be inserted. If set to TRUE, HAL implementation MUST insert the following bytes before type field. DSAP = 0xaa, SSAP = 0xaa, Control = 0x03, followed by 3 bytes each = 0x00
 *                        protocol - ethernet protocol
 *                        priority - priority of the frame with which scheduler should transmit the frame
 *
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SendDataFrame(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SendDataFrame ----->Entry\n");
    int apIndex = 0;
    mac_address_t sta;
    char mac[20] = {'\0'};
    unsigned int tmp_MACConv[6] = {0};
    unsigned char data = 0;
    unsigned int length = 0;
    unsigned char insert_llc = 0;
    unsigned int protocol = 0;
    unsigned int priority = 0;
    wifi_data_priority_t prio = wifi_data_priority_be;
    int returnValue = 0;
    char details[500] = {'\0'};

    if(&req["apIndex"]==NULL || &req["MacAddress"]==NULL || &req["length"]==NULL || &req["protocol"]==NULL || &req["priority"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    length = req["length"].asInt();
    protocol = req["protocol"].asInt();
    insert_llc = req["insert_llc"].asInt();
    priority = req["priority"].asInt();
    prio = wifi_data_priority_t(priority);
    strcpy(mac, req["MacAddress"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &tmp_MACConv[0], &tmp_MACConv[1], &tmp_MACConv[2], &tmp_MACConv[3], &tmp_MACConv[4], &tmp_MACConv[5]);

    for(int index = 0 ; index <6; index++)
    {
        sta[index]=(unsigned char)tmp_MACConv[index];
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d, MAC : %s, Length : %d, Insert_LLC : %d, Protocol : %d, Priority : %s\n", apIndex, sta, length, insert_llc, protocol, prio);
    returnValue = ssp_WIFIHALSendDataFrame(apIndex, sta, &data, length, &insert_llc, protocol, prio);

    if(0 == returnValue)
    {
        sprintf(details, "wifi_sendDataFrame was invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_sendDataFrame was not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SendDataFrame ---->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SendDataFrame ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetVAPTelemetry
 * Description          : This function invokes WiFi hal get api wifi_getVAPTelemetry()
 * @param [in] req-     : apIndex - Access Point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetVAPTelemetry(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetVAPTelemetry ----->Entry\n");
    wifi_VAPTelemetry_t VAPTelemetry;
    int apIndex = 0;
    int returnValue = 0;
    char details[1000] = {'\0'};

    if (&req["apIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    returnValue = ssp_WIFIHALGetVAPTelemetry(apIndex, &VAPTelemetry);

    if(0 == returnValue)
    {
        sprintf(details, "\n wifi_getVAPTelemetry was invoked successfully; Value returned is : txOverflow = %lu", VAPTelemetry.txOverflow);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "\n wifi_getVAPTelemetry not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetVAPTelemetry  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetVAPTelemetry ---->Exiting\n");
    return;
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_GetRadioVapInfoMap
 * Description          : This function invokes WiFi hal api wifi_getRadioVapInfoMap
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioVapInfoMap(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioVapInfoMap ----->Entry\n");
    wifi_radio_index_t radioIndex = 0;
    wifi_vap_info_map_t map;
    int returnValue = 1;
    char details[2000] = {'\0'};

    if(&req["apIndex"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["apIndex"].asInt();

    returnValue = ssp_WIFIHALGetRadioVapInfoMap(radioIndex,&map);
    if(0 == returnValue)
    {

        sprintf(details,"The numner of Radio maps are : %lu, ",map.num_vaps);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getRadioVapInfoMap operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioVapInfoMap ---->Error in execution\n");
        return;
    }
	DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioVapInfoMap ----->Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_SetNeighborReports
 * Description          : This function invokes WiFi hal api wifi_setNeighborReports()
 * @param [in] req-     : apIndex - Index of VAP
 *                        reports - Number of reports in the in_NeighborReports set
 *                        bssid - MAC address of the connected client
 *                        info - information on the bssid
 *                        opClass - regulatory data
 *                        channel - radio channel value
 *                        phyTable - physical type
 *
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SetNeighborReports(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetNeighborReports ----->Entry\n");
    unsigned int apIndex = 0;
    unsigned int reports = 0;
    bssid_t MacAddress;
    char mac[20] = {'\0'};
    unsigned int tmp_MACConv[6] = {0};
    unsigned char info = 0;
    unsigned char opClass = 0;
    unsigned char channel = 0;
    unsigned char phyTable = 0;
    wifi_NeighborReport_t neighborReports;
    int max_count = 6;
    int returnValue = 0;
    char details[500] = {'\0'};

    if(&req["apIndex"]==NULL || &req["reports"]==NULL || &req["bssid"]==NULL || &req["info"]==NULL || &req["opClass"]==NULL || &req["channel"]==NULL || &req["phyTable"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    reports = req["reports"].asInt();
    neighborReports.info = req["info"].asInt();
    neighborReports.opClass = req["opClass"].asInt();
    neighborReports.channel = req["channel"].asInt();
    neighborReports.phyTable = req["phyTable"].asInt();

    strcpy(mac, req["bssid"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &tmp_MACConv[0], &tmp_MACConv[1], &tmp_MACConv[2], &tmp_MACConv[3], &tmp_MACConv[4], &tmp_MACConv[5]);
    for(int index = 0 ; index < max_count; index++)
    {
        MacAddress[index]=(unsigned char)tmp_MACConv[index];
    }
    memcpy(neighborReports.bssid, MacAddress, max_count);

    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d, Number of reports : %d, BSSID : %s, Info : %d, opClass : %d, Channel : %d, PhyTable : %d\n", apIndex, reports, neighborReports.bssid, neighborReports.info, neighborReports.opClass, neighborReports.channel, neighborReports.phyTable);
    returnValue = ssp_WIFIHALSetNeighborReports(apIndex, reports, &neighborReports);

    if(0 == returnValue)
    {
        sprintf(details, "wifi_setNeighborReports was invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_setNeighborReports was not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetNeighborReports ---->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetNeighborReports ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedClientDiagnosticResult
 * Description          : This function invokes WiFi hal api wifi_getApAssociatedClientDiagnosticResult
 * @param [in] req-     : apIndex - ap index of the wifi
 *                      : mac_addr - client MAC address
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedClientDiagnosticResult(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedClientDiagnosticResult ----->Entry\n");
    wifi_associated_dev3_t *dev_conn = (wifi_associated_dev3_t *) malloc(sizeof(wifi_associated_dev3_t));
    memset(dev_conn, 0, sizeof(wifi_associated_dev3_t));
    int apIndex = 0;
    char MAC[64] = {'\0'};
    int returnValue = 0;
    char details[2000] = {'\0'};

    if(&req["apIndex"]==NULL || &req["mac_addr"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    strcpy(MAC, req["mac_addr"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d, MAC : %s\n", apIndex, MAC);
    returnValue = ssp_WIFIHALGetApAssociatedClientDiagnosticResult(apIndex, MAC, dev_conn);

    if(0 == returnValue)
    {
        sprintf(details,"Client Diagnostic Result : MAC=%02x:%02x:%02x:%02x:%02x:%02x, IP=%s, AuthState=%d, LastDataDownlinkRate=%u, LastDataUplinkRate=%u, SignalStrength=%d, Retransmissions=%u, Active=%d, OperatingStd= %s, OperatingChBw=%s, SNR=%d, interferenceSources=%s, DataFramesSentAck=%lu, cli_DataFramesSentNoAck=%lu, cli_BytesSent=%lu, cli_BytesReceived=%lu, cli_RSSI=%d, cli_MinRSSI=%d, cli_MaxRSSI=%d, Disassociations=%u, AuthFailures=%u, cli_Associations=%llu, PacketsSent=%lu, PacketsReceived=%lu, ErrorsSent=%lu, RetransCount=%lu, FailedRetransCount=%lu, RetryCount=%lu, MultipleRetryCount=%lu, MaxDownlinkRate=%u, MaxUplinkRate=%u", dev_conn->cli_MACAddress[0], dev_conn->cli_MACAddress[1], dev_conn->cli_MACAddress[2], dev_conn->cli_MACAddress[3], dev_conn->cli_MACAddress[4], dev_conn->cli_MACAddress[5], dev_conn->cli_IPAddress, dev_conn->cli_AuthenticationState, dev_conn->cli_LastDataDownlinkRate, dev_conn->cli_LastDataUplinkRate, dev_conn->cli_SignalStrength, dev_conn->cli_Retransmissions, dev_conn->cli_Active, dev_conn->cli_OperatingStandard, dev_conn->cli_OperatingChannelBandwidth, dev_conn->cli_SNR, dev_conn->cli_InterferenceSources, dev_conn->cli_DataFramesSentAck, dev_conn->cli_DataFramesSentNoAck, dev_conn->cli_BytesSent, dev_conn->cli_BytesReceived, dev_conn->cli_RSSI, dev_conn->cli_MinRSSI, dev_conn->cli_MaxRSSI, dev_conn->cli_Disassociations, dev_conn->cli_AuthenticationFailures, dev_conn->cli_Associations, dev_conn->cli_PacketsSent, dev_conn->cli_PacketsReceived, dev_conn->cli_ErrorsSent, dev_conn->cli_RetransCount, dev_conn->cli_FailedRetransCount, dev_conn->cli_RetryCount, dev_conn->cli_MultipleRetryCount, dev_conn->cli_MaxDownlinkRate, dev_conn->cli_MaxUplinkRate);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedClientDiagnosticResult operation failed");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedClientDiagnosticResult ---->Error in execution\n");
    }

    free(dev_conn);
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedClientDiagnosticResult ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetAPCapabilities
 * Description          : This function invokes WiFi hal get api wifi_getAPCapabilities()
 * @param [in] req-     : apIndex - Access Point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetAPCapabilities(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAPCapabilities ----->Entry\n");
    wifi_ap_capabilities_t *APCapabilities = (wifi_ap_capabilities_t *)malloc(sizeof(wifi_ap_capabilities_t));
    memset(APCapabilities, 0, sizeof(wifi_ap_capabilities_t));
    int apIndex = 0;
    int returnValue = 0;
    char details[1000] = {'\0'};
    char output[1000] = {'\0'};

    if (&req["apIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);
    returnValue = ssp_WIFIHALGetAPCapabilities(apIndex, APCapabilities, output);

    if(0 == returnValue)
    {
        sprintf(details, "wifi_getAPCapabilities invoked successfully; Details : %s", output);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "\n wifi_getAPCapabilities not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAPCapabilities  --->Error in execution\n");
    }

    free(APCapabilities);
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAPCapabilities ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetAvailableBSSColor
 * Description          : This function invokes WiFi hal's wifi_getAvailableBSSColor() api
 * @param [in] req-     : radioIndex - radio index value of wifi
 *                        maxNumberColors - WL_COLOR_MAX_VALUE from wlioctl.h
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetAvailableBSSColor(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAvailableBSSColor --->Entry\n");
    int radioIndex = 0;
    int maxNumberColors = 0;
    unsigned char colorList[200] = {0};
    int numColorReturned = 0;
    int returnValue = 0;
    char details[1000] = {'\0'};
    char details_add[200] = {'\0'};
    int iteration = 0;

    if(&req["radioIndex"]==NULL || &req["maxNumberColors"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["radioIndex"].asInt();
    maxNumberColors = req["maxNumberColors"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\n radioIndex : %d, maxNumberColors : %d", radioIndex, maxNumberColors);
    returnValue = ssp_WIFIHALGetAvailableBSSColor(radioIndex, maxNumberColors, colorList, &numColorReturned);

    if(0 == returnValue)
    {
        sprintf(details, "WIFIHAL_GetAvailableBSSColor operation success :: NumColorReturned : %d, ", numColorReturned);

        if (numColorReturned > 0)
        {
            sprintf(details_add, " Available BSSColor List = ");
            strcat(details, details_add);
            for (iteration = 0; iteration < numColorReturned; iteration++)
            {
                sprintf(details_add, "%d ", colorList[iteration]);
                strcat(details, details_add);
            }
        }
        else
        {
             sprintf(details_add, " Available BSSColor List is Empty\n");
             strcat(details, details_add);
        }

        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "WIFIHAL_GetAvailableBSSColor operation failed");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAvailableBSSColor --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAvailableBSSColor ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetFTMobilityDomainID
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
 *                        get /set is related to FTMobilityDomainID
 * @param [in] req-     : methodName - HAL API name (wifi_getFTMobilityDomainID or wifi_setFTMobilityDomainID)
 *                        apIndex - Access Point index
 *                        radioIndex - WiFi Radio Index
 *                        mobilityDomain - Value of the FT Mobility Domain for this AP to get/set
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetFTMobilityDomainID(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTMobilityDomainID  ----->Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    int radioIndex = 0;
    int returnValue = 0;
    int retValue = 0;
    char details[200] = {'\0'};
    int size = 64;
    unsigned char mobilityDomain[64] = {'\0'};
    int mobilityDomain_Int = 0;
    int * mobilityDomain_IntPtr = NULL;
    char details_add[200] = {'\0'};

    if(&req["apIndex"]==NULL || &req["methodName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(methodName, req["methodName"].asCString());
    apIndex = req["apIndex"].asInt();

    if(!strncmp(methodName, "set",3))
    {
        printf("wifi_setFTMobilityDomainID operation to be done\n");

        if(&req["mobilityDomain"]==NULL || &req["radioIndex"]==NULL)
        {
            response["result"]="FAILURE";
            response["details"]="NULL parameter as input argument";
            return;
        }

        mobilityDomain_Int = req["mobilityDomain"].asInt();
        mobilityDomain_IntPtr = &mobilityDomain_Int;
        memcpy(mobilityDomain, (char *)mobilityDomain_IntPtr, size);
        radioIndex = req["radioIndex"].asInt();

        DEBUG_PRINT(DEBUG_TRACE,"\n apIndex : %d", apIndex);
        DEBUG_PRINT(DEBUG_TRACE,"\n Mobility Domain ID[0] : 0x%x, Mobility Domain ID[1] : 0x%x", mobilityDomain[0], mobilityDomain[1]);
        returnValue = ssp_WIFIHALGetOrSetFTMobilityDomainID(apIndex, mobilityDomain, methodName);

        if(0 == returnValue)
        {
            sprintf(details_add, "wifi_%s operation success;", methodName);
            strcat(details, details_add);

            retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
            if(0 == retValue)
            {
                sprintf(details_add, " applyRadioSettings operation success");
                strcat(details, details_add);
            }
            else
            {
                sprintf(details_add, " applyRadioSettings operation failed");
                strcat(details, details_add);
            }

            response["result"]="SUCCESS";
            response["details"]=details;
        }
        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTMobilityDomainID --->Error in execution\n");
        }
    }
    else
    {
        printf("wifi_getFTMobilityDomainID operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetFTMobilityDomainID(apIndex, mobilityDomain, methodName);

        if(0 == returnValue)
        {
            sprintf(details, "Mobility Domain ID[0] : 0x%x, Mobility Domian ID[1] : 0x%x", mobilityDomain[0], mobilityDomain[1]);
            DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
            response["result"]="SUCCESS";
            response["details"]=details;
        }
        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTMobilityDomainID --->Error in execution\n");
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTMobilityDomainID ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetFTR0KeyHolderID
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
 *                        get /set is related to FTR0KeyHolderID
 * @param [in] req-     : methodName - HAL API name (wifi_getFTR0KeyHolderID or wifi_setFTR0KeyHolderID)
 *                        apIndex - Access Point index
 *                        radioIndex - WiFi Radio Index
 *                        KeyHolderID - Value of the FTR0 Key Holder ID for this AP to get/set
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetFTR0KeyHolderID(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTR0KeyHolderID  ----->Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    int radioIndex = 0;
    int returnValue = 0;
    int retValue = 0;
    char details[2000] = {'\0'};
    unsigned char key_id[64] = {'\0'};
    char KeyHolderID[64] = {'\0'};
    char details_add[1000] = {'\0'};

    if(&req["apIndex"]==NULL || &req["methodName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    strcpy(methodName, req["methodName"].asCString());

    if(!strncmp(methodName, "set",3))
    {
        printf("wifi_setFTR0KeyHolderID operation to be done\n");

        if(&req["KeyHolderID"]==NULL || &req["radioIndex"]==NULL)
        {
            response["result"]="FAILURE";
            response["details"]="NULL parameter as input argument";
            return;
        }

        strcpy(KeyHolderID, req["KeyHolderID"].asCString());
        memcpy(&key_id[0], KeyHolderID, strlen(KeyHolderID));
        radioIndex = req["radioIndex"].asInt();

        DEBUG_PRINT(DEBUG_TRACE,"\n apIndex : %d", apIndex);
        DEBUG_PRINT(DEBUG_TRACE,"\n Key Holder ID : %s", KeyHolderID);
        DEBUG_PRINT(DEBUG_TRACE,"\n Key_ID : %p\n", &key_id[0]);

        if(key_id[0] == '\0')
        {
            DEBUG_PRINT(DEBUG_TRACE, "Key Holder ID[0] : 0x%x", key_id[0]);
        }
        else
        {
            for(int index = 0; key_id[index] != '\0'; index++)
            {
                DEBUG_PRINT(DEBUG_TRACE, "Key Holder ID[%d] : 0x%x", index, key_id[index]);
            }
        }

        returnValue = ssp_WIFIHALGetOrSetFTR0KeyHolderID(apIndex, &key_id[0], methodName);

        if(0 == returnValue)
        {
            sprintf(details_add, "wifi_%s operation success;", methodName);
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", details_add);
            strcat(details, details_add);
            retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);

            if(0 == retValue)
            {
                sprintf(details_add, " applyRadioSettings operation success");
                DEBUG_PRINT(DEBUG_TRACE,"\n%s", details_add);
                strcat(details, details_add);
            }
            else
            {
                sprintf(details_add, " applyRadioSettings operation failed");
                DEBUG_PRINT(DEBUG_TRACE,"\n%s", details_add);
                strcat(details, details_add);
            }
            response["result"]="SUCCESS";
            response["details"]=details;
        }

        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTR0KeyHolderID --->Error in execution\n");
        }
    }

    else
    {
        printf("wifi_getFTR0KeyHolderID operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetFTR0KeyHolderID(apIndex, &key_id[0], methodName);

        if(0 == returnValue)
        {
            sprintf(details_add, "FTR0 Key Holder ID Details -");
            strcat(details, details_add);

            if(key_id[0] == '\0')
            {
                sprintf(details_add, " Key Holder ID[0] : 0x%x", key_id[0]);
                strcat(details, details_add);
            }
            else
            {
                for(int index = 0; key_id[index] != '\0'; index++)
                {
                    sprintf(details_add, " Key Holder ID[%d] : 0x%x", index, key_id[index]);
                    strcat(details, details_add);
                }
            }

            DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
            response["result"]="SUCCESS";
            response["details"]=details;
        }
        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTR0KeyHolderID --->Error in execution\n");
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTR0KeyHolderID ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRMCapabilities
 * Description          : This function invokes WiFi hal api wifi_getRMCapabilities
 * @param [in] req-     : peer - connected client mac address
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRMCapabilities(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRMCapabilities ----->Entry\n");
    mac_address_t peer;
    int max_size = 6;
    char mac[20] = {'\0'};
    unsigned int tmp_MACConv[6] = {0};
    unsigned char out_Capabilities[5] = {'\0'};
    int returnValue = 0;
    char details[2000] = {'\0'};

    if(&req["peer"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(mac, req["peer"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &tmp_MACConv[0], &tmp_MACConv[1], &tmp_MACConv[2], &tmp_MACConv[3], &tmp_MACConv[4], &tmp_MACConv[5]);

    for(int index = 0 ; index < max_size; index++)
    {
        peer[index]=(unsigned char)tmp_MACConv[index];
    }

    DEBUG_PRINT(DEBUG_TRACE,"\nPeer : %s\n", peer);
    returnValue = ssp_WIFIHALGetRMCapabilities(peer, out_Capabilities);

    if(0 == returnValue)
    {
        sprintf(details,"wifi_getRMCapabilities operation success : capabilities[0] : %02X, capabilities[1] : %02X, capabilities[2] : %02X, capabilities[3] :  %02X, capabilities[4] : %02X ", out_Capabilities[0], out_Capabilities[1], out_Capabilities[2], out_Capabilities[3], out_Capabilities[4]);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getRMCapabilities operation failed");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRMCapabilities ---->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRMCapabilities ---->Exiting\n");
    return;
}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApSecurity
 * Description          : This function invokes WiFi hal get api wifi_getApSecurity()
 * @param [in] req-     : apIndex - Access Point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApSecurity(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApSecurity ----->Entry\n");
    wifi_vap_security_t security;
    int apIndex = 0;
    int returnValue = 0;
    char details[2000] = {'\0'};
    char output[2000] = {'\0'};

    if (&req["apIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);

    returnValue = ssp_WIFIHALGetApSecurity(apIndex, &security, output);

    if(0 == returnValue)
    {
        sprintf(details, "wifi_getApSecurity invoked successfully; Details : %s", output);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getApSecurity not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApSecurity  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApSecurity ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_SetApSecurity
 * Description          : This function invokes WiFi hal get api wifi_setApSecurity()
 * @param [in] req-     : apIndex - Access Point index
 *                        mode - Access Point security mode
 *                        mfp - MFP value disabled, optional or required
 *                        encr - Access Point encryption method
 *                        key_type - Access Point key type
 *                        key - Access Point key according to the key type
 *                        wpa3_transition_disable - If Access Point mode is WPA3-Personal-Transition,
 *                        then wpa3_transition_enable will hold its enable state
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SetApSecurity(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApSecurity ----->Entry\n");
    wifi_vap_security_t security;
    int apIndex = 0;
    int mode = 0;
    int returnValue = 0;
    char details[2000] = {'\0'};

    if (&req["apIndex"] == NULL || &req["mode"] == NULL || &req["mfp"] == NULL || &req["encr"] == NULL || &req["key_type"] == NULL || &req["key"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);

    mode = req["mode"].asInt();
    switch(mode)
    {
        case 1 :
                security.mode = wifi_security_mode_none;
                break;
        case 2 :
                security.mode = wifi_security_mode_wep_64;
                break;
        case 4 :
                security.mode = wifi_security_mode_wep_128;
                break;
        case 8 :
                security.mode = wifi_security_mode_wpa_personal;
                break;
        case 16 :
                security.mode = wifi_security_mode_wpa2_personal;
                break;
        case 32 :
                security.mode = wifi_security_mode_wpa_wpa2_personal;
                break;
        case 64 :
                security.mode = wifi_security_mode_wpa_enterprise;
                break;
        case 128 :
                security.mode = wifi_security_mode_wpa2_enterprise;
                break;
        case 256 :
                security.mode = wifi_security_mode_wpa_wpa2_enterprise;
                break;
        case 512 :
                security.mode = wifi_security_mode_wpa3_personal;
                break;
        case 1024 :
                security.mode = wifi_security_mode_wpa3_transition;

                if (&req["wpa3_transition_disable"] == NULL)
                {
                    response["result"]="FAILURE";
                    response["details"]="WPA3 Transition Disable parameter is not received when security mode is WPA3-Personal-Transition";
                    return;
                }
                else
                {
                    security.wpa3_transition_disable = req["wpa3_transition_disable"].asBool();
                    DEBUG_PRINT(DEBUG_TRACE,"\n WPA3 Transition Disable : %s", security.wpa3_transition_disable ? "true" : "false");
                }
                break;
        case 2048 :
                security.mode = wifi_security_mode_wpa3_enterprise;
                break;
        default :
               response["result"]="FAILURE";
               response["details"]="Invalid Mode";
               return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n Security Mode : 0x%04x", security.mode);

#if defined(WIFI_HAL_VERSION_3)
    security.mfp = (wifi_mfp_cfg_t)req["mfp"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n MFP : %d", security.mfp);
#endif

    security.encr = (wifi_encryption_method_t)req["encr"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Encryption Method : %d", security.encr);

    security.u.key.type = (wifi_security_key_type_t)req["key_type"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Key Type : %d", security.u.key.type);

    strcpy(security.u.key.key, req["key"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\n Key : %s", security.u.key.key);

    returnValue = ssp_WIFIHALSetApSecurity(apIndex, &security);

    if(0 == returnValue)
    {
        sprintf(details, "wifi_setApSecurity invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_setApSecurity not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApSecurity  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApSecurity ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApWpsConfiguration
 * Description          : This function invokes WiFi hal get api wifi_getApWpsConfiguration()
 * @param [in] req-     : apIndex - Access Point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApWpsConfiguration(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApWpsConfiguration ----->Entry\n");
    wifi_wps_t wpsConfig;
    int apIndex = 0;
    int returnValue = 0;
    char details[2000] = {'\0'};
    char output[2000] = {'\0'};

    if (&req["apIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);

    returnValue = ssp_WIFIHALGetApWpsConfiguration(apIndex, &wpsConfig, output);

    if(0 == returnValue)
    {
        sprintf(details, "wifi_getApWpsConfiguration invoked successfully; Details : %s", output);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getApWpsConfiguration not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApWpsConfiguration  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApWpsConfiguration ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_SetApWpsConfiguration
 * Description          : This function invokes WiFi hal get api wifi_setApWpsConfiguration()
 * @param [in] req-     : apIndex - Access Point index
 *                        enable - Access Point WPS enable status
 *                        pin - Access Point WPS PIN
 *                        num_methods - Number of WPS configuration methods
 *                        methods - Access Point WPS methods
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SetApWpsConfiguration(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApWpsConfiguration ----->Entry\n");
    wifi_wps_t wpsConfig;
    int apIndex = 0;
    int radioIndex = 0;
    int returnValue = 0;
    int retValue = 0;
    char details[2000] = {'\0'};
    char detailsAdd[1000] = {'\0'};

    if (&req["apIndex"] == NULL || &req["enable"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);

    wpsConfig.enable = req["enable"].asBool();
    DEBUG_PRINT(DEBUG_TRACE,"\n WPS Mode : %d", wpsConfig.enable);

    if (wpsConfig.enable)
    {
        if (&req["pin"] == NULL || &req["methods"] == NULL || &req["radioIndex"] == NULL)
        {
            response["result"]="FAILURE";
            response["details"]="If WPS mode is set to enable, WPS PIN and WPS Configuration methods cannot be NULL parameters";
            return;
        }

        radioIndex = req["radioIndex"].asInt();
        DEBUG_PRINT(DEBUG_TRACE,"\n radioIndex : %d", radioIndex);

        strcpy(wpsConfig.pin, req["pin"].asCString());
        DEBUG_PRINT(DEBUG_TRACE,"\n WPS PIN : %s", wpsConfig.pin);

        wpsConfig.methods = (wifi_onboarding_methods_t)req["methods"].asInt();
        DEBUG_PRINT(DEBUG_TRACE,"\n WPS Methods : 0x%04x", wpsConfig.methods);
    }

    returnValue = ssp_WIFIHALSetApWpsConfiguration(apIndex, &wpsConfig);

    if(0 == returnValue)
    {
        sprintf(detailsAdd, "wifi_setApWpsConfiguration operation success;");
        DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
        strcat(details, detailsAdd);

        retValue = ssp_WIFIHALApplySettings(radioIndex, (char *)"setApWpsConfiguration");

        if(0 == retValue)
        {
            sprintf(detailsAdd, " applyRadioSettings operation success");
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            strcat(details, detailsAdd);
            response["result"]="SUCCESS";
        }
        else
        {
            sprintf(detailsAdd, " applyRadioSettings operation failed");
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            strcat(details, detailsAdd);
            response["result"]="FAILURE";
        }

        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_setApWpsConfiguration not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApWpsConfiguration  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApWpsConfiguration ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetFTR1KeyHolderID
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
 *                        get /set is related to FTR1KeyHolderID
 * @param [in] req-     : methodName - HAL API name (wifi_getFTR1KeyHolderID or wifi_setFTR1KeyHolderID)
 *                        apIndex - Access Point index
 *                        radioIndex - WiFi Radio Index
 *                        KeyHolderID - Value of the FTR1 Key Holder ID for this AP to get/set
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetFTR1KeyHolderID(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTR1KeyHolderID  ----->Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    int radioIndex = 0;
    int returnValue = 0;
    int retValue = 0;
    char details[2000] = {'\0'};
    unsigned char keyId[64] = {'\0'};
    char keyHolderID[64] = {'\0'};
    char detailsAdd[1000] = {'\0'};

    if(&req["apIndex"]==NULL || &req["methodName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    strcpy(methodName, req["methodName"].asCString());

    if(!strncmp(methodName, "set",3))
    {
        printf("wifi_setFTR1KeyHolderID operation to be done\n");

        if(&req["KeyHolderID"]==NULL || &req["radioIndex"]==NULL)
        {
            response["result"]="FAILURE";
            response["details"]="NULL parameter as input argument";
            return;
        }

        strcpy(keyHolderID, req["KeyHolderID"].asCString());
        memcpy(&keyId[0], keyHolderID, strlen(keyHolderID));

        radioIndex = req["radioIndex"].asInt();

        DEBUG_PRINT(DEBUG_TRACE,"\n apIndex : %d", apIndex);
        DEBUG_PRINT(DEBUG_TRACE,"\n Key Holder ID : %s", keyHolderID);
        DEBUG_PRINT(DEBUG_TRACE,"\n Key_ID : %p\n", &keyId[0]);

        if(keyId[0] == '\0')
        {
            DEBUG_PRINT(DEBUG_TRACE, "Key Holder ID : 0x%x", keyId[0]);
        }
        else
        {
            for(int index = 0; index < 64 && keyId[index] != '\0'; index++)
            {
                DEBUG_PRINT(DEBUG_TRACE, "Key Holder ID[%d] : 0x%x", index, keyId[index]);
            }
        }

        returnValue = ssp_WIFIHALGetOrSetFTR1KeyHolderID(apIndex, &keyId[0], methodName);

        if(0 == returnValue)
        {
            sprintf(detailsAdd, "wifi_%s operation success;", methodName);
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            strcat(details, detailsAdd);
            retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);

            if(0 == retValue)
            {
                sprintf(detailsAdd, " applyRadioSettings operation success");
                DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
                strcat(details, detailsAdd);
                response["result"]="SUCCESS";
            }
            else
            {
                sprintf(detailsAdd, " applyRadioSettings operation failed");
                DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
                strcat(details, detailsAdd);
                response["result"]="FAILURE";
            }

            response["details"]=details;
        }
        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTR1KeyHolderID --->Error in execution\n");
        }
    }
    else
    {
        printf("wifi_getFTR1KeyHolderID operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetFTR1KeyHolderID(apIndex, &keyId[0], methodName);

        if(0 == returnValue)
        {
            sprintf(detailsAdd, "FTR1 Key Holder ID Details -");
            strcat(details, detailsAdd);

            if(keyId[0] == '\0')
            {
                sprintf(detailsAdd, " Key Holder ID[0] : 0x%x", keyId[0]);
                strcat(details, detailsAdd);
            }
            else
            {
                for(int index = 0; index < 64 && keyId[index] != '\0' ; index++)
                {
                    sprintf(detailsAdd, " Key Holder ID[%d] : 0x%x", index, keyId[index]);
                    strcat(details, detailsAdd);
                }
            }

            DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
            response["result"]="SUCCESS";
            response["details"]=details;
        }
        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTR1KeyHolderID --->Error in execution\n");
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTR1KeyHolderID ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_SetBSSColor
 * Description          : This function invokes WiFi hal's wifi_setBSSColor() api
 * @param [in] req-     : radioIndex - radio index value of wifi
 *                        color - color value to be set
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SetBSSColor(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetBSSColor --->Entry\n");
    int radioIndex = 0;
    unsigned char color = 0;
    int retValue = 0;
    int returnValue = 0;
    char details[2000] = {'\0'};
    char detailsAdd[1000] = {'\0'};

    if(&req["radioIndex"]==NULL || &req["color"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["radioIndex"].asInt();
    color = req["color"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n radioIndex : %d, color : %d", radioIndex, color);

    returnValue = ssp_WIFIHALSetBSSColor(radioIndex, color);

    if(0 == returnValue)
    {
        sprintf(detailsAdd, "wifi_setBSSColor operation success;");
        DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
        strcat(details, detailsAdd);

        retValue = ssp_WIFIHALApplySettings(radioIndex, (char *)"setBSSColor");

        if(0 == retValue)
        {
            sprintf(detailsAdd, " applyRadioSettings operation success");
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            strcat(details, detailsAdd);
            response["result"]="SUCCESS";
        }
        else
        {
            sprintf(detailsAdd, " applyRadioSettings operation failed");
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            strcat(details, detailsAdd);
            response["result"]="FAILURE";
        }

        response["details"]=details;
    }
    else
    {
        sprintf(details, "WIFIHAL_SetBSSColor operation failed");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetBSSColor --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetBSSColor ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_PushApFastTransitionConfig
 * Description          : This function invokes WiFi hal's Push FT API
 * @param [in] req-     : apIndex - Access Point index
 *                        radioIndex - WiFi Radio Index
 *                        support - FT support(Disabled/Full/Adaptive)
 *                        mobilityDomain - Value of the FT Mobility Domain for this AP to set
 *                        overDS - FT Over DS activated(Enabled/Disabled)
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_PushApFastTransitionConfig(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApFastTransitionConfig  ----->Entry\n");
    int apIndex = 0;
    int radioIndex = 0;
    int returnValue = 0;
    int retValue = 0;
    wifi_FastTransitionConfig_t ftCfg;
    char detailsAdd[200] = {'\0'};
    char details[200] = {'\0'};

    if(&req["apIndex"]==NULL || &req["support"]==NULL || &req["mobilityDomain"]==NULL || &req["overDS"]==NULL || &req["radioIndex"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n apIndex : %d", apIndex);

    ftCfg.support = (wifi_fastTrasitionSupport_t)req["support"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n FT Support : %d", ftCfg.support);

    ftCfg.mobilityDomain = req["mobilityDomain"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Mobility Domain ID : 0x%04x", ftCfg.mobilityDomain);

    ftCfg.overDS = req["overDS"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n FT Over DS : %d", ftCfg.overDS);

    radioIndex = req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n radioIndex : %d", radioIndex);

    returnValue = ssp_WIFIHALPushApFastTransitionConfig(apIndex, &ftCfg);

    if(0 == returnValue)
    {
        sprintf(detailsAdd, "wifi_PushApFastTransitionConfig operation success;");
        strcat(details, detailsAdd);
        retValue = ssp_WIFIHALApplySettings(radioIndex, (char *)"PushApFastTransitionConfig");

        if(0 == retValue)
        {
            sprintf(detailsAdd, " applyRadioSettings operation success");
            strcat(details, detailsAdd);
            response["result"]="SUCCESS";
        }
        else
        {
            sprintf(detailsAdd, " applyRadioSettings operation failed");
            strcat(details, detailsAdd);
            response["result"]="FAILURE";
        }

        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_PushApFastTransitionConfig operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApFastTransitionConfig --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApFastTransitionConfig ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetMuEdca
 * Description          : This function invokes WiFi hal get api wifi_getMuEdca()
 * @param [in] req-     : radioIndex - radio index
 * @param [in] req-     : accessCategory - Access Category for MU (Multi-User) EDCA
 *                        (Enhanced Distributed Channel Access) includes background, best effort,
 *                        video, voice
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetMuEdca(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetMuEdca ----->Entry\n");
    wifi_edca_t edca;
    int radioIndex = 0;
    int returnValue = 0;
    wifi_access_category_t accessCategory = wifi_access_category_background;
    char details[2000] = {'\0'};
    char output[2000] = {'\0'};

    if (&req["radioIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Radio Index : %d", radioIndex);

    accessCategory = (wifi_access_category_t)req["accessCategory"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Access Category : %d", accessCategory);

    returnValue = ssp_WIFIHALGetMuEdca(radioIndex, accessCategory, &edca, output);

    if(0 == returnValue)
    {
        sprintf(details, "wifi_getMuEdca invoked successfully; Details : %s", output);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getMuEdca not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetMuEdca  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetMuEdca ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRadioOperatingParameters
 * Description          : This function invokes WiFi hal get api wifi_getRadioOperatingParameters()
 * @param [in] req-     : radioIndex - radio index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioOperatingParameters(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioOperatingParameters ----->Entry\n");
    wifi_radio_operationParam_t operationParams;
    int radioIndex = 0;
    int returnValue = 0;
    char details[2000] = {'\0'};
    char output[2000] = {'\0'};

    if (&req["radioIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = (wifi_radio_index_t)req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Radio Index : %d", radioIndex);

    returnValue = ssp_WIFIHALGetRadioOperatingParameters(radioIndex, &operationParams, output);

    if(0 == returnValue)
    {
        sprintf(details, "wifi_getRadioOperatingParameters invoked successfully; Details : %s", output);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getRadioOperatingParameters not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioOperatingParameters  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioOperatingParameters ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRadioChannels
 * Description          : This function invokes WiFi hal get api wifi_getRadioChannels()
 * @param [in] req-     : radioIndex - radio index
 * @param [in] req-     : numberOfChannels - Number of channels available for each radio
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioChannels(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioChannels ----->Entry\n");
    wifi_channelMap_t radioChannels[NUM_CH_ALL];
    memset(&radioChannels, 0, sizeof(radioChannels));
    int radioIndex = 0;
    int numberOfChannels = 0;
    int returnValue = 0;
    char details[4000] = {'\0'};
    char output[4000] = {'\0'};

    if (&req["radioIndex"] == NULL || &req["numberOfChannels"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Radio Index : %d", radioIndex);

    numberOfChannels = req["numberOfChannels"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Number of channels : %d", numberOfChannels);

    returnValue = ssp_WIFIHALGetRadioChannels(radioIndex, radioChannels, NUM_CH_ALL, numberOfChannels, output);

    if(0 == returnValue)
    {
        sprintf(details, "wifi_getRadioChannels invoked successfully; Details : %s", output);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getRadioChannels not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioChannels  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioChannels ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetEAPParam
 * Description          : This function invokes WiFi hal get api wifi_getEAP_Param()
 * @param [in] req-     : apIndex - Access Point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetEAPParam(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetEAPParam ----->Entry\n");
    wifi_eap_config_t eapConfig;
    memset(&eapConfig, 0, sizeof(eapConfig));
    int apIndex = 0;
    int returnValue = 0;
    char details[2000] = {'\0'};
    char output[2000] = {'\0'};

    if (&req["apIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);

    returnValue = ssp_WIFIHALGetEAPParam(apIndex, &eapConfig, output);

    if(0 == returnValue)
    {
        sprintf(details, "wifi_getEAP_Param invoked successfully; Details : %s", output);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getEAP_Param not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetEAPParam  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetEAPParam ---->Exiting\n");
    return;
}
