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
#include "CCSPMBUS_Stub.h"
#include "ssp_tdk_wrp.h"
#include "ssp_tdk_mbus_wrp.h"

/* To provide external linkage to C Functions defined in TDKB Component folder */
extern "C"
{
    /* Wrapper Functions to invoke RDKB API's */
    int ssp_register(bool);
    int ssp_terminate();
    GETPARAMVALUES* ssp_getParameterValue(char *pParamName,int *paramsize);
    int ssp_setParameterValue(char *pParamName,char *pParamValue,char *pParamType, int commit);
    GETPARAMATTR* ssp_getParameterAttr(char *pParamAttr,int *pParamAttrSize);
    int ssp_setParameterAttr(char *pParamName,char *pAttrNotify,char *pAttrAccess);
    GETPARAMNAMES* ssp_getParameterNames(char *pPathName,int recursive,int *pParamSize);
    int ssp_addTableRow(char *pObjTbl,int *pInstanceNumber);
    int ssp_deleteTableRow(char *pObjTbl);
    int ssp_setCommit(char *pObjTbl);
    int ssp_setSessionId(int priority, int sessionId);
    void free_Memory_Names(int size,GETPARAMNAMES *Freestruct);
    void free_Memory_val(int size,GETPARAMVALUES *Freestruct);
    void free_Memory_Attr(int size,GETPARAMATTR *Freestruct);

    int ssp_mbus_init(char *pCfg);
    int ssp_mbus_exit();
    int ssp_mbus_register_event(char *pEvtName);
    int ssp_mbus_unregister_event(char *pEvtName);
    int ssp_mbus_loadcfg(char *pCfg);
    int ssp_mbus_load_dmlxml(char *pCmpDmXml);
    int ssp_mbus_register_path();
    int ssp_mbus_query_status();
    int ssp_mbus_get_allocmemory();
    int ssp_mbus_get_maxmemory();
    int ssp_mbus_register_capabilities();
    int ssp_mbus_unregister_namespace();
    int ssp_mbus_unregistercomponent();
    int ssp_mbus_namespace_supportedby_component();
    int ssp_mbus_component_supporting_dynamictbl();
    int ssp_mbus_get_registered_components();
    int ssp_mbus_check_namespace_datatype();
    int ssp_mbus_dump_component_registry();
    int ssp_mbus_issystem_ready();
    int ssp_mbus_bus_check();
    int ssp_mbus_inform_end_session();
    int ssp_mbus_req_sessionid();
    int ssp_mbus_register_base();
    int ssp_mbus_getHealth(char *cmpId, char*cmpPath);
    int ssp_mbus_SendsystemReadySignal(void);
    int ssp_mbus_unloadcfg();

};

/***************************************************************************
 *Function name	: initialize
 *Description	: Initialize Function will be used for registering the wrapper method
 *  	  	  with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/

bool CCSPMBUS::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE,"CCSPMBUS Initialize\n");
    return TEST_SUCCESS;
}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string CCSPMBUS::testmodulepre_requisites()
{
    int returnValue = 0;
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
bool CCSPMBUS::testmodulepost_requisites()
{

    return TEST_SUCCESS;
}


/*******************************************************************************************
 *
 * Function Name        : CCSPMBUS_GetParamValues
 * Description          : This function will retrieve the list of parameter values
 *                        associated with the specified namespace
 *
 * @param [in] req      : paramName - Specific parameter name for which value to be retrieved
 *
 * @param [out] response - SUCCESS - All parameter values are retrieved
 *                         FAILURE - Failed to retrieve the parameter values
 ********************************************************************************************/
void CCSPMBUS::CCSPMBUS_GetParamValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetParamValues --->Entry\n");

    char paramName[MAX_PARAM_SIZE];
    int paramSize = 0;
    int loop = 0;
    GETPARAMVALUES *paramValue;

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    /* Copy the input arguments to the local variables */
    strcpy(paramName,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n Input parameter is %s",paramName);

    int returnVal=0;

    DEBUG_PRINT(DEBUG_TRACE,"Initiate to register with Component register\n");

    returnVal=ssp_register(1);
    if(returnVal == 0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"CCSPMBUS stub registered with CR\n");
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Failed to register with CR\n");
        return;
    }

    /* Retrieve the specified parameter value */
    paramValue = ssp_getParameterValue(&paramName[0],&paramSize);
    if(paramValue == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the value of parameter name";
    }
    else
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the value of parameter name";

        for(loop = 0; loop < paramSize; loop++)
        {
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Id is %d\n",loop);
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Name is %s\n",paramValue[loop].pParamNames);
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Value is %s",paramValue[loop].pParamValues);
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Type is %d\n",paramValue[loop].pParamType);
        }

        /* Free the memory */
        free_Memory_val(paramSize,paramValue);
    }

    DEBUG_PRINT(DEBUG_TRACE,"Initiate to unregistered from Component register\n");

    returnVal=ssp_terminate();
    if(returnVal == 0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"CCSPMBUS stub unregistered from CR \n");
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Failed to unregistered from CR\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetParamValues --->Exit\n");

	return;
}


