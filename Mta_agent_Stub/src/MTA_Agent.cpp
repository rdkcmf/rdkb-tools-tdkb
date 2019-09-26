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

#include "MTA_Agent.h"
#include "ssp_tdk_wrp.h"

extern "C" {

GETPARAMVALUES* ssp_getParameterValue(char* pParamName,int* pParamsize);
int ssp_register(bool);
int ssp_setParameterValue(char *pParamName,char *pParamValue,char *pParamType, int commit);
GETPARAMNAMES *ssp_getParameterNames(char* pPathName,int recursive,int* pParamSize);
int ssp_setParameterAttr(char* pParamName,char* pAttrNotify,char* pAttrAccess);
GETPARAMATTR* ssp_getParameterAttr(char* pParamAttr,int* pParamAttrSize);
int ssp_terminate();
void free_Memory_Names(int size,GETPARAMNAMES *Freestruct);
void free_Memory_val(int size,GETPARAMVALUES *Freestruct);
void free_Memory_Attr(int size,GETPARAMATTR *Freestruct);
int ssp_setCommit(char *pObjTbl);
int ssp_addTableRow(char *pObjTbl);
int ssp_deleteTableRow(char *pObjTbl);
int ssp_setSessionId(int priority, int sessionId,char *pComponentName,int override);
int ssp_getHealth(char *pComponentName);
}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Descrption    : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string MTA_Agent::testmodulepre_requisites()
{

    int returnVal=0;

    DEBUG_PRINT(DEBUG_TRACE,"testmodulepre_requisites::Initiate to register with Component register\n");

    returnVal=ssp_register(1);
    if(returnVal == 0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"testmodulepre_requisites::MTAAgent stub registered with CR\n");
        return "SUCCESS";
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"testmodulepre_requisites::Failed to register with CR\n");
        return "FAILURE";
    }
}

/***************************************************************************
 *Function name : testmodulepost_requisites
 *Descrption    : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/
bool MTA_Agent::testmodulepost_requisites()
{
  int returnVal=0;

    DEBUG_PRINT(DEBUG_TRACE,"Initiate to unregistered from Component register\n");

    returnVal=ssp_terminate();
    if(returnVal == 0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"WECB stub unregistered from CR \n");
        return TEST_SUCCESS;
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Failed to unregistered from CR\n");
        return TEST_FAILURE;
    }
}
/***************************************************************************
 *Function name : MTA_agent_Init
 *Descrption    : MTA_Agent_Init will be used for initiating
 *                in CCSP module
 *
 *****************************************************************************/
void MTA_Agent::MTA_agent_Init(IN const Json::Value& req, OUT Json::Value& response)
{
    int i=0;
    DEBUG_PRINT(DEBUG_TRACE,"Intiating a session with MTA Agent component\n");
    i=ssp_register(1);
    if(i==0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"MTA Component is intiated \n");
        response["result"] = "SUCCESS";
        response["details"] = "Intiation Success";
	return;
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Failed to intialize properly");
        response["result"] = "FAILURE";
        response["details"] = "Intiation FAILURE";
	return;
    }
}


