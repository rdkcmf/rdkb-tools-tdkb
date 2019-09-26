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
#include <sstream>
#include "WIFIAgent.h"
#include "ssp_tdk_wrp.h"

/* To provide external linkage to C Functions defined in TDKB Component folder */

extern "C"
{
    int ssp_register(bool);
    GETPARAMVALUES* ssp_getParameterValue(char *pParamName,int *pParamsize);
    int ssp_setParameterValue(char *pParamName,char *pParamValue,char *pParamType,int commit);
    GETPARAMATTR* ssp_getParameterAttr(char *pParamAttr,int *pParamAttrSize);
    int ssp_setParameterAttr(char *pParamName,char *pAttrNotify,char *pAttrAccess);
    GETPARAMNAMES* ssp_getParameterNames(char *pPathName,int recursive,int *pParamSize);
    int ssp_addTableRow(char *pObjTbl,int *pInstanceNumber);
    int ssp_deleteTableRow(char *pObjTbl);
    int ssp_setCommit(char *pObjTbl);
    int ssp_getHealth(char *pComponentName);
    int ssp_setSessionId(int priority, int sessionId,char *pComponentName,int override);
    int ssp_setMultipleParameterValue(char **paramList, int size);
    int ssp_WiFiHalCallMethodForBool(int radioIndex, unsigned char *output, char* method);
    int ssp_WiFiCallMethodForULong(int radioIndex, unsigned long *uLongVar, char* methodName);
    int ssp_WiFiCallMethodForString(int radioIndex, char *output, char* methodName);
    int ssp_WiFiCallMethodForInt(int radioIndex, int *output, char* methodName);

};

