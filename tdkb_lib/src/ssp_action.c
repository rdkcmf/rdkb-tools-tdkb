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
/**********************************************************************
   Copyright [2014] [Cisco Systems, Inc.]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
**********************************************************************/

/**********************************************************************

    module: ssp_action.c

        For CCSP Secure Software Download

    ---------------------------------------------------------------

description:

SSP implementation of the General Bootloader Interface
Service.

 *   ssp_create_pnm
 *   ssp_engage_pnm
 *   ssp_cancel_pnm
 *   ssp_PnmCCDmGetComponentName
 *   ssp_PnmCCDmGetComponentVersion
 *   ssp_PnmCCDmGetComponentAuthor
 *   ssp_PnmCCDmGetComponentHealth
 *   ssp_PnmCCDmGetComponentState
 *   ssp_PnmCCDmGetLoggingEnabled
 *   ssp_PnmCCDmSetLoggingEnabled
 *   ssp_PnmCCDmGetLoggingLevel
 *   ssp_PnmCCDmSetLoggingLevel
 *   ssp_PnmCCDmGetMemMaxUsage
 *   ssp_PnmCCDmGetMemMinUsage
 *   ssp_PnmCCDmGetMemConsumed

 ---------------------------------------------------------------

environment:

Embedded Linux

---------------------------------------------------------------

author:

Sabarinath
Sugasini

---------------------------------------------------------------

revision:

10/05/2015  initial revision.

 **********************************************************************/

#include "ssp_global.h"
#include "ccsp_trace.h"
extern ULONG                                       g_ulAllocatedSizePeak;

extern  PDSLH_CPE_CONTROLLER_OBJECT     pDslhCpeController;
extern  PDSLH_DATAMODEL_AGENT_OBJECT    g_DslhDataModelAgent;
extern  PCOMPONENT_COMMON_DM            g_pComponent_Common_Dm;
extern  PCCSP_FC_CONTEXT                pPnmFcContext;
extern  PCCSP_CCD_INTERFACE             pPnmCcdIf;
extern  ANSC_HANDLE                     bus_handle;
extern char                             g_Subsystem[32];

static  COMPONENT_COMMON_DM             CommonDm = {0};

ANSC_STATUS
    ssp_create_pnm
(
 PCCSP_COMPONENT_CFG         pStartCfg
 )
{
    /* Create component common data model object */

    g_pComponent_Common_Dm = (PCOMPONENT_COMMON_DM)AnscAllocateMemory(sizeof(COMPONENT_COMMON_DM));

    if ( !g_pComponent_Common_Dm )
    {
        return ANSC_STATUS_RESOURCES;
    }

    ComponentCommonDmInit(g_pComponent_Common_Dm);

    g_pComponent_Common_Dm->Name     = AnscCloneString(pStartCfg->ComponentName);
    g_pComponent_Common_Dm->Version  = 1;
    g_pComponent_Common_Dm->Author   = AnscCloneString("CCSP");

    /* Create ComponentCommonDatamodel interface*/
    if ( !pPnmCcdIf )
    {
        pPnmCcdIf = (PCCSP_CCD_INTERFACE)AnscAllocateMemory(sizeof(CCSP_CCD_INTERFACE));

        if ( !pPnmCcdIf )
        {
            return ANSC_STATUS_RESOURCES;
        }
        else
        {
            AnscCopyString(pPnmCcdIf->Name, CCSP_CCD_INTERFACE_NAME);

            pPnmCcdIf->InterfaceId              = CCSP_CCD_INTERFACE_ID;
            pPnmCcdIf->hOwnerContext            = NULL;
            pPnmCcdIf->Size                     = sizeof(CCSP_CCD_INTERFACE);

            pPnmCcdIf->GetComponentName         = ssp_PnmCCDmGetComponentName;
            pPnmCcdIf->GetComponentVersion      = ssp_PnmCCDmGetComponentVersion;
            pPnmCcdIf->GetComponentAuthor       = ssp_PnmCCDmGetComponentAuthor;
            pPnmCcdIf->GetComponentHealth       = ssp_PnmCCDmGetComponentHealth;
            pPnmCcdIf->GetComponentState        = ssp_PnmCCDmGetComponentState;
            pPnmCcdIf->GetLoggingEnabled        = ssp_PnmCCDmGetLoggingEnabled;
            pPnmCcdIf->SetLoggingEnabled        = ssp_PnmCCDmSetLoggingEnabled;
            pPnmCcdIf->GetLoggingLevel          = ssp_PnmCCDmGetLoggingLevel;
            pPnmCcdIf->SetLoggingLevel          = ssp_PnmCCDmSetLoggingLevel;
            pPnmCcdIf->GetMemMaxUsage           = ssp_PnmCCDmGetMemMaxUsage;
            pPnmCcdIf->GetMemMinUsage           = ssp_PnmCCDmGetMemMinUsage;
            pPnmCcdIf->GetMemConsumed           = ssp_PnmCCDmGetMemConsumed;
            pPnmCcdIf->ApplyChanges             = ssp_PnmCCDmApplyChanges;
        }
    }

    /* Create context used by data model */
    pPnmFcContext = (PCCSP_FC_CONTEXT)AnscAllocateMemory(sizeof(CCSP_FC_CONTEXT));

    if ( !pPnmFcContext )
    {
        return ANSC_STATUS_RESOURCES;
    }
    else
    {
        AnscZeroMemory(pPnmFcContext, sizeof(CCSP_FC_CONTEXT));
    }

    pDslhCpeController = DslhCreateCpeController(NULL, NULL, NULL);

    if ( !pDslhCpeController )
    {
        CcspTraceWarning(("CANNOT Create pDslhCpeController... Exit!\n"));

        return ANSC_STATUS_RESOURCES;
    }

    return ANSC_STATUS_SUCCESS;
}


