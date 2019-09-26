/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2018 RDK Management
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
#include "tdkb_tr181_stub.h"
#include "ssp_tdk_wrp.h"
/* To provide external linkage to C Functions defined in TDKB Component folder */
extern "C"
{
    int ssp_register(bool);
    int ssp_terminate();
    GETPARAMVALUES* ssp_getParameterValue(char *pParamName,int *pParamsize);
    int ssp_setParameterValue(char *pParamName,char *pParamValue,char *pParamType, int commit);
    int ssp_addTableRow(char *pObjTbl,int *pInstanceNumber);
    int ssp_deleteTableRow(char *pObjTbl);
    int ssp_setMultipleParameterValue(char **paramList, int size);
    void free_Memory_val(int size,GETPARAMVALUES *Freestruct);
};
/***************************************************************************
 *Function name : initialize
 *Description   : Initialize Function will be used for registering the wrapper method
 *                with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/
bool TDKB_TR181Stub::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE,"TDK::TDKB_TR181Stub Initialize\n");
    return TEST_SUCCESS;
}
/***************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string TDKB_TR181Stub::testmodulepre_requisites()
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
bool TDKB_TR181Stub::testmodulepost_requisites()
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

/***************************************************************************
 *Function name : TDKB_TR181Stub_Get
 *Descrption    : Get Param Value API functionality checking
 *
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *****************************************************************************/
void TDKB_TR181Stub::TDKB_TR181Stub_Get(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function TDKB_TR181Stub_Get \n");
    int size_ret=0;
    GETPARAMVALUES *DataParamValue;
    string ParamName=req["ParamName"].asCString();
    DataParamValue=ssp_getParameterValue(&ParamName[0],&size_ret);
    if((DataParamValue == NULL))
    {
        printf("TDKB_TR181Stub_Get funtion returns NULL as o/p\n");
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Parameter Values are as :\n");
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Name is %s\n",ParamName.c_str());
            DEBUG_PRINT(DEBUG_TRACE,"Value is %s",DataParamValue[0].pParamValues);
            DEBUG_PRINT(DEBUG_TRACE," Type is %d\n",DataParamValue[0].pParamType);
            response["result"] = "SUCCESS";
            response["details"] = DataParamValue[0].pParamValues;
            free_Memory_val(size_ret,DataParamValue);
            return;
    }
    response["result"] = "FAILURE";
    response["details"] = "Failed to get the value of parameter";
    return;
}

/***************************************************************************
 *Function name :TDKB_TR181Stub _Set
 *Descrption    : Component Set Param Value API functionality checking
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - ParamValue : Holds the value of the parameter
 * @param [in]  req - Type : Holds the Type of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *****************************************************************************/
void TDKB_TR181Stub::TDKB_TR181Stub_Set(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"Inside Function TDKB_TR181Stub_Set \n");
    int size_ret=0,i=0,setResult=0;
    char Details[80] = {'\0'};
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
        sprintf(Details,"FAILURE : Parameter value is not SET. Set returns failure with errorcode :%d", setResult);
        response["result"] = "FAILURE";
        response["details"] = Details;
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

