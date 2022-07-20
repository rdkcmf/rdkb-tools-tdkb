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

#ifndef __WIFIHAL_STUB_H__
#define __WIFIHAL_STUB_H__

#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>
extern "C"
{
#include "wifi_hal.h"

extern int wifi_getDeclineBARequestEnable(int radioIndex, unsigned char *enable);
extern int wifi_setDeclineBARequestEnable(int radioIndex, unsigned char enable);
extern int wifi_getDfsEnable(int radioIndex, unsigned char *enable);
extern int wifi_setDfsEnable(int radioIndex, unsigned char enable);
extern int wifi_setRadioDfsRefreshPeriod(int radioIndex, long unsigned int uLongVar);
extern int wifi_getApBasicAuthenticationMode(int radioIndex, char* output);
extern int wifi_kickAssociatedDevice(int radioIndex, wifi_device_t* dev);
extern int wifi_getAssociatedDeviceDetail(int apIndex, int devIndex, wifi_device_t *dev);
extern int wifi_setDTIMInterval(int radioIndex, int output);
extern int wifi_getApVlanID(int radioIndex, int* output);
extern int wifi_pushChannel(int radioIndex, int output);
extern int wifi_getIndexFromName(char* ssidName, int *output);
extern int wifi_clearRadioResetCount();
extern int wifi_ifConfigUp(int apIndex);
extern int wifi_ifConfigDown(int apIndex);
extern int wifi_initRadio(int radioIndex);
extern int wifi_getAutoBlockAckEnable(int radioIndex, unsigned char *output_bool);
extern int wifi_setAutoBlockAckEnable(int radioIndex, unsigned char output_bool);
extern int wifi_getRadioAbsoluteTransmitPower_priv(int radioIndex, long unsigned int *output_ulong);
extern int wifi_factoryReset_post(int index, int commit, int restart);
extern int wifi_apply_wldm(void);
}

#define TEST_SUCCESS true
#define TEST_FAILURE false

#define SSP_SUCCESS       0
#define SSP_FAILURE       1

/* for reference added it,(IN) indicates accepting the request from Test Manager and (OUT)
   indicates sending the response for the request back to the Manager */
#ifndef IN
#define IN
#endif

#ifndef OUT
#define OUT
#endif

using namespace std;

/* RDKTestAgent : This Class provides interface for the module to enable RPC mechanism. */
class RDKTestAgent;

/* RDKTestStubInterface : This Class provides provides interface for the modules.  */
class WIFIHAL : public RDKTestStubInterface, public AbstractServer<WIFIHAL>
{
    public:

