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
#include "TAD_stub.h"
#include "ssp_tdk_wrp.h"

/* To provide external linkage to C Functions defined in TDKB Component folder */


extern "C"
{
    int ssp_register(bool);
    int ssp_terminate();
    GETPARAMVALUES* ssp_getParameterValue(char *pParamName,int *pParamsize);
    int ssp_setParameterValue(char *pParamName,char *pParamValue,char *pParamType, int commit);
    void free_Memory_val(int size,GETPARAMVALUES *Freestruct);
    int ssp_Diag_Init();
    int ssp_Diag_Start(int mode);
    int ssp_Diag_Stop(int mode);
    int ssp_Diag_SetCfg(int mode, diag_cfg *cfg);
    int ssp_Diag_GetCfg(int mode, diag_cfg *cfg);
    int ssp_Diag_GetState(int mode, int *state);

};

/***************************************************************************
 *Function name : initialize
 *Description   : Initialize Function will be used for registering the wrapper method
 *                with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/

bool TADstub::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE,"TDK::TADstub Initialize\n");

    return TEST_SUCCESS;

}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string TADstub::testmodulepre_requisites()
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
bool TADstub::testmodulepost_requisites()
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
 * Function Name        : TADstub_Get
 * Description          : This function will invoke TDK Component GET Value wrapper
 *                        function to get parameter value
 *
 * @param [in] req- This holds Path name for Parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                         ssp_getParameterValue
 ********************************************************************************************/

void TADstub::TADstub_Get(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n TADstub_Get --->Entry\n");

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
        DEBUG_PRINT(DEBUG_TRACE,"\n TADstub_Get --->Exit\n");
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

    DEBUG_PRINT(DEBUG_TRACE,"\n TADstub_Get --->Exit\n");

    return;
}
/***************************************************************************
 *Function name : TADstub_Set
 *Descrption    : TAD Component Set Param Value API functionality checking
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - ParamValue : Holds the value of the parameter
 * @param [in]  req - Type : Holds the Type of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *****************************************************************************/
void TADstub::TADstub_Set(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"TADstub_Set --->Entry \n");

    int size_ret=0,i=0,setResult=0;
    char ParamName[MAX_PARAM_SIZE];
    char ParamValue[MAX_PARAM_SIZE];
    char Type[MAX_PARAM_SIZE];
    strcpy(ParamName,req["ParamName"].asCString());
    strcpy(ParamValue,req["ParamValue"].asCString());
    strcpy(Type,req["Type"].asCString());

    GETPARAMVALUES *DataParamValue1;
    char oldParamValue[50] = {0};
    char newParamValue[50] = {0};
    int src, dst=0;

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
        printf("ParamValue that is set:%s\n",&ParamValue[0]);
        printf("Value Retrieved after set:%s\n",&DataParamValue1[i].pParamValues[0]);

        strcpy(oldParamValue, &DataParamValue1[i].pParamValues[0]);

        printf("Check for any special characters appened in the value retrieved and remove\n");
        for (src=0; oldParamValue[src] != 0; src++)
        if (oldParamValue[src] != '\'')
        {
             newParamValue[dst] = oldParamValue[src];
             dst++;
        }
        newParamValue[dst] = 0;

        printf("Value after truncating special characters:%s\n",newParamValue);

        if(strcmp(&ParamValue[0], newParamValue)==0)
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
 *Function name : TADstub_SetDiagnosticsState
 *Descrption    : TAD Component SetDiagnosticsState API functionality checking
 * @param [in]  req - ParamName : Holds the name of the parameter
 * @param [in]  req - ParamValue : Holds the value of the parameter
 * @param [in]  req - Type : Holds the Type of the parameter
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *****************************************************************************/
void TADstub::TADstub_SetDiagnosticsState(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"TADstub_SetDiagnosticsState --->Entry \n");

    int setResult=0;
    char ParamName[MAX_PARAM_SIZE];
    char ParamValue[MAX_PARAM_SIZE];
    char Type[MAX_PARAM_SIZE];
    strcpy(ParamName,req["ParamName"].asCString());
    strcpy(ParamValue,req["ParamValue"].asCString());
    strcpy(Type,req["Type"].asCString());

    setResult=ssp_setParameterValue(&ParamName[0],&ParamValue[0],&Type[0],1);
    if(setResult==0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"Parameter Values have been set.\n");
        response["result"] = "SUCCESS";
        response["details"] = "Set has been validated successfully";
        return;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Parameter value is not SET. Set returns failure";
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : TADstub_Init
 * Description          : This function will invoke ssp wrapper for diagnostics init function
 *
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 ********************************************************************************************/

