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

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "ssp_tdk_cmhal_wrp.h"


/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_GetParamCharValue
 * Description          : This function will invoke the hal api of CM to get the char values
 *
 * @param [in]          : paramName: specifies the name of the API
			  value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CMHAL_GetParamCharValue(char* paramName, char* value)
{
    int return_status = 0;
    CMMGMT_CM_DOCSIS_INFO docsisinfo;
    CMMGMT_CM_IPV6DHCP_INFO v6dhcpinfo;
    CMMGMT_CM_DHCP_INFO v4dhcpinfo;
    PCMMGMT_CM_DS_CHANNEL pDsFreq,temp_DsFreq;
    PCMMGMT_CM_US_CHANNEL pUsFreq,temp_UsFreq;
    PCMMGMT_CM_US_CHANNEL pUsPower,temp_UsPower;
    PCMMGMT_CM_DS_CHANNEL pDsPower,temp_DsPower;
    printf("\nEntering ssp_CMHAL_GetParamCharValues function\n\n");
    if( !(strcmp(paramName, "CMStatus")) )
    {
        return_status = docsis_getCMStatus(value);
        printf("Return status of docsis_getCMStatus %d", return_status);

        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetCharParamValues : Failed to get the CM status\n");
            return SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "MddIpModeOverride")) )
    {
        return_status = docsis_GetMddIpModeOverride(value);
        printf("Return status of docsis_GetMddIpModeOverride %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetParamCharValues : Failed to get MddIpModeOverride\n");
            return SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "ProvIpType")) )
    {
        return_status = docsis_GetProvIpType(value);
        printf("Return status of docsis_GetProvIpType %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetParamCharValues : Failed to get IPType\n");
            return SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "MarketInfo")) )
    {
        return_status = cm_hal_GetMarket(value);
        printf("Return status of cm_hal_GetMarket %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetCharParamValues : Failed to get Market info\n");
            return SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "version")) )
    {
       if(value)
       {
           return_status = docsis_GetDOCSISInfo(&docsisinfo);
           printf("ssp_CMHAL_GetParamCharValue: Version retreived :%s\n",docsisinfo.DOCSISVersion);
           strcpy(value, docsisinfo.DOCSISVersion);
       }
       else
           return_status = docsis_GetDOCSISInfo((PCMMGMT_CM_DOCSIS_INFO)value);
    }
    else if( !(strcmp(paramName, "Ipv6DhcpBootFileName")) )
    {
        if(value)
        {
           strcpy(value, " ");
            return_status = cm_hal_GetIPv6DHCPInfo(&v6dhcpinfo);
           printf("ssp_CMHAL_GetParamCharValue: BootFileName retreived :%s\n",v6dhcpinfo.IPv6BootFileName);
            strcpy(value, v6dhcpinfo.IPv6BootFileName);
        }
        else
            return_status = cm_hal_GetIPv6DHCPInfo((PCMMGMT_CM_IPV6DHCP_INFO)value);
    }
    else if( !(strcmp(paramName, "RebindTimeRemaining")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = cm_hal_GetDHCPInfo(&v4dhcpinfo);
           printf("ssp_CMHAL_GetParamCharValue: RebindTimeRemaining retreived :%s\n",v4dhcpinfo.RebindTimeRemaining);
            strcpy(value, v4dhcpinfo.RebindTimeRemaining);
        }
        else
            return_status = cm_hal_GetDHCPInfo((PCMMGMT_CM_DHCP_INFO)value);
    }
    else if( !(strcmp(paramName, "RenewTimeRemaining")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = cm_hal_GetDHCPInfo(&v4dhcpinfo);
           printf("ssp_CMHAL_GetParamCharValue: RenewTimeRemaining retreived :%s\n",v4dhcpinfo.RenewTimeRemaining);
            strcpy(value, v4dhcpinfo.RenewTimeRemaining);
        }
        else
            return_status = cm_hal_GetDHCPInfo((PCMMGMT_CM_DHCP_INFO)value);
    }
    else if( !(strcmp(paramName, "Ipv4DhcpBootFileName")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = cm_hal_GetDHCPInfo(&v4dhcpinfo);
           printf("ssp_CMHAL_GetParamCharValue: BootFileName retreived :%s\n",v4dhcpinfo.BootFileName);
            strcpy(value, v4dhcpinfo.BootFileName);
        }
        else
            return_status = cm_hal_GetDHCPInfo((PCMMGMT_CM_DHCP_INFO)value);
    }
    else if( !(strcmp(paramName, "Ipv6DhcpIPAddress")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = cm_hal_GetIPv6DHCPInfo(&v6dhcpinfo);
            printf("ssp_CMHAL_GetParamCharValue: IPAddress retreived :%s\n",v6dhcpinfo.IPv6Address);
            strcpy(value, v6dhcpinfo.IPv6Address);
	 }
        else
            return_status = cm_hal_GetIPv6DHCPInfo((PCMMGMT_CM_IPV6DHCP_INFO)value);
    }
    else if( !(strcmp(paramName, "ConfigFileName")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = docsis_GetDOCSISInfo(&docsisinfo);
           printf("ssp_CMHAL_GetParamCharValue: ConfigFileName retreived :%s\n",docsisinfo.DOCSISConfigFileName);
            strcpy(value, docsisinfo.DOCSISConfigFileName);
        }
        else
            return_status = docsis_GetDOCSISInfo((PCMMGMT_CM_DOCSIS_INFO)value);
    }
    else if( !(strcmp(paramName, "DS_DataRate")) )
    {
        if(value)
        {
            return_status = docsis_GetDOCSISInfo(&docsisinfo);
            printf("ssp_CMHAL_GetParamCharValue: DownstreamDataRate retreived :%s\n",docsisinfo.DOCSISDownstreamDataRate);
            strcpy(value, docsisinfo.DOCSISDownstreamDataRate);
        }
        else
            return_status = docsis_GetDOCSISInfo((PCMMGMT_CM_DOCSIS_INFO)value);
    }
    else if( !(strcmp(paramName, "US_DataRate")) )
    {
        if(value)
        {
            return_status = docsis_GetDOCSISInfo(&docsisinfo);
            printf("ssp_CMHAL_GetParamCharValue: UpstreamDataRate retreived :%s\n",docsisinfo.DOCSISUpstreamDataRate);
            strcpy(value, docsisinfo.DOCSISUpstreamDataRate);
        }
        else
            return_status = docsis_GetDOCSISInfo((PCMMGMT_CM_DOCSIS_INFO)value);
    }
    else if( !(strcmp(paramName, "DS_Frequency")) )
    {
       long unsigned int  count = 0;
       return_status = docsis_GetNumOfActiveRxChannels(&count);
       printf("Count of Active Rx channels is %lu\n",count);
       if (return_status == 0)
       {
           pDsFreq = (PCMMGMT_CM_DS_CHANNEL) malloc(sizeof(CMMGMT_CM_DS_CHANNEL)*count);

           if(!pDsFreq)
           {
               printf("Memory has not allocated successfully \n ");
           }
           else
           {
               return_status = docsis_GetDSChannel(&pDsFreq);

               int i = 0;
	       strcpy(value, "");
               for(i=0;i<count;i++)
               {
                   printf("ssp_CMHAL_GetParamCharValue: DS Frequency retreived :%s\n",pDsFreq[i].Frequency);
                   char FreqString[64] = {0};

                   strcpy(FreqString,pDsFreq[i].Frequency);
                   strcat(value, FreqString);
                   strcat(value, ",");
               }
           }

           if(pDsFreq != NULL)
           {
               free(pDsFreq);
           }
       }
    }
    else if( !(strcmp(paramName, "US_Frequency")) )
    {
        long unsigned int  count = 0;
       return_status = docsis_GetNumOfActiveTxChannels(&count);
        printf("Count of Active Tx channels is %lu\n",count);
        if (return_status == 0)
        {
            pUsFreq = (PCMMGMT_CM_US_CHANNEL) malloc(sizeof(CMMGMT_CM_US_CHANNEL)*count);

            if(!pUsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                if (value)
                {
                    return_status = docsis_GetUSChannel(&pUsFreq);
                    int i = 0;
                    strcpy(value,"");
                    for(i=0;i<count;i++)
                   {
                    printf("ssp_CMHAL_GetParamCharValue: US Frequency retreived :%s\n",pUsFreq[i].Frequency);
                    char FreqString[64] = {0};
                    strcpy(FreqString,pUsFreq[i].Frequency);
                    strcat(value, FreqString);
                    strcat(value, ",");
                   }
                }   
                else
                {
                    return_status = docsis_GetUSChannel(NULL);
                    printf("docsis_GetUSChannel return status is %d",return_status);
                }
            }
            if(pUsFreq != NULL)
            {
                 free(pUsFreq);
            }
        }
    }
    else if( !(strcmp(paramName, "ModulationAndSNRLevel")) )
    {
        long unsigned int  count = 0;
        return_status = docsis_GetNumOfActiveRxChannels(&count);
        printf("Count of Active Rx channels is %lu\n",count);
	if (return_status == 0)
        {
            pDsFreq = (PCMMGMT_CM_DS_CHANNEL) malloc(sizeof(CMMGMT_CM_DS_CHANNEL)*count);

            if(!pDsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                if (value)
                {
                   return_status = docsis_GetDSChannel(&pDsFreq);
                   int i = 0;
                   strcpy(value, "");
                   for(i=0;i<count;i++)
                   {
                      printf("ssp_CMHAL_GetParamCharValue: DS Modulation retreived :%s\n",pDsFreq[i].Modulation);
                      printf("ssp_CMHAL_GetParamCharValue: DS SNR Level retreived :%s\n",pDsFreq[i].SNRLevel);
                      char SNRString[64] = {0};
                      strcpy(SNRString,pDsFreq[i].SNRLevel);
                      strcat(value, pDsFreq[i].Modulation);
                      strcat(value, ":");
                      strcat(value, SNRString);
                      strcat(value, ",");
                   }
                }
                else
                {
                    return_status = docsis_GetDSChannel(NULL);
                    printf("docsis_GetDSChannel return status is %d",return_status);
                }
            }
            if(pDsFreq != NULL)
            {
                 free(pDsFreq);
            }
        }
    }
    else if( !(strcmp(paramName, "LockStatusAndChannelID")) )
    {
        long unsigned int  count = 0;
        return_status = docsis_GetNumOfActiveRxChannels(&count);
        printf("Count of Active Rx channels is %lu\n",count);
        if (return_status == 0)
        {
            pDsFreq = (PCMMGMT_CM_DS_CHANNEL) malloc(sizeof(CMMGMT_CM_DS_CHANNEL)*count);

            if(!pDsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                return_status = docsis_GetDSChannel(&pDsFreq);

                int i = 0;
                strcpy(value, "");
                for(i=0;i<count;i++)
                {
                    printf("ssp_CMHAL_GetParamCharValue: DS LockStatus retreived :%s\n",pDsFreq[i].LockStatus);
                    printf("ssp_CMHAL_GetParamCharValue: DS ChannelID retreived :%lu\n",pDsFreq[i].ChannelID);
                    char Channelid[16] = {0};
                    sprintf(Channelid,"%lu",pDsFreq[i].ChannelID);
                    strcat(value, pDsFreq[i].LockStatus);
		    strcat(value, ":");
                    strcat(value, Channelid);
                    strcat(value, ",");
                }
            }
            if(pDsFreq != NULL)
            {
                 free(pDsFreq);
            }
        }
    }
    else if( !(strcmp(paramName, "ModulationAndUSPower")) )
    {
        long unsigned int  count = 0;
        return_status = docsis_GetNumOfActiveTxChannels(&count);
        printf("Count of Active Tx channels is %lu\n",count);
        if (return_status == 0)
        {
            pUsPower = (PCMMGMT_CM_US_CHANNEL) malloc(sizeof(CMMGMT_CM_US_CHANNEL)*count);
            if(!pUsPower)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                return_status =  docsis_GetUSChannel(&pUsPower);
                int i = 0;
                strcpy(value, "");
                temp_UsPower=pUsPower;
                for(i=0;i<count;i++)
                {
                    printf("ssp_CMHAL_GetParamCharValue: US Modulation retreived :%s\n",temp_UsPower->Modulation);
                    printf("ssp_CMHAL_GetParamCharValue: US Power Level retreived :%s\n",temp_UsPower->PowerLevel);
                    char PowerString[64] = {0};
                    strcpy(PowerString,temp_UsPower->PowerLevel);
                    strcat(value, temp_UsPower->Modulation);
                    strcat(value, ":");
                    strcat(value, PowerString);
                    strcat(value, ",");
                    temp_UsPower++;
                }
            }
            free(pUsPower);
        }
    }
    else if( !(strcmp(paramName, "DS_Power")) )
    {
       long unsigned int  count;
       return_status = docsis_GetNumOfActiveRxChannels(&count);
       printf("Count of Active Rx channels is %lu\n",count);
       if (return_status == 0)
       {
           pDsPower = (PCMMGMT_CM_DS_CHANNEL) malloc(sizeof(CMMGMT_CM_DS_CHANNEL)*count);
           if(!pDsPower)
           {
               printf("Memory has not allocated successfully \n ");
	   }
           else
           {
               return_status = docsis_GetDSChannel(&pDsPower);
               int i;
               strcpy(value, "");
               temp_DsPower=pDsPower;
               for(i=0;i<count;i++)
               {
                   printf("ssp_CMHAL_GetParamCharValue: DS Power retreived :%s\n",temp_DsPower->PowerLevel);
                   char PowerString[128];
                   strcpy(PowerString,temp_DsPower->PowerLevel);
                   strcat(value, PowerString);
                   strcat(value, ",");
                   temp_DsPower++;
               }
           }
           free(pDsPower);
       }
    }
     else if( !(strcmp(paramName, "TimeServer")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = cm_hal_GetIPv6DHCPInfo(&v6dhcpinfo);
           printf("ssp_CMHAL_GetParamCharValue: TimeServer retreived :%s\n",v6dhcpinfo.IPv6TimeServer);
            strcpy(value,v6dhcpinfo.IPv6TimeServer);
        }
        else
            return_status = cm_hal_GetIPv6DHCPInfo((PCMMGMT_CM_IPV6DHCP_INFO)value);
    }

    else if( !(strcmp(paramName, "Ipv4TimeServer")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = cm_hal_GetDHCPInfo(&v4dhcpinfo);
            printf("ssp_CMHAL_GetParamCharValue: IPV4TimeServer retreived :%s\n",v4dhcpinfo.TimeServer);
            strcpy(value, v4dhcpinfo.TimeServer);
        }
        else
            return_status = cm_hal_GetDHCPInfo((PCMMGMT_CM_DHCP_INFO)value);
    }
  
    else if( !(strcmp(paramName, "USChannelIDAndFrequency")) )
    {
        long unsigned int  count;
        return_status = docsis_GetNumOfActiveTxChannels(&count);
        printf("Count of Active Tx channels is %lu\n",count);
        if (return_status == 0)
        {
            pUsFreq = (PCMMGMT_CM_US_CHANNEL) malloc(sizeof(CMMGMT_CM_US_CHANNEL)*count);
            if(!pUsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                return_status =  docsis_GetUSChannel(&pUsFreq);
                int i;
                strcpy(value, "");
                temp_UsFreq=pUsFreq;
                for(i=0;i<count;i++)
                {
                    printf("ssp_CMHAL_GetParamCharValue: US Channel ID retreived :%lu\n",temp_UsFreq->ChannelID);
                    printf("ssp_CMHAL_GetParamCharValue: US Frequency retreived :%s\n",temp_UsFreq->Frequency);
                    char FreqString[64];
		    char Channelid[16];
                    sprintf(Channelid,"%lu",temp_UsFreq->ChannelID);
                    strcpy(FreqString,temp_UsFreq->Frequency);
                    strcat(value, Channelid);
                    strcat(value, ":");
                    strcat(value, FreqString);
                    strcat(value, ",");
                    temp_UsFreq++;
                }
            }
            free(pUsFreq);
        }
    }
    else if( !(strcmp(paramName, "USSymbolRate")) )
    {
        long unsigned int  count;
       return_status = docsis_GetNumOfActiveTxChannels(&count);
        printf("Count of Active Tx channels is %lu\n",count);
        if (return_status == 0)
        {
            pUsFreq = (PCMMGMT_CM_US_CHANNEL) malloc(sizeof(CMMGMT_CM_US_CHANNEL)*count);
            if(!pUsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                return_status = docsis_GetUSChannel(&pUsFreq);
                int i;
                strcpy(value,"");
                temp_UsFreq=pUsFreq;
                for(i=0;i<count;i++)
                {
                    printf("ssp_CMHAL_GetParamCharValue: US symbol retreived :%s\n",temp_UsFreq->SymbolRate);
                    char FreqString[64];
                    strcpy(FreqString,temp_UsFreq->SymbolRate);
                    strcat(value, FreqString);
                    strcat(value, ",");
                    temp_UsFreq++;
                }
            }
            free(pUsFreq);
        }
    }
    else if( !(strcmp(paramName, "DSChannelIDAndFrequency")) )
    {
        long unsigned int  count;
        return_status = docsis_GetNumOfActiveRxChannels(&count);
        printf("Count of Active Rx channels is %lu\n",count);
        if (return_status == 0)
        {
            pDsFreq = (PCMMGMT_CM_DS_CHANNEL) malloc(sizeof(CMMGMT_CM_DS_CHANNEL)*count);
	    if(!pDsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                return_status =  docsis_GetDSChannel(&pDsFreq);
                int i;
                strcpy(value, "");
                temp_DsFreq=pDsFreq;
                for(i=0;i<count;i++)
                {
                    printf("ssp_CMHAL_GetParamCharValue: DS Channel ID retreived :%lu\n",temp_DsFreq->ChannelID);
                    printf("ssp_CMHAL_GetParamCharValue: DS Frequency retreived :%s\n",temp_DsFreq->Frequency);
                    char FreqString[64];
                    char Channelid[16];
                    sprintf(Channelid,"%lu",temp_DsFreq->ChannelID);
                    strcpy(FreqString,temp_DsFreq->Frequency);
                    strcat(value, Channelid);
                    strcat(value, ":");
                    strcat(value, FreqString);
                    strcat(value, ",");
                    temp_DsFreq++;
                }
            }
            free(pDsFreq);
        }
    }
    else if( !(strcmp(paramName, "DownstreamScanning")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = docsis_GetDOCSISInfo(&docsisinfo);
           printf("ssp_CMHAL_GetParamCharValue: Downstream Scanning retreived :%s\n",docsisinfo.DOCSISDownstreamScanning);
            strcpy(value, docsisinfo.DOCSISDownstreamScanning);
        }
        else
            return_status = docsis_GetDOCSISInfo((PCMMGMT_CM_DOCSIS_INFO)value);
    }
    else if( !(strcmp(paramName, "DSLockStatusAndFrequency")) )
    {
        long unsigned int  count;
        return_status = docsis_GetNumOfActiveRxChannels(&count);
        printf("Count of Active Rx channels is %lu\n",count);
        if (return_status == 0)
        {
            pDsFreq = (PCMMGMT_CM_DS_CHANNEL) malloc(sizeof(CMMGMT_CM_DS_CHANNEL)*count);
            if(!pDsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                return_status =  docsis_GetDSChannel(&pDsFreq);
                int i;
                strcpy(value, "");
                temp_DsFreq=pDsFreq;
                for(i=0;i<count;i++)
                {
                    printf("ssp_CMHAL_GetParamCharValue: DS LockStatus retreived :%s\n",temp_DsFreq->LockStatus);
                    printf("ssp_CMHAL_GetParamCharValues: DS Frequency retreived :%s\n",temp_DsFreq->Frequency);
                    char FreqString[64];
                    strcpy(FreqString,temp_DsFreq->Frequency);
                    FreqString[strlen(FreqString)- 4]  = '\0';
                    strcat(value, temp_DsFreq->LockStatus);
                    strcat(value, ":");
                    strcat(value, FreqString);
                    strcat(value, ",");
                    temp_DsFreq++;
                }
            }
            free(pDsFreq);
        }
    }
    else if( !(strcmp(paramName, "UpstreamRanging")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = docsis_GetDOCSISInfo(&docsisinfo);
           printf("ssp_CMHal_GetStructValues: Upstream Ranging Ranging retreived :%s\n",docsisinfo.DOCSISUpstreamRanging);
            strcpy(value, docsisinfo.DOCSISUpstreamRanging);
        }
        else
            return_status = docsis_GetDOCSISInfo((PCMMGMT_CM_DOCSIS_INFO)value);
    }
    else if( !(strcmp(paramName, "ToDStatus")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = docsis_GetDOCSISInfo(&docsisinfo);
           printf("ssp_CMHal_GetStructValues: ToD Status retreived :%s\n",docsisinfo.ToDStatus);
            strcpy(value, docsisinfo.ToDStatus);
        }
        else
            return_status = docsis_GetDOCSISInfo((PCMMGMT_CM_DOCSIS_INFO)value);
    }
    else if( !(strcmp(paramName, "Ipv6DhcpPrefix")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = cm_hal_GetIPv6DHCPInfo(&v6dhcpinfo);
           printf("ssp_CMHal_GetParamCharValue: IPv6 Prefix retreived :%s\n",v6dhcpinfo.IPv6Prefix);
            strcpy(value, v6dhcpinfo.IPv6Prefix);
        }
        else
            return_status = cm_hal_GetIPv6DHCPInfo((PCMMGMT_CM_IPV6DHCP_INFO)value);
    }
     else if( !(strcmp(paramName, "USLockStatusAndModulation")) )
    {
        long unsigned int  count;
        return_status = docsis_GetNumOfActiveTxChannels(&count);
        printf("Count of Active Tx channels is %lu\n",count);
        if (return_status == 0)
        {
            pUsFreq = (PCMMGMT_CM_US_CHANNEL) malloc(sizeof(CMMGMT_CM_US_CHANNEL)*count);
            if(!pUsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                return_status =  docsis_GetUSChannel(&pUsFreq);
                int i;
                strcpy(value, "");
                temp_UsFreq=pUsFreq;
                for(i=0;i<count;i++)
                {
                    printf("ssp_CMHAL_GetParamCharValue: US LockStatus retreived :%s\n",temp_UsFreq->LockStatus);
                    printf("ssp_CMHAL_GetParamCharValue: US Modulation retreived :%s\n",temp_UsFreq->Modulation);

                    strcat(value, temp_UsFreq->LockStatus);
                    strcat(value, ":");
                    strcat(value, temp_UsFreq->Modulation);
                    strcat(value, ",");
                    temp_UsFreq++;
                }
            }
            free(pUsFreq);
        }
    }
    else if( !(strcmp(paramName, "DSLockStatusAndModulation")) )
    {
        long unsigned int  count;
        return_status = docsis_GetNumOfActiveRxChannels(&count);
        printf("Count of Active Rx channels is %lu\n",count);
        if (return_status == 0)
        {
            pDsFreq = (PCMMGMT_CM_DS_CHANNEL) malloc(sizeof(CMMGMT_CM_DS_CHANNEL)*count);
            if(!pDsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                return_status =  docsis_GetDSChannel(&pDsFreq);
                int i;
                strcpy(value, "");
                temp_DsFreq=pDsFreq;
                for(i=0;i<count;i++)
                {
                    printf("ssp_CMHAL_GetParamCharValue: DS LockStatus retreived :%s\n",temp_DsFreq->LockStatus);
                    printf("ssp_CMHAL_GetParamCharValue: DS Modulation retreived :%s\n",temp_DsFreq->Modulation);
                    strcat(value, temp_DsFreq->LockStatus);
                    strcat(value, ":");
                    strcat(value, temp_DsFreq->Modulation);
                    strcat(value, ",");
                    temp_DsFreq++;
                }
            }
            free(pDsFreq);
        }
    }
     else if( !(strcmp(paramName, "USChannelIDAndType")) )
    {
        long unsigned int  count;
        return_status = docsis_GetNumOfActiveTxChannels(&count);
        printf("Count of Active Tx channels is %lu\n",count);
        if (return_status == 0)
        {
            pUsFreq = (PCMMGMT_CM_US_CHANNEL) malloc(sizeof(CMMGMT_CM_US_CHANNEL)*count);
            if(!pUsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                return_status =  docsis_GetUSChannel(&pUsFreq);
                int i;
                strcpy(value, "");
                temp_UsFreq=pUsFreq;
                for(i=0;i<count;i++)
                {
                    printf("ssp_CMHAL_GetParamCharValue: US Channel ID retreived :%lu\n",temp_UsFreq->ChannelID);
                    printf("ssp_CMHAL_GetParamCharValue: US Frequency retreived :%s\n",temp_UsFreq->ChannelType);
                    char FreqString[64];
                    char Channelid[16];
                    sprintf(Channelid,"%lu",temp_UsFreq->ChannelID);
                    strcpy(FreqString,temp_UsFreq->ChannelType);
                    strcat(value, Channelid);
                    strcat(value, ":");
                    strcat(value, FreqString);
                    strcat(value, ",");
                    temp_UsFreq++;
                }
            }
            free(pUsFreq);
        }
    }
    else if( !(strcmp(paramName, "DSChannelIDAndPower")) )
    {
        long unsigned int  count;
        return_status = docsis_GetNumOfActiveRxChannels(&count);
        printf("Count of Active Rx channels is %lu\n",count);
        if (return_status == 0)
        {
            pDsFreq = (PCMMGMT_CM_DS_CHANNEL) malloc(sizeof(CMMGMT_CM_DS_CHANNEL)*count);
            if(!pDsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                return_status =  docsis_GetDSChannel(&pDsFreq);
                int i;
                strcpy(value, "");
                temp_DsFreq=pDsFreq;
                for(i=0;i<count;i++)
                {
                    printf("ssp_CMHAL_GetParamCharValue: DS Channel ID retreived :%lu\n",temp_DsFreq->ChannelID);
                    printf("ssp_CMHAL_GetParamCharValue: DS Power retreived :%s\n",temp_DsFreq->PowerLevel);
                    char PowerString[64];
                    char Channelid[16];
                    sprintf(Channelid,"%lu",temp_DsFreq->ChannelID);
                    strcpy(PowerString,temp_DsFreq->PowerLevel);
                    strcat(value, Channelid);
                    strcat(value, ":");
                    strcat(value, PowerString);
                    strcat(value, ",");
                    temp_DsFreq++;
                }
            }
            free(pDsFreq);
        }
    }
    else if( !(strcmp(paramName, "USChannelIDAndPower")) )
    {
        long unsigned int  count;
        return_status = docsis_GetNumOfActiveTxChannels(&count);
        printf("Count of Active Tx channels is %lu\n",count);
        if (return_status == 0)
        {
            pUsFreq = (PCMMGMT_CM_US_CHANNEL) malloc(sizeof(CMMGMT_CM_US_CHANNEL)*count);
            if(!pUsFreq)
            {
                printf("Memory has not allocated successfully \n ");
            }
            else
            {
                return_status =  docsis_GetUSChannel(&pUsFreq);
                int i;
                strcpy(value, "");
                temp_UsFreq=pUsFreq;
                for(i=0;i<count;i++)
                {
                    printf("ssp_CMHAL_GetParamCharValue: US Channel ID retreived :%lu\n",temp_UsFreq->ChannelID);
                    printf("ssp_CMHAL_GetParamCharValue: US Power retreived :%s\n",temp_UsFreq->PowerLevel);
                    char PowerString[64];
                    char Channelid[16];
                    sprintf(Channelid,"%lu",temp_UsFreq->ChannelID);
                    strcpy(PowerString,temp_UsFreq->PowerLevel);
                    strcat(value, Channelid);
                    strcat(value, ":");
                    strcat(value, PowerString);
                    strcat(value, ",");
                    temp_UsFreq++;
                }
            }
            free(pUsFreq);
        }
    }
    else if( !(strcmp(paramName, "DOCSISDataRegComplete")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = docsis_GetDOCSISInfo(&docsisinfo);
           printf("ssp_CMHAL_GetParamCharValue: DHCP Status  retreived :%s\n",docsisinfo.DOCSISDataRegComplete);
            strcpy(value, docsisinfo.DOCSISDataRegComplete);
        }
        else
            return_status = docsis_GetDOCSISInfo((PCMMGMT_CM_DOCSIS_INFO)value);
    }
    else if( !(strcmp(paramName, "DownstreamRanging")) )
    {
        if(value)
        {
            strcpy(value, " ");
            return_status = docsis_GetDOCSISInfo(&docsisinfo);
           printf("ssp_CMHAL_GetParamCharValue: Downstream Ranging retreived :%s\n",docsisinfo.DOCSISDownstreamRanging);
            strcpy(value, docsisinfo.DOCSISDownstreamRanging);
        }
        else
            return_status = docsis_GetDOCSISInfo((PCMMGMT_CM_DOCSIS_INFO)value);
    }
    else if( !(strcmp(paramName, "Cert")) )
    {
        return_status = docsis_GetCert(value);
        printf("Return status of docsis_GetCert %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetCharParamValues : Failed to get Cert info\n");
            return SSP_FAILURE;
        }
    }
    else
    {
         printf("Invalid parameter name");
	 return_status = SSP_FAILURE;
    }
    return return_status;

}