/***************************************************************************
 *Function name	: initialize
 *Description	: Initialize Function will be used for registering the wrapper method
 *        	  	  with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/

bool WIFIAgent::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE,"TDK::WIFIAgent Initialize\n");
    return TEST_SUCCESS;

}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string WIFIAgent::testmodulepre_requisites()
{
    int returnValue;
    int bStart = 1;
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent::testmodulepre_requisites");
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
bool WIFIAgent::testmodulepost_requisites()
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
 * Function Name	: WIFIAgent_Start
 * Description		: This function will invoke TDK Component that will attach to
 * 		        	  CCSP Component Registrar (CR)
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_register
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_Start(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_start --->Entry \n");

    bool bStart = 1;
    int returnValue = 0;

    returnValue = ssp_register(bStart);

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="NULL";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_start --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name	: WIFIAgent_Get
 * Description		: This function will invoke TDK Component GET Value wrapper
 *       			  function to get parameter value
 *
 * @param [in] req- This holds Path name for Parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 		            	   ssp_getParameterValue
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_Get(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_get --->Entry\n");
    bool bReturn = TEST_FAILURE;
    char ParamNames[MAX_PARAM_SIZE];
    GETPARAMVALUES *resultDetails;
    int	paramsize=0;
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

    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_get --->Exit\n");

    return;
}

/*******************************************************************************************
 *
 * Function Name	: WIFIAgent_Set
 * Description		: This function will invoke TDK Component SET Value wrapper
 * 			          function
 *
 * @param [in] req-        This hods Path name, Value to set and its type
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 		            	   ssp_setParameterValue
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_Set(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_set --->Entry\n");
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

    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_Set:: ParamName input is %s",ParamName);
    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_Set:: ParamValue input is %s",ParamValue);
    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_Set:: ParamType input is %s",ParamType);


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
        response["details"]="WIFIAgentStub::SET API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdk_wifiagent_set --->Error in Set API Validation of WIFI Agent in DUT !!! \n");
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
        response["details"]="WIFIAgentStub::SET API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdk_wifiagent_set --->Error in Set API Validation in DUT !!! \n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_set --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIAgent_SetMultiple
 * Description          : This function will set multiple parameter value at one shot
 *
 * @param [in] req-        ParamList will hold the entire list to be set.
 *
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                         ssp_setMultipleParameterValue
********************************************************************************************/
void WIFIAgent::WIFIAgent_SetMultiple(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_SetMultiple --->Entry\n");

    int returnValue = 0;
    int retVal = 0;
    char params[1000] = {'\0'};
    char **paramlist  = NULL;
    int num_spaces = 0;
    int index = 0;
    int size = 0;
    int commit = 1;

    strcpy(params,req["paramList"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_SetMultiple:: ParamList input is %s\n",params);

    char *list = strtok (params, "|");
    while (list) {
    paramlist = (char **) realloc (paramlist, ++num_spaces * sizeof(char *));
    if (paramlist == NULL)
    {
         return;
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
       response["details"]="WIFIAgent_SetMultiple::SET API Validation is Failure";
       DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_SetMultiple: Failed to set multiple parameters !!! \n");
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
        response["details"]="WIFIAgent_SetMultiple::SET API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_SetMultiple --->Error in Set API Validation in DUT !!! \n");
    }

    /* free the memory allocated */
   free(paramlist);

   DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_SetMultiple --->Exit\n");

   return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIAgent_Set_Get
 * Description          : This function will invoke TDK Component SET and GET Value wrapper
 *                        function for functional Validation
 *
 * @param [in] req-        This hods Path name, Value to set and its type
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                         ssp_setParameterValue and ssp_getParameterValue
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_Set_Get(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_set_get --->Entry\n");

    bool bReturn = TEST_FAILURE;
    //Set Param
    int returnValue = 0;
    int retVal = 0;
    char ParamName[MAX_PARAM_SIZE];
    char ParamValue[MAX_PARAM_SIZE];
    char ParamType[MAX_PARAM_SIZE];
    int commit = 1;

    //Get Param
    char ParamNames[MAX_PARAM_SIZE];
    GETPARAMVALUES *resultDetails;
    int     paramsize=0;

    //Set Param
    strcpy(ParamName,req["paramName"].asCString());
    strcpy(ParamValue,req["paramValue"].asCString());
    strcpy(ParamType,req["paramType"].asCString());

    //Get param
    strcpy(ParamNames,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_Set_Get:: ParamName input is %s",ParamName);
    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_Set_Get:: ParamValue input is %s",ParamValue);
    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_Set_Get:: ParamType input is %s",ParamType);


    returnValue = ssp_setParameterValue(&ParamName[0],&ParamValue[0],&ParamType[0],commit);

    if(0 != returnValue)
    {
        response["result"]="FAILURE";
        response["details"]="WIFIAgentStub::SET API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdk_wifiagent_set_get --->Error in Set API Validation of WIFI Agent in DUT !!! \n");
        return;
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
        response["result"]="SUCCESS";
        response["details"]="SET API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="WIFIAgentStub::SET API ApplySetting is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdk_wifiagent_set --->Error in Set API ApplySetting Validation in DUT !!! \n");
        return;
    }

    resultDetails = ssp_getParameterValue(&ParamNames[0],&paramsize);

    if(resultDetails == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="Get Parameter Value API Validation Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_set_get --->Error in Get API Validation of WIFI Agent in DUT !!! \n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_set_get:: Value of resultDetails[0].pParamValues is %s and strlen is %d",resultDetails[0].pParamValues,strlen((const char *)resultDetails[0].pParamValues));

    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_set_get:: Value of ParamValue[0] is %s and strlen is %d",&ParamValue[0],strlen((const char *)&ParamValue[0]));

    if((strcmp(resultDetails[0].pParamValues,&ParamValue[0])) == 0)
    {
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="Set Get Functional Validation is Succeeded";
    }
    else
    {

        response["result"]="FAILURE";
        response["details"]="Set Get Functional Validation Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_set_get --->Error in Functional Validation of WIFI Agent in DUT !!! \n");
    }

    if(resultDetails != NULL)
    {

        for(int i=0; i < paramsize; i++)
        {
            free(resultDetails[i].pParamValues);
        }
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_set_get --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name	: WIFIAgent_GetAttr
 * Description		: This function is called through RPC which will invoke TDK
 * 			          Wrapper Get attribute function
 *
 * @param [in] req- 	   This holds Attribute path name
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_getParameterAttr
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_GetAttr(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_GetAttr --->Entry\n");
    int attrCnt=0;
    int retParamAttrSize = 0;
    char ParamAttr[MAX_PARAM_SIZE];
    GETPARAMATTR *resultDetails;
    bool bReturn = TEST_FAILURE;

    strcpy(ParamAttr,req["paramname"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n Input path name is %s\n",ParamAttr);

    resultDetails = ssp_getParameterAttr(&ParamAttr[0],&retParamAttrSize);

    if(resultDetails == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="WIFIAgentStub::GET Parameter Attribute API Validation is Failure";
    }
    else
    {
        for(attrCnt=0; attrCnt < retParamAttrSize; attrCnt++)
        {
            free(resultDetails[attrCnt].pParamAccess);
            free(resultDetails[attrCnt].pParamNotify);
        }
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="GET Parameter Attribute API Validation is Success";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_GetAttr --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name	: WIFIAgent_SetAttr
 * Description		: This function is called through TM RPC which will invoke TDK
 *      			  Wrapper Set Attribute Function
 *
 * @param [in] req- 	  This holds attribute path name and it attributes values to be set
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 	            		   ssp_setParameterAttr
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_SetAttr(IN const Json::Value& req, OUT Json::Value& response)
{

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_SetAttr --->Entry\n");
    bool bReturn = TEST_FAILURE;
    int returnValue;
    char AttrNotify[MAX_PARAM_SIZE];
    char AttrAccess[MAX_PARAM_SIZE];
    char ParamName[MAX_PARAM_SIZE];

    strcpy(ParamName,req["paramname"].asCString());

    strcpy(AttrNotify,req["notification"].asCString());

    strcpy(AttrAccess,req["accessControlChanged"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n Input path name is %s\n",ParamName);
    DEBUG_PRINT(DEBUG_TRACE,"\n Input notification is %s\n",AttrNotify);
    DEBUG_PRINT(DEBUG_TRACE,"\n Input access control is %s\n",AttrAccess);

    returnValue = ssp_setParameterAttr(&ParamName[0],&AttrNotify[0],&AttrAccess[0]);

    if(returnValue!=0)
    {
        response["result"]="FAILURE";
        response["details"]="WIFIAgentStub::SET Parameter Attribute API Validation Failure";
    }
    else
    {
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="SET Parameter Attribute API Validation is Success";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_SetAttr --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name	: WIFIAgent_GetNames
 * Description		: This function is called through TM RPC which will invoke TDK
 * 		        	  Wrapper function to get Parameter names of given component path
 *
 * @param [in] req- 	  This holds path name
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_getParameterNames
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_GetNames(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_GetNames --->Entry\n");
    int retParamNameSize = 0;
    char PathName[MAX_PARAM_SIZE];
    GETPARAMNAMES *resultDetails;
    int  recursive=0;
    bool bReturn = TEST_FAILURE;

    strcpy(PathName,req["pathname"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n Input path name is %s \n",PathName);

    recursive = req["brecursive"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\n Input path name is %s and recursive is %d\n",PathName,recursive);

    resultDetails = ssp_getParameterNames(&PathName[0],recursive,&retParamNameSize);

    if(resultDetails == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="WIFIAGENT::Get Param Name API Validation Fail";
    }
    else
    {
        for(int nameCnt=0; nameCnt < retParamNameSize; nameCnt++)
        {
            free(resultDetails[nameCnt].pParamNames);
        }
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="Get Parameter Names API Validation is Success";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_GetNames --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIAgent_AddObject
 * Description          : Add a row to the table object
 *
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 		                   ssp_addTableRow
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_AddObject(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_AddObject --->Entry\n");

    int returnValue;
    int instanceNumber=0;
    char paramName[MAX_PARAM_SIZE];
    bool bReturn = TEST_FAILURE;

    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
        return;
    }

    strcpy(paramName,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_AddObject:: ParamName input is %s",paramName);

    returnValue = ssp_addTableRow(&paramName[0],&instanceNumber);

    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_AddObject::Object added with instance %d",instanceNumber);

    if(0 == returnValue)
    {
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="ADD OBJECT API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="WIFIAgent::ADD OBJECT API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_AddObject --->Error in adding object !!! \n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_AddObject --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIAgent_DelObject
 * Description          : Delete a row from the table object
 *
 * @param [in] req-	This holds parameter path name
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_deleteTableRow
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_DelObject(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_DelObject --->Entry\n");

    int returnValue;
    char paramName[MAX_PARAM_SIZE];
    bool bReturn = TEST_FAILURE;
    int instanceNumber=0;
    int apitest=0;
    std::ostringstream sin;

    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
        return;
    }

    strcpy(paramName,req["paramName"].asCString());
    apitest = req["apiTest"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_DelObject:: ParamName input is %s",paramName);
    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_DelObject:: apiTest input is %d",apitest);

    if(apitest != 0)
    {

        returnValue = ssp_addTableRow(&paramName[0],&instanceNumber);

        if(returnValue == 0)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_AddObject::Object added with instance %d",instanceNumber);
            sin << instanceNumber;
            std::string val = sin.str();
            strcat(paramName,val.c_str());
            strcat(paramName,".");
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_DelObject:: Modified ParamName input is %s",paramName);

    returnValue = ssp_deleteTableRow(&paramName[0]);

    if(0 == returnValue)
    {
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="DELETE OBJECT API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="WIFIAgentStub::Delete Object API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_DelObject --->Error in deleting object !!! \n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_DelObject --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIAgent_SetCommit
 * Description          : Commit the changes in the table object
 *
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_setCommit
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_SetCommit(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_SetCommit --->Entry\n");

    int returnValue;
    char paramName[MAX_PARAM_SIZE];
    bool bReturn = TEST_FAILURE;

    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
        return;
    }

    strcpy(paramName,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_SetCommit:: ParamName input is %s",paramName);

    returnValue = ssp_setCommit(&paramName[0]);

    if(0 == returnValue)
    {
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="COMMIT API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="WIFIAgnetStub::Commit API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n ssp_setCommit --->Error in committing the changes !!! \n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_SetCommit --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIAgent_GetHealth
 * Description          : Get the health  of the component
 *
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_getHealth
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_GetHealth(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_GetHealth --->Entry\n");

    int returnValue;
    char paramName[MAX_PARAM_SIZE];

    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="WIFIAgentStub::Error Invoking TDK Component";
        return;
    }

    strcpy(paramName,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_GetHealth:: ParamName input is %s",paramName);

    returnValue = ssp_getHealth(&paramName[0]);

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="GET HEALTH API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="WIFIAgentStub::GET HEALTH API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_GetHealth --->Error in retrieving the component !!! \n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_GetHealth --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIAgent_SetSessionId
 * Description          : Set the session Id
 *
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_setSessionId
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_SetSessionId(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_SetSessionId --->Entry\n");

    int returnValue;
    int priority = 0;
    int sessionId = 0;
    int override = 0;
    char pathname[MAX_PARAM_SIZE];

    strcpy(pathname,req["pathname"].asCString());

    if(&req["priority"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
        return;
    }

    if(&req["sessionId"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
        return;
    }

    priority = req["priority"].asInt();
    sessionId = req["sessionId"].asInt();
    override = req["override"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_SetSessionId:: priority is %d",priority);
    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_SetSessionId:: sessionId is %d",sessionId);
    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_SetSessionId:: override is %d",override);
    DEBUG_PRINT(DEBUG_TRACE,"\nWIFIAgent_SetSessionId:: pathname is %s",pathname);

    returnValue = ssp_setSessionId(priority,sessionId,&pathname[0],override);

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="SET SESSION ID API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="WIFIAgent_Stub::SET SESSION ID API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_SetSessionId --->Error in setting the session Id !!! \n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIAgent_SetSessionId --->Exit\n");
    return;
}



/*******************************************************************************************
 *
 * Function Name	: WIFIAgent_Stop
 * Description		: This function is called through TM RPC which will invoke TDK
 *			  Wrapper Stop function
 *
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_register
 ********************************************************************************************/

void WIFIAgent::WIFIAgent_Stop(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_stop --->Entry\n");
    int returnValue;
    bool bStart = 0;

    returnValue = ssp_register(bStart);

    if( 0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="NULL";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
        DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_stop --->Error in Execution \n");
        return;
    }


    DEBUG_PRINT(DEBUG_TRACE,"\n wifiagent_stop --->Exit\n");
    return;
}

/**************************************************************************
 * Function Name	: CreateObject
 * Description	: This function will be used to create a new object for the
 *		  class "WIFIAgent".
 *
 **************************************************************************/

extern "C" WIFIAgent* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new WIFIAgent(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/

bool WIFIAgent::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"WIFIAgent shutting down\n");
    return TEST_SUCCESS;
}


/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(WIFIAgent *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying WIFIAgent object\n");
    delete stubobj;
}