/***************************************************************************
 *Function name : MTA_agent_GetParameterValues
 *Descrption    : MTA Component Get Param Value API functionality checking
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void MTA_Agent::MTA_agent_GetParameterValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function GetParamValues \n");
    int size_ret=0,i=0;
    GETPARAMVALUES *DataParamValue;
    string ParamName=req["ParamName"].asCString();
    DataParamValue=ssp_getParameterValue(&ParamName[0],&size_ret);
    if((DataParamValue == NULL))
    {
        printf("GetParamValue funtion returns NULL as o/p\n");
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Parameter Values are as :\n");
        for (i=0;i<size_ret;i++)
        {
            printf("Parameter No.%d\n",i);
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Name is %s\n",ParamName.c_str());
            DEBUG_PRINT(DEBUG_TRACE,"Value is %s",DataParamValue[i].pParamValues);
            DEBUG_PRINT(DEBUG_TRACE," Type is %d\n",DataParamValue[i].pParamType);
        }
        if(i==size_ret)
        {
            free_Memory_val(size_ret,DataParamValue);
            response["result"] = "SUCCESS";
            response["details"] = "Get Param value Success";
	    return;
        }

    }
    free_Memory_val(size_ret,DataParamValue);
    response["result"] = "FAILURE";
    response["details"] = "Get Param value Failure of the function";
    return;

}

/***************************************************************************
 *Function name : MTA_agent_SetParameterValues
 *Descrption    : MTA Component Set Param Value API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - ParamValue : Holds the value of the parameter
 * @param [in]  req - Type : Holds the Type of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void MTA_Agent::MTA_agent_SetParameterValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function SetParamValues \n");
    int size_ret=0,i=0,setResult=0;
    string ParamName=req["ParamName"].asCString();
    string ParamValue=req["ParamValue"].asCString();
    string Type=req["Type"].asCString();
    GETPARAMVALUES *DataParamValue1;
    setResult=ssp_setParameterValue(&ParamName[0],&ParamValue[0],&Type[0],1);
    if(setResult==0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"Parameter Values have been set.Needs to cross be checked with Get Parameter Names\n");
        DataParamValue1=ssp_getParameterValue(&ParamName[0],&size_ret);
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Parameter value is not changed Set returns failure";
	return;

    }

    if((DataParamValue1== NULL))
    {
        printf("SetParamValue funtion returns NULL as output\n");
    }
    else
    {

        printf("Set Value:%s\n",&ParamValue[0]);
        printf("Value retrieved is:%s\n",DataParamValue1[0].pParamValues);

        if(strcmp(&ParamValue[0],DataParamValue1[0].pParamValues)==0)
        {
            printf("Set has been validated successfully\n");
            free_Memory_val(size_ret,DataParamValue1);
            response["result"] = "SUCCESS";
            response["details"] = "Set has been validated successfully";
	    return;
        }
        else
        {
            free_Memory_val(size_ret,DataParamValue1);
            printf("Parameter Value has not changed after a proper Set\n");
        }
    }

    response["result"] = "FAILURE";
    response["details"] = "FAILURE : Parameter Value has not changed after a proper Set";
    return;
}
/***************************************************************************
 *Function name : MTA_agent_GetParameterNames
 *Descrption    : MTA Component Get Param Name API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - ParamList : Holds the List of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void MTA_Agent::MTA_agent_GetParameterNames(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Fucntion GetParamNames \n");
    string ParamName=req["ParamName"].asCString();
    string ParamList=req["ParamList"].asCString();
    int size=0,i=0;
    int size_ret=0;
    GETPARAMNAMES *DataValue;
    GETPARAMNAMES *DataValue1;
    DataValue=ssp_getParameterNames(&ParamName[0],1,&size_ret);
    if(NULL==DataValue)
    {
        response["result"] = "FAILURE";
        response["details"] = "Get Param Name for Parameter returned NULL";
	return;
    }
    DataValue1=ssp_getParameterNames(&ParamList[0],0,&size);
    if(NULL==DataValue1)
    {
        printf("Get Param Name for ParameterList returned NULL\n");
        free_Memory_Names(size_ret,DataValue);
    }
    else
    {
        for(i=0;i<size;i++)
        {
            if(strcmp(DataValue1[i].pParamNames,DataValue[0].pParamNames)==0)
            {
                if(DataValue[0].writable==DataValue1[i].writable)
                {
                    free_Memory_Names(size,DataValue1);
                    printf("Parameter Name has been fetched successfully and it matched with parameter List\n");
                    response["result"] = "SUCCESS";
                    response["details"] = "Parameter Name has been fetched successfully and it matched with parameter List";
		    return;
                }
                else
                {
                    free_Memory_Names(size,DataValue1);
                    printf("Parameter attributes does not match with the parameter List\n");
                    response["result"] = "FAILURE";
                    response["details"] = "Parameter Name and its attributes does not match with the parameter List";
		    return;
                }
            }
        }
        free_Memory_Names(size,DataValue1);
        response["result"] = "FAILURE";
        response["details"] = "Parameter Name does not match with the paramters in paramter list";
	return;
    }
}
/***************************************************************************
 *Function name : MTA_agent_GetParameterAttr
 *Descrption    : MTA Component Get Param Attribute API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void MTA_Agent::MTA_agent_GetParameterAttr(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function GetParamAttributes \n");
    int size_ret=0,i=0;
    GETPARAMATTR *DataParamAttr;
    string ParamName=req["ParamName"].asCString();
    DataParamAttr=ssp_getParameterAttr(&ParamName[0],&size_ret);
    if((DataParamAttr == NULL))
    {
        printf("GetParamAttribute funtion returns NULL as o/p\n");
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Parameter Attributes are as :\n");

        for (i=0;i<size_ret;i++)
        {
            printf("Parameter No.%d\n",i);
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Name is %s\n",ParamName.c_str());
            DEBUG_PRINT(DEBUG_TRACE," Access is %s",DataParamAttr[i].pParamAccess);
            DEBUG_PRINT(DEBUG_TRACE," Notification is %s\n",DataParamAttr[i].pParamNotify);
        }

        if(i==size_ret)
        {
            free_Memory_Attr(size_ret,DataParamAttr);
            response["result"] = "SUCCESS";
            response["details"] = "Get Param Attribute Success";
	    return;
        }

    }
    response["result"] = "FAILURE";
    response["details"] = "Get Param Attribute Failure of the function";
    return;

}
/***************************************************************************
 *Function name : MTA_agent_SetParameterAttr
 *Descrption    : MTA Component Set Param Attribute API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - AccessControl : Holds the attribute of the parameter
 * @param [in]  req - Notify : Holds the attribute of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void MTA_Agent::MTA_agent_SetParameterAttr(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function SetParamAttributes \n");
    if((&req["ParamName"]==NULL) || (&req["AccessControl"]==NULL) || (&req["Notify"]==NULL))
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
 	return;
    }

    int size_ret=0,i=0,setResult=0;
    GETPARAMATTR *DataParamAttr1;
    GETPARAMATTR *oldParamAttr;
    string ParamName=req["ParamName"].asCString();
    string AccessControl=req["AccessControl"].asCString();
    string Notify=req["Notify"].asCString();
    oldParamAttr = ssp_getParameterAttr(&ParamName[0],&size_ret);
    if(oldParamAttr == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the attributes of the parameter name";
	return;
    }

    setResult=ssp_setParameterAttr(&ParamName[0],&Notify[0],&AccessControl[0]);

    if(setResult==0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"Parameter Attributes have been set.Needs to cross be checked with Get Parameter Attributes\n");

        sleep(10);
        DataParamAttr1=ssp_getParameterAttr(&ParamName[0],&size_ret);

    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Parameter Attribute has not changed Set Attribute failure";
	return;

    }
    if((strcmp(&Notify[0],"off")!= 0) && (strcmp(&Notify[0],"unchange")!= 0))
    {
        strcpy(&Notify[0],"on");
    }

    /* No change in notify if value is passed as unchange */
    if(strcmp(&Notify[0],"unchange")== 0)
    {
        strcpy(&Notify[0],oldParamAttr[0].pParamNotify);
    }

    /* No change in accessControl if value is passed as unchange */
    if(strcmp(&AccessControl[0],"unchange")== 0)
    {
        strcpy(&AccessControl[0],oldParamAttr[0].pParamAccess);
    }

    if((DataParamAttr1== NULL))
    {
        printf("GetParamAttributes funtion returns NULL as output\n");
    }
    else
    {
        for(i=0;i<size_ret;i++)
        {
            if((strcmp(&Notify[0],DataParamAttr1[i].pParamNotify)==0) && (strcmp(&AccessControl[0],DataParamAttr1[i].pParamAccess)==0))
            {
                printf("Set has been validated successfully\n");
                if(i==(size_ret-1))
                {
                    free_Memory_Attr(size_ret,DataParamAttr1);
                    response["result"] = "SUCCESS";
                    response["details"] = "Set has been validated successfully";
		    return;
                }
            }
            else
            {
                free_Memory_Attr(size_ret,DataParamAttr1);

                response["result"] = "FAILURE";
                response["details"] = "Set failed Attribute does not match";
		return;
            }
        }
    }
    response["result"] = "FAILURE";
    response["details"] = "FAILURE : Get Parameter attribute function returned NULL";