        WIFIHAL(TcpSocketServer &ptrRpcServer) : AbstractServer <WIFIHAL>(ptrRpcServer)
        {

            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetParamBoolValue", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER,"param", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetParamBoolValue);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetParamULongValue", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER,"param", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetParamULongValue);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetParamStringValue", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "param", JSON_STRING, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetParamStringValue);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetRadioStandard", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "param", JSON_STRING, "paramType",  JSON_STRING, "gOnly",JSON_INTEGER, "nOnly",JSON_INTEGER, "acOnly",JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetOrSetRadioStandard);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetParamIntValue", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "param", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetParamIntValue);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetParamUIntValue", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "param", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetParamUIntValue);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetIndexFromName", PARAMS_BY_NAME, JSON_STRING, "param", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetIndexFromName);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApIndexFromName", PARAMS_BY_NAME, JSON_STRING, "param", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetApIndexFromName);
            this->bindAndAddMethod(Procedure("WIFIHAL_ClearRadioResetCount", PARAMS_BY_NAME, JSON_STRING, NULL), &WIFIHAL::WIFIHAL_ClearRadioResetCount);
            this->bindAndAddMethod(Procedure("WIFIHAL_Reset", PARAMS_BY_NAME, JSON_STRING, NULL), &WIFIHAL::WIFIHAL_Reset);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetSecurityRadiusServer", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "port", JSON_INTEGER, "IPAddress", JSON_STRING, "RadiusSecret", JSON_STRING, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetSecurityRadiusServer);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetApBridgeInfo", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "bridgeName", JSON_STRING, "IP", JSON_STRING, "subnet", JSON_STRING, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetApBridgeInfo);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetRadioDCSScanTime", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "output_interval_seconds", JSON_INTEGER, "output_dwell_milliseconds", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetRadioDCSScanTime);
            this->bindAndAddMethod(Procedure("WIFIHAL_AddorDelApAclDevice", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"apIndex", JSON_INTEGER, "DeviceMacAddress", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_AddorDelApAclDevice);
            this->bindAndAddMethod(Procedure("WIFIHAL_IfConfigUporDown", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"apIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_IfConfigUporDown);
            this->bindAndAddMethod(Procedure("WIFIHAL_ParamRadioIndex", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_ParamRadioIndex);
            this->bindAndAddMethod(Procedure("WIFIHAL_StartorStopHostApd", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_StartorStopHostApd);
            this->bindAndAddMethod(Procedure("WIFIHAL_FactoryReset", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_FactoryReset);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetSecurityRadiusSettings",PARAMS_BY_NAME, JSON_STRING, "methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "RadiusServerRetries", JSON_INTEGER, "RadiusServerRequestTimeout", JSON_INTEGER, "PMKLifetime", JSON_INTEGER, "PMKCaching", JSON_INTEGER, "PMKCacheInterval", JSON_INTEGER, "MaxAuthenticationAttempts", JSON_INTEGER, "BlacklistTableTimeout", JSON_INTEGER, "IdentityRequestRetryInterval", JSON_INTEGER, "QuietPeriodAfterFailedAuthentication", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetOrSetSecurityRadiusSettings);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetSSIDTrafficStats2",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetSSIDTrafficStats2);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioTrafficStats2",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetRadioTrafficStats2);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceDiagnosticResult",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult);
            this->bindAndAddMethod(Procedure("WIFIHAL_Down", PARAMS_BY_NAME, JSON_STRING, NULL), &WIFIHAL::WIFIHAL_Down);
            this->bindAndAddMethod(Procedure("WIFIHAL_Init", PARAMS_BY_NAME, JSON_STRING, NULL), &WIFIHAL::WIFIHAL_Init);
            this->bindAndAddMethod(Procedure("WIFIHAL_CreateInitialConfigFiles", PARAMS_BY_NAME, JSON_STRING, NULL), &WIFIHAL::WIFIHAL_CreateInitialConfigFiles);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetNeighboringWiFiDiagnosticResult2",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetNeighboringWiFiDiagnosticResult2);
            this->bindAndAddMethod(Procedure("WIFIHAL_PushRadioChannel2",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER, "channel",JSON_INTEGER, "channel_width_MHz",JSON_INTEGER, "csa_beacon_count",JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_PushRadioChannel2);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetNeighboringWiFiStatus",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetNeighboringWiFiStatus);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioChannelStats",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER, "channel", JSON_INTEGER, "inPool", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetRadioChannelStats);
            this->bindAndAddMethod(Procedure("WIFIHAL_ParamApIndex", PARAMS_BY_NAME, JSON_STRING, "methodName", JSON_STRING, "apIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_ParamApIndex);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDevice", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDevice);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApDeviceRSSI", PARAMS_BY_NAME, JSON_STRING, "methodName", JSON_STRING, "apIndex", JSON_INTEGER, "MAC", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetApDeviceRSSI);
            this->bindAndAddMethod(Procedure("WIFIHAL_DelApAclDevices", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_DelApAclDevices);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApAclDevices", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetApAclDevices);
            this->bindAndAddMethod(Procedure("WIFIHAL_CreateAp", PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "radioIndex", JSON_INTEGER, "essid", JSON_STRING, "hideSsid", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_CreateAp);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceStats",PARAMS_BY_NAME, JSON_STRING, "apIndex",JSON_INTEGER, "MAC", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceStats);
            this->bindAndAddMethod(Procedure("WIFIHAL_StartNeighborScan", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER,"scan_mode", JSON_INTEGER,"dwell_time", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_StartNeighborScan);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceTxStatsResult",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER, "MAC", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceTxStatsResult);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceRxStatsResult",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER, "MAC", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceRxStatsResult);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApDeviceTxRxRate", PARAMS_BY_NAME, JSON_STRING, "methodName", JSON_STRING, "apIndex", JSON_INTEGER, "MAC", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetApDeviceTxRxRate);
            this->bindAndAddMethod(Procedure("WIFIHAL_SetApScanFilter", PARAMS_BY_NAME, JSON_STRING, "methodName", JSON_STRING, "apIndex", JSON_INTEGER, "essid", JSON_STRING,"mode", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SetApScanFilter);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceDiagnosticResult3",PARAMS_BY_NAME, JSON_STRING, "apIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult3);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioChannelStats2",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetRadioChannelStats2);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceTidStatsResult",PARAMS_BY_NAME,JSON_STRING,"radioIndex",JSON_INTEGER,"MAC",JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceTidStatsResult);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetBandSteeringLog",PARAMS_BY_NAME,JSON_STRING,"record_index",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetBandSteeringLog);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceDiagnosticResult2",PARAMS_BY_NAME,JSON_STRING,"apIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult2);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioMode",PARAMS_BY_NAME,JSON_STRING,"radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetRadioMode);
            this->bindAndAddMethod(Procedure("WIFIHAL_SetRadioMode",PARAMS_BY_NAME,JSON_STRING,"radioIndex",JSON_INTEGER,"chnmode",JSON_STRING,"puremode",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_SetRadioMode);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetAssociatedDeviceDetail", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER, "devIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetAssociatedDeviceDetail);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetBasicTrafficStats", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetBasicTrafficStats);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetWifiTrafficStats", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetWifiTrafficStats);
            this->bindAndAddMethod(Procedure("WIFIHAL_SteeringClientDisconnect", PARAMS_BY_NAME, JSON_STRING, "steeringgroupIndex", JSON_INTEGER, "apIndex", JSON_INTEGER, "clientMAC", JSON_STRING, "disconnectType", JSON_INTEGER, "reason", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SteeringClientDisconnect);
            this->bindAndAddMethod(Procedure("WIFIHAL_SteeringClientSet", PARAMS_BY_NAME, JSON_STRING, "steeringgroupIndex", JSON_INTEGER, "apIndex", JSON_INTEGER, "clientMAC", JSON_STRING, "rssiProbeHWM", JSON_INTEGER, "rssiProbeLWM", JSON_INTEGER, "rssiAuthHWM", JSON_INTEGER, "rssiAuthLWM", JSON_INTEGER, "rssiInactXing", JSON_INTEGER, "rssiHighXing", JSON_INTEGER, "rssiLowXing", JSON_INTEGER, "authRejectReason", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SteeringClientSet);
            this->bindAndAddMethod(Procedure("WIFIHAL_SteeringClientRemove", PARAMS_BY_NAME, JSON_STRING, "steeringgroupIndex", JSON_INTEGER, "apIndex", JSON_INTEGER, "clientMAC", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_SteeringClientRemove);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetBTMClientCapabilityList", PARAMS_BY_NAME, JSON_STRING, "count", JSON_INTEGER, "apIndex", JSON_INTEGER, "clientMAC", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetBTMClientCapabilityList);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApRoamingConsortiumElement", PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetApRoamingConsortiumElement);
            this->bindAndAddMethod(Procedure("WIFIHAL_PushApRoamingConsortiumElement", PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "ouiCount", JSON_INTEGER, "ouiList", JSON_STRING, "ouiLen", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_PushApRoamingConsortiumElement);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetBSSColorValue", PARAMS_BY_NAME, JSON_STRING,"radioIndex", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetBSSColorValue);
            this->bindAndAddMethod(Procedure("WIFIHAL_ApplyGASConfiguration",PARAMS_BY_NAME, JSON_STRING, "advertisementID", JSON_INTEGER, "pauseForServerResponse", JSON_INTEGER, "responseTimeout", JSON_INTEGER, "comeBackDelay", JSON_INTEGER, "responseBufferingTime", JSON_INTEGER, "queryResponseLengthLimit", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_ApplyGASConfiguration);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApInterworkingElement", PARAMS_BY_NAME, JSON_STRING,"radioIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetApInterworkingElement);
            this->bindAndAddMethod(Procedure("WIFIHAL_PushApInterworkingElement",PARAMS_BY_NAME, JSON_STRING, "radioIndex", JSON_INTEGER, "interworkingEnabled", JSON_INTEGER, "accessNetworkType", JSON_INTEGER, "internetAvailable", JSON_INTEGER, "asra", JSON_INTEGER, "esra", JSON_INTEGER, "uesa", JSON_INTEGER, "venueOptionPresent", JSON_INTEGER, "venueType", JSON_INTEGER, "venueGroup", JSON_INTEGER, "hessOptionPresent", JSON_INTEGER, "hessid", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_PushApInterworkingElement);
            this->bindAndAddMethod(Procedure("WIFIHAL_EnableCSIEngine",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "MacAddress", JSON_STRING, "enable", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_EnableCSIEngine);
            this->bindAndAddMethod(Procedure("WIFIHAL_SendDataFrame",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "MacAddress", JSON_STRING, "length", JSON_INTEGER, "insert_llc", JSON_INTEGER, "protocol", JSON_INTEGER, "priority", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SendDataFrame);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetVAPTelemetry", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetVAPTelemetry);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioVapInfoMap", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetRadioVapInfoMap);
            this->bindAndAddMethod(Procedure("WIFIHAL_SetNeighborReports",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "reports", JSON_INTEGER, "bssid", JSON_STRING, "info", JSON_INTEGER, "opClass", JSON_INTEGER, "channel", JSON_INTEGER, "phyTable", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SetNeighborReports);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedClientDiagnosticResult",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "mac_addr", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetApAssociatedClientDiagnosticResult);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetAPCapabilities",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetAPCapabilities);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetAvailableBSSColor",PARAMS_BY_NAME, JSON_STRING, "radioIndex", JSON_INTEGER, "maxNumberColors", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetAvailableBSSColor);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetFTMobilityDomainID",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "radioIndex", JSON_INTEGER, "mobilityDomain", JSON_INTEGER, "methodName", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetOrSetFTMobilityDomainID);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetFTR0KeyHolderID",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "radioIndex", JSON_INTEGER, "KeyHolderID", JSON_STRING, "methodName", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetOrSetFTR0KeyHolderID);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetRMCapabilities",PARAMS_BY_NAME, JSON_STRING, "peer", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetRMCapabilities);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApSecurity",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetApSecurity);
            this->bindAndAddMethod(Procedure("WIFIHAL_SetApSecurity",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "mode", JSON_INTEGER, "mfp", JSON_INTEGER, "encr", JSON_INTEGER, "key_type", JSON_INTEGER, "key", JSON_STRING, "wpa3_transition_disable", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SetApSecurity);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetApWpsConfiguration",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetApWpsConfiguration);
            this->bindAndAddMethod(Procedure("WIFIHAL_SetApWpsConfiguration",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "radioIndex", JSON_INTEGER, "enable", JSON_INTEGER, "pin", JSON_STRING, "methods", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SetApWpsConfiguration);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetFTR1KeyHolderID",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "radioIndex", JSON_INTEGER, "KeyHolderID", JSON_STRING, "methodName", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetOrSetFTR1KeyHolderID);
            this->bindAndAddMethod(Procedure("WIFIHAL_SetBSSColor",PARAMS_BY_NAME, JSON_STRING, "radioIndex", JSON_INTEGER, "color", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SetBSSColor);
            this->bindAndAddMethod(Procedure("WIFIHAL_PushApFastTransitionConfig",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "support", JSON_INTEGER, "mobilityDomain", JSON_INTEGER, "overDS", JSON_INTEGER, "radioIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_PushApFastTransitionConfig);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetMuEdca",PARAMS_BY_NAME, JSON_STRING, "radioIndex", JSON_INTEGER, "accessCategory", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetMuEdca);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioOperatingParameters",PARAMS_BY_NAME, JSON_STRING, "radioIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetRadioOperatingParameters);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioChannels",PARAMS_BY_NAME, JSON_STRING, "radioIndex", JSON_INTEGER, "numberOfChannels", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetRadioChannels);
            this->bindAndAddMethod(Procedure("WIFIHAL_GetEAPParam",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetEAPParam);
        }

        /*inherited functions*/
        bool initialize(IN const char* szVersion);
        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

        /*WIFIHAL Stub Wrapper functions*/
        void WIFIHAL_GetOrSetParamULongValue(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetParamBoolValue(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetParamStringValue(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetRadioStandard(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetParamIntValue(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetParamUIntValue(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetIndexFromName(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApIndexFromName(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_ClearRadioResetCount(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_Reset(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetSecurityRadiusServer(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetApBridgeInfo(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetRadioDCSScanTime(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_AddorDelApAclDevice(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_IfConfigUporDown(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_ParamRadioIndex(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_StartorStopHostApd(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_FactoryReset(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetSecurityRadiusSettings(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetSSIDTrafficStats2(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRadioTrafficStats2(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_Down(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_Init(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_CreateInitialConfigFiles(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceDiagnosticResult(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetNeighboringWiFiDiagnosticResult2(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_PushRadioChannel2(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetNeighboringWiFiStatus(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRadioChannelStats(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_ParamApIndex(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDevice(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApDeviceRSSI(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_DelApAclDevices(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAclDevices(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRadioChannelStats2 (IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceTxStatsResult(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceRxStatsResult(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApDeviceTxRxRate(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceStats(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetApScanFilter(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_CreateAp(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceDiagnosticResult3(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_StartNeighborScan(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceTidStatsResult(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetBandSteeringLog(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceDiagnosticResult2(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRadioMode(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetRadioMode(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetAssociatedDeviceDetail(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetBasicTrafficStats(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetWifiTrafficStats(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SteeringClientDisconnect(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SteeringClientSet(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SteeringClientRemove(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetBTMClientCapabilityList(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApRoamingConsortiumElement(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_PushApRoamingConsortiumElement(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetBSSColorValue(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_ApplyGASConfiguration(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApInterworkingElement(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_PushApInterworkingElement(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_EnableCSIEngine(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SendDataFrame(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetVAPTelemetry(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRadioVapInfoMap(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetNeighborReports(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedClientDiagnosticResult(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetAPCapabilities(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetAvailableBSSColor(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetFTMobilityDomainID(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetFTR0KeyHolderID(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRMCapabilities(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApSecurity(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetApSecurity(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApWpsConfiguration(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetApWpsConfiguration(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetFTR1KeyHolderID(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetBSSColor(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_PushApFastTransitionConfig(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetMuEdca(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRadioOperatingParameters(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRadioChannels(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetEAPParam(IN const Json::Value& req, OUT Json::Value& response);
};

#endif //__WIFIHAL_STUB_H__