/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_GetParamUlongValue
 * Description          : This function will invoke the hal api of CM to get the ulong values
 *
 * @param [in]          :  paramName: specifies the name of the API
                           value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CMHAL_GetParamUlongValue(char* paramName, unsigned long* value)
{
    int return_status = 0;
    CMMGMT_CM_DHCP_INFO v4dhcpinfo;
    CMMGMT_CM_IPV6DHCP_INFO v6dhcpinfo;
    CMMGMT_CM_EventLogEntry_t entryArray[50];
    printf("\nEntering ssp_CMHAL_GetParamUlongValue function\n\n");
    if( !(strcmp(paramName, "DownFreq")) )
    {
        *value = docsis_GetDownFreq();
        printf("ssp_CMHAL_GetParamUlongValue:DownFreq is %lu", *value);

        if ( *value == 0)
        {
            printf("ssp_CMHAL_GetParamUlongValue : Failed to get the Down Frequency\n");
            return_status =SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "NumberofActiveRxChannels")) )
    {
        return_status = docsis_GetNumOfActiveRxChannels(value);
        printf("Return status of docsis_GetNumOfActiveRxChannels %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetParamCharValue : Failed to get NumberofActiveRxChannels\n");
            return_status =SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "NumberofActiveTxChannels")) )
    {
        return_status = docsis_GetNumOfActiveTxChannels(value);
        printf("Return status of docsis_GetNumOfActiveTxChannels %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetCharValue : Failed to get NumberofActiveRxChannels\n");
            return_status =SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "Ipv4DhcpIPAddress")) )
    {
        if(value)
        {
            return_status = cm_hal_GetDHCPInfo(&v4dhcpinfo);
	    printf("ssp_CMHal_GetParamUlongValue: IPAddress retreived :%lu\n",(long unsigned int)v4dhcpinfo.IPAddress.Value);
            *value = v4dhcpinfo.IPAddress.Value;
        }
        else
            return_status = cm_hal_GetDHCPInfo((PCMMGMT_CM_DHCP_INFO)value);
        
    }
    else if( !(strcmp(paramName, "LeaseTimeRemaining")) )
    {
        if(value)
        {
            return_status = cm_hal_GetDHCPInfo(&v4dhcpinfo);
            printf("ssp_CMHal_GetParamUlongValue: LeaseTimeRemaining retreived :%lu\n",v4dhcpinfo.LeaseTimeRemaining);
            *value = v4dhcpinfo.LeaseTimeRemaining;
        }
        else
            return_status = cm_hal_GetDHCPInfo((PCMMGMT_CM_DHCP_INFO)value);
    }
    else if( !(strcmp(paramName, "IPv6LeaseTimeRemaining")) )
    {
        if(value)
        {
            return_status = cm_hal_GetIPv6DHCPInfo(&v6dhcpinfo);
            printf("ssp_CMHAL_GetParamCharValue: IPv6LeaseTimeRemaining retreived :%lu\n",v6dhcpinfo.IPv6LeaseTimeRemaining);
            *value = v6dhcpinfo.IPv6LeaseTimeRemaining;
        }
        else
            return_status = cm_hal_GetIPv6DHCPInfo((PCMMGMT_CM_IPV6DHCP_INFO)value);
    }

    else if( !(strcmp(paramName, "IPv6RebindTimeRemaining")) )
    {
        if(value)
        {
            return_status = cm_hal_GetIPv6DHCPInfo(&v6dhcpinfo);
            printf("ssp_CMHAL_GetParamCharValue: IPv6RebindTimeRemaining retreived :%lu\n",v6dhcpinfo.IPv6RebindTimeRemaining);
            *value = v6dhcpinfo.IPv6RebindTimeRemaining;
        }
        else
            return_status = cm_hal_GetIPv6DHCPInfo((PCMMGMT_CM_IPV6DHCP_INFO)value);
    }
      else if( !(strcmp(paramName, "IPv6RenewTimeRemaining")) )
    {
        if(value)
        {
            return_status = cm_hal_GetIPv6DHCPInfo(&v6dhcpinfo);
            printf("ssp_CMHAL_GetParamCharValue: IPv6RenewTimeRemaining retreived :%lu\n",v6dhcpinfo.IPv6RenewTimeRemaining);
            *value = v6dhcpinfo.IPv6RenewTimeRemaining;
        }
        else
            return_status = cm_hal_GetIPv6DHCPInfo((PCMMGMT_CM_IPV6DHCP_INFO)value);
    }
    else if( !(strcmp(paramName, "CertStatus")) )
    {
        return_status = docsis_GetCertStatus(value);
        printf("Return status of docsis_GetCertStatus %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetParamUlongValue : Failed to get CertStatus\n");
            return_status =SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "USChannelId")) )
    {
	*value = -1;
        *value = docsis_GetUSChannelId();
        printf("ssp_CMHAL_GetParamUlongValue:US Channel id is %lu", *value);

        if ( *value == -1)
        {
            printf("ssp_CMHAL_GetParamUlongValue : Failed to get the US Channel ID\n");
            return_status =SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "DownloadInterface")) )
    {
        return_status = cm_hal_Get_HTTP_Download_Interface((unsigned int*)value);
        printf("Return status of cm_hal_Get_HTTP_Download_Interface %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetParamCharValue : Failed to get cm_hal_Get_HTTP_Download_Interface\n");
            return_status =SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "EventLogItemsCount")) )
    {
       memset(entryArray, 0, 50*sizeof(CMMGMT_CM_EventLogEntry_t));
       *value = docsis_GetDocsisEventLogItems(entryArray,50);
       if(value)
       {
           printf("ssp_CMHal_GetParamUlongValue: Number of Docsis Event log items:%lu\n",*value);
           return_status = SSP_SUCCESS;
       }
       else
       {
           return_status =SSP_FAILURE;
       }
    }
    else if( !(strcmp(paramName, "CableModemResetCount")) )
    {
        return_status = cm_hal_Get_CableModemResetCount(value);
        printf("Return status of cm_hal_Get_CableModemResetCount %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetParamUlongValue: Failed to get CableModemResetCount\n");
            return_status =SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "LocalResetCount")) )
    {
        return_status = cm_hal_Get_LocalResetCount(value);
        printf("Return status of cm_hal_Get_LocalResetCount %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetParamUlongValue: Failed to get LocalResetCount\n");
            return_status =SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "DocsisResetCount")) )
    {
        return_status = cm_hal_Get_DocsisResetCount(value);
        printf("Return status of cm_hal_Get_DocsisResetCount %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetParamUlongValue: Failed to get DocsisResetCount\n");
            return_status =SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "ErouterResetCount")) )
    {
        return_status = cm_hal_Get_ErouterResetCount(value);
        printf("Return status of cm_hal_Get_ErouterResetCount %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetParamUlongValue: Failed to get ErouterResetCount\n");
            return_status =SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "Reboot_Ready")) )
    {
        return_status = cm_hal_Reboot_Ready(value);
        printf("Return status of cm_hal_Reboot_Ready %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_CMHAL_GetParamUlongValue: Failed to get cm_hal_Reboot_Ready");
            return_status =SSP_FAILURE;
        }
    }
    else if(!(strcmp(paramName, "HTTP_Download_Status")))
    {
       *value = cm_hal_Get_HTTP_Download_Status();
        printf("ssp_CMHAL_GetParamUlongValue:Download status is %lu", *value);
    }
    else
    {
        printf("Invalid parameter name");
        return_status =SSP_FAILURE;
    }
    return return_status;

}

