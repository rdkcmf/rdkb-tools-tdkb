/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
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

#include "MoCAHAL.h"
#define MAX_BUFFER_SIZE 1024
#define RETURN_SUCCESS 0
#define RETURN_FAILURE 1

/***************************************************************************
 *Function name : initialize
 *Description   : Initialize Function will be used for registering the wrapper method
 *                        with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/
bool MoCAHAL::initialize(IN const char* szVersion)
{
    return TEST_SUCCESS;
}


/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string MoCAHAL::testmodulepre_requisites()
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL testmodulepre_requisites --->Entry\n");
    return "SUCCESS";

}


/***************************************************************************
 *Function name : testmodulepost_requisites
 *Description    : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/
bool MoCAHAL::testmodulepost_requisites()
{
    return TEST_SUCCESS;
}


/**************************************************************************
 * Function Name        : CreateObject
 * Description  : This function will be used to create a new object for the
 *                class "MoCAHAL".
*
 **************************************************************************/
extern "C" MoCAHAL* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new MoCAHAL(ptrtcpServer);
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_GetIfConfig
 * Description          : This function gets the MoCA Configuration Parameters that were previously set
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_GetIfConfig(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfConfig --->Entry\n");
    int ifIndex;
    int returnValue;
    char details[1000] = {'\0'};
    moca_cfg_t moca_config;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_GetIfConfig(ifIndex, &moca_config);
    else
	returnValue = ssp_MoCAHAL_GetIfConfig(ifIndex, NULL);
    if(0 == returnValue)
    {
	sprintf(details, "Value returned is :InstanceNumber=%lu, Alias=%s, bEnabled=%d, bPreferredNC=%d,  PrivacyEnabledSetting=%d, FreqCurrentMaskSetting=%s, KeyPassphrase=%s, TxPowerLimit=%d, AutoPowerControlPhyRate=%lu, BeaconPowerLimit=%lu, MaxIngressBWThreshold=%lu, MaxEgressBWThreshold=%lu, Reset=%d, MixedMode=%d, ChannelScanning=%d, AutoPowerControlEnable=%d, EnableTabooBit=%d, NodeTabooMask=%s, ChannelScanMask=%s",moca_config.InstanceNumber, moca_config.Alias, moca_config.bEnabled, moca_config.bPreferredNC, moca_config.PrivacyEnabledSetting, moca_config.FreqCurrentMaskSetting, moca_config.KeyPassphrase, moca_config.TxPowerLimit, moca_config.AutoPowerControlPhyRate, moca_config.BeaconPowerLimit, moca_config.MaxIngressBWThreshold, moca_config.MaxEgressBWThreshold, moca_config.Reset, moca_config.MixedMode, moca_config.ChannelScanning, moca_config.AutoPowerControlEnable, moca_config.EnableTabooBit, moca_config.NodeTabooMask, moca_config.ChannelScanMask);
        response["result"]="SUCCESS";
        response["details"]=details;
	DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfConfig ---->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_GetIfConfig operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfConfig ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_SetIfConfig
 * Description          : This function Sets the MoCA Configuration Parameters
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
		       : privacyEnable -  Enable/Disable Link Privacy. A Password is required when Privacy is enabled
		       : keyPassphrase - Privacy Password. This field is valid only if the Link Privacy is enabled
		       : autoPowerRate - PowerCtrlPhyTarget Used as a reference to achieve the PHY rate by adjusting  power
		       : autoPowerEnable - Enable/Disable adjusting Power to achieve the Target PHY rate

 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/

void MoCAHAL::MoCAHAL_SetIfConfig(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_SetIfConfig --->Entry\n");
    int ifIndex = 0;
    int returnValue = 0;
    moca_cfg_t moca_config;
    char paramType[10] = {'\0'};
    char key[18] = {'\0'};
    int  privacyEnable = 0, autoPowerRate  = 0, autoPowerEnable;

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();

    returnValue = ssp_MoCAHAL_GetIfConfig(ifIndex, &moca_config);

    privacyEnable = req["privacyEnable"].asInt();
    autoPowerRate = req["autoPowerRate"].asInt();
    autoPowerEnable = req["autoPowerEnable"].asInt();
    strcpy(key, req["keyPassphrase"].asCString());

    moca_config.PrivacyEnabledSetting = privacyEnable;
    memset(moca_config.KeyPassphrase, 0, 18);
    memcpy(moca_config.KeyPassphrase, key, strlen(key));
    moca_config.AutoPowerControlPhyRate = autoPowerRate;
    moca_config.AutoPowerControlEnable = autoPowerEnable;

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_SetIfConfig(ifIndex, &moca_config);
    else
        returnValue = ssp_MoCAHAL_SetIfConfig(ifIndex, NULL);
    if(0 == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="MoCAHAL_SetIfConfig operation success";
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_SetIfConfig ---->Execution success\n");
        return;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="MoCAHAL_SetIfConfig operation failed";
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_SetIfConfig ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_IfGetDynamicInfo
 * Description          : This function gets the Dynamic Status information on the interface & its associated network.
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/

void MoCAHAL::MoCAHAL_IfGetDynamicInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetDynamicInfo --->Entry\n");
    int ifIndex;
    int returnValue;
    char details[1500] = {'\0'};
    moca_dynamic_info_t dynamic_info;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_IfGetDynamicInfo(ifIndex, &dynamic_info);
    else
	returnValue = ssp_MoCAHAL_IfGetDynamicInfo(ifIndex, NULL);
    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :Status=%d, LastChange=%lu, MaxIngressBW=%lu, MaxEgressBW=%lu, CurrentVersion=%s, NetworkCoordinator=%lu, NodeID=%lu, BackupNC=%lu, PrivacyEnabled=%d, FreqCurrentMask=%s, CurrentOperFreq=%lu, LastOperFreq=%lu, TxBcastRate=%lu, MaxIngressBWThresholdReached=%d, MaxEgressBWThresholdReached=%d, NumberOfConnectedClients=%lu, NetworkCoordinatorMACAddress=%s, LinkUpTime=%lu", dynamic_info.Status, dynamic_info.LastChange, dynamic_info.MaxIngressBW, dynamic_info.MaxEgressBW, dynamic_info.CurrentVersion, dynamic_info.NetworkCoordinator, dynamic_info.NodeID, dynamic_info.BackupNC, dynamic_info.PrivacyEnabled, dynamic_info.FreqCurrentMask, dynamic_info.CurrentOperFreq, dynamic_info.LastOperFreq, dynamic_info.TxBcastRate, dynamic_info.MaxIngressBWThresholdReached, dynamic_info.MaxEgressBWThresholdReached, dynamic_info.NumberOfConnectedClients, dynamic_info.NetworkCoordinatorMACAddress, dynamic_info.LinkUpTime);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetDynamicInfo--->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_IfGetDynamicInfo operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetDynamicInfo ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_IfGetStaticInfo
 * Description          : This function gets the Static Information from the Local Node
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_IfGetStaticInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetStaticInfo --->Entry\n");
    int ifIndex;
    int returnValue;
    char details[1000] = {'\0'};
    moca_static_info_t static_info;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_IfGetStaticInfo(ifIndex, &static_info);
    else
	returnValue = ssp_MoCAHAL_IfGetStaticInfo(ifIndex, NULL);

    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :Name=%s, MacAddress=%s, FirmwareVersion=%s, MaxBitRate=%lu, HighestVersion=%s, FreqCapabilityMask=%s, NetworkTabooMask=%s, TxBcastPowerReduction=%lu, QAM256Capable=%d, PacketAggregationCapability=%d", static_info.Name, static_info.MacAddress, static_info.FirmwareVersion, static_info.MaxBitRate, static_info.HighestVersion, static_info.FreqCapabilityMask, static_info.NetworkTabooMask, static_info.TxBcastPowerReduction, static_info.QAM256Capable, static_info.PacketAggregationCapability);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetStaticInfo--->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_IfGetStaticInfo operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetStaticInfo ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_IfGetStats
 * Description          : This function Gets the Statistics on the Interface at Network Layer
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_IfGetStats(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetStats --->Entry\n");
    int ifIndex;
    int returnValue;
    char details[1000] = {'\0'};
    moca_stats_t stats;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_IfGetStats(ifIndex, &stats);
    else
        returnValue = ssp_MoCAHAL_IfGetStats(ifIndex, NULL);

    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :BytesSent=%lu, BytesReceived=%lu, PacketsSent=%lu, PacketsReceived=%lu, ErrorsSent=%lu, ErrorsReceived=%lu, UnicastPacketsSent=%lu, UnicastPacketsReceived=%lu, DiscardPacketsSent=%lu, DiscardPacketsReceived=%lu, MulticastPacketsSent=%lu, MulticastPacketsReceived=%lu, BroadcastPacketsSent=%lu, BroadcastPacketsReceived=%lu, UnknownProtoPacketsReceived=%lu, ExtAggrAverageTx=%lu, ExtAggrAverageTx=%lu", stats.BytesSent, stats.BytesReceived, stats.PacketsSent, stats.PacketsReceived, stats.ErrorsSent, stats.ErrorsReceived, stats.UnicastPacketsSent, stats.UnicastPacketsReceived, stats.DiscardPacketsSent, stats.DiscardPacketsReceived, stats.MulticastPacketsSent, stats.MulticastPacketsReceived, stats.BroadcastPacketsSent, stats.BroadcastPacketsReceived, stats.UnknownProtoPacketsReceived, stats.ExtAggrAverageTx, stats.ExtAggrAverageTx);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetStats--->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_IfGetStats operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetStats ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_GetNumAssociatedDevices
 * Description          : This function Gets the Number of Nodes on the MoCA network.
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_GetNumAssociatedDevices(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetNumAssociatedDevices --->Entry\n");
    int ifIndex;
    int returnValue;
    char details[1000] = {'\0'};
    ULONG devCount;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_GetNumAssociatedDevices(ifIndex, &devCount);
    else
        returnValue = ssp_MoCAHAL_GetNumAssociatedDevices(ifIndex, NULL);

    if(0 == returnValue)
    {
        sprintf(details, "Value returned is : %lu",devCount);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetNumAssociatedDevices--->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_GetNumAssociatedDevices operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetNumAssociatedDevices ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_IfGetExtCounter
 * Description          : This function Gets the Statistics on the Interface at MoCA MAC Layer.
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_IfGetExtCounter(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetExtCounter---->Entry\n");
    int ifIndex;
    int returnValue;
    char details[1000] = {'\0'};
    moca_mac_counters_t mac_counters;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_IfGetExtCounter(ifIndex, &mac_counters);
    else
        returnValue = ssp_MoCAHAL_IfGetExtCounter(ifIndex, NULL);

    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :Map=%lu, Rsrv=%lu, Lc=%lu, Adm=%lu, Probe=%lu, Async=%lu", mac_counters.Map, mac_counters.Rsrv, mac_counters.Lc, mac_counters.Adm, mac_counters.Probe, mac_counters.Async);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetExtCounter--->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_IfGetExtCounter operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetExtCounter---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_IfGetExtAggrCounter
 * Description          : Gets the Aggregate DATA units Transferred (Tx & Rx).
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_IfGetExtAggrCounter(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetExtAggrCounter---->Entry\n");
    int ifIndex;
    int returnValue;
    char details[100] = {'\0'};
    moca_aggregate_counters_t moca_aggregate_counts;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_IfGetExtAggrCounter(ifIndex, &moca_aggregate_counts);
    else
        returnValue = ssp_MoCAHAL_IfGetExtAggrCounter(ifIndex, NULL);

    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :Tx=%lu, Rx=%lu", moca_aggregate_counts.Tx,moca_aggregate_counts.Rx);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetExtAggrCounter--->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_IfGetExtAggrCounter operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_IfGetExtAggrCounter---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_GetMocaCPEs
 * Description          : Get MAC Address of all the Nodes Connected on MoCA Network.
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_GetMocaCPEs(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetMocaCPEs---->Entry\n");
    int ifIndex;
    int returnValue;
    char details[100] = {'\0'};
    moca_cpe_t cpes;
    int num_cpes;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_GetMocaCPEs(ifIndex, &cpes, &num_cpes);
    else
        returnValue = ssp_MoCAHAL_GetMocaCPEs(ifIndex, &cpes, NULL);

    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :mac_addr=%s", cpes.mac_addr);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetMocaCPEs--->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_GetMocaCPEs operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetMocaCPEs---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_GetMocaCPEs
 * Description          : Get Information on all the associated Devices on the network
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
		       : devCount - no: of associated devices
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_GetAssociatedDevices(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetAssociatedDevices---->Entry\n");
    int ifIndex;
    int returnValue;
    char details[1500] = {'\0'};
    moca_associated_device_t *pdevice_array = NULL;
    int devCount, i;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();
    devCount = req["devCount"].asInt();

    pdevice_array = (moca_associated_device_t*) malloc(sizeof(moca_associated_device_t)*devCount);
    if(!pdevice_array)
    {
         DEBUG_PRINT(DEBUG_TRACE,"\nMemory has not allocated successfully \n ");
    }
    else
    {
        if(strcmp(paramType, "NULL"))
            returnValue = ssp_MoCAHAL_GetAssociatedDevices(ifIndex, &pdevice_array);
        else
            returnValue = ssp_MoCAHAL_GetAssociatedDevices(ifIndex, NULL);
        if(0 == returnValue)
        {
            if(pdevice_array!=NULL)
            {
                sprintf(details, "Value returned is :MACAddress=%s, NodeID=%lu, PreferredNC=%d, HighestVersion=%s, PHYTxRate=%lu, PHYRxRate=%lu, TxPowerControlReduction=%lu, RxPowerLevel=%d, TxBcastRate=%lu, RxBcastPowerLevel=%d, TxPackets=%lu, RxPackets=%lu, RxErroredAndMissedPackets=%lu, QAM256Capable=%d, PacketAggregationCapability=%d, RxSNR=%lu, Active=%d, RxBcastRate=%lu, NumberOfClients=%lu", pdevice_array->MACAddress, pdevice_array->NodeID, pdevice_array->PreferredNC, pdevice_array->HighestVersion, pdevice_array->PHYTxRate, pdevice_array->PHYRxRate, pdevice_array->TxPowerControlReduction, pdevice_array->RxPowerLevel, pdevice_array->TxBcastRate, pdevice_array->RxBcastPowerLevel, pdevice_array->TxPackets, pdevice_array->RxPackets, pdevice_array->RxErroredAndMissedPackets, pdevice_array->QAM256Capable, pdevice_array->PacketAggregationCapability, pdevice_array->RxSNR, pdevice_array->Active, pdevice_array->RxBcastRate, pdevice_array->NumberOfClients);
                for(i=0; i<devCount; i++)
                {
                    printf("Associated device%d values are: MACAddress=%s, NodeID=%lu, PreferredNC=%d, HighestVersion=%s, PHYTxRate=%lu, PHYRxRate=%lu, TxPowerControlReduction=%lu, RxPowerLevel=%d, TxBcastRate=%lu, RxBcastPowerLevel=%d, TxPackets=%lu, RxPackets=%lu, RxErroredAndMissedPackets=%lu, QAM256Capable=%d, PacketAggregationCapability=%d, RxSNR=%lu, Active=%d, RxBcastRate=%lu, NumberOfClients=%lu",devCount+1, pdevice_array[devCount].MACAddress, pdevice_array[devCount].NodeID, pdevice_array[devCount].PreferredNC, pdevice_array[devCount].HighestVersion, pdevice_array[devCount].PHYTxRate, pdevice_array[devCount].PHYRxRate, pdevice_array[devCount].TxPowerControlReduction, pdevice_array[devCount].RxPowerLevel, pdevice_array[devCount].TxBcastRate, pdevice_array[devCount].RxBcastPowerLevel, pdevice_array[devCount].TxPackets, pdevice_array[devCount].RxPackets, pdevice_array[devCount].RxErroredAndMissedPackets, pdevice_array[devCount].QAM256Capable, pdevice_array[devCount].PacketAggregationCapability, pdevice_array[devCount].RxSNR, pdevice_array[devCount].Active, pdevice_array[devCount].RxBcastRate, pdevice_array[devCount].NumberOfClients);
                }
                response["result"]="SUCCESS";
                response["details"]=details;
                DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetAssociatedDevices--->Execution success\n");
            }
            else
            {
                sprintf(details, "MoCAHAL_GetAssociatedDevices returned empty buffer");
                response["result"]="FAILURE";
                response["details"]=details;
                DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetAssociatedDevices--->Execution failed\n");
            }
            return;
        }
        else
        {
            sprintf(details, "MoCAHAL_GetAssociatedDevices operation failed");
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetAssociatedDevices---->Error in execution\n");
            return;
        }

       if(pdevice_array != NULL)
           free(pdevice_array);
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_FreqMaskToValue
 * Description          : converts Mask Value to Frequency Number.
 * 
 * @param [in] req-    : mask - mask valueto be converted
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_FreqMaskToValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_FreqMaskToValue---->Entry\n");
    unsigned char mask[128] = {'\0'};
    int returnValue;
    char details[100] = {'\0'};

    strcpy((char*)mask, req["mask"].asCString());

    returnValue = ssp_MoCAHAL_FreqMaskToValue(mask);
    if(0 < returnValue)
    {
        sprintf(details, "Value returned is : %d", returnValue);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_FreqMaskToValue--->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_FreqMaskToValue operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_FreqMaskToValue---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_HardwareEquipped
 * Description          : returns whether the MoCA Hardware is Equipped or Not.
 *
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_HardwareEquipped(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_HardwareEquipped--->Entry\n");
    int returnValue;
    char details[100] = {'\0'};

    returnValue = ssp_MoCAHAL_HardwareEquipped();
    if(1 == returnValue)
    {
        sprintf(details, "Value returned is : %d", returnValue);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_HardwareEquipped-->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_HardwareEquipped operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_HardwareEquipped--->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_GetFullMeshRates
 * Description          : Gets the MoCA Mesh Table.
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
		       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_GetFullMeshRates(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetFullMeshRates---->Entry\n");
    int ifIndex;
    int returnValue;
    char details[1000] = {'\0'};
    moca_mesh_table_t deviceArray;
    unsigned long count;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();
    count = req["count"].asInt();

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_GetFullMeshRates(ifIndex, &deviceArray, &count);
    else
        returnValue = ssp_MoCAHAL_GetFullMeshRates(ifIndex, NULL, NULL);
    if(0 == returnValue)
    {
        sprintf(details, "Value returned is :RxNodeID=%lu, TxNodeID=%lu, TxRate=%lu", deviceArray.RxNodeID, deviceArray.TxNodeID, deviceArray.TxRate);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetFullMeshRates--->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_GetFullMeshRates operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetFullMeshRates---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_GetFlowStatistics
 * Description          : Gets the MoCA flow Table.
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_GetFlowStatistics(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetFlowStatistics--->Entry\n");
    int ifIndex;
    int returnValue;
    char details[1000] = {'\0'};
    moca_flow_table_t deviceArray;
    unsigned long count;
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());
    ifIndex = req["ifIndex"].asInt();

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_GetFlowStatistics(ifIndex, &deviceArray, &count);
    else
        returnValue = ssp_MoCAHAL_GetFlowStatistics(ifIndex, NULL, NULL);
    if(0 == returnValue)
    {
        sprintf(details, "tableEntryCount=%lu, FlowID=%lu, IngressNodeID=%lu, EgressNodeID=%lu, FlowTimeLeft=%lu, DestinationMACAddress=%s, PacketSize=%lu, PeakDataRate=%lu, BurstSize=%lu, FlowTag=%lu, LeaseTime=%lu", deviceArray.FlowID, deviceArray.IngressNodeID, deviceArray.EgressNodeID, deviceArray.FlowTimeLeft, deviceArray.DestinationMACAddress, deviceArray.PacketSize, deviceArray.PeakDataRate, deviceArray.BurstSize, deviceArray.FlowTag, deviceArray.LeaseTime);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetFlowStatistics-->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_GetFlowStatistics operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetFlowStatistics--->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_GetResetCount
 * Description          : Gets the MoCA reset count
 *
 * @param [in] req-    : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_GetResetCount(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetResetCount--->Entry\n");
    int returnValue;
    unsigned long count;
    char details[100] = {'\0'};
    char paramType[10] = {'\0'};

    strcpy(paramType, req["paramType"].asCString());

    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_GetResetCount(&count);
    else
        returnValue = ssp_MoCAHAL_GetResetCount(NULL);
    if(0 == returnValue)
    {
        sprintf(details, "Value returned is : %d", count);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetResetCount-->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_GetResetCount operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetResetCount--->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_GetIfAcaConfig
 * Description          : Gets the MoCA interface ACA config
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_GetIfAcaConfig(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfAcaConfig--->Entry\n");
    int ifIndex = 0;
    int returnValue = RETURN_FAILURE;
    char details[MAX_BUFFER_SIZE] = {'\0'};
    moca_aca_cfg_t acaCfg = {0};
    char paramType[10] = "NULL";

    if(&req["paramType"])
    {
        strcpy(paramType, req["paramType"].asCString());
    }

    if(&req["ifIndex"] == NULL)
    {
            response["result"] = "FAILURE";
            response["details"] = "NULL parameter as input argument";
            return;
    }
    ifIndex = req["ifIndex"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfAcaConfig--->entering ssp\n");
    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_GetIfAcaConfig(ifIndex, &acaCfg);
    else
        returnValue = ssp_MoCAHAL_GetIfAcaConfig(ifIndex, NULL);

    if(RETURN_SUCCESS == returnValue)
    {
        sprintf(details, "Value returned is :NodeID=%lu, ProbeType=%d, Channel=%lu, ReportNodes=%lu, ACAStart=%d", acaCfg.NodeID, acaCfg.Type, acaCfg.Channel, acaCfg.ReportNodes, acaCfg.ACAStart);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfAcaConfig-->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_GetIfAcaConfig operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfAcaConfig--->Error in execution\n");
        return;
    }
}

/****************************************************************************************
Utility function to parse and print the output of SC Mode
*****************************************************************************************/
static void print_subcarriers(UCHAR ScMod[])
{
   int subCarrier1;
   int print_nums = 1;

   for (subCarrier1 = 0; subCarrier1 < 512; subCarrier1++)
   {
      if (print_nums)
      {
         printf("%3d - %3d:  ", subCarrier1, subCarrier1 + 31 );
         print_nums = 0;
      }
      printf ("%x", ScMod[subCarrier1]) ;
      if (((subCarrier1 + 1) % 32) == 0) {
         printf ("\n") ;
         print_nums = 1;
      }
   }
   printf("\n");
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_GetIfScmod
 * Description          : Gets the MoCA SC Mode status
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_GetIfScmod(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfScmod--->Entry\n");
    int ifIndex = 0, i=0;
    int returnValue = RETURN_FAILURE;
    char details[MAX_BUFFER_SIZE] = {'\0'};
    moca_scmod_stat_t *pscmodStat = NULL;
    char paramType[10] = "NULL";
    int numOfEntries = 0;

    if(&req["paramType"])
    {
        strcpy(paramType, req["paramType"].asCString());
    }

    if(&req["ifIndex"] == NULL)
    {
            response["result"] = "FAILURE";
            response["details"] = "NULL parameter as input argument";
            return;
    }
    ifIndex = req["ifIndex"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfScmod--->entering ssp\n");
    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_GetIfScmod(ifIndex, &numOfEntries, &pscmodStat);
    else
        returnValue = ssp_MoCAHAL_GetIfScmod(ifIndex, &numOfEntries, NULL);

    if(RETURN_SUCCESS == returnValue && pscmodStat != NULL)
    {
        for(i = 0; i < numOfEntries; i++)
        {
            if (strlen(details) < 512)
            {
                printf("TxNode:%d, RxNode:%d, Channel:%d\n",
                        pscmodStat[i].TxNode, pscmodStat[i].RxNode, pscmodStat[i].Channel);

                printf("Mod\n");
                print_subcarriers(pscmodStat[i].Mod);
                printf("Nper\n");
                print_subcarriers(pscmodStat[i].Nper);
                printf("Vlper\n");
                print_subcarriers(pscmodStat[i].Vlper);
                printf("\n");
                sprintf((details + strlen(details)), "TxNode=%d, RxNode=%d, Channel=%d", pscmodStat[i].TxNode, pscmodStat[i].RxNode, pscmodStat[i].Channel);
            }
            else break;
        }

        free(pscmodStat);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfScmod-->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_GetIfScmod operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfScmod--->Error in execution\n");
        return;
    }
}

/****************************************************************************************
Utility function to parse and print the output of ACA status
*****************************************************************************************/
static void aca_status_print_report(moca_aca_stat_t acaStat)
{
   int i;
   printf("Assessment Type         %s(%d)\n", (acaStat.acaCfg.Type == 0)? "QUIET":"EVM", acaStat.acaCfg.Type);
   printf("ACA Status:             %d\n", acaStat.stat);
   printf("Total Power:            %d dBm\n", acaStat.RxPower);
   printf("ACATrapCompleted:            %d\n", acaStat.ACATrapCompleted);

   printf("Power profile:          ");
   for (i = 0; i < 512; i++) {
      printf("%4d ", acaStat.ACAPowProfile[i]);
      if (i % 8 == 7) printf("\n                    ");
   }
   printf("\n");
}

/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_GetIfAcaStatus
 * Description          : Gets the MoCA interface ACA status
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                       : paramType - To indicate negative test scenario. it has to be set as NULL for negative sceanario
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_GetIfAcaStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfAcaStatus--->Entry\n");
    int ifIndex = 0;
    int returnValue = RETURN_FAILURE;
    char details[MAX_BUFFER_SIZE] = {'\0'};
    moca_aca_stat_t acaStat;
    char paramType[10] = "NULL";

    if(&req["paramType"])
    {
        strcpy(paramType, req["paramType"].asCString());
    }

    if(&req["ifIndex"] == NULL)
    {
            response["result"] = "FAILURE";
            response["details"] = "NULL parameter as input argument";
            return;
    }
    ifIndex = req["ifIndex"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfAcaStatus--->entering ssp\n");
    if(strcmp(paramType, "NULL"))
        returnValue = ssp_MoCAHAL_GetIfAcaStatus(ifIndex, &acaStat);
    else
        returnValue = ssp_MoCAHAL_GetIfAcaConfig(ifIndex, NULL);

    if(RETURN_SUCCESS == returnValue)
    {
        sprintf(details, "Value returned is :ACA status -> ACA Status=%d, Total Power=%d dBm, ACATrapCompleted=%d \n ACA Config->  Assessment Type=%s(%d), NodeId= %u, Channel= %u, ReportNodes= %u, ACAStart= %d", acaStat.stat, acaStat.RxPower, acaStat.ACATrapCompleted, (acaStat.acaCfg.Type == 0)? "QUIET":"EVM", acaStat.acaCfg.Type, acaStat.acaCfg.NodeID, acaStat.acaCfg.Channel, acaStat.acaCfg.ReportNodes, acaStat.acaCfg.ACAStart);
	aca_status_print_report(acaStat);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfAcaStatus-->Execution success\n");
        return;
    }
    else
    {
        sprintf(details, "MoCAHAL_GetIfAcaStatus operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_GetIfAcaStatus--->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_CancelIfAca
 * Description          : Cancels the ACA process
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_CancelIfAca(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_CancelIfAca--->Entry\n");
    int ifIndex = 0;
    int returnValue = RETURN_FAILURE;

    if(&req["ifIndex"] == NULL)
    {
            response["result"] = "FAILURE";
            response["details"] = "NULL parameter as input argument";
            return;
    }
    ifIndex = req["ifIndex"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_CancelIfAca--->entering ssp\n");

    returnValue = ssp_MoCAHAL_CancelIfAca(ifIndex);

    if(RETURN_SUCCESS == returnValue)
    {
        response["result"]="SUCCESS";
        response["details"]="MoCAHAL_CancelIfAca returns SUCCESS";
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_CancelIfAca--->Execution success\n");
        return;
    }
    else
    {
        response["result"]="FAILURE";
        response["details"]="MoCAHAL_CancelIfAca operation failed";
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_CancelIfAca--->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : MoCAHAL_SetIfAcaConfig
 * Description          : Sets the MoCA Configuration Parameters to start the ACA process
 *
 * @param [in] req-    : ifIndex - index of the MoCA interface
                        : nodeId - The NodeID where we want to start the ACA testing
                        : channel - The Channel on which ACA test should start
                        : reportNodes - MoCA Nodes that are requested to be part of the channel assessment
                        : probeType - The Probe Type could be Enum EVM=1 or Quite=0
                        : ACAStart - To start ACA
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void MoCAHAL::MoCAHAL_SetIfAcaConfig(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_SetIfAcaConfig--->Entry\n");
    int ifIndex = 0;
    char details[MAX_BUFFER_SIZE] = {'\0'};
    moca_aca_cfg_t acaCfg = {0};
    int returnValue = RETURN_FAILURE;

    if(&req["ifIndex"] == NULL || &req["nodeId"] == NULL || &req["channel"] == NULL || &req["reportNodes"] == NULL || &req["probeType"] == NULL || &req["ACAStart"] == NULL)
    {
            response["result"] = "FAILURE";
            response["details"] = "NULL parameter as input argument";
            return;
    }
    ifIndex = req["ifIndex"].asInt();
    acaCfg.NodeID = req["nodeId"].asInt();
    acaCfg.Channel = req["channel"].asInt();
    acaCfg.ReportNodes = req["reportNodes"].asInt();
    acaCfg.Type = (PROBE_TYPE)req["probeType"].asInt();
    acaCfg.ACAStart = req["ACAStart"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\nValues to be set are :NodeID=%lu, ProbeType=%d, Channel=%lu, ReportNodes=%lu, ACAStart=%d", acaCfg.NodeID, acaCfg.Type, acaCfg.Channel, acaCfg.ReportNodes, acaCfg.ACAStart);
    DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_SetIfAcaConfig--->entering ssp\n");

    returnValue = ssp_MoCAHAL_SetIfAcaConfig(ifIndex, acaCfg);

    if(RETURN_SUCCESS == returnValue)
    {
       returnValue = ssp_MoCAHAL_GetIfAcaConfig(ifIndex, &acaCfg);
       if(RETURN_SUCCESS == returnValue)
       {
            sprintf(details, "Value returned is :NodeID=%lu, ProbeType=%d, Channel=%lu, ReportNodes=%lu, ACAStart=%d", acaCfg.NodeID, acaCfg.Type, acaCfg.Channel, acaCfg.ReportNodes, acaCfg.ACAStart);
            response["result"]="SUCCESS";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_SetIfAcaConfig--->Execution success\n");
            return;
       }
       else
       {
            response["result"]="FAILURE";
            response["details"]="Get ACA config in MoCAHAL_SetIfAcaConfig failed";
            return;
       }
    }
    else
    {
        sprintf(details, "MoCAHAL_SetIfAcaConfig opeeration failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n MoCAHAL_SetIfAcaConfig---->Error in execution\n");
        return;
    }
}


/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/
bool MoCAHAL::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"MoCAHAL shutting down\n");
    return TEST_SUCCESS;
}

/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(MoCAHAL *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying MoCAHAL object\n");
    delete stubobj;
}