void TADstub::TADstub_Init(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"TADstub_Init --->Entry \n");
    int status;

    status = ssp_Diag_Init();
    if(status)
    {
        printf("TADstub_Init failed\n");
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Diag init failed";
        return;
    }
    else
    {
        printf("TADstub_Init success\n");
        response["result"] = "SUCCESS";
        response["details"] = "SUCCESS : Diag init success";
        return;
    }
}


/***************************************************************************
 *Function name : TADstub_Start
 *Descrption    : This function will invoke ssp wrapper for diagnostics start function

 * @param [in]   - mode : Specifies whether mode is ping or traceroute
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *****************************************************************************/
void TADstub::TADstub_Start(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"TADstub_Start --->Entry \n");
    int status;
    int mode = req["mode"].asInt();

    status = ssp_Diag_Start(mode);
    if(status)
    {
        printf("TADstub_Start failed\n");
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Diag start failed";
        return;
    }
    else
    {
        printf("TADstub_Start success\n");
        response["result"] = "SUCCESS";
        response["details"] = "SUCCESS : Diag start success";
        return;
    }
}


/***************************************************************************
 *Function name : TADstub_Stop
 *Descrption    : This function will invoke ssp wrapper for diagnostics stop function

 * @param [in]   - mode : Specifies whether mode is ping or traceroute
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *****************************************************************************/
void TADstub::TADstub_Stop(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"TADstub_Stop --->Entry \n");
    int status;
    int mode = req["mode"].asInt();

    status = ssp_Diag_Stop(mode);
    if(status)
    {
        printf("TADstub_Stop failed\n");
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Diag stop failed";
        return;
    }
    else
    {
        printf("TADstub_Stop success\n");
        response["result"] = "SUCCESS";
        response["details"] = "SUCCESS : Diag stop success";
        return;
    }
}


/***************************************************************************
 *Function name : TADstub_SetCfg
 *Descrption    : This function will invoke ssp wrapper for diagnostics setCfg function
                for setting the config values of diagnostics

 * @param [in]   - mode : Specifies whether mode is ping or traceroute
 * @param [in]   - host : Specifies the host name
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *****************************************************************************/
void TADstub::TADstub_SetCfg(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"TADstub_Stop --->Entry \n");
    int status;
    diag_cfg cfg;
    int mode = req["mode"].asInt();
    strcpy(cfg.host, req["host"].asCString());

    status = ssp_Diag_SetCfg(mode, &cfg);
    if(status)
    {
        printf("TADstub_SetCfg failed\n");
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Diag setcfg failed";
        return;
    }
    else
    {
        printf("TADstub_SetCfg success\n");
        response["result"] = "SUCCESS";
        response["details"] = "SUCCESS : Diag setCfg success";
        return;
    }
}


/***************************************************************************
 *Function name : TADstub_SetCfg
 *Descrption    : This function will invoke ssp wrapper for diagnostics getCfg function
                for setting the config values of diagnostics

 * @param [in]   - mode : Specifies whether mode is ping or traceroute
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *****************************************************************************/
void TADstub::TADstub_GetCfg(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"TADstub_Stop --->Entry \n");
    int status;
    diag_cfg cfg; char result[200] = {'\0'};
    int mode = req["mode"].asInt();

    status = ssp_Diag_GetCfg(mode, &cfg);
    if(status)
    {
        printf("TADstub_GetCfg failed\n");
        response["result"] = "FAILURE";
        response["details"] = "FAILURE : Diag getcfg failed";
        return;
    }
    else
    {
        printf("TADstub_GetCfg success\n");
        response["result"] = "SUCCESS"; sprintf(result, "host fromcfg is %s", cfg.host);
        response["details"] = result;
        return;
    }
}


/***************************************************************************
 *Function name : TADstub_GetState
 *Descrption    : This function will invoke ssp wrapper for diagnostics getState function
                for getting the diagnostics state

 * @param [in]   - mode : Specifies whether mode is ping or traceroute
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value
 *
 *****************************************************************************/

void TADstub::TADstub_GetState(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"TADstub_State --->Entry \n");
    int status;
    int mode = req["mode"].asInt();
    int state;
    char result[200] = {'\0'};

    status = ssp_Diag_GetState(mode, &state);
    sprintf(result, "state is %d", state);
    if(status)
    {
        printf("TADstub_GetState failed\n");
        response["result"] = "FAILURE";
        response["details"] = result;
        return;
    }
    else
    {
        printf("TADstub_GetState success\n");
        response["result"] = "SUCCESS";
        response["details"] = result;
        return;
    }
}


/**************************************************************************
 * Function Name        : CreateObject
 * Description  : This function will be used to create a new object for the
 *                class "TADstub".
 *
 **************************************************************************/

extern "C" TADstub* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new TADstub(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/

bool TADstub::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"TADstub shutting down\n");

    return TEST_SUCCESS;
}


/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(TADstub *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying TADstub object\n");
    delete stubobj;
}


