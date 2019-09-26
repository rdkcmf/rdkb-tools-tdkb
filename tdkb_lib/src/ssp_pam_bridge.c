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


#ifndef __SSP_PAM_BRIDGE_C__
#define __SSP_PAM_BRIDGE_C__

#include "ssp_global.h"
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

#include "cosa_apis.h"
#include "cosa_dml_api_common.h"
#include "cosa_dhcpv4_apis.h"
#include "cosa_dml_api_dns.h"
#include "cosa_bridging_dml.h"
#include "cosa_x_cisco_com_multilan_apis.h"
#include "cosa_ethernet_apis_multilan.h"

#define SSP_SUCCESS       0

#define SSP_FAILURE       1

#define BUFFER_SIZE       1023

/*******************************************************************************************
 *
 * Function Name        : ssp_pam_Bridging_GetParamUlongValue
 * Description          : This function will retrieve the values of ulong params
 *
 * @param [in]          : paramName - parameter name whose values to be retrieved
 * @param [out]         : ulongValue - Holds the value of the parameter
 * @param [out]         : module - Holds the module function to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_pam_Bridging_GetParamUlongValue(char* paramName, unsigned long* ulongValue, char *module)
{
    int return_status = 0;
    unsigned long value = 0;
    printf("\n Entering ssp_pam_Bridging_GetParamUlongValue function\n\n");

    if(strcmp(module,"Bridging") == 0)
    {
    	return_status = Bridging_GetParamUlongValue(bus_handle_client,paramName,&value);
    }
    else if(strcmp(module,"Bridge") == 0)
    {
	return_status = Bridge_GetParamUlongValue(bus_handle_client,paramName,&value);
    }
    else if(strcmp(module,"Port") == 0)
    {
	return_status = Port_GetParamUlongValue(bus_handle_client,paramName,&value);
    }
    else if(strcmp(module,"PortStats") == 0)
    {
        return_status = PortStats_GetParamUlongValue(bus_handle_client,paramName,&value);
    }
    else if(strcmp(module,"Filter") == 0)
    {
        return_status = Filter_GetParamUlongValue(bus_handle_client,paramName,&value);
    }
    else
    {
	printf("Invalid module type received\n");
	return 1;
    }

    if ( return_status == 0)
    {
        printf("ssp_pam_Bridging_GetParamUlongValue:Failed to retrieve the ulongValue\n");
        return 1;
    }

    *ulongValue = value;
    printf("ssp_pam_Bridging_GetParamUlongValue: ulongValue:%lu\n",*ulongValue);
    return 0;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAAgentRestart
 * Description          : This function will kill the CMAgent process which is running by default
 *                        and check if the process has restarted after kill.
 *
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAAgentRestart()
{
    printf("\n Entering ssp_MTAAgentRestart function\n\n");

    if(0 == system("pidof CcspMtaAgentSsp > /dev/null"))  {
        printf("\nMTAAgent process is running\n");
        printf("\nGoing to kill MTAAgent process\n");
        system ("kill -9 `pidof CcspMtaAgentSsp`");
        sleep(1500);

        if(0 == system("pidof CcspMtaAgentSsp > /dev/null"))   {
            printf("\nMTAAgent process has restarted \n");
            return 0;

        }

        else
        {
            printf ("\nMTAAgent process is not restarted after kill\n");
            return 1;
        }
    }

    else {

        printf ("\nMTAAgent process is not running\n");
        return 1;
    }
    printf("\n Exiting ssp_MTAAgentRestart function\n\n");
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CRRestart
 * Description          : This function will kill the CR process which is running by default
 *                        and check if the system has rebooted after kill.
 *
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CRRestart()
{
    printf("\n Entering ssp_CRRestart function\n\n");

    if(0 == system("pidof CcspCrSsp > /dev/null"))  {
        printf("\nCR is running\n");
        printf("\nGoing to kill CR process\n");
        system ("kill -9 `pidof CcspCrSsp`");
        sleep(1800);

        if(0 == system("pidof CcspCrSsp > /dev/null"))   {
            printf("\nCcspCrSsp process has restarted \n");
            return 0;

        }

        else
        {
            printf ("\nCcspCrSsp process is not restarted after kill\n");
            return 1;
        }
    }

    else {

        printf ("\nCcspCrSsp process is not running\n");
        return 1;
    }
    printf("\n Exiting ssp_CRRestart function\n\n");
}

/*******************************************************************************************
 *
 * Function Name        : ssp_pam_Init()
 * Description          : This function will check if the pam module is getting initialised
                          or not
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_pam_Init()
{
    int return_status = 0;
    unsigned long value = 0;
    printf("\n Entering ssp_pam_Init function\n\n");
       return_status = CosaDmlDiInit(NULL,NULL);

    if ( return_status == 0)
    {
        printf("ssp_pam_Init: success\n");
        return 0;
    }

    else
       {
    printf("ssp_pam_Init:Failed to initialise\n");
    return 1;
       }
}

int ssp_DmlMlanInit()
{
    int return_status = 0;
    return_status = CosaDmlMTAInit(NULL,(PANSC_HANDLE)bus_handle_client);
    if ( return_status != 0)
    {
        printf("ssp_CosaDmlMtaInit:Failed to Initialize \n");
        return 1;
    }
    return 0;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_DmlMlanGetParamValue
 * Description          : This function will grt the attributes of mlan
 *
 * @param [in]          : MethodName - get api to be invoked
 * @param [out]         : pValue - Holds the value of the attribute
 * @param [out]         : size - Holds the size of the attribute
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_DmlMlanGetParamValue(char* MethodName, char* pValue, PULONG size)
{
    int return_status = 0;
    int unload_status = 0;
    ANSC_HANDLE hContext = NULL;
    printf("\n Entering ssp_DmlMlanGetParamValue function\n\n");

    return_status = CosaDmlMlanInit(NULL, &hContext);
    if ( return_status != SSP_SUCCESS || hContext == NULL)
    {
        printf("ssp_CosaDmlMlanInit:Failed to Initialize the DML of Cosa Mlan\n");
        return SSP_FAILURE;
    }
    printf("ssp_CosaDmlMlanInit: Initialized the DML of Cosa Mlan\n");

    if( !(strcmp(MethodName, "PrimayLANIPInterface")) )
        return_status = CosaDmlMlanGetPrimaryLanIpIf(&hContext, pValue, size);
    else if( !(strcmp(MethodName, "HomeSecurityIPInterface")) )
        return_status = CosaDmlMlanGetHomeSecurityIpIf(&hContext, pValue, size);
    else if( !(strcmp(MethodName, "PrimaryLANBridge")) )
        return_status = CosaDmlMlanGetPrimaryLanBridge(&hContext, pValue, size);
    else if( !(strcmp(MethodName, "PrimaryLANBridgeHSPorts")) )
        return_status = CosaDmlMlanGetPrimaryLanBridgeHsPorts(&hContext, pValue, size);
    else if( !(strcmp(MethodName, "PrimaryLANDHCPv4ServerPool")) )
        return_status = CosaDmlMlanGetPrimaryLanDhcpv4ServerPool(&hContext, pValue, size);
    else if( !(strcmp(MethodName, "HomeSecurityBridge")) )
        return_status = CosaDmlMlanGetHomeSecurityBridge(&hContext, pValue, size);
    else if( !(strcmp(MethodName, "HomeSecurityBridgePorts")) )
        return_status = CosaDmlMlanGetHomeSecurityBridgePorts(&hContext, pValue, size);
    else if( !(strcmp(MethodName, "HomeSecurityDHCPv4ServerPool")) )
        return_status = CosaDmlMlanGetHomeSecurityDhcpv4ServerPool(&hContext, pValue, size);
    else if( !(strcmp(MethodName, "HomeSecurityWiFiRadio")) )
        return_status = CosaDmlMlanGetHomeSecurityWiFiRadio(&hContext, pValue, size);
    else if( !(strcmp(MethodName, "HomeSecurityWiFiSsid")) )
        return_status = CosaDmlMlanGetHomeSecurityWiFiSsid(&hContext, pValue, size);
    else if( !(strcmp(MethodName, "HomeSecurityWiFiAp")) )
        return_status = CosaDmlMlanGetHomeSecurityWiFiAp(&hContext, pValue, size);
    else if( !(strcmp(MethodName, "Init")) )
        return_status = SSP_SUCCESS;
    else
        return_status = SSP_FAILURE;
    printf("Returned from CosaDmlMlanGetPrimaryLanIpIf()\n");
    unload_status = CosaDmlMlanUnload(hContext);
    if ( unload_status == SSP_SUCCESS && hContext == NULL)
    {
        printf("CosaDmlMlanUnload:success \n");
    }
    else
       printf("CosaDmlMlanUnload:failed \n");

//check if the value of size variable is changed on returning from the get api
    if ( return_status != SSP_SUCCESS || *size == BUFFER_SIZE)
    {
        printf("ssp_DmlMlanGetParamValue:failed to retrieve the MLAN information %s %lu\n", pValue, *size);
        return SSP_FAILURE;
    }
        printf("ssp_DmlMlanGetParamValue: retrieved MLAN information  %s %lu \n", pValue, *size);
        return SSP_SUCCESS;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_DmlEthGetParamValue
 * Description          : This function will get the attributes of ethernet port
 *
 * @param [in]          : MethodName - get api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_DmlEthGetParamValue(char* MethodName)
{
    int return_status = 0;
    int unload_status = 0;
    ANSC_HANDLE hContext = NULL;
    unsigned long count = 0;
    printf("\n Entering ssp_DmlEthGetParamValue function\n\n");

    return_status = CosaDmlEthInit(NULL, &hContext);
    if ( return_status != SSP_SUCCESS || hContext == NULL)
    {
        printf("ssp_CosaEthMlanInit:Failed to Initialize the DML of Cosa Eth\n");
        return SSP_FAILURE;
    }
    printf("ssp_CosaEthMlanInit: Initialized the DML of Cosa Eth\n");

    if( !(strcmp(MethodName, "GetStats")) )
    {
       COSA_DML_ETH_STATS stats = {0};
        int i = 0;

        count = CosaDmlEthPortGetNumberOfEntries(hContext);
        for(i = 1; i<=count; i++)
        {
            return_status = CosaDmlEthPortGetStats(hContext, i, &stats);
            printf("In ssp CosaDmlEthGetParamVal() stats.BytesReceived, stats.BytesSent, stats.PacketsSent, stats.PacketsReceived, stats.BroadcastPacketsSent %lu %lu %lu %lu %lu\n", stats.BytesReceived, stats.BytesSent, stats.PacketsSent, stats.PacketsReceived, stats.BroadcastPacketsSent);

            if ( stats.BytesSent != 0 )
            {
                return_status = SSP_SUCCESS;
                break;
            }
            else
                return_status = SSP_FAILURE;
	}
    }

    else if( !(strcmp(MethodName, "GetDinfo")) )
    {
	char status[20]="";
        COSA_DML_ETH_PORT_DINFO dinfo = {0};
        return_status = CosaDmlEthPortGetDinfo(hContext, 1, &dinfo);
	printf("In ssp CosaDmlEthGetParamVal() dinfo.Status %lu\n", dinfo.Status);
	if( dinfo.Status == 1)
          sprintf(status,"Up");
        else if( dinfo.Status == 2)
          sprintf(status,"Down");
        else if( dinfo.Status == 3)
          sprintf(status,"Unknown");
        else if( dinfo.Status == 4)
          sprintf(status,"Dormant");
        else if( dinfo.Status == 5)
          sprintf(status,"NotPresent");
        else if(dinfo.Status == 6)
          sprintf(status,"LowerLayerDown");
        else if( dinfo.Status == 7)
          sprintf(status,"Error");
        else
          return_status = SSP_FAILURE;
	printf("Status is %s\n", status);
    }

    else if( !(strcmp(MethodName, "GetCfg")) )
    {
        COSA_DML_ETH_PORT_CFG cfg = {0};
        cfg.InstanceNumber = 1;
        return_status = CosaDmlEthPortGetCfg(hContext, &cfg);
	printf("In ssp CosaDmlEthGetParamVal() cfg.bEnabled %d\n", cfg.bEnabled);
	if(cfg.bEnabled !=0 && cfg.bEnabled !=1)
           return_status = SSP_FAILURE;
    }

    else if( !(strcmp(MethodName, "GetEntryCount")) )
    {
       count = CosaDmlEthPortGetNumberOfEntries(hContext);
       printf("In ssp CosaDmlEthPortGetNumberOfEntries() returned %lu\n", count);
        if( count ==0 )
           return_status = SSP_FAILURE;
       else
           return_status = SSP_SUCCESS;
    }

    else if( !(strcmp(MethodName, "GetEntry")) )
    {
        COSA_DML_ETH_PORT_FULL entry = {0};
        return_status = CosaDmlEthPortGetEntry(hContext, 1, &entry);
        printf("In ssp CosaDmlEthGetParamVal() entry name %s\n", entry.StaticInfo.Name);

        if( strlen(entry.StaticInfo.Name)==0 )
            return_status = SSP_FAILURE;
    }

    else if( !(strcmp(MethodName, "Init")) )
        return_status = SSP_SUCCESS;

    else
       return_status = SSP_FAILURE;

    if ( return_status != SSP_SUCCESS )
        printf("ssp_DmlEthGetParamValue:failed to retrieve the Eth information \n");
    else
        printf("ssp_DmlEthGetParamValue: retrieved Eth information \n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_DmlDiGetParamValue
 * Description          : This function will grt the attributes of mlan
 *
 * @param [in]          : MethodName - get api to be invoked
 * @param [out]         : pValue - Holds the value of the attribute
 * @param [out]         : size - Holds the size of the attribute
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_DmlDiGetParamValue(char* MethodName, char* pValue, PULONG size)
{
    int return_status = 0;
    int unload_status = 0;
    ANSC_HANDLE hContext = NULL;
    *size = 0;
    printf("\n Entering ssp_DmlMlanGetParamValue function\n\n");

    return_status = CosaDmlDiInit(NULL, &hContext);
    if ( return_status != SSP_SUCCESS )
    {
        printf("ssp_CosaDmlMlanInit:Failed to Initialize the DML of Cosa Di\n");
        return SSP_FAILURE;
    }
    printf("ssp_CosaDmlMlanInit: Initialized the DML of Cosa Di\n");

    if( !(strcmp(MethodName, "Manufacturer")) )
        return_status = CosaDmlDiGetManufacturer(NULL,pValue,size);
    else if( !(strcmp(MethodName, "ManufacturerOUI")) )
        return_status = CosaDmlDiGetManufacturerOUI(NULL,pValue,size);
    else if( !(strcmp(MethodName, "ModelName")) )
        return_status = CosaDmlDiGetModelName(NULL,pValue,size);
    else if( !(strcmp(MethodName, "Description")) )
        return_status = CosaDmlDiGetDescription(NULL,pValue,size);
    else if( !(strcmp(MethodName, "ProductClass")) )
        return_status = CosaDmlDiGetProductClass(NULL,pValue,size);
    else if( !(strcmp(MethodName, "SerialNumber")) )
        return_status = CosaDmlDiGetSerialNumber(NULL,pValue,size);
    else if( !(strcmp(MethodName, "Init")) )
    {
       return_status = SSP_SUCCESS;
       *size = 1;
    }
    else
       return_status = SSP_FAILURE;

    if ( return_status != SSP_SUCCESS || *size == 0 )
    {
        printf("ssp_DmlDiGetParamValue:failed to retrieve the Di information \n");
        return SSP_FAILURE;
    }
        printf("ssp_DmlDiGetParamValue: retrieved Di information \n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlUpnpInit
 * Description          : This function will initialize the DML UPNP of Pam
 *
 * @param [in]          : None
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlUpnpInit(void)
{

    int return_status = 0;
    ANSC_HANDLE pam_handle = NULL;

    printf("\n Entering ssp_CosaDmlUpnpInit function\n\n");

    pam_handle = bus_handle_client;

    return_status = CosaDmlUpnpInit(NULL,(PANSC_HANDLE)pam_handle);

    if ( return_status != 0)
    {
        printf("ssp_CosaDmlUpnpInit:Failed to Initialize the upnp of pam\n");
        return 1;
    }
    return 0;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlUpnpEnable
 * Description          : This function will invoke the cosa api of PAM to retrieve the
 *                        Set Enable of Upnp
 *
 * @param [in]          : Value - holds the booleanvalue
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlUpnpEnable(char* MethodName,int boolValue)
{
    int return_status = 0;
    ANSC_HANDLE pam_handle = NULL;

    printf("\n Entering ssp_CosaDmlUpnpDevEnable function\n\n");

    BOOLEAN value = (boolValue == 0)?FALSE:TRUE;
    pam_handle = bus_handle_client;

    if( !(strcmp(MethodName, "UpnpDev")) )
    {
        return_status = CosaDmlUpnpDevEnable(pam_handle,value);
    }
    else if( !(strcmp(MethodName, "UpnpMediaServer")) )
    {
       return_status = CosaDmlUpnpDevEnableMediaServer(pam_handle,value);
    }
    else if( !(strcmp(MethodName, "UpnpIgd")) )
    {
       return_status = CosaDmlUpnpDevEnableIgd(pam_handle,value);
    }

    if ( return_status != 1)
    {
        printf("ssp_CosaDmlUpnpEnable:Upnp is enabled\n");
        return 0;
    }
    printf("ssp_CosaDmlUpnpEnable:Upnp is disabled\n");
    return 1;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlUpnpGetState
 * Description          : This function will invoke the cosa api of MTA to retrieve the
 *                        state of upnpdev Igd
 *
 * @param [in]          : Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlUpnpGetState(char* MethodName)
{
    int return_status = 0;
    ANSC_HANDLE pam_handle = NULL;

    printf("\n Entering ssp_CosaDmlUpnpGetState function\n\n");

    pam_handle = bus_handle_client;

    if( !(strcmp(MethodName, "UpnpIgd")) )
    {
        return_status = CosaDmlUpnpDevGetIgdState(pam_handle);
    }
    if( !(strcmp(MethodName, "UpnpDev")) )
    {
           return_status = CosaDmlUpnpDevGetState(pam_handle);
    }
    if( !(strcmp(MethodName, "UpnpMediaServer")) )
    {
           return_status = CosaDmlUpnpDevGetMediaServerState(pam_handle);
    }
    printf("return_status is %d",return_status);
    if ( return_status != 0)
    {
        printf("ssp_CosaDmlUpnpGetState: state of upnp is enabled\n");
    }
    printf("ssp_CosaDmlUpnpGetState: state of upnp is disabled");
    return 0;

}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlDhcpInit
 * Description          : This function will initialize the DML DHCP of Pam
 *
 * @param [in]          : None
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlDhcpInit(void)
{

    int return_status = 0;
    ANSC_HANDLE pam_handle = NULL;

    printf("\n Entering ssp_CosaDmlDhcpInit function\n\n");

    pam_handle = bus_handle_client;

    return_status = CosaDmlDhcpInit(NULL,(PANSC_HANDLE)pam_handle);

    if ( return_status != 0)
    {
        printf("ssp_CosaDmlDhcpInit:Failed to Initialize the Dhcp of pam\n");
        return 1;
    }

    return 0;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlDhcpGet
 * Description          : This function will invoke the cosa api of PAM to retrieve the DHCP config
 *
 *
 * @param [in]          : handleType - message bus handle
 * @param [in]          : bufferType - Valid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlDhcpGet(char* MethodName, void* cfg)
{
    int return_status = 0;
    ANSC_HANDLE pam_handle = NULL;
    COSA_DML_DHCPC_CFG DhcpCfg;
    COSA_DML_DHCPC_INFO DhcpInfo;
    int instnum=1;

    printf("\n Entering ssp_CosaDmlDhcpGet function\n\n");

    pam_handle = bus_handle_client;

    if( !(strcmp(MethodName, "DhcpcConf")) )
    {
       CFG* temp = cfg;
	DhcpCfg.InstanceNumber =1;
        return_status = CosaDmlDhcpcGetCfg(pam_handle,&DhcpCfg);

        printf("ssp_CosaDmlDhcpcGetCfg: Instance Number  retrieved:%d\n",DhcpCfg.InstanceNumber);
        printf("ssp_CosaDmlDhcpcGetCfg: Alias retrieved:%s\n",DhcpCfg.Alias);
        printf("ssp_CosaDmlDhcpcGetCfg: Status retrieved:%d\n",DhcpCfg.bEnabled);
        printf("ssp_CosaDmlDhcpcGetCfg: Interface retrieved:%s\n",DhcpCfg.Interface);
        printf("ssp_CosaDmlDhcpcGetCfg: PassthroughEnable retrieved:%d\n",DhcpCfg.PassthroughEnable);

        temp->InstanceNumber =(unsigned long)DhcpCfg.InstanceNumber;
        strcpy(temp->Alias ,DhcpCfg.Alias);
        temp->bEnabled = (int)DhcpCfg.bEnabled;
        strcpy(temp->Interface,DhcpCfg.Interface);
        temp->PassthroughEnable = (int)DhcpCfg.PassthroughEnable;
    }

    else if( !(strcmp(MethodName, "DhcpcInfo")) )
    {
       INFO* temp = cfg;
       return_status = CosaDmlDhcpcGetInfo(pam_handle,instnum,&DhcpInfo);

        printf("ssp_CosaDmlDhcpcGetInfo: Status retrieved:%d\n",DhcpInfo.Status);
        printf("ssp_CosaDmlDhcpcGetInfo: DHCP status retrieved:%d\n",DhcpInfo.DHCPStatus);
        printf("ssp_CosaDmlDhcpcGetInfo: DhcpInfo of IP routers retrieved:%d\n",DhcpInfo.NumIPRouters);
        printf("ssp_CosaDmlDhcpcGetInfo: DhcpInfo of Dns servers retrieved:%d\n",DhcpInfo.NumDnsServers);

        temp->Status=(unsigned long)DhcpInfo.Status;
        temp->DHCPStatus =(unsigned long)DhcpInfo.DHCPStatus;
        temp->NumIPRouters=(int)DhcpInfo.NumIPRouters;
        temp->NumDnsServers=(int)DhcpInfo.NumDnsServers;
    }
    else if ( !(strcmp(MethodName, "DhcpcNumberOfEntries")) )
    {
       int* temp =cfg;
       return_status = CosaDmlDhcpcGetNumberOfEntries(pam_handle);
       if (return_status ==1)
       {
           printf("ssp_CosaDmlDhcpcGetNumberOfEntries info:%d\n",return_status);
           *temp=return_status;
          return_status=0;
       }
    }

    else if ( !(strcmp(MethodName, "DhcpcInstanceNumber")) )
    {
       CFG* temp =cfg;
       DhcpCfg.InstanceNumber =1;
       return_status = CosaDmlDhcpcGetCfg(pam_handle,&DhcpCfg);
       printf("ssp_CosaDmlDhcpcGetCfg: Instance Number  retrieved:%d\n",DhcpCfg.InstanceNumber);
       temp->InstanceNumber =(unsigned long)DhcpCfg.InstanceNumber;
    }

    else if ( !(strcmp(MethodName, "DhcpsNumberOfPools")) )
    {
       int* temp =cfg;
       return_status = CosaDmlDhcpsGetNumberOfPools(pam_handle);
       if (return_status !=0)
       {
            printf("ssp_CosaDmlDhcpcGetNumberOfEntries info:%d\n",return_status);
            *temp=return_status;
           return_status=0;
       }
    }

    else if ( !(strcmp(MethodName, "DhcpsState")) )
    {
       int* temp = cfg;
       return_status = CosaDmlDhcpsGetState(pam_handle);
       if ( return_status != 0)
        {
           printf("ssp_CosaDmlDhcpsGetState: DhcpsGetState is enabled\n");*temp=return_status;
           return_status=0;
        }
        printf("ssp_CosaDmlDhcpsGetState: DhcpsGetState is disabled");*temp=return_status;
        return_status=0;

    }

    if ( return_status != 0)
    {
        printf("ssp_CosaDmlDhcpcGetCfg:Failed to retrieve the Config\n");
        return 1;
    }
    return 0;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlDhcpsEnable
 * Description          : This function will invoke the cosa api of PAM to retrieve the Set Enable of DHCP server
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlDhcpsEnable(int boolValue)
{
    int return_status = 0;
    ANSC_HANDLE pam_handle = NULL;
    printf("\n Entering ssp_CosaDmlDhcpsEnable function\n\n");
    BOOLEAN value = (boolValue == 0)?FALSE:TRUE;
    pam_handle = bus_handle_client;

    return_status = CosaDmlDhcpsEnable(pam_handle,value);
    if ( return_status != 1)
    {
        printf("ssp_CosaDmlDhcpsEnable:DHCP server is enabled\n");
        return 0;
    }
    printf("ssp_CosaDmlDhcpsEnable:DHCP server is disabled\n");
    return 1;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlDnsInit
 * Description          : This function will initialize the DML DNS of Pam
 *
 * @param [in]          : None
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlDnsInit(void)
{

    int return_status = 0;
    ANSC_HANDLE pam_handle = NULL;

    printf("\n Entering ssp_CosaDmlDnsInit function\n\n");

    pam_handle = bus_handle_client;

    return_status = CosaDmlDnsInit(NULL,(PANSC_HANDLE)pam_handle);

    if ( return_status != 0)
    {
        printf("ssp_CosaDmlDnsInit:Failed to Initialize the Dns of pam\n");
        return 1;
    }

    return 0;
}

/********************************************************************************************
 *Parameter Name        : ssp_CosaDmlDnsGet
 * Description          : This function will invoke the cosa api of PAM to retrieve the value of DNS apis
 *
 * @param [in]          : MethodName - name of api
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlDnsGet(char* MethodName, void* cfg)
{
    int return_status = 0;
    ANSC_HANDLE pam_handle = NULL;
    COSA_DML_DNS_CLIENT_SERVER DnsCfg;
    unsigned long DNSServers=0;
    pam_handle = bus_handle_client;

    printf("\n Entering ssp_CosaDmlDnsGet function\n\n");
    if( !(strcmp(MethodName, "DnsClientServerCfg")) )
    {
       DNS* temp= cfg;
       return_status = CosaDmlDnsClientGetServer(pam_handle,&DnsCfg);

       printf("ssp_CosaDmlDnsClientGetServer: Instance Number  retrieved:%d\n",DnsCfg.InstanceNumber);
       printf("ssp_CosaDmlDnsGet: Alias retrieved:%s\n",DnsCfg.Alias);
       printf("ssp_CosaDmlDnsGet: Status retrieved:%d\n",DnsCfg.bEnabled);
       printf("ssp_CosaDmlDnsGet: Interface retrieved:%s\n",DnsCfg.Interface);

       temp->InstanceNumber =(unsigned long)DnsCfg.InstanceNumber;
       strcpy(temp->Alias ,DnsCfg.Alias);
       temp->bEnabled = (int)DnsCfg.bEnabled;
       strcpy(temp->Interface,DnsCfg.Interface);
    }

    else if ( !(strcmp(MethodName, "DnsClientStatus")) )
    {
       int* temp =cfg;
       return_status = CosaDmlIpDnsGetClientStatus(pam_handle);
       if ( return_status != 0)
       {
       printf("ssp_CosaDmlDnsGet: IpDnsGetClientStatus is enabled\n");
       *temp = return_status;
       return_status=0;
       }
       printf("ssp_CosaDmlIpDnsGetClientStatus: IpDnsGetClientStatus is disabled");
       *temp = return_status;
       return_status=0;
    }
    else if( !(strcmp(MethodName, "DnsClientServers")) )
    {
       int* temp =cfg;
       return_status = CosaDmlDnsClientGetServers(pam_handle,&DNSServers);
       if (return_status != 0)
       {
       printf("ssp_CosaDmlDnsGet: number of servers is %d\n",DNSServers);
       *temp = (int)DNSServers;
       return_status =0;
       }
    }
    else if ( !(strcmp(MethodName, "DnsRelayStatus")) )
    {
       int* temp =cfg;
       return_status = CosaDmlIpDnsGetRelayStatus(pam_handle);
       if ( return_status != 0)
       {
        printf("ssp_CosaDmlDnsGet: IpDnsGetRelayStatus is enabled\n");
        *temp = return_status;
        return_status=0;
       }
       printf("ssp_CosaDmlDnsGet: IpDnsGetRelayStatus is disabled");
       *temp = return_status;
       return_status=0;
    }
    else if( !(strcmp(MethodName, "DnsRelayServers")) )
    {
       int* temp =cfg;
       return_status = CosaDmlDnsRelayGetServers(pam_handle,&DNSServers);
       if (return_status != 0)
       {
       printf("ssp_CosaDmlDnsGet: number of servers is %d\n",DNSServers);
       *temp = (int)DNSServers;
       return_status =0;
        }
    }
    if ( return_status != 0)
    {
        printf("ssp_CosaDmlDnsGet:Failed to retrieve the information \n");
        return 1;
    }

    return 0;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlDnsEnable
 * Description          : This function will invoke the cosa api of PAM to retrieve the
 *                        Set Enable of Dns
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlDnsEnable(char* MethodName, int boolValue)
{
    int return_status = 0;
    ANSC_HANDLE pam_handle = NULL;
    printf("\n Entering ssp_CosaDmlDnsEnable function\n\n");
    BOOLEAN value = (boolValue == 0)?FALSE:TRUE;

    pam_handle = bus_handle_client;
    if( !(strcmp(MethodName, "DnsClient")) )
    {
               return_status = CosaDmlDnsEnableClient(pam_handle,value);
       }
        else if( !(strcmp(MethodName, "DnsRelay")) )
    {
               return_status = CosaDmlDnsEnableRelay(pam_handle,value);
       }

    if ( return_status != 1)
    {
        printf("ssp_CosaDmlDnsEnable:Dns is enabled\n");
        return 0;
    }
    printf("ssp_CosaDmlDnsEnableClient:Dns is disabled\n");
    return 1;
}

#endif
