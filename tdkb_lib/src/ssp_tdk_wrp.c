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

#ifdef __GNUC__
#if (!defined _BUILD_ANDROID) && (!defined _NO_EXECINFO_H_)
#include <execinfo.h>
#endif
#endif
#include "ssp_global.h"
#include "stdlib.h"
#include "ccsp_dm_api.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include "pthread.h"
#include "ssp_tdk_wrp.h"
#include "cosa_apis.h"
#include "plugin_main_apis.h"
#include "diag_inter.h"
#include "diag.h"

char subsystem_prefix[32]={0};
extern  PDSLH_CPE_CONTROLLER_OBJECT     pDslhCpeController;
GETPARAMNAMES *GetNames;
GETPARAMVALUES *GetValues;
GETPARAMATTR *GetAttr;
/*******************************************************************************************
 *
 * Function Name        : ssp_getParameterValue
 * Description          : This function will call base interface funtion which is defined
 *            		  on top of dbus calls to get Parameter value from ccsp
 *			  Component
 * @param [in]  pParamName - Pointer to Parameter Name
 * @param [out] pParamsize - To hold the size of number of parameters fetched from component
 ********************************************************************************************/
GETPARAMVALUES* ssp_getParameterValue(char *pParamName,int *pParamsize)
{
    char dst_pathname_cr[64] = {0};
    componentStruct_t **ppComponents = NULL;
    int size2 = 0;
    int ret ;
    char *dst_componentid = NULL;
    char *dst_pathname = NULL;
    parameterValStruct_t **parameterVal = NULL;
    int size = 0;
    int i;
    int cmpt;
    char *pCompArr_ParamName[MAX_PARAM_SIZE];
    char *pParamValue[MAX_PARAM_NAMES_ARRAY];

    printf("\nssp_getParameterValue::Entering ssp_getParameterValue Function in Component Stub ...\n");

    pCompArr_ParamName[0] = pParamName;

    strcat(dst_pathname_cr,subsystem_prefix);
    strcat(dst_pathname_cr, CCSP_DBUS_INTERFACE_CR);

    printf("dst_pathname_cr:%s\n",dst_pathname_cr);

    /* This function will identify Component path through Component Registrar (CR)
       pParam Name is used to as input and CR will return back the respective component
       dbus path
     */
    ret = CcspBaseIf_discComponentSupportingNamespace
        (
         bus_handle_client,
         dst_pathname_cr,
         pParamName,
         subsystem_prefix,
         &ppComponents,
         &size2
        );


    if ( ret == CCSP_SUCCESS )
    {
        if ( size2 == 0 )
        {
            printf("ssp_getParameterValue::Can't find destination component.\n");
            return NULL;
        }
    }
    else
    {
        printf("ssp_getParameterValue::Can't find destination component.\n");
        return NULL;
    }


    for(cmpt=0; cmpt < size2 ; cmpt++)
    {
        dst_componentid = ppComponents[cmpt]->componentName;
        printf("\nssp_getParameterValue::Destination Component ID is %s\n",dst_componentid);
        dst_pathname    = ppComponents[cmpt]->dbusPath;
        printf("\nssp_getParameterValue::Destination Component Name is %s\n",dst_pathname);

        ret = CcspBaseIf_getParameterValues(
                bus_handle_client,
                dst_componentid,
                dst_pathname,
                pCompArr_ParamName,
                1,
                &size ,
                &parameterVal
                );
        GetValues=(GETPARAMVALUES *)malloc(size*sizeof(GETPARAMVALUES));
        if(NULL==GetValues)
        {
            printf("Malloc failed for the struct in GetParameter Values\n");
            return NULL;
        }
        memset(GetValues,0,size*sizeof(GETPARAMVALUES));

        if(ret == CCSP_SUCCESS  && size >= 1)
        {
            for ( i = 0; i < size; i++ )
            {
                GetValues[i].pParamValues = (char *)malloc(MAX_PARAM_SIZE*sizeof(char*));
                if(NULL==GetValues[i].pParamValues)
                {
                    printf("Malloc failed for the struct in GetParameter Values\n");
                    return NULL;
                }
                GetValues[i].pParamNames = (char *)malloc(MAX_PARAM_SIZE*sizeof(char*));
                if(NULL==GetValues[i].pParamNames)
                {
                    printf("Malloc failed for the struct in GetParameter Values\n");
                    return NULL;
                }
                memset(GetValues[i].pParamValues,0,MAX_PARAM_SIZE*sizeof(char*));
                strcpy(GetValues[i].pParamValues,parameterVal[i]->parameterValue);
                memset(GetValues[i].pParamNames,0,MAX_PARAM_SIZE*sizeof(char*));
                strcpy(GetValues[i].pParamNames,parameterVal[i]->parameterName);
                GetValues[i].pParamType=parameterVal[i]->type;

            }

        }
        else
        {
            printf("CcspBaseIf_getParameterValues function returned 1\n");
            return NULL;
        }

    }//end of cmpt count
    *pParamsize = size;
    free_parameterValStruct_t (bus_handle_client, size, parameterVal);
    parameterVal = NULL;

    free_componentStruct_t(bus_handle_client, size2, ppComponents);

    printf("ssp_getParameterValue::Returning param value to agent stub\n");
    return GetValues;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_setParameterValue
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to get Parameter value from CCSP Component
 * @param [in]  pParamName - Pointer to Parameter Name
 * @param [out] pParamsize - To hold the size of number of parameters fetched from Component
 ********************************************************************************************/


int ssp_setParameterValue(char *pParamName,char *pParamValue,char *pParamType, int commit)
{
    char        dst_pathname_cr[64] =  {0};
    componentStruct_t ** ppComponents = NULL;
    int         size2 = 0;
    int         ret ;
    char *      dst_componentid         =  NULL;
    char *      dst_pathname            =  NULL;
    parameterValStruct_t **parameterVal = NULL;
    int         size = 0;
    int         i;
    unsigned char bTmp = 0;
    char * pFaultParameter = NULL;
    parameterValStruct_t val[MAX_COMP_ARRAY] = {{0}};


    strcat(dst_pathname_cr,subsystem_prefix);
    strcat(dst_pathname_cr, CCSP_DBUS_INTERFACE_CR);

    printf("dst_pathname_cr:%s\n",dst_pathname_cr);
    bTmp = commit;

    /* This function will identify Component path through Component Registrar (CR)
       pParam Name is used to as input and CR will return back the respective component
       dbus path
     */
    ret = CcspBaseIf_discComponentSupportingNamespace
        (
         bus_handle_client,
         dst_pathname_cr,
         pParamName,
         subsystem_prefix,
         &ppComponents,
         &size2
        );

    if ( ret == CCSP_SUCCESS )
    {
        if ( size2 == 0 )
        {
            printf("\nssp_setParameterValue::Can't find destination component.\n");
            return 1;
        }
    }
    else
    {
        printf("\nssp_setParameterValue::Can't find destination component.\n");
        return ret;
    }

    dst_componentid = ppComponents[0]->componentName;
    printf("\nssp_setParameterValue::Destination Component ID is %s\n",dst_componentid);
    dst_pathname    = ppComponents[0]->dbusPath;
    printf("\nssp_setParameterValue::Destination Component Name is %s\n",dst_pathname);

    val[0].parameterName  = AnscCloneString(pParamName);
    val[0].parameterValue = AnscCloneString(pParamValue);

    if(strcmp(pParamType,"string")==0)
    {
        val[0].type = ccsp_string;
    }
    else if (strcmp(pParamType,"int")==0)
    {
        val[0].type = ccsp_int;
    }
    else if (strcmp(pParamType,"unsignedint")==0)
    {
        val[0].type = ccsp_unsignedInt;
    }
    else if (strcmp(pParamType,"unsignedInt")==0)
    {
        val[0].type = ccsp_unsignedInt;
    }
    else if (strcmp(pParamType,"boolean")==0)
    {
        val[0].type = ccsp_boolean;
    }
    else if (strcmp(pParamType,"bool")==0)
    {
        val[0].type = ccsp_boolean;
    }
    else if (strcmp(pParamType,"datetime")==0)
    {
        val[0].type = ccsp_dateTime;
    }
    else if (strcmp(pParamType,"base64")==0)
    {
        val[0].type = ccsp_base64;
    }
    else if (strcmp(pParamType,"long")==0)
    {
        val[0].type = ccsp_long;
    }
    else if (strcmp(pParamType,"unsignedlong")==0)
    {
        val[0].type = ccsp_unsignedLong;
    }
    else if (strcmp(pParamType,"float")==0)
    {
        val[0].type = ccsp_float;
    }
    else if (strcmp(pParamType,"double")==0)
    {
        val[0].type = ccsp_double;
    }
    else if (strcmp(pParamType,"byte")==0)
    {
        val[0].type = ccsp_byte;
    }
    else if (strcmp(pParamType,"none")==0)
    {
        val[0].type = ccsp_none;
    }

    printf("\nssp_setParameterValue:: val param name is %s",val[0].parameterName);
    printf("\nssp_setParameterValue:: val param value is %s",val[0].parameterValue);
    printf("\nssp_setParameterValue:: val param type is %d",val[0].type);

    ret = CcspBaseIf_setParameterValues(
            bus_handle_client,
            dst_componentid,
            dst_pathname,
            0,
            DSLH_MPA_ACCESS_CONTROL_CLIENTTOOL,
            val,
            1,
            bTmp,
            &pFaultParameter
            );

    free_componentStruct_t(bus_handle_client, size2, ppComponents);

    if ( ret == CCSP_SUCCESS )
    {
        printf("\nssp_setParameterValue::Execution succeed.\n");
    }
    else
    {
        printf("\nssp_setParameterValue::Execution fail(error code:(%d)).\n",ret);
        return ret;
    }

    if ( pFaultParameter != NULL )
        AnscFreeMemory(pFaultParameter);

    return 0;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_getParameterNames
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to get Parameter Names from CCSP Component
 * @param [in]  pParamName - Pointer to Path Name that holds Parameters info
 * @param [in]  recursive  - This integer variable used to find next level names from
 *                           given path
 * @param [out] pParamsize - To hold the count for number of parameters fetched from Component
 ********************************************************************************************/

GETPARAMNAMES* ssp_getParameterNames(char *pPathName,int recursive,int *pParamSize)
{
    char dst_pathname_cr[64] = {0};
    componentStruct_t **ppComponents = NULL;
    int size2 = 0;
    int ret ;
    char *dst_componentid = NULL;
    char *dst_pathname = NULL;
    parameterInfoStruct_t **infoStru = NULL;
    int size = 0;
    int i;
    int cmpt;
    strcat(dst_pathname_cr,subsystem_prefix);
    strcat(dst_pathname_cr, CCSP_DBUS_INTERFACE_CR);

    /* This function will identify Component path through Component Registrar (CR)
       pParam Name is used to as input and CR will return back the respective component
       dbus path */

    ret = CcspBaseIf_discComponentSupportingNamespace
        (
         bus_handle_client,
         dst_pathname_cr,
         pPathName,
         subsystem_prefix,
         &ppComponents,
         &size2
        );


    if ( ret == CCSP_SUCCESS )
    {
        if ( size2 == 0 )
        {
            printf("\nssp_getParameterNames::Can't find destination component.\n");
            return NULL;
        }
    }
    else
    {
        printf("\nssp_getParameterNames::Can't find destination component.\n");
        return NULL;
    }

    for(cmpt=0; cmpt < size2 ; cmpt++)
    {
        dst_componentid = ppComponents[cmpt]->componentName;
        printf("\nssp_getParameterNames::Destination Component ID is %s\n",dst_componentid);
        dst_pathname    = ppComponents[cmpt]->dbusPath;
        printf("\nssp_getParameterNames::Destination Component Name is %s\n",dst_pathname);

        ret = CcspBaseIf_getParameterNames(
                bus_handle_client,
                dst_componentid,
                dst_pathname,
                pPathName,
                recursive,
                &size ,
                &infoStru
                );

        GetNames=(GETPARAMNAMES *) malloc(size*sizeof(GETPARAMNAMES));
        if(NULL==GetNames)
        {
            printf("Malloc failed for the struct in GetParameter Names\n");
            return NULL;
        }
        memset(GetNames,0,size*sizeof(GETPARAMNAMES));

        if(ret == CCSP_SUCCESS  && size >= 1)
        {
            for ( i = 0; i < size; i++ )
            {
                printf("ssp_getParameterNames::Parameter name: %s Parameter WRITABLE:%d\n",
                        infoStru[i]->parameterName,infoStru[i]->writable);

                GetNames[i].pParamNames = (char *)malloc(MAX_PARAM_SIZE*sizeof(char));
                if(NULL==GetNames[i].pParamNames)
                {
                    printf("Malloc failed for the struct in GetParameter Names\n");
                    return NULL;
                }
                memset(GetNames[i].pParamNames,0,MAX_PARAM_SIZE*sizeof(char));
                strcpy(GetNames[i].pParamNames,infoStru[i]->parameterName);
                GetNames[i].writable=infoStru[i]->writable;
            }

        }
        else
        {
            printf("CcspBaseIf_getParameterNames function returned 1 as result\n");
            return NULL;
        }

    }//end of cmpt count
    *pParamSize = size;
    free_parameterInfoStruct_t (bus_handle_client,size,infoStru);
    infoStru = NULL;

    free_componentStruct_t(bus_handle_client, size2, ppComponents);
    printf("ssp_getParameterNames::Returning param names(s) to component agent stub\n");
    return GetNames;

}

/*******************************************************************************************
 *
 * Function Name        : ssp_addTableRow
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to add object table to Component
 *                        for the respective parameter
 * @param [in]  pObjTbl - Pointer to Table object name
 * @param [out] N/A
 ********************************************************************************************/

int ssp_addTableRow(char *pObjTbl,int *pInstanceNumber)
{

    char dst_pathname_cr[64] =  {0};
    componentStruct_t ** ppComponents = NULL;
    int size2 = 0;
    int ret = 0;
    char *dst_componentid = NULL;
    char *dst_pathname = NULL;
    int instanceNumber = 0;

    if(pObjTbl == NULL)
    {
        printf("\nssp_addTableRow::Null parameter passed as argument\n");
        return 1;
    }

    strcat(dst_pathname_cr,subsystem_prefix);
    strcat(dst_pathname_cr, CCSP_DBUS_INTERFACE_CR);

    /* This function will identify Component path through Component Registrar (CR)
       pParam Name is used to as input and CR will return back the respective component
       dbus path
     */
    ret = CcspBaseIf_discComponentSupportingNamespace
        (
         bus_handle_client,
         dst_pathname_cr,
         pObjTbl,
         subsystem_prefix,
         &ppComponents,
         &size2
        );

    if ( ret == CCSP_SUCCESS )
    {
        if ( size2 == 0 )
        {
            printf("\nssp_addTableRow::Can't find destination component.\n");
            return 1;
        }
    }
    else
    {
        printf("\nssp_addTableRow::Can't find destination component.\n");
        return 1;
    }

    dst_componentid = ppComponents[0]->componentName;
    printf("\nssp_addTableRow::Destination Component ID is %s\n",dst_componentid);
    dst_pathname = ppComponents[0]->dbusPath;
    printf("\nssp_addTableRow::Destination Component Name is %s\n",dst_pathname);

    ret = CcspBaseIf_AddTblRow(
            bus_handle_client,
            dst_componentid,
            dst_pathname,
            0,
            pObjTbl,
            &instanceNumber
            );

    printf("\nssp_addTableRow::Instance number of Object added:%d\n",instanceNumber);

    *pInstanceNumber = instanceNumber;

    free_componentStruct_t(bus_handle_client, size2, ppComponents);

    if ( ret == CCSP_SUCCESS )
    {
        printf("\nssp_addTableRow::Added a row to the table object\n");
    }
    else
    {
        printf("\nssp_addTableRow::Failed to add a row to the table object(error code:(%d)).\n",ret);
        return 1;
    }

    return 0;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_deleteTableRow
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to delete the user defined table inside
 *			  ccsp Component
 * @param [in]  pObjTbl - Pointer to Table object name
 * @param [out] N/A
 ********************************************************************************************/

int ssp_deleteTableRow(char *pObjTbl)
{

    char        dst_pathname_cr[64] =  {0};
    componentStruct_t ** ppComponents = NULL;
    int         size2 = 0;
    int         ret ;
    char *      dst_componentid         =  NULL;
    char *      dst_pathname            =  NULL;


    if(pObjTbl == NULL)
    {
        printf("\nssp_deleteTableRow::Null parameter passed as argument\n");
        return 1;
    }

    strcat(dst_pathname_cr,subsystem_prefix);
    strcat(dst_pathname_cr, CCSP_DBUS_INTERFACE_CR);

    /* This function will identify Component path through Component Registrar (CR)
       pParam Name is used to as input and CR will return back the respective component
       dbus path
     */
    ret = CcspBaseIf_discComponentSupportingNamespace
        (
         bus_handle_client,
         dst_pathname_cr,
         pObjTbl,
         subsystem_prefix,
         &ppComponents,
         &size2
        );

    if ( ret == CCSP_SUCCESS )
    {
        if ( size2 == 0 )
        {
            printf("\nssp_deleteTableRow::Can't find destination component.\n");
            return 1;
        }
    }
    else
    {
        printf("\nssp_deleteTableRow::Can't find destination component.\n");
        return 1;
    }

    dst_componentid = ppComponents[0]->componentName;
    printf("\nssp_deleteTableRow::Destination Component ID is %s\n",dst_componentid);
    dst_pathname    = ppComponents[0]->dbusPath;
    printf("\nssp_deleteTableRow::Destination Component Name is %s\n",dst_pathname);

    ret = CcspBaseIf_DeleteTblRow(
            bus_handle_client,
            dst_componentid,
            dst_pathname,
            0,
            pObjTbl
            );

    free_componentStruct_t(bus_handle_client, size2, ppComponents);

    if ( ret == CCSP_SUCCESS )
    {
        printf("\nssp_deleteTableRow::Deleted a row from the table object\n");
    }
    else
    {
        printf("\nssp_deleteTableRow::Failed to delete a row from the table object(error code:(%d)).\n",ret);
        return 1;
    }
    return 0;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_setCommit
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to commit Values to Non-Vol of ccsp
 *			  Component
 * @param [in]  pObjTbl - Pointer to Table object name
 * @param [out] N/A
 ********************************************************************************************/

int ssp_setCommit(char *pObjTbl)
{

    char dst_pathname_cr[64] =  {0};
    componentStruct_t ** ppComponents = NULL;
    int size2 = 0;
    int ret ;
    char *dst_componentid         =  NULL;
    char *dst_pathname            =  NULL;

    if(pObjTbl == NULL)
    {
        printf("\nssp_setCommit::Null parameter passed as argument\n");
        return 1;
    }

    strcat(dst_pathname_cr,subsystem_prefix);
    strcat(dst_pathname_cr, CCSP_DBUS_INTERFACE_CR);

    /* This function will identify Component path through Component Registrar (CR)
       pParam Name is used to as input and CR will return back the respective component
       dbus path
     */
    ret = CcspBaseIf_discComponentSupportingNamespace
        (
         bus_handle_client,
         dst_pathname_cr,
         pObjTbl,
         subsystem_prefix,
         &ppComponents,
         &size2
        );

    if ( ret == CCSP_SUCCESS )
    {
        if ( size2 == 0 )
        {
            printf("\nssp_setCommit::Can't find destination component.\n");
            return 1;
        }
    }
    else
    {
        printf("\nssp_setCommit::Can't find destination component.\n");
        return 1;
    }

    dst_componentid = ppComponents[0]->componentName;
    printf("\nssp_setCommit::Destination Component ID is %s\n",dst_componentid);
    dst_pathname = ppComponents[0]->dbusPath;
    printf("\nssp_setCommit::Destination Component Name is %s\n",dst_pathname);

    ret = CcspBaseIf_setCommit(
            bus_handle_client,
            dst_componentid,
            dst_pathname,
            0,
            DSLH_MAP_ACCESS_CONTROL_ANY,
            1
            );

    free_componentStruct_t(bus_handle_client, size2, ppComponents);

    if ( ret == CCSP_SUCCESS )
    {
        printf("\nssp_setCommit::Successfully committed the changes\n");
    }
    else
    {
        printf("\nssp_setCommit::Failed to commit the changes(error code:(%d)).\n",ret);
        return 1;
    }

    return 0;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_getHealth
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to get working condition of ccsp Component
 * @param [in]  pComponentName - Pointer to Component Name (ccsp component)
 * @param [out] N/A
 ********************************************************************************************/

int ssp_getHealth(char *pComponentName)
{

    char dst_pathname_cr[64] = {0};
    componentStruct_t ** ppComponents = NULL;
    int size2 = 0;
    int ret ;
    char *dst_componentid = NULL;
    char *dst_pathname = NULL;
    int health = 0;

    if(pComponentName == NULL)
    {
        printf("\nssp_getHealth::Null parameter passed as argument\n");
        return 1;
    }

    strcat(dst_pathname_cr,subsystem_prefix);
    strcat(dst_pathname_cr, CCSP_DBUS_INTERFACE_CR);

    /* This function will identify Component path through Component Registrar (CR)
       pParam Name is used to as input and CR will return back the respective component
       dbus path
     */
    ret = CcspBaseIf_discComponentSupportingNamespace
        (
         bus_handle_client,
         dst_pathname_cr,
         pComponentName,
         subsystem_prefix,
         &ppComponents,
         &size2
        );
    if ( ret == CCSP_SUCCESS )
    {
        if ( size2 == 0 )
        {
            printf("\nssp_getHealth::Can't find destination component.\n");
            return 1;
        }
    }
    else
    {
        printf("\nssp_getHealth::Can't find destination component.\n");
        return 1;
    }

    dst_componentid = ppComponents[0]->componentName;
    printf("\nssp_getHealth::Destination Component ID is %s\n",dst_componentid);
    dst_pathname    = ppComponents[0]->dbusPath;
    printf("\nssp_getHealth::Destination Component Name is %s\n",dst_pathname);

    ret = CcspBaseIf_getHealth(
            bus_handle_client,
            dst_componentid,
            dst_pathname,
            &health
            );

    printf("\nssp_getHealth::Component Health:%d\n",health);

    free_componentStruct_t(bus_handle_client, size2, ppComponents);

    if ( ret == CCSP_SUCCESS )
    {
        printf("\nssp_getHealth::Successfully retrieved the health of the component\n");
    }
    else
    {
        printf("\nssp_getHealth::Failed to retrieve the component health(error code:(%d)).\n",ret);
        return 1;
    }

    return 0;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_setSessionId
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to set session id of ccsp Component
 *
 * @param [in]  priority - Integer value that holds Priority Value
 * @param [in]  sessionId -Integer value that session id Value
 * @param [in]  pComponentName - Pointer to Path name of Component
 * @param [in]  override -Integer value that will inform to override the existing session id
 * @param [out] N/A
 ********************************************************************************************/

int ssp_setSessionId(int priority, int sessionId,int *pComponentName,int override)
{
    int ret = 0;
    char dst_pathname_cr[64] = {0};
    int size2 = 0;
    componentStruct_t ** ppComponents = NULL;
    char *dst_componentid = NULL;
    char *dst_pathname = NULL;

    if(override == 0)
    {
        strcat(dst_pathname_cr,subsystem_prefix);
        strcat(dst_pathname_cr, CCSP_DBUS_INTERFACE_CR);

        /* This function will identify Component path through Component Registrar (CR)
           pParam Name is used to as input and CR will return back the respective component
           dbus path
         */
        ret = CcspBaseIf_discComponentSupportingNamespace
            (
             bus_handle_client,
             dst_pathname_cr,
             pComponentName,
             subsystem_prefix,
             &ppComponents,
             &size2
            );

        if ( ret == CCSP_SUCCESS )
        {
            if ( size2 == 0 )
            {
                printf("\nssp_setSessionId::Can't find destination component.\n");
                return 1;
            }
        }
        else
        {
            printf("\nssp_setSessionId::Can't find destination component.\n");
            return 1;
        }

        dst_componentid = ppComponents[0]->componentName;
        printf("\nssp_setSessionId::Destination Component ID is %s\n",dst_componentid);
        dst_pathname = ppComponents[0]->dbusPath;
        printf("\nssp_setSessionId::Destination Component Name is %s\n",dst_pathname);

        ret = CcspBaseIf_getCurrentSessionID
            (
             bus_handle_client,
             dst_pathname_cr,
             &priority,
             &sessionId
            );

        if ( ret == CCSP_SUCCESS )
        {
            printf("\nssp_setSessionId::Successfully received the session Id as %d\n",sessionId);
        }
        else
        {
            printf("\nssp_setSessionId::Failed to received the session Id of CR(error code:(%d)).\n",ret);
            return 1;
        }
    }//override
    ret = CcspBaseIf_SendcurrentSessionIDSignal(
            bus_handle_client,
            priority,
            sessionId
            );

    if ( ret == CCSP_SUCCESS )
    {
        printf("\nssp_setSessionId::Successfully set the session Id\n");
    }
    else
    {
        printf("\nssp_setSessionId::Failed to set the session Id(error code:(%d)).\n",ret);
        return 1;
    }

    return 0;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_getParameterAttr
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to get Parameter attributes that holds
 *			  additional info to Parameter
 * @param [in]  pParamAttr - Pointer to Attribute Parameter path
 * @param [out] pParamsize - To hold the count for number of attributes parameters fetched
 * 			     from ccsp Component
 ********************************************************************************************/
GETPARAMATTR* ssp_getParameterAttr(char *pParamAttr,int *pParamAttrSize)
{

    char dst_pathname_cr[64] = {0};
    componentStruct_t **ppComponents = NULL;
    int size2 = 0;
    int ret ;
    char *dst_componentid = NULL;
    char *dst_pathname = NULL;
    int size = 0;
    int i;
    int cmpt;
    char *pParamNameAttr[MAX_PARAM_NAMES_ARRAY];
    parameterAttributeStruct_t **ppCcspAttrArray = NULL;
    int nCcspAttrArraySize = 0;

    pParamNameAttr[0] = pParamAttr;

    strcat(dst_pathname_cr,subsystem_prefix);
    strcat(dst_pathname_cr, CCSP_DBUS_INTERFACE_CR);

    /* This function will identify Component path through Component Registrar (CR)
       pParam Name is used to as input and CR will return back the respective component
       dbus path
     */
    ret = CcspBaseIf_discComponentSupportingNamespace
        (
         bus_handle_client,
         dst_pathname_cr,
         pParamAttr,
         subsystem_prefix,
         &ppComponents,
         &size2
        );


    if ( ret == CCSP_SUCCESS )
    {
        if ( size2 == 0 )
        {
            printf("\nssp_getParameterAttr::Can't find destination component.\n");
            return NULL;
        }
    }
    else
    {
        printf("\nssp_getParameterAttr::Can't find destination component.\n");
        return NULL;
    }
    for(cmpt=0; cmpt < size2; cmpt++)
    {

        dst_componentid = ppComponents[cmpt]->componentName;
        printf("\nssp_getParameterAttr::Destination Component ID is %s\n",dst_componentid);
        dst_pathname = ppComponents[cmpt]->dbusPath;
        printf("\nssp_getParameterAttr::Destination Component Name is %s\n",dst_pathname);

        ret = CcspBaseIf_getParameterAttributes
            (
             bus_handle_client,
             dst_componentid,
             dst_pathname,
             pParamNameAttr,
             1,
             &nCcspAttrArraySize,
             &ppCcspAttrArray
            );
        GetAttr=(GETPARAMATTR *)malloc(nCcspAttrArraySize*sizeof(GETPARAMATTR));
        if(GetAttr==NULL)
        {
            printf("Malloc failed in Get Arttribute function \n");
            return NULL;
        }

        if(ret == CCSP_SUCCESS  && nCcspAttrArraySize >= 1)
        {
            for ( i = 0; i < nCcspAttrArraySize; i++ )
            {

                GetAttr[i].pParamNames = (char *)malloc(MAX_PARAM_SIZE*sizeof(char));
                if(NULL==GetAttr[i].pParamNames)
                {
                    printf("Malloc failed for the struct in GetAttr\n");
                    return NULL;
                }
                memset(GetAttr[i].pParamNames,0,MAX_PARAM_SIZE*sizeof(char));
                strcpy(GetAttr[i].pParamNames,ppCcspAttrArray[i]->parameterName);

                GetAttr[i].pParamAccess = (char *)malloc(MAX_ATTRIBUTE_SIZE*sizeof(char));
                GetAttr[i].pParamNotify= (char *)malloc(MAX_ATTRIBUTE_SIZE*sizeof(char));
                if((GetAttr[i].pParamAccess==NULL) || (GetAttr[i].pParamNotify==NULL))
                {
                    printf("Malloc returned NULL in GetAttr function\n");
                    return NULL;
                }
                memset(GetAttr[i].pParamAccess,0,MAX_ATTRIBUTE_SIZE*sizeof(char));
                memset(GetAttr[i].pParamNotify,0,MAX_ATTRIBUTE_SIZE*sizeof(char));
                if (  ppCcspAttrArray[i]->notification == 1)
                    strcpy(GetAttr[i].pParamNotify,"on");
                else if ( ppCcspAttrArray[i]->notification ==0)
                    strcpy(GetAttr[i].pParamNotify, "off");
                else
                    strcpy(GetAttr[i].pParamNotify, "off");

                if ( ppCcspAttrArray[i]->accessControlBitmask == 0x0)
                    strcpy(GetAttr[i].pParamAccess,"acs");
                else if ( ppCcspAttrArray[i]->accessControlBitmask == 0x1)
                    strcpy(GetAttr[i].pParamAccess,"xmpp");
                else if ( ppCcspAttrArray[i]->accessControlBitmask == 0x2)
                    strcpy(GetAttr[i].pParamAccess,"cli");
                else if ( ppCcspAttrArray[i]->accessControlBitmask == 0x4)
                    strcpy(GetAttr[i].pParamAccess,"webgui");
                else if ( ppCcspAttrArray[i]->accessControlBitmask == 0xFFFFFFFF)
                    strcpy(GetAttr[i].pParamAccess,"anybody");
                printf("Parameter Name:%s\n",GetAttr[i].pParamNames);
                printf("Notification :%s AccessControl %s\n",GetAttr[i].pParamNotify,GetAttr[i].pParamAccess);

            }
        }
        else
        {
            printf("CcspBaseIf_getParameterAttributes function returned 1 \n");
            return NULL;
        }

    }

    *pParamAttrSize = nCcspAttrArraySize;
    free_parameterAttributeStruct_t (bus_handle_client,nCcspAttrArraySize,ppCcspAttrArray);
    ppCcspAttrArray = NULL;
    free_componentStruct_t(bus_handle_client, size2, ppComponents);
    printf("Return from the Get Attributes Component Stub\n");
    return GetAttr;
}

/*******************************************************************************************
 * Function Name        : ssp_setParameterAttr
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to get Parameter attributes that holds
 *			  additional info to Parameter
 * @param [in]  pParamName  - Pointer to Attribute Parameter path
 * @param [in]  pAttrNotify - This will change the "notification" attribute for the parmeter
 *			      that can be off,passive or active
 * @param [in]	pAttrAccess - This will change the "accessControlChanged" attribute for the
 * 			      given parameter that can be "acs","xmpp","cli","webgui" or
 * 			      "anybody"
 * @param [out] N/A
 ********************************************************************************************/

int ssp_setParameterAttr(char *pParamName,char *pAttrNotify,char *pAttrAccess)
{

    char dst_pathname_cr[64] =  {0};
    componentStruct_t ** ppComponents = NULL;
    int size2 = 0;
    int ret ;
    char *dst_componentid         =  NULL;
    char *dst_pathname            =  NULL;
    int size = 0;
    int i;
    int nCcspAttrArraySize   = 0;
    parameterAttributeStruct_t valAttr[MAX_COMP_ARRAY] = {{0}};

    strcat(dst_pathname_cr,subsystem_prefix);
    strcat(dst_pathname_cr, CCSP_DBUS_INTERFACE_CR);

    /* This function will identify Component path through Component Registrar (CR)
       pParam Name is used to as input and CR will return back the respective component
       dbus path
     */
    ret = CcspBaseIf_discComponentSupportingNamespace
        (
         bus_handle_client,
         dst_pathname_cr,
         pParamName,
         subsystem_prefix,
         &ppComponents,
         &size2
        );


    if ( ret == CCSP_SUCCESS )
    {
        if ( size2 == 0 )
        {
            printf("ssp_setParameterAttr::Can't find destination component.\n");
            return 1;
        }
    }
    else
    {
        printf("ssp_setParameterAttr::Can't find destination component.\n");
        return 1;
    }

    dst_componentid = ppComponents[0]->componentName;
    printf("\n ssp_setParameterAttr::Destination Component ID is %s\n",dst_componentid);
    dst_pathname    = ppComponents[0]->dbusPath;
    printf("\n ssp_setParameterAttr::Destination Component Name is %s\n",dst_pathname);

    valAttr[size].parameterName  = pParamName;
    valAttr[size].notificationChanged = 1;
    valAttr[size].accessControlChanged = 1;


    if ( strcmp(pAttrNotify,"passive" )==0 )
        valAttr[size].notification = 1;
    else if ( strcmp(pAttrNotify,"active")==0 )
        valAttr[size].notification = 2;
    else if ( strcmp(pAttrNotify, "off")==0 )
        valAttr[size].notification = 0;
    else
    {
        valAttr[size].notification = 0;
        valAttr[size].notificationChanged = 0;
    }

    if ( strcmp(pAttrAccess,"acs" )==0 )
        valAttr[size].accessControlBitmask = 0x0;
    else if ( strcmp(pAttrAccess,"xmpp")==0 )
        valAttr[size].accessControlBitmask = 0x1;
    else if ( strcmp(pAttrAccess,"cli")==0 )
        valAttr[size].accessControlBitmask = 0x2;
    else if ( strcmp(pAttrAccess,"webgui")==0 )
        valAttr[size].accessControlBitmask = 0x4;
    else if ( strcmp(pAttrAccess,"anybody")==0 )
        valAttr[size].accessControlBitmask = 0xFFFFFFFF;
    else
    {
        valAttr[size].accessControlBitmask = 0;
        valAttr[size].accessControlChanged = 0;
    }



    ret = CcspBaseIf_setParameterAttributes(
            bus_handle_client,
            dst_componentid,
            dst_pathname,
            0,
            valAttr,
            1
            );

    free_componentStruct_t(bus_handle_client, size2, ppComponents);

    if ( ret == CCSP_SUCCESS )
    {
        printf("\n ssp_setParameterAttr::Execution succeed.\n");
    }
    else
    {
        printf("\n ssp_setParameterAttr::Execution fail(error code:(%d)).\n",ret);
        return 1;
    }

    return 0;
}

/*******************************************************************************************
 *
 * Function Name        : free_Memory_Names
 * Description          : This function will free memory allocated for GetParamterNames API
 ********************************************************************************************/
void free_Memory_Names(int size,GETPARAMNAMES *Freestruct)
{
    int i=0;
    for(i=0;i<size;i++)
    {

        free(Freestruct[i].pParamNames);
        Freestruct[i].pParamNames=NULL;
    }

    free(Freestruct);
    Freestruct=NULL;
}
/*******************************************************************************************
 *
 * Function Name        : free_Memory_val
 * Description          : This function will free memory allocated for GetParamterValues API
 ********************************************************************************************/
void free_Memory_val(int size,GETPARAMVALUES *Freestruct)
{
    int i=0;
    for(i=0;i<size;i++)
    {
        free(Freestruct[i].pParamValues);
        Freestruct[i].pParamValues=NULL;
        free(Freestruct[i].pParamNames);
        Freestruct[i].pParamNames=NULL;
    }

    free(Freestruct);
    Freestruct=NULL;
}
/*******************************************************************************************
 *
 * Function Name        : free_Memory_Attr
 * Description          : This function will free memory allocated for GetParamterAttributes API
 ********************************************************************************************/
void free_Memory_Attr(int size,GETPARAMATTR *Freestruct)
{
    int i=0;
    for(i=0;i<size;i++)
    {
        free(Freestruct[i].pParamAccess);
        Freestruct[i].pParamAccess=NULL;
        free(Freestruct[i].pParamNotify);
        Freestruct[i].pParamNotify=NULL;
        free(Freestruct[i].pParamNames);
        Freestruct[i].pParamNames=NULL;

    }
    free(Freestruct);
    Freestruct=NULL;
}

int ssp_setMultipleParameterValue(char **paramList, int size)
{
    char        dst_pathname_cr[64] =  {0};
    componentStruct_t ** ppComponents = NULL;
    int         size2 = 0;
    int         ret ;
    char *      dst_componentid         =  NULL;
    char *      dst_pathname            =  NULL;
    parameterValStruct_t **parameterVal = NULL;
    int         j, i = 0;
    unsigned char bTmp = 0;
    char * pFaultParameter = NULL;
    parameterValStruct_t val[MAX_COMP_ARRAY] = {{NULL},{NULL},{NULL}};
    int index = 0;
    char *pParamName = NULL;
    char* pParamType = NULL;

    strcat(dst_pathname_cr,subsystem_prefix);
    strcat(dst_pathname_cr, CCSP_DBUS_INTERFACE_CR);

    printf("dst_pathname_cr:%s\n",dst_pathname_cr);

    bTmp = 1;

    /*This function will identify Component path through Component Registrar (CR)
     pParam Name is used to as input and CR will return back the respective component
     dbus path */
    ret = CcspBaseIf_discComponentSupportingNamespace
          (
            bus_handle_client,
            dst_pathname_cr,
            paramList[i],
            subsystem_prefix,
            &ppComponents,
            &size2
          );

    if ( ret == CCSP_SUCCESS )
    {
        if ( size2 == 0 )
        {
            printf("\nssp_setParameterValue::Can't find destination component.\n");
            return 1;
        }
    }
    else
    {
        printf("\nssp_setParameterValue::Can't find destination component.\n");
        return 1;
    }

    dst_componentid = ppComponents[0]->componentName;
    printf("\nssp_setParameterValue::Destination Component ID is %s\n",dst_componentid);
    dst_pathname    = ppComponents[0]->dbusPath;
    printf("\nssp_setParameterValue::Destination Component Name is %s\n",dst_pathname);

    while( paramList[i]!=NULL )
    {
        val[j].parameterName  = paramList[i];
        i++;
        val[j].parameterValue = paramList[i];
        i++;
        pParamType = paramList[i];

        if(strcmp(pParamType,"string")==0)
        {
            val[j].type = ccsp_string;
        }
        else if (strcmp(pParamType,"int")==0)
        {
            val[j].type = ccsp_int;
        }
        else if (strcmp(pParamType,"unsignedint")==0)
        {
            val[j].type = ccsp_unsignedInt;
        }
        else if (strcmp(pParamType,"unsignedInt")==0)
        {
            val[j].type = ccsp_unsignedInt;
        }
        else if (strcmp(pParamType,"boolean")==0)
        {
            val[j].type = ccsp_boolean;
        }
        else if (strcmp(pParamType,"bool")==0)
        {
            val[j].type = ccsp_boolean;
        }
        else if (strcmp(pParamType,"datetime")==0)
        {
            val[j].type = ccsp_dateTime;
        }
        else if (strcmp(pParamType,"base64")==0)
        {
            val[j].type = ccsp_base64;
        }
        else if (strcmp(pParamType,"long")==0)
        {
            val[j].type = ccsp_long;
        }
        else if (strcmp(pParamType,"unsignedlong")==0)
        {
            val[j].type = ccsp_unsignedLong;
        }
        else if (strcmp(pParamType,"float")==0)
        {
            val[j].type = ccsp_float;
        }
        else if (strcmp(pParamType,"double")==0)
        {
            val[j].type = ccsp_double;
        }
        else if (strcmp(pParamType,"byte")==0)
        {
            val[j].type = ccsp_byte;
        }
        else if (strcmp(pParamType,"none")==0)
        {
           val[j].type = ccsp_none;
        }

        printf("\nssp_setParameterValue:: val%d param name is %s",j, val[j].parameterName);
        printf("\nssp_setParameterValue:: val%d param value is %s",j, val[j].parameterValue);
        printf("\nssp_setParameterValue:: val%d param type is %d",j, val[j].type);
        i++;
        j++;

    }

    ret = CcspBaseIf_setParameterValues(
            bus_handle_client,
            dst_componentid,
            dst_pathname,
            0,
            DSLH_MPA_ACCESS_CONTROL_CLIENTTOOL,
            val,
            size,
            bTmp,
            &pFaultParameter
            );

    free_componentStruct_t(bus_handle_client, size2, ppComponents);

    if ( ret == CCSP_SUCCESS )
    {
        printf("\nssp_setParameterValue::Execution succeed.\n");
    }
    else
    {
        printf("\nssp_setParameterValue::Execution fail(error code:(%d)).\n",ret);
        return 1;
    }

 if ( pFaultParameter != NULL )
        AnscFreeMemory(pFaultParameter);

    return 0;
}


int ssp_Diag_Init()
{
    diag_err_t status = diag_init();

    if(status != DIAG_ERR_OK)
    {
        printf("ssp_BbhmDiagipStartDiag: diag_init failed\n");
        return 1;
    }
    else
    {
        printf("ssp_BbhmDiagipStartDiag: diag_init success\n");
        return 0;
    }
}

int ssp_Diag_Start(int mode)
{
    diag_err_t status;
    diag_mode_t diag_mode = mode;
    diag_obj_t *diag_ping_obj;

    status = diag_start(diag_mode);
    if(status == DIAG_ERR_OK)
    {
        printf("diag_start success\n");
        return 0;
    }
    else
    {
        printf("diag_start failed. status %d\n", status);
        return 1;
    }
}


int ssp_Diag_Stop(int mode)
{
    diag_err_t status;
    diag_mode_t diag_mode = mode;

    status = diag_stop(mode);
    sleep(20);

    if(status == DIAG_ERR_OK)
    {
        printf("diag_stop success. Status is %d\n", status);
        return 0;
    }
    else
    {
        printf("diag_stop failed. Status is %d\n", status);
        return 1;
    }
    diag_term();
}

int ssp_Diag_SetCfg(int mode, diag_cfg *cfg)
{
    printf("In ssp_Diag_SetCfg\n");
    diag_err_t status;
    diag_cfg_t cfg_t;
    strcpy(cfg_t.host, cfg->host);
    cfg_t.cnt = PING_DEF_COUNT;
    cfg_t.timo = PING_DEF_TIMEO;
    cfg_t.size = PING_DEF_BSIZE;

    status = diag_setcfg(mode, &cfg_t);
    if(status == DIAG_ERR_OK ){
        printf("diag_set_cfg success.\n");
        return 0;
    }
    else
    {
        printf("diag_set_cfg failed %d host %s\n", status, cfg_t.host);
        return 1;
    }
}


int ssp_Diag_GetCfg(int mode, diag_cfg *cfg)
{
    printf("In ssp_Diag_GetCfg\n");
    diag_err_t status; diag_cfg_t cfg_t;

    status = diag_getcfg(mode, &cfg_t); strcpy(cfg->host, cfg_t.host);
    if(status == DIAG_ERR_OK ){
        printf("diag_get_cfg success.\n");
        return 0;
    }
    else
    {
        printf("diag_get_cfg failed\n");
        return 1;
    }
}


int ssp_Diag_GetState(int mode, int *state)
{
    printf("In ssp_Diag_GetState\n");
    diag_err_t status;

    status = diag_getstate(mode, state);
    if(status == DIAG_ERR_OK ){
        printf("diag_getstate success.\n");
        return 0;
    }
    else
    {
        printf("diag_getstate failed\n");
        return 1;
    }
}