//    return TEST_FAILURE;
    return;
}
/***************************************************************************
 *Function name : MTA_agent_Commit
 *Descrption    : MTA Component Set Param Value API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - ParamValue : Holds the value of the parameter
 * @param [in]  req - Type : Holds the type of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void MTA_Agent::MTA_agent_Commit(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function SetParamValues \n");
    int size_ret=0,i=0,setResult=0,commit=0;
    string ParamName=req["ParamName"].asCString();
    string ParamValue=req["ParamValue"].asCString();
    string Type=req["Type"].asCString();
    GETPARAMVALUES *DataParamValue1;
    GETPARAMVALUES *DataParamValue2;
    setResult=ssp_setParameterValue(&ParamName[0],&ParamValue[0],&Type[0],0);
    if(setResult==0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"Parameter Values have been set.Needs to cross be checked with Get Parameter Names\n");

        DataParamValue1=ssp_getParameterValue(&ParamName[0],&size_ret);
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Parameter value is not SET. Set returns failure";
	return;

    }
    if((DataParamValue1== NULL))
    {
        printf("GetParamValue funtion returns NULL as output\n");
    }
    else
    {

        for(i=0;i<size_ret;i++)
        {
            if(strcmp(&ParamValue[0],&DataParamValue1[i].pParamValues[0])==0)
            {
                printf("Set has reflected in the Parameter even Commit is set to FALSE\n");

                free_Memory_val(size_ret,DataParamValue1);
                response["result"] = "FAILURE";
                response["details"] = "Set has reflected in the Parameter even Commit is set to FALSE";
		return;
            }
        }
        printf("Parameter Value has not changed after Set\n");
    }
    commit=ssp_setCommit(&ParamName[0]); //Calling commit function to commit the Values
    if(commit==0)
    {
        DataParamValue2=ssp_getParameterValue(&ParamName[0],&size_ret);
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Commit failed .";
	return;
    }

    if((DataParamValue2== NULL))
    {
        printf("GetParamValue funtion returns NULL as output\n");
    }
    else
    {

        for(i=0;i<size_ret;i++)
        {
            if(strcmp(&ParamValue[0],&DataParamValue2[i].pParamValues[0])==0)
            {
                free_Memory_val(size_ret,DataParamValue2);
                response["result"] = "SUCCESS";
                response["details"] = "Set has been validated successfully when Commit is done externally";
		return;
            }
        }
        free_Memory_val(size_ret,DataParamValue2);
        printf("Parameter Value has not changed after Set Commit\n");

    }
    response["result"] = "FAILURE";
    response["details"] ="Failure of the Set commit function";
    return;
}
/***************************************************************************
 *Function name : MTA_agent_GetParameterNames_NextLevel
 *Descrption    : MTA Component Get Param Name API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void MTA_Agent::MTA_agent_GetParameterNames_NextLevel(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"MTA_agent_GetParameterNames_NextLevel \n");
    string ParamName=req["ParamName"].asCString();
    GETPARAMNAMES *DataValue;
    int size_ret=0;
    DataValue=ssp_getParameterNames(&ParamName[0],0,&size_ret);
    if(NULL==DataValue)
    {
        response["result"] = "FAILURE";
        response["details"] = "Get Param Name for Parameter returned NULL";
	return;
    }
    else
    {
        free_Memory_Names(size_ret,DataValue);
        response["result"] = "SUCCESS";
        response["details"] = "Get Param Names success";
	return;

    }
}

/***************************************************************************
 *Function name : MTA_agent_AddTbl
 *Descrption    : In MTA Component, to add instances of a paramter functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void MTA_Agent::MTA_agent_AddTbl(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function Add table functionality \n");
    int size_ret=0;
    string ParamName=req["ParamName"].asCString();
    size_ret=ssp_addTableRow(&ParamName[0]);
    if((size_ret == 1))
    {
        printf("Add table funciton failed, for read-only Paramter\n");
    }
    else
    {
        printf("Add table function passed for read-only parameter");
        response["result"] = "FAILURE";
        response["details"] = "Add table function passed for read-only parameter";
	return;

    }
    response["result"] = "SUCCESS";
    response["details"] = "Add table funciton failed for read-only Paramter";
    return;

}
/***************************************************************************
 *Function name : MTA_agent_DelTble
 *Descrption    : In MTA Component, to delete instances of a paramter functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void MTA_Agent::MTA_agent_DelTble(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function Delete table functionality \n");
    int size_ret=0;
    string ParamName=req["ParamName"].asCString();
    size_ret=ssp_addTableRow(&ParamName[0]);
    if((size_ret == 1))
    {
        printf("Delete table funciton failed for read-only Parmeter\n");
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "Delete table function passed for read-only parameter";
	return;

    }
    response["result"] = "SUCCESS";
    response["details"] = "Delete table funciton failed for read-only Parmeter";
    return;

}
/***************************************************************************
 *Function name : MTA_agent_GetHealth
 *Descrption    : In MTA Component, to get working condition of ccsp Component
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void MTA_Agent::MTA_agent_GetHealth(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function Get Health functionality \n");
    int size_ret=0;
    string ParamName=req["ParamName"].asCString();
    size_ret=ssp_getHealth(&ParamName[0]);
    if((size_ret == 1))
    {
        printf("Failed to retrieve the component health\n");
    }
    else
    {
        printf("Successfully retrieved the health of the component");
        response["result"] = "SUCCESS";
        response["details"] = "Successfully retrieved the health of the component";
	return;

    }
    response["result"] = "FAILURE";
    response["details"] = "Failed to retrieve the component health";
    return;

}
/***************************************************************************
 *Function name : MTA_agent_SetSessionId
 *Descrption    : In MTA Component, to set session id of ccsp Component
 *
 * @param [in]  req - Priority : Holds the int value
 * @param [in]  req - SessionId : Holds the session ID value
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void MTA_Agent::MTA_agent_SetSessionId(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTA_agent_SetSessionId --->Entry\n");
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

    DEBUG_PRINT(DEBUG_TRACE,"\nMtaAgent_SetSessionId:: priority is %d",priority);
    DEBUG_PRINT(DEBUG_TRACE,"\nMtaAgent_SetSessionId:: sessionId is %d",sessionId);
    DEBUG_PRINT(DEBUG_TRACE,"\nMtaAgent_SetSessionId:: override is %d",override);
    DEBUG_PRINT(DEBUG_TRACE,"\nMtaAgent_SetSessionId:: pathname is %s",pathname);


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
        response["details"]="MtaAgent_Stub::SET SESSION ID API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n MtaAgent_SetSessionId --->Error in setting the session Id !!! \n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MtaAgent_SetSessionId --->Exit\n");
    return;

}

/**************************************************************************
Function name : MTA_agent_Terminate

Description   : Terminating the session of MTA AGENT CCSP component
 **************************************************************************/
