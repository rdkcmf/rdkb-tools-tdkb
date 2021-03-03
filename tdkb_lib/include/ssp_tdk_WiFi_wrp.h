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

#include <stdint.h>
#include "wifi_hal.h"
#define SSP_SUCCESS       0
#define SSP_FAILURE       1

int ssp_wifi_init();
int ssp_WIFIHALApplySettings(int radioIndex, char* methodName);
int ssp_WIFIHALGetOrSetParamULongValue(int radioIndex, unsigned long *uLongVar, char* methodName);
int ssp_WIFIHALGetOrSetParamBoolValue(int radioIndex, unsigned char *enable, char* method);
int ssp_WIFIHALGetOrSetParamStringValue(int radioIndex, char* output, char* method);
int ssp_WIFIHALGetOrSetRadioStandard(int radioIndex, char* output, char* method, unsigned char *gOnly, unsigned char *nOnly, unsigned char *acOnly);
int ssp_WIFIHALGetOrSetParamIntValue(int radioIndex, int* output, char* method);
int ssp_WIFIHALGetIndexFromName(char* ssidName, int* output);
int ssp_WIFIHALGetApIndexFromName(char* ssidName, int* output);
int ssp_WIFIHALClearRadioResetCount();
int ssp_WIFIHALReset();
int ssp_WIFIHALGetOrSetSecurityRadiusServer(int radioIndex, char* IPAddress, unsigned int* port, char* RadiusSecret, char* method);
int ssp_WIFIHALGetOrSetApBridgeInfo(int radioIndex, char* bridgeName, char* IP, char* subnet, char* method);
int ssp_WIFIHALGetOrSetRadioDCSScanTime(int radioIndex, int* output_interval_seconds,int* output_dwell_milliseconds, char* methodName);
int ssp_WIFIHALAddorDelApAclDevice(int apIndex, char* DeviceMacAddress, char* method);
int ssp_WIFIHALIfConfigUporDown(int apIndex, char* method);
int ssp_WIFIHALParamRadioIndex(int radioIndex, char* method);
int ssp_WIFIHALStartorStopHostApd(char* method);
int ssp_WIFIHALFactoryReset(char* method);
int ssp_WIFIHALGetOrSetSecurityRadiusSettings(int radioIndex, wifi_radius_setting_t *radiusSetting, char* method);
int ssp_WIFIHALGetSSIDTrafficStats2(int radioIndex,  wifi_ssidTrafficStats2_t *ssidTrafficStats2);
int ssp_WIFIHALGetRadioTrafficStats2(int radioIndex, wifi_radioTrafficStats2_t *TrafficStats2);
int ssp_WIFIHALDown();
int ssp_WIFIHALCreateInitialConfigFiles();
int ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult(int radioIndex, wifi_associated_dev_t **associated_dev, unsigned int *output_array_size);
int ssp_WIFIHALGetNeighboringWiFiDiagnosticResult2(int radioIndex, wifi_neighbor_ap2_t **neighbor_ap2, unsigned int *output_array_size);
int ssp_WIFIHALPushRadioChannel2(int radioIndex, unsigned int channel,unsigned int channel_width_MHz,unsigned int csa_beacon_count);
int ssp_WIFIHALGetNeighboringWiFiStatus(int radioIndex, wifi_neighbor_ap2_t **neighbor_ap2, unsigned int *output_array_size);
int ssp_WIFIHALGetRadioChannelStats(int radioIndex,  wifi_channelStats_t *channelStats, int array_size);
int ssp_WIFIHALParamApIndex(int apIndex, char* method);
int ssp_WIFIHALGetApAssociatedDevice(int apIndex, char* associated_dev , unsigned int output_array_size);
int ssp_WIFIHALGetApDeviceRSSI(int ap_index, char *MAC, int *output_RSSI, char* method);
int ssp_WIFIHALGetApDeviceTxRxRate(int apIndex, char *MAC, int *output_TxRxMb, char* method);
int ssp_WIFIHALDelApAclDevices(int apIndex);
int ssp_WIFIHALGetApAclDevices(int apIndex, char *mac_addr, unsigned int output_array_size);
int ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult3(int apIndex, wifi_associated_dev3_t **associated_dev_array, unsigned int *output_array_size);
int ssp_WIFIHAL_CreateAp(int apIndex, int radioIndex, char *essid, unsigned char hideSsid);
int ssp_WIFIHALGetApAssociatedDeviceStats(int apIndex, mac_address_t *clientMacAddress, wifi_associated_dev_stats_t *associated_dev_stats, unsigned long long *handle);
int ssp_WIFIHALSetApScanFilter(int apIndex, int mode, char* essid, char *method);
int ssp_WIFIHALGetApAssociatedDeviceRxStatsResult(int radioIndex, mac_address_t *clientMacAddress, wifi_associated_dev_rate_info_rx_stats_t **stats_array, unsigned int *output_array_size, unsigned long long *handle);
int ssp_WIFIHALGetApAssociatedDeviceTxStatsResult(int radioIndex, mac_address_t *clientMacAddress, wifi_associated_dev_rate_info_tx_stats_t **stats_array, unsigned int *output_array_size, unsigned long long *handle);
int ssp_WIFIHALGetRadioChannelStats2(int radioIndex, wifi_channelStats2_t *outputChannelStats2);
int ssp_WIFIHALStartNeighborScan(int apIndex, wifi_neighborScanMode_t scan_mode, int dwell_time, unsigned int chan_num, unsigned int* chan_list);
int ssp_WIFIHALGetApAssociatedDeviceTidStatsResult(int radioIndex,  mac_address_t *clientMacAddress, wifi_associated_dev_tid_stats_t *tid_stats, unsigned long long *handle);
int ssp_WIFIHALGetBandSteeringLog(int  record_index, unsigned long *pSteeringTime, char  *pClientMAC, int *pSourceSSIDIndex, int *pDestSSIDIndex, int *pSteeringReason);
int ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult2(int apIndex, wifi_associated_dev2_t **associated_dev_array, unsigned int *dev_cnt);
int ssp_WIFIHALGetRadioMode(int radioIndex, char* output_string, unsigned int *puremode);
int ssp_WIFIHALSetRadioMode(int radioIndex, char* output_string, unsigned int puremode);
int ssp_WIFIHALGetAssociatedDeviceDetail(int apIndex, int devIndex, wifi_device_t *dev);
int ssp_WIFIHALGetBasicTrafficStats(int apIndex, wifi_basicTrafficStats_t *output_struct);
int ssp_WIFIHALGetWifiTrafficStats(int apIndex, wifi_trafficStats_t *output_struct);
int ssp_WIFIHALSteeringClientDisconnect(unsigned int steeringgroupIndex, int apIndex, mac_address_t client_mac, wifi_disconnectType_t type, unsigned int reason);
int ssp_WIFIHALSteeringClientSet(unsigned int steeringgroupIndex, int apIndex, mac_address_t client_mac, wifi_steering_clientConfig_t *cli_cfg);
int ssp_WIFIHALSteeringClientRemove(unsigned int steeringgroupIndex, int apIndex, mac_address_t client_mac);
int ssp_WIFIHALGetBTMClientCapabilityList(int apIndex, wifi_BTMCapabilities_t* btm_caps);
int ssp_WIFIHALGetApRoamingConsortiumElement(int apIndex, wifi_roamingConsortiumElement_t* roam);
int ssp_WIFIHALPushApRoamingConsortiumElement(int apIndex, wifi_roamingConsortiumElement_t* roam);
int ssp_WIFIHALGetBSSColorValue(int radioIndex, unsigned char *color);
int ssp_WIFIHALApplyGASConfiguration(wifi_GASConfiguration_t *GASConfiguration);
