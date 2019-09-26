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
#include "TR069Agent.h"
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
}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Descrption    : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string TR069Agent::testmodulepre_requisites()
{
    int returnVal=0;

    DEBUG_PRINT(DEBUG_TRACE,"testmodulepre_requisites::Initiate to register with Component register\n");

    returnVal=ssp_register(1);
    if(returnVal == 0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"testmodulepre_requisites::WECB stub registered with CR\n");
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
bool TR069Agent::testmodulepost_requisites()
{
    int returnVal=0;

    DEBUG_PRINT(DEBUG_TRACE,"Initiate to unregistered from Component register\n");

    returnVal=ssp_terminate();
    if(returnVal == 0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"TR069 stub unregistered from CR \n");
        return TEST_SUCCESS;
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Failed to unregistered from CR\n");
        return TEST_FAILURE;
    }
}
/***************************************************************************
 *Function name : TR069Agent_Init
 *Descrption    : TR069Agent_Init will be used for intiating
 *                in CCSP module
 *
 *****************************************************************************/
void TR069Agent::TR069Agent_Init(IN const Json::Value& req, OUT Json::Value& response)
{
    int i=0;
    DEBUG_PRINT(DEBUG_TRACE,"Intiating a session with TR069 component\n");
    i=ssp_register(1);
    if(i==0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"TR069 Component is intiated \n");
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
 *Function name : TR069Agent_GetParameterValues
 *Descrption    : TR069Pa Component Get Param Value API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void TR069Agent::TR069Agent_GetParameterValues(IN const Json::Value& req, OUT Json::Value& response)
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
    response["result"] = "FAILURE";
    response["details"] = "Get Param value Failure of the function";
    return;

}

/***************************************************************************
 *Function name : TR069Agent_SetParameterValues
 *Descrption    : TR069Pa Component Set Param Value API functionality checking
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - ParamValue : Holds the value of the parameter
 * @param [in]  req - Type : Holds the Type of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *****************************************************************************/
void TR069Agent::TR069Agent_SetParameterValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function SetParamValues \n");
    int size_ret=0,i=0,setResult=0;
    GETPARAMVALUES *DataParamValue1;
    string ParamName=req["ParamName"].asCString();
    string ParamValue=req["ParamValue"].asCString();
    string Type=req["Type"].asCString();

    setResult=ssp_setParameterValue(&ParamName[0],&ParamValue[0],&Type[0],1);
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
        if(strcmp(&ParamValue[0],&DataParamValue1[i].pParamValues[0])==0)
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
 *Function name : TR069Agent_GetParameterNames
 *Descrption    : TR069 Component Get Param Name API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - ParamList : Holds the List of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void TR069Agent::TR069Agent_GetParameterNames(IN const Json::Value& req, OUT Json::Value& response)
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
 *Function name : TR069Agent_GetParameterAttr
 *Descrption    : TR069Pa Component Get Param Attribute API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void TR069Agent::TR069Agent_GetParameterAttr(IN const Json::Value& req, OUT Json::Value& response)
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
 *Function name : TR069Agent_SetParameterAttr
 *Descrption    : TR069Pa Component Set Param Attribute API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - AccessControl : Holds the attribute of the parameter
 * @param [in]  req - Notify : Holds the attribute of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void TR069Agent::TR069Agent_SetParameterAttr(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function SetParamAttributes \n");
    int size_ret=0,i=0,setResult=0;
    GETPARAMATTR *DataParamAttr1;
    string ParamName=req["ParamName"].asCString();
    string AccessControl=req["AccessControl"].asCString();
    string Notify=req["Notify"].asCString();

    setResult=ssp_setParameterAttr(&ParamName[0],&Notify[0],&AccessControl[0]);
    if(setResult==0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"Parameter Attributes have been set.Needs to cross be checked with Get Parameter Attributes\n");
        DataParamAttr1=ssp_getParameterAttr(&ParamName[0],&size_ret);

    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Parameter attribute is not SET. Set returns failure";
        return;
    }

    if((DataParamAttr1== NULL))
    {
        printf("SetParamAttributes funtion returns NULL as output\n");
    }
    else
    {
        for(i=0;i<size_ret;i++)
        {
            if(strcmp(Notify.c_str(),"off")!=0)
            {
                strcpy(&Notify[0],"on");
            }
            if((strcmp(&Notify[0],&DataParamAttr1[i].pParamNotify[0])==0) && (strcmp(&AccessControl[0],&DataParamAttr1[i].pParamAccess[0])==0))
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
                response["details"] = "Set failed";
                return;
            }
        }
    }

    response["result"] = "FAILURE";
    response["details"] = "FAILURE : Parameter Attribute has not changed after a proper Set";
    return;
}


/**************************************************************************
  Function name : TR069Agent::Terminate

Description   : Terminating the session of TR069 PA CCSP component
 ***************************************************************************/
void TR069Agent::TR069Agent_Terminate(IN const Json::Value& req, OUT Json::Value& response)
{
    int i=0;
    DEBUG_PRINT(DEBUG_TRACE,"Terminating TR069 component Session\n");
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
  Function name : TR069Agent::initialize

Arguments     : Input arguments are Version string and TR069Agent obj ptr

Description   : Registering all the wrapper functions with the agent for using these functions in the script
 ***************************************************************************/
bool TR069Agent::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE, "TR069Agent Initialize\n");
    return TEST_SUCCESS;
}

/**************************************************************************
  Function Name   : CreateObject

Arguments       : NULL

Description     : This function is used to create a new object of the class "TR069Agent".
 **************************************************************************/

extern "C" TR069Agent* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new TR069Agent(ptrtcpServer);
}

/**************************************************************************
  Function Name   : cleanup

Arguments       : NULL

Description     : This function will be used to the close things cleanly.
 **************************************************************************/
bool TR069Agent::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE, "cleaningup\n");
    return TEST_SUCCESS;
}

/**************************************************************************
  Function Name : DestroyObject

Arguments     : Input argument is TR069Agent Object

Description   : This function will be used to destory the TR069Agent object.
 **************************************************************************/
extern "C" void DestroyObject(TR069Agent *stubobj)
{
    DEBUG_PRINT(DEBUG_TRACE, "Destroying TR069Agent object\n");
    delete stubobj;
}