/*******************************************************************************************
 *
 * Function Name        : CCSPMBUS_SetParamValues
 * Description          : This function will set the specified value to the parameter name
 *
 * @param [in] req      : paramName - parameter name for which the value to be set
 *                        paramValue - value to be set for the parameter name
 *                        paramType - type of the parameter value
 *
 * @param [out] response - SUCCESS - Value for the parameter name is set
 *                         FAILURE - Failed to set the value to the parameter name
 ********************************************************************************************/
void CCSPMBUS::CCSPMBUS_SetParamValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_SetParamValues --->Entry\n");

    int returnValue = 0;
    char paramName[MAX_PARAM_SIZE];
    char paramValue[MAX_PARAM_SIZE];
    char paramType[MAX_PARAM_SIZE];
    int paramSize = 0;
    int commit = 0;
    GETPARAMVALUES *getParamValue;
    int returnVal=0;

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["paramValue"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["paramType"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    if(&req["commit"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
	return;
    }

    /* Copy the input arguments to the local variables */
    strcpy(paramName,req["paramName"].asCString());
    strcpy(paramValue,req["paramValue"].asCString());
    strcpy(paramType,req["paramType"].asCString());
    commit = req["commit"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\nCCSPMBUS_SetParamValues:: ParamName input is %s",paramName);
    DEBUG_PRINT(DEBUG_TRACE,"\nCCSPMBUS_SetParamValues:: ParamValue input is %s",paramValue);
    DEBUG_PRINT(DEBUG_TRACE,"\nCCSPMBUS_SetParamValues:: ParamType input is %s",paramType);
    DEBUG_PRINT(DEBUG_TRACE,"\nCCSPMBUS_SetParamValues:: Commit input is %d",commit);

    DEBUG_PRINT(DEBUG_TRACE,"Initiate to register with Component register\n");

    returnVal=ssp_register(1);
    if(returnVal == 0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"CCSPMBUS stub registered with CR\n");
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Failed to register with CR\n");
        return;
    }

    /* Set the value for the specified parameter name */
    returnValue = ssp_setParameterValue(&paramName[0],&paramValue[0],&paramType[0],commit);
    if(0 == returnValue)
    {
        /* Retrieve the specified parameter value */
        getParamValue = ssp_getParameterValue(&paramName[0],&paramSize);
        if(getParamValue == NULL)
        {
            response["result"]="FAILURE";
            response["details"]="Failed to retrieve the value of parameter name";
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Name is %s\n",paramName);
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Value is %s",getParamValue[0].pParamValues);
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Type is %d\n",getParamValue[0].pParamType);

            /* Check whether set and get values are same */
            if(strcmp(&paramValue[0],&getParamValue[0].pParamValues[0])==0)
            {
                /* Free the memory */
                free_Memory_val(paramSize,getParamValue);

                /* Set the result details */
                response["result"]="SUCCESS";
                response["details"]="Successfully set the value for the specified parameter";
            }
            else
            {
                /* Free the memory */
                free_Memory_val(paramSize,getParamValue);

                /* Set the result details */
                response["result"]="FAILURE";
                response["details"]="Validation Failed - Set and Get values are not matching";
            }
        }
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set the value for the specified parameter";
    }


    returnVal=ssp_terminate();
    if(returnVal == 0)
    {
        DEBUG_PRINT(DEBUG_TRACE,"CCSPMBUS stub unregistered from CR \n");
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"Failed to unregistered from CR\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetParamValues --->Exit\n");

    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_SetParamValues --->Exit\n");
	return;
}



/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_Init
 * Description		: This function will invoke Message bus init that will init dbus
 * 	        		  functions and interface calls
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_init
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_Init(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_Init --->Entry \n");

    int returnValue = 0;
    char configFile[MAX_PARAM_SIZE];

    strcpy(configFile,req["cfgfileName"].asCString());

    printf("\n CCSPMBUS_Init :: Input msg config file is %s",configFile);

    returnValue = ssp_mbus_init(configFile);

    printf("\n CCSPMBUS_Init :: Status of Bus Init %s",returnValue);

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_Init :: Message Bus Initialization Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_Init :: Message Bus Initialization Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdk_mbus_init Error --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_Init --->Exit\n");
	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_Exit
 * Description		: This function is called through TM RPC which will invoke Message bus
 *                    Exit function
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_exit
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_Exit(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_Exit --->Entry\n");

    int returnValue = SSP_MBUS_FAILURE;


    returnValue = ssp_mbus_exit();

    if( SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_Exit :: MBUS DE-INITIALIZTION SUCCESS";
    }
    else
    {
        response["result"]="FAILURE";

        if( returnValue == SSP_MBUS_EXEC_ERROR )
        {
            response["details"]="CCSPMBUS_Exit :: Message Bus EXIT INVOKE ERROR / Is INIT CALLED?";
        }
        else
        {
            response["details"]="CCSPMBUS_Exit :: MBUS DE-INITIALIZTION FAILURE";
        }

        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_Exit --->Error in  execution \n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_Exit --->Exit\n");
	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_RegisterEvent
 * Description		: This function is called through TM RPC which will invoke Message bus
 *                    Exit function
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_exit
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_RegisterEvent(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_RegisterEvent --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;
    char eventName[MAX_PARAM_SIZE];

    strcpy(eventName,req["eventName"].asCString());

    returnValue = ssp_mbus_register_event(eventName);

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_RegisterEvent :: MBUS Register Event Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_RegisterEvent :: MBUS Register Event Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n ssp_mbus_register_event Error --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_RegisterEvent --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_UnRegisterEvent
 * Description		: This function is called through TM RPC which will invoke Message bus
 *                    Exit function
 * @param [in] req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_exit
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_UnRegisterEvent(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_UnRegisterEvent --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;
    char eventName[MAX_PARAM_SIZE];

    strcpy(eventName,req["eventName"].asCString());

    returnValue = ssp_mbus_unregister_event(eventName);

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_UnRegisterEvent :: MBUS UnRegister Event Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_UnRegisterEvent :: MBUS UnRegister Event Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdk_mbus_unregister_event Error --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_UnRegisterEvent --->Exit\n");

	return;
}


/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_LoadCfg
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific config file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_loadcfg
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_LoadCfg(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_LoadCfg --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;
    char configFile[MAX_PARAM_SIZE] = {0};

    /* Retrieve the current TDK path */
    string cfgFilePath = getenv("TDK_PATH");

    string cfgfileName = req["cmpCfgFile"].asString();

    /* concatenate the path and file name of the cfg */
    cfgFilePath = cfgFilePath + cfgfileName;

    strcpy(configFile,cfgFilePath.c_str());

    printf("Cfg file to be loaded:%s\n",configFile);

    returnValue = ssp_mbus_loadcfg(configFile);

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_LoadCfg :: Component Config file loading SUCCESS";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_LoadCfg :: Component Config file loading FAILURE";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdk_mbus_loadcfg Error --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_LoadCfg --->Exit \n");
    return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_LoadDmXml
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_LoadDmXml(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_LoadDmXml --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;
    char dmlXmlFile[MAX_PARAM_SIZE] = {0};

    /* Retrieve the current TDK path */
    string xmlFilePath = getenv("TDK_PATH");

    string xmlfileName = req["xmlfileName"].asString();

    /* string concatenate the path and file name */
    xmlFilePath = xmlFilePath + xmlfileName;

    strcpy(dmlXmlFile,xmlFilePath.c_str());

    printf("DataModel XML file to be loaded:%s\n",dmlXmlFile);

    returnValue = ssp_mbus_load_dmlxml(dmlXmlFile);
    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_LoadDmXml :: Component data model xml file loading SUCCESS";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_LoadDmXml :: Component data model xml file loading FAILURE";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdk_mbus_load_dmlxml Error --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_LoadDmXml --->Exit \n");
	return;
}


/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_RegisterPath
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_register_path
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_RegisterPath(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_RegisterPath --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_register_path();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_RegisterPath :: MBUS Register Path Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_RegisterPath :: MBUS Register Path Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdk_mbus_register_path Error --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_RegisterPath --->Exit\n");

	return;
}


/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_QueryStatus
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_QueryStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_QueryStatus --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_mbus_query_status();

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_QueryStatus :: MBUS Query Status Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_QueryStatus :: MBUS Query Status Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdk_mbus_query_status Error --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_QueryStatus --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_GetAllocMemory
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_GetAllocMemory(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetAllocMemory --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_get_allocmemory();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Mbus_GetAllocMemory:: CCSPMBUS Get allocated Memory Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Mbus_GetAllocMemory:: CCSPMBUS Get Allocated Memory Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n tdk_mbus_get_alloc_memory--->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetAllocMemory--->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_GetMaxMemory
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_GetMaxMemory(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetMaxMemory --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_get_maxmemory();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_GetMaxMemory:: Mbus Get Max Memory Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_GetMaxMemory:: Mbus Get Max Memory Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetMaxMemory --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetMaxMemory --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_RegisterCapabilities
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_RegisterCapabilities(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_RegisterCapabilities --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_register_capabilities();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_RegisterCapabilities :: Mbus Register Capabilities Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_RegisterCapabilities ::Mbus Register Capabilities Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_RegisterCapabilities --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_RegisterCapabilities --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_UnRegisterNamespace
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_UnRegisterNamespace(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_UnRegisterNamespace --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_unregister_namespace();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_UnRegisterNamespace :: UnRegister Namespace Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_UnRegisterNamespace :: UnRegister Namespace Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_UnRegisterNamespace --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_UnRegisterNamespace -->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_UnRegisterComponent
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_UnRegisterComponent(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_UnRegisterComponent --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_unregistercomponent();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_UnRegisterComponent :: UnRegister Component Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_UnRegisterComponent :: MBUS UnRegister Component Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_UnRegisterComponent ERROR --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_UnRegisterComponent --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_DiskNamespaceSupportedByComponent
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_DiskNamespaceSupportedByComponent(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_DiskNamespaceSupportedByComponent --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_namespace_supportedby_component();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_DiskNamespaceSupportedByComponent :: DiskNamespace Supported By Component Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_DiskNamespaceSupportedByComponent :: DiskNamespace Supported By Component Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_DiskNamespaceSupportedByComponent Error --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_DiskNamespaceSupportedByComponent --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_DiskComponentSupportingDynamicTbl
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_DiskComponentSupportingDynamicTbl(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_DiskComponentSupportingDynamicTbl --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_component_supporting_dynamictbl();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_DiskComponentSupportingDynamicTbl :: Disk Component Supporting Dynamic Tbl Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_DiskComponentSupportingDynamicTbl :: Disk Component Supporting Dynamic Tbl Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_DiskComponentSupportingDynamicTbl --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_DiskComponentSupportingDynamicTbl --->Exit\n");

    return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_GetRegisteredComponents
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_GetRegisteredComponents(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetRegisteredComponents --->Entry \n");

    int returnValue = 0;

    returnValue = ssp_mbus_get_registered_components();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_GetRegisteredComponents :: Get Registered Components Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_GetRegisteredComponents :: Get Registered Components Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetRegisteredComponents Error --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetRegisteredComponents --->Exit\n");

	return;
}


/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_GetHealth
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_GetHealth(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetHealth --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;
    char cmpId[MAX_PARAM_SIZE];
    char cmpPath[MAX_PARAM_SIZE];

    strcpy(cmpId,req["cmpId"].asCString());
    strcpy(cmpPath,req["cmpPath"].asCString());

    returnValue = ssp_mbus_getHealth(cmpId,cmpPath);

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_GetHealth :: Retrieved the component health";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_GetHealth :: Failed to retrievd the component health";
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_GetHealth --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_DumpComponentRegistry
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_DumpComponentRegistry(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_DumpComponentRegistry --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_dump_component_registry();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_DumpComponentRegistry :: Dump Component Registry Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_DumpComponentRegistry :: Dump Component Registry Failure";
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n tdk_mbus_DumpComponentRegistry --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_IsSystemReady
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_IsSystemReady(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_IsSystemReady --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_issystem_ready();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_IsSystemReady :: IsSystem Ready Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_IsSystemReady :: IsSystem Ready Failure";
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_IsSystemReady --->Exit\n");

	return;
}


/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_SendSignal
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_SendSignal(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_SendSignal --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_SendsystemReadySignal();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_SendSignal :: Successfully send the event signal";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_SendSignal :: Failed to send the event signal";
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_SendSignal --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name	: CCSPMBUS_RegisterBase
 * Description		: This function will invoke ssp function that inturn will
 * 	        		  call ccsp base functions to load component specific data model
 *                    xml file
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 * 			               ssp_mbus_load_dmlxml
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_RegisterBase(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_RegisterBase--->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_register_base();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_RegisterBase :: Register Base Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_RegisterBase :: Register Base Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_RegisterBase Error --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_RegisterBase --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name        : CCSPMBUS_ReqSessionId
 * Description          : This function will invoke ssp function that inturn will
 *                                call ccsp base functions to request session ID from CR
 *
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                                     ssp_mbus_req_sessionid
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_ReqSessionId(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_ReqSessionId --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_req_sessionid();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_ReqSessionId :: MBUS ReqSession Id Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_ReqSessionId :: MBUS ReqSession Id Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_ReqSessionId  Error --->Exit\n");
	return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_ReqSessionId --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name        : CCSPMBUS_InformEndSession
 * Description          : This function will invoke ssp function that inturn will
 *                                call ccsp base functions to close/inform end of session to the CR
 *
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                                     ssp_mbus_inform_end_session
 ********************************************************************************************/
void CCSPMBUS::CCSPMBUS_InformEndSession(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_InformEndSession --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_inform_end_session();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_InformEndOfSession :: MBus Inform End Of Session Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_InformEndOfSession :: MBus Inform End Of Session Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_InformEndSession Error --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_InformEndSession --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name        : CCSPMBUS_BusCheck
 * Description          : This function will invoke ssp function that inturn will
 *                                call ccsp base functions to check the bus status of a component
 *                    from CR
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                                     ssp_mbus_bus_check
 ********************************************************************************************/
void CCSPMBUS::CCSPMBUS_BusCheck(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_BusCheck --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;


    returnValue = ssp_mbus_bus_check();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_BusCheck :: MBus BusCheck Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_BusCheck :: MBus BusCheck Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_BusCheck --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_BusCheck --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name        : CCSPMBUS_CheckNamespaceDataType
 * Description          : This function will invoke ssp function that inturn will
 *                                call ccsp base functions to get/check datatype of a given
 *                    namespace
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                                     ssp_mbus_check_namespace_datatype
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_CheckNamespaceDataType(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n  CCSPMBUS_CheckNamespaceDataType --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;


    returnValue = ssp_mbus_check_namespace_datatype();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_CheckNamespaceDataType :: MBus Check Namespace DataType Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_CheckNamespaceDataType :: MBus Check Namespace DataType Failure";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_CheckNamespaceDataType Error --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_CheckNamespaceDataType --->Exit\n");

	return;
}

/*******************************************************************************************
 *
 * Function Name        : CCSPMBUS_UnloadCfg
 * Description          : This function will free the memory of global pointer
 *
 * @param [in]  req-
 * @param [out] response - filled with SUCCESS or FAILURE based on the return value of
 *                         ssp_mbus_unloadcfg
 ********************************************************************************************/

void CCSPMBUS::CCSPMBUS_UnloadCfg(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n  CCSPMBUS_UnloadCfg --->Entry \n");

    int returnValue = SSP_MBUS_FAILURE;

    returnValue = ssp_mbus_unloadcfg();

    if(SSP_MBUS_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="CCSPMBUS_UnloadCfg :: Unloading cfg file Success";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="CCSPMBUS_UnloadCfg :: Unloading cfg file failed";
        DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_UnloadCfg Error --->Exit\n");
	return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n CCSPMBUS_UnloadCfg --->Exit\n");

	return;
}

/**************************************************************************
 * Function Name	: CreateObject
 * Description	    : This function will be used to create a new object for the
 *		              class "CCSPMBUS".
 *
 **************************************************************************/
extern "C" CCSPMBUS* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new CCSPMBUS(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/
bool CCSPMBUS::cleanup(IN const char* szVersion)
{

    DEBUG_PRINT(DEBUG_LOG,"CCSPMBUS cleanup --> Entry \n");
    return TEST_SUCCESS;
}

/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(CCSPMBUS *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying CCSPMBUS object\n");
    delete stubobj;
}

