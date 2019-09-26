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

#ifndef __SSP_MBUS_WRP_C__
#define __SSP_MBUS_WRP_C__

#include "ssp_global.h"
#include "ccsp_dm_api.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ssp_tdk_wrp.h"
#include "ssp_tdk_mbus_wrp.h"
#include "ssp_tdk_mbus_lib.h"
#include <ccsp_message_bus.h>
#include <ccsp_base_api.h>
#include "ccsp_memory.h"
#include <ccsp_custom.h>
#include <dslh_definitions_database.h>
#if !defined(CCSP_INC_no_asm_sigcontext_h)
#endif

//Global Declarations

void *tdk_bus_handle = NULL;
PCCSP_COMPONENT_CFG gpTDKStartCfg = NULL ;
PCCSP_DM_XML_CFG_LIST gpTDKDmXml  = NULL;
name_spaceType_t name_space[11];
int sessionId=0;
extern char subsystem_prefix[32];

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_loadcfg
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to load Component specific base config file
 *
 * @param [in]          : pCmpCfg - Config file name with absolute path
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_loadcfg(char *pCmpCfg)
{
    int return_status = SSP_MBUS_FAILURE;
    int eRTName[100] = {0};
    printf("\n ssp_mbus_loadcfg :: Make file option for subsytem flag eRT is set to %d",eRT);
    if(eRT == 1)
    {
        strcpy(subsystem_prefix,"eRT.");
    }

    if (gpTDKStartCfg == NULL)
    {
        gpTDKStartCfg = (PCCSP_COMPONENT_CFG)AnscAllocateMemory(sizeof(CCSP_COMPONENT_CFG));
    }

    return_status = CcspComponentLoadCfg(pCmpCfg,
            gpTDKStartCfg);

    strcat(eRTName,subsystem_prefix);
    strcat(eRTName,gpTDKStartCfg->ComponentId);
    strcpy(gpTDKStartCfg->ComponentId,eRTName);

    eRTName[0] = '\0';
    strcat(eRTName,subsystem_prefix);
    strcat(eRTName,gpTDKStartCfg->ComponentName);
    strcpy(gpTDKStartCfg->ComponentName,eRTName);
    sprintf(gpTDKStartCfg->DbusPath,"/com/cisco/spvtg/ccsp/tdkb");

    gpTDKStartCfg->Version = 1;

    printf("\ngpTDKStartCfg->ComponentId is %s",gpTDKStartCfg->ComponentId);
    printf("\ngpTDKStartCfg->ComponentName is %s",gpTDKStartCfg->ComponentName);
    printf("\ngpTDKStartCfg->DbusPath is %s",gpTDKStartCfg->DbusPath);
    printf("\ngpTDKStartCfg->Version is %d",gpTDKStartCfg->Version);

    if(return_status != SSP_MBUS_SUCCESS)
    {
        printf("\n ssp_mbus_loadcfg :: CcspComponentLoadCfg fails with ansc return status value %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }

    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_load_dmlxml
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to load Component specific DataModel XML file
 *
 * @param [in]          : pCmpDmXml - DataModel file name with absolute path
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_load_dmlxml(char *pCmpDmXml)
{
    int return_status = SSP_MBUS_FAILURE;

    if(gpTDKDmXml == NULL)
    {
        gpTDKDmXml = (PCCSP_DM_XML_CFG_LIST)AnscAllocateMemory(sizeof(CCSP_DM_XML_CFG_LIST));
    }

    return_status = CcspComponentLoadDmXmlList(pCmpDmXml,
            &gpTDKDmXml);

    if(return_status != SSP_MBUS_SUCCESS)
    {
        printf("\n ssp_mbus_load_dmlxml :: CcspComponentLoadDmXmlList fails with ansc return status value %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    else
    {
        printf("\n ssp_mbus_load_dmlxml :: CcspComponentLoadDmXmlList success with ansc return status value %d",return_status);
    }
    if(gpTDKDmXml!= NULL)
    {
        AnscFreeMemory(gpTDKDmXml);
        gpTDKDmXml = NULL;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_init
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to initialize message bus that provides valid
 *                        handle
 *
 * @param [in]          : pCfg    - Config file name with absolute path
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_init(char *pCfg)
{

    int return_status;

    printf("\n ssp_mbus_init :: Entering");

    return_status = CCSP_Message_Bus_Init(gpTDKStartCfg->ComponentName,
            pCfg,
            &tdk_bus_handle,
            Ansc_AllocateMemory_Callback,
            Ansc_FreeMemory_Callback);

    if ( return_status == SSP_MBUS_SUCCESS )
    {
        printf("\n ssp_mbus_init :: CCSP_Message_Bus_Init Success and bus hadle instance is %x",tdk_bus_handle);
    }
    else
    {
        printf("\n ssp_mbus_init :: CCSP_Message_Bus_Init Failure and returns Error Status as %d",return_status);
        return SSP_MBUS_FAILURE;
    }

    return  SSP_MBUS_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_exit
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to close the message bus handle
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_exit()
{

    int return_status = SSP_MBUS_FAILURE;

    CCSP_Message_Bus_Exit(tdk_bus_handle);
    tdk_bus_handle = NULL;

    if(tdk_bus_handle == NULL)
    {
        printf("\n ssp_mbus_exit :: CCSP_Message_Bus_Exit has close the bus handle successfully\n");
        ssp_mbus_unloadcfg();
        return SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_exit :: CCSP_Message_Bus_Exit FAILURE. Existing bus handle %x is not closed\n",tdk_bus_handle);
    }

    return SSP_MBUS_FAILURE;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_register_path
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_register_path()
{

    int return_status = SSP_MBUS_FAILURE;

    printf("\n ssp_mbus_register_path is invoking Base API with Dbus path %s",gpTDKStartCfg->DbusPath);

    /* Invoke API Under Test to Register bus path */
    return_status = CCSP_Message_Bus_Register_Path(tdk_bus_handle,
            gpTDKStartCfg->DbusPath,
            tdk_path_message_func,
            tdk_bus_handle);

    if(return_status == CCSP_Message_Bus_OK)
    {
        printf("\n ssp_mbus_register_path :: CCSP_Message_Bus_Register_Path function registers bus path with name %s is success with return value %d",gpTDKStartCfg->DbusPath,return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_register_path :: CCSP_Message_Bus_Register_Path function registers bus path with name %s is failure with return value %d",gpTDKStartCfg->DbusPath,return_status);
        return_status = SSP_MBUS_FAILURE;
    }

    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_register_capabilities
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_register_capabilities()
{

    int return_status = SSP_MBUS_FAILURE;
    char buf[11][256];
    const char *subsystem_prefix = "TDKB";

    sprintf(buf[0],"%s%s.Name",CCSP_NAME_PREFIX,gpTDKStartCfg->ComponentName);
    name_space[0].name_space = buf[0];
    name_space[0].dataType = ccsp_string;

    sprintf(buf[1],"%s%s.Version",CCSP_NAME_PREFIX,gpTDKStartCfg->ComponentName);
    name_space[1].name_space = buf[1];
    name_space[1].dataType = ccsp_int;

    sprintf(buf[2],"%s%s.Author",CCSP_NAME_PREFIX,gpTDKStartCfg->ComponentName);
    name_space[2].name_space = buf[2];
    name_space[2].dataType = ccsp_string;

    sprintf(buf[3],"%s%s.Health",CCSP_NAME_PREFIX,gpTDKStartCfg->ComponentName);
    name_space[3].name_space = buf[3];
    name_space[3].dataType = ccsp_string;

    sprintf(buf[4],"%s%s.State",CCSP_NAME_PREFIX,gpTDKStartCfg->ComponentName);
    name_space[4].name_space = buf[4];
    name_space[4].dataType = ccsp_int;

    sprintf(buf[5],"%s%s.Logging.Enable",CCSP_NAME_PREFIX,gpTDKStartCfg->ComponentName);
    name_space[5].name_space = buf[5];
    name_space[5].dataType = ccsp_boolean;

    sprintf(buf[6],"%s%s.Logging.LogLevel",CCSP_NAME_PREFIX,gpTDKStartCfg->ComponentName);
    name_space[6].name_space = buf[6];
    name_space[6].dataType = ccsp_int;

    sprintf(buf[7],"%s%s.Memory.MinUsage",CCSP_NAME_PREFIX,gpTDKStartCfg->ComponentName);
    name_space[7].name_space = buf[7];
    name_space[7].dataType = ccsp_int;

    sprintf(buf[8],"%s%s.Memory.MaxUsage",CCSP_NAME_PREFIX,gpTDKStartCfg->ComponentName);
    name_space[8].name_space = buf[8];
    name_space[8].dataType = ccsp_int;

    sprintf(buf[9],"%s%s.Memory.Consumed",CCSP_NAME_PREFIX,gpTDKStartCfg->ComponentName);
    name_space[9].name_space = buf[9];
    name_space[9].dataType = ccsp_int;

    return_status =  CcspBaseIf_registerCapabilities(tdk_bus_handle,
            CCSP_CR_NAME,
            gpTDKStartCfg->ComponentName,
            gpTDKStartCfg->Version,
            gpTDKStartCfg->DbusPath,
            subsystem_prefix,
            name_space,
            10);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_register_capabilities :: CcspBaseIf_registerCapabilities function is success with return value %d",return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_register_capabilities:: CcspBaseIf_registerCapabilities function is failure with return value %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }

    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_register_base
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_register_base()
{
    int return_status = SSP_MBUS_FAILURE;

    return_status =  CcspBaseIf_registerBase(tdk_bus_handle,
            CCSP_CR_NAME,
            gpTDKStartCfg->ComponentName,
            gpTDKStartCfg->Version,
            gpTDKStartCfg->DbusPath,
            "0");

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_register_base :: CcspBaseIf_registerBase function is success with return status %d",return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_register_base :: CcspBaseIf_registerBase function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }

    return return_status;
}

/*******************************************************************************************
 *
 * Function Name    : registerEventCb
 * Description      : This function is callback function for the event registration
 *
 *
 * @param [in]  val -  Holds the signal Structure Value
 * @param [in]  size - size of the user data
 * @param [in]  user_data - Pointer to the user data
 * @param [out] - Nil
 *
 ********************************************************************************************/
static void registerEventCb(parameterSigStruct_t* val, int size, void* user_data)
{
    printf("\n registerEventCb:: Send Signal has triggered the Registered Event \n\n");
}


/*******************************************************************************************
 *
 * Function Name    : registerEventCb
 * Description      : This function is callback function for the event registration
 * @param [in]      : Nil
 * @param [out]     : return status of type integer
 ********************************************************************************************/

int ssp_mbus_SendsystemReadySignal(void)
{
    int return_status = 0;

    if(tdk_bus_handle == NULL)
    {
        printf("\n Bus handle doesnt exist. Message bus needs to be initialized first");
        return SSP_MBUS_FAILURE;
    }

    return_status = CcspBaseIf_SendsystemReadySignal(tdk_bus_handle);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_SendsystemReadySignal :: Successfully send the system ready signal %d",return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_SendsystemReadySignal :: Failed to send the system ready signal %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;

}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_register_event
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to close the message bus handle
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_register_event(char *pEventName)
{
    int return_status = SSP_MBUS_FAILURE;


    CCSP_Base_Func_CB cb;
    memset(&cb, 0 , sizeof(cb));
    cb.systemReadySignal = registerEventCb;

    CcspBaseIf_SetCallback
        (
         tdk_bus_handle,
         &cb
        );

    printf("\nssp_mbus_register_event:: Event requested for register with CR is %s",pEventName);

    return_status = CcspBaseIf_Register_Event(tdk_bus_handle,
            0,
            pEventName);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_register_event :: CcspBaseIf_Register_Event function is success with return status %d",return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_register_event :: CcspBaseIf_Register_Event function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }

    /* To De-Init/close the tdk bus handle irrespective the registration status*/

    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_unregister_event
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to close the message bus handle
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_unregister_event(char *pEventName)
{

    int return_status = SSP_MBUS_FAILURE;


    printf("\nssp_mbus_register_event:: Event requested for Unregister with CR is %s",pEventName);

    return_status = CcspBaseIf_UnRegister_Event(tdk_bus_handle,
            0,
            pEventName);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_unregister_event :: CcspBaseIf_UnRegister_Event function is success with return status %d",return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_unregister_event :: CcspBaseIf_UnRegister_Event function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }

    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_query_status
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to check the status of a given component
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_query_status()
{

    int return_status = SSP_MBUS_FAILURE;
    int internalState = 0;

    /* Invoke API Under Test to Query Component(TDK) Status */
    return_status = CcspBaseIf_queryStatus(tdk_bus_handle,
            CCSP_CR_NAME,
            "/com/cisco/spvtg/ccsp/CR",
            &internalState
            );

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_query_status :: CcspBaseIf_queryStatus function returns state as  %d is success with return value %d",internalState,return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_query_status :: CcspBaseIf_queryStatus function returns state as %d is failure with return value %d",internalState,return_status);
        return_status = SSP_MBUS_FAILURE;
    }

    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_get_allocmemory
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_get_allocmemory()
{
    int return_status = SSP_MBUS_FAILURE;
    int allocatedMemory = 0;

    /* Invoke API Under Test to Query Component(TDK) Staus */
    return_status = CcspBaseIf_getAllocatedMemory (tdk_bus_handle,
            CCSP_CR_NAME,
            "/com/cisco/spvtg/ccsp/CR",
            &allocatedMemory);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_get_allocmemory :: CcspBaseIf_getAllocatedMemory function returns allocated memory as %d is success with return value %d",allocatedMemory,return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_get_allocmemory :: CcspBaseIf_getAllocatedMemory function returns allocated memory as %d is failure with return value %d",allocatedMemory,return_status);
        return_status = SSP_MBUS_FAILURE;
    }

    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_get_maxmemory
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : pCfg    - N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_get_maxmemory()
{
    int return_status = SSP_MBUS_FAILURE;
    int maxMemory = 0;

    /* Invoke API Under Test to Query Component(TDK) Staus */
    return_status = CcspBaseIf_getMaxMemoryUsage(tdk_bus_handle,
            CCSP_CR_NAME,
            "/com/cisco/spvtg/ccsp/CR",
            &maxMemory);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_get_maxmemory :: CcspBaseIf_getMaxMemoryUsage function returns maximum memory as %d is success with return value %d",maxMemory,return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_get_maxmemory :: CcspBaseIf_getMaxMemoryUsage function returns maximum memory as %d is failure with return value %d",maxMemory,return_status);
        return_status = SSP_MBUS_FAILURE;
    }


    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_namespace_supportedby_component
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : pCfg    - N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_namespace_supportedby_component()
{
    name_spaceType_t**              pNsArray;
    int                             nNsArraySize;
    int return_status = SSP_MBUS_FAILURE;
    return_status = CcspBaseIf_discNamespaceSupportedByComponent(tdk_bus_handle,
            CCSP_CR_NAME,
            gpTDKStartCfg->ComponentName,
            &pNsArray,
            &nNsArraySize);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_namespace_supportedby_component :: CcspBaseIf_discNamespaceSupportedByComponent function is success with namespace as %s with size %d and  return status %d",pNsArray[0]->name_space,nNsArraySize,return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_namespace_supportedby_component :: CcspBaseIf_discNamespaceSupportedByComponent function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }

    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_component_supporting_dynamictbl
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_component_supporting_dynamictbl()
{
    componentStruct_t   *component;
    int return_status = SSP_MBUS_FAILURE;
    /* Component name is used as namepace - To be verified while testing */
    return_status = CcspBaseIf_discComponentSupportingDynamicTbl (tdk_bus_handle,
            CCSP_CR_NAME,
            gpTDKStartCfg->ComponentName,
            "TDKB",
            &component);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_component_supporting_dynamictbl :: CcspBaseIf_discComponentSupportingDynamicTbl function is success with component name as %s and return status %d",component->componentName,return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_component_supporting_dynamictbl :: CcspBaseIf_discComponentSupportingDynamicTbl function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_get_registered_components
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_get_registered_components()
{

    componentStruct_t   **component;
    int componentSize=0;
    int cmpLoopCnt=0;
    int return_status = SSP_MBUS_FAILURE;
    return_status = CcspBaseIf_getRegisteredComponents(tdk_bus_handle,
            CCSP_CR_NAME,
            &component,
            &componentSize);

    if(return_status == CCSP_SUCCESS)
    {
        for(cmpLoopCnt=0;cmpLoopCnt<componentSize;cmpLoopCnt++)
        {
            printf("\n ssp_mbus_get_registered_components :: CcspBaseIf_getRegisteredComponents function is success with component name  as %s for  index %d and  return status %d",component[cmpLoopCnt]->componentName,cmpLoopCnt+1,return_status);
        }
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_get_registered_components :: CcspBaseIf_getRegisteredComponents function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;

}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_check_namespace_datatype
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_check_namespace_datatype()
{
    name_spaceType_t NameSt;
    dbus_bool   typeRet;
    int return_status = SSP_MBUS_FAILURE;
    return_status = CcspBaseIf_checkNamespaceDataType (tdk_bus_handle,
            CCSP_CR_NAME,
            name_space,
            "TDKB",
            &typeRet);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_check_namespace_datatype :: CcspBaseIf_checkNamespaceDataType function is success for namespace %s datatype is  %d and  return status %d",name_space->name_space,typeRet,return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_check_namespace_datatype :: CcspBaseIf_checkNamespaceDataType function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_dump_component_registry
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_dump_component_registry()
{

    int return_status = SSP_MBUS_FAILURE;

    return_status = CcspBaseIf_dumpComponentRegistry (tdk_bus_handle,
                                                      CCSP_CR_NAME);

    /* RDKB-109:The return code from dbus is 1 and this is not a error as per dbus spec. CR dump is available in the CRlog.txt.0 */
    if((return_status == CCSP_SUCCESS) || (return_status == 1))
    {
        printf("\n ssp_mbus_dump_component_registry :: CcspBaseIf_dumpComponentRegistry function is success and  return status %d",return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_dump_component_registry :: CcspBaseIf_dumpComponentRegistry function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_issystem_ready
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_issystem_ready()
{

    dbus_bool   systemStatus;
    int return_status = SSP_MBUS_FAILURE;
    return_status = CcspBaseIf_isSystemReady(tdk_bus_handle,
            CCSP_CR_NAME,
            &systemStatus);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_issystem_ready :: CcspBaseIf_isSystemReady function is success and  system status is %d with return status %d",systemStatus,return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_issystem_ready :: CcspBaseIf_isSystemReady function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_getHealth
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to get health of the component
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_getHealth(char *cmpId, char*cmpPath)
{

    printf("Entering ssp_mbus_getHealth\n");
    int return_status = 0;
    int health = 0;

    if(tdk_bus_handle == NULL)
    {
        printf("\n Bus handle doesnt exist. Message bus needs to be initialized first");
        return SSP_MBUS_FAILURE;
    }

    if(cmpId == NULL)
    {
        printf("Input argument is NULL\n\n");
        return SSP_MBUS_FAILURE;
    }

    if(cmpPath == NULL)
    {
        printf("Input argument is NULL\n\n");
        return SSP_MBUS_FAILURE;
    }

    printf("\n ssp_mbus_getHealth :: Component id to be check is %s",cmpId);
    printf("\n ssp_mbus_getHealth :: Component Path to be check is %s",cmpPath);

    return_status = CcspBaseIf_getHealth(tdk_bus_handle,cmpId,cmpPath,&health);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_getHealth :: Successfully retrieved the health of the component %d",return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_getHealth :: Failed to retrieve the health of the component %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;

}
/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_bus_check
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_bus_check()
{

    int return_status = SSP_MBUS_FAILURE;
    return_status = CcspBaseIf_busCheck(tdk_bus_handle,
            CCSP_CR_NAME);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_bus_check :: CcspBaseIf_busCheck function is success with return status %d",return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_bus_check :: CcspBaseIf_busCheck function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_req_sessionid
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_req_sessionid(char *pCfg,char *pcmpCfg,int apitest)
{
    int return_status = SSP_MBUS_FAILURE;
    int priority=1;
    return_status = CcspBaseIf_requestSessionID(tdk_bus_handle,
            CCSP_CR_NAME,
            priority,
            &sessionId);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_req_sessionid :: CcspBaseIf_requestSessionID function is success and session id is %d with return status %d",sessionId,return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_req_sessionid :: CcspBaseIf_requestSessionID function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_unregister_namespace
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_unregister_namespace()
{
    int return_status = SSP_MBUS_FAILURE;
    return_status = CcspBaseIf_unregisterNamespace (tdk_bus_handle,
            CCSP_CR_NAME,
            CCSP_PAM_NAME,
            CCSP_TDKB_NAMESPACE);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_unregister_namespace :: CcspBaseIf_unregisterNamespace function is success with return value %d",return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_unregister_namespace :: CcspBaseIf_unregisterNamespace function is failure with return value %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_unregistercomponent
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_unregistercomponent()
{

    int return_status = SSP_MBUS_FAILURE;
    return_status = CcspBaseIf_unregisterComponent (tdk_bus_handle,
            CCSP_CR_NAME,
            gpTDKStartCfg->ComponentName
            );

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_unregistercomponent :: CcspBaseIf_unregisterComponent function is success with return value %d",return_status);
        return_status = SSP_MBUS_SUCCESS;
    }
    else
    {
        printf("\n ssp_mbus_unregistercomponent :: CcspBaseIf_unregisterComponent function is failure with return value %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_inform_end_session
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to register a component path
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mbus_inform_end_session()
{
    int return_status = SSP_MBUS_FAILURE;
    return_status = CcspBaseIf_informEndOfSession(tdk_bus_handle,
            CCSP_CR_NAME,
            sessionId);

    if(return_status == CCSP_SUCCESS)
    {
        printf("\n ssp_mbus_inform_end_session :: CcspBaseIf_informEndOfSession function is success for session id %d with return status %d",sessionId,return_status);
        return_status = SSP_MBUS_SUCCESS;
        sessionId=0;
    }
    else
    {
        printf("\n ssp_mbus_inform_end_session :: CcspBaseIf_informEndOfSession function is failure and return status %d",return_status);
        return_status = SSP_MBUS_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mbus_unloadcfg
 * Description          : This function will call base interface funtion which is defined
 *                        on top of dbus calls to unload Component specific base config file
 *
 * @param [in]          : N/A
 * @param [out]         : N/A
 ********************************************************************************************/

int ssp_mbus_unloadcfg()
{

    printf("Entering ssp_mbus_unloadcfg function\n");
    if(gpTDKStartCfg != NULL)
    {
        AnscFreeMemory(gpTDKStartCfg);
    }

    gpTDKStartCfg = NULL;

    printf("Exiting ssp_mbus_unloadcfg function\n");

    return 0;
}
#endif