/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_GetErrorCodeWords
 * Description          : This function will invoke the hal api of CM to get the error code words
 *
 * @param [in]          :  isNegativeScenario : for executing negative scenario
                           value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CMHAL_GetErrorCodeWords(char *value, int isNegativeScenario)
{
    int return_status = 0;
    int i=0;
    PCMMGMT_CM_ERROR_CODEWORDS perrorcodes = NULL;
    long unsigned int  count = 0;
    printf("\nEntering ssp_CMHAL_GetErrorCodeWords function\n\n");

    if(isNegativeScenario)
    {
        printf("Executing negative scenario\n");
        return_status = docsis_GetErrorCodewords(NULL);
    }
    else
    {
        printf("Executing positive scenario\n");

        return_status = docsis_GetNumOfActiveRxChannels(&count);
        printf("Count of Active Rx channels is %lu\n",count);
        if (return_status == 0)
        {
            perrorcodes = (PCMMGMT_CM_ERROR_CODEWORDS) malloc(sizeof(CMMGMT_CM_ERROR_CODEWORDS)*count);

            if(!perrorcodes)
            {
                printf("Memory has not allocated successfully \n ");
		return_status = SSP_FAILURE;
            }
            else
            {
                return_status = docsis_GetErrorCodewords(&perrorcodes);
                printf("Return status of docsis_GetErrorCodewords: %d\n",return_status);
                strcpy(value,"");
                for (i=0;i<count;i++)
                {
                    printf("UnerroredCodewords :%lu, CorrectableCodewords :%lu, UncorrectableCodewords :%lu\n",perrorcodes[i].UnerroredCodewords,perrorcodes[i].CorrectableCodewords,perrorcodes[i].UncorrectableCodewords);
                    char str[64]= {0};
                    sprintf(str,"%lu,%lu,%lu",perrorcodes[i].UnerroredCodewords,perrorcodes[i].CorrectableCodewords,perrorcodes[i].UncorrectableCodewords);
                    strcat(value,str);
                    strcat(value," ");
                }
            }
        }
    }
    if(perrorcodes != NULL)
    {
       free(perrorcodes);
    }

    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_Init
 * Description          : This function will invoke the hal api of CM to init the CM
 *
 * @param [in]          :  paramName: specifies the name of the API

 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_Init(char* paramName)
{
    int return_status = 0;
    printf("\nEntering ssp_CMHAL_Init function\n\n");

    if( !(strcmp(paramName, "InitDB")) )
    {
        return_status = cm_hal_InitDB();
        printf("Return status of cm_hal_InitDB %d", return_status);
    }
    else if( !(strcmp(paramName, "InitDS")) )
    {
        return_status = docsis_InitDS();
        printf("Return status of docsis_InitDS %d", return_status);
    }
    else if( !(strcmp(paramName, "InitUS")) )
    {
        return_status = docsis_InitUS();
        printf("Return status of docsis_InitUS %d", return_status);
    }
    else if( !(strcmp(paramName, "ReinitMac")) )
    {
        return_status = cm_hal_ReinitMac();
        printf("Return status of cm_hal_ReinitMac %d", return_status);
    }
    else
    {
         printf("Invalid parameter name");
         return_status = SSP_FAILURE;
    }
    return return_status;
}

/*****************************************************************************************************************
 * Function Name : ssp_CMHAL_GetDocsisEventLogItems
 * Description   : This function will Retrieve the DocsisEventLogItems
 * @param [in]   : entryArray - to get  the event log items
 *		    len- length of array
 *		   isNegativeScenario - to execute the negative scenarios
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_CMHAL_GetDocsisEventLogItems(CMMGMT_CM_EventLogEntry_t *entryArray,int len,int isNegativeScenario)
{
       int result = RETURN_ERR;
       int count =0;
       int i =0;

       printf("Entering the ssp_CMHAL_GetDocsisEventLogItems wrapper\n");

       if(isNegativeScenario)
       {
           result = docsis_GetDocsisEventLogItems(NULL, 0);
       }
       else
       {
          memset(entryArray, 0, len*sizeof(CMMGMT_CM_EventLogEntry_t));
          count = docsis_GetDocsisEventLogItems(entryArray,len);
          printf("Count is %d\n",count);
              for (i=0;i<count;i++)
              {
		 printf("Time: %s,EventID: %d,EventLevel : %d, Description:%s",ctime(&(entryArray[i].docsDevEvFirstTime.tv_sec)), entryArray[i].docsDevEvId, entryArray[i].docsDevEvLevel, entryArray[i].docsDevEvText);
                 result = RETURN_OK;
              }
        }

        if(result == RETURN_OK)
        {
           printf("ssp_CMHAL_GetDocsisEventLogItems function returns success\n");
        }
        return result;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_SetLEDFlashStatus
 * Description          : This function will invoke the hal api of cm_hal_HTTP_LED_Flash() to enable/disable LED Flash
 *
 * @param [in]          :  LedFlash: specifies enable/disable status
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_SetLEDFlashStatus(BOOLEAN LedFlash)
{
    int return_status = 0;
    printf("\nEntering ssp_CMHAL_SetLEDFlashStatus function\n\n");

    return_status = cm_hal_HTTP_LED_Flash(LedFlash);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_CMHAL_SetLEDFlashStatus::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_CMHAL_SetLEDFlashStatus::Success\n");
     return SSP_SUCCESS;
    }
}

/*****************************************************************************************************************
 * Function Name : ssp_CMHAL_ClearDocsisEventLog
 * Description   : This function will clear the docsis event log
 * @param [in]   : None
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_CMHAL_ClearDocsisEventLog(void)
{
       int result = RETURN_ERR;
       printf("Entering the ssp_CMHAL_ClearDocsisEventLog wrapper\n");
       result = docsis_ClearDocsisEventLog();
       printf("result is %d\n",result);
       if(result == RETURN_OK)
       {
          printf("ssp_CMHAL_ClearDocsisEventLog function returns success\n");
       }
       else
       {
          printf("ssp_CMHAL_ClearDocsisEventLog function returns failure\n");
       }

       return result;
}

/********************************************************************************************************************************
 *
 * Function Name        : ssp_CMHAL_GetCPEList
 * Description          : This function will invoke the hal api of cm_hal_GetCPEList to get the list of CPEs connected to the CM
 *
 * @param [in]          : InstanceNum : To save the instance number
 *			  cpeList : To save the cpeList
 *			  isNegativeScenario : To execute the negative scenario
                          lanMode :  The lan mode in which device is currently operational
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************************************************/
int ssp_CMHAL_GetCPEList(unsigned long int *InstanceNum, char *cpeList, char *lanMode,int isNegativeScenario)
{
       int result = RETURN_ERR;
       int return_status = RETURN_ERR;
       PCMMGMT_DML_CPE_LIST pInfo = NULL;
       int i =0;
       printf("Entering the ssp_CMHAL_GetCPEList wrapper\n");
       if(isNegativeScenario)
       {
           result = cm_hal_GetCPEList(NULL, NULL, NULL);
       }
       else
       {
          printf("Executing positive scenarios\n");
          result = cm_hal_GetCPEList(&pInfo,InstanceNum,lanMode);
          printf("Result is %d, InstanceNum is :%lu, LanMode is :%s\n",result,*InstanceNum,lanMode);
          if (result == RETURN_OK)
          {
              printf("cm_hal_GetCPEList returns success\n");
              if(*InstanceNum > 0)
              {
                printf("inst num is greater than zero\n");
                strcpy(cpeList,"");
                for (i=0;i<*InstanceNum;i++)
                  {
                     printf("IPaddress: %s, MACAddress: %s \n",pInfo[i].IPAddress,pInfo[i].MACAddress);
                     strcat(cpeList,pInfo[i].IPAddress);
                     strcat(cpeList,",");
                     strcat(cpeList,pInfo[i].MACAddress);
                     strcat(cpeList,"::");
                     printf("cpeList:%s\n",cpeList);
                     return_status = RETURN_OK;
                  }
              }
              else{ printf("Instance number is not greater than zero\n");}
           }
           else{ printf("cm_hal_GetCPEList returns failure\n");}
        }
        if(return_status == RETURN_OK)
        {
           printf("ssp_CMHAL_GetDocsisEventLogItems function returns success\n");
        }
        return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_SetMddIpModeOverride
 * Description          : This function will invoke the hal api of docsis_SetMddIpModeOverride to set MddIPModeOverride
 *
 * @param [in]          :  Value : The value of MddIpModeOverride to set
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_SetMddIpModeOverride(char* Value)
{
    int return_status = 0;
    printf("\nEntering ssp_CMHAL_SetMddIpModeOverride function\n");
    return_status = docsis_SetMddIpModeOverride(Value);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_CMHAL_SetMddIpModeOverride::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_CMHAL_SetMddIpModeOverride::Success\n");
     return SSP_SUCCESS;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_SetStartFreq
 * Description          : This function will invoke the cosa api of CM to set
 *                        start frequency
 *
 * @param [in]          : Value - The value to set
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
 int ssp_CMHAL_SetStartFreq(unsigned long int Value)
{
    //Since the api is a void function, validation of this function is done inside the python scripts
    printf("\n Entering ssp_CMHAL_SetStartFreq function\n");
    docsis_SetStartFreq(Value);
    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_SetUSChannelId
 * Description          : This function will invoke the cosa api of CM to set
 *                        USChannelId
 *
 * @param [in]          : Value - The value to set
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
 int ssp_CMHAL_SetUSChannelId(int Value)
{
    printf(" Entering ssp_CMHAL_SetUSChannelId function\n");
    //Since the api is a void function, validation of this function is done inside the python scripts
    docsis_SetUSChannelId(Value);
    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_SetHTTP_Download_Interface
 * Description          : This function will invoke the hal api of cm_hal_Set_HTTP_Download_Interface()
 *
 * @param [in]          : interface - The value of download interface to set
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_SetHTTP_Download_Interface(unsigned int interface)
{
    int return_status = 0;
    printf("\nEntering ssp_CMHAL_SetHTTP_Download_Interface function\n\n");

    return_status = cm_hal_Set_HTTP_Download_Interface(interface);
    printf("\n return_status of cm_hal_Set_HTTP_Download_Interface: %d",return_status);

    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_CMHAL_SetHTTP_Download_Interface::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_CMHAL_SetHTTP_Download_Interface::Success\n");
     return SSP_SUCCESS;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_Download
 * Description          : This function will invoke the hal api of cm_hal_HTTP_Download() to start the download
 *
 * @param [in]          : None
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_Download()
{
    int return_status = 0;
    printf("\nEntering ssp_CMHAL_Download function\n\n");

    return_status = cm_hal_HTTP_Download();
    printf("return_status of cm_hal_HTTP_Download is %d",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_CMHAL_Download::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_CMHAL_Download::Success\n");
     return SSP_SUCCESS;
    }
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_Reboot_Now
 * Description          : This function will invoke the hal api of cm_hal_HTTP_Download_Reboot_Now() to start the reboot
 *
 * @param [in]          : None
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_Reboot_Now()
{
    int return_status = 0;
    printf("\nEntering ssp_CMHAL_Reboot_Now function\n\n");

    return_status = cm_hal_HTTP_Download_Reboot_Now();
    printf("return_status of cm_hal_HTTP_Download_Reboot_Now is %d",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_CMHAL_Reboot_Now::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_CMHAL_Reboot_Now::Success\n");
     return SSP_SUCCESS;
    }
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_GetHTTP_Download_Url
 * Description          : This function will invoke the hal api of CM to get the HTTP_Download_Url
 *
 * @param [in]          : httpURL : The URL of site from which the file should download
                          filename: The name of the file which is to be download
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_GetHTTP_Download_Url(char* httpURL, char* filename)
{
    int return_status = 0;
    printf("\nEntering ssp_CMHAL_GetHTTP_Download_Url function\n\n");
    return_status = cm_hal_Get_HTTP_Download_Url(httpURL,filename);
    printf("Return status of cm_hal_Get_HTTP_Download_Url %d", return_status);
    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CMHAL_GetHTTP_Download_Url :Failed to get the HTTP_Download_Url\n");
        return SSP_FAILURE;
    }
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_SetHTTP_Download_Url
 * Description          : This function will invoke the hal api of cm_hal_Set_HTTP_Download_Url
 *
 * @param [in]          :  Value : The value of HTTP_Download_Url to set
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_SetHTTP_Download_Url(char* httpURL, char* filename)
{
    int return_status = 0;
    printf("\nEntering ssp_CMHAL_SetHTTP_Download_Url function\n");

    return_status = cm_hal_Set_HTTP_Download_Url(httpURL,filename);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_CMHAL_SetHTTP_Download_Url::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_CMHAL_SetHTTP_Download_Url::Success\n");
     return SSP_SUCCESS;
    }
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_FWupdateAndFactoryReset
 * Description          : This function will invoke the hal api of cm_hal_FWupdateAndFactoryReset()
 *
 * @param [in]          : None
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_FWupdateAndFactoryReset(char* url, char* name)
{
    int return_status = 0;
    printf("\nEntering ssp_CMHAL_FWupdateAndFactoryReset function\n\n");
    printf("\nssp_CMHAL_FWupdateAndFactoryReset URL is %s and image name is %s \n\n",url,name);

    return_status = cm_hal_FWupdateAndFactoryReset(url,name);

    printf("return_status of cm_hal_FWupdateAndFactoryReset is %d",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_CMHAL_FWupdateAndFactoryReset::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_CMHAL_FWupdateAndFactoryReset::Success\n");
     return SSP_SUCCESS;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_GetDsOfdmChanTable
 * Description          : This function will invoke the hal api of CM to get the char values
 *
 * @param [in]          : paramName: specifies the name of the API
                          value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_GetDsOfdmChanTable(char* paramName, char* value, int *numberofEntries)
{
    int return_status = 0;
    PDOCSIF31_CM_DS_OFDM_CHAN pDsOfdmDetails = {0};
    printf("\nEntering ssp_CMHAL_GetDsOfdmChanTable function\n\n");
    int i =0;
    if (numberofEntries)
    {
       strcpy(value, "");
       return_status = docsis_GetDsOfdmChanTable(&pDsOfdmDetails,numberofEntries);
       printf("ssp_CMHAL_GetDsOfdmChanTable: no of entries in table:%d\n",*numberofEntries);
       printf("return status is %d",return_status);
       if (*numberofEntries==0)
          return_status =0;
       else if (return_status == 0 && *numberofEntries>0)
       {
            if( !(strcmp(paramName, "DS_OFDM_ChannelId")) )
            {
               for(i=0;i<*numberofEntries;i++)
               {
                  printf("ssp_CMHAL_GetDsOfdmChanTable: DS OFDM ChannelID retreived :%d\n",pDsOfdmDetails[i].ChannelId);
                  sprintf(value,"%d",pDsOfdmDetails[i].ChannelId);
                  strcat(value, ",");
               }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_ChannelIndicator")) )
            {
	        for(i=0;i<*numberofEntries;i++)
                {
		   printf("ssp_CMHAL_GetParamCharValue: DS OFDM Channel Indicator retrieved :%d\n",pDsOfdmDetails[i].ChanIndicator);
                   sprintf(value,"%d",pDsOfdmDetails[i].ChanIndicator);
                   strcat(value, ",");
                }
	    }
            else if( !(strcmp(paramName, "DS_OFDM_FirstActiveSubcarrierNum")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetParamCharValue:  Number of FirstActiveSubcarrier retrieved :%d\n",pDsOfdmDetails[i].FirstActiveSubcarrierNum);
                    sprintf(value,"%d",pDsOfdmDetails[i].FirstActiveSubcarrierNum);
                    strcat(value, ",");
                 }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_LastActiveSubcarrierNum")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetParamCharValue:  Number of LastActiveSubcarrier retrieved :%d\n",pDsOfdmDetails[i].LastActiveSubcarrierNum);
                    sprintf(value,"%d",pDsOfdmDetails[i].LastActiveSubcarrierNum);
                    strcat(value, ",");
                 }
            }  
	    else if( !(strcmp(paramName, "DS_OFDM_NumActiveSubcarriers")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetParamCharValue:  Number of ActiveSubcarrier retrieved :%d\n",pDsOfdmDetails[i].NumActiveSubcarriers);
                    sprintf(value,"%d",pDsOfdmDetails[i].NumActiveSubcarriers);
                    strcat(value, ",");
                 }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_SubcarrierSpacing")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetParamCharValue:  SubcarrierSpacing retrieved :%d\n",pDsOfdmDetails[i].SubcarrierSpacing);
                    sprintf(value,"%d",pDsOfdmDetails[i].SubcarrierSpacing);
                    strcat(value, ",");
                 }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_CyclicPrefix")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                     printf("ssp_CMHAL_GetParamCharValue:  OFDM CyclicPrefix retrieved :%d\n",pDsOfdmDetails[i].CyclicPrefix);
                     sprintf(value,"%d",pDsOfdmDetails[i].CyclicPrefix);
                     strcat(value, ",");
                 }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_RollOffPeriod")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetParamCharValue:  OFDM RollOffPeriod retrieved :%d\n",pDsOfdmDetails[i].RollOffPeriod);
                    sprintf(value,"%d",pDsOfdmDetails[i].RollOffPeriod);
                    strcat(value, ",");
                 }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_PlcFreq")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetParamCharValue:  OFDM PlcFreq retrieved :%d\n",pDsOfdmDetails[i].PlcFreq);
                    sprintf(value,"%d",pDsOfdmDetails[i].PlcFreq);
                    strcat(value, ",");
                 }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_NumPilots")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                     printf("ssp_CMHAL_GetParamCharValue:  OFDM NumPilots retrieved :%d\n",pDsOfdmDetails[i].NumPilots);
                     sprintf(value,"%d",pDsOfdmDetails[i].NumPilots);
                     strcat(value, ",");
                 }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_TimeInterleaverDepth")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                     printf("ssp_CMHAL_GetParamCharValue:  OFDM TimeInterleaverDepth retrieved :%d\n",pDsOfdmDetails[i].TimeInterleaverDepth);
                     sprintf(value,"%d",pDsOfdmDetails[i].TimeInterleaverDepth);
                     strcat(value, ",");
                 }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_PlcTotalCodewords")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetParamCharValue:  OFDM PlcTotalCodewords retrieved :%llu\n",pDsOfdmDetails[i].PlcTotalCodewords);
                    sprintf(value,"%llu",pDsOfdmDetails[i].PlcTotalCodewords);
                    strcat(value, ",");
                 }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_PlcUnreliableCodewords")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                     printf("ssp_CMHAL_GetParamCharValue:  OFDM PlcUnreliableCodewords retrieved :%llu\n",pDsOfdmDetails[i].PlcUnreliableCodewords);
                     sprintf(value,"%llu",pDsOfdmDetails[i].PlcUnreliableCodewords);
                     strcat(value, ",");
                 }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_NcpTotalFields")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetParamCharValue:  OFDM NcpTotalFields retrieved :%llu\n",pDsOfdmDetails[i].NcpTotalFields);
                    sprintf(value,"%llu",pDsOfdmDetails[i].NcpTotalFields);
                    strcat(value, ",");
                 }
            }
	    else if( !(strcmp(paramName, "DS_OFDM_NcpFieldCrcFailures")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetParamCharValue:  OFDM NcpFieldCrcFailures retrieved :%llu\n",pDsOfdmDetails[i].NcpFieldCrcFailures);
                    sprintf(value,"%llu",pDsOfdmDetails[i].NcpFieldCrcFailures);
                    strcat(value, ",");
                 }
            }
	
            else
            {
                 printf("Invalid parameter name");
                 return_status = SSP_FAILURE;
            }
       }
       else
           printf("\ndocsis_GetDsOfdmChanTable returns failure\n\n");
   }
   else
   {
       return_status = docsis_GetDsOfdmChanTable(NULL,NULL);
       printf("docsis_GetDsOfdmChanTable return status is %d",return_status);
   }
   return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_GetUsOfdmChanTable
 * Description          : This function will invoke the hal api of CM to get the char values
 *
 * @param [in]          : paramName: specifies the name of the API
                          value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_GetUsOfdmChanTable(char* paramName, char* value, int *numberofEntries)
{
    int return_status = 0;
    PDOCSIF31_CM_US_OFDMA_CHAN pUsOfdmDetails = {0};
    printf("\nEntering ssp_CMHAL_GetUsOfdmChanTable function\n\n");
    int i =0;
    strcpy(value, "");
    if (numberofEntries)
    {
        return_status = docsis_GetUsOfdmaChanTable(&pUsOfdmDetails,numberofEntries);
        printf("ssp_CMHAL_GetUsOfdmChanTable: no of entries in table:%d\n",*numberofEntries);
        printf("return status is %d",return_status);    
        if (*numberofEntries==0)
	   return_status =0;
        else if (return_status == 0 && *numberofEntries>0)
        {
           if( !(strcmp(paramName, "US_OFDM_ChannelId")) )
           {
              for(i=0;i<*numberofEntries;i++)
              {
                printf("ssp_CMHAL_GetUsOfdmChanTable: US OFDM ChannelID retreived :%d\n",pUsOfdmDetails[i].ChannelId);
                sprintf(value,"%d",pUsOfdmDetails[i].ChannelId);
                strcat(value, ",");
              }
           }     
	   else if( !(strcmp(paramName, "US_OFDM_FirstActiveSubcarrierNum")) )
           {
                for(i=0;i<*numberofEntries;i++)
                {
                   printf("ssp_CMHAL_GetUsOfdmChanTable: US OFDM FirstActiveSubcarrier retrieved :%d\n",pUsOfdmDetails[i].FirstActiveSubcarrierNum);
                   sprintf(value,"%d",pUsOfdmDetails[i].FirstActiveSubcarrierNum);
                   strcat(value, ",");
                }
           } 
	   else if( !(strcmp(paramName, "US_OFDM_LastActiveSubcarrierNum")) )
           {
                for(i=0;i<*numberofEntries;i++)
                {
                   printf("ssp_CMHAL_GetUsOfdmChanTable: US OFDM LastActiveSubcarrier retrieved :%d\n",pUsOfdmDetails[i].LastActiveSubcarrierNum);
                   sprintf(value,"%d",pUsOfdmDetails[i].LastActiveSubcarrierNum);
                   strcat(value, ",");
                }
           }
	   else if( !(strcmp(paramName, "US_OFDM_ActiveSubcarriers")) )
           {
                for(i=0;i<*numberofEntries;i++)
                {
                    printf("ssp_CMHAL_GetUsOfdmChanTable: US OFDM ActiveSubcarriers retrieved :%d\n",pUsOfdmDetails[i].NumActiveSubcarriers);
                    sprintf(value,"%d",pUsOfdmDetails[i].NumActiveSubcarriers);
                    strcat(value, ",");
                }
           }
	   else if( !(strcmp(paramName, "US_OFDM_SubcarrierSpacing")) )
           {
                for(i=0;i<*numberofEntries;i++)
                {
                    printf("ssp_CMHAL_GetUsOfdmChanTable: US OFDM SubcarrierSpacing retrieved :%d\n",pUsOfdmDetails[i].SubcarrierSpacing);
                    sprintf(value,"%d",pUsOfdmDetails[i].SubcarrierSpacing);
                    strcat(value, ",");
                }
           }
	   else if( !(strcmp(paramName, "US_OFDM_CyclicPrefix")) )
           {
                for(i=0;i<*numberofEntries;i++)
                {
                    printf("ssp_CMHAL_GetUsOfdmChanTable: US OFDM CyclicPrefix retrieved :%d\n",pUsOfdmDetails[i].CyclicPrefix);
                    sprintf(value,"%d",pUsOfdmDetails[i].CyclicPrefix);
                    strcat(value, ",");
                }
           }
	   else if( !(strcmp(paramName, "US_OFDM_RollOffPeriod")) )
           {
                for(i=0;i<*numberofEntries;i++)
                {
                    printf("ssp_CMHAL_GetUsOfdmChanTable: US OFDM RollOffPeriod retrieved :%d\n",pUsOfdmDetails[i].RollOffPeriod);
                    sprintf(value,"%d",pUsOfdmDetails[i].RollOffPeriod);
                    strcat(value, ",");
                }
           }
	   else if( !(strcmp(paramName, "US_OFDM_NumSymbolsPerFrame")) )
           { 
                for(i=0;i<*numberofEntries;i++)
                {
                    printf("ssp_CMHAL_GetUsOfdmChanTable: US OFDM NumSymbolsPerFrame retrieved :%d\n",pUsOfdmDetails[i].NumSymbolsPerFrame);
                    sprintf(value,"%d",pUsOfdmDetails[i].NumSymbolsPerFrame);
                    strcat(value, ",");
                }
           }
	   else if( !(strcmp(paramName, "US_OFDM_TxPower")) )
           {
                for(i=0;i<*numberofEntries;i++)
                {
                    printf("ssp_CMHAL_GetUsOfdmChanTable: US OFDM TxPower retrieved :%d\n",pUsOfdmDetails[i].TxPower);
                    sprintf(value,"%d",pUsOfdmDetails[i].TxPower);
                    strcat(value, ",");
                }
           }
	   else if( !(strcmp(paramName, "US_OFDM_PreEqEnabled")) )
           {
                for(i=0;i<*numberofEntries;i++)
                {
                   printf("ssp_CMHAL_GetUsOfdmChanTable: US OFDM PreEqEnabled retrieved :%d\n",pUsOfdmDetails[i].PreEqEnabled);
                   sprintf(value,"%d",pUsOfdmDetails[i].PreEqEnabled);
                   strcat(value, ",");
                }
           }
           else
           {
               printf("Invalid parameter name");
               return_status = SSP_FAILURE;
           }
        }
        else
        printf("\ndocsis_GetUsOfdmChanTable returns failure\n\n");
    }
    else
    {
        return_status =docsis_GetUsOfdmaChanTable(NULL,NULL);
        printf("docsis_GetUsOfdmaChanTable return status is %d",return_status);
    }
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_GetStatusOfdmaUsTable
 * Description          : This function will invoke the hal api of CM to get the char values
 *
 * @param [in]          : paramName: specifies the name of the API
                          value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_GetStatusOfdmaUsTable(char* paramName, char* value, int *numberofEntries)
{
    int return_status = 0;
    PDOCSIF31_CMSTATUSOFDMA_US pdmaUsTableStatus = {0};
    printf("\nssp_CMHAL_GetStatusOfdmaUsTable function\n\n");

    int i =0;
    strcpy(value, "");
   
    if (numberofEntries)
    {
       return_status = docsis_GetStatusOfdmaUsTable(&pdmaUsTableStatus,numberofEntries);
       printf("ssp_CMHAL_GetStatusOfdmaUsTable: no of entries in table:%d\n",*numberofEntries);

       printf("return status is %d",return_status);
       if (*numberofEntries==0)
        return_status =0;
       else if (return_status == 0 && *numberofEntries>0)
       {
            if( !(strcmp(paramName, "USTable_Numberofentries")) )
            {
                for(i=0;i<*numberofEntries;i++)
                {
                   printf("ssp_CMHAL_GetStatusOfdmaUsTable: USTable ChannelID Status  retreived :%d\n",pdmaUsTableStatus[i].ChannelId);
                   sprintf(value,"%d",pdmaUsTableStatus[i].ChannelId);
                   strcat(value, ",");
                }
            }
            else if( !(strcmp(paramName, "USTable_T3Timeouts_Status")) )
            {
                for(i=0;i<*numberofEntries;i++)
                {
                    printf("ssp_CMHAL_GetStatusOfdmaUsTable: USTable T3Timeouts Status retrieved :%d\n",pdmaUsTableStatus[i].T3Timeouts);
                    sprintf(value,"%d",pdmaUsTableStatus[i].T3Timeouts);
                    strcat(value, ",");
                }
            }
            else if( !(strcmp(paramName, "USTable_T4Timeouts_Status")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetStatusOfdmaUsTable: USTable T4Timeouts Status retrieved :%d\n",pdmaUsTableStatus[i].T4Timeouts);
                    sprintf(value,"%d",pdmaUsTableStatus[i].T4Timeouts);
                    strcat(value, ",");
                 }
            }
            else if( !(strcmp(paramName, "USTable_RangingAborteds_Status")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                     printf("ssp_CMHAL_GetStatusOfdmaUsTable: USTable RangingAborteds Status retrieved :%d\n",pdmaUsTableStatus[i].RangingAborteds);
                     sprintf(value,"%d",pdmaUsTableStatus[i].RangingAborteds);
                     strcat(value, ",");
                 }
            }
            else if( !(strcmp(paramName, "USTable_T3Exceededs_Status")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetStatusOfdmaUsTable: USTable T3Exceededs Status retrieved :%d\n",pdmaUsTableStatus[i].T3Exceededs);
                    sprintf(value,"%d",pdmaUsTableStatus[i].T3Exceededs);
                    strcat(value, ",");
                 }
            }
            else if( !(strcmp(paramName, "USTable_IsMuted_Status")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetStatusOfdmaUsTable: USTable IsMuted Status retrieved :%d\n",pdmaUsTableStatus[i].IsMuted);
                    sprintf(value,"%d",pdmaUsTableStatus[i].IsMuted);
                    strcat(value, ",");
                 }
            }
            else if( !(strcmp(paramName, "USTable_RangingStatus_Status")) )
            {
                 for(i=0;i<*numberofEntries;i++)
                 {
                    printf("ssp_CMHAL_GetStatusOfdmaUsTable: USTable RangingStatus Status retrieved :%d\n",pdmaUsTableStatus[i].RangingStatus);
                    sprintf(value,"%d",pdmaUsTableStatus[i].RangingStatus);
                    strcat(value, ",");
                 }
            }
            else
            {
                 printf("Invalid parameter name");
                 return_status = SSP_FAILURE;
            }
       }
       else
           printf("\ndocsis_GetDsOfdmChanTable returns failure\n\n");
    }
    else
    {  
        return_status = docsis_GetStatusOfdmaUsTable(NULL,NULL);
        printf("docsis_GetStatusOfdmaUsTable return status is %d",return_status);
    }
    return return_status;

}

/*******************************************************************************************
 *
 * Function Name        : ssp_CMHAL_IsEnergyDetected
 * Description          : This function will invoke the hal api of CM to get the Engery Detected status
 *
 * @param [in]          : energyDetected: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CMHAL_IsEnergyDetected(char* energyDetected)
{
    printf("ssp_CMHAL_IsEnergyDetected Function Entry \n");
    int return_status = 0;
    return_status = docsis_IsEnergyDetected(energyDetected);
    if(SSP_SUCCESS == return_status)
    {
        if(energyDetected != NULL)
        {
            printf("energyDetected = %s\n",energyDetected);
            return SSP_SUCCESS;
        }
        else
        {
            printf("energyDEtected is NULL");
            return SSP_FAILURE;
        }
    }
    else
    {
        printf("Call docsis_IsEnergyDetected returns error");
        return SSP_FAILURE;
    }
}
