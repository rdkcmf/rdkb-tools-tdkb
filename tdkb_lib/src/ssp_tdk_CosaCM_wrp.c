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

#ifndef __SSP_COSACM_WRP_C__
#define __SSP_COSACM_WRP_C__

#include "ssp_global.h"
#include "ccsp_dm_api.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pthread.h"
#include "ssp_tdk_wrp.h"
#include "ssp_tdk_CosaCM_wrp.h"
#include <pthread.h>
#include <ccsp_message_bus.h>
#include <ccsp_base_api.h>
#include <sys/time.h>
#include <time.h>
#include <signal.h>
#include "ccsp_memory.h"
#include <ccsp_custom.h>
#include <dslh_definitions_database.h>
#include <sys/ucontext.h>
#include "cosa_x_cisco_com_cablemodem_apis.h"
#include <unistd.h>
#include "cm_hal.h"

ANSC_HANDLE cm_handle = NULL;
PCOSA_BACKEND_MANAGER_OBJECT g_pCosaBEManager;

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlCMGetResetCount
 * Description          : This function will invoke the cosa api of CM to retrieve the reset count
 *                        value for the specified reset type.
 *
 * @param [in]          : handleType - message bus handle
 * @param [in]          : bufferType - Valid or NULL pointer
 * @param [in]          : pResetType - reset type can be CM, Docsis, Erouter or local
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlCMGetResetCount(int handleType, int bufferType, char *pResetType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    CM_RESET_TYPE resetType = 0;
    ULONG resetCount = 0;

    printf("\n Entering ssp_CosaDmlCMGetResetCount function\n\n");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }

    if((strcmp(pResetType,"CMResetCount")==0))
    {
        resetType = CABLE_MODEM_RESET;
    }
    else if((strcmp(pResetType,"LocalResetCount")==0))
    {
        resetType = LOCAL_RESET;
    }
    else if((strcmp(pResetType,"DocsisResetCount")==0))
    {
        resetType = DOCSIS_RESET;
    }
    else if((strcmp(pResetType,"ErouterResetCount")==0))
    {
        resetType = EROUTER_RESET;
    }

    printf("ssp_CosaDmlCMGetResetCount: Reset Type:%d\n",resetType);

    if(bufferType == 0)
    {
        return_status = CosaDmlCMGetResetCount(cm_handle,resetType,&resetCount);
    }
    else
    {
        return_status = CosaDmlCMGetResetCount(cm_handle,resetType,NULL);
    }

    printf("ssp_CosaDmlCMGetResetCount: ResetCount retrieved:%d\n",resetCount);

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlCMGetResetCount:Failed to retrieve the reset count\n");
        return SSP_FAILURE;
    }
    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlCMGetLockedUpstreamChID
 * Description          : This function will invoke the cosa api of CM to retrieve the currently
 *                        locked upstream channel Id
 *
 * @param [in]          : handleType - Message Bus handle
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlCMGetLockedUpstreamChID(int handleType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    ULONG *pChannelId  = NULL;

    printf("\n Entering ssp_CosaDmlCMGetLockedUpstreamChID function\n\n");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }

    return_status = CosaDmlCMGetLockedUpstreamChID(NULL,pChannelId);

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlCMGetLockedUpstreamChID: Failed to retrieve the upstream channel Id\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlCMSetLockedUpstreamChID
 * Description          : This function will invoke the cosa api of CM to lock upstream channel
 *                        Id for the specified value.
 *
 * @param [in]          : handleType - Message bus handle
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlCMSetLockedUpstreamChID(int handleType, int channelId)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    ULONG channelValue = (ULONG)channelId;

    printf("\n Entering ssp_CosaDmlCMSetLockedUpstreamChID function\n\n");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }

    printf("ssp_CosaDmlCMSetLockedUpstreamChID: Upstream Channel Id to be set:%d\n",channelValue);
    return_status = CosaDmlCMSetLockedUpstreamChID(cm_handle,&channelValue);

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlCMSetLockedUpstreamChID:Failed to lock the upstream channel Id\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlCMGetStartDSFrequency
 * Description          : This function will invoke the cosa api of CM to retrieve the Downstream
 *                        frequency
 *
 * @param [in]          : handleType - Message bus handle
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlCMGetStartDSFrequency(int handleType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    ULONG *pFrequency  = NULL;

    printf("\n Entering ssp_CosaDmlCMGetStartDSFrequency function\n\n");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }

    return_status = CosaDmlCMGetStartDSFrequency(cm_handle,&pFrequency);

    printf("ssp_CosaDmlCMGetStartDSFrequency: Downstream Frequency retrieved:%d\n",pFrequency);

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlCMGetStartDSFrequency:Failed to retrieve the downstream channel\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlCMSetStartDSFrequency
 * Description          : This function will invoke the cosa api of CM to set the downstream
 *                        frequency
 * @param [in]          : handleType - Message Bus handle
 * @param [in]          : frequency - Downstream frequency to be set
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlCMSetStartDSFrequency(int handleType, int frequency)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    ULONG frequencyValue = (ULONG)frequency;

    printf("\n Entering ssp_CosaDmlCMSetStartDSFrequency function\n\n");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }

    printf("ssp_CosaDmlCMSetStartDSFrequency: Downstream frequency to be set:%d\n",(int)frequencyValue);
    return_status = CosaDmlCMSetStartDSFrequency(cm_handle,frequencyValue);

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlCMSetStartDSFrequency:Failed to set the downstream frequency\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlCMGetProvType
 * Description          : This function will invoke the cosa api of CM to get the cable modem
 *                        provisioning type.
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlCMGetProvType(int handleType, int bufferType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    char *provType = NULL;

    printf("\n Entering ssp_CosaDmlCMGetProvType function\n\n");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }

    if(bufferType == 0)
    {
        provType = ((char *) malloc(20));
        return_status = CosaDmlCMGetProvType(cm_handle,provType);
        printf("ssp_CosaDmlCMGetProvType: Provisioning type retrieved:%s\n",provType);
    }
    else
    {
        return_status = CosaDmlCMGetProvType(cm_handle,NULL);
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlCMGetProvType:Failed to retrieve the provisioning type of cable modem\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlCMGetIPv6DHCPInfo
 * Description          : This function will invoke the cosa api of CM to retrieve the DHCP
 *                        information of IPv6
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlCMGetIPv6DHCPInfo(int handleType, int bufferType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    COSA_CM_IPV6DHCP_INFO dhcpIpv6 = {0};

    printf("\n Entering ssp_CosaDmlCMGetIPv6DHCPInfo function\n\n");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }

    if(bufferType == 0)
    {
       return_status = CosaDmlCMGetIPv6DHCPInfo(cm_handle,&dhcpIpv6);
       printf("DHCPv6 Details:\n");
       printf("IPV6 Address:%s\n",dhcpIpv6.IPv6Address);
    }
    else
    {
       return_status = CosaDmlCMGetIPv6DHCPInfo(cm_handle,NULL);
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlCMGetIPv6DHCPInfo:Failed to retrieve the DHCP information of IPv6 \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlCMGetStatus
 * Description          : This function will get CM Status.
 * @param [in]          : Value - Get CM Status value
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlCMGetStatus(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    char *pValue = NULL;

    printf("Entering ssp_CosaDmlCMGetStatus");
    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }
    if(Value == 0)
    {
        pValue = ((char *) malloc(100));
    }
    return_status = CosaDmlCMGetStatus(cm_handle,pValue);
    printf("Return status of CosaDmlCMGetStatus is %d \n", return_status);
    if(return_status == SSP_SUCCESS)
    {
        printf("\n ssp_CosaDmlCMGetStatus :: CosaDmlCMGetStatus function is success with return status %d",return_status);
        return_status = SSP_SUCCESS;
    }
    else
    {
        printf("\n ssp_CosaDmlCMGetStatus :: CosaDmlCMGetStatus function is failure and return status %d",return_status);
        return_status = SSP_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaCMGetLoopDiagnosticsStart
 * Description          : This function will get Loop Diagnostics start details
 * @param [in]          : Value -
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaCMGetLoopDiagnosticsStart(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    bool bValue = 0;
    printf("Entering ssp_CosaCMGetLoopDiagnosticsStart");
    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }
    if(Value == 0)
    {
        return_status = CosaDmlCMGetLoopDiagnosticsStart(cm_handle,&bValue);
        printf("Loop Diagnostic Start:%d\n",bValue);
    }
    else
    {
	return_status = CosaDmlCMGetLoopDiagnosticsStart(cm_handle,NULL);
    }

    if(return_status == SSP_SUCCESS)
    {
        printf("\n ssp_CosaCMGetLoopDiagnosticsStart :: CosaCMGetLoopDiagnosticsStart function is success with return status %d",return_status);
        return_status = SSP_SUCCESS;
    }
    else
    {
        printf("\n ssp_CosaCMGetLoopDiagnosticsStart :: CosaCMGetLoopDiagnosticsStart function is failure and return status %d",return_status);
        return_status = SSP_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlCMGetLoopDiagnosticsDetails
 * Description          : This function will get Loop Diagnostics details
 * @param [in]          : boolValue -
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlCMGetLoopDiagnosticsDetails(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    char pValue[20] = {0};
    printf("Entering ssp_CosaDmlCMGetLoopDiagnosticsDetails");
    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }
    if(Value == 0)
    {
        return_status = CosaDmlCMGetLoopDiagnosticsDetails(cm_handle,pValue);
        printf("Loop Diagnostic Details:%s\n",pValue);
    }
    else
    {
	return_status = CosaDmlCMGetLoopDiagnosticsDetails(cm_handle,NULL);
    }

    if(return_status == SSP_SUCCESS)
    {
        printf("\n ssp_CosaDmlCMGetLoopDiagnosticsDetails :: CosaDmlCMGetLoopDiagnosticsDetails function is success with return status %d",return_status);
        return_status = SSP_SUCCESS;
    }
    else
    {
        printf("\n ssp_CosaDmlCMGetLoopDiagnosticsDetails:: CosaDmlCMGetLoopDiagnosticsDetails function is failure and return status %d",return_status);
        return_status = SSP_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_CosaDmlCMGetTelephonyRegistrationStatus
 * Description          : This function will get the telephony registration status
 * @param [in]          : boolValue -
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlCMGetTelephonyRegistrationStatus(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    char pValue[30] = {0};

    printf("Entering ssp_CosaDmlCMGetTelephonyRegistrationStatus");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }
    if(Value == 0)
    {
    	return_status = CosaDmlCMGetTelephonyRegistrationStatus(cm_handle,pValue);
        printf("Telephony Registration Status:%s\n",pValue);
    }
    else
    {
    	return_status = CosaDmlCMGetTelephonyRegistrationStatus(cm_handle,NULL);
    }

    if(return_status == SSP_SUCCESS)
    {
        printf("\n ssp_CosaDmlCMGetTelephonyRegistrationStatus :: CosaDmlCMGetTelephonyRegistrationStatus function is success with return status %d",return_status);
        return_status = SSP_SUCCESS;
    }
    else
    {
        printf("\n ssp_CosaDmlCMGetTelephonyRegistrationStatus :: CosaDmlCMGetTelephonyRegistrationStatus function is failure and return status %d",return_status);
        return_status = SSP_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_CosaDmlCMGetTelephonyDHCPStatus
 * Description          : This function will get
 * @param [in]          : boolValue -
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlCMGetTelephonyDHCPStatus(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    char pValue[30] = {0};

    printf("Entering ssp_CosaDmlCMGetTelephonyDHCPStatus");
    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }
    if(Value == 0)
    {
  	return_status = CosaDmlCMGetTelephonyDHCPStatus(cm_handle,pValue);
        printf("Telephony DHCP Status:%s\n",pValue);
    }
    else
    {
	return_status = CosaDmlCMGetTelephonyDHCPStatus(cm_handle,NULL);
    }

    if(return_status == SSP_SUCCESS)
    {
        printf("\n ssp_CosaDmlCMGetTelephonyDHCPStatus :: CosaDmlCMGetTelephonyDHCPStatus function is success with return status %d",return_status);
        return_status = SSP_SUCCESS;
    }
    else
    {
        printf("\n ssp_CosaDmlCMGetTelephonyDHCPStatus :: CosaDmlCMGetTelephonyDHCPStatus function is failure and return status %d",return_status);
        return_status = SSP_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_CosaDmlCMGetTelephonyTftpStatus
 * Description          : This function will get
 * @param [in]          : boolValue -
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlCMGetTelephonyTftpStatus(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    char pValue[30] = {0};

    printf("Entering ssp_CosaDmlCMGetTelephonyTftpStatus");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }
    if(Value == 0)
    {
  	return_status = CosaDmlCMGetTelephonyTftpStatus(cm_handle,pValue);
    }
    else
    {
    	return_status = CosaDmlCMGetTelephonyTftpStatus(cm_handle,NULL);
    }

    if(return_status == SSP_SUCCESS)
    {
        printf("\n ssp_CosaDmlCMGetTelephonyTftpStatus :: CosaDmlCMGetTelephonyTftpStatus function is success with return status %d",return_status);
        return_status = SSP_SUCCESS;
    }
    else
    {
        printf("\n ssp_CosaDmlCMGetTelephonyTftpStatus :: CosaDmlCMGetTelephonyTftpStatus function is failure and return status %d",return_status);
        return_status = SSP_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_CosaDmlCMSetLoopDiagnosticsStart
 * Description          : This function will set Loop Diagnostics Start
 * @param [in]          : boolValue -
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlCMSetLoopDiagnosticsStart(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;

    printf("Entering ssp_CosaDmlCMSetLoopDiagnosticsStart");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }

    return_status = CosaDmlCMSetLoopDiagnosticsStart(cm_handle,Value);
    if(return_status == SSP_SUCCESS)
    {
        printf("\n ssp_CosaDmlCMSetLoopDiagnosticsStart :: CosaDmlCMSetLoopDiagnosticsStart function is success with return status %d",return_status);
        return_status = SSP_SUCCESS;
    }
    else
    {
        printf("\n ssp_CosaDmlCMSetLoopDiagnosticsStart :: CosaDmlCMSetLoopDiagnosticsStart function is failure and return status %d",return_status);
        return_status = SSP_FAILURE;
    }
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_GetDHCPInfo
 * Description          : This function will invoke the cosa api of CM to retrieve the DHCP
 *                        information
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_GetDHCPInfo(int handleType, int bufferType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    COSA_CM_DHCP_INFO dhcp = {0};

    printf("\n Entering ssp_cosacm_GetDHCPInfo function\n\n");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }

    if(bufferType == 0)
    {
        return_status = CosaDmlCMGetDHCPInfo(cm_handle, &dhcp);
        printf("DHCP Info Details:\n");
        printf("MAC Address:%s\n",dhcp.MACAddress);
    }
    else
    {
        return_status = CosaDmlCMGetDHCPInfo(cm_handle, NULL);
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_cosacm_GetDHCPInfo:Failed to retrieve the DHCP information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_GetDOCSISInfo
 * Description          : This function will invoke the cosa api of CM to retrieve the DOCSIS
 *                        information
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_GetDOCSISInfo(int handleType, int bufferType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    COSA_CM_DOCSIS_INFO docsis = {0};

    printf("\n Entering ssp_cosacm_GetDOCSISInfo function\n\n");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }

    if(bufferType == 0)
    {
        return_status = CosaDmlCMGetDOCSISInfo(cm_handle,&docsis);
        printf("DOCSIS Info Max CPE Allowed:%d\n",docsis.MaxCpeAllowed);
    }
    else
    {
        return_status = CosaDmlCMGetDOCSISInfo(cm_handle,NULL);

    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_cosacm_GetDOCSISInfo:Failed to retrieve the DOCSIS information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_GetLog
 * Description          : This function will invoke the cosa api of CM to retrieve the Log
 *                        information
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_GetLog(int handleType, int bufferType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    COSA_DML_CM_LOG log = {0};

    printf("\n Entering ssp_cosacm_GetLog function\n\n");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }
    if(bufferType == 0)
    {
        return_status = CosaDmlCmGetLog(cm_handle,&log);
        printf("Log Info:\n");
        printf("Enable Log:%d\n",log.EnableLog);
    }
    else
    {
        return_status = CosaDmlCmGetLog(cm_handle,NULL);
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_cosacm_GetLog:Failed to retrieve the Log information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_SetLog
 * Description          : This function will invoke the cosa api of CM to set the log information
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_SetLog(int handleType, int bufferType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    COSA_DML_CM_LOG log = {0};

    printf("\n Entering ssp_cosacm_SetLog function\n\n");

    if(handleType == 0)
    {
        cm_handle = bus_handle_client;
    }
    if(bufferType == 0)
    {
         log.EnableLog = 1;
         log.CleanDocsisLog = 1;
         return_status = CosaDmlCmSetLog(cm_handle,&log);
    }
    else
    {
	 return_status = CosaDmlCmSetLog(cm_handle,NULL);
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_cosacm_SetLog:Failed to set the log information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_GetDocsisLog
 * Description          : This function will invoke the cosa api of CM to set the DOCSIS log information
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_cosacm_GetDocsisLog(int handleType, int bufferType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    ULONG count = 0;
    COSA_DML_DOCSISLOG_FULL *ppConf = NULL;

    printf("\n Entering ssp_cosacm_GetDocsisLog function\n\n");

    if(handleType == 0)
    {
	cm_handle = bus_handle_client;
    }
    if(bufferType == 0)
    {
        count=(COSA_DML_DOCSISLOG_FULL*)malloc(sizeof(COSA_DML_DOCSISLOG_FULL));
        return_status = CosaDmlCmGetDocsisLog(cm_handle,&count,&ppConf);
        printf("ssp_cosacm_GetDocsisLog: DOCSIS Log Info:%s\n",ppConf->Description);
    }
    else
    {
        return_status = CosaDmlCmGetDocsisLog(cm_handle,NULL,NULL);
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_cosacm_GetDocsisLog:Failed to retrieve the DOCSIS Log information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_GetDownstreamChannel
 * Description          : This function will invoke the cosa api of CM to set the Downstream channel information
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_GetDownstreamChannel(int handleType, int bufferType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    ULONG Count = 0;
    COSA_CM_DS_CHANNEL *pcfg = NULL;

    printf("\n Entering ssp_cosacm_GetDownstreamChannel function\n\n");

    if(handleType == 0)
    {
	cm_handle = bus_handle_client;
    }
    if(bufferType == 0)
    {
        pcfg = (COSA_CM_DS_CHANNEL*)malloc(sizeof(COSA_CM_DS_CHANNEL));
        return_status = CosaDmlCmGetDownstreamChannel(cm_handle,&Count,&pcfg);
        printf("ssp_cosacm_GetDownstreamChannel: Downstream channel Info:%s\n",pcfg->Frequency);
    }
    else
    {
        return_status = CosaDmlCmGetDownstreamChannel(cm_handle,NULL,NULL);
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_cosacm_GetDownstreamChannel:Failed to retrieve the Downstream channel information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_GetUpstreamChannel
 * Description          : This function will invoke the cosa api of CM to set the Upstream channel information
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_GetUpstreamChannel(int handleType, int bufferType)
{
    int return_status = 0;
    ANSC_HANDLE cm_handle = NULL;
    ULONG Count = 0;
    COSA_CM_US_CHANNEL *pcfg = NULL;

    printf("\n Entering ssp_cosacm_GetUpstreamChannel function\n\n");

    if(handleType == 0)
    {
	cm_handle = bus_handle_client;
    }
    if(bufferType == 0)
    {
        pcfg = (COSA_CM_US_CHANNEL*)malloc(sizeof(COSA_CM_US_CHANNEL));
        return_status = CosaDmlCmGetUpstreamChannel(cm_handle,&Count,&pcfg);
        printf("ssp_cosacm_GetUpstreamChannel: Upstream channel Info:%s\n",pcfg->Frequency);
    }
    else
    {
        return_status = CosaDmlCmGetUpstreamChannel(cm_handle,NULL,NULL);
    }

    if ( return_status != SSP_SUCCESS)
    {
        free(Count);
        printf("ssp_cosacm_GetUpstreamChannel:Failed to retrieve the Upstream channel information \n");
        return SSP_FAILURE;
    }


    return SSP_SUCCESS;
}

/*******************************************************************************************
 * Function Name        : ssp_CosaCableModemCreate
 * Description          : This function will create cabel Modem.
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaCableModemCreate()
{
    int return_status = 0;

    printf("Entering ssp_CosaCableModemCreate\n");

    printf("Create handle for the cable modem\n");
    g_pCosaBEManager = (PCOSA_BACKEND_MANAGER_OBJECT)CosaBackEndManagerCreate();
    if(g_pCosaBEManager !=NULL)
    {
        printf("\n ssp_CosaCableModemCreate :: CosaCableModemCreate function is success with return status %d\n",return_status);
        return_status = SSP_SUCCESS;
    }
    else
    {
        printf("\n ssp_CosaCableModemCreate :: CosaCableModemCreate function is failure and return status %d\n",return_status);
        return_status = SSP_FAILURE;
    }

    printf("Exiting ssp_CosaCableModemCreate\n");
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_CosaCableModemInitialize
 * Description          : This function will initialize Cable Modem
 * @param [in]          : Value - pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaCableModemInitialize(int Value)
{
    int return_status = 0;

    printf("Entering ssp_CosaCableModemInitialize\n");

    if(Value == 0)
    {
	printf("Create handle for the cable modem\n");
        g_pCosaBEManager = (PCOSA_BACKEND_MANAGER_OBJECT)CosaBackEndManagerCreate();
        if ( g_pCosaBEManager != NULL )
        {
             printf("Negative Scenario: Initialize the Cable Modem with NULL handle\n");
             return_status = CosaBackEndManagerInitialize(NULL);
        }
        else
        {
		printf("g_pCosaBEManager handle created for cable modem is NULL\n");
                return_status = SSP_FAILURE;
        }

        if(return_status == SSP_SUCCESS)
        {
            printf("\n ssp_CosaCableModemInitialize :: CosaCableModemInitialize function fails to handle NULL scenarios %d\n",return_status);
            return 1;
        }
        else
        {
            printf("\n ssp_CosaCableModemInitialize :: CosaCableModemInitialize function handles NULL scenarios and return status %d\n",return_status);
            return 0;
        }

    }
    else if (Value == 1)
    {
        printf("Create handle for the cable modem\n");
        g_pCosaBEManager = (PCOSA_BACKEND_MANAGER_OBJECT)CosaBackEndManagerCreate();
        if ( g_pCosaBEManager != NULL )
        {
             printf("Initialize the cable modem\n");
             return_status = CosaBackEndManagerInitialize((ANSC_HANDLE)g_pCosaBEManager);
        }
        else
        {
		printf("g_pCosaBEManager handle created for cable modem is NULL\n");
      		return_status = SSP_FAILURE;
        }

        if(return_status == SSP_SUCCESS)
        {
            printf("\n ssp_CosaCableModemInitialize :: CosaCableModemInitialize function is success with return status %d\n",return_status);
            return 0;
        }
        else
        {
            printf("\n ssp_CosaCableModemInitialize :: CosaCableModemInitialize function is failure and return status %d\n",return_status);
            return 1;
        }
    }
    else
    {
        printf("\nNo Handle type is passed\n");
        return return_status;
    }
}
/*******************************************************************************************
 * Function Name        : ssp_CosaCableModemRemove
 * Description          : This function will Remove Cable modem
 * @param [in]          : pObject - pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaCableModemRemove(int Value)
{
    int return_status = 0;

    printf("Entering ssp_CosaCableModemRemove\n");

    if(Value == 0)
    {
	printf("Create handle for the cable modem\n");
        g_pCosaBEManager = (PCOSA_BACKEND_MANAGER_OBJECT)CosaBackEndManagerCreate();
        if ( g_pCosaBEManager != NULL )
        {
	     printf("Initialize the cable modem\n");
             return_status = CosaBackEndManagerInitialize((ANSC_HANDLE)g_pCosaBEManager);
    	     printf("Negative Scenario: Free the cable modem resources created using NULL handle\n");
             return_status = CosaBackEndManagerRemove(NULL);
        }
        else
        {
		printf("g_pCosaBEManager handle created for cable modem is NULL\n");
                return_status = SSP_FAILURE;
        }

        if(return_status == SSP_SUCCESS)
        {
            printf("\n ssp_CosaCableModemRemove :: CosaCableModemRemove function does not handle NULL sceanrios with return status %d\n",return_status);
            return 1;
        }
        else
        {
            printf("\n ssp_CosaCableModemRemove :: CosaCableModemRemove function handles failure scenarios and return status %d\n",return_status);
            return 0;
        }

    }
    else if (Value == 1)
    {
	printf("Create handle for the cable modem\n");
	g_pCosaBEManager = (PCOSA_BACKEND_MANAGER_OBJECT)CosaBackEndManagerCreate();
        if ( g_pCosaBEManager != NULL )
        {
	     printf("Initialize the cable modem\n");
             return_status = CosaBackEndManagerInitialize((ANSC_HANDLE)g_pCosaBEManager);
	     sleep(20);
 	     printf("Free the cable modem resources created\n");
	     return_status = CosaBackEndManagerRemove((ANSC_HANDLE)g_pCosaBEManager);
        }
        else
        {
		printf("g_pCosaBEManager handle created for cable modem is NULL\n");
		return_status = SSP_FAILURE;
        }

        if(return_status == SSP_SUCCESS)
        {
            printf("\n ssp_CosaCableModemRemove :: CosaCableModemRemove function is success with return status %d\n",return_status);
            g_pCosaBEManager = NULL;
            return 0;
        }
        else
        {
            printf("\n ssp_CosaCableModemRemove :: CosaCableModemRemove function is failure and return status %d\n",return_status);
            g_pCosaBEManager = NULL;
            return 1;
        }
    }
    else
    {
        printf("\nNo value paseed\n");
        return return_status;
    }
}
/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getmarket
 * Description          : This function will invoke the cosa api of CM to get Market in which
 *                        this particular DUT can be used
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getmarket()
{
    int return_status = 0;
    char *value = NULL;

    printf("\n Entering ssp_cosacm_getmarket function\n\n");

    value = ((char *) malloc(20));

    if(value == NULL)
    {
        printf("\n ssp_cosacm_getmarket :: Get Value Memory alloc error \n");
        return SSP_FAILURE;
    }
    return_status = CosaDmlCMGetMarket(bus_handle_client,value);
    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_getmarket:Failed to get the DUT Market Info \n");
        return SSP_FAILURE;
    }
    if(value != NULL)
    {
        free(value);
    }
    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_setmddipoverride
 * Description          : This function will invoke the cosa api of CM to set MDD IP Override
 *                        Function
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_setmddipoverride(char *value)
{
    int return_status = 0;

    printf("\n Entering ssp_cosacm_setmddipoverride function\n\n");

    return_status = CosaDmlCMSetMDDIPOverride(bus_handle_client,value);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_setmddipoverride :Failed to set the MDDIPOverride \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getmddipoverride
 * Description          : This function will invoke the cosa api of CM to get MDD IP Override
 *                        Function current Configuration
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getmddipoverride(char *value)
{

    int return_status = 0;

    printf("\n Entering ssp_cosacm_getmddipoverride function\n\n");

    return_status = CosaDmlCMGetMDDIPOverride(bus_handle_client,value);

    printf("MDD value retrieved is :%s\n",value);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_getmddipoverride:Failed to get the MDDIPOverride \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;


}
/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getcert
 * Description          : This function will invoke the cosa api of CM to get certificate
 *                        access information
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getcert()
{

    int return_status = 0;
    char *value = NULL;
    int*     pBool;

    printf("\n Entering ssp_cosacm_getcert function\n\n");

    value = ((char *) malloc(20));

    if(value == NULL)
    {
        printf("\n ssp_cosacm_getcert :: Get Value Memory alloc error \n");
        return SSP_FAILURE;
    }

    return_status = CosaDmlCmGetCMCert(bus_handle_client,value);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_getcert:Failed\n");
        return SSP_FAILURE;
    }

    if(value != NULL)
    {
        free(value);
    }

    return SSP_SUCCESS;

}


/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getcmerrorcodewords
 * Description          : This function will invoke the cosa api of CM to get Error Code
 *                        Words Information. It contains channel coding related information
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getcmerrorcodewords()
{
    int return_status = 0;
    ULONG count = 0;
    PCOSA_DML_CMERRORCODEWORDS_FULL **pCfg  = NULL;

    printf("\n Entering ssp_cosacm_getcmerrorcodewords function\n\n");

    return_status = CosaDmlCmGetCMErrorCodewords(bus_handle_client,&count,&pCfg);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_getcmerrorcodewords:Failed to retrieve the error code words\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getcertstatus
 * Description          : This function will invoke the cosa api of CM to certificate availability
 *                        status
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getcertstatus()
{

    int return_status = 0;
    bool bValue;

    printf("\n Entering ssp_cosacm_getcertstatus function\n\n");

    return_status = CosaDmlCmGetCMCertStatus(bus_handle_client,&bValue);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_getcertstatus:Failed to get the Certificate Status info \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;

}

/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getcpelist
 * Description          : This function will invoke the cosa api of CM to Wireless/Wired Clients
 *                        connected with this DUT
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getcpelist()
{
    int return_status = 0;
    ULONG ulInstanceNumber=0;
    ANSC_HANDLE cm_handle = NULL;
    COSA_DML_CPE_LIST pCPEList = {0};

    printf("\nEntering ssp_cosacm_getcpelist function\n\n");

    return_status = CosaDmlCmGetCPEList(cm_handle,&ulInstanceNumber,&pCPEList);
    printf("Return status of CosaDmlCmGetCPEList is %d \n", return_status);

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_cosacm_getcpelist :Failed to get the CPE List Info \n");
        return SSP_FAILURE;
    }

    printf("\nCosaDmlCmGetCPEList return instance number as %l with info \n",ulInstanceNumber);

    return SSP_SUCCESS;

}

/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getmarket_memory_unalloc
 * Description          : This function will invoke the cosa api of CM to get Market in which
 *                        this particular DUT can be used
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getmarket_memory_unalloc()
{
    int return_status = 0;

    printf("\n Entering ssp_cosacm_getmarket_memory_unalloc function\n\n");

    return_status = CosaDmlCMGetMarket(bus_handle_client,NULL);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_getmarket_memory_unalloc:Failed to get the DUT Market Info \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;

}

/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_setmddipoverride_memory_unalloc
 * Description          : This function will invoke the cosa api of CM to set MDD IP Override
 *                        Function
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_setmddipoverride_memory_unalloc()
{
    int return_status = 0;

    printf("\n Entering ssp_cosacm_setmddipoverride function\n\n");

    return_status = CosaDmlCMSetMDDIPOverride(bus_handle_client,NULL);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_setmddipoverride_memory_unalloc :Failed to set the MDDIPOverride \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getmddipoverride_memory_unalloc
 * Description          : This function will invoke the cosa api of CM to get MDD IP Override
 *                        Function current Configuration
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getmddipoverride_memory_unalloc()
{

    int return_status = 0;

    printf("\n Entering ssp_cosacm_getmddipoverride_memory_unalloc function\n\n");

    return_status = CosaDmlCMGetMDDIPOverride(bus_handle_client,NULL);

    printf("Return status of CosaDmlCMGetMDDIPOverride %d ",return_status);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_get_mddipoverride_memory_unalloc:Failed to get the MDDIPOverride \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getcert_memory_unalloc
 * Description          : This function will invoke the cosa api of CM to get certificate
 *                        access information
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getcert_memory_unalloc()
{

    int return_status = 0;
    char *value = NULL;

    printf("\n Entering ssp_cosacm_getcert_memory_unalloc function\n\n");

    return_status = CosaDmlCmGetCMCert(bus_handle_client,value);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_getcert_memory_unalloc:Failed to get the MDDIPOverride \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;

}


/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getcmerrorcodewords_invalid_arg
 * Description          : This function will invoke the cosa api of CM to get Error Code
 *                        Words Information. It contains channel coding related information
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getcmerrorcodewords_invalid_arg()
{
    int return_status = 0;

    printf("\n Entering ssp_cosacm_getcmerrorcodewords_invalid_arg function\n\n");

    return_status = CosaDmlCmGetCMErrorCodewords(bus_handle_client,NULL,NULL);

    printf("Return status of CosaDmlCmGetCMErrorCodewords %d ",return_status);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_getcmerrorcodewords_invalid_arg:Failed to retrieve the error code words\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getcertstatus_invalid_arg
 * Description          : This function will invoke the cosa api of CM to certificate availability
 *                        status
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getcertstatus_invalid_arg()
{

    int return_status = 0;
    bool *bValue=NULL;

    printf("\n Entering ssp_cosacm_getcertstatus_invalid_arg function\n\n");

    return_status = CosaDmlCmGetCMCertStatus(bus_handle_client,bValue);

    printf("Return status of CosaDmlCmGetCMCertStatus %d ", return_status);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\n ssp_cosacm_getcertstatus_invalid_arg:Failed to get the Certificate Status info \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;

}

/*******************************************************************************************
 *
 * Function Name        : ssp_cosacm_getcpelist_invalid_arg
 * Description          : This function will invoke the cosa api of CM to Wireless/Wired Clients
 *                        connected with this DUT
 *
 * @param [in]          : N/A
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_cosacm_getcpelist_invalid_arg()
{

    int return_status = 0;

    printf("\nEntering ssp_cosacm_getcpelist_invalid_arg function\n\n");

    return_status = CosaDmlCmGetCPEList(bus_handle_client,NULL,NULL);

    printf("Return status of CosaDmlCmGetCPEList %d", return_status);

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_cosacm_getcpelist_invalid_arg :Failed to get the CPE List Info \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;

}

#endif