void MTA_Agent::MTA_agent_Terminate(IN const Json::Value& req, OUT Json::Value& response)
{
    int i=0;
    DEBUG_PRINT(DEBUG_TRACE,"Terminating MTA AGENT component Session\n");
    i=ssp_terminate();
    if(i==0)
    {
        response["result"] = "SUCCESS";
        response["details"] = "Termination Success";
	return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "Termination Failure";
	return;
    }
}


/**************************************************************************
Function name : MTA_Agent::initialize

Arguments     : Input arguments are Version string and MTA_Agent obj ptr

Description   : Registering all the wrapper functions with the agent for using these functions in the script
 ***************************************************************************/
bool MTA_Agent::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE, "MTA_Agent Initialize----->Entry\n");
    return TEST_SUCCESS;
}
/**************************************************************************
Function Name   : CreateObject

Arguments       : NULL

Description     : This function is used to create a new object of the class "MTA_Agent".
 **************************************************************************/

extern "C" MTA_Agent* CreateObject(TcpSocketServer &ptrtcpServer)
{
	return new MTA_Agent(ptrtcpServer);
}

/**************************************************************************
Function Name   : cleanup

Arguments       : NULL

Description     : This function will be used to the close things cleanly.
 **************************************************************************/
bool MTA_Agent::cleanup(IN const char* szVersion)
{
	DEBUG_PRINT(DEBUG_TRACE, "cleaningup\n");
	return TEST_SUCCESS;
}

/**************************************************************************
Function Name : DestroyObject

Arguments     : Input argument is MTA_Agent Object

Description   : This function will be used to destory the MTA_Agent object.
 **************************************************************************/
extern "C" void DestroyObject(MTA_Agent *stubobj)
{
	DEBUG_PRINT(DEBUG_TRACE, "Destroying MTA_Agent object\n");
	delete stubobj;
		}