ANSC_STATUS
    ssp_engage_pnm
(
 PCCSP_COMPONENT_CFG         pStartCfg
 )
{
    ANSC_STATUS                     returnStatus    = ANSC_STATUS_SUCCESS;
    char                            CrName[256]     = {0};
    PCCSP_DM_XML_CFG_LIST           pXmlCfgList     = NULL;

    g_pComponent_Common_Dm->Health = CCSP_COMMON_COMPONENT_HEALTH_Yellow;


    if ( pPnmCcdIf )
    {
        pPnmFcContext->hCcspCcdIf = (ANSC_HANDLE)pPnmCcdIf;
        pPnmFcContext->hMessageBus = bus_handle;
    }

    g_DslhDataModelAgent->SetFcContext((ANSC_HANDLE)g_DslhDataModelAgent, (ANSC_HANDLE)pPnmFcContext);

    pDslhCpeController->AddInterface((ANSC_HANDLE)pDslhCpeController, (ANSC_HANDLE)MsgHelper_CreateCcdMbiIf((void*)bus_handle,g_Subsystem));
    pDslhCpeController->AddInterface((ANSC_HANDLE)pDslhCpeController, (ANSC_HANDLE)pPnmCcdIf);
    pDslhCpeController->SetDbusHandle((ANSC_HANDLE)pDslhCpeController, bus_handle);
    pDslhCpeController->Engage((ANSC_HANDLE)pDslhCpeController);

    if ( g_Subsystem[0] != 0 )
    {
        _ansc_sprintf(CrName, "%s%s", g_Subsystem, CCSP_DBUS_INTERFACE_CR);
    }
    else
    {
        _ansc_sprintf(CrName, "%s", CCSP_DBUS_INTERFACE_CR);
    }

    returnStatus = CcspComponentLoadDmXmlList(pStartCfg->DmXmlCfgFileName, &pXmlCfgList);

    if ( returnStatus != ANSC_STATUS_SUCCESS )
    {
        return  returnStatus;
    }

    returnStatus =
        pDslhCpeController->RegisterCcspDataModel
        (
         (ANSC_HANDLE)pDslhCpeController,
         CrName,                             /* CCSP CR ID */
         pXmlCfgList->FileList[0],           /* Data Model XML file. Can be empty if only base data model supported. */
         pStartCfg->ComponentName,           /* Component Name    */
         pStartCfg->Version,                 /* Component Version */
         pStartCfg->DbusPath,                /* Component Path    */
         g_Subsystem                         /* Component Prefix  */
        );

    if ( returnStatus == ANSC_STATUS_SUCCESS || returnStatus == CCSP_SUCCESS )
    {
        /* System is fully initialized */
        g_pComponent_Common_Dm->Health = CCSP_COMMON_COMPONENT_HEALTH_Green;
    }

    AnscFreeMemory(pXmlCfgList);

    return ANSC_STATUS_SUCCESS;
}


ANSC_STATUS
    ssp_cancel_pnm
