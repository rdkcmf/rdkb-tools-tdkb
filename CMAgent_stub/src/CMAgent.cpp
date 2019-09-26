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
#include "CMAgent.h"
#include "ssp_tdk_wrp.h"

/* To provide external linkage to C Functions defined in TDKB Component folder */
extern "C"
{
    int ssp_register(bool);
    int ssp_terminate();
    GETPARAMVALUES* ssp_getParameterValue(char *pParamName,int *pParamsize);
    int ssp_setParameterValue(char *pParamName,char *pParamValue,char *pParamType);
    GETPARAMATTR* ssp_getParameterAttr(char *pParamAttr,int *pParamAttrSize);
    int ssp_setParameterAttr(char *pParamName,char *pAttrNotify,char *pAttrAccess);
    GETPARAMNAMES* ssp_getParameterNames(char *pPathName,int recursive,int *pParamSize);
    int ssp_addTableRow(char *pObjTbl,int *pInstanceNumber);
    int ssp_deleteTableRow(char *pObjTbl);
    int ssp_setCommit(char *pObjTbl);
    int ssp_getHealth(char *pComponentName);
    int ssp_setSessionId(int priority, int sessionId,char *pComponentName,int override);
};

/***************************************************************************
 *Function name	: initialize
 *Description	: Initialize Function will be used for registering the wrapper method
 *  	  	  with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/

bool CMAgent::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE,"TDK::CMAgent Initialize\n");
    return TEST_SUCCESS;

}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string CMAgent::testmodulepre_requisites()
{
    int returnValue;
    int bStart = 1;
    returnValue = ssp_register(bStart);

    if(0 != returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepre_requisites --->Error invoking TDK Agent in DUT !!! \n");
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
bool CMAgent::testmodulepost_requisites()
{
    int returnValue;
    int bStart = 0;
    returnValue = ssp_terminate();

    if(0 != returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepost_requisites --->Error invoking TDK Agent in DUT !!! \n");
        return TEST_FAILURE;
    }

    return TEST_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name	: CMAgent_Get
 * Description		: This function will invoke TDK Component GET Value wrapper
 * 			  function to get parameter value
 *
 * @param [in] req- This holds Path name for Parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_getParameterValue
 ********************************************************************************************/

