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

#include "wecb.h"
#include "ssp_tdk_wrp.h"

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
};

/***************************************************************************
 *Function name	: initialize
 *Description	: Initialize Function will be used for registering the wrapper method
 *  	  	  with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/

bool WECB::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE,"WECB Initialize\n");
    return TEST_SUCCESS;
}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string WECB::testmodulepre_requisites()
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
 *Description    : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/
bool WECB::testmodulepost_requisites()
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

/*******************************************************************************************
 *
 * Function Name	: WECB_GetParamNames
 * Description		: This function will retrieve the list of parameters associated with
 * 			          the specified namespace
 *
 * @param [in] req 	: paramName - Specific parameter name to be retrieved
 *                    paramList - List associated with the namespace
 *                    recursive - 0 for single parameter and 1 for entire list
 *
 * @param [out] response - SUCCESS - All parameter names are retrieved
 *			   FAILURE - Failed to retrieve the parameter names
 ********************************************************************************************/
void WECB::WECB_GetParamNames(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_GetParamNames --->Entry\n");

    char paramName[MAX_PARAM_SIZE];
    char paramList[MAX_PARAM_SIZE];
    int recursive = 0;
    int paramSize = 0;
    int paramListSize = 0;
    int loop = 0;
    int flag = 0;
    GETPARAMNAMES *paramValue;
    GETPARAMNAMES *paramListValue;

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["paramList"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["recursive"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    /* Copy the input arguments to the local variables */
    strcpy(paramName,req["paramName"].asCString());
    strcpy(paramList,req["paramList"].asCString());
    recursive = req["recursive"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\n Input parameter name is %s \n",paramName);
    DEBUG_PRINT(DEBUG_TRACE,"\n Input parameter List is %s \n",paramList);
    DEBUG_PRINT(DEBUG_TRACE,"\n Input recursive value is %d\n",recursive);

    /* Retrieve the specified parameter name */
    paramValue = ssp_getParameterNames(&paramName[0],recursive, &paramSize);
    if(paramValue != NULL)
    {
        /* Retrieve the list of parameter names */
        paramListValue = ssp_getParameterNames(&paramList[0],recursive, &paramListSize);
        if(paramListValue != NULL)
        {
            for(loop=0;loop < paramListSize;loop++)
            {
                if(strcmp(paramListValue[loop].pParamNames,paramValue[0].pParamNames)==0)
                {
                    flag = 1;
                    if(paramListValue[loop].writable == paramValue[0].writable)
                    {
                        free_Memory_Names(paramListSize,paramListValue);
                        printf("Parameter Name has been fetched successfully and it matched with parameter List\n");
                        response["result"] = "SUCCESS";
                        response["details"] = "Parameter Name has been fetched successfully";
                        return;
                    }
                    else
                    {
                        printf("Writeable parameter of the parameter name not matching with the parameter list\n");
                        response["result"] = "FAILURE";
                        response["details"] = "Writeable parameter of the parameter name not matching with the parameter list";
                        return;
                    }
                }
            }
            if(flag ==0)
            {
                free_Memory_Names(paramListSize,paramListValue);
                printf("Parameter name not matching with the parameter list\n");
                response["result"] = "FAILURE";
                response["details"] = "Parameter name not matching with the parameter list";
                return;
            }
        }
        else
        {
            free_Memory_Names(paramSize,paramValue);
            response["result"]="FAILURE";
            response["details"]="Failed to get the list of parameter name details";
        }
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the parameter name details";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_GetParamNames --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WECB_GetParamValues
 * Description          : This function will retrieve the list of parameter values
 *                        associated with the specified namespace
 *
 * @param [in] req      : paramName - Specific parameter name for which value to be retrieved
 *
 * @param [out] response - SUCCESS - All parameter values are retrieved
 *                         FAILURE - Failed to retrieve the parameter values
 ********************************************************************************************/
void WECB::WECB_GetParamValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_GetParamValues --->Entry\n");

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

    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_GetParamValues --->Exit\n");

    return;
}

/*******************************************************************************************
 *
 * Function Name        : WECB_GetParamAttributes
 * Description          : This function will retrieve the list of parameters attributes
 *                       associated with the specified namespace
 *
 * @param [in] req      : paramName - List associated with the namespace
 *
 * @param [out] response - SUCCESS - All attributes associated with the param name are retrieved
 *                         FAILURE - Failed to retrieve the parameter attributes
 ********************************************************************************************/
void WECB::WECB_GetParamAttributes(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_GetParamAttributes --->Entry\n");

    int paramAttrSize = 0;
    char paramName[MAX_PARAM_SIZE];
    GETPARAMATTR *paramAttr;
    int loop = 0;

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

    /* Retrieve the attributes of specified parameter name */
    paramAttr = ssp_getParameterAttr(&paramName[0],&paramAttrSize);
    if(paramAttr == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the attributes of the parameter name";
    }
    else
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully retrieved the attributes of parameter name";

        for (loop = 0;loop < paramAttrSize;loop ++)
        {
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Id is %d\n",loop);
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Name is %s\n",paramAttr[loop].pParamNames);
            DEBUG_PRINT(DEBUG_TRACE,"Access Control is %s",paramAttr[loop].pParamAccess);
            DEBUG_PRINT(DEBUG_TRACE," Notification is %s\n",paramAttr[loop].pParamNotify);
        }

        /* Free the memory */
        free_Memory_Attr(paramAttrSize,paramAttr);
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_GetParamAttributes --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WECB_SetParamValues
 * Description          : This function will set the specified value to the parameter name
 *
 * @param [in] req      : paramName - parameter name for which the value to be set
 *                        paramValue - value to be set for the parameter name
 *                        paramType - type of the parameter value
 *
 * @param [out] response - SUCCESS - Value for the parameter name is set
 *                         FAILURE - Failed to set the value to the parameter name
 ********************************************************************************************/
void WECB::WECB_SetParamValues(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_SetParamValues --->Entry\n");

    int returnValue = 0;
    char paramName[MAX_PARAM_SIZE];
    char paramValue[MAX_PARAM_SIZE];
    char paramType[MAX_PARAM_SIZE];
    int paramSize = 0;
    int commit = 0;
    GETPARAMVALUES *getParamValue;

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

    DEBUG_PRINT(DEBUG_TRACE,"\nWECB_SetParamValues:: ParamName input is %s",paramName);
    DEBUG_PRINT(DEBUG_TRACE,"\nWECB_SetParamValues:: ParamValue input is %s",paramValue);
    DEBUG_PRINT(DEBUG_TRACE,"\nWECB_SetParamValues:: ParamType input is %s",paramType);
    DEBUG_PRINT(DEBUG_TRACE,"\nWECB_SetParamValues:: Commit input is %d",commit);

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

    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_SetParamValues --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WECB_SetParamAttribute
 * Description          : This function will set the values for the attributes of the
 *                        parameter
 *
 * @param [in] req      : paramName - parameter name for which the value to be set
 *                        notify - Attribute value to be set (On/Off/active/passive)
 *                        accessControl - Attribute value to be set (webui/anybody)
 *
 * @param [out] response - SUCCESS - Parameter attributes are set
 *                         FAILURE - Failed to set the Parameter attributes
 ********************************************************************************************/
void WECB::WECB_SetParamAttribute(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_SetParamAttribute --->Entry\n");

    int returnValue = 0;
    char attrNotify[MAX_PARAM_SIZE];
    char attrAccess[MAX_PARAM_SIZE];
    char paramName[MAX_PARAM_SIZE];
    GETPARAMATTR *paramAttr;
    GETPARAMATTR *oldParamAttr;
    int paramAttrSize = 0;
    int oldParamAttrSize = 0;

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["notify"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["accessControl"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    /* Copy the input arguments to the local variables */
    strcpy(paramName,req["paramName"].asCString());
    strcpy(attrNotify,req["notify"].asCString());
    strcpy(attrAccess,req["accessControl"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n Input path name is %s\n",paramName);
    DEBUG_PRINT(DEBUG_TRACE,"\n Input notification is %s\n",attrNotify);
    DEBUG_PRINT(DEBUG_TRACE,"\n Input access control is %s\n",attrAccess);

    /* Get the current attributes of the parameter */
    oldParamAttr = ssp_getParameterAttr(&paramName[0],&oldParamAttrSize);
    if(oldParamAttr == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="Failed to retrieve the attributes of the parameter name";
        return;
    }

    /* Set attributes for the specified parameter */
    returnValue = ssp_setParameterAttr(&paramName[0],&attrNotify[0],&attrAccess[0]);
    if(returnValue!=0)
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set the attributes for the parameter";
    }
    else
    {
        sleep(10);
        /* Retrieve the attributes of specified parameter name */
        paramAttr = ssp_getParameterAttr(&paramName[0],&paramAttrSize);
        if(paramAttr == NULL)
        {
            response["result"]="FAILURE";
            response["details"]="Failed to retrieve the attributes of the parameter name";
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"Parameter Name is %s\n",paramName);
            DEBUG_PRINT(DEBUG_TRACE,"Access Control is %s",paramAttr[0].pParamAccess);
            DEBUG_PRINT(DEBUG_TRACE," Notification is %s\n",paramAttr[0].pParamNotify);

            /* Notify will be set only as "on" if value is passed as active/passive */
            if((strcmp(attrNotify,"off")!= 0)&&(strcmp(attrNotify,"unchange")!= 0))
            {
                DEBUG_PRINT(DEBUG_TRACE,"Entering into active/passive condition");
                strcpy(attrNotify,"on");
            }

            /* No change in notify if value is passed as unchange */
            if(strcmp(attrNotify,"unchange")== 0)
            {
                DEBUG_PRINT(DEBUG_TRACE,"Entering unchange condition of Notify");
                strcpy(attrNotify,oldParamAttr[0].pParamNotify);
            }

            /* No change in accessControl if value is passed as unchange */
            if(strcmp(attrAccess,"unchange")== 0)
            {
                DEBUG_PRINT(DEBUG_TRACE,"Entering unchange condition of Access Control");
                strcpy(attrAccess,oldParamAttr[0].pParamAccess);
            }

            if((strcmp(&attrNotify[0],&paramAttr[0].pParamNotify[0])==0) &&
                    (strcmp(&attrAccess[0],&paramAttr[0].pParamAccess[0])==0))
            {
                /* Free the memory */
                free_Memory_Attr(paramAttrSize,paramAttr);

                response["result"]="SUCCESS";
                response["details"]="Successfully set the attributes for the parameter";
            }
            else
            {
                /* Free the memory */
                free_Memory_Attr(paramAttrSize,paramAttr);

                response["result"]="FAILURE";
                response["details"]="Validation failure - Set and get attributes value not matching";
            }
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_SetParamAttribute --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WECB_SetSessionId
 * Description          : This function will set the session Id of the component
 *
 * @param [in] req      : priority - 0 to run and 1 to terminate the component
 *
 * @param [out] response - SUCCESS - Session Id is set
 *                         FAILURE - Failed to set the session Id
 ********************************************************************************************/
void WECB::WECB_SetSessionId(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_SetSessionId --->Entry\n");

    int returnValue = 0;
    int priority = 0;
    int sessionId = 0;

    /* Validate the input arguments */
    if(&req["sessionId"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    /* Copy the input arguments to the local variables */
    sessionId = req["sessionId"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\n sessionId is %d",sessionId);

    /* Set session Id for the running component */
    returnValue = ssp_setSessionId(priority,sessionId);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully set the session Id";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set the session Id";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_SetSessionId --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WECB_AddObject
 * Description          : This function will add an entry to the table object
 *
 * @param [in] req      : paramName - List associated with the namespace
 *
 * @param [out] response - SUCCESS - Added entry to the table object
 *                         FAILURE - Failed to add entry to the table object
 ********************************************************************************************/
void WECB::WECB_AddObject(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_AddObject --->Entry\n");

    int returnValue = 0;
    char paramName[MAX_PARAM_SIZE];
    int instanceNumber = 0;

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    /* Copy the input arguments to the local variables */
    strcpy(paramName,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n ParamName input is %s",paramName);

    /* Add row to the table object */
    returnValue = ssp_addTableRow(&paramName[0],&instanceNumber);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully added entry to the table object ";
        DEBUG_PRINT(DEBUG_TRACE,"\n Added Instance number is %d",instanceNumber);
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to add entry to the table object";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_AddObject --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WECB_DelObject
 * Description          : This function will delete entry from the table object
 *
 * @param [in] req      : paramName - Table name from which entry to be deleted
 *
 * @param [out] response - SUCCESS - Deleted entry from the table object
 *                         FAILURE - Failed to delete entry from the table object
 ********************************************************************************************/
void WECB::WECB_DelObject(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_DelObject --->Entry\n");

    int returnValue = 0;
    char paramName[MAX_PARAM_SIZE];

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
        return;
    }

    /* Copy the input arguments to the local variables */
    strcpy(paramName,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n ParamName input is %s",paramName);

    /* Delete row from the table object */
    returnValue = ssp_deleteTableRow(&paramName[0]);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully deleted the row from the table object";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to delete the row from the table object";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_DelObject --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WECB_SetCommit
 * Description          : This function will commit the changes done in the table.
 *
 * @param [in] req      : paramName - parameter to be committed
 *
 * @param [out] response - SUCCESS - Changes to the component committed
 *                         FAILURE - Failed to commit the changes
 ********************************************************************************************/
void WECB::WECB_SetCommit(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_SetCommit --->Entry\n");

    int returnValue = 0;
    char paramName[MAX_PARAM_SIZE];

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL";
        return;
    }

    /* Copy the input arguments to the local variables */
    strcpy(paramName,req["paramName"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\nParamName input is %s",paramName);

    /* Set the changes done in the component */
    returnValue = ssp_setCommit(&paramName[0]);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully committed the changes in the component";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to commit the changes in the component";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WECB_SetCommit --->Exit\n");
    return;
}

/**************************************************************************
 * Function Name	: CreateObject
 * Description	    : This function will be used to create a new object for the
 *		              class "WECB".
 *
 **************************************************************************/
extern "C" WECB* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new WECB(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/
bool WECB::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"WECB cleanup --> Entry \n");
    return TEST_SUCCESS;
}

/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(WECB *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying WECB object\n");
    delete stubobj;
}

