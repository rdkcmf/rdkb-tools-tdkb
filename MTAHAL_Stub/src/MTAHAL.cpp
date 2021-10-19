/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2018 RDK Management
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

#include "MTAHAL.h"

/***************************************************************************
 * Function name : initialize
 * Description   : Initialize Function will be used for registering the wrapper method
 *                 with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/

bool MTAHAL::initialize(IN const char* szVersion)
{
    return TEST_SUCCESS;
}

/***************************************************************************
 * Function name : testmodulepre_requisites
 * Description   : testmodulepre_requisites will  be used for setting the
 *                 pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string MTAHAL::testmodulepre_requisites()
{
    return "SUCCESS";
}


/***************************************************************************
 * Function name : testmodulepost_requisites
 * Description   : testmodulepost_requisites will be used for resetting the
 *                 pre-requisites that are set
 *
 *****************************************************************************/
bool MTAHAL::testmodulepost_requisites()
{
    DEBUG_PRINT(DEBUG_LOG,"DBG:MTAHAL:testmodulepost_requisites() \n");
    return 0;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetParamCharValue
 * Description   : This will get the char values
 * @param [in]   : req - paramName : Holds the name of api
 *                 req - value     : Holds char value
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void MTAHAL::MTAHAL_GetParamCharValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetParamCharValue ---> Entry \n");

    int returnValue = 0;
    char paramName[100] = {'\0'};
    char Details[1024] = {'\0'};
    char value[1024] = {'\0'};
    int isNegativeScenario = 0;
    /* Validate the input arguments */

    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }
    
    strcpy(paramName,req["paramName"].asCString());

    if(isNegativeScenario)
    {
       DEBUG_PRINT(DEBUG_TRACE,"\n Executing Negative Scenario\n");
       returnValue = ssp_MTAHAL_GetParamCharValue(paramName,NULL);
    }
    else
    {  DEBUG_PRINT(DEBUG_TRACE,"\n Executing Positive Sceanrio\n");
       returnValue = ssp_MTAHAL_GetParamCharValue(paramName,value);
    }

    if(0 == returnValue)
    {
        sprintf(Details,"%s", value);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
        DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetParamCharValue ---> Exit\n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetParamCharValue ---> Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetParamUlongValue
 * Description   : This will get the Ulong values
 * @param [in]   : req - paramName : Holds the name of api
 *                 req - value     : Holds the Ulong value
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
*
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetParamUlongValue ---> Entry \n");
    int returnValue = 0;
    char paramName[100] = {'\0'};
    char Details[64] = {'\0'};
    unsigned long value = 0;
    int isNegativeScenario = 0;

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["flag"])
    {
       isNegativeScenario = req["flag"].asInt();
    }    

    strcpy(paramName,req["paramName"].asCString());

    if(isNegativeScenario)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Executing Negative Scenario\n");
        returnValue = ssp_MTAHAL_GetParamUlongValue(paramName,NULL);
    }
    else
    {
       DEBUG_PRINT(DEBUG_TRACE,"\n Executing Positive Sceanrio \n");
        returnValue = ssp_MTAHAL_GetParamUlongValue(paramName,&value);
    }

    if(0 == returnValue)
    {
        sprintf(Details,"%d", value);
        response["result"]="SUCCESS";
        response["details"]=Details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
        DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetParamUlongValue ---> Exit\n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetParamUlongValue ---> Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_SetParamUlongValue
 * Description   : This will set the Ulong values
 * @param [in]   : req - paramName : Holds the name of api
 * 		           req - value     : Holds whether Value passed
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_SetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_SetParamUlongValue ---> Entry \n");
    int returnValue = 0;
    char paramName[100] = {'\0'};
    unsigned long value = 0;

    /* Validate the input arguments */
    if(&req["paramName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    if(&req["value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(paramName,req["paramName"].asCString());
    value = req["value"].asInt();

    returnValue = ssp_MTAHAL_SetParamUlongValue(paramName,value);

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully set the value";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to set the value";
        DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_SetParamUlongValue ---> Exit\n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_SetParamUlongValue ---> Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetDHCPInfo
 * Description   : This will get the all DHCP info for MTA
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetDHCPInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetDHCPInfo --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'};
    MTAMGMT_MTA_DHCP_INFO dhcpInfo;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MTAHAL_GetDHCPInfo(&dhcpInfo);
    else
        returnValue = ssp_MTAHAL_GetDHCPInfo(NULL);

    if(0 == returnValue)
    {
        sprintf(details, "IPAddress=%u;BootFileName=%s;FQDN=%s;SubnetMask=%u;Gateway=%u;LeaseTimeRemaining=%d;RebindTimeRemaining=%s;RenewTimeRemaining=%s;PrimaryDNS=%u;SecondaryDNS=%u;DHCPOption3=%s;DHCPOption6=%s;DHCPOption7=%s;DHCPOption8=%s;PCVersion=%s;MACAddress=%s;PrimaryDHCPServer=%u;SecondaryDHCPServer=%u",
                dhcpInfo.IPAddress.Value, dhcpInfo.BootFileName, dhcpInfo.FQDN, dhcpInfo.SubnetMask.Value, dhcpInfo.Gateway.Value, dhcpInfo.LeaseTimeRemaining, dhcpInfo.RebindTimeRemaining, dhcpInfo.RenewTimeRemaining, dhcpInfo.PrimaryDNS.Value, dhcpInfo.SecondaryDNS.Value, dhcpInfo.DHCPOption3, dhcpInfo.DHCPOption6, dhcpInfo.DHCPOption7, dhcpInfo.DHCPOption8, dhcpInfo.PCVersion, dhcpInfo.MACAddress, dhcpInfo.PrimaryDHCPServer.Value, dhcpInfo.SecondaryDHCPServer.Value);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetDHCPInfo --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetLineTableGetEntry
 * Description   : This will get the entry of the line table at the given index
 * @param [in]   : req - value : index of the line table
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetLineTableGetEntry(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetLineTableGetEntry --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'};
    MTAMGMT_MTA_LINETABLE_INFO info;
    unsigned long value = 0;
    char paramType[10] = {'\0'};

    if(&req["value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    value = req["value"].asInt();
    strcpy(paramType, req["paramType"].asCString());

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MTAHAL_GetLineTableGetEntry(value, &info);
    else
        returnValue = ssp_MTAHAL_GetLineTableGetEntry(value, NULL);


    if(0 == returnValue)
    {
        sprintf(details, "InstanceNumber=%u;LineNumber=%u;Status=%u;HazardousPotential=%s;ForeignEMF=%s;ResistiveFaults=%s;ReceiverOffHook=%s;RingerEquivalency=%s;CAName=%s;CAPort=%u;MWD=%u;CallsNumber=%u;CallsUpdateTime=%u",
                info.InstanceNumber,info.LineNumber,info.Status,info.HazardousPotential,info.ForeignEMF,info.ResistiveFaults,info.ReceiverOffHook,info.RingerEquivalency,info.CAName,info.CAPort,info.MWD,info.CallsNumber,info.CallsUpdateTime);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetLineTableGetEntry --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_TriggerDiagnostics
 * Description   : This will trigger GR909 Diagnostics
 * @param [in]   : req - value : line number
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_TriggerDiagnostics(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_TriggerDiagnostics --->Entry \n");
    int returnValue = 0;
    unsigned long value = 0;

    if(&req["value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    value = req["value"].asInt();

    returnValue = ssp_MTAHAL_TriggerDiagnostics(value);

    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="Successfully trigger the diagnostics";
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_TriggerDiagnostics --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetServiceFlow
 * Description   : This will get all the service flow info
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetServiceFlow(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetServiceFlow --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'}, *d;
    unsigned long count = 0;
    PMTAMGMT_MTA_SERVICE_FLOW pFlow = NULL, p;
    int i;

    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MTAHAL_GetServiceFlow(&count, &pFlow);
    else
        returnValue = ssp_MTAHAL_GetServiceFlow(&count, NULL);

    if(0 == returnValue)
    {
        if (pFlow)
        {
            p = pFlow;
            d = details;
            for (i=0; i<count; i++)
            {
                sprintf(d,"FLOW=%u;SFID=%u;ServiceClassName=%s;Direction=%s;ScheduleType=%u;DefaultFlow=%d;NomGrantInterval=%u;UnsolicitGrantSize=%u;TolGrantJitter=%u;NomPollInterval=%u;MinReservedPkt=%u;MaxTrafficRate=%u;MinReservedRate=%u;MaxTrafficBurst=%u;TrafficType=%s;NumberOfPackets=%u;",
                        i,p->SFID,p->ServiceClassName,p->Direction,p->ScheduleType,p->DefaultFlow,p->NomGrantInterval,p->UnsolicitGrantSize,p->TolGrantJitter,p->NomPollInterval,p->MinReservedPkt,p->MaxTrafficRate,p->MinReservedRate,p->MaxTrafficBurst,p->TrafficType,p->NumberOfPackets);
                d = details + strlen(details);
                p++;
            }
            free(pFlow);
        }
        else
        {
            sprintf(details, "There is no ServiceFlow data to display");
        }
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetServiceFlow --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetCalls
 * Description   : This will get all call info for the given instance number of LineTable
 * @param [in]   : req - value : instance number
 *                 req - count : Holds the line number of Call
 *                 req - pCfg  : Holds the MTA call info
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetCalls(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetCalls --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'}, *d;
    unsigned long value = 0;
    unsigned long count = 0;
    PMTAMGMT_MTA_CALLS pCfg = NULL, p;
    int i;

    if(&req["value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    value = req["value"].asInt();

    returnValue = ssp_MTAHAL_GetCalls(value, &count, &pCfg);

    if(0 == returnValue)
    {
        if (pCfg)
        {
            p = pCfg;
            d = details;
            for (i=0; i<count; i++)
            {
                sprintf(d,"COUNT=%u;Codec=%s;RemoteCodec=%s;CallStartTime=%s;CallEndTime=%s;CWErrorRate=%s;PktLossConcealment=%s;JitterBufferAdaptive=%d;Originator=%d;RemoteIPAddress=%X;CallDuration=%u;CWErrors=%s;SNR=%s;MicroReflections=%s;DownstreamPower=%s;UpstreamPower=%s;EQIAverage=%s;EQIMinimum=%s;EQIMaximum=%s;EQIInstantaneous=%s;MOS_LQ=%s;MOS_CQ=%s;EchoReturnLoss=%s;SignalLevel=%s;NoiseLevel=%s;LossRate=%s;DiscardRate=%s;BurstDensity=%s;GapDensity=%s;BurstDuration=%s;GapDuration=%s;RoundTripDelay=%s;Gmin=%s;RFactor=%s;ExternalRFactor=%s;JitterBufRate=%s;JBNominalDelay=%s;JBMaxDelay=%s;JBAbsMaxDelay=%s;TxPackets=%s;TxOctets=%s;RxPackets=%s;RxOctets=%s;PacketLoss=%s;IntervalJitter=%s;",
                        i+1,p->Codec,p->RemoteCodec,p->CallStartTime,p->CallEndTime,p->CWErrorRate,p->PktLossConcealment,p->JitterBufferAdaptive,p->Originator,p->RemoteIPAddress.Value,p->CallDuration,p->CWErrors,p->SNR,p->MicroReflections,p->DownstreamPower,p->UpstreamPower,p->EQIAverage,p->EQIMinimum,p->EQIMaximum,p->EQIInstantaneous,p->MOS_LQ,p->MOS_CQ,p->EchoReturnLoss,p->SignalLevel,p->NoiseLevel,p->LossRate,p->DiscardRate,p->BurstDensity,p->GapDensity,p->BurstDuration,p->GapDuration,p->RoundTripDelay,p->Gmin,p->RFactor,p->ExternalRFactor,p->JitterBufRate,p->JBNominalDelay,p->JBMaxDelay,p->JBAbsMaxDelay,p->TxPackets,p->TxOctets,p->RxPackets,p->RxOctets,p->PacketLoss,p->IntervalJitter);
                if (strlen(details) < 512)
                {
                    d = details + strlen(details);
                    p++;
                }
                else break;
            }
            free(pCfg);
        }
        else
        {
            sprintf(details, "There is no data to display for Line %d", value+1);
        }
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetCalls --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetCALLP
 * Description   : This will get the CALLP status info for the line number
 * @param [in]   : req - value : line number for which to retrieve info on
  		           req - info  : CallP info, to be returned
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetCALLP(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetCALLP --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'};
    MTAMGMT_MTA_CALLP callp;
    unsigned long value = 0;
    char paramType[10] = {'\0'};

    if(&req["value"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    value = req["value"].asInt();
    strcpy(paramType, req["paramType"].asCString());

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MTAHAL_GetCALLP(value, &callp);
    else
        returnValue = ssp_MTAHAL_GetCALLP(value, NULL);


    if(0 == returnValue)
    {
        sprintf(details, "LCState=%s;CallPState=%s;LoopCurrent=%s",callp.LCState,callp.CallPState,callp.LoopCurrent);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetCALLP --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetDSXLogs
 * Description   : This will get the all DSX log entries
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetDSXLogs(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetDSXLogs --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'}, *d;
    PMTAMGMT_MTA_DSXLOG pLog = NULL, p;
    unsigned long count = 0;
    int i;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MTAHAL_GetDSXLogs(&count, &pLog);
    else
        returnValue = ssp_MTAHAL_GetDSXLogs(&count, NULL);

    if(0 == returnValue)
    {
        if (pLog)
        {
            p = pLog;
            d = details;
            sprintf(d, "COUNT=%u;",count);
            d = details + strlen(details);
            for (i=0; i<count; i++)
            {
                sprintf(d, "Time=%s;Description=%s;ID=%u;Level=%u;",p->Time,p->Description,p->ID,p->Level);
                if (strlen(details) < 512)
                {
                    d = details + strlen(details);
                    p++;
                }
                else break;
            }
            free(pLog);
        }
        else
        {
            sprintf(details, "There is no log available");
        }
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetDSXLogs --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetMtaLog
 * Description   : This will get the all MTA log entries
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetMtaLog(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetMtaLog --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'}, *d, desc[100];
    PMTAMGMT_MTA_MTALOG_FULL pLog = NULL, p;
    unsigned long count = 0;
    int i;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MTAHAL_GetMtaLog(&count, &pLog);
    else
        returnValue = ssp_MTAHAL_GetMtaLog(&count, NULL);

    if(0 == returnValue)
    {
        if (pLog)
        {
            p = pLog;
            d = details;
            sprintf(d, "COUNT=%u;",count);
            d = details + strlen(details);
            for (i=0; i<count; i++)
            {
                memset(desc, '\0', 100);
                if (p->pDescription)
                {
                    strncpy(desc, p->pDescription, 99);
                }
                sprintf(d, "Index=%u;EventID=%u;EventLevel=%s;Time=%s;Description=%s;",
                        p->Index,p->EventID,p->EventLevel,p->Time,desc);
                if (strlen(details) < 512)
                {
                    d = details + strlen(details);
                    p++;
                }
                else break;
            }
            p = pLog;
            for (i=0; i<count; i++)
            {
                free(p->pDescription);
                p++;
            }
            free(pLog);
        }
        else
        {
            sprintf(details, "There is no log available");
        }
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetMtaLog --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetDhcpStatus
 * Description   : This will get the DHCP status for MTA
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetDhcpStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetDhcpStatus --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'};
    MTAMGMT_MTA_STATUS output_pIpv4status;
    MTAMGMT_MTA_STATUS output_pIpv6status;
    char const *status_string[4] = { "MTA_INIT", "MTA_START", "MTA_COMPLETE", "MTA_ERROR" };
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
       isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
       DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
       returnValue  = ssp_MTAHAL_getDhcpStatus(NULL,NULL);
    }
    else
    {
       returnValue = ssp_MTAHAL_getDhcpStatus(&output_pIpv4status, &output_pIpv6status);
    }

    if(0 == returnValue)
    {
        sprintf(details, "Ipv4 status=%s;Ipv6 status=%s", status_string[output_pIpv4status], status_string[output_pIpv6status]);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetDhcpStatus --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetConfigFileStatus
 * Description   : This will get the MTA config file status
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetConfigFileStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetConfigFileStatus --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'};
    MTAMGMT_MTA_STATUS output_status;
    char const *status_string[4] = { "MTA_INIT", "MTA_START", "MTA_COMPLETE", "MTA_ERROR" };
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
       isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
       DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
       returnValue = ssp_MTAHAL_getConfigFileStatus(NULL);
    }
    else
    {
       returnValue = ssp_MTAHAL_getConfigFileStatus(&output_status);
    }

    if(0 == returnValue)
    {
        sprintf(details, "Config File Status=%s", status_string[output_status]);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetConfigFileStatus --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetLineRegisterStatus
 * Description   : This will get the register status for all lines
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetLineRegisterStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetLineRegisterStatus --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'}, *d;
    MTAMGMT_MTA_STATUS status[8];
    unsigned long array_size = 0;
    int i;
    char const *status_string[4] = { "MTA_INIT", "MTA_START", "MTA_COMPLETE", "MTA_ERROR" };
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
        isNegativeScenario = req["flag"].asInt();
    }

    returnValue = ssp_MTAHAL_GetParamUlongValue((char *)"LineTableNumberOfEntries", &array_size);

    if(0 == returnValue && array_size != 0)
    {
        if(isNegativeScenario)
        {
          DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
          returnValue = ssp_MTAHAL_getLineRegisterStatus(NULL,0);
        }
        else
        {
          returnValue = ssp_MTAHAL_getLineRegisterStatus(status, array_size);
        }
        if(0 == returnValue)
        {
            d = details;
            for (i=0; i<array_size; i++)
            {
                sprintf(d, "Line %d=%s;", i+1, status_string[status[i]]);
                d = details + strlen(details);
            }
            response["result"]="SUCCESS";
            response["details"]=details;
        }
        else
        {
            response["result"]="FAILURE";
            response["details"]="Failed to get the value";
        }
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetLineRegisterStatus --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetHandsets
 * Description   : This will get the GetHandsets info
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetHandsets(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetHandsets --->Entry \n");
    int returnValue = 0;
    char details[1024] = {'\0'}, *d;
    PMTAMGMT_MTA_HANDSETS_INFO pHandsets = NULL, p;
    unsigned long count = 0;
    int i;
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
       isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
       DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
       returnValue = ssp_MTAHAL_GetHandsets(NULL,NULL);
    }
    else
    {
      returnValue = ssp_MTAHAL_GetHandsets(&count, &pHandsets);
    }

    if(0 == returnValue)
    {
        if (pHandsets)
        {
            p = pHandsets;
            d = details;
            sprintf(d, "COUNT=%u;",count);
            d = details + strlen(details);
            for (i=0; i<count; i++)
            {
                sprintf(d, "InstanceNumber=%lu;Status=%d;LastActiveTime=%s;HandsetName=%s,HandsetFirmware=%s,OperatingTN=%s,SupportedTN=%s;",p->InstanceNumber,p->Status,p->LastActiveTime,p->HandsetName,p->HandsetFirmware,p->OperatingTN,p->SupportedTN);
                if (strlen(details) < 512)
                {
                    d = details + strlen(details);
                    p++;
                }
                else break;
            }
            free(pHandsets);
        }
        else
        {
            sprintf(details, "There is no handset info available");
        }
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="Failed to get the value";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetHandsets--->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_InitDB
 * Description   : Retrieves the global information for all shared DBs and makes them accessible locally.
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_InitDB(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_InitDB --->Entry \n");
    int returnValue = 0;

    returnValue = ssp_MTAHAL_InitDB();

    if(0 == returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE, "Successfully initiated the MTA\n");
        response["result"] = "SUCCESS";
        response["details"] = "MTA initiated successfully";
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "MTAHAL_InitDB function has failed";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_InitDB --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_devResetNow
 * Description   : Reset MTA device
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_devResetNow(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_devResetNow --->Entry \n");
    int returnValue = 0;

    returnValue = ssp_MTAHAL_devResetNow();

    if(0 == returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE, "Successfully reset the MTA\n");
        response["result"] = "SUCCESS";
        response["details"] = "MTA is reset successfully";
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "MTAHAL_devResetNow function has failed";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_devResetNow --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_getMtaOperationalStatus
 * Description   : This will get the MTA operational status
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_getMtaOperationalStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_getMtaOperationalStatus --->Entry \n");
    int returnValue = 0;
    char details[100] = {'\0'};
    MTAMGMT_MTA_STATUS status;
    char const *status_string[4] = { "MTA_INIT", "MTA_START", "MTA_COMPLETE", "MTA_ERROR" };
    int isNegativeScenario = 0;

    if(&req["flag"])
    {
      isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
        DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
        returnValue = ssp_MTAHAL_getMtaOperationalStatus(NULL);
    }
    else
    {
       returnValue = ssp_MTAHAL_getMtaOperationalStatus(&status);
    }

    if(0 == returnValue)
    {
        sprintf(details, "MTA operational status: %s", status_string[status]);
        DEBUG_PRINT(DEBUG_TRACE, "Successfully reset the MTA\n");
        response["result"] = "SUCCESS";
        response["details"] = details;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "Failed to get the value";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_getMtaOperationalStatus --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : ssp_MTAHAL_start_provisioning
 * Description   : This API call will start IP provisioning for all the lines for IPv4/IPv6 , or dual mode
 * @param [in]   : req - mtaIPMode
 *                      req - dhcpOption122Suboption1
 *                      req - dhcpOption122Suboption2
 *                      req - dhcpOption2171CccV6DssID1
 *                      req - dhcpOption2171CccV6DssID2
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/

void MTAHAL::MTAHAL_start_provisioning(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_start_provisioning ---> Entry \n");

    int returnValue = 0;
    int mtaIPMode = 0;
    char dhcpOption122Suboption1[9] = {'\0'};
    char dhcpOption122Suboption2[9] = {'\0'};
    char dhcpOption2171CccV6DssID1[65] = {'\0'};
    char dhcpOption2171CccV6DssID2[65] = {'\0'};

    /* Validate the input arguments */
    if(&req["mtaIPMode"]==NULL ||
       &req["dhcpOption122Suboption1"]==NULL ||
       &req["dhcpOption122Suboption2"]==NULL ||
       &req["dhcpOption2171CccV6DssID1"]==NULL ||
       &req["dhcpOption2171CccV6DssID2"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    mtaIPMode = req["mtaIPMode"].asInt();
    strcpy(dhcpOption122Suboption1,req["dhcpOption122Suboption1"].asCString());
    strcpy(dhcpOption122Suboption2,req["dhcpOption122Suboption2"].asCString());
    strcpy(dhcpOption2171CccV6DssID1,req["dhcpOption2171CccV6DssID1"].asCString());
    strcpy(dhcpOption2171CccV6DssID2,req["dhcpOption2171CccV6DssID2"].asCString());

    returnValue = ssp_MTAHAL_start_provisioning(mtaIPMode, dhcpOption122Suboption1, dhcpOption122Suboption2, dhcpOption2171CccV6DssID1, dhcpOption2171CccV6DssID2);

    if(0 == returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE, "Successfully start MTA provisioning\n");
        response["result"] = "SUCCESS";
        response["details"] = "MTA start provisioning successfully";
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "Failed to start provisioning";
        DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_start_provisioning ---> Exit\n");
        return;
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_start_provisioning ---> Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_LineRegisterStatus_callback_register
 * Description   : This call back will be invoked to returing MTA line register status
 * @param [in]   : N/A
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_LineRegisterStatus_callback_register(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_LineRegisterStatus_callback_register --->Entry \n");
    int returnValue = 0;

    returnValue = ssp_MTAHAL_LineRegisterStatus_callback_register();

    if(0 == returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE, "Successfully registered MTA Line Register Status Callback\n");
        response["result"] = "SUCCESS";
        response["details"] = "MTA Line Register Status Callback registered";
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "Failed to registered MTA Line Register Status Callback";
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_LineRegisterStatus_callback_register --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name : MTAHAL_GetMtaProvisioningStatus
 * Description   : This will get the MTA Provisioning status
 * @param [in]   : flag - For negative scenario
 * @param [out]  : response - filled with SUCCESS or FAILURE based on the return value
 *
 *******************************************************************************************/
void MTAHAL::MTAHAL_GetMtaProvisioningStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetMtaProvisioningStatus --->Entry \n");
    int returnValue = 0;
    char details[100] = {'\0'};
    MTAMGMT_MTA_PROVISION_STATUS status;
    char const *status_string[4] = { "MTA_PROVISIONED", "MTA_NON_PROVISIONED" };
    int isNegativeScenario = 0;
    if(&req["flag"])
    {
      isNegativeScenario = req["flag"].asInt();
    }
    if(isNegativeScenario)
    {
        DEBUG_PRINT(DEBUG_TRACE, "Executing negative scenario\n");
        returnValue = ssp_MTAHAL_getMtaProvisioningStatus(NULL);
    }
    else
    {
       returnValue = ssp_MTAHAL_getMtaProvisioningStatus(&status);
    }
    if(0 == returnValue)
    {
        sprintf(details, "MTA Provisioning status: %s", status_string[status]);
        DEBUG_PRINT(DEBUG_TRACE, "Successfully retrieved the Provisioning Status of MTA\n");
        response["result"] = "SUCCESS";
        response["details"] = details;
    }
    else
    {
        response["result"] = "FAILURE";
        response["details"] = "Failed to get the value";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n MTAHAL_GetMtaProvisioningStatus --->Exit\n");
    return;
}

/**************************************************************************
 * Function Name : CreateObject
 * Description   : This function will be used to create a new object for the
 *                 class "MTAHAL".
 *
 **************************************************************************/

extern "C" MTAHAL* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new MTAHAL(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/

bool MTAHAL::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"MTAHAL shutting down\n");
    return TEST_SUCCESS;
}

/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object
 *
 **************************************************************************/
extern "C" void DestroyObject(MTAHAL *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying MTAHAL object\n");
    delete stubobj;
}