(
 PCCSP_COMPONENT_CFG         pStartCfg
 )
{
    int                             nRet  = 0;
    char                            CrName[256];
    char                            CpName[256];

    if( pDslhCpeController == NULL)
    {
        return ANSC_STATUS_SUCCESS;
    }

    if ( g_Subsystem[0] != 0 )
    {
        _ansc_sprintf(CrName, "%s%s", g_Subsystem, CCSP_DBUS_INTERFACE_CR);
        _ansc_sprintf(CpName, "%s%s", g_Subsystem, pStartCfg->ComponentName);
    }
    else
    {
        _ansc_sprintf(CrName, "%s", CCSP_DBUS_INTERFACE_CR);
        _ansc_sprintf(CpName, "%s", pStartCfg->ComponentName);
    }
    /* unregister component */
    nRet = CcspBaseIf_unregisterComponent(bus_handle, CrName, CpName );
    AnscTrace("unregisterComponent returns %d\n", nRet);


    pDslhCpeController->Cancel((ANSC_HANDLE)pDslhCpeController);
    AnscFreeMemory(pDslhCpeController);
    pDslhCpeController = NULL;

    return ANSC_STATUS_SUCCESS;
}


char*
    ssp_PnmCCDmGetComponentName
(
 ANSC_HANDLE                     hThisObject
 )
{
    return g_pComponent_Common_Dm->Name;
}


ULONG
    ssp_PnmCCDmGetComponentVersion
(
 ANSC_HANDLE                     hThisObject
 )
{
    return g_pComponent_Common_Dm->Version;
}


char*
    ssp_PnmCCDmGetComponentAuthor
(
 ANSC_HANDLE                     hThisObject
 )
{
    return g_pComponent_Common_Dm->Author;
}


ULONG
    ssp_PnmCCDmGetComponentHealth
(
 ANSC_HANDLE                     hThisObject
 )
{
    return g_pComponent_Common_Dm->Health;
}


ULONG
    ssp_PnmCCDmGetComponentState
(
 ANSC_HANDLE                     hThisObject
 )
{
    return g_pComponent_Common_Dm->State;
}



BOOL
    ssp_PnmCCDmGetLoggingEnabled
(
 ANSC_HANDLE                     hThisObject
 )
{
    return g_pComponent_Common_Dm->LogEnable;
}


ANSC_STATUS
    ssp_PnmCCDmSetLoggingEnabled
(
 ANSC_HANDLE                     hThisObject,
 BOOL                            bEnabled
 )
{
    /*CommonDm.LogEnable = bEnabled;*/
    if(g_pComponent_Common_Dm->LogEnable == bEnabled) return ANSC_STATUS_SUCCESS;
    g_pComponent_Common_Dm->LogEnable = bEnabled;

    if (!bEnabled)
        AnscSetTraceLevel(CCSP_TRACE_INVALID_LEVEL);
    else
        AnscSetTraceLevel(g_pComponent_Common_Dm->LogLevel);

    return ANSC_STATUS_SUCCESS;
}


ULONG
    ssp_PnmCCDmGetLoggingLevel
(
 ANSC_HANDLE                     hThisObject
 )
{
    return g_pComponent_Common_Dm->LogLevel;
}


ANSC_STATUS
    ssp_PnmCCDmSetLoggingLevel
(
 ANSC_HANDLE                     hThisObject,
 ULONG                           LogLevel
 )
{
    /*CommonDm.LogLevel = LogLevel; */
    if(g_pComponent_Common_Dm->LogLevel == LogLevel) return ANSC_STATUS_SUCCESS;
    g_pComponent_Common_Dm->LogLevel = LogLevel;

    if (g_pComponent_Common_Dm->LogEnable)
        AnscSetTraceLevel(LogLevel);

    return ANSC_STATUS_SUCCESS;
}


ULONG
    ssp_PnmCCDmGetMemMaxUsage
(
 ANSC_HANDLE                     hThisObject
 )
{
    return g_ulAllocatedSizePeak;
}


ULONG
    ssp_PnmCCDmGetMemMinUsage
(
 ANSC_HANDLE                     hThisObject
 )
{
    return g_pComponent_Common_Dm->MemMinUsage;
}


ULONG
    ssp_PnmCCDmGetMemConsumed
(
 ANSC_HANDLE                     hThisObject
 )
{
    LONG             size = 0;

    size = AnscGetComponentMemorySize(gpPnmStartCfg->ComponentName);
    if (size == -1 )
        size = 0;

    return size;
}


ANSC_STATUS
    ssp_PnmCCDmApplyChanges
(
 ANSC_HANDLE                     hThisObject
 )
{
    ANSC_STATUS                         returnStatus    = ANSC_STATUS_SUCCESS;

    return returnStatus;
}