/*******************************************************************************************
 *
 * Function Name        : TDKB_TR181Stub_AddObject
 * Description          : Add a row to the table object
 *
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                         ssp_addTableRow
********************************************************************************************/
void TDKB_TR181Stub::TDKB_TR181Stub_AddObject(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TDKB_TR181Stub_AddObject --->Entry\n");
    int returnValue = 0;
    char paramName[MAX_PARAM_SIZE];
    int instanceNumber = 0;
    char Details[80] = {'\0'};
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
        return;
    }
    strcpy(paramName,req["paramName"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\nTDKB_TR181Stub_AddObject:: ParamName input is %s",paramName);
    returnValue = ssp_addTableRow(&paramName[0],&instanceNumber);
    if(0 == returnValue)
    {
        sprintf(Details,"ADD OBJECT API Validation is Success.Instance Number is :%d", instanceNumber);
        DEBUG_PRINT(DEBUG_TRACE,"\nTDKB_TR181Stub_AddObject::instance added is %d",instanceNumber);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="TDKB_TR181Stub::ADD OBJECT API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n TDKB_TR181Stub_AddObject --->Error in adding object !!! \n");
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n TDKB_TR181Stub_AddObject --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : TDKB_TR181Stub_SetMultiple
 * Description          : This function will set multiple parameter value at one shot
 *
 * @param [in] req-        ParamList will hold the entire list to be set.
 *
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                         ssp_setMultipleParameterValue
********************************************************************************************/
void TDKB_TR181Stub::TDKB_TR181Stub_SetMultiple(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TDKB_TR181Stub_SetMultiple --->Entry\n");
    int returnValue = 0;
    char params[1000] = {'\0'};
    char **paramlist  = NULL;
    int num_spaces = 0;
    int index = 0;
    int size = 0;
    strcpy(params,req["paramList"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\nTDKB_TR181Stub_Set:: ParamList input is %s\n",params);
    char *list = strtok (params, "|");
    while (list) {
    paramlist = (char **) realloc (paramlist, ++num_spaces * sizeof(char *));
    if (paramlist == NULL)
    return; /* memory allocation failed */
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
       response["details"]="TDKB_TR181Stub::SET API Validation is Failure";
       DEBUG_PRINT(DEBUG_TRACE,"\n TDKB_TR181Stub_SetMultiple: Failed to set multiple parameters !!! \n");
   }
    /* free the memory allocated */
   free(paramlist);
   DEBUG_PRINT(DEBUG_TRACE,"\n TDKB_TR181Stub_SetMultiple --->Exit\n");
   return;
}

/*******************************************************************************************
 *
 * Function Name        : TDKB_TR181Stub_DelObject
 * Description          : Delete a row from the table object
 *
 * @param [in] req-     This holds parameter path name
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                         ssp_deleteTableRow
********************************************************************************************/
void TDKB_TR181Stub::TDKB_TR181Stub_DelObject(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TDKB_TR181Stub_DelObject --->Entry\n");
    int returnValue = 0;
    char paramName[MAX_PARAM_SIZE];
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
    DEBUG_PRINT(DEBUG_TRACE,"\nTDKB_TR181Stub_DelObject:: ParamName input is %s",paramName);
    DEBUG_PRINT(DEBUG_TRACE,"\nTDKB_TR181Stub_DelObject:: apiTest input is %d",apitest);
    if(apitest != 0)
    {
        returnValue = ssp_addTableRow(&paramName[0],&instanceNumber);
        if(returnValue == 0)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\nTDKB_TR181Stub_AddObject::Object added with instance %d",instanceNumber);
            sin << instanceNumber;
            std::string val = sin.str();
            strcat(paramName,val.c_str());
            strcat(paramName,".");
        }
    }
    DEBUG_PRINT(DEBUG_TRACE,"\nTDKB_TR181Stub_DelObject:: Modified ParamName input is %s",paramName);
    returnValue = ssp_deleteTableRow(&paramName[0]);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="DELETE OBJECT API Validation is Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="TDKB_TR181Stub::Delete Object API Validation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n TDKB_TR181Stub_DelObject --->Error in deleting object !!! \n");
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n TDKB_TR181Stub_DelObject --->Exit\n");
    return;
}

/**************************************************************************
 * Function Name        : CreateObject
 * Description  : This function will be used to create a new object for the
 *                class "TDKB_TR181Stub".
 *
 **************************************************************************/
extern "C" TDKB_TR181Stub* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new TDKB_TR181Stub(ptrtcpServer);
}
/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/
bool TDKB_TR181Stub::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"TDKB_TR181Stub shutting down\n");
    return TEST_SUCCESS;
}
/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(TDKB_TR181Stub *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying TDKB_TR181Stub object\n");
    delete stubobj;
}

