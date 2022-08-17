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
#include "LMLite_Stub.h"
#include "ssp_tdk_wrp.h"

/* To provide external linkage to C Functions defined in TDKB Component folder */
extern "C"
{
    int ssp_register(bool);
    int ssp_terminate();
    GETPARAMVALUES* ssp_getParameterValue(char *pParamName,int *pParamsize);
    int ssp_setParameterValue(char *pParamName,char *pParamValue,char *pParamType, int commit);
    void free_Memory_val(int size,GETPARAMVALUES *Freestruct);

};

/***************************************************************************
 *Function name : initialize
 *Description   : Initialize Function will be used for registering the wrapper method
 *                with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/

bool LMLiteStub::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE,"TDK::LMLiteStub Initialize\n");

    return TEST_SUCCESS;

}

/***************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string LMLiteStub::testmodulepre_requisites()
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
bool LMLiteStub::testmodulepost_requisites()
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
 * Function Name        : LMLiteStub_Get
 * Description          : This function will invoke TDK Component GET Value wrapper
 *                        function to get parameter value
 *
 * @param [in] req- This holds Path name for Parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                         ssp_getParameterValue
 ********************************************************************************************/

void LMLiteStub::LMLiteStub_Get(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n LMLiteStub_Get --->Entry\n");

    char ParamNames[MAX_PARAM_SIZE];
    GETPARAMVALUES *resultDetails;
    int paramsize=0;

    strcpy(ParamNames,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n ParamNames input is %s",ParamNames);

    resultDetails = ssp_getParameterValue(&ParamNames[0],&paramsize);

    if(resultDetails == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="Get Parameter Value API Validation Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n LMLiteStub_Get --->Exit\n");
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

    DEBUG_PRINT(DEBUG_TRACE,"\n LMLiteStub_Get --->Exit\n");

    return;
}
/***************************************************************************
 *Function name : LMLiteStub_Set
 *Descrption    : LMLite Component Set Param Value API functionality checking
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - ParamValue : Holds the value of the parameter
 * @param [in]  req - Type : Holds the Type of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *****************************************************************************/
void LMLiteStub::LMLiteStub_Set(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"LMLiteStub_Set --->Entry \n");

    int size_ret=0,i=0,setResult=0;
    char ParamName[MAX_PARAM_SIZE];
    char ParamValue[MAX_PARAM_SIZE];
    char Type[MAX_PARAM_SIZE];
    strcpy(ParamName,req["ParamName"].asCString());
    strcpy(ParamValue,req["ParamValue"].asCString());
    strcpy(Type,req["Type"].asCString());

    GETPARAMVALUES *DataParamValue1;

    setResult=ssp_setParameterValue(&ParamName[0],&ParamValue[0],&Type[0],1);
    if(setResult==0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"Parameter Values have been set.Needs to be cross checked with Get Parameter Names\n");
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

/*******************************************************************************************
 *
 * Function Name         : LMLiteStub_Set_Get
 * Description           : This function will invoke TDK Component SET and GET Value wrapper
 *                         function for functional Validation
 * @param [in] req       : This holds Path name, Value to set and its type
 * @param [out] response : filled with SUCCESS or FAILURE based on the return value of
 *                         ssp_setParameterValue and ssp_getParameterValue
 ********************************************************************************************/
void LMLiteStub::LMLiteStub_Set_Get(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\nLMLiteStub_Set_Get --->Entry\n");

    int returnValue = 0;
    char ParamName[MAX_PARAM_SIZE];
    char ParamValue[MAX_PARAM_SIZE];
    char ParamType[MAX_PARAM_SIZE];
    GETPARAMVALUES *resultDetails;
    int paramsize=0;
    int commit = 1;

    if(&req["ParamName"] == NULL || &req["ParamValue"] == NULL || &req["ParamType"] == NULL)
    {
        response["result"] = "FAILURE";
        response["details"] = "NULL parameter as input argument";
        return;
    }

    //Set Param
    strcpy(ParamName,req["ParamName"].asCString());
    strcpy(ParamValue,req["ParamValue"].asCString());
    strcpy(ParamType,req["ParamType"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nLMLiteStub_Set_Get:: ParamName input is %s",ParamName);
    DEBUG_PRINT(DEBUG_TRACE,"\nLMLiteStub_Set_Get:: ParamValue input is %s",ParamValue);
    DEBUG_PRINT(DEBUG_TRACE,"\nLMLiteStub_Set_Get:: ParamType input is %s",ParamType);

    //Setting the parameter value
    returnValue = ssp_setParameterValue(&ParamName[0],&ParamValue[0],&ParamType[0],commit);

    if(0 == returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\nLMLiteStub_Set_Get --->Set operation success in DUT !!! \n");
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="LMLiteStub::SET Operation is Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\nLMLiteStub_Set_Get --->Error in Set operation in DUT !!! \n");
        return;
    }

    //Getting the parameter value
    resultDetails = ssp_getParameterValue(&ParamName[0],&paramsize);

    if(resultDetails == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="Get Parameter Value Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\nLMLiteStub_Set_Get --->Error in Get operation in DUT !!! \n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\nLMLiteStub_Set_Get:: Value of resultDetails[0].pParamValues is %s and strlen is %d",resultDetails[0].pParamValues,strlen((const char *)resultDetails[0].pParamValues));
    DEBUG_PRINT(DEBUG_TRACE,"\nLMLiteStub_Set_Get:: Value of ParamValue[0] is %s and strlen is %d",&ParamValue[0],strlen((const char *)&ParamValue[0]));

    if((strcmp(resultDetails[0].pParamValues,&ParamValue[0])) == 0)
    {
        response["result"]="SUCCESS";
        response["details"]="Set Get Functional Validation is success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Set Get Functional Validation failed";
        DEBUG_PRINT(DEBUG_TRACE,"\nLMLiteStub_Set_Get --->Error in Functional Validation in DUT !!! \n");
    }

    if(resultDetails != NULL)
    {
        for(int i=0; i < paramsize; i++)
        {
            free(resultDetails[i].pParamValues);
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\nLMLiteStub_Set_Get --->Exit\n");
    return;
}

/**************************************************************************
 * Function Name        : CreateObject
 * Description  : This function will be used to create a new object for the
 *                class "LMLiteStub".
 *
 **************************************************************************/

extern "C" LMLiteStub* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new LMLiteStub(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/

bool LMLiteStub::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"LMLiteStub shutting down\n");
    return TEST_SUCCESS;
}


/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(LMLiteStub *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying LMLiteStub object\n");
    delete stubobj;
}