void CMAgent::CMAgent_Get(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_Get --->Entry\n");

    char ParamNames[MAX_PARAM_SIZE];
    GETPARAMVALUES *resultDetails;
    int	paramsize=0;

    strcpy(ParamNames,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n ParamNames input is %s",ParamNames);

    resultDetails = ssp_getParameterValue(&ParamNames[0],&paramsize);

    if(resultDetails == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="Get Parameter Value API Validation Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_Get --->Exit\n");
	return;
    }
    else
    {
        response["result"]="SUCCESS";
        response["details"]=resultDetails[0].pParamValues;

        for(int i=0; i < paramsize; i++)
        {
            free(resultDetails[i].pParamValues);
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_Get --->Exit\n");

    return;
}

/*******************************************************************************************
 *
 * Function Name	: CMAgent_Set
 * Description		: This function will invoke TDK Component SET Value wrapper
 * 			          function
 *
 * @param [in] req-        This holds Path name, Value to set and its type
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_setParameterValue
 ********************************************************************************************/

void CMAgent::CMAgent_Set(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_Set --->Entry\n");

    int returnValue = 0;
    char ParamName[MAX_PARAM_SIZE];
    char ParamValue[MAX_PARAM_SIZE];
    char ParamType[MAX_PARAM_SIZE];

    strcpy(ParamName,req["paramName"].asCString());
    strcpy(ParamValue,req["paramValue"].asCString());
    strcpy(ParamType,req["paramType"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_Set:: ParamName input is %s",ParamName);
    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_Set:: ParamValue input is %s",ParamValue);
    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_Set:: ParamType input is %s",ParamType);

    returnValue = ssp_setParameterValue(&ParamName[0],&ParamValue[0],&ParamType[0]);

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="SET API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CMAgentStub::SET API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_Set --->Error in Set API Validation of CM Agent in DUT !!! \n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_Set --->Exit\n");
    return;
}


/*******************************************************************************************
 *
 * Function Name	: CMAgent_Set_Get
 * Description		: This function will invoke TDK Component SET and GET Value wrapper
 * 			          function for functional Validation
 *
 * @param [in] req-        This hods Path name, Value to set and its type
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_setParameterValue and ssp_getParameterValue
 ********************************************************************************************/

void CMAgent::CMAgent_Set_Get(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_Set_Get --->Entry\n");

    bool	bReturn = TEST_FAILURE;
    //Set Param
    int returnValue = 0;
    char ParamName[MAX_PARAM_SIZE];
    char ParamValue[MAX_PARAM_SIZE];
    char ParamType[MAX_PARAM_SIZE];

    //Get Param
    char ParamNames[MAX_PARAM_SIZE];
    GETPARAMVALUES *resultDetails;
    int	paramsize=0;

    //Set Param
    strcpy(ParamName,req["paramName"].asCString());
    strcpy(ParamValue,req["paramValue"].asCString());
    strcpy(ParamType,req["paramType"].asCString());

    //Get param
    strcpy(ParamNames,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_Set_Get:: ParamName input is %s",ParamName);
    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_Set_Get:: ParamValue input is %s",ParamValue);
    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_Set_Get:: ParamType input is %s",ParamType);

    returnValue = ssp_setParameterValue(&ParamName[0],&ParamValue[0],&ParamType[0]);

    if(0 != returnValue)
    {
        response["result"]="FAILURE";
        response["details"]="CMAgentStub::SET API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_Set_Get --->Error in Set API Validation of CM Agent in DUT !!! \n");
	return;
    }


    resultDetails = ssp_getParameterValue(&ParamNames[0],&paramsize);

    if(resultDetails == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="Get Parameter Value API Validation Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_Set_Get --->Error in Get API Validation of CM Agent in DUT !!! \n");
	return;
    }

    if((strcmp(resultDetails[0].pParamValues,&ParamValue[0])) == 0)
    {
        response["result"]="SUCCESS";
        response["details"]="Set Get Functional Validation is Succeeded";
        bReturn = TEST_SUCCESS;
    }
    else
    {

        response["result"]="FAILURE";
        response["details"]="Set Get Functional Validation Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_Set_Get --->Error in Functional Validation of CM Agent in DUT !!! \n");
    }

    if(resultDetails != NULL)
    {

        for(int i=0; i < paramsize; i++)
        {
            free(resultDetails[i].pParamValues);
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_Set_Get --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name	: CMAgent_GetAttr
 * Description		: This function is called through RPC which will invoke TDK
 * 			  Wrapper Get attribute function
 *
 * @param [in] req- 	   This holds Attribute path name
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_getParameterAttr
 ********************************************************************************************/

void CMAgent::CMAgent_GetAttr(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_GetAttr --->Entry\n");
    bool bReturn = TEST_FAILURE;
    int attrCnt=0;
    int retParamAttrSize = 0;
    char ParamAttr[MAX_PARAM_SIZE];
    GETPARAMATTR *resultDetails;

    strcpy(ParamAttr,req["paramname"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n Input path name is %s\n",ParamAttr);


    resultDetails = ssp_getParameterAttr(&ParamAttr[0],&retParamAttrSize);

    if(resultDetails == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="CMAgentStub::GET Parameter Attribute API Validation is Failure";
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

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_GetAttr --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name	: CMAgent_SetAttr
 * Description		: This function is called through TM RPC which will invoke TDK
 * 			  Wrapper Set Attribute Function
 *
 * @param [in] req- 	  This holds attribute path name and it attributes values to be set
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_setParameterAttr
 ********************************************************************************************/

void CMAgent::CMAgent_SetAttr(IN const Json::Value& req, OUT Json::Value& response)
{

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_SetAttr --->Entry\n");

    int returnValue = 0;
    bool bReturn = TEST_FAILURE;
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
        response["details"]="CMAgentStub::SET Parameter Attribute API Validation Failure";
    }
    else
    {
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="SET Parameter Attribute API Validation is Success";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_SetAttr --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name	: CMAgent_GetNames
 * Description		: This function is called through TM RPC which will invoke TDK
 * 			  Wrapper function to get Parameter names of given component path
 *
 * @param [in] req- 	  This holds path name
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_getParameterNames
 ********************************************************************************************/

void CMAgent::CMAgent_GetNames(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_GetNames --->Entry\n");
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
        response["details"]="CMAGENT::Get Param Name API Validation Fail";
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

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_GetNames --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : CMAgent_AddObject
 * Description          : Add a row to the table object
 *
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_addTableRow
 ********************************************************************************************/

void CMAgent::CMAgent_AddObject(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_AddObject --->Entry\n");
    bool bReturn = TEST_FAILURE;
    int returnValue = 0;
    char paramName[MAX_PARAM_SIZE];
    int instanceNumber = 0;

    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
	return;
    }

    strcpy(paramName,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_AddObject:: ParamName input is %s",paramName);


    returnValue = ssp_addTableRow(&paramName[0],&instanceNumber);


    if(0 == returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_AddObject::instance added is %d",instanceNumber);
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="ADD OBJECT API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CMAgent::ADD OBJECT API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_AddObject --->Error in adding object !!! \n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_AddObject --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : CMAgent_DelObject
 * Description          : Delete a row from the table object
 *
 * @param [in] req-	This holds parameter path name
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_deleteTableRow
 ********************************************************************************************/

void CMAgent::CMAgent_DelObject(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_DelObject --->Entry\n");

    int returnValue = 0;
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

    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_DelObject:: ParamName input is %s",paramName);
    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_DelObject:: apiTest input is %d",apitest);

    if(apitest != 0)
    {

        returnValue = ssp_addTableRow(&paramName[0],&instanceNumber);

        if(returnValue == 0)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_AddObject::Object added with instance %d",instanceNumber);
            sin << instanceNumber;
            std::string val = sin.str();
            strcat(paramName,val.c_str());
            strcat(paramName,".");
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_DelObject:: Modified ParamName input is %s",paramName);

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
        response["details"]="CMAgentStub::Delete Object API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_DelObject --->Error in deleting object !!! \n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_DelObject --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : CMAgent_SetCommit
 * Description          : Commit the changes in the table object
 *
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_setCommit
 ********************************************************************************************/

void CMAgent::CMAgent_SetCommit(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_SetCommit --->Entry\n");
    bool bReturn = TEST_FAILURE;
    int returnValue = 0;
    char paramName[MAX_PARAM_SIZE];

    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
	return;
    }

    strcpy(paramName,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_SetCommit:: ParamName input is %s",paramName);


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
        response["details"]="CMAgentStub::Commit API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_SetCommit --->Error in committing the changes !!! \n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_SetCommit --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : CMAgent_GetHealth
 * Description          : Get the health  of the component
 *
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_getHealth
 ********************************************************************************************/

void CMAgent::CMAgent_GetHealth(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_GetHealth --->Entry\n");
    bool bReturn = TEST_FAILURE;
    int returnValue = 0;
    char paramName[MAX_PARAM_SIZE];

    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="CMAgentStub::Error Invoking TDK Component";
	return;
    }

    strcpy(paramName,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_GetHealth:: ParamName input is %s",paramName);


    returnValue = ssp_getHealth(&paramName[0]);

    if(0 == returnValue)
    {
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="GET HEALTH API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CMAgentStub::GET HEALTH API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_GetHealth --->Error in retrieving the component !!! \n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_GetHealth --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : CMAgent_SetSessionId
 * Description          : Set the session Id
 *
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			   ssp_setSessionId
 ********************************************************************************************/

void CMAgent::CMAgent_SetSessionId(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_SetSessionId --->Entry\n");
    bool bReturn = TEST_FAILURE;
    int returnValue = 0;
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

    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_SetSessionId:: priority is %d",priority);
    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_SetSessionId:: sessionId is %d",sessionId);
    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_SetSessionId:: override is %d",override);
    DEBUG_PRINT(DEBUG_TRACE,"\nCMAgent_SetSessionId:: pathname is %s",pathname);


    returnValue = ssp_setSessionId(priority,sessionId,&pathname[0],override);

    if(0 == returnValue)
    {
        bReturn = TEST_SUCCESS;
        response["result"]="SUCCESS";
        response["details"]="SET SESSION ID API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CMAgent_Stub::SET SESSION ID API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_SetSessionId --->Error in setting the session Id !!! \n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CMAgent_SetSessionId --->Exit\n");
    return;
}



/**************************************************************************
 * Function Name	: CreateObject
 * Description	: This function will be used to create a new object for the
 *		  class "CMAgent".
 *
 **************************************************************************/

extern "C" CMAgent* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new CMAgent(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/

bool CMAgent::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"CMAgent shutting down\n");
    return TEST_SUCCESS;
}


/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(CMAgent *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying CMAgent object\n");
    delete stubobj;
}

