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

#include "WIFIHAL.h"
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALApplySettings
 * Description          : This function invokes WiFi hal api wifi_applyRadioSettings
 * @param [in] req-     : radioIndex - radio index value of wifi
                          methodName - name of the wifi hal api to be invoked
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
int ssp_WIFIHALApplySettings(int radioIndex, char* methodName)
{
    printf("\n ssp_WIFIHALApplySettings-----> Entry\n");
    printf("Radio/SSID index:%d\n",radioIndex);
    printf("MethodName: %s\n", methodName);
    int return_status = SSP_SUCCESS;

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;
    strncpy(apiInfo.api_name, "wifi_apply", 1024);
    return_status = wifi_api_send_msg(&apiInfo);
    if (return_status == RETURN_OK) {
        printf("wifi_apply complete.\n");
    }
    printf("return value from wifi_apply is %d\n",return_status);
    #else

    if(strstr(methodName, "setRadio")||strstr(methodName, "setAp")||strstr(methodName, "setBandSteering")||strstr(methodName, "wifi_down"))
    {
        return_status = wifi_applyRadioSettings(radioIndex);
        printf("return value from wifi_applyRadioSettings is %d\n",return_status);
    }
    else if(strstr(methodName, "setSSID"))
    {
        return_status = wifi_applySSIDSettings(radioIndex);
        printf("return value from wifi_applySSIDSettings is %d\n",return_status);
    }

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALApplySettings::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALApplySettings::Success\n");
    }
    printf("\n ssp_WIFIHALApplySettings----> Exit\n");
    #endif
    return return_status;
}

/********************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetOrSetParamBoolValue
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is Bool
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : enable     - the value to be get/set
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetParamBoolValue(int radioIndex, unsigned char *enable, char* method)
{
    printf("\n ssp_WIFIHALGetOrSetParamBoolValue----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    if(enable)
        printf("GetorSetParam: %d\n" , *enable);
    else
        printf("Validation with NULL buffer\n");
    printf("MethodName: %s\n", method);
    int return_status = SSP_FAILURE;

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;
    char api_name[200] = "wifi_";
    strcat(api_name, method);

    if(isSockSetApi(api_name)){
        printf("is sock api\n");
        strncpy(apiInfo.api_name, api_name, 1024);
        if(enable)
            snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%d",*enable);
        else
            return SSP_FAILURE;
        apiInfo.radioIndex = radioIndex;
        return_status = wifi_api_send_msg(&apiInfo);
        printf("\n ssp_WIFIHALGetOrSetParamBoolValue----> Exit, ret:status %d \n", return_status);
        return return_status;
    }
    #endif

    if(!strcmp(method, "getRadioEnable"))
        return_status = wifi_getRadioEnable(radioIndex, enable);
    else if(!strcmp(method, "setRadioEnable"))
        return_status = wifi_setRadioEnable(radioIndex, *enable);
    else if(!strcmp(method, "getSSIDEnable"))
        return_status = wifi_getSSIDEnable(radioIndex, enable);
    else if(!strcmp(method, "setSSIDEnable"))
        return_status = wifi_setSSIDEnable(radioIndex, *enable);
    else if(!strcmp(method, "getRadioDCSSupported"))
        return_status = wifi_getRadioDCSSupported(radioIndex, enable);
    else if(!strcmp(method, "getRadioDCSEnable"))
        return_status = wifi_getRadioDCSEnable(radioIndex, enable);
    else if(!strcmp(method, "setRadioDCSEnable"))
        return_status = wifi_setRadioDCSEnable(radioIndex, *enable);
    else if(!strcmp(method, "getRadioDFSSupported"))
        return_status = wifi_getRadioDfsSupport(radioIndex, enable);
    else if(!strcmp(method, "getRadioDFSEnable"))
        return_status = wifi_getRadioDfsEnable(radioIndex, enable);
    else if(!strcmp(method, "setRadioDfsEnable"))
        return_status = wifi_setRadioDfsEnable(radioIndex, *enable);
    else if(!strcmp(method, "getAutoChannelRefreshPeriodSupported"))
        return_status = wifi_getRadioAutoChannelRefreshPeriodSupported(radioIndex, enable);
    else if(!strcmp(method, "setRadioAutoChannelEnable"))
        return_status = wifi_setRadioAutoChannelEnable(radioIndex, *enable);
    else if(!strcmp(method, "getAutoChannelEnable"))
        return_status = wifi_getRadioAutoChannelEnable(radioIndex, enable);
    else if(!strcmp(method, "getAutoChannelSupported"))
        return_status = wifi_getRadioAutoChannelSupported(radioIndex, enable);
    else if(!strcmp(method, "getRadioStatus"))
        return_status = wifi_getRadioStatus(radioIndex,enable);
    else if(!strcmp(method, "getApEnable"))
        return_status = wifi_getApEnable(radioIndex,enable);
    else if(!strcmp(method, "setApEnable"))
        return_status = wifi_setApEnable(radioIndex, *enable);
    else if(!strcmp(method, "getApIsolationEnable"))
        return_status = wifi_getApIsolationEnable(radioIndex,enable);
    else if(!strcmp(method, "setApIsolationEnable"))
        return_status = wifi_setApIsolationEnable(radioIndex, *enable);
    else if(!strcmp(method, "getRadioIEEE80211hSupported"))
        return_status = wifi_getRadioIEEE80211hSupported(radioIndex,enable);
    else if(!strcmp(method, "getRadioIEEE80211hEnabled"))
        return_status = wifi_getRadioIEEE80211hEnabled(radioIndex,enable);
    else if(!strcmp(method, "setRadioIEEE80211hEnabled"))
        return_status = wifi_setRadioIEEE80211hEnabled(radioIndex, *enable);
    else if(!strcmp(method, "getBandSteeringCapability"))
        return_status = wifi_getBandSteeringCapability(enable);
    else if(!strcmp(method, "getBandSteeringEnable"))
        return_status = wifi_getBandSteeringEnable(enable);
    else if(!strcmp(method, "setBandSteeringEnable"))
        return_status = wifi_setBandSteeringEnable(*enable);
    else if(!strcmp(method, "getRadioReverseDirectionGrantSupported"))
        return_status = wifi_getRadioReverseDirectionGrantSupported(radioIndex,enable);
    else if(!strcmp(method, "getRadioReverseDirectionGrantEnable"))
        return_status = wifi_getRadioReverseDirectionGrantEnable(radioIndex,enable);
    else if(!strcmp(method, "setRadioReverseDirectionGrantEnable"))
        return_status = wifi_setRadioReverseDirectionGrantEnable(radioIndex, *enable);
    else if(!strcmp(method, "getRadioDeclineBARequestEnable"))
        return_status = wifi_getRadioDeclineBARequestEnable(radioIndex, enable);
    else if(!strcmp(method, "setRadioDeclineBARequestEnable"))
        return_status = wifi_setRadioDeclineBARequestEnable(radioIndex,*enable);
    else if(!strcmp(method, "getRadioAutoBlockAckEnable"))
        return_status = wifi_getRadioAutoBlockAckEnable(radioIndex,enable);
    else if(!strcmp(method, "setRadioAutoBlockAckEnable"))
        return_status = wifi_setRadioAutoBlockAckEnable(radioIndex, *enable);
    else if(!strcmp(method, "getRadio11nGreenfieldSupported"))
        return_status = wifi_getRadio11nGreenfieldSupported(radioIndex,enable);
    else if(!strcmp(method, "getRadio11nGreenfieldEnable"))
        return_status = wifi_getRadio11nGreenfieldEnable(radioIndex,enable);
    else if(!strcmp(method, "setRadio11nGreenfieldEnable"))
        return_status = wifi_setRadio11nGreenfieldEnable(radioIndex, *enable);
    else if(!strcmp(method, "getRadioIGMPSnoopingEnable"))
        return_status = wifi_getRadioIGMPSnoopingEnable(radioIndex,enable);
    else if(!strcmp(method, "setRadioIGMPSnoopingEnable"))
        return_status = wifi_setRadioIGMPSnoopingEnable(radioIndex,*enable);
    else if(!strcmp(method, "getApRtsThresholdSupported"))
        return_status = wifi_getApRtsThresholdSupported(radioIndex,enable);
    else if(!strcmp(method, "getApSsidAdvertisementEnable"))
        return_status = wifi_getApSsidAdvertisementEnable(radioIndex,enable);
    else if(!strcmp(method, "setApSsidAdvertisementEnable"))
        return_status = wifi_setApSsidAdvertisementEnable(radioIndex, *enable);
    else if(!strcmp(method, "getApWMMCapability"))
        return_status = wifi_getApWMMCapability(radioIndex,enable);
    else if(!strcmp(method, "getApUAPSDCapability"))
        return_status = wifi_getApUAPSDCapability(radioIndex,enable);
    else if(!strcmp(method, "getApWmmEnable"))
        return_status = wifi_getApWmmEnable(radioIndex,enable);
    else if(!strcmp(method, "setApWmmEnable"))
        return_status = wifi_setApWmmEnable(radioIndex, *enable);
    else if(!strcmp(method, "getApWmmUapsdEnable"))
        return_status = wifi_getApWmmUapsdEnable(radioIndex,enable);
    else if(!strcmp(method, "setApWmmUapsdEnable"))
        return_status = wifi_setApWmmUapsdEnable(radioIndex, *enable);
    else if(!strcmp(method, "getApWpsEnable"))
        return_status = wifi_getApWpsEnable(radioIndex,enable);
    else if(!strcmp(method, "setApWpsEnable"))
        return_status = wifi_setApWpsEnable(radioIndex,*enable);
    else if(!strcmp(method, "getRadioAMSDUEnable"))
        return_status = wifi_getRadioAMSDUEnable(radioIndex, enable);
    else if(!strcmp(method, "setRadioAMSDUEnable"))
        return_status = wifi_setRadioAMSDUEnable(radioIndex, *enable);
    else if(!strcmp(method, "getApRtsThresholdSupported"))
        return_status = wifi_getApRtsThresholdSupported(radioIndex, enable);
    else if(!strcmp(method, "pushSsidAdvertisementEnable"))
        return_status = wifi_pushSsidAdvertisementEnable(radioIndex, *enable);
    else if(!strcmp(method, "setRadioCtsProtectionEnable"))
        return_status = wifi_setRadioCtsProtectionEnable(radioIndex, *enable);
    else if(!strcmp(method, "setRadioObssCoexistenceEnable"))
        return_status = wifi_setRadioObssCoexistenceEnable(radioIndex, *enable);
    else if(!strcmp(method, "setRadioSTBCEnable"))
        return_status = wifi_setRadioSTBCEnable(radioIndex, *enable);
    else if(!strcmp(method, "getDeclineBARequestEnable"))
        return_status = wifi_getDeclineBARequestEnable(radioIndex, enable);
    else if(!strcmp(method, "setDeclineBARequestEnable"))
        return_status = wifi_setDeclineBARequestEnable(radioIndex, *enable);
    else if(!strcmp(method, "getDfsEnable"))
        return_status = wifi_getDfsEnable(radioIndex, enable);
    else if(!strcmp(method, "setDfsEnable"))
        return_status = wifi_setDfsEnable(radioIndex, *enable);
    else if(!strcmp(method, "pushSsidAdvertisementEnable"))
        return_status = wifi_pushSsidAdvertisementEnable(radioIndex, *enable);
    else if(!strcmp(method, "createHostApdConfig"))
        return_status = wifi_createHostApdConfig(radioIndex, *enable);
    else if(!strcmp(method, "kickApAclAssociatedDevices"))
        return_status = wifi_kickApAclAssociatedDevices(radioIndex, *enable);
    else if(!strcmp(method, "setRadioTrafficStatsRadioStatisticsEnable"))
        return_status = wifi_setRadioTrafficStatsRadioStatisticsEnable(radioIndex, *enable);
    else if(!strcmp(method, "getRadioStatsEnable"))
        return_status = wifi_getRadioStatsEnable(radioIndex, enable);
    else if(!strcmp(method, "setRadioStatsEnable"))
        return_status = wifi_setRadioStatsEnable(radioIndex, *enable);
    else if(!strcmp(method, "getRadioDcsScanning"))
        return_status = wifi_getRadioDcsScanning(radioIndex, enable);
    else if(!strcmp(method, "setRadioDcsScanning"))
        return_status = wifi_setRadioDcsScanning(radioIndex, *enable);
    else if(!strcmp(method, "pushApEnable"))
        return_status = wifi_pushApEnable(radioIndex,*enable);
    else if(!strcmp(method, "pushApSsidAdvertisementEnable"))
        return_status = wifi_pushApSsidAdvertisementEnable(radioIndex, *enable);
    else if(!strcmp(method, "getATMCapable"))
        return_status = wifi_getATMCapable(enable);
    else if(!strcmp(method, "getBSSTransitionImplemented"))
        return_status = wifi_getBSSTransitionImplemented(radioIndex,enable);
    else if(!strcmp(method, "getBSSTransitionActivation"))
        return_status = wifi_getBSSTransitionActivation(radioIndex,enable);
    else if(!strcmp(method, "setCountryIe"))
        return_status = wifi_setCountryIe(radioIndex, *enable);
    else if(!strcmp(method, "setLayer2TrafficInspectionFiltering"))
        return_status = wifi_setLayer2TrafficInspectionFiltering(radioIndex, *enable);
    else if(!strcmp(method, "setDownStreamGroupAddress"))
        return_status = wifi_setDownStreamGroupAddress(radioIndex, *enable);
    else if(!strcmp(method, "setBssLoad"))
        return_status = wifi_setBssLoad(radioIndex, *enable);
    else if(!strcmp(method, "setProxyArp"))
        return_status = wifi_setProxyArp(radioIndex, *enable);
    else if(!strcmp(method, "pushApHotspotElement"))
        return_status = wifi_pushApHotspotElement(radioIndex, *enable);
    else if(!strcmp(method, "setP2PCrossConnect"))
        return_status = wifi_setP2PCrossConnect(radioIndex, *enable);
/*    else if(!strcmp(method, "getAtmBandEnable"))
    {
        if(enable)
           return_status = wifi_getAtmBandEnable(radioIndex, enable);
        else
            return_status = wifi_getAtmBandEnable(radioIndex, NULL);
    }*/
    else if(!strcmp(method, "getATMEnable"))
    {
        if(enable)
           return_status = wifi_getATMEnable(enable);
        else
            return_status = wifi_getATMEnable(NULL);
    }
    else if(!strcmp(method, "setATMEnable"))
    {
        if(enable)
           return_status = wifi_setATMEnable(*enable);
        else
            return_status = wifi_setATMEnable(0);
    }
    else if(!strcmp(method, "getCountryIe"))
    {
        if(enable)
            return_status = wifi_getCountryIe(radioIndex, enable);
        else
            return_status = wifi_getCountryIe(radioIndex, NULL);
    }
    else if(!strcmp(method, "getLayer2TrafficInspectionFiltering"))
    {
        if(enable)
            return_status = wifi_getLayer2TrafficInspectionFiltering(radioIndex, enable);
        else
            return_status = wifi_getLayer2TrafficInspectionFiltering(radioIndex, NULL);
    }
    else if(!strcmp(method, "getDownStreamGroupAddress"))
    {
        if(enable)
            return_status = wifi_getDownStreamGroupAddress(radioIndex, enable);
        else
            return_status = wifi_getDownStreamGroupAddress(radioIndex, NULL);
    }
    else if(!strcmp(method, "getBssLoad"))
    {
        if(enable)
            return_status = wifi_getBssLoad(radioIndex, enable);
        else
            return_status = wifi_getBssLoad(radioIndex, NULL);
    }
    else if(!strcmp(method, "getProxyArp"))
    {
        if(enable)
            return_status = wifi_getProxyArp(radioIndex, enable);
        else
            return_status = wifi_getProxyArp(radioIndex, NULL);
    }
    else if(!strcmp(method, "getApHotspotElement"))
    {
        if(enable)
            return_status = wifi_getApHotspotElement(radioIndex, enable);
        else
            return_status = wifi_getApHotspotElement(radioIndex, NULL);
    }
    else if(!strcmp(method, "getP2PCrossConnect"))
    {
        if(enable)
            return_status = wifi_getP2PCrossConnect(radioIndex, enable);
        else
            return_status = wifi_getP2PCrossConnect(radioIndex, NULL);
    }
    else if(!strcmp(method, "getBSSColorEnabled"))
    {
        if(enable)
            return_status = wifi_getBSSColorEnabled(radioIndex, enable);
        else
            return_status = wifi_getBSSColorEnabled(radioIndex, NULL);
    }
    else if(!strcmp(method, "setBSSColorEnabled"))
        return_status = wifi_setBSSColorEnabled(radioIndex, *enable);
    else if(!strcmp(method, "getAutoBlockAckEnable"))
    {
        if(enable)
            return_status = wifi_getAutoBlockAckEnable(radioIndex, enable);
        else
            return_status = wifi_getAutoBlockAckEnable(radioIndex, NULL);
    }
    else if(!strcmp(method, "setAutoBlockAckEnable"))
        return_status = wifi_setAutoBlockAckEnable(radioIndex, *enable);
    else if(!strcmp(method, "getApInterworkingServiceEnable"))
    {
        if(enable)
            return_status = wifi_getApInterworkingServiceEnable(radioIndex, enable);
        else
            return_status = wifi_getApInterworkingServiceEnable(radioIndex, NULL);
    }
    else if(!strcmp(method, "setApInterworkingServiceEnable"))
        return_status = wifi_setApInterworkingServiceEnable(radioIndex, *enable);
    else if(!strcmp(method, "getApInterworkingServiceCapability"))
    {
        if(enable)
            return_status = wifi_getApInterworkingServiceCapability(radioIndex, enable);
        else
            return_status = wifi_getApInterworkingServiceCapability(radioIndex, NULL);
    }
    else if(!strcmp(method, "enableGreylistAccessControl"))
        return_status = wifi_enableGreylistAccessControl(*enable);
    else if(!strcmp(method, "setClientDetailedStatisticsEnable"))
        return_status = wifi_setClientDetailedStatisticsEnable(radioIndex, *enable);
    else if(!strcmp(method, "getNeighborReportActivation"))
    {
        if(enable)
            return_status = wifi_getNeighborReportActivation(radioIndex, enable);
        else
            return_status = wifi_getNeighborReportActivation(radioIndex, NULL);
    }

    else if(!strcmp(method, "setNeighborReportActivation"))
        return_status = wifi_setNeighborReportActivation(radioIndex, *enable);
    else if(!strcmp(method, "getFTOverDSActivated"))
    {
        if(enable)
            return_status = wifi_getFTOverDSActivated(radioIndex, enable);
        else
            return_status = wifi_getFTOverDSActivated(radioIndex, NULL);
    }
    else if(!strcmp(method, "setFTOverDSActivated"))
        return_status = wifi_setFTOverDSActivated(radioIndex, enable);
    else if(!strcmp(method, "getBSSTransitionActivated"))
    {
        if(enable)
            return_status = wifi_getBSSTransitionActivated(radioIndex, enable);
        else
            return_status = wifi_getBSSTransitionActivated(radioIndex, NULL);
    }
    else if(!strcmp(method, "setFastBSSTransitionActivated"))
        return_status = wifi_setFastBSSTransitionActivated(radioIndex, *enable);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WIFIHALGetOrSetParamBoolValue: Invalid methodName\n");
    }
    if(enable)
        printf("ssp_WIFIHALGetOrSetParamBoolValue: Enable status is %d\n", *enable);
    printf("\n ssp_WIFIHALGetOrSetParamBoolValue----> Exit, ret:status %d \n", return_status);
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WiFiHalCallMethodForULong
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is Unsigned long
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : enable     - the value to be get/set
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_WIFIHALGetOrSetParamULongValue(int radioIndex, unsigned long *uLongVar, char* method)
{
    printf("\n ssp_WIFIHALGetOrSetParamULongValue-----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    if(uLongVar)
        printf("GetorSetParam: %lu\n" , *uLongVar);
    printf("MethodName: %s\n", method);
    int return_status = SSP_FAILURE;

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;
    char api_name[200] = "wifi_";
    strcat(api_name, method);

    if(isSockSetApi(api_name)){
        printf("is sock api\n");
        strncpy(apiInfo.api_name, api_name, 1024);
        if(uLongVar)
            snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%lu",*uLongVar);
        else
            return SSP_FAILURE;
        apiInfo.radioIndex = radioIndex;
        return_status = wifi_api_send_msg(&apiInfo);
        printf("\n ssp_WIFIHALGetOrSetParamULongValue---> Exit, ret:status %d \n", return_status);
        return return_status;
    }
    #endif

    if(!strcmp(method, "getRadioChannel"))
        return_status = wifi_getRadioChannel(radioIndex, uLongVar);
    else if(!strcmp(method, "setRadioChannel"))
        return_status = wifi_setRadioChannel(radioIndex, *uLongVar);
    else if(!strcmp(method, "getAutoChannelRefreshPeriod"))
        return_status = wifi_getRadioAutoChannelRefreshPeriod(radioIndex, uLongVar);
    else if(!strcmp(method, "setRadioAutoChannelRefreshPeriod"))
        return_status = wifi_setRadioAutoChannelRefreshPeriod(radioIndex, *uLongVar);
    else if(!strcmp(method, "setRadioDfsRefreshPeriod"))
        return_status = wifi_setRadioDfsRefreshPeriod(radioIndex, *uLongVar);
    else if(!strcmp(method, "getRadioNumberOfEntries"))
        return_status = wifi_getRadioNumberOfEntries(uLongVar);
    else if(!strcmp(method, "getSSIDNumberOfEntries"))
        return_status = wifi_getSSIDNumberOfEntries(uLongVar);
    else if(!strcmp(method, "getRadioTransmitPower"))
        return_status = wifi_getRadioTransmitPower(radioIndex, uLongVar);
    else if(!strcmp(method, "setRadioTransmitPower"))
        return_status = wifi_setRadioTransmitPower(radioIndex, *uLongVar);
    else if(!strcmp(method, "getApNumDevicesAssociated"))
        return_status = wifi_getApNumDevicesAssociated(radioIndex, uLongVar);
    else if(!strcmp(method, "getApWpsDevicePIN"))
        return_status = wifi_getApWpsDevicePIN(radioIndex, uLongVar);
    else if(!strcmp(method, "setApWpsDevicePIN"))
        return_status = wifi_setApWpsDevicePIN(radioIndex, *uLongVar);
    else if(!strcmp(method, "getRadioUpTime"))
        return_status = wifi_getRadioUpTime(radioIndex, uLongVar);
    else if(!strcmp(method, "getApAssociatedDevicesHighWatermarkDate"))
        return_status = wifi_getApAssociatedDevicesHighWatermarkDate(radioIndex, uLongVar);
    else if(!strcmp(method, "getRadioResetCount"))
        return_status = wifi_getRadioResetCount(radioIndex, uLongVar);
    else if(!strcmp(method, "getRadioPercentageTransmitPower"))
        return_status = wifi_getRadioPercentageTransmitPower(radioIndex, uLongVar);
    else if(!strcmp(method, "getRadioAbsoluteTransmitPower_priv"))
        return_status = wifi_getRadioAbsoluteTransmitPower_priv(radioIndex, uLongVar);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForULong: Invalid methodName\n");
    }

    if(uLongVar)
        printf("ssp_WiFiHalCallMethodForULong:: return value is %lu\n", *uLongVar);
    printf("ssp_WiFiHalCallMethodForULong::  ret:status %d\n", return_status);
    printf("\n ssp_WiFiHalCallMethodForULong---> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WiFiHalCallMethodForString
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is a string value
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : enable     - the value to be get/set
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetParamStringValue(int radioIndex, char* output, char* method)
{
    printf("\n ssp_WIFIHALGetOrSetParamStringValue----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    if(output)
        printf("GetorSetParam: %s\n" , output);
    else
        printf("Validation with NULL buffer\n");
    printf("MethodName: %s\n", method);
    int return_status = SSP_FAILURE;
    wifi_device_t dev;
    memset(&dev, 0, sizeof(wifi_device_t));
    char mac[64] = {'\0'};
    char *token = NULL;
    int count = 0;

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;
    char api_name[200] = "wifi_";
    strcat(api_name, method);

    if(isSockSetApi(api_name)){
        printf("is sock api\n");
        strncpy(apiInfo.api_name, api_name, 1024);
        strncpy(apiInfo.api_data, output, 1024);
        apiInfo.radioIndex = radioIndex;
        return_status = wifi_api_send_msg(&apiInfo);
        printf("\n ssp_WIFIHALGetOrSetParamStringValue----> Exit, ret:status %d \n", return_status);
        return return_status;
    }
    #endif

    if(!strcmp(method, "getRadioChannelsInUse"))
        return_status = wifi_getRadioChannelsInUse(radioIndex, output);
    else if(!strcmp(method, "getRadioPossibleChannels"))
        return_status = wifi_getRadioPossibleChannels(radioIndex, output);
    else if(!strcmp(method, "getChannelBandwidth"))
        return_status = wifi_getRadioOperatingChannelBandwidth(radioIndex, output);
    else if(!strcmp(method, "setRadioOperatingChannelBandwidth"))
        return_status = wifi_setRadioOperatingChannelBandwidth(radioIndex, output);
    else if(!strcmp(method, "getRadioGuardInterval"))
        return_status = wifi_getRadioGuardInterval(radioIndex, output);
    else if(!strcmp(method, "setRadioGuardInterval"))
        return_status = wifi_setRadioGuardInterval(radioIndex, output);
    else if(!strcmp(method, "getOperationalDataTransmitRates"))
        return_status = wifi_getRadioOperationalDataTransmitRates(radioIndex, output);
    else if(!strcmp(method, "setOperationalDataTransmitRates"))
        return_status = wifi_setRadioOperationalDataTransmitRates(radioIndex, output);
    else if(!strcmp(method, "getSupportedDataTransmitRates"))
        return_status = wifi_getRadioSupportedDataTransmitRates(radioIndex, output);
    else if(!strcmp(method, "getRadioSupportedFrequencyBands"))
        return_status = wifi_getRadioSupportedFrequencyBands(radioIndex, output);
    else if(!strcmp(method, "getRadioOperatingFrequencyBand"))
        return_status = wifi_getRadioOperatingFrequencyBand(radioIndex, output);
    else if(!strcmp(method, "getRadioSupportedStandards"))
        return_status = wifi_getRadioSupportedStandards(radioIndex, output);
    else if(!strcmp(method, "getRadioIfName"))
        return_status = wifi_getRadioIfName(radioIndex, output);
    else if(!strcmp(method, "getSSIDStatus"))
        return_status = wifi_getSSIDStatus(radioIndex, output);
    else if(!strcmp(method, "getApBasicAuthenticationMode"))
        return_status = wifi_getApBasicAuthenticationMode(radioIndex,output);
    else if(!strcmp(method, "setApBasicAuthenticationMode"))
        return_status = wifi_setApBasicAuthenticationMode(radioIndex,output);
    else if(!strcmp(method, "getApBeaconType"))
        return_status = wifi_getApBeaconType(radioIndex,output);
    else if(!strcmp(method, "setApBeaconType"))
        return_status = wifi_setApBeaconType(radioIndex,output);
    else if(!strcmp(method, "getApSecurityModeEnabled"))
        return_status = wifi_getApSecurityModeEnabled(radioIndex,output);
    else if(!strcmp(method, "setApSecurityModeEnabled"))
        return_status = wifi_setApSecurityModeEnabled(radioIndex,output);
    else if(!strcmp(method, "getApWpaEncryptionMode"))
        return_status = wifi_getApWpaEncryptionMode(radioIndex,output);
    else if(!strcmp(method, "setApWpaEncryptionMode"))
        return_status = wifi_setApWpaEncryptionMode(radioIndex,output);
    else if(!strcmp(method, "getRadioExtChannel"))
        return_status = wifi_getRadioExtChannel(radioIndex,output);
    else if(!strcmp(method, "setRadioExtChannel"))
        return_status = wifi_setRadioExtChannel(radioIndex,output);
    else if(!strcmp(method, "getRadioBasicDataTransmitRates"))
        return_status = wifi_getRadioBasicDataTransmitRates(radioIndex,output);
    else if(!strcmp(method, "setRadioBasicDataTransmitRates"))
        return_status = wifi_setRadioBasicDataTransmitRates(radioIndex,output);
    else if(!strcmp(method, "getSSIDName"))
        return_status = wifi_getSSIDName(radioIndex,output);
    else if(!strcmp(method, "setSSIDName"))
        return_status = wifi_setSSIDName(radioIndex,output);
    else if(!strcmp(method, "getRadioDCSChannelPool"))
        return_status = wifi_getRadioDCSChannelPool(radioIndex,output);
    else if(!strcmp(method, "setRadioDCSChannelPool"))
        return_status = wifi_setRadioDCSChannelPool(radioIndex,output);
    else if(!strcmp(method, "getApStatus"))
        return_status = wifi_getApStatus(radioIndex,output);
    else if(!strcmp(method, "getApSecurityModesSupported"))
        return_status = wifi_getApSecurityModesSupported(radioIndex,output);
    else if(!strcmp(method, "getApSecurityPreSharedKey"))
        return_status = wifi_getApSecurityPreSharedKey(radioIndex,output);
    else if(!strcmp(method, "setApSecurityPreSharedKey"))
        return_status = wifi_setApSecurityPreSharedKey(radioIndex,output);
    else if(!strcmp(method, "getApSecurityKeyPassphrase"))
        return_status = wifi_getApSecurityKeyPassphrase(radioIndex,output);
    else if(!strcmp(method, "setApSecurityKeyPassphrase"))
        return_status = wifi_setApSecurityKeyPassphrase(radioIndex,output);
    else if(!strcmp(method, "getApWpsConfigMethodsSupported"))
        return_status = wifi_getApWpsConfigMethodsSupported(radioIndex,output);
    else if(!strcmp(method, "getApWpsConfigMethodsEnabled"))
        return_status = wifi_getApWpsConfigMethodsEnabled(radioIndex,output);
    else if(!strcmp(method, "setApWpsConfigMethodsEnabled"))
        return_status = wifi_setApWpsConfigMethodsEnabled(radioIndex,output);
    else if(!strcmp(method, "getRadioTransmitPowerSupported"))
        return_status = wifi_getRadioTransmitPowerSupported(radioIndex,output);
    else if(!strcmp(method, "getRadioMaxBitRate"))
        return_status = wifi_getRadioMaxBitRate(radioIndex, output);
    else if(!strcmp(method, "getRadioCountryCode"))
        return_status = wifi_getRadioCountryCode(radioIndex,output);
    else if(!strcmp(method, "setRadioCountryCode"))
        return_status = wifi_setRadioCountryCode(radioIndex,output);
    else if(!strcmp(method, "getSSIDMACAddress"))
        return_status = wifi_getSSIDMACAddress(radioIndex,output);
    else if(!strcmp(method, "getApWpsConfigurationState"))
        return_status = wifi_getApWpsConfigurationState(radioIndex,output);
    else if(!strcmp(method, "getBaseBSSID"))
        return_status = wifi_getBaseBSSID(radioIndex, output);
    else if(!strcmp(method, "getHalVersion"))
        return_status = wifi_getHalVersion(output);
    else if(!strcmp(method, "getBandSteeringApGroup"))
        return_status = wifi_getBandSteeringApGroup(output);
    else if(!strcmp(method, "setBandSteeringApGroup"))
        return_status = wifi_setBandSteeringApGroup(output);
    else if(!strcmp(method, "pushSSID"))
        return_status = wifi_pushSSID(radioIndex, output);
    else if(!strcmp(method, "getApName"))
        return_status = wifi_getApName(radioIndex, output);
    else if(!strcmp(method, "setApWpsEnrolleePin"))
        return_status = wifi_setApWpsEnrolleePin(radioIndex, output);
    else if(!strcmp(method, "kickApAssociatedDevice"))
        return_status = wifi_kickApAssociatedDevice(radioIndex, output);
    else if(!strcmp(method, "getSSIDNameStatus"))
        return_status = wifi_getSSIDNameStatus(radioIndex, output);
    else if(!strcmp(method, "setApBeaconRate"))
        return_status = wifi_setApBeaconRate(radioIndex, output);
    else if(!strcmp(method, "getApBeaconRate"))
        return_status = wifi_getApBeaconRate(radioIndex, output);
    else if(!strcmp(method, "setApWpsButtonPush"))
        return_status = wifi_setApWpsButtonPush(radioIndex);
    else if(!strcmp(method, "getApSecurityMFPConfig"))
        return_status = wifi_getApSecurityMFPConfig(radioIndex, output);
    else if(!strcmp(method, "setApSecurityMFPConfig"))
        return_status = wifi_setApSecurityMFPConfig(radioIndex, output);
    else if(!strcmp(method, "kickAssociatedDevice"))
    {
        strncpy(mac, output, 64);
        token = mac;
        token = strtok(token, ":");
        while ((token != NULL) && (count<6))
        {
             dev.wifi_devMacAddress[count] = (int) strtol(token, NULL, 16);
             count++;
             token = strtok(NULL, ":");
        }
        return_status = wifi_kickAssociatedDevice(radioIndex, &dev);
    }
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForString: Invalid methodName\n");
    }

    if(output)
        printf("ssp_WiFiHalCallMethodForString: return value is %s\n", output);
    printf("ssp_WiFiHalCallMethodForString: ret:status %d\n", return_status);
    printf("\n ssp_WiFiHalCallMethodForString--> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WiFiHalCallMethodForInt
 * Description          : This function invokes WiFi hal's get apis, when the value to be
                          get  is an integer value
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : enable     - the value to be get/set
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetParamIntValue(int radioIndex, int* output, char* method)
{
    printf("\n ssp_WIFIHALGetOrSetParamIntValue----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    if(output)
        printf("GetorSetParam: %d\n" , *output);
    else
        printf("NULL buffer validation\n");
    printf("MethodName: %s\n", method);
    int return_status = SSP_FAILURE;

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;
    char api_name[200] = "wifi_";
    strcat(api_name, method);

    if(isSockSetApi(api_name)){
        printf("is sock api\n");
        strncpy(apiInfo.api_name, api_name, 1024);
        if(output)
            snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%d",*output);
        else
            return SSP_FAILURE;
        apiInfo.radioIndex = radioIndex;
        return_status = wifi_api_send_msg(&apiInfo);
        printf("\n ssp_WIFIHALGetOrSetParamIntValue---> Exit, ret:status %d \n", return_status);
        return return_status;
    }
    #endif

    if(!strcmp(method, "getRadioMCS"))
        return_status = wifi_getRadioMCS(radioIndex, output);
    else if(!strcmp(method, "setRadioMCS"))
        return_status = wifi_setRadioMCS(radioIndex, *output);
    else if(!strcmp(method, "getRadioStatsReceivedSignalLevel"))
        return_status = wifi_getRadioStatsReceivedSignalLevel(radioIndex, 0, output);
    else if(!strcmp(method, "getApRadioIndex"))
        return_status = wifi_getApRadioIndex(radioIndex, output);
    else if(!strcmp(method, "setApRadioIndex"))
        return_status = wifi_setApRadioIndex(radioIndex, *output);
    else if(!strcmp(method, "getSSIDRadioIndex"))
        return_status = wifi_getSSIDRadioIndex(radioIndex, output);
    else if(!strcmp(method, "setApBeaconInterval"))
        return_status = wifi_setApBeaconInterval(radioIndex, *output);
    else if(!strcmp(method, "setDTIMInterval"))
        return_status = wifi_setDTIMInterval(radioIndex, *output);
    else if(!strcmp(method, "setApAuthMode"))
        return_status = wifi_setApAuthMode(radioIndex, *output);
    else if(!strcmp(method, "getApMacAddressControlMode"))
        return_status = wifi_getApMacAddressControlMode(radioIndex, output);
    else if(!strcmp(method, "setApMacAddressControlMode"))
        return_status = wifi_setApMacAddressControlMode(radioIndex, *output);
    else if(!strcmp(method, "getBandSteeringBandUtilizationThreshold"))
        return_status = wifi_getBandSteeringBandUtilizationThreshold(radioIndex, output);
    else if(!strcmp(method, "setBandSteeringBandUtilizationThreshold"))
        return_status = wifi_setBandSteeringBandUtilizationThreshold(radioIndex, *output);
    else if(!strcmp(method, "getBandSteeringRSSIThreshold"))
        return_status = wifi_getBandSteeringRSSIThreshold(radioIndex, output);
    else if(!strcmp(method, "setBandSteeringRSSIThreshold"))
        return_status = wifi_setBandSteeringRSSIThreshold(radioIndex, *output);
    else if(!strcmp(method, "getBandSteeringPhyRateThreshold"))
        return_status = wifi_getBandSteeringPhyRateThreshold(radioIndex, output);
    else if(!strcmp(method, "setBandSteeringPhyRateThreshold"))
        return_status = wifi_setBandSteeringPhyRateThreshold(radioIndex, *output);
    else if(!strcmp(method, "getApManagementFramePowerControl"))
        return_status = wifi_getApManagementFramePowerControl(radioIndex, output);
    else if(!strcmp(method, "setApManagementFramePowerControl"))
        return_status = wifi_setApManagementFramePowerControl(radioIndex, *output);
    else if(!strcmp(method, "getApVlanID"))
        return_status = wifi_getApVlanID(radioIndex, output);
    else if(!strcmp(method, "setApSecurityReset")){
        return_status = wifi_setApSecurityReset(radioIndex);
#if defined BCM_COMMON_WIFIHAL
        return_status = wifi_factoryReset_post(radioIndex,1,1);}
#else
        }
#endif
    else if(!strcmp(method, "getBandSteeringOverloadInactiveTime"))
        return_status = wifi_getBandSteeringOverloadInactiveTime(radioIndex, output);
    else if(!strcmp(method, "setBandSteeringOverloadInactiveTime"))
        return_status = wifi_setBandSteeringOverloadInactiveTime(radioIndex, *output);
    else if(!strcmp(method, "getBandSteeringIdleInactiveTime"))
        return_status = wifi_getBandSteeringIdleInactiveTime(radioIndex, output);
    else if(!strcmp(method, "setBandSteeringIdleInactiveTime"))
        return_status = wifi_setBandSteeringIdleInactiveTime(radioIndex, *output);
    else if(!strcmp(method, "getRadioTxChainMask"))
        return_status = wifi_getRadioTxChainMask(radioIndex, output);
    else if(!strcmp(method, "setRadioTxChainMask"))
        return_status = wifi_setRadioTxChainMask(radioIndex, *output);
    else if(!strcmp(method, "getRadioRxChainMask"))
        return_status = wifi_getRadioRxChainMask(radioIndex, output);
    else if(!strcmp(method, "setRadioRxChainMask"))
        return_status = wifi_setRadioRxChainMask(radioIndex, *output);
    else if(!strcmp(method, "getRadioCarrierSenseThresholdRange"))
        return_status = wifi_getRadioCarrierSenseThresholdRange(radioIndex, output);
    else if(!strcmp(method, "getRadioCarrierSenseThresholdInUse"))
        return_status = wifi_getRadioCarrierSenseThresholdInUse(radioIndex, output);
    else if(!strcmp(method, "setRadioDcsDwelltime"))
        return_status = wifi_setRadioDcsDwelltime(radioIndex, *output);
    else if(!strcmp(method, "getRadioDcsDwelltime"))
        return_status = wifi_getRadioDcsDwelltime(radioIndex, output);
    else if(!strcmp(method, "pushRadioChannel"))
        return_status = wifi_pushRadioChannel(radioIndex, *output);
    else if(!strcmp(method, "getRadioBandUtilization"))
        return_status = wifi_getRadioBandUtilization(radioIndex, output);
    else if(!strcmp(method, "setApCsaDeauth"))
        return_status = wifi_setApCsaDeauth(radioIndex, *output);
    else if(!strcmp(method, "setBSSTransitionActivation"))
        return_status = wifi_setBSSTransitionActivation(radioIndex, *output);
    else if(!strcmp(method, "setApDTIMInterval"))
          return_status = wifi_setApDTIMInterval(radioIndex, *output);
    else if(!strcmp(method, "getDownlinkMuType"))
    {
        if(output)
            return_status = wifi_getDownlinkMuType(radioIndex, (wifi_dl_mu_type_t*)output);
        else
            return_status = wifi_getDownlinkMuType(radioIndex, NULL);
    }
    else if(!strcmp(method, "getUplinkMuType"))
    {
        if(output)
            return_status = wifi_getUplinkMuType(radioIndex, (wifi_ul_mu_type_t*)output);
        else
            return_status = wifi_getUplinkMuType(radioIndex, NULL);
    }
    else if(!strcmp(method, "getGuardInterval"))
    {
        if(output)
            return_status = wifi_getGuardInterval(radioIndex, (wifi_guard_interval_t*)output);
        else
            return_status = wifi_getGuardInterval(radioIndex, NULL);
    }
    else if(!strcmp(method, "setDownlinkMuType"))
          return_status = wifi_setDownlinkMuType(radioIndex, (wifi_dl_mu_type_t)*output);
    else if(!strcmp(method, "setUplinkMuType"))
          return_status = wifi_setUplinkMuType(radioIndex, (wifi_ul_mu_type_t)*output);
    else if(!strcmp(method, "setGuardInterval"))
          return_status = wifi_setGuardInterval(radioIndex, (wifi_guard_interval_t)*output);
    else if(!strcmp(method, "getRadioClientInactivityTimout"))
    {
        if(output)
            return_status = wifi_getRadioClientInactivityTimout(radioIndex, output);
        else
            return_status = wifi_getRadioClientInactivityTimout(radioIndex, NULL);
    }
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForInt: Invalid methodName\n");
    }

    if(output)
        printf("ssp_WiFiHalCallMethodForInt: return value is %d\n", *output);
    printf("ssp_WiFiHalCallMethodForInt: ret:status %d\n", return_status);
    printf("\n ssp_WiFiHalCallMethodForInt--> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetOrSetParamUIntValue
 * Description          : This function invokes WiFi hal's get apis, when the value to be
                          get  is an unsigned integer value
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : enable     - the value to be get/set
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetParamUIntValue(int radioIndex, unsigned int* output, char* method)
{
    printf("\n ssp_WIFIHALGetOrSetParamUIntValue----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    if(output)
        printf("GetorSetParam: %u\n" , *output);
    else
        printf("Validation with NULL buffer\n");
    printf("MethodName: %s\n", method);
    int return_status = SSP_FAILURE;

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;
    char api_name[200] = "wifi_";
    strcat(api_name, method);

    if(isSockSetApi(api_name)){
        printf("is sock api\n");
        strncpy(apiInfo.api_name, api_name, 1024);
        if(output)
            snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%u",*output);
        else
            return SSP_FAILURE;
        apiInfo.radioIndex = radioIndex;
        return_status = wifi_api_send_msg(&apiInfo);
        printf("\n ssp_WIFIHALGetOrSetParamUIntValue---> Exit, ret:status %d \n", return_status);
        return return_status;
    }
    #endif

    if(!strcmp(method, "getRadioBeaconPeriod"))
        return_status = wifi_getRadioBeaconPeriod(radioIndex, output);
    else if(!strcmp(method, "setRadioBeaconPeriod"))
        return_status = wifi_setRadioBeaconPeriod(radioIndex, *output);
    else if(!strcmp(method, "getApAclDeviceNum"))
        return_status = wifi_getApAclDeviceNum(radioIndex, output);
    else if(!strcmp(method, "getApRetryLimit"))
        return_status = wifi_getApRetryLimit(radioIndex, output);
    else if(!strcmp(method, "setApRetryLimit"))
        return_status = wifi_setApRetryLimit(radioIndex, *output);
    else if(!strcmp(method, "getApMaxAssociatedDevices"))
        return_status = wifi_getApMaxAssociatedDevices(radioIndex, output);
    else if(!strcmp(method, "setApMaxAssociatedDevices"))
        return_status = wifi_setApMaxAssociatedDevices(radioIndex, *output);
    else if(!strcmp(method, "getApAssociatedDevicesHighWatermarkThreshold"))
        return_status = wifi_getApAssociatedDevicesHighWatermarkThreshold(radioIndex, output);
    else if(!strcmp(method, "setApAssociatedDevicesHighWatermarkThreshold"))
        return_status = wifi_setApAssociatedDevicesHighWatermarkThreshold(radioIndex, *output);
    else if(!strcmp(method, "getApAssociatedDevicesHighWatermark"))
        return_status = wifi_getApAssociatedDevicesHighWatermark(radioIndex, output);
    else if(!strcmp(method, "getApAssociatedDevicesHighWatermarkThresholdReached"))
        return_status = wifi_getApAssociatedDevicesHighWatermarkThresholdReached(radioIndex, output);
    else if(!strcmp(method, "setApRtsThreshold"))
        return_status = wifi_setApRtsThreshold(radioIndex, *output);
    else if(!strcmp(method, "pushChannel"))
        return_status = wifi_pushChannel(radioIndex, *output);
    else if(!strcmp(method, "setRadioFragmentationThreshold"))
        return_status = wifi_setRadioFragmentationThreshold(radioIndex, *output);
/*    else if(!strcmp(method, "getAtmBandMode"))
    {
        if(output)
           return_status = wifi_getAtmBandMode(radioIndex, output);
        else
            return_status = wifi_getAtmBandMode(radioIndex, NULL);
    }
    else if(!strcmp(method, "getAtmBandWeights"))
    {
        if(output)
           return_status = wifi_getAtmBandWeights(radioIndex, output);
        else
            return_status = wifi_getAtmBandWeights(radioIndex, NULL);
    }
    else if(!strcmp(method, "getAtmBandDistributionType"))
    {
        if(output)
          return_status = wifi_getAtmBandDistributionType(radioIndex, output);
        else
            return_status = wifi_getAtmBandDistributionType(radioIndex, NULL);
    }
    else if(!strcmp(method, "getAtmBandDirection"))
    {
         if(output)
           return_status = wifi_getAtmBandDirection(radioIndex, output);
         else
             return_status = wifi_getAtmBandDirection(radioIndex, NULL);
    }
    else if(!strcmp(method, "getSoftBlockWaitingTime"))
    {
        if(output)
           return_status = wifi_getSoftBlockWaitingTime(radioIndex, output);
        else
            return_status = wifi_getSoftBlockWaitingTime(radioIndex, NULL);
    }*/
    else if(!strcmp(method, "getInterworkingAccessNetworkType"))
    {
        if(output)
           return_status = wifi_getInterworkingAccessNetworkType(radioIndex, output);
        else
            return_status = wifi_getInterworkingAccessNetworkType(radioIndex, NULL);
    }
    else if(!strcmp(method, "setInterworkingAccessNetworkType"))
        return_status = wifi_setInterworkingAccessNetworkType(radioIndex, *output);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForUInt: Invalid methodName\n");
    }
    if(output)
        printf("ssp_WiFiHalCallMethodForUInt: return value is %d\n", *output);
    printf("\n ssp_WiFiHalCallMethodForUInt:, ret:status %d \n", return_status);
    printf("\n ssp_WiFiHalCallMethodForUInt--> Exit\n");
    return return_status;
}

/***************************************************************************
 *Function name : initialize
 *Description   : Initialize Function will be used for registering the wrapper method
 *                        with the agent so that wrapper function will be used in the script
 *
 *****************************************************************************/
bool WIFIHAL::initialize(IN const char* szVersion)
{
    return TEST_SUCCESS;
}


/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string WIFIHAL::testmodulepre_requisites()
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL testmodulepre_requisites --->Entry\n");

    int return_status = SSP_SUCCESS;

#if defined(_COSA_BCM_MIPS_)
    DEBUG_PRINT(DEBUG_TRACE,"\nInvoking wifi_init HAL API\n");

    return_status = wifi_init();

    DEBUG_PRINT(DEBUG_TRACE,"\nreturn value from wifi_init is %d\n",return_status);
#endif

    if(SSP_SUCCESS == return_status)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepre_requisites ---> Initialize SUCCESS !!! \n");
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL testmodulepre_requisites --->Exit\n");
        return "SUCCESS";
    }
    else
    {
       DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepre_requisites --->Failed to initialize !!! \n");
       DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL testmodulepre_requisites --->Exit\n");
       return "FAILURE";
    }
}


/***************************************************************************
 *Function name : testmodulepost_requisites
 *Description    : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/
bool WIFIHAL::testmodulepost_requisites()
{
    return TEST_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetParamBoolValue
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is BOOL
 *
 * @param [in] req-    : methodName - identifier for the hal api name
 			  radioIndex - radio index value of wifi
                          enable     - the bool value to be get/set
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetParamBoolValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamBoolValue --->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex;
    unsigned char enable;
    int returnValue = SSP_SUCCESS;
    int retValue = SSP_SUCCESS;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    enable = req["param"].asInt();
    strcpy(paramType, req["paramType"].asCString());

    if(!(strncmp(methodName, "set",3)&&strncmp(methodName, "push",4)&&strncmp(methodName, "create",6)))
    {
	printf("wifi_set operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetParamBoolValue(radioIndex, &enable, methodName);
        if(SSP_SUCCESS == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap")||strstr(methodName, "BandSteering")||strstr(methodName, "BSSColor"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(SSP_SUCCESS == retValue)
                {
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    printf("applyRadioSettings operation failed\n");
                }
            }
	    else
		return;
        }
    }
    else
    {
        printf("wifi_get operation to be done\n");
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            returnValue = ssp_WIFIHALGetOrSetParamBoolValue(radioIndex, &enable, methodName);
        else
            returnValue = ssp_WIFIHALGetOrSetParamBoolValue(radioIndex, NULL, methodName);
        if(SSP_SUCCESS == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",enable);
            sprintf(details, "Enable state : %s", int(enable)? "Enabled" : "Disabled");
            response["result"]="SUCCESS";
            response["details"]=details;
	    return;
        }
     }
     sprintf(details, "%s operation failed", methodName);
     response["result"]="FAILURE";
     response["details"]=details;
     DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForBool --->Error in execution\n");
     return;
}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetParamULongValue
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is Unsigned long
 *
 * @param [in] req-    : methodName - identifier for the hal api name
			 radioIndex - radio index value of wifi
                         param     - the ulong value to be get/set
                         paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetParamULongValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamULongValue------>Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    unsigned long uLongVar = 0;
    int returnValue = SSP_SUCCESS;
    int retValue = SSP_SUCCESS;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    uLongVar = (unsigned long)req["param"].asLargestUInt();
    strcpy(paramType, req["paramType"].asCString());

    if(!strncmp(methodName, "set",3))
    {
	printf("wifi_set operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetParamULongValue(radioIndex, &uLongVar, methodName);
        if(SSP_SUCCESS == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(SSP_SUCCESS == retValue)
                {
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    printf("applyRadioSettings operation failed\n");
                }
            }
	    else
		return;
        }
    }
    else
    {
       printf("wifi_get operation to be done\n");
       //paramType is set as NULL for negative test scenarios, for NULL pointer checks
       if(strcmp(paramType, "NULL"))
           returnValue = ssp_WIFIHALGetOrSetParamULongValue(radioIndex, &uLongVar, methodName);
       else
           returnValue = ssp_WIFIHALGetOrSetParamULongValue(radioIndex, NULL, methodName);
       if(SSP_SUCCESS == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %lu\n",uLongVar);
            sprintf(details, "Value returned is :%lu", uLongVar);
            response["result"]="SUCCESS";
            response["details"]=details;
	    return;
        }
     }
     sprintf(details, "%s operation failed", methodName);
     response["result"]="FAILURE";
     response["details"]=details;
     DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForULong --->Error in execution\n");
     return;

}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetParamStringValue
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is a string
 *
 * @param [in] req-    : methodName - identifier for the hal api name
 			  radioIndex - radio index value of wifi
                          param     - the string value to be get
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetParamStringValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamStringValue  ----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    char output[1000] = {'\0'};
    int returnValue = SSP_SUCCESS;
    int retValue = SSP_SUCCESS;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    char param[200] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());
    strcpy(param, req["param"].asCString());

    if(!(strncmp(methodName, "set",3)&&strncmp(methodName, "push",4)&&strncmp(methodName, "kick",4)))
    {
	printf("wifi_set operation to be done\n");
        returnValue = ssp_WIFIHALGetOrSetParamStringValue(radioIndex, param, methodName);
        if(SSP_SUCCESS == returnValue)
        {
            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(SSP_SUCCESS == retValue)
                {
                    sprintf(details, "%s operation success", methodName);
                    response["result"]="SUCCESS";
                    response["details"]=details;
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    sprintf(details, "%s operation failed", methodName);
                    response["result"]="FAILURE";
                    response["details"]=details;
                    printf("applyRadioSettings operation Failed\n");
                    return;
                }
            }
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForString --->Error in execution\n");
            return;
        }
    }
    else
    {
        printf("wifi_get operation to be done\n");
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            returnValue = ssp_WIFIHALGetOrSetParamStringValue(radioIndex, output, methodName);
        else
            returnValue = ssp_WIFIHALGetOrSetParamStringValue(radioIndex, NULL, methodName);

        if(SSP_SUCCESS == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %s\n",output);
            sprintf(details, "Value returned is :%s", output);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForString --->Error in execution\n");
            return;
        }
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetRadioStandard
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is a string
 *
 * @param [in] req-    : methodName - identifier for the hal api name
                          radioIndex - radio index value of wifi
                          param     - the string value to be get
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
			  gOnly, nOnly, acOnly - the bool values to be set/get
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetRadioStandard(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamRadioStandard ----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    char output[1000] = {'\0'};
    int return_status = SSP_SUCCESS;
    int retValue = SSP_SUCCESS;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    char param[200] = {'\0'};
    unsigned char gOnly, nOnly, acOnly;

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());
    strcpy(param, req["param"].asCString());
    gOnly = req["gOnly"].asInt();
    nOnly = req["nOnly"].asInt();
    acOnly = req["acOnly"].asInt();

    if(!strcmp(methodName, "setRadioChannelMode"))
    {
        printf("wifi_set operation to be done\n");
        #if defined BCM_COMMON_WIFIHAL
        wifi_api_info_t apiInfo;

        if(!strcmp(methodName, "setRadioChannelMode")){
            printf("is sock api\n");
            strncpy(apiInfo.api_name, "wifi_setRadioChannelMode", 1024);
            snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%s %d %d %d", param, gOnly, nOnly, acOnly);
            apiInfo.radioIndex = radioIndex;
            return_status = wifi_api_send_msg(&apiInfo);
        }
        #else
        return_status = wifi_setRadioChannelMode(radioIndex, param, gOnly, nOnly, acOnly);
        #endif
        printf("\n WIFIHALGetOrSetRadioStandard, wifi_setRadioChannelMode() ret:status %d \n", return_status);
        if(SSP_SUCCESS == return_status)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(SSP_SUCCESS == retValue)
                {
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    printf("applyRadioSettings operation failed\n");
		    response["result"]="FAILURE";
		    response["details"] = "applySetting operation failed";
                    return;
                }
            }
            else
                return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForRadioStandard --->Error in execution\n");
            return;
        }
    }
    else if(!strcmp(methodName, "getRadioStandard"))
    {
        printf("wifi_get operation to be done\n");
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            return_status = wifi_getRadioStandard(radioIndex, output, &gOnly, &nOnly, &acOnly);
        else
            return_status = wifi_getRadioStandard(radioIndex, NULL, &gOnly, &nOnly, &acOnly);

    }
    else
    {
        return_status = SSP_FAILURE;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiHalCallMethodForRadioStandard: Invalid methodName\n");
    }

    if(SSP_SUCCESS == return_status)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n output: %s\n",output);
        printf("WiFiHalCallMethodForRadioStandard: return value is %s %d %d %d\n", output, gOnly, nOnly, acOnly);
        sprintf(details, "Value returned is :%s %d %d %d", output,gOnly,nOnly,acOnly);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "%s operation failed", methodName);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForRadioStandard --->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetParamIntValue
 * Description          : This function invokes WiFi hal's get apis, when the value to be
                          get  is an integer
 *
 * @param [in] req-    : methodName - identifier for the hal api name
 			  radioIndex - radio index value of wifi
                          param     - the int value to be get
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetParamIntValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamIntValue----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    int intParam = 0;
    int returnValue = SSP_SUCCESS;
    int retValue = SSP_SUCCESS;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    intParam = req["param"].asInt();
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());

    if(!strncmp(methodName, "set",3))
    {
	printf("wifi_set operation to be done\n");
        printf("MethodName : %s\n",methodName);
        returnValue = ssp_WIFIHALGetOrSetParamIntValue(radioIndex, &intParam, methodName);
        if(SSP_SUCCESS == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap")||strstr(methodName, "MuType"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(SSP_SUCCESS == retValue)
                {
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    printf("applyRadioSettings operation failed\n");
                }
            }
	    else
		return;
        }
    }
    else
    {
        printf("wifi_get operation to be done\n");
        printf("MethodName : %s\n",methodName);
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            //When the paramType is not equal to NULL
            returnValue = ssp_WIFIHALGetOrSetParamIntValue(radioIndex, &intParam, methodName);
        else
            //When the paramType is NULL i.e., negative scenario
            returnValue = ssp_WIFIHALGetOrSetParamIntValue(radioIndex, NULL, methodName);
        if(SSP_SUCCESS == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",intParam);
            sprintf(details, "Value returned is :%d", intParam);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
     }
     sprintf(details, "%s operation failed", methodName);
     response["result"]="FAILURE";
     response["details"]=details;
     DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForInt --->Error in execution\n");
     return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetParamUIntValue
 * Description          : This function invokes WiFi hal's get apis, when the value to be
                          get  is an unsigned integer
 *
 * @param [in] req-    : methodName - identifier for the hal api name
 			  radioIndex - radio index value of wifi
                          param     - the int value to be get
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetParamUIntValue (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetParamUIntValue----->Entry\n");

    char methodName[50] = {'\0'};
    int radioIndex = 0;
    unsigned int uintParam = 0;
    int returnValue = SSP_SUCCESS;
    int retValue = SSP_SUCCESS;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    uintParam = req["param"].asInt();
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());

    if(!strncmp(methodName, "set",3))
    {
	printf("wifi_set operation to be done\n");
        printf("MethodName : %s\n",methodName);
        returnValue = ssp_WIFIHALGetOrSetParamUIntValue(radioIndex, &uintParam, methodName);
        if(SSP_SUCCESS == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            if(strstr(methodName, "Radio")||strstr(methodName, "SSID")||strstr(methodName, "Ap"))
            {
                retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
                if(SSP_SUCCESS == retValue)
                {
                    printf("applyRadioSettings operation success\n");
                    return;
                }
                else
                {
                    printf("applyRadioSettings operation failed\n");
                }
            }
	    else
		return;
        }
    }
    else
    {
        printf("wifi_get operation to be done\n");
        printf("MethodName : %s\n",methodName);
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
            //When the paramType is not equal to NULL
            returnValue = ssp_WIFIHALGetOrSetParamUIntValue(radioIndex, &uintParam, methodName);
        else
            //When the paramType is NULL i.e., negative scenario
            returnValue = ssp_WIFIHALGetOrSetParamUIntValue(radioIndex, NULL, methodName);
        if(SSP_SUCCESS == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %u\n",uintParam);
            sprintf(details, "Value returned is :%u", uintParam);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
     }
     sprintf(details, "%s operation failed", methodName);
     response["result"]="FAILURE";
     response["details"]=details;
     DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForUInt --->Error in execution\n");
     return;
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetIndexFromName
 * Description          : This function invokes WiFi hal api wifi_getIndexFromName()

 * @param [in] req-     : param     - the ssid name to be passed
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetIndexFromName (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetIndexFromName ----->Entry\n");

    int return_status = SSP_SUCCESS;
    int output = 1;
    char ssidName[10] = {'\0'};
    char details[200] = {'\0'};

    strcpy(ssidName, req["param"].asCString());

    return_status = wifi_getIndexFromName(ssidName, &output);
    printf("return status of wifi_getIndexFromName is %d\n",return_status);

    if(SSP_SUCCESS == return_status)
    {
         DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",output);
         sprintf(details, "Value returned is :%d", output);
         response["result"]="SUCCESS";
         response["details"]=details;
         return;
    }
    else
    {
         sprintf(details, "GetIndexFromName operation failed");
         response["result"]="FAILURE";
         response["details"]=details;
         return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetIndexFromName  --->Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_ClearRadioResetCount
 * Description          : This function invokes WiFi hal api wifi_clearRadioResetCount()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_ClearRadioResetCount (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ClearRadioResetCount ----->Entry\n");

    int returnValue = SSP_SUCCESS;
    char details[200] = {'\0'};

    returnValue = wifi_clearRadioResetCount();
    if(SSP_SUCCESS == returnValue)
    {
         sprintf(details, "ClearRadioResetCount operation success");
         response["result"]="SUCCESS";
         response["details"]=details;
         return;
    }
    else
    {
         sprintf(details, "ClearRadioResetCount operation failed");
         response["result"]="FAILURE";
         response["details"]=details;
         return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ClearRadioResetCount  --->Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_Reset
 * Description          : This function invokes WiFi hal api wifi_reset()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_Reset (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Reset ----->Entry\n");

    int returnValue = SSP_SUCCESS;
    char details[200] = {'\0'};

    returnValue = wifi_reset();
    if(SSP_SUCCESS == returnValue)
    {
         sprintf(details, "wifi_reset operation success");
         response["result"]="SUCCESS";
         response["details"]=details;
         return;
    }
    else
    {
         sprintf(details, "wifi_reset operation failed");
         response["result"]="FAILURE";
         response["details"]=details;
         return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Reset --->Exit\n");
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetSecurityRadiusServer
 * Description          : This function invokes WiFi hal's get/set api's which are
                          related to SecurityRadiusServer
 *
 * @param [in] req-    :  methodName - identifier for the hal api name
                          radioIndex - radio index value of wifi
                          IPAddress - IP Address of the RADIUS server used for WLAN security
			  port - port  number of the RADIUS server used for WLAN security
			  RadiusSecret - RadiusSecret of the RADIUS server used for WLAN security
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetSecurityRadiusServer(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetSecurityRadiusServer----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    int return_status = SSP_SUCCESS;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    unsigned int port = 0;
    char IPAddress[50] = {'\0'};
    char RadiusSecret[100] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    port = req["port"].asInt();
    strcpy(IPAddress, req["IPAddress"].asCString());
    strcpy(RadiusSecret, req["RadiusSecret"].asCString());
    strcpy(paramType, req["paramType"].asCString());

    if(!strncmp(methodName, "set",3))
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Set operation requested\n");
        printf("MethodName : %s\n",methodName);
        #if defined BCM_COMMON_WIFIHAL
        wifi_api_info_t apiInfo;
        char api_name[200] = "wifi_";
        strcat(api_name, methodName);

        if(!strcmp(methodName, "setApSecurityRadiusServer") || !strcmp(methodName, "setApSecuritySecondaryRadiusServer")){
            printf("is sock api\n");
            strncpy(apiInfo.api_name, api_name, 1024);
            snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%s %d %s", IPAddress, port, RadiusSecret);
            apiInfo.radioIndex = radioIndex;
            return_status = wifi_api_send_msg(&apiInfo);
        }
        #else
	if(!strcmp(methodName, "setApSecurityRadiusServer"))
	    return_status = wifi_setApSecurityRadiusServer(radioIndex, IPAddress, port, RadiusSecret);
	else if(!strcmp(methodName, "setApSecuritySecondaryRadiusServer"))
            return_status = wifi_setApSecuritySecondaryRadiusServer(radioIndex, IPAddress, port, RadiusSecret);
        #endif
        printf("\n WIFIHALGetOrSetSecurityRadiusServer, ret:status %d \n", return_status);

        if(SSP_SUCCESS == return_status)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetSecurityRadiusServer ---->Error in execution\n");
            return;
       }
    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Get operation requested\n");
        printf("MethodName : %s\n",methodName);
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(!strcmp(methodName, "getApSecurityRadiusServer"))
	    if(strcmp(paramType, "NULL"))
                return_status = wifi_getApSecurityRadiusServer(radioIndex, IPAddress, &port, RadiusSecret);
	    else
		return_status = wifi_getApSecurityRadiusServer(radioIndex, NULL, NULL, NULL);
        else if(!strcmp(methodName, "getApSecuritySecondaryRadiusServer"))
            if(strcmp(paramType, "NULL"))
                return_status = wifi_getApSecuritySecondaryRadiusServer(radioIndex, IPAddress, &port, RadiusSecret);
	    else
		return_status = wifi_getApSecuritySecondaryRadiusServer(radioIndex, NULL, NULL, NULL);
        else
        {
            return_status = SSP_FAILURE;
            printf("\n WiFiHalCallMethodForSecurityRadiusServer: Invalid methodName\n");
        }

        if(SSP_SUCCESS == return_status)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %s\n%d\n%s\n",IPAddress,port,RadiusSecret);
            sprintf(details, "Value returned is :IPAddress=%s,Port=%u,RadiusSecret=%s",IPAddress, port, RadiusSecret);
            response["result"]="SUCCESS";
            response["details"]=details;
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %s\n%d\n%s\n",IPAddress,port,RadiusSecret);
            DEBUG_PRINT(DEBUG_TRACE,"\n%s returned failure", methodName);
            sprintf(details, "Value returned is :IPAddress=%s,Port=%u,RadiusSecret=%s",IPAddress, port, RadiusSecret);
            response["result"]="FAILURE";
            response["details"]=details;
        }
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetSecurityRadiusServer ---->Exiting\n");
        return;
     }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetApBridgeInfo
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is related to ApBridgeInfo
 *
 * @param [in] req-    : methodName - identifier for the hal api name
                          radioIndex - radio index value of wifi
                          bridgeName,IP,subnet - the string value to be get/set
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetApBridgeInfo(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetApBridgeInfo  ----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    char output[1000] = {'\0'};
    int returnValue = SSP_SUCCESS;
    int retValue = SSP_SUCCESS;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    char bridgeName[32] = {'\0'};
    char IP[20] = {'\0'};
    char subnet[50] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());
    strcpy(bridgeName, req["bridgeName"].asCString());
    strcpy(IP, req["IP"].asCString());
    strcpy(subnet, req["subnet"].asCString());

    if(!strcmp(methodName, "setApBridgeInfo"))
    {
        printf("wifi_set operation to be done\n");
	returnValue = wifi_setApBridgeInfo(radioIndex, bridgeName, IP, subnet);
        if(SSP_SUCCESS == returnValue)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
            if(SSP_SUCCESS == retValue)
            {
                printf("applyRadioSettings operation success\n");
                return;
            }
            else
            {
                printf("applyRadioSettings operation failed\n");
		response["result"]="FAILURE";
		response["details"]="applySettings operation failed";
                return;
            }
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForApBridgeInfo --->Error in execution\n");
            return;
        }
    }
    else if(!strcmp(methodName, "getApBridgeInfo"))
    {
        printf("wifi_get operation to be done\n");
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
	    returnValue = wifi_getApBridgeInfo(radioIndex, bridgeName, IP, subnet);
        else
	    returnValue = wifi_getApBridgeInfo(radioIndex, NULL, NULL, NULL);

        if(SSP_SUCCESS == returnValue)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %s\n%s\n%s\n",bridgeName,IP,subnet);
            sprintf(details, "Value returned is :bridgeName=%s,IP=%s,subnet=%s",bridgeName,IP,subnet);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForApBridgeInfo --->Error in execution\n");
            return;
	}
    }
    else
    {
	printf("\n WiFiHalCallMethodForApBridgeInfo: Invalid methodName\n");
        response["result"]="FAILURE";
	response["details"]="Invalid methodName";
	return;
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetRadioDCSScanTime
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is related to RadioDCSScanTime
 *
 * @param [in] req-    : methodName - identifier for the hal api name
                         radioIndex - radio index value of wifi
                         output_interval_seconds,output_dwell_milliseconds - the integer value to be get/set
                         paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetRadioDCSScanTime(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetRadioDCSScanTime----->Entry\n");
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    char output[1000] = {'\0'};
    int return_status = SSP_SUCCESS;
    int retValue = SSP_SUCCESS;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    int output_interval_seconds = 0;
    int output_dwell_milliseconds = 0;

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());
    output_interval_seconds = req["output_interval_seconds"].asInt();
    output_dwell_milliseconds = req["output_dwell_milliseconds"].asInt();

    if(!strcmp(methodName, "setRadioDCSScanTime"))
    {
        printf("wifi_set operation to be done\n");
        #if defined BCM_COMMON_WIFIHAL
        wifi_api_info_t apiInfo;

        if(!strcmp(methodName, "setRadioDCSScanTime")){
            printf("is sock api\n");
            strncpy(apiInfo.api_name, "wifi_setRadioDCSScanTime", 1024);
            snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%d %d", output_interval_seconds, output_dwell_milliseconds);
            apiInfo.radioIndex = radioIndex;
            return_status = wifi_api_send_msg(&apiInfo);
            printf("\n wifi_setRadioDCSScanTime(), ret:status %d \n", return_status);
        }
        #else
        return_status = wifi_setRadioDCSScanTime(radioIndex, output_interval_seconds, output_dwell_milliseconds);
        #endif
        if(SSP_SUCCESS == return_status)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;

            retValue = ssp_WIFIHALApplySettings(radioIndex,methodName);
            if(SSP_SUCCESS == retValue)
            {
                printf("applyRadioSettings operation success\n");
                return;
            }
            else
            {
                printf("applyRadioSettings operation failed\n");
                response["result"]="FAILURE";
                response["details"]="applySettings operation failed";
                return;
            }
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForRadioDCSScanTime --->Error in execution\n");
            return;
        }
    }
    else if(!strcmp(methodName, "getRadioDCSScanTime"))
    {
        printf("wifi_get operation to be done\n");
        //paramType is set as NULL for negative test scenarios, for NULL pointer checks
        if(strcmp(paramType, "NULL"))
	    return_status = wifi_getRadioDCSScanTime(radioIndex, &output_interval_seconds, &output_dwell_milliseconds);
        else
	    return_status = wifi_getRadioDCSScanTime(radioIndex,  NULL, NULL);

        if(SSP_SUCCESS == return_status)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n%d\n",output_interval_seconds,output_dwell_milliseconds);
            sprintf(details, "Value returned is :output_interval_seconds=%d,output_dwell_milliseconds=%d",output_interval_seconds,output_dwell_milliseconds);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            sprintf(details, "%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForRadioDCSScanTime --->Error in execution\n");
            return;
        }
    }
    else
    {
        printf("\n WiFiHalCallMethodForApBridgeInfo: Invalid methodName\n");
        response["result"]="FAILURE";
        response["details"]="Invalid methodName";
        return;
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_AddorDelApAclDevice
 * Description          : This function invokes WiFi hal's add/delete apis, when the value to be
                          added/deleted is related to ApAclDevice
 *
 * @param [in] req-    : methodName - identifier for the hal api name
                          apIndex - ap index value of wifi
                          DeviceMacAddress - the MacAddress(string)of the device to be added/deleted
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_AddorDelApAclDevice(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_AddorDelApAclDevice------>Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    char output[1000] = {'\0'};
    int return_status = SSP_SUCCESS;
    char details[200] = {'\0'};
    char DeviceMacAddress[64] = {'\0'};
    strcpy(methodName, req["methodName"].asCString());
    apIndex = req["apIndex"].asInt();
    strcpy(DeviceMacAddress, req["DeviceMacAddress"].asCString());

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;
    char api_name[200] = "wifi_";
    strcat(api_name, methodName);

    printf("is sock api\n");
    strncpy(apiInfo.api_name, api_name, 1024);
    strncpy(apiInfo.api_data, DeviceMacAddress, 1024);
    apiInfo.radioIndex = apIndex;
    return_status = wifi_api_send_msg(&apiInfo);
    printf("\n WIFIHALAddorDelApAclDevice, ret:status %d \n", return_status);
    #else
    if(!strcmp(methodName, "addApAclDevice"))
    {
        printf("wifi_add operation to be done\n");
        return_status = wifi_addApAclDevice(apIndex, DeviceMacAddress);
    }
    else if(!strcmp(methodName, "delApAclDevice"))
    {
        printf("wifi_delete operation to be done\n");
        return_status = wifi_delApAclDevice(apIndex, DeviceMacAddress);
    }
    else
    {
        return_status = SSP_FAILURE;
        printf("\n WiFiHalCallMethodForAddorDelApAclDevice: Invalid methodName\n");
    }
    #endif

    if(SSP_SUCCESS == return_status)
    {
        sprintf(details, "%s operation success", methodName);
        response["result"]="SUCCESS";
        response["details"]=details;
	DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForAddApAclDevice SUCCESS, Exit\n");
        return;
    }
    else
    {
        sprintf(details, "%s operation failed", methodName);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForAddApAclDevice --->Error in execution\n");
        return;
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_IfConfigUporDown
 * Description          : This function invokes WiFi hal api's wifi_ifConfigDown() or wifi_ifConfigUp()

 * @param [in] req-     :  apIndex - ap Index value of wifi
                           methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_IfConfigUporDown(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_IfConfigUporDown------>Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    char output[1000] = {'\0'};
    int return_status = SSP_FAILURE;
    char details[200] = {'\0'};
    strcpy(methodName, req["methodName"].asCString());
    apIndex = req["apIndex"].asInt();

    if(!strcmp(methodName, "ifConfigUp"))
    {
        printf("wifi_IfConfigUp operation to be done\n");
	return_status = wifi_ifConfigUp(apIndex);
    }
    else if(!strcmp(methodName, "ifConfigDown"))
    {
	printf("wifi_IfConfigDown operation to be done\n");
	return_status = wifi_ifConfigDown(apIndex);
    }
    else
    {
        return_status = SSP_FAILURE;
        printf("\n WiFiHalCallMethodForAddorDelApAclDevice: Invalid methodName\n");
    }

    if(SSP_SUCCESS == return_status)
    {
        sprintf(details, "%s operation success", methodName);
        response["result"]="SUCCESS";
        response["details"]=details;
	DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForIfConfigUp exiting");
        return;
    }
    else
    {
        sprintf(details, "%s operation failed", methodName);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForIfConfigUp --->Error in execution\n");
        return;
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_ParamRadioIndex
 * Description          : This function invokes WiFi hal api's which require radioIndex as input
 * @param [in] req-     :  radioIndex - radio Index value of wifi
                           methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_ParamRadioIndex(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ParamRadioIndex------>Entry\n");
    char method[50] = {'\0'};
    int radioIndex = 0;
    char output[1000] = {'\0'};
    int return_status = SSP_SUCCESS;
    char details[200] = {'\0'};
    strcpy(method, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;
    char api_name[200] = "wifi_";
    strcat(api_name, method);

    if(isSockSetApi(api_name)){
        printf("is sock api\n");
        strncpy(apiInfo.api_name, api_name, 1024);
        apiInfo.radioIndex = radioIndex;
        return_status = wifi_api_send_msg(&apiInfo);
        if(!strcmp(method,"disableApEncryption") && (return_status == SSP_SUCCESS))
        {
            return_status = wifi_disableApEncryption(radioIndex);
            if(return_status == SSP_SUCCESS)
                return_status = ssp_WIFIHALApplySettings(radioIndex, method);
        }
        printf("\n WIFIHALParamRadioIndex, ret:status %d \n", return_status);
        if(SSP_SUCCESS == return_status){

            sprintf(details, "%s operation success", method);
            response["result"]="SUCCESS";
            response["details"]=details;
        }
        else
        {
            sprintf(details, "%s operation failed", method);
            response["result"]="FAILURE";
            response["details"]=details;
        }
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForParamRadioIndex --->Exiting\n");
        return;
    }
    #endif

    if(!strcmp(method, "cancelApWPS"))
        return_status = wifi_cancelApWPS(radioIndex);
    else if(!strcmp(method, "setApSecurityReset"))
        return_status = wifi_setApSecurityReset(radioIndex);
    else if(!strcmp(method, "resetApVlanCfg"))
        return_status = wifi_resetApVlanCfg(radioIndex);
    else if(!strcmp(method,"disableApEncryption")){
        return_status = wifi_disableApEncryption(radioIndex);
        if(return_status == SSP_SUCCESS)
            return_status = ssp_WIFIHALApplySettings(radioIndex, method);
    }
    else if(!strcmp(method,"removeApSecVaribles"))
        return_status = wifi_removeApSecVaribles(radioIndex);
    else if(!strcmp(method, "initRadio"))
        return_status = wifi_initRadio(radioIndex);
    else if(!strcmp(method, "factoryResetRadio")){
        return_status = wifi_factoryResetRadio(radioIndex);
    #if defined BCM_COMMON_WIFIHAL
        return_status = wifi_factoryReset_post(radioIndex,1,1);}
    #else
    }
    #endif
    else
    {
        return_status = SSP_FAILURE;
        printf("\n WiFiHalCallMethodForParamRadioIndex: Invalid methodName\n");
    }

    if(SSP_SUCCESS == return_status)
    {
        sprintf(details, "%s operation success", method);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ParamRadioIndex --->Exit\n");
        return;
    }
    else
    {
        sprintf(details, "%s operation failed", method);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForParamRadioIndex --->Error in execution\n");
        return;
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_StartorStopHostApd
 * Description          : This function invokes WiFi hal api's wifi_startHostApd() and wifi_stopHostApd()
 * @param [in] req-     : methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_StartorStopHostApd(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_StartorStopHostApd ----->Entry\n");
    int return_status = SSP_FAILURE;
    char details[200] = {'\0'};
    char output[1000] = {'\0'};
    char methodName[50] = {'\0'};
    strcpy(methodName, req["methodName"].asCString());

    if(!strcmp(methodName, "startHostApd"))
        return_status = wifi_startHostApd();
    else if(!strcmp(methodName, "stopHostApd"))
        return_status = wifi_stopHostApd();
    else
    {
        return_status = SSP_FAILURE;
        printf("\n WiFiHalCallMethodForStartorStopHostApd: Invalid methodName\n");
    }

    if(SSP_SUCCESS == return_status)
    {
        sprintf(details, "%s operation success", methodName);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_StartorStopHostApd --->Exit\n");
        return;
    }
    else
    {
        sprintf(details, "%s operation failed", methodName);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForStartorStopHostApd --->Error in execution\n");
        return;
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_FactoryReset
 * Description          : This function invokes WiFi hal api's wifi_factoryResetRadios() and wifi_factoryReset()
 * @param [in] req-     : methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_FactoryReset(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_FactoryReset ----->Entry\n");
    int return_status = SSP_FAILURE;
    char details[200] = {'\0'};
    char output[1000] = {'\0'};
    char methodName[50] = {'\0'};
    strcpy(methodName, req["methodName"].asCString());

    if(!strcmp(methodName, "factoryReset")){
        return_status = wifi_factoryReset();
    #if defined BCM_COMMON_WIFIHAL
        return_status = wifi_factoryReset_post(-1, 1,1);}
    #else
        }
    #endif
    else if(!strcmp(methodName, "factoryResetRadios")){
        return_status = wifi_factoryResetRadios();
    #if defined BCM_COMMON_WIFIHAL
        return_status = wifi_factoryReset_post(-1, 1,1);}
    #else
        }
    #endif
    else
    {
        return_status = SSP_FAILURE;
        printf("\n WiFiHalCallMethodForFactoryReset: Invalid methodName\n");
    }

    if(SSP_SUCCESS == return_status)
    {
        sprintf(details, "%s operation success", methodName);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_FactoryReset --->Exit\n");
        return;
    }
    else
    {
        sprintf(details, "%s operation failed", methodName);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForFactoryReset --->Error in execution\n");
        return;
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetSecurityRadiusSettings
 * Description          : This function invokes WiFi hal get/set api's which are
                          related to SecurityRadiusSettings()

 * @param [in] req-     : radioIndex - radio Index value of wifi
                          methodName - identifier for the hal api name
			  RadiusServerRetries - Number of retries for Radius requests
			  RadiusServerRequestTimeout - Radius request timeout in seconds after which the request must be retransmitted for the # of
                                                       retries available
			  PMKLifetime - Default time in seconds after which a Wi-Fi client is forced to ReAuthenticate (def 8 hrs)
			  PMKCaching - Time interval in seconds after which the PMKSA (Pairwise Master Key Security Association)cache is purged (def 5min)
			  MaxAuthenticationAttempts - Indicates the # of time, a client can attempt to login with incorrect credentials.
                                                      When this limit is reached, the client is blacklisted and not allowed to attempt loging
                                                      into the network. Settings this parameter to 0 (zero) disables the blacklisting feature.
			  BlacklistTableTimeout - Time interval in seconds for which a client will continue to be blacklisted once it is marked so
			  IdentityRequestRetryInterval - Time Interval in seconds between identity requests retries. A value of 0 (zero) disables it
			  QuietPeriodAfterFailedAuthentication - The enforced quiet period (time interval) in seconds following failed authentication.
                                                                 A value of 0 (zero) disables it
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetSecurityRadiusSettings (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetSecurityRadiusSettings ----->Entry\n");

    wifi_radius_setting_t radiusSetting;
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[500] = {'\0'};

    strcpy(methodName, req["methodName"].asCString());
    radioIndex = req["radioIndex"].asInt();
    radiusSetting.RadiusServerRetries = req["RadiusServerRetries"].asInt();
    radiusSetting.RadiusServerRequestTimeout = req["RadiusServerRequestTimeout"].asInt();
    radiusSetting.PMKLifetime = req["PMKLifetime"].asInt();
    radiusSetting.PMKCaching = req["PMKCaching"].asInt();
    radiusSetting.PMKCacheInterval = req["PMKCacheInterval"].asInt();
    radiusSetting.MaxAuthenticationAttempts = req["MaxAuthenticationAttempts"].asInt();
    radiusSetting.BlacklistTableTimeout = req["BlacklistTableTimeout"].asInt();
    radiusSetting.IdentityRequestRetryInterval = req["IdentityRequestRetryInterval"].asInt();
    radiusSetting.QuietPeriodAfterFailedAuthentication = req["QuietPeriodAfterFailedAuthentication"].asInt();

    if(!strcmp(methodName, "setApSecurityRadiusSettings"))
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Set operation requested\n");
        printf("MethodName : %s\n",methodName);
        #if defined BCM_COMMON_WIFIHAL
        wifi_api_info_t apiInfo;

        if(!strcmp(methodName, "setApSecurityRadiusSettings")){
            printf("is sock api\n");
            strncpy(apiInfo.api_name, "wifi_setApSecurityRadiusSettings", 1024);
            snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%d %d %d %d %d %d %d %d %d", radiusSetting.RadiusServerRetries, radiusSetting.RadiusServerRequestTimeout, radiusSetting.PMKLifetime, radiusSetting.PMKCaching, radiusSetting.PMKCacheInterval, radiusSetting.MaxAuthenticationAttempts, radiusSetting.BlacklistTableTimeout, radiusSetting.IdentityRequestRetryInterval, radiusSetting.QuietPeriodAfterFailedAuthentication);
            apiInfo.radioIndex = radioIndex;
            return_status = wifi_api_send_msg(&apiInfo);
            printf("\n WIFIHALGetOrSetSecurityRadiusSettings, ret:status %d \n", return_status);
        }
        #else
        return_status = wifi_setApSecurityRadiusSettings(radioIndex, &radiusSetting);
        #endif

        if(SSP_SUCCESS == return_status)
        {
            sprintf(details, "%s operation success", methodName);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
    }
    else if(!strcmp(methodName, "getApSecurityRadiusSettings"))
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n Get operation requested\n");
        printf("MethodName : %s\n",methodName);
	return_status = wifi_getApSecurityRadiusSettings(radioIndex, &radiusSetting);
        if(SSP_SUCCESS == return_status)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\n output: ");
            sprintf(details, "Value returned is :RadiusServerRetries=%d,RadiusServerRequestTimeout=%d,PMKLifetime=%d,PMKCaching=%d,PMKCacheInterval=%d,MaxAuthenticationAttempts=%d,BlacklistTableTimeout=%d,IdentityRequestRetryInterval=%d,QuietPeriodAfterFailedAuthentication=%d",radiusSetting.RadiusServerRetries,radiusSetting.RadiusServerRequestTimeout,radiusSetting.PMKLifetime,radiusSetting.PMKCaching,radiusSetting.PMKCacheInterval,radiusSetting.MaxAuthenticationAttempts,radiusSetting.BlacklistTableTimeout,radiusSetting.IdentityRequestRetryInterval,radiusSetting.QuietPeriodAfterFailedAuthentication);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
    }
    else
    {
        printf("\n WIFIHAL_GetOrSetSecurityRadiusSettings: Invalid methodName\n");
        response["result"]="FAILURE";
        response["details"]="Invalid methodName";
        return;
    }
     sprintf(details, "%s operation failed", methodName);
     response["result"]="FAILURE";
     response["details"]=details;
     DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetSecurityRadiusSettings ---->Error in execution\n");
     return;
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetSSIDTrafficStats2
 * Description          : This function invokes WiFi hal api wifi_getSSIDTrafficStats2

 * @param [in] req-     : radioIndex - radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetSSIDTrafficStats2(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetSSIDTrafficStats2 ----->Entry\n");

    wifi_ssidTrafficStats2_t ssidTrafficStats2;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[1000] = {'\0'};

    radioIndex = req["radioIndex"].asInt();

    return_status = wifi_getSSIDTrafficStats2(radioIndex, &ssidTrafficStats2);
    if(SSP_SUCCESS == return_status)
    {
        sprintf(details, "Value returned is :ssid_BytesSent=%lu,ssid_BytesReceived=%lu,ssid_PacketsSent=%lu,ssid_PacketsReceived=%lu,ssid_RetransCount=%lu,ssid_FailedRetransCount=%lu,ssid_RetryCount=%lu,ssid_MultipleRetryCount=%lu,ssid_ACKFailureCount=%lu,ssid_AggregatedPacketCount=%lu,ssid_ErrorsSent=%lu,ssid_ErrorsReceived=%lu,ssid_UnicastPacketsSent=%lu,ssid_UnicastPacketsReceived=%lu,ssid_DiscardedPacketsSent=%lu,ssid_UnicastPacketsReceived=%lu,ssid_DiscardedPacketsSent%lu,ssid_DiscardedPacketsReceived=%lu,ssid_MulticastPacketsSent=%lu,ssid_MulticastPacketsReceived=%lu,ssid_BroadcastPacketsSent=%lu,ssid_BroadcastPacketsRecevied=%lu,ssid_UnknownPacketsReceived=%lu\n",ssidTrafficStats2.ssid_BytesSent,ssidTrafficStats2.ssid_BytesReceived,ssidTrafficStats2.ssid_PacketsSent,ssidTrafficStats2.ssid_PacketsReceived,ssidTrafficStats2.ssid_RetransCount,ssidTrafficStats2.ssid_FailedRetransCount,ssidTrafficStats2.ssid_RetryCount,ssidTrafficStats2.ssid_MultipleRetryCount,ssidTrafficStats2.ssid_ACKFailureCount,ssidTrafficStats2.ssid_AggregatedPacketCount,ssidTrafficStats2.ssid_ErrorsSent,ssidTrafficStats2.ssid_ErrorsReceived,ssidTrafficStats2.ssid_UnicastPacketsSent,ssidTrafficStats2.ssid_UnicastPacketsReceived,ssidTrafficStats2.ssid_DiscardedPacketsSent,ssidTrafficStats2.ssid_UnicastPacketsReceived,ssidTrafficStats2.ssid_DiscardedPacketsSent,ssidTrafficStats2.ssid_DiscardedPacketsReceived,ssidTrafficStats2.ssid_MulticastPacketsSent,ssidTrafficStats2.ssid_MulticastPacketsReceived,ssidTrafficStats2.ssid_BroadcastPacketsSent,ssidTrafficStats2.ssid_BroadcastPacketsRecevied,ssidTrafficStats2.ssid_UnknownPacketsReceived);
        response["result"]="SUCCESS";
        response["details"]=details;
	DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetSSIDTrafficStats2 ----->Exit\n");
        return;
    }
    else
    {
        sprintf(details, "wifi_getSSIDTrafficStats2 operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetSSIDTrafficStats2 ---->Error in execution\n");
        return;
    }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRadioTrafficStats2
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getRadioTrafficStats2()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioTrafficStats2 (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioTrafficStats2 ----->Entry\n");
    wifi_radioTrafficStats2_t TrafficStats2;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[1000] = {'\0'};
    radioIndex = req["radioIndex"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\n Get operation requested\n");
    return_status = wifi_getRadioTrafficStats2(radioIndex, &TrafficStats2);
    if(SSP_SUCCESS == return_status)
    {
        sprintf(details, "Value returned is :radio_BytesSent=%lu,radio_BytesReceived=%lu,radio_PacketsSent=%lu,radio_ErrorsSent=%lu,radio_PacketsReceived=%lu,radio_ErrorsReceived=%lu,radio_DiscardPacketsSent=%lu,radio_DiscardPacketsReceived=%lu,radio_PLCPErrorCount=%lu,radio_FCSErrorCount=%lu,radio_InvalidMACCount=%lu,radio_PacketsOtherReceived=%lu,radio_NoiseFloor=%lu,radio_ChannelUtilization=%lu,radio_ActivityFactor=%lu,radio_CarrierSenseThreshold_Exceeded=%lu,radio_RetransmissionMetirc=%lu,radio_MaximumNoiseFloorOnChannel=%lu,radio_MinimumNoiseFloorOnChannel=%lu,radio_MedianNoiseFloorOnChannel=%lu,radio_StatisticsStartTime=%lu",TrafficStats2.radio_BytesSent,TrafficStats2.radio_BytesReceived,TrafficStats2.radio_PacketsSent,TrafficStats2.radio_ErrorsSent,TrafficStats2.radio_PacketsReceived,TrafficStats2.radio_ErrorsReceived,TrafficStats2.radio_DiscardPacketsSent,TrafficStats2.radio_DiscardPacketsReceived,TrafficStats2.radio_PLCPErrorCount,TrafficStats2.radio_FCSErrorCount,TrafficStats2.radio_InvalidMACCount,TrafficStats2.radio_PacketsOtherReceived,TrafficStats2.radio_NoiseFloor,TrafficStats2.radio_ChannelUtilization,TrafficStats2.radio_ActivityFactor,TrafficStats2.radio_CarrierSenseThreshold_Exceeded,TrafficStats2.radio_RetransmissionMetirc,TrafficStats2.radio_MaximumNoiseFloorOnChannel,TrafficStats2.radio_MinimumNoiseFloorOnChannel,TrafficStats2.radio_MedianNoiseFloorOnChannel,TrafficStats2.radio_StatisticsStartTime);
        response["result"]="SUCCESS";
        response["details"]=details;
	DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioTrafficStats2 ----->Exit\n");
	return;
    }
    else
    {
        sprintf(details, "wifi_getRadioTrafficStats2 operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetRadioTrafficStats2  --->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedDeviceDiagnosticResult
 * Description          : This function invokes WiFi hal api wifi_getApAssociatedDeviceDiagnosticResult
 * @param [in] req-     : radioIndex - radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult ----->Entry\n");
    wifi_associated_dev_t *associated_dev = NULL, *iteration_ptr = NULL;
    unsigned int output_array_size = 0;
    int iteration = 0;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[4000] = {'\0'};
    char output[2000] = {'\0'};

    if (&req["radioIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Radio Index : %d", radioIndex);

    return_status = wifi_getApAssociatedDeviceDiagnosticResult(radioIndex, &associated_dev, &output_array_size);
    DEBUG_PRINT(DEBUG_TRACE,"\n Return status from wifi_getApAssociatedDeviceDiagnosticResult() : %d", return_status);

    if(SSP_SUCCESS == return_status)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\nOutput Array Size = %u", output_array_size);
        sprintf(output, "Output Array Size = %u", output_array_size);
        strcat(details, output);

        if(associated_dev and output_array_size > 0)
        {
            for (iteration = 0, iteration_ptr = associated_dev; iteration < output_array_size; iteration++, iteration_ptr++)
            {
                DEBUG_PRINT(DEBUG_TRACE, "\nFor STA %d : MAC=%02x:%02x:%02x:%02x:%02x:%02x, AuthState=%d, LastDataDownlinkRate=%u, LastDataUplinkRate=%u, SignalStrength=%d, Retransmissions=%u, OperatingStd= %s, OperatingChBw=%s, SNR=%d, DataFramesSentAck=%lu, cli_DataFramesSentNoAck=%lu, cli_RSSI=%d, Disassociations=%u, AuthFailures=%u", iteration + 1, iteration_ptr->cli_MACAddress[0], iteration_ptr->cli_MACAddress[1], iteration_ptr->cli_MACAddress[2], iteration_ptr->cli_MACAddress[3], iteration_ptr->cli_MACAddress[4], iteration_ptr->cli_MACAddress[5], iteration_ptr->cli_AuthenticationState, iteration_ptr->cli_LastDataDownlinkRate, iteration_ptr->cli_LastDataUplinkRate, iteration_ptr->cli_SignalStrength, iteration_ptr->cli_Retransmissions, iteration_ptr->cli_OperatingStandard, iteration_ptr->cli_OperatingChannelBandwidth, iteration_ptr->cli_SNR, iteration_ptr->cli_DataFramesSentAck, iteration_ptr->cli_DataFramesSentNoAck, iteration_ptr->cli_RSSI, iteration_ptr->cli_Disassociations, iteration_ptr->cli_AuthenticationFailures);
                sprintf(output, " For STA %d : MAC=%02x:%02x:%02x:%02x:%02x:%02x, AuthState=%d, LastDataDownlinkRate=%u, LastDataUplinkRate=%u, SignalStrength=%d, Retransmissions=%u, OperatingStd= %s, OperatingChBw=%s, SNR=%d, DataFramesSentAck=%lu, cli_DataFramesSentNoAck=%lu, cli_RSSI=%d, Disassociations=%u, AuthFailures=%u", iteration + 1, iteration_ptr->cli_MACAddress[0], iteration_ptr->cli_MACAddress[1], iteration_ptr->cli_MACAddress[2], iteration_ptr->cli_MACAddress[3], iteration_ptr->cli_MACAddress[4], iteration_ptr->cli_MACAddress[5], iteration_ptr->cli_AuthenticationState, iteration_ptr->cli_LastDataDownlinkRate, iteration_ptr->cli_LastDataUplinkRate, iteration_ptr->cli_SignalStrength, iteration_ptr->cli_Retransmissions, iteration_ptr->cli_OperatingStandard, iteration_ptr->cli_OperatingChannelBandwidth, iteration_ptr->cli_SNR, iteration_ptr->cli_DataFramesSentAck, iteration_ptr->cli_DataFramesSentNoAck, iteration_ptr->cli_RSSI, iteration_ptr->cli_Disassociations, iteration_ptr->cli_AuthenticationFailures);
                strcat(details, output);
            }

        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"\nwifi_getApAssociatedDeviceDiagnosticResult returned empty buffer");
            sprintf(output, " wifi_getApAssociatedDeviceDiagnosticResult returned empty buffer");
            strcat(details, output);
        }

        response["result"]="SUCCESS";
        response["details"]=details;
        free(associated_dev);
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceDiagnosticResult operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult ---->Error in execution\n");
    }


    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetNeighboringWiFiDiagnosticResult2
 * Description          : This function invokes WiFi hal api wifi_getNeighboringWiFiDiagnosticResult2

 * @param [in] req-     : radioIndex - radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetNeighboringWiFiDiagnosticResult2(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetNeighboringWiFiDiagnosticResult2 ----->Entry\n");

    wifi_neighbor_ap2_t *neighbor_ap2 = NULL,*pt = NULL;
    unsigned int output_array_size = 0;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    unsigned int i = 0;
    char details[1000] = {'\0'};

    radioIndex = req["radioIndex"].asInt();

    return_status = wifi_getNeighboringWiFiDiagnosticResult2(radioIndex, &neighbor_ap2, &output_array_size);
    if(SSP_SUCCESS == return_status)
    {
        if(neighbor_ap2 != NULL and output_array_size > 0)
        {
	    for(i=0, pt=neighbor_ap2; i<output_array_size; i++, pt++)
	    {
	         if((pt->ap_SSID!="") and (strcmp(pt->ap_SSID,"OutOfService")!=0))
		     break;
	    }
	    if(i==output_array_size)
                sprintf(details, "Value returned is :ap_SSID=%s,ap_BSSID=%s,ap_Mode=%s,ap_Channel=%d,ap_SignalStrength=%d,ap_SecurityModeEnabled=%s,ap_EncryptionMode=%s,ap_OperatingFrequencyBand=%s,ap_SupportedStandards=%s,ap_OperatingStandards=%s,ap_OperatingChannelBandwidth=%s,ap_BeaconPeriod=%d,ap_Noise=%d,ap_BasicDataTransferRates=%s,ap_SupportedDataTransferRates=%s,ap_DTIMPeriod=%d,ap_ChannelUtilization=%d,output_array_size=%u",neighbor_ap2->ap_SSID,neighbor_ap2->ap_BSSID,neighbor_ap2->ap_Mode,neighbor_ap2->ap_Channel,neighbor_ap2->ap_SignalStrength,neighbor_ap2->ap_SecurityModeEnabled,neighbor_ap2->ap_EncryptionMode,neighbor_ap2->ap_OperatingFrequencyBand,neighbor_ap2->ap_SupportedStandards,neighbor_ap2->ap_OperatingStandards,neighbor_ap2->ap_OperatingChannelBandwidth,neighbor_ap2->ap_BeaconPeriod,neighbor_ap2->ap_Noise,neighbor_ap2->ap_BasicDataTransferRates,neighbor_ap2->ap_SupportedDataTransferRates,neighbor_ap2->ap_DTIMPeriod,neighbor_ap2->ap_ChannelUtilization,output_array_size);
           else
	       sprintf(details, "Value returned is :ap_SSID=%s,ap_BSSID=%s,ap_Mode=%s,ap_Channel=%d,ap_SignalStrength=%d,ap_SecurityModeEnabled=%s,ap_EncryptionMode=%s,ap_OperatingFrequencyBand=%s,ap_SupportedStandards=%s,ap_OperatingStandards=%s,ap_OperatingChannelBandwidth=%s,ap_BeaconPeriod=%d,ap_Noise=%d,ap_BasicDataTransferRates=%s,ap_SupportedDataTransferRates=%s,ap_DTIMPeriod=%d,ap_ChannelUtilization=%d,output_array_size=%u",pt->ap_SSID,pt->ap_BSSID,pt->ap_Mode,pt->ap_Channel,pt->ap_SignalStrength,pt->ap_SecurityModeEnabled,pt->ap_EncryptionMode,pt->ap_OperatingFrequencyBand,pt->ap_SupportedStandards,pt->ap_OperatingStandards,pt->ap_OperatingChannelBandwidth,pt->ap_BeaconPeriod,pt->ap_Noise,pt->ap_BasicDataTransferRates,pt->ap_SupportedDataTransferRates,pt->ap_DTIMPeriod,pt->ap_ChannelUtilization,output_array_size);
           response["result"]="SUCCESS";
           response["details"]=details;
	   DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetNeighboringWiFiDiagnosticResult2 ----->Exit\n");
           return;
        }
	else
        {
            response["result"]="SUCCESS";
            response["details"]="No neighbouring Accesspoints found by wifi_getNeighboringWiFiDiagnosticResult2";
	    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetNeighboringWiFiDiagnosticResult2 ----->Exit\n");
            return;
        }
    }
    else
    {
        sprintf(details, "wifi_getNeighboringWiFiDiagnosticResult2 operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetNeighboringWiFiDiagnosticResult2 ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_Down
 * Description          : This function invokes WiFi hal api wifi_down()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_Down (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Down ----->Entry\n");

    int returnValue;
    char details[200] = {'\0'};
    int return_status = SSP_FAILURE;
    int radioIndex = 0;

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;

    printf("is sock api\n");
    strncpy(apiInfo.api_name, "wifi_down", 1024);
    return_status = wifi_api_send_msg(&apiInfo);
    #else
    return_status = wifi_down();
    #endif
    DEBUG_PRINT(DEBUG_TRACE,"\nreturn value from ssp_WIFIHALDown is %d\n",return_status);

    if(SSP_SUCCESS == return_status)
    {
            sprintf(details, "wifi_down operation success");
            response["result"]="SUCCESS";
            response["details"]=details;
            return_status = ssp_WIFIHALApplySettings(radioIndex, (char *)"wifi_down");
            if(SSP_SUCCESS == return_status)
            {
                printf("applyRadioSettings operation success\n");
		DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Down --->Exit\n");
                return;
            }
            else
            {
                printf("applyRadioSettings operation failed\n");
            }
    }
    else
    {
            sprintf(details, "wifi_down operation failed");
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Down --->Exit\n");
            return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_Init
 * Description          : This function invokes WiFi hal api wifi_init()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_Init (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Init ----->Entry\n");

    int return_status = SSP_SUCCESS;
    char details[200] = {'\0'};

    #if defined(_COSA_BCM_MIPS_)
    printf("Invoking wifi_init HAL API\n");

    return_status = wifi_init();

    printf("return value from wifi_init is %d\n",return_status);
    #endif

    if(return_status == SSP_SUCCESS)
    {
            sprintf(details, "wifi_init operation success");
            response["result"]="SUCCESS";
            response["details"]=details;
	    printf("\nwifi_init::WIFI HAL Initialization success\n");
            DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Init --->Exit\n");
            return;
    }
    else
    {
            sprintf(details, "wifi_init operation failed");
            response["result"]="FAILURE";
            response["details"]=details;
	    printf("\nwifi_init::Failed to initialize the WIFI HAL\n");
            DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_Init --->Exit\n");
            return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_CreateInitialConfigFiles
 * Description          : This function invokes WiFi hal api wifi_createInitialConfigFiles()

 * @param [in] req-     : NIL
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_CreateInitialConfigFiles (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_CreateInitialConfigFiles ----->Entry\n");

    int return_status = SSP_FAILURE;
    char details[200] = {'\0'};
    return_status = wifi_createInitialConfigFiles();
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_createInitialConfigFiles operation success");
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
         sprintf(details, "wifi_createInitialConfigFiles operation failed");
         response["result"]="FAILURE";
         response["details"]=details;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_CreateInitialConfigFiles --->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_PushRadioChannel2
 * Description          : This function invokes WiFi hal api's wifi_pushRadioChannel2()
 * @param [in] req-     : methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_PushRadioChannel2(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushRadioChannel2 ----->Entry\n");
    int return_status = SSP_FAILURE;
    char details[200] = {'\0'};
    char methodName[50] = {'\0'};
    int radioIndex = 0;
    unsigned int channel = 0;
    unsigned int channel_width_MHz = 0;
    unsigned int csa_beacon_count = 0;

    radioIndex = req["radioIndex"].asInt();
    channel = req["channel"].asInt();
    channel_width_MHz = req["channel_width_MHz"].asInt();
    csa_beacon_count = req["csa_beacon_count"].asInt();

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;

    printf("is sock api\n");
    strncpy(apiInfo.api_name, "wifi_pushRadioChannel2", 1024);
    snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%u %u %u", channel, channel_width_MHz, csa_beacon_count);
    apiInfo.radioIndex = radioIndex;
    return_status = wifi_api_send_msg(&apiInfo);
    printf("\n WIFIHALPushRadioChannel2, ret:status %d \n", return_status);
    #else
    return_status = wifi_pushRadioChannel2(radioIndex, channel, channel_width_MHz, csa_beacon_count);
    #endif

    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "%s operation success", methodName);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushRadioChannel2 --->Exit\n");
        return;
    }
    else
    {
        sprintf(details, "%s operation failed", methodName);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForPushRadioChannel2 --->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetNeighboringWiFiStatus
 * Description          : This function invokes WiFi hal api wifi_getNeighboringWiFiStatus

 * @param [in] req-     : radioIndex - radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetNeighboringWiFiStatus(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetNeighboringWiFiStatus ----->Entry\n");

    wifi_neighbor_ap2_t *neighbor_ap2 = NULL;
    unsigned int output_array_size = 0;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[1000] = {'\0'};

    radioIndex = req["radioIndex"].asInt();

    return_status = wifi_getNeighboringWiFiStatus(radioIndex, &neighbor_ap2, &output_array_size);
    if(return_status == SSP_SUCCESS)
    {
        if(neighbor_ap2 != NULL and output_array_size > 0)
        {
            sprintf(details, "Value returned is :ap_SSID=%s,ap_BSSID=%s,ap_Mode=%s,ap_Channel=%d,ap_SignalStrength=%d,ap_SecurityModeEnabled=%s,ap_EncryptionMode=%s,ap_OperatingFrequencyBand=%s,ap_SupportedStandards=%s,ap_OperatingStandards=%s,ap_OperatingChannelBandwidth=%s,ap_BeaconPeriod=%d,ap_Noise=%d,ap_BasicDataTransferRates=%s,ap_SupportedDataTransferRates=%s,ap_DTIMPeriod=%d,ap_ChannelUtilization=%d,output_array_size=%u",neighbor_ap2->ap_SSID,neighbor_ap2->ap_BSSID,neighbor_ap2->ap_Mode,neighbor_ap2->ap_Channel,neighbor_ap2->ap_SignalStrength,neighbor_ap2->ap_SecurityModeEnabled,neighbor_ap2->ap_EncryptionMode,neighbor_ap2->ap_OperatingFrequencyBand,neighbor_ap2->ap_SupportedStandards,neighbor_ap2->ap_OperatingStandards,neighbor_ap2->ap_OperatingChannelBandwidth,neighbor_ap2->ap_BeaconPeriod,neighbor_ap2->ap_Noise,neighbor_ap2->ap_BasicDataTransferRates,neighbor_ap2->ap_SupportedDataTransferRates,neighbor_ap2->ap_DTIMPeriod,neighbor_ap2->ap_ChannelUtilization,output_array_size);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
        }
        else
        {
            response["result"]="SUCCESS";
            response["details"]="No neighbouring WiFi found by wifi_getNeighboringWiFiStatus";
            return;
        }
    }
    else
    {
        sprintf(details, "wifi_getNeighboringWiFiStatus operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetNeighboringWiFiStatus ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRadioChannelStats
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getRadioChannelStats()
 * @param [in] req-     : radioIndex : radio index of the wifi
                          channel : the channel number of which stats need to be retrieved
                          inPool : whether channel is in pool or not
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioChannelStats (IN const Json::Value& req, OUT Json::Value& response)
{
    wifi_channelStats_t channelStats;
    memset(&channelStats, 0, sizeof(channelStats));
    int array_size = 1;
    int radioIndex = 0;
    int channel = 0;
    int inPool = 0;
    int return_status = SSP_FAILURE;
    char details[1000] = {'\0'};

    if (&req["radioIndex"] == NULL || &req["channel"] == NULL || &req["inPool"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\nRadio Index : %d", radioIndex);

    channel = req["channel"].asInt();
    channelStats.ch_number = channel;
    DEBUG_PRINT(DEBUG_TRACE,"\nChannel : %d", channelStats.ch_number);

    inPool = req["inPool"].asInt();
    channelStats.ch_in_pool = inPool;
    DEBUG_PRINT(DEBUG_TRACE,"\nChannel in Pool : %d", channelStats.ch_in_pool);

    return_status = wifi_getRadioChannelStats(radioIndex, &channelStats, array_size);
    DEBUG_PRINT(DEBUG_TRACE, "\n Return value from wifi_getRadioChannelStats() is : %d\n", return_status);

    if(return_status == SSP_SUCCESS)
    {

        DEBUG_PRINT(DEBUG_TRACE, "\nwifi_getRadioChannelStats returned success; Retrieving the channel stats : ch_number=%d, ch_in_pool=%d, ch_noise=%d, ch_radar_noise=%d, ch_max_80211_rssi=%d, ch_non_80211_noise=%d, ch_utilization=%d, ch_utilization_total=%llu, ch_utilization_busy=%llu, ch_utilization_busy_tx=%llu, ch_utilization_busy_rx=%llu, ch_utilization_busy_self=%llu, ch_utilization_busy_ext=%llu", channelStats.ch_number, channelStats.ch_in_pool, channelStats.ch_noise, channelStats.ch_radar_noise, channelStats.ch_max_80211_rssi, channelStats.ch_non_80211_noise, channelStats.ch_utilization, channelStats.ch_utilization_total, channelStats.ch_utilization_busy, channelStats.ch_utilization_busy_tx, channelStats.ch_utilization_busy_rx, channelStats.ch_utilization_busy_self, channelStats.ch_utilization_busy_ext);
        sprintf(details, "wifi_getRadioChannelStats returned success; Retrieving the channel stats : ch_number=%d, ch_in_pool=%d, ch_noise=%d, ch_radar_noise=%d, ch_max_80211_rssi=%d, ch_non_80211_noise=%d, ch_utilization=%d, ch_utilization_total=%llu, ch_utilization_busy=%llu, ch_utilization_busy_tx=%llu, ch_utilization_busy_rx=%llu, ch_utilization_busy_self=%llu, ch_utilization_busy_ext=%llu", channelStats.ch_number, channelStats.ch_in_pool, channelStats.ch_noise, channelStats.ch_radar_noise, channelStats.ch_max_80211_rssi, channelStats.ch_non_80211_noise, channelStats.ch_utilization, channelStats.ch_utilization_total, channelStats.ch_utilization_busy, channelStats.ch_utilization_busy_tx, channelStats.ch_utilization_busy_rx, channelStats.ch_utilization_busy_self, channelStats.ch_utilization_busy_ext);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getRadioChannelStats operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioChannelStats  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioChannelStats ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_ParamApIndex
 * Description          : This function invokes WiFi hal api's which require apIndex as input
 * @param [in] req-     : apIndex -ap Index value of wifi
                           methodName - identifier for the hal api name
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_ParamApIndex(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ParamApIndex------>Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    int return_status = SSP_FAILURE;
    char details[200] = {'\0'};
    strcpy(methodName, req["methodName"].asCString());
    apIndex = req["apIndex"].asInt();

    if(!strcmp(methodName, "deleteAp")){
        #if defined BCM_COMMON_WIFIHAL
        wifi_api_info_t apiInfo;

        printf("is sock api\n");
        strncpy(apiInfo.api_name, "wifi_deleteAp", 1024);
        apiInfo.radioIndex = apIndex;
        return_status = wifi_api_send_msg(&apiInfo);
        #else
        return_status = wifi_deleteAp(apIndex);
        #endif
        printf("\n wifi_deleteAp, ret:status %d \n", return_status);
    }
    else if(!strcmp(methodName, "factoryResetAP")){
        return_status = wifi_factoryResetAP(apIndex);
    #if defined BCM_COMMON_WIFIHAL
        return_status = wifi_factoryReset_post(apIndex,1,1);}
    #else
    }
    #endif
    else
    {
        return_status = SSP_FAILURE;
        printf("\n WiFiHalCallMethodForParamApIndex: Invalid methodName\n");
    }

    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "%s operation success", methodName);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ParamApIndex --->Exit\n");
        return;
    }
    else
    {
        sprintf(details, "%s operation failed", methodName);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ParamApIndex--->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_GetApAssociatedDevice
 * Description          : This function invokes WiFi hal api wifi_getApAssociatedDeviceDiagnosticResult
 * @param [in] req-     : radioIndex - radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDevice(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDevice ----->Entry\n");
    char associated_dev[1024]={0};
    unsigned int output_array_size=1024;
    int apIndex = 1;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    apIndex = req["apIndex"].asInt();
    return_status = wifi_getApAssociatedDevice(apIndex, associated_dev, output_array_size);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details,"List of Associated Device: Devices=%s:Value returned is : output_array_size=%d",associated_dev,strlen(associated_dev));
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDevice operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDevice ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_GetApDeviceRSSI
 * Description          : This function invokes WiFi hal api wifi_getApDeviceRSSI
 * @param [in] req-     : apIndex      Access Point index
                                                  MAC          Client MAC in upcase format
                                                  output_RSSI  RSSI is in dbm
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApDeviceRSSI(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApDeviceRSSI ----->Entry\n");
    char methodName[50] = {'\0'};
    int return_status = SSP_FAILURE;
    int apIndex = 0;
    int output_RSSI = 0;
    char MAC[64] = {'\0'};
    char details[200] = {'\0'};

    apIndex = req["apIndex"].asInt();
    strcpy(MAC, req["MAC"].asCString());
    strcpy(methodName, req["methodName"].asCString());

    return_status = wifi_getApDeviceRSSI(apIndex, MAC, &output_RSSI);
    if(return_status == SSP_SUCCESS)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",output_RSSI);
        sprintf(details, "Value returned is :%d", output_RSSI);
        response["result"]="SUCCESS";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApDeviceRSSI  --->Exit\n");
        return;
    }
    else
    {
        sprintf(details, "GetApDeviceRSSI operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        return;
    }
}

/*******************************************************************************************
  *
 * Function Name        : WIFIHAL_DelApAclDevices
 * Description          : This function invokes WiFi hal's delete api Ap Acl Devices *
 * @param [in] req-    : methodName - identifier for the hal api name
                          apIndex - ap index value of wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_DelApAclDevices(IN const Json::Value& req, OUT Json::Value& response){
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_AddorDelApAclDevice------>Entry\n");
    int apIndex = 0;
    int return_status = SSP_FAILURE;
    char details[200] = {'\0'};

    apIndex = req["apIndex"].asInt();
    printf("wifi_del operation to be done\n");

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;

    printf("is sock api\n");
    strncpy(apiInfo.api_name, "wifi_delApAclDevices", 1024);
    apiInfo.radioIndex = apIndex;
    return_status = wifi_api_send_msg(&apiInfo);
    #else
    return_status = wifi_delApAclDevices(apIndex);
    #endif

    printf("\n wifi_delApAclDevices, ret:status %d \n", return_status);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "%s operation success", __FUNCTION__);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "%s operation failed", __FUNCTION__);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForDelApAclDevices --->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAclDevices
 * Description          : This function invokes WiFi hal api wifi_getApAclDevices
 * @param [in] req-     : apIndex - ap index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAclDevices(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAclDevices ----->Entry\n");
    char mac_addr[512]={'\0'};
    //unsigned int output_array_size;
    int apIndex = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    apIndex = req["apIndex"].asInt();

    return_status = wifi_getApAclDevices(apIndex, mac_addr, sizeof(mac_addr));
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details,"List of Mac Address; %s ;Value returned is ; output_array_size=%d",mac_addr,strlen(mac_addr));
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getApAclDevices operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAclDevices ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_GetApDeviceTxRxRate
 * Description          : This function invokes WiFi hal apis
 * @param [in] req-     : apIndex      Access Point index
                                                  MAC          Client MAC in upcase format
                                                  output_TxRx in Mbps
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApDeviceTxRxRate(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApDeviceTxRxRate ----->Entry\n");
    char method[50] = {'\0'};
    int return_status = SSP_FAILURE;
    int apIndex = 0;
    int output_TxRx = 0;
    char MAC[64] = {'\0'};
    char details[200] = {'\0'};

    apIndex = req["apIndex"].asInt();
    strcpy(MAC, req["MAC"].asCString());
    strcpy(method, req["methodName"].asCString());

    if(!strcmp(method, "getApDeviceRxrate"))
        return_status = wifi_getApDeviceRxrate(apIndex, MAC, &output_TxRx);
    else if(!strcmp(method, "getApDeviceTxrate"))
        return_status = wifi_getApDeviceTxrate(apIndex, MAC, &output_TxRx);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n WIFIHALGetApDeviceTxRxRate: Invalid methodName\n");
    }

    if(return_status == SSP_SUCCESS)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",output_TxRx);
        sprintf(details, "Value returned is :%d", output_TxRx);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "GetApDeviceTxRxRate operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApDeviceTxRxRate  --->Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_CreateAp
 * Description          : This function invokes WiFi hal api wifi_createAp
 * @param [in] req-     : apIndex     Access Point index
 * @param [in] req-     :  radioIndex  Radio index
 * @param [in] req-     :  essid       SSID Name
 * @param [in] req-     :  hideSsid    True/False, to SSID advertisement enable value

 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
*********************************************************************************************/
void WIFIHAL::WIFIHAL_CreateAp(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_CreateAp ----->Entry\n");
    int apIndex = 1;
    int radioIndex = 1;
    int return_status = SSP_FAILURE;
    char details[1000] = {'\0'};
    char detailsAdd[1000] = {'\0'};
    char essid[20] = {'\0'};
    unsigned char hideSsid;

    apIndex = req["apIndex"].asInt();
    radioIndex = req["radioIndex"].asInt();
    strcpy(essid, req["essid"].asCString());
    hideSsid = req["hideSsid"].asInt();

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;

    printf("is sock api\n");
    strncpy(apiInfo.api_name, "wifi_createAp", 1024);
    snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%d %s %d", radioIndex, essid, hideSsid);
    apiInfo.radioIndex = apIndex;
    return_status = wifi_api_send_msg(&apiInfo);
    #else
    return_status = wifi_createAp(apIndex, radioIndex, essid, hideSsid);
    #endif
    printf("\n wifi_createAp, ret:status %d \n", return_status);

    if(return_status == SSP_SUCCESS)
    {
	sprintf(detailsAdd, "wifi_createAp operation SUCCESS");
	DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
	strcat(details, detailsAdd);
	return_status = ssp_WIFIHALApplySettings(radioIndex, (char *)"createAp");
	if(return_status == SSP_SUCCESS)
	{
		sprintf(detailsAdd, " applyRadioSettings operation success");
		DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
		strcat(details, detailsAdd);
		response["result"]="SUCCESS";
	}
	else
	{
		sprintf(detailsAdd, " applyRadioSettings operation failed");
		DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
		strcat(details, detailsAdd);
		response["result"]="FAILURE";
	}
	response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_createAp operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_CreateAp ---->Error in execution\n");
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_CreateAp ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedDeviceDiagnosticResult3
 * Description          : This function invokes WiFi hal api wifi_getApAssociatedDeviceDiagnosticResult3
 * @param [in] req-     : apIndex - ap index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult3(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult3 ----->Entry\n");
    wifi_associated_dev3_t *associated_dev_array = NULL;
    unsigned int output_array_size = 0;
    int apIndex = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    apIndex = req["apIndex"].asInt();

    return_status = wifi_getApAssociatedDeviceDiagnosticResult3(apIndex, &associated_dev_array, &output_array_size);
    if(return_status == SSP_SUCCESS)
    {
       if(associated_dev_array and output_array_size > 0)
       {
            sprintf(details,"Value returned is : output_array_size=%u, MAC=%02x:%02x:%02x:%02x:%02x:%02x, IP=%s, AuthState=%d, LastDataDownlinkRate=%u, LastDataUplinkRate=%u, SignalStrength=%d, Retransmissions=%u, Active=%d, OperatingStd= %s, OperatingChBw=%s, SNR=%d, interferenceSources=%s, DataFramesSentAck=%lu, cli_DataFramesSentNoAck=%lu, cli_BytesSent=%lu, cli_BytesReceived=%lu, cli_RSSI=%d, cli_MinRSSI=%d, cli_MaxRSSI=%d, Disassociations=%u, AuthFailures=%u, cli_Associations=%llu, PacketsSent=%lu, PacketsReceived=%lu, ErrorsSent=%lu, RetransCount=%lu, FailedRetransCount=%lu, RetryCount=%lu, MultipleRetryCount=%lu, MaxDownlinkRate=%u, MaxUplinkRate=%u",output_array_size,associated_dev_array->cli_MACAddress[0],associated_dev_array->cli_MACAddress[1],associated_dev_array->cli_MACAddress[2],associated_dev_array->cli_MACAddress[3],associated_dev_array->cli_MACAddress[4],associated_dev_array->cli_MACAddress[5],associated_dev_array->cli_IPAddress,associated_dev_array->cli_AuthenticationState,associated_dev_array->cli_LastDataDownlinkRate,associated_dev_array->cli_LastDataUplinkRate,associated_dev_array->cli_SignalStrength,associated_dev_array->cli_Retransmissions,associated_dev_array->cli_Active,associated_dev_array->cli_OperatingStandard,associated_dev_array->cli_OperatingChannelBandwidth,associated_dev_array->cli_SNR,associated_dev_array->cli_InterferenceSources,associated_dev_array->cli_DataFramesSentAck,associated_dev_array->cli_DataFramesSentNoAck,associated_dev_array->cli_BytesSent,associated_dev_array->cli_BytesReceived,associated_dev_array->cli_RSSI,associated_dev_array->cli_MinRSSI,associated_dev_array->cli_MaxRSSI,associated_dev_array->cli_Disassociations,associated_dev_array->cli_AuthenticationFailures,associated_dev_array->cli_Associations,associated_dev_array->cli_PacketsSent,associated_dev_array->cli_PacketsReceived,associated_dev_array->cli_ErrorsSent,associated_dev_array->cli_RetransCount,associated_dev_array->cli_FailedRetransCount,associated_dev_array->cli_RetryCount,associated_dev_array->cli_MultipleRetryCount,associated_dev_array->cli_MaxDownlinkRate,associated_dev_array->cli_MaxUplinkRate);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
       else
       {
           sprintf(details, "wifi_getApAssociatedDeviceDiagnosticResult3 returned empty buffer");
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult3 ----> returned empty buffer\n");
            return;
        }
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceDiagnosticResult3 operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult3 ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_SetApScanFilter
 * Description          : This function invokes WiFi hal's set api, when the value to be set is related to ApScanFilter
 *
 * @param [in] req-    : methodName - identifier for the hal api name
 *                       apIndex - ap index value of wifi
 *                       mode - the mode value to be set
 *                       essid - the string value to be set
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 * ******************************************************************************************/
void WIFIHAL::WIFIHAL_SetApScanFilter(IN const Json::Value& req, OUT Json::Value& response)
{
       DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApScanFilter  ----->Entry\n");
       char methodName[50] = {'\0'};
       int apIndex = 1;
       int return_status = SSP_FAILURE;
       char details[200] = {'\0'};
       int mode = 0;
       char essid[20] = {'\0'};

       strcpy(methodName, req["methodName"].asCString());
       apIndex = req["apIndex"].asInt();
       mode = req["mode"].asInt();
       strcpy(essid, req["essid"].asCString());

       printf("wifi_set operation to be done\n");
       if(!strcmp(methodName, "setApScanFilter")){
           #if defined BCM_COMMON_WIFIHAL
           wifi_api_info_t apiInfo;

           printf("is sock api\n");
           strncpy(apiInfo.api_name, "wifi_setApScanFilter", 1024);
           snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%d %s", mode, essid);
           apiInfo.radioIndex = apIndex;
           return_status = wifi_api_send_msg(&apiInfo);
           #else
           return_status = wifi_setApScanFilter(apIndex, mode, essid);
           #endif
           printf("\n wifi_setApScanFilter, ret status %d \n", return_status);
       }
       else
       {
            return_status = SSP_FAILURE;
            printf("\n WiFiHalCallMethodForApSacnFilter: Invalid methodName\n");
       }
       if(return_status == SSP_SUCCESS)
       {
               sprintf(details, "%s operation success", methodName);
               response["result"]="SUCCESS";
               response["details"]=details;
       }
       else
       {
               sprintf(details, "%s operation failed", methodName);
               response["result"]="FAILURE";
               response["details"]=details;
               DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForApScanFilter --->Error in execution\n");
               return;
       }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedDeviceStats
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getApAssociatedDeviceStats
 * @param [in] req-     : apIndex : apIndex value of wifi
                        : MAC : DeviceMacAddress - the MacAddress(string)of the device
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceStats(IN const Json::Value& req, OUT Json::Value& response)
{
       DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceStats----->Entry\n");
       wifi_associated_dev_stats_t associated_dev_stats;
       unsigned long long handle = 0;
       int apIndex = 1;
       int i =0;
       char ClientAddress[64] = {'\0'};
       int return_status = SSP_FAILURE;
       mac_address_t MAC;
       unsigned int tmp_MACConv[6];
       char details[2000] = {'\0'};

       apIndex = req["apIndex"].asInt();
       strcpy(ClientAddress, req["MAC"].asCString());
       sscanf(ClientAddress, "%02x:%02x:%02x:%02x:%02x:%02x",
                       &tmp_MACConv[0],
                       &tmp_MACConv[1],
                       &tmp_MACConv[2],
                       &tmp_MACConv[3],
                       &tmp_MACConv[4],
                       &tmp_MACConv[5]);

       for(i =0 ;i <6; i++)
               MAC[i]=(unsigned char)tmp_MACConv[i];

       return_status = wifi_getApAssociatedDeviceStats(apIndex, &MAC, &associated_dev_stats, &handle);
       if(return_status == SSP_SUCCESS)
       {
               sprintf(details, "Value returned is :cli_rx_bytes=%llu,cli_tx_bytes=%llu,cli_rx_frames=%llu,cli_tx_frames=%llu,cli_rx_retries=%llu,cli_tx_retries=%llu,cli_rx_errors=%llu,cli_tx_errors=%llu,cli_rx_rate=%lf,cli_tx_rate=%lf,cli_rssi_bcn_rssi=%s,cli_rssi_bcn_time_s=%s,cli_rssi_bcn_count=%d,cli_rssi_ack_rssi=%s,cli_rssi_ack_time_s=%s,cli_rssi_ack_count=%d\n",associated_dev_stats.cli_rx_bytes,associated_dev_stats.cli_tx_bytes,associated_dev_stats.cli_rx_frames,associated_dev_stats.cli_tx_frames,associated_dev_stats.cli_rx_retries,associated_dev_stats.cli_tx_retries,associated_dev_stats.cli_rx_errors,associated_dev_stats.cli_tx_errors,associated_dev_stats.cli_rx_rate,associated_dev_stats.cli_tx_rate,associated_dev_stats.cli_rssi_bcn.rssi,associated_dev_stats.cli_rssi_bcn.time_s,associated_dev_stats.cli_rssi_bcn.count,associated_dev_stats.cli_rssi_ack.rssi,associated_dev_stats.cli_rssi_ack.time_s,associated_dev_stats.cli_rssi_ack.count);
               response["result"]="SUCCESS";
               response["details"]=details;
               return;
       }
       else
       {
               sprintf(details, "wifi_getApAssociatedDeviceStats operation failed");
               response["result"]="FAILURE";
               response["details"]=details;
               DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceStats ---->Error in execution\n");
               return;
       }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedDeviceTxStatsResult
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getApAssociatedDeviceTxStatsResult
 * @param [in] req-     : radioIndex : radio Index value of wifi
                        : MAC : DeviceMacAddress - the MacAddress(string)of the device
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceTxStatsResult(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceTxStatsResult ----->Entry\n");
//    wifi_associated_dev_rate_info_tx_stats_t *stats_array = (wifi_associated_dev_rate_info_tx_stats_t*)malloc(sizeof(wifi_associated_dev_rate_info_tx_stats_t));
    wifi_associated_dev_rate_info_tx_stats_t *tx_stats = NULL;
    unsigned int output_array_size = 0;
    unsigned long long handle = 0;
    int radioIndex = 1;
    int return_status = SSP_FAILURE;
    mac_address_t MAC;
    char details[2000] = {'\0'};
    int i =0;
    char ClientAddress[64] = {'\0'};
    unsigned char tmp_MACConv[6] = {0};

    radioIndex = req["radioIndex"].asInt();
    strcpy(ClientAddress, req["MAC"].asCString());
    sscanf(ClientAddress, "%02x:%02x:%02x:%02x:%02x:%02x",
                           &tmp_MACConv[0],
                           &tmp_MACConv[1],
                           &tmp_MACConv[2],
                           &tmp_MACConv[3],
                           &tmp_MACConv[4],
                           &tmp_MACConv[5]);

    for(i =0 ;i <6; i++)
        MAC[i]=(unsigned char)tmp_MACConv[i];

    //returnValue = ssp_WIFIHALGetApAssociatedDeviceTxStatsResult(radioIndex, &MAC, &stats_array, &output_array_size, &handle);
    return_status = wifi_getApAssociatedDeviceTxStatsResult(radioIndex, (mac_address_t *)tmp_MACConv, &tx_stats, &output_array_size, &handle);
    if(return_status == SSP_SUCCESS)
    {
       if(tx_stats && output_array_size>0)
       {
            sprintf(details,"Value returned is : output_array_size=%d rate %1u/%02u/%1u (%08x) bytes %20llu   msdus %20llu    mpdus %20llu ppdus %20llu retries %20llu attempts %20llu",output_array_size,tx_stats[0].nss,tx_stats[0].mcs,tx_stats[0].bw,tx_stats[0].flags,tx_stats[0].bytes,tx_stats[0].msdus,tx_stats[0].mpdus,tx_stats[0].ppdus,tx_stats[0].retries,tx_stats[0].attempts);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
        else
        {
            sprintf(details,"wifi_getApAssociatedDeviceTxStatsResult returned empty buffer");
            response["result"]="FAILURE";
            response["details"]=details;
            return;
        }
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceTxStatsResult operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceTxStatsResult ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedDeviceRxStatsResult
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getApAssociatedDeviceRxStatsResult
 * @param [in] req-     : radioIndex : radio Index value of wifi
                        : MAC : DeviceMacAddress - the MacAddress(string)of the device
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceRxStatsResult(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceRxStatsResult ----->Entry\n");
    wifi_associated_dev_rate_info_rx_stats_t *stats_array = NULL;
    unsigned int output_array_size = 0;
    unsigned long long handle = 0;
    int radioIndex = 1;
    int return_status = SSP_FAILURE;
    mac_address_t MAC;
    char details[2000] = {'\0'};
    int i =0;
    char ClientAddress[64] = {'\0'};
    unsigned char tmp_MACConv[6];

    radioIndex = req["radioIndex"].asInt();
    strcpy(ClientAddress, req["MAC"].asCString());
    sscanf(ClientAddress, "%02x:%02x:%02x:%02x:%02x:%02x",
                           &tmp_MACConv[0],
                           &tmp_MACConv[1],
                           &tmp_MACConv[2],
                           &tmp_MACConv[3],
                           &tmp_MACConv[4],
                           &tmp_MACConv[5]);

    for(i =0 ;i <6; i++)
        MAC[i]=(unsigned char)tmp_MACConv[i];

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceRxStatsResult MAC %02x:%02x:%02x:%02x:%02x:%02x\n",MAC[0],MAC[1],MAC[2],MAC[3],MAC[4],MAC[5]);
    return_status = wifi_getApAssociatedDeviceRxStatsResult(radioIndex, (mac_address_t *)tmp_MACConv, &stats_array, &output_array_size, &handle);
    if(return_status == SSP_SUCCESS)
    {
       if(stats_array && output_array_size>0)
       {
            sprintf(details,"Value returned is : output_array_size=%d, rate %1u/%02u/%1u (%08llx)   bytes %20llu   msdus %20llu    mpdus %20llu ppdus %20llu retries %20llu     rssi %20u",output_array_size,stats_array->nss, stats_array->mcs, stats_array->bw, stats_array->flags,stats_array->bytes, stats_array->msdus, stats_array->mpdus, stats_array->ppdus, stats_array->retries, stats_array->rssi_combined);
            response["result"]="SUCCESS";
            response["details"]=details;
            return;
       }
       else
       {
           sprintf(details,"wifi_getApAssociatedDeviceRxStatsResult returned empty buffer");
           response["result"]="FAILURE";
           response["details"]=details;
           return;
       }
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceRxStatsResult operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceRxStatsResult ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRadioChannelStats2
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getRadioChannelStats2()

 * @param [in] req-     : radioIndex : radio index of the wifi
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioChannelStats2 (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioChannelStats ----->Entry\n");
    wifi_channelStats2_t channelStats;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[1000] = {'\0'};

    radioIndex = req["radioIndex"].asInt();

    return_status = wifi_getRadioChannelStats2(radioIndex,  &channelStats);
    printf("return value from wifi_getRadioChannelStats2 is %d\n",return_status);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "Value returned is :ch_Frequency=%d,ch_NoiseFloor=%d,ch_Non80211Noise=%d,ch_Max80211Rssi=%d,ch_ObssUtil=%d,ch_SelfBssUtil=%d",channelStats.ch_Frequency,channelStats.ch_NoiseFloor,channelStats.ch_Non80211Noise,channelStats.ch_Max80211Rssi,channelStats.ch_ObssUtil,channelStats.ch_SelfBssUtil);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getRadioChannelStats2 operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetRadioChannelStats2  --->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_StartNeighborScan
 * Description          : This function invokes WiFi hal api wifi_startNeighborScan
 * @param [in] req-     : apIndex - The index of access point array.
 * @param [out]         : scan_mode    - structure with the scan info
                        : dwell_time - Amount of time spent on each channel in the hopping sequence.
                        : chan_num - The channel number.
                        : chan_list - List of channels.
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_StartNeighborScan(IN const Json::Value& req, OUT Json::Value& response)
{
       DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_StartNeighborScan ----->Entry\n");
       wifi_neighborScanMode_t scan_mode = WIFI_RADIO_SCAN_MODE_NONE;;
       int scan_mode_tmp = 0;
       int dwell_time = 0;
       unsigned int chan_num = 0;
       unsigned int chan_list[100] = {0};
       int apIndex = 1;
       int return_status = SSP_FAILURE;
       char details[1000] = {'\0'};

       DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_StartNeighborScan: getting param\n");
       apIndex = req["apIndex"].asInt();
       dwell_time = req["dwell_time"].asInt();
//     chan_num = req["chan_num"].asInt();
//     chan_list = req["chan_list"].asInt();
       scan_mode_tmp = req["scan_mode"].asInt();

       /*Setting the scan mode */
       if(scan_mode_tmp == WIFI_RADIO_SCAN_MODE_NONE)
               scan_mode = WIFI_RADIO_SCAN_MODE_NONE;
       else if (scan_mode_tmp == WIFI_RADIO_SCAN_MODE_FULL)
               scan_mode = WIFI_RADIO_SCAN_MODE_FULL;
       else if (scan_mode_tmp == WIFI_RADIO_SCAN_MODE_ONCHAN)
               scan_mode = WIFI_RADIO_SCAN_MODE_ONCHAN;
       else if (scan_mode_tmp ==  WIFI_RADIO_SCAN_MODE_OFFCHAN)
               scan_mode = WIFI_RADIO_SCAN_MODE_OFFCHAN;
       else if (scan_mode_tmp == WIFI_RADIO_SCAN_MODE_SURVEY)
               scan_mode = WIFI_RADIO_SCAN_MODE_SURVEY;
       else
               printf("\nScan_mode is not valid\n");

       return_status = wifi_startNeighborScan(apIndex, scan_mode, dwell_time, chan_num, chan_list);
       if(return_status == SSP_SUCCESS)
       {
               sprintf(details, "wifi_startNeighborScan operation success");
               response["result"]="SUCCESS";
               response["details"]=details;
               return;
       }
       else
       {
               sprintf(details, "wifi_startNeighborScan operation failed");
               response["result"]="FAILURE";
               response["details"]=details;
               DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_StartNeighborScan ---->Error in execution\n");
               return;
       }
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetBSSColorValue
 * Description          : This function invokes WiFi hal's wifi_getBSSColor() api
 * @param [in] req-    :  radioIndex - radio index value of wifi
                          paramType  - To indicate negative test scenario. it is set as NULL for negative sceanario, otherwise empty
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetBSSColorValue(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBSSColorValue --->Entry\n");
    int radioIndex = 0;
    unsigned char color = 0;
    int return_status = SSP_FAILURE;
    char details[200] = {'\0'};
    char paramType[10] = {'\0'};
    radioIndex = req["radioIndex"].asInt();
    strcpy(paramType, req["paramType"].asCString());

    printf("wifi_getBSSColor operation to be done\n");
    //paramType is set as NULL for negative test scenarios, for NULL pointer checks
    if(strcmp(paramType, "NULL"))
        return_status = wifi_getBSSColor(radioIndex, &color);
    else
        return_status = wifi_getBSSColor(radioIndex, NULL);
    if(return_status == SSP_SUCCESS)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",color);
        sprintf(details, "Value returned is :%d", color);
        response["result"]="SUCCESS";
        response["details"]=details;
	return;
    }
    else
    {
        sprintf(details, "WIFIHAL_GetBSSColorValue operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBSSColorValue --->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_ApplyGASConfiguration
 * Description          : This function invokes WiFi hal api wifi_applyGASConfiguration()
 * @param [in] req-     : Values correspond to the dot11GASAdvertisementEntry field definitions
                          AdvertisementID
			  PauseForServerResponse
			  ResponseTimeout
			  ComeBackDelay
			  ResponseBufferingTime
			  QueryResponseLengthLimit
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_ApplyGASConfiguration(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ApplyGASConfiguration ----->Entry\n");
    wifi_GASConfiguration_t GASConfiguration = {0};
    int return_status = SSP_FAILURE;
    char details[500] = {'\0'};

    GASConfiguration.AdvertisementID = req["advertisementID"].asInt();
    GASConfiguration.PauseForServerResponse = req["pauseForServerResponse"].asInt();
    GASConfiguration.ResponseTimeout = req["responseTimeout"].asInt();
    GASConfiguration.ComeBackDelay = req["comeBackDelay"].asInt();
    GASConfiguration.ResponseBufferingTime = req["responseBufferingTime"].asInt();
    GASConfiguration.QueryResponseLengthLimit = req["queryResponseLengthLimit"].asInt();

    return_status = wifi_applyGASConfiguration(&GASConfiguration);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "WIFIHAL_ApplyGASConfiguration operation success");
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "WIFIHAL_ApplyGASConfiguration operation failure");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_ApplyGASConfiguration ---->Error in execution\n");
        return;
    }
}

/*********************************************************************************************
 * Function Name        :  WIFIHAL_GetApAssociatedDeviceTidStatsResult
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getApAssociatedDeviceTidStatsResult
 * @param [in] req-     : radioIndex : radio Index value of wifi
                        : MAC : DeviceMacAddress - the MacAddress(string)of the device
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceTidStatsResult(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceTidStatsResult ----->Entry\n");
    int i =0,n=0;
    int radioIndex = 1;
    wifi_associated_dev_tid_stats_t tid_stats;
    wifi_associated_dev_tid_entry_t *s = NULL;
    char ClientAddress[64] = {'\0'};
    unsigned char tmp_MACConv[6];
    unsigned long long handle = 0;
    unsigned char ac =0 ,tid =0;
    unsigned long long ewma_time_ms = 0,sum_time_ms = 0,num_msdus = 0 ;
    int return_status = SSP_FAILURE;
    char details[1000] = {'\0'};

    mac_address_t MAC;
    radioIndex = req["radioIndex"].asInt();
    strcpy(ClientAddress, req["MAC"].asCString());
    sscanf(ClientAddress, "%02x:%02x:%02x:%02x:%02x:%02x",
                           &tmp_MACConv[0],
                           &tmp_MACConv[1],
                           &tmp_MACConv[2],
                           &tmp_MACConv[3],
                           &tmp_MACConv[4],
                           &tmp_MACConv[5]);
    for(i =0 ;i <6; i++)
        MAC[i]=(unsigned char)tmp_MACConv[i];

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceTidStatsResult MAC %02x:%02x:%02x:%02x:%02x:%02x\n",MAC[0],MAC[1],MAC[2],MAC[3],MAC[4],MAC[5]);
    return_status = wifi_getApAssociatedDeviceTidStatsResult(radioIndex, (mac_address_t *)tmp_MACConv, & tid_stats, &handle);
    if(return_status == SSP_SUCCESS)
    {
          n = (sizeof(tid_stats.tid_array)/sizeof(tid_stats.tid_array[0]));
          printf ("Size of array is %d ",n);
          if ( n > 0)
          {
              for (i=0; i< n; i++)
              {
                  s = &tid_stats.tid_array[i];
                  printf("ac : %s,tid:%s,ewma_time_ms:%llu,sum_time_ms:%llu,num_msdus:%llu",s->ac,s->tid,s->ewma_time_ms,s->sum_time_ms,s->num_msdus);
                  ac = s->ac;
                  tid = s->tid;
                  ewma_time_ms = s->ewma_time_ms;
                  sum_time_ms = s->sum_time_ms;
                  num_msdus = s->num_msdus;
              }
              sprintf(details," Value returned is : ac : %s,tid:%s,ewma_time_ms:%llu,sum_time_ms:%llu,num_msdus:%llu",ac,tid,ewma_time_ms,sum_time_ms,num_msdus);
              response["result"]="SUCCESS";
              response["details"]=details;

          }
          else
          {
             sprintf(details,"wifi_getApAssociatedDeviceTidStatsResult returned empty buffer");
             response["result"]="FAILURE";
             response["details"]=details;

          }
          return;

    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceTidStatsResult operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceTidStatsResult  ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetBandSteeringLog
 * Description          : This function invokes WiFi hal get api which are
                          related to wifi_getBandSteeringLog
 * @param [in] req-     : record_index: index value of record
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation

 * @@param[out] pSteeringTime      Returns the UTC time in seconds
 * @param[out] pSteeringReason    Returns the predefined steering trigger reason
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetBandSteeringLog(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBandSteeringLog ----->Entry\n");
    char pClientMAC[64] = {'\0'};
    int  pSourceSSIDIndex = 0;
    int  pDestSSIDIndex = 0;
    int  pSteeringReason = 0 ;
    int  record_index = 0;
    char details[1000] = {'\0'};
    int return_status = SSP_FAILURE;
    unsigned long pSteeringTime = 0;
    record_index = req["record_index"].asInt();

    return_status = wifi_getBandSteeringLog(record_index, &pSteeringTime, pClientMAC, &pSourceSSIDIndex, &pDestSSIDIndex, &pSteeringReason);
    if(return_status == SSP_SUCCESS)
    {
      sprintf(details,"Value returned is : pSteeringTime: %lu ,pSteeringReason : %d, pClientMAC :%s,pSourceSSIDIndex :%s ,pDestSSIDIndex :%s",pSteeringTime,pSteeringReason,pClientMAC,pSourceSSIDIndex,pDestSSIDIndex);
      response["result"]="SUCCESS";
      response["details"]=details;
      return;
    }
    else
    {
        sprintf(details, "wifi_getBandSteeringLog operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBandSteeringLog---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name                    : WIFIHAL_GetApAssociatedDeviceDiagnosticResult2
 * Description                      : This function invokes WiFi hal api wifi_getApAssociatedDeviceDiagnosticResult2
 * @param[in] apIndex               :Access Point index
 * @param [out] response            : filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult2(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult2 ----->Entry\n");
    int apIndex = 1;
    wifi_associated_dev2_t *associated_dev2 = NULL;
    unsigned int dev_cnt = 0;
    char details[2000] = {'\0'};
    int return_status = SSP_FAILURE;
    apIndex  = req["apIndex"].asInt();

    return_status = wifi_getApAssociatedDeviceDiagnosticResult2(apIndex, &associated_dev2, &dev_cnt);
    if(return_status == SSP_SUCCESS)
    {
        if(associated_dev2 && dev_cnt > 0)
        {
             sprintf(details, "Value returned is : dev count:%u,cli_IPAddress :%s",dev_cnt,associated_dev2->cli_IPAddress);
             response["result"]="SUCCESS";
             response["details"]=details;
        }
        else
        {
           sprintf(details,"wifi_getApAssociatedDeviceDiagnosticResult2 returned empty buffer");
           response["result"]="FAILURE";
           response["details"]=details;

        }

        if(associated_dev2)
           free(associated_dev2);

        return;
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedDeviceDiagnosticResult2 failed");
        response["result"]="FAILURE";
        response["details"]=details;
        free(associated_dev2);
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedDeviceDiagnosticResult2 ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 *
 * Function Name                    : WIFIHAL_GetRadioMode
 * Description                      : This function invokes WiFi HAL API wifi_getRadioMode()
 * @param[in] radioIndex            : WiFi Radio index
 * @param [out] response            : filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioMode(IN const Json::Value& req, OUT Json::Value& response)
{

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioMode ----->Entry\n");
    int return_status = SSP_FAILURE;
    int radioIndex = 1;
    char details[1000] = {'\0'};
    radioIndex  = req["radioIndex"].asInt();
    unsigned int puremode = 0;
    char opStandard[32] = {'\0'};

    return_status = wifi_getRadioMode(radioIndex, opStandard, &puremode);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "Value returned is : puremode:%d, opStandard:%s",puremode,opStandard);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getRadioMode failed");
        response["result"]="FAILURE";
        response["details"]=details;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioMode ----->Exit\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name                    : WIFIHAL_SetRadioMode
 * Description                      : This function invokes WiFi HAL API wifi_setRadioMode()
 * @param[in] radioIndex            : WiFi Radio index
              chnmode               : Channel Mode
              pure mode             : Operation standard values
 * @param [out] response            : filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SetRadioMode(IN const Json::Value& req, OUT Json::Value& response)
{

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetRadioMode ----->Entry\n");
    int return_status = SSP_FAILURE;
    int radioIndex = 1;
    unsigned int puremode = 1;
    char chnMode[32] = {'\0'};

    radioIndex  = req["radioIndex"].asInt();
    strcpy(chnMode,req["chnmode"].asCString());
    puremode = req["puremode"].asInt();

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;

    printf("is sock api\n");
    strncpy(apiInfo.api_name, "wifi_setRadioMode", 1024);
    snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%s %u", chnMode, puremode);
    apiInfo.radioIndex = radioIndex;
    return_status = wifi_api_send_msg(&apiInfo);
    #else
    return_status = wifi_setRadioMode(radioIndex, chnMode, puremode);
    #endif
    printf("\n wifi_setRadioMode, ret:status %d \n", return_status);

    if(return_status == SSP_SUCCESS)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n wifi_setRadioMode operation success\n");
        return_status = ssp_WIFIHALApplySettings(radioIndex, (char *)"setRadioMode");
        if(return_status == SSP_SUCCESS)
        {
            DEBUG_PRINT(DEBUG_TRACE,"\napplyRadioSettings operation success\n");
            response["result"]="SUCCESS";
            response["details"]="wifi_setRadioMode operation success";
        }
        else
        {
            DEBUG_PRINT(DEBUG_TRACE,"\napplyRadioSettings operation failed\n");
            response["result"]="FAILURE";
            response["details"]="wifi_applyRadioSettings failed";
        }

    }
    else
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n wifi_setRadioMode operation success\n");
        response["result"]="FAILURE";
        response["details"]="wifi_setRadioMode operation Failed";
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetRadioMode ----->Exit\n");
    return;
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApIndexFromName
 * Description          : This function invokes WiFi hal api wifi_getApIndexFromName()
 * @param [in] req-     : param     - the ssid name to be passed
 * @param [out] response - Access Point index, to be returned
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApIndexFromName (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApIndexFromName ----->Entry\n");
    int return_status = SSP_FAILURE;
    int output = 1;
    char ssidName[10] = {'\0'};
    char details[200] = {'\0'};

    strcpy(ssidName, req["param"].asCString());

    return_status = wifi_getApIndexFromName(ssidName, &output);
    printf("return value from wifi_getApIndexFromName is %d\n",return_status);
    if(return_status == SSP_SUCCESS)
    {
         DEBUG_PRINT(DEBUG_TRACE,"\n output: %d\n",output);
         sprintf(details, "Value returned is :%d", output);
         response["result"]="SUCCESS";
         response["details"]=details;
    }
    else
    {
         sprintf(details, "GetApIndexFromName operation failed");
         response["result"]="FAILURE";
         response["details"]=details;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApIndexFromName  --->Exit\n");
    return;
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_GetAssociatedDeviceDetail
 * Description          : This function invokes WiFi hal api wifi_getAssociatedDeviceDetail
 * @param [in] req-     : apIndex - access point index
                          devIndex - Index of associated device
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetAssociatedDeviceDetail(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAssociatedDeviceDetail ----->Entry\n");
    int apIndex = 0;
    int devIndex = 0;
    wifi_device_t dev;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};

    apIndex = req["apIndex"].asInt();
    devIndex = req["devIndex"].asInt();

    return_status = wifi_getAssociatedDeviceDetail(apIndex, devIndex, &dev);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details,"Associated Device MAC Address : %02x:%02x:%02x:%02x:%02x:%02x Auth State : %d Rx Rate : %d Tx Rate : %d", dev.wifi_devMacAddress[0], dev.wifi_devMacAddress[1],
                        dev.wifi_devMacAddress[2], dev.wifi_devMacAddress[3], dev.wifi_devMacAddress[4], dev.wifi_devMacAddress[5],
                        dev.wifi_devAssociatedDeviceAuthentiationState, dev.wifi_devTxRate, dev.wifi_devRxRate);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getAssociatedDeviceDetail operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAssociatedDeviceDetail ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_GetBasicTrafficStats
 * Description          : This function invokes WiFi hal api wifi_getBasicTrafficStats
 * @param [in] req-     : apIndex - access point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetBasicTrafficStats(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBasicTrafficStats ----->Entry\n");
    int apIndex = 0;
    wifi_basicTrafficStats_t stats={0};
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};

    apIndex = req["apIndex"].asInt();

    return_status = wifi_getBasicTrafficStats(apIndex, &stats);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details,"BasicTrafficStats Details- wifi_BytesSent %lu, wifi_BytesReceived %lu, wifi_PacketsSent %lu, wifi_PacketsReceived %lu, wifi_Associations %lu", stats.wifi_BytesSent, stats.wifi_BytesReceived, stats.wifi_PacketsSent, stats.wifi_PacketsReceived, stats.wifi_Associations);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getBasicTrafficStats operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBasicTrafficStats ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_GetWifiTrafficStats
 * Description          : This function invokes WiFi hal api wifi_getWifiTrafficStats
 * @param [in] req-     : apIndex - access point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetWifiTrafficStats(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetWifiTrafficStats ----->Entry\n");
    int apIndex = 0;
    wifi_trafficStats_t stats={0};
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};

    apIndex = req["apIndex"].asInt();

    return_status = wifi_getWifiTrafficStats(apIndex, &stats);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details,"WifiTrafficStats Details- wifi_ErrorsSent %lu, wifi_ErrorsReceived %lu, wifi_UnicastPacketsSent %lu, wifi_UnicastPacketsReceived %lu, wifi_DiscardedPacketsSent %lu, wifi_DiscardedPacketsReceived %lu, wifi_MulticastPacketsSent %lu, wifi_MulticastPacketsReceived %lu", stats.wifi_ErrorsSent, stats.wifi_ErrorsReceived, stats.wifi_UnicastPacketsSent, stats.wifi_UnicastPacketsReceived, stats.wifi_DiscardedPacketsSent, stats.wifi_DiscardedPacketsReceived, stats.wifi_MulticastPacketsSent, stats.wifi_MulticastPacketsReceived);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getWifiTrafficStats operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetWifiTrafficStats ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_SteeringClientDisconnect
 * Description          : This function invokes WiFi hal api wifi_steering_clientDisconnect
 * @param [in] req-     : steeringgroupIndex - Wifi Steering Group index
			  apIndex - access point index
			  clientMAC - The Client's MAC address
			  disconnectType - Disconnect Type
			  reason - Reason code to provide in deauth/disassoc frame
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SteeringClientDisconnect(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientDisconnect ----->Entry\n");
    int apIndex = 0;
    unsigned int steeringgroupIndex = 0;
    char mac[20] = {'\0'};
    mac_address_t client_mac;
    unsigned int macInt[6];
    wifi_disconnectType_t type;
    unsigned int reason = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    int k = 0;

    apIndex = req["apIndex"].asInt();
    steeringgroupIndex = req["steeringgroupIndex"].asInt();
    type = (wifi_disconnectType_t)req["disconnectType"].asInt();
    reason = (unsigned int)req["reason"].asInt();
    strcpy(mac, req["clientMAC"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &macInt[0], &macInt[1], &macInt[2], &macInt[3], &macInt[4], &macInt[5]);
    for (k = 0; k < 6; k++) {
         client_mac[k] = (unsigned char)macInt[k];
    }

    return_status = wifi_steering_clientDisconnect(steeringgroupIndex, apIndex, client_mac, type, reason);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_steering_clientDisconnect operation is success");
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_steering_clientDisconnect operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientDisconnect ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_SteeringClientSet
 * Description          : This function invokes WiFi hal api wifi_steering_clientSet
 * @param [in] req-     : steeringgroupIndex - Wifi Steering Group index
                          apIndex - access point index
                          clientMAC - The Client's MAC address
                          rssiProbeHWM - Probe response RSSI high water mark
                          rssiProbeLWM - Probe response RSSI low water mark
                          rssiAuthHWM - Auth response RSSI high water mark
                          rssiAuthLWM - Auth response RSSI low water mark
                          rssiInactXing - Inactive RSSI crossing threshold
                          rssiHighXing - High RSSI crossing threshold
                          rssiLowXing - Low RSSI crossing threshold
                          authRejectReason - Inactive RSSI crossing threshold
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SteeringClientSet(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientSet ----->Entry\n");
    int apIndex = 0;
    unsigned int steeringgroupIndex = 0;
    char mac[20] = {'\0'};
    mac_address_t client_mac;
    unsigned int macInt[6];
    wifi_steering_clientConfig_t cli_cfg = {0};
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    int k = 0;

    apIndex = req["apIndex"].asInt();
    steeringgroupIndex = req["steeringgroupIndex"].asInt();
    cli_cfg.rssiProbeHWM = req["rssiProbeHWM"].asInt();
    cli_cfg.rssiProbeLWM = req["rssiProbeLWM"].asInt();
    cli_cfg.rssiAuthHWM = req["rssiAuthHWM"].asInt();
    cli_cfg.rssiAuthLWM = req["rssiAuthLWM"].asInt();
    cli_cfg.rssiInactXing = req["rssiInactXing"].asInt();
    cli_cfg.rssiHighXing = req["rssiHighXing"].asInt();
    cli_cfg.rssiLowXing = req["rssiLowXing"].asInt();
    cli_cfg.authRejectReason = req["authRejectReason"].asInt();
    strcpy(mac, req["clientMAC"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &macInt[0], &macInt[1], &macInt[2], &macInt[3], &macInt[4], &macInt[5]);
    for (k = 0; k < 6; k++) {
         client_mac[k] = (unsigned char)macInt[k];
    }

    return_status = wifi_steering_clientSet(steeringgroupIndex, apIndex, client_mac, &cli_cfg);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_steering_clientSet operation is success");
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_steering_clientSet operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientSet ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_SteeringClientRemove
 * Description          : This function invokes WiFi hal api wifi_steering_clientRemove
 * @param [in] req-     : steeringgroupIndex - Wifi Steering Group index
                          apIndex - access point index
                          clientMAC - The Client's MAC address
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SteeringClientRemove(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientRemove ----->Entry\n");
    int apIndex = 0;
    unsigned int steeringgroupIndex = 0;
    char mac[20] = {'\0'};
    mac_address_t client_mac;
    unsigned int macInt[6];
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    int k = 0;

    apIndex = req["apIndex"].asInt();
    steeringgroupIndex = req["steeringgroupIndex"].asInt();
    strcpy(mac, req["clientMAC"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &macInt[0], &macInt[1], &macInt[2], &macInt[3], &macInt[4], &macInt[5]);
    for (k = 0; k < 6; k++) {
         client_mac[k] = (unsigned char)macInt[k];
    }

    return_status = wifi_steering_clientRemove(steeringgroupIndex, apIndex, client_mac);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_steering_clientRemove operation is success");
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_steering_clientRemove operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SteeringClientRemove ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_GetBTMClientCapabilityList
 * Description          : This function invokes WiFi hal api wifi_getBTMClientCapabilityList
 * @param [in] req-     : apIndex - access point index
                          count - no: of MAC entries being passed
                          clientMAC - The Client's MAC address
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetBTMClientCapabilityList(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBTMClientCapabilityList ----->Entry\n");
    int apIndex = 0;
    int count = 0;
    char mac[20] = {'\0'};
    mac_address_t client_mac;
    wifi_BTMCapabilities_t btm_caps;
    unsigned int macInt[6];
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    int k = 0;

    apIndex = req["apIndex"].asInt();
    btm_caps.entries = req["count"].asInt();
    strcpy(mac, req["clientMAC"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &macInt[0], &macInt[1], &macInt[2], &macInt[3], &macInt[4], &macInt[5]);
    for (k = 0; k < 6; k++) {
         client_mac[k] = (unsigned char)macInt[k];
         btm_caps.peer[0][k] = client_mac[k];
    }

    return_status = wifi_getBTMClientCapabilityList(apIndex, &btm_caps);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_getBTMClientCapabilityList output is: Entries %d, MAC %x:%x:%x:%x:%x:%x, Capability %d", btm_caps.entries, btm_caps.peer[0][0],  btm_caps.peer[0][1], btm_caps.peer[0][2], btm_caps.peer[0][3], btm_caps.peer[0][4], btm_caps.peer[0][5], btm_caps.capability[0]);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getBTMClientCapabilityList operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetBTMClientCapabilityList ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_GetApRoamingConsortiumElement
 * Description          : This function invokes WiFi hal api wifi_getApRoamingConsortiumElement
 * @param [in] req-     : apIndex - access point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApRoamingConsortiumElement(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApRoamingConsortiumElement ----->Entry\n");

    wifi_roamingConsortiumElement_t roam = {0};
    int apIndex = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    char tempstr[33] = {'\0'};
    int elemCount = 0;
    int index = 0;
    int len= 0;

    if(&req["apIndex"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();

    return_status = wifi_getApRoamingConsortiumElement(apIndex, &roam);
    if(return_status == SSP_SUCCESS)
    {
        elemCount = (int)roam.wifiRoamingConsortiumCount;
        sprintf(details, "wifi_getApRoamingConsortiumElement output is: EntryCount %d", elemCount);
        for(index=0; index<3; ++index)
        {
                tempstr[0] = '\0';
                for(len=0; len<roam.wifiRoamingConsortiumLen[index] && len<16; ++len) {
                        sprintf(&tempstr[len*2], "%02x", roam.wifiRoamingConsortiumOui[index][len]);
                }
                sprintf(details + strlen(details), ", OUI[%d] %s, LenOfOUI[%d] %u", index, tempstr, index, roam.wifiRoamingConsortiumLen[index]);
        }
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getApRoamingConsortiumElement operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApRoamingConsortiumElement ---->Error in execution\n");
        return;
    }
}


/*******************************************************************************************
 * Function Name        : WIFIHAL_PushApRoamingConsortiumElement
 * Description          : This function invokes WiFi hal api wifi_pushApRoamingConsortiumElement
 * @param [in] req-     : apIndex - access point index
                        : ouiCount - no: of OUIs to be set
                        : ouiList - OUI values to be est
                        : ouiLen - length of each OUI value
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_PushApRoamingConsortiumElement(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApRoamingConsortiumElement ----->Entry\n");

    wifi_roamingConsortiumElement_t roam = {0};
    int apIndex = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    char tempOui[110] = {'\0'};
    char tempOuiLen[10] = {'\0'};
    char *token = NULL;
    int index = 0;
    int len = 0;
    unsigned int ouiInt = 0;

    if(&req["apIndex"]==NULL || &req["ouiList"]==NULL || &req["ouiCount"]==NULL || &req["ouiLen"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    apIndex = req["apIndex"].asInt();
    strcpy(tempOui, req["ouiList"].asCString());
    roam.wifiRoamingConsortiumCount = req["ouiCount"].asInt();
    strcpy(tempOuiLen, req["ouiLen"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\n tempOui = %s, ouiCount = %u, tempOuiLen = %s\n",tempOui, roam.wifiRoamingConsortiumCount, tempOuiLen);

    //split and save the input oui lengths' list
    token = strtok(tempOuiLen, ",");
    while (token != NULL && index < 3)
    {
        roam.wifiRoamingConsortiumLen[index]=atoi(token);
        DEBUG_PRINT(DEBUG_TRACE,"\n wifiRoamingConsortiumOuiLen[%d] = %u\n", index, roam.wifiRoamingConsortiumLen[index]);
        index++;
        token = strtok(NULL, ",");
    }

    //split and save the input oui list
    token = strtok(tempOui, ",");
    index = 0;
    while (token != NULL && index < 3)
    {
        len=0;
        while (sscanf(&token[len*2], "%2x", &ouiInt) != EOF and len<15)
        {
            roam.wifiRoamingConsortiumOui[index][len] = (unsigned char)ouiInt;
            DEBUG_PRINT(DEBUG_TRACE,"\n roam.wifiRoamingConsortiumOui[%d][%d] = %u\n", index, len, ouiInt);
            len++;
        }
        index++;
        token = strtok(NULL, ",");
    }

    return_status = wifi_pushApRoamingConsortiumElement(apIndex, &roam);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_pushApRoamingConsortiumElement operation is success");
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_pushApRoamingConsortiumElement operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApRoamingConsortiumElement ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
*
 * Function Name        : WIFIHAL_GetApInterworkingElement
 * Description          : This function invokes WiFi hal get api wifi_getApInterworkingElement()
 * @param [in] req-     : RadioIndex. 0 - 2.4GHz, 1 - 5GHz
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApInterworkingElement (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApInterworkingElement ----->Entry\n");
    wifi_InterworkingElement_t element;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[1000] = {'\0'};
    if(&req["radioIndex"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    radioIndex = req["radioIndex"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\n Get operation requested\n");
    return_status = wifi_getApInterworkingElement(radioIndex, &element);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "Value returned is :interworkingEnabled=%d, accessNetworkType=%d, internetAvailable=%d, asra=%d, esra=%d, uesa=%d, venueOptionPresent=%d, venueType=%d, venueGroup=%d, hessOptionPresent=%d, hessid=%s", element.interworkingEnabled, element.accessNetworkType, element.internetAvailable, element.asra, element.esr, element.uesa, element.venueOptionPresent, element.venueType, element.venueGroup, element.hessOptionPresent, element.hessid);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
	response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getApInterworkingElement operation failed");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetApInterworkingElement  --->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_PushApInterworkingElement
 * Description          : This function invokes WiFi hal push api wifi_pushApInterworkingElement()
 * @param [in] req-     : radioIndex - radio Index value of wifi
                          interworkingEnabled - if Interworking Service is enabled or disabled(0/1)
                          accessNetworkType - Network Type(0-15), specifies the type of network - Optional parameter
                          internetAvailable - Internet available or not - Optional parameter
                          asra - Optional parameter
                          esra - Optional parameter
                          uesa - Optional parameter
                          venueOptionPresent - Optional parameter - True when venue information has been provided
                          venueType - Optional parameter
                          venueGroup - Optional parameter
                          hessOptionPresent - Optional parameter - True when hessid is present
                          hessid - Optional parameter - Mac Address
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_PushApInterworkingElement (IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApInterworkingElement ----->Entry\n");
    wifi_InterworkingElement_t element;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[500] = {'\0'};

    if(&req["radioIndex"]== NULL || &req["interworkingEnabled"]== NULL || &req["accessNetworkType"]== NULL || &req["internetAvailable"]== NULL || &req["asra"]== NULL || &req["esra"]== NULL || &req["uesa"]== NULL || &req["venueOptionPresent"]== NULL || &req["venueType"]== NULL || &req["venueGroup"]== NULL &req["hessOptionPresent"]== NULL || &req["hessid"]== NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }
    radioIndex = req["radioIndex"].asInt();
    element.interworkingEnabled = req["interworkingEnabled"].asBool();
    element.accessNetworkType = req["accessNetworkType"].asUInt();
    element.internetAvailable = req["internetAvailable"].asBool();
    element.asra = req["asra"].asBool();
    element.esr = req["esra"].asBool();
    element.uesa = req["uesa"].asBool();
    element.venueOptionPresent = req["venueOptionPresent"].asBool();
    element.venueType = req["venueType"].asInt();
    element.venueGroup = req["venueGroup"].asInt();
    element.hessOptionPresent = req["hessOptionPresent"].asBool();
    strcpy(element.hessid, req["hessid"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n Invoking wifi_pushApInterworkingElement\n");
    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;

    printf("is sock api\n");
    strncpy(apiInfo.api_name, "wifi_pushApInterworkingElement", 1024);
    memcpy(apiInfo.api_data, &element, sizeof(wifi_InterworkingElement_t));
    apiInfo.radioIndex = radioIndex;
    return_status = wifi_api_send_msg(&apiInfo);
    #else
    return_status = wifi_pushApInterworkingElement(radioIndex, &element);
    #endif
    printf("\n wifi_pushApInterworkingElement, ret:status %d \n", return_status);

    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_pushApInterworkingElement was invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_pushApInterworkingElement was not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApInterworkingElement ---->Error in execution\n");
        return;
    }
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_EnableCSIEngine
 * Description          : This function invokes WiFi hal api wifi_enableCSIEngine()
 * @param [in] req-     : apIndex - WiFi Access Point Index value
                          MacAddress - Mac Address of client device connected
                          enable - Whether CSI data collection is enabled or not
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_EnableCSIEngine(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_EnableCSIEngine ----->Entry\n");
    int apIndex = 0;
    mac_address_t MAC;
    char mac[20] = {'\0'};
    unsigned int tmp_MACConv[6] = {0};
    unsigned char enable;
    int return_status = SSP_FAILURE;
    char details[500] = {'\0'};

    if(&req["apIndex"]==NULL || &req["MacAddress"]==NULL || &req["enable"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    enable = req["enable"].asInt();
    strcpy(mac, req["MacAddress"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &tmp_MACConv[0], &tmp_MACConv[1], &tmp_MACConv[2], &tmp_MACConv[3], &tmp_MACConv[4], &tmp_MACConv[5]);

    for(int index = 0 ; index <6; index++)
    {
        MAC[index]=(unsigned char)tmp_MACConv[index];
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d, MAC : %s, Enable : %d\n", apIndex, MAC, enable);
    return_status = wifi_enableCSIEngine(apIndex, MAC, enable);
    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_enableCSIEngine was invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_enableCSIEngine was not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_EnableCSIEngine ---->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_EnableCSIEngine ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_SendDataFrame
 * Description          : This function invokes WiFi hal api wifi_sendDataFrame()
 * @param [in] req-     : apIndex - Index of VAP
 *                        MacAddress - MAC address of the station associated in this VAP
 *                        length - length of data
 *                        insert_llc - whether LLC header should be inserted. If set to TRUE, HAL implementation MUST insert the following bytes before type field. DSAP = 0xaa, SSAP = 0xaa, Control = 0x03, followed by 3 bytes each = 0x00
 *                        protocol - ethernet protocol
 *                        priority - priority of the frame with which scheduler should transmit the frame
 *
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SendDataFrame(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SendDataFrame ----->Entry\n");
    int apIndex = 0;
    mac_address_t sta;
    char mac[20] = {'\0'};
    unsigned int tmp_MACConv[6] = {0};
    unsigned char data = 0;
    unsigned int length = 0;
    unsigned char insert_llc = 0;
    unsigned int protocol = 0;
    unsigned int priority = 0;
    wifi_data_priority_t prio = wifi_data_priority_be;
    int return_status = SSP_FAILURE;
    char details[500] = {'\0'};

    if(&req["apIndex"]==NULL || &req["MacAddress"]==NULL || &req["length"]==NULL || &req["protocol"]==NULL || &req["priority"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    length = req["length"].asInt();
    protocol = req["protocol"].asInt();
    insert_llc = req["insert_llc"].asInt();
    priority = req["priority"].asInt();
    prio = wifi_data_priority_t(priority);
    strcpy(mac, req["MacAddress"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &tmp_MACConv[0], &tmp_MACConv[1], &tmp_MACConv[2], &tmp_MACConv[3], &tmp_MACConv[4], &tmp_MACConv[5]);

    for(int index = 0 ; index <6; index++)
    {
        sta[index]=(unsigned char)tmp_MACConv[index];
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d, MAC : %s, Length : %d, Insert_LLC : %d, Protocol : %d, Priority : %d\n", apIndex, sta, length, insert_llc, protocol, prio);
    return_status = wifi_sendDataFrame(apIndex, sta, &data, length, insert_llc, protocol, prio);

    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_sendDataFrame was invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_sendDataFrame was not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SendDataFrame ---->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SendDataFrame ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetVAPTelemetry
 * Description          : This function invokes WiFi hal get api wifi_getVAPTelemetry()
 * @param [in] req-     : apIndex - Access Point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetVAPTelemetry(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetVAPTelemetry ----->Entry\n");
    wifi_VAPTelemetry_t VAPTelemetry;
    int apIndex = 0;
    int return_status = SSP_FAILURE;
    char details[1000] = {'\0'};

    if (&req["apIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    return_status = wifi_getVAPTelemetry(apIndex, &VAPTelemetry);

    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "\n wifi_getVAPTelemetry was invoked successfully; Value returned is : txOverflow = %lu", VAPTelemetry.txOverflow);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "\n wifi_getVAPTelemetry not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetVAPTelemetry  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetVAPTelemetry ---->Exiting\n");
    return;
}

/*******************************************************************************************
 * Function Name        : WIFIHAL_GetRadioVapInfoMap
 * Description          : This function invokes WiFi hal api wifi_getRadioVapInfoMap
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioVapInfoMap(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioVapInfoMap ----->Entry\n");
    wifi_radio_index_t radioIndex = 0;
    wifi_vap_info_map_t map;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};

    if(&req["apIndex"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["apIndex"].asInt();

    return_status = wifi_getRadioVapInfoMap(radioIndex, &map);
    if(return_status == SSP_SUCCESS)
    {

        sprintf(details,"The numner of Radio maps are : %lu, ",map.num_vaps);
        response["result"]="SUCCESS";
        response["details"]=details;
        return;
    }
    else
    {
        sprintf(details, "wifi_getRadioVapInfoMap operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioVapInfoMap ---->Error in execution\n");
        return;
    }
	DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioVapInfoMap ----->Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_SetNeighborReports
 * Description          : This function invokes WiFi hal api wifi_setNeighborReports()
 * @param [in] req-     : apIndex - Index of VAP
 *                        reports - Number of reports in the in_NeighborReports set
 *                        bssid - MAC address of the connected client
 *                        info - information on the bssid
 *                        opClass - regulatory data
 *                        channel - radio channel value
 *                        phyTable - physical type
 *
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SetNeighborReports(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetNeighborReports ----->Entry\n");
    unsigned int apIndex = 0;
    unsigned int reports = 0;
    bssid_t MacAddress;
    char mac[20] = {'\0'};
    unsigned int tmp_MACConv[6] = {0};
    wifi_NeighborReport_t neighborReports;
    int max_count = 6;
    int return_status = SSP_FAILURE;
    char details[500] = {'\0'};

    if(&req["apIndex"]==NULL || &req["reports"]==NULL || &req["bssid"]==NULL || &req["info"]==NULL || &req["opClass"]==NULL || &req["channel"]==NULL || &req["phyTable"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    reports = req["reports"].asInt();
    neighborReports.info = req["info"].asInt();
    neighborReports.opClass = req["opClass"].asInt();
    neighborReports.channel = req["channel"].asInt();
    neighborReports.phyTable = req["phyTable"].asInt();

    strcpy(mac, req["bssid"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &tmp_MACConv[0], &tmp_MACConv[1], &tmp_MACConv[2], &tmp_MACConv[3], &tmp_MACConv[4], &tmp_MACConv[5]);
    for(int index = 0 ; index < max_count; index++)
    {
        MacAddress[index]=(unsigned char)tmp_MACConv[index];
    }
    memcpy(neighborReports.bssid, MacAddress, max_count);

    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d, Number of reports : %d, BSSID : %s, Info : %d, opClass : %d, Channel : %d, PhyTable : %d\n", apIndex, reports, neighborReports.bssid, neighborReports.info, neighborReports.opClass, neighborReports.channel, neighborReports.phyTable);
    return_status = wifi_setNeighborReports(apIndex, reports, &neighborReports);

    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_setNeighborReports was invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_setNeighborReports was not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetNeighborReports ---->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetNeighborReports ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApAssociatedClientDiagnosticResult
 * Description          : This function invokes WiFi hal api wifi_getApAssociatedClientDiagnosticResult
 * @param [in] req-     : apIndex - ap index of the wifi
 *                      : mac_addr - client MAC address
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApAssociatedClientDiagnosticResult(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedClientDiagnosticResult ----->Entry\n");
    wifi_associated_dev3_t *dev_conn = (wifi_associated_dev3_t *) malloc(sizeof(wifi_associated_dev3_t));
    memset(dev_conn, 0, sizeof(wifi_associated_dev3_t));
    int apIndex = 0;
    char MAC[64] = {'\0'};
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};

    if(&req["apIndex"]==NULL || &req["mac_addr"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    strcpy(MAC, req["mac_addr"].asCString());

    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d, MAC : %s\n", apIndex, MAC);
    return_status = wifi_getApAssociatedClientDiagnosticResult(apIndex, MAC, dev_conn);

    if(return_status == SSP_SUCCESS)
    {
        printf("\nWIFIHALGetApAssociatedClientDiagnosticResult::Success\n");
        printf("\nClient Diagnostic Result : MAC=%02x:%02x:%02x:%02x:%02x:%02x, IP=%s, AuthState=%d, LastDataDownlinkRate=%u, LastDataUplinkRate=%u, SignalStrength=%d, Retransmissions=%u, Active=%d, OperatingStd= %s, OperatingChBw=%s, SNR=%d, interferenceSources=%s, DataFramesSentAck=%lu, cli_DataFramesSentNoAck=%lu, cli_BytesSent=%lu, cli_BytesReceived=%lu, cli_RSSI=%d, cli_MinRSSI=%d, cli_MaxRSSI=%d, Disassociations=%u, AuthFailures=%u, cli_Associations=%llu, PacketsSent=%lu, PacketsReceived=%lu, ErrorsSent=%lu, RetransCount=%lu, FailedRetransCount=%lu, RetryCount=%lu, MultipleRetryCount=%lu, MaxDownlinkRate=%u, MaxUplinkRate=%u\n", dev_conn->cli_MACAddress[0], dev_conn->cli_MACAddress[1], dev_conn->cli_MACAddress[2], dev_conn->cli_MACAddress[3], dev_conn->cli_MACAddress[4], dev_conn->cli_MACAddress[5], dev_conn->cli_IPAddress, dev_conn->cli_AuthenticationState, dev_conn->cli_LastDataDownlinkRate, dev_conn->cli_LastDataUplinkRate, dev_conn->cli_SignalStrength, dev_conn->cli_Retransmissions, dev_conn->cli_Active, dev_conn->cli_OperatingStandard, dev_conn->cli_OperatingChannelBandwidth, dev_conn->cli_SNR, dev_conn->cli_InterferenceSources, dev_conn->cli_DataFramesSentAck, dev_conn->cli_DataFramesSentNoAck, dev_conn->cli_BytesSent, dev_conn->cli_BytesReceived, dev_conn->cli_RSSI, dev_conn->cli_MinRSSI, dev_conn->cli_MaxRSSI, dev_conn->cli_Disassociations, dev_conn->cli_AuthenticationFailures, dev_conn->cli_Associations, dev_conn->cli_PacketsSent, dev_conn->cli_PacketsReceived, dev_conn->cli_ErrorsSent, dev_conn->cli_RetransCount, dev_conn->cli_FailedRetransCount, dev_conn->cli_RetryCount, dev_conn->cli_MultipleRetryCount, dev_conn->cli_MaxDownlinkRate, dev_conn->cli_MaxUplinkRate);

        sprintf(details,"Client Diagnostic Result : MAC=%02x:%02x:%02x:%02x:%02x:%02x, IP=%s, AuthState=%d, LastDataDownlinkRate=%u, LastDataUplinkRate=%u, SignalStrength=%d, Retransmissions=%u, Active=%d, OperatingStd= %s, OperatingChBw=%s, SNR=%d, interferenceSources=%s, DataFramesSentAck=%lu, cli_DataFramesSentNoAck=%lu, cli_BytesSent=%lu, cli_BytesReceived=%lu, cli_RSSI=%d, cli_MinRSSI=%d, cli_MaxRSSI=%d, Disassociations=%u, AuthFailures=%u, cli_Associations=%llu, PacketsSent=%lu, PacketsReceived=%lu, ErrorsSent=%lu, RetransCount=%lu, FailedRetransCount=%lu, RetryCount=%lu, MultipleRetryCount=%lu, MaxDownlinkRate=%u, MaxUplinkRate=%u", dev_conn->cli_MACAddress[0], dev_conn->cli_MACAddress[1], dev_conn->cli_MACAddress[2], dev_conn->cli_MACAddress[3], dev_conn->cli_MACAddress[4], dev_conn->cli_MACAddress[5], dev_conn->cli_IPAddress, dev_conn->cli_AuthenticationState, dev_conn->cli_LastDataDownlinkRate, dev_conn->cli_LastDataUplinkRate, dev_conn->cli_SignalStrength, dev_conn->cli_Retransmissions, dev_conn->cli_Active, dev_conn->cli_OperatingStandard, dev_conn->cli_OperatingChannelBandwidth, dev_conn->cli_SNR, dev_conn->cli_InterferenceSources, dev_conn->cli_DataFramesSentAck, dev_conn->cli_DataFramesSentNoAck, dev_conn->cli_BytesSent, dev_conn->cli_BytesReceived, dev_conn->cli_RSSI, dev_conn->cli_MinRSSI, dev_conn->cli_MaxRSSI, dev_conn->cli_Disassociations, dev_conn->cli_AuthenticationFailures, dev_conn->cli_Associations, dev_conn->cli_PacketsSent, dev_conn->cli_PacketsReceived, dev_conn->cli_ErrorsSent, dev_conn->cli_RetransCount, dev_conn->cli_FailedRetransCount, dev_conn->cli_RetryCount, dev_conn->cli_MultipleRetryCount, dev_conn->cli_MaxDownlinkRate, dev_conn->cli_MaxUplinkRate);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getApAssociatedClientDiagnosticResult operation failed");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedClientDiagnosticResult ---->Error in execution\n");
    }

    free(dev_conn);
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApAssociatedClientDiagnosticResult ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetAPCapabilities
 * Description          : This function invokes WiFi hal get api wifi_getAPCapabilities()
 * @param [in] req-     : apIndex - Access Point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetAPCapabilities(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAPCapabilities ----->Entry\n");
    wifi_ap_capabilities_t *apCapabilities = (wifi_ap_capabilities_t *)malloc(sizeof(wifi_ap_capabilities_t));
    memset(apCapabilities, 0, sizeof(wifi_ap_capabilities_t));
    int apIndex = 0;
    int return_status = SSP_FAILURE;
    char details[1000] = {'\0'};
    char output[1000] = {'\0'};

    if (&req["apIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);

    return_status = wifi_getAPCapabilities(apIndex, apCapabilities);

    if(return_status == SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetAPCapabilities::Success; Access Point Capabilities : RTS Threshold Supported = %s, Security Modes Supported = 0x%04x, Onboarding Methods Supported = 0x%04x, WMM Supported = %s, UAPSD Supported = %s, Interworking Service Supported = %s, BSS Transition Implemented = %s\n", (apCapabilities->rtsThresholdSupported) ? "TRUE" : "FALSE", apCapabilities->securityModesSupported, apCapabilities->methodsSupported, (apCapabilities->WMMSupported) ? "TRUE" : "FALSE", (apCapabilities->UAPSDSupported) ? "TRUE" : "FALSE", (apCapabilities->interworkingServiceSupported) ? "TRUE" : "FALSE", (apCapabilities->BSSTransitionImplemented) ? "TRUE" : "FALSE");

        sprintf(output, "Access Point Capabilities : RTS Threshold Supported = %s, Security Modes Supported = 0x%04x, Onboarding Methods Supported = 0x%04x, WMM Supported = %s, UAPSD Supported = %s, Interworking Service Supported = %s, BSS Transition Implemented = %s\n", (apCapabilities->rtsThresholdSupported) ? "TRUE" : "FALSE", apCapabilities->securityModesSupported, apCapabilities->methodsSupported, (apCapabilities->WMMSupported) ? "TRUE" : "FALSE", (apCapabilities->UAPSDSupported) ? "TRUE" : "FALSE", (apCapabilities->interworkingServiceSupported) ? "TRUE" : "FALSE", (apCapabilities->BSSTransitionImplemented) ? "TRUE" : "FALSE");

        sprintf(details, "wifi_getAPCapabilities invoked successfully; Details : %s", output);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "\n wifi_getAPCapabilities not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAPCapabilities  --->Error in execution\n");
    }

    free(apCapabilities);
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAPCapabilities ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetAvailableBSSColor
 * Description          : This function invokes WiFi hal's wifi_getAvailableBSSColor() api
 * @param [in] req-     : radioIndex - radio index value of wifi
 *                        maxNumberColors - WL_COLOR_MAX_VALUE from wlioctl.h
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetAvailableBSSColor(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAvailableBSSColor --->Entry\n");
    int radioIndex = 0;
    int maxNumberColors = 0;
    unsigned char colorList[200] = {0};
    int numColorReturned = 0;
    int return_status = SSP_FAILURE;
    char details[1000] = {'\0'};
    char details_add[200] = {'\0'};
    int iteration = 0;

    if(&req["radioIndex"]==NULL || &req["maxNumberColors"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["radioIndex"].asInt();
    maxNumberColors = req["maxNumberColors"].asInt();

    DEBUG_PRINT(DEBUG_TRACE,"\n radioIndex : %d, maxNumberColors : %d", radioIndex, maxNumberColors);
    return_status = wifi_getAvailableBSSColor(radioIndex, maxNumberColors, colorList, &numColorReturned);

    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "WIFIHAL_GetAvailableBSSColor operation success :: NumColorReturned : %d, ", numColorReturned);
	DEBUG_PRINT(DEBUG_TRACE, "\nWIFIHAL_GetAvailableBSSColor operation success :: NumColorReturned : %d, ", numColorReturned);

        if (numColorReturned > 0)
        {
            sprintf(details_add, " Available BSSColor List = ");
	    DEBUG_PRINT(DEBUG_TRACE, "\nAvailable BSSColor List = ");
            strcat(details, details_add);
            for (iteration = 0; iteration < numColorReturned; iteration++)
            {
		printf("%d ", colorList[iteration]);
                sprintf(details_add, "%d ", colorList[iteration]);
                strcat(details, details_add);
            }
        }
        else
        {
             DEBUG_PRINT(DEBUG_TRACE, "\nAvailable BSSColor List is Empty\n");
             sprintf(details_add, " Available BSSColor List is Empty\n");
             strcat(details, details_add);
        }

        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "WIFIHAL_GetAvailableBSSColor operation failed");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAvailableBSSColor --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetAvailableBSSColor ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetFTMobilityDomainID
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
 *                        get /set is related to FTMobilityDomainID
 * @param [in] req-     : methodName - HAL API name (wifi_getFTMobilityDomainID or wifi_setFTMobilityDomainID)
 *                        apIndex - Access Point index
 *                        radioIndex - WiFi Radio Index
 *                        mobilityDomain - Value of the FT Mobility Domain for this AP to get/set
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetFTMobilityDomainID(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTMobilityDomainID  ----->Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[200] = {'\0'};
    int size = 64;
    unsigned char mobilityDomain[64] = {'\0'};
    int mobilityDomain_Int = 0;
    int * mobilityDomain_IntPtr = NULL;
    char details_add[200] = {'\0'};

    if(&req["apIndex"]==NULL || &req["methodName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(methodName, req["methodName"].asCString());
    apIndex = req["apIndex"].asInt();

    if(!strncmp(methodName, "set",3))
    {
        printf("wifi_setFTMobilityDomainID operation to be done\n");

        if(&req["mobilityDomain"]==NULL || &req["radioIndex"]==NULL)
        {
            response["result"]="FAILURE";
            response["details"]="NULL parameter as input argument";
            return;
        }

        mobilityDomain_Int = req["mobilityDomain"].asInt();
        mobilityDomain_IntPtr = &mobilityDomain_Int;
        memcpy(mobilityDomain, (char *)mobilityDomain_IntPtr, size);
        radioIndex = req["radioIndex"].asInt();

        DEBUG_PRINT(DEBUG_TRACE,"\n apIndex : %d", apIndex);
        DEBUG_PRINT(DEBUG_TRACE,"\n Mobility Domain ID[0] : 0x%x, Mobility Domain ID[1] : 0x%x", mobilityDomain[0], mobilityDomain[1]);
        return_status = wifi_setFTMobilityDomainID(apIndex, mobilityDomain);

        if(return_status == SSP_SUCCESS)
        {
            sprintf(details_add, "wifi_%s operation success;", methodName);
            strcat(details, details_add);

            return_status = ssp_WIFIHALApplySettings(radioIndex,methodName);
            if(return_status == SSP_SUCCESS)
            {
                sprintf(details_add, " applyRadioSettings operation success");
                strcat(details, details_add);
            }
            else
            {
                sprintf(details_add, " applyRadioSettings operation failed");
                strcat(details, details_add);
            }

            response["result"]="SUCCESS";
            response["details"]=details;
        }
        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTMobilityDomainID --->Error in execution\n");
        }
    }
    else
    {
        printf("wifi_getFTMobilityDomainID operation to be done\n");
	return_status = wifi_getFTMobilityDomainID(apIndex, mobilityDomain);

        if(return_status == SSP_SUCCESS)
        {
            sprintf(details, "Mobility Domain ID[0] : 0x%x, Mobility Domian ID[1] : 0x%x", mobilityDomain[0], mobilityDomain[1]);
            DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHALGetOrSetFTMobilityDomainID::Success, details: %s", details);
            response["result"]="SUCCESS";
            response["details"]=details;
        }
        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTMobilityDomainID --->Error in execution\n");
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTMobilityDomainID ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetFTR0KeyHolderID
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
 *                        get /set is related to FTR0KeyHolderID
 * @param [in] req-     : methodName - HAL API name (wifi_getFTR0KeyHolderID or wifi_setFTR0KeyHolderID)
 *                        apIndex - Access Point index
 *                        radioIndex - WiFi Radio Index
 *                        KeyHolderID - Value of the FTR0 Key Holder ID for this AP to get/set
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetFTR0KeyHolderID(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTR0KeyHolderID  ----->Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    unsigned char key_id[64] = {'\0'};
    char KeyHolderID[64] = {'\0'};
    char details_add[1000] = {'\0'};

    if(&req["apIndex"]==NULL || &req["methodName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    strcpy(methodName, req["methodName"].asCString());

    if(!strncmp(methodName, "set",3))
    {
        printf("wifi_setFTR0KeyHolderID operation to be done\n");

        if(&req["KeyHolderID"]==NULL || &req["radioIndex"]==NULL)
        {
            response["result"]="FAILURE";
            response["details"]="NULL parameter as input argument";
            return;
        }

        strcpy(KeyHolderID, req["KeyHolderID"].asCString());
        memcpy(&key_id[0], KeyHolderID, strlen(KeyHolderID));
        radioIndex = req["radioIndex"].asInt();

        DEBUG_PRINT(DEBUG_TRACE,"\n apIndex : %d", apIndex);
        DEBUG_PRINT(DEBUG_TRACE,"\n Key Holder ID : %s", KeyHolderID);
        DEBUG_PRINT(DEBUG_TRACE,"\n Key_ID : %p\n", &key_id[0]);

        if(key_id[0] == '\0')
        {
            DEBUG_PRINT(DEBUG_TRACE, "Key Holder ID[0] : 0x%x", key_id[0]);
        }
        else
        {
            for(int index = 0; key_id[index] != '\0'; index++)
            {
                DEBUG_PRINT(DEBUG_TRACE, "Key Holder ID[%d] : 0x%x", index, key_id[index]);
            }
        }
        return_status = wifi_setFTR0KeyHolderID(apIndex, key_id);

        if(return_status == SSP_SUCCESS)
        {
            sprintf(details_add, "wifi_%s operation success;", methodName);
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", details_add);
            strcat(details, details_add);
            return_status = ssp_WIFIHALApplySettings(radioIndex,methodName);

            if(return_status == SSP_SUCCESS)
            {
                sprintf(details_add, " applyRadioSettings operation success");
                DEBUG_PRINT(DEBUG_TRACE,"\n%s", details_add);
                strcat(details, details_add);
            }
            else
            {
                sprintf(details_add, " applyRadioSettings operation failed");
                DEBUG_PRINT(DEBUG_TRACE,"\n%s", details_add);
                strcat(details, details_add);
            }
            response["result"]="SUCCESS";
            response["details"]=details;
        }

        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTR0KeyHolderID --->Error in execution\n");
        }
    }

    else
    {
        printf("wifi_getFTR0KeyHolderID operation to be done\n");
        return_status = wifi_getFTR0KeyHolderID(apIndex, key_id);
        if(return_status == SSP_SUCCESS)
        {
            sprintf(details_add, "FTR0 Key Holder ID Details -");
            strcat(details, details_add);

            if(key_id[0] == '\0')
            {
                sprintf(details_add, " Key Holder ID[0] : 0x%x", key_id[0]);
                strcat(details, details_add);
            }
            else
            {
                for(int index = 0; key_id[index] != '\0'; index++)
                {
                    sprintf(details_add, " Key Holder ID[%d] : 0x%x", index, key_id[index]);
                    strcat(details, details_add);
                }
            }

            DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
            response["result"]="SUCCESS";
            response["details"]=details;
        }
        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTR0KeyHolderID --->Error in execution\n");
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTR0KeyHolderID ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRMCapabilities
 * Description          : This function invokes WiFi hal api wifi_getRMCapabilities
 * @param [in] req-     : peer - connected client mac address
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRMCapabilities(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRMCapabilities ----->Entry\n");
    mac_address_t peer;
    int max_size = 6;
    char mac[20] = {'\0'};
    unsigned int tmp_MACConv[6] = {0};
    unsigned char out_Capabilities[5] = {'\0'};
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};

    if(&req["peer"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    strcpy(mac, req["peer"].asCString());
    sscanf(mac, "%02x:%02x:%02x:%02x:%02x:%02x", &tmp_MACConv[0], &tmp_MACConv[1], &tmp_MACConv[2], &tmp_MACConv[3], &tmp_MACConv[4], &tmp_MACConv[5]);

    for(int index = 0 ; index < max_size; index++)
    {
        peer[index]=(unsigned char)tmp_MACConv[index];
    }

    DEBUG_PRINT(DEBUG_TRACE,"\nPeer : %s\n", peer);
    return_status = wifi_getRMCapabilities((char*)peer, out_Capabilities);

    if(return_status == SSP_SUCCESS)
    {
        sprintf(details,"wifi_getRMCapabilities operation success : capabilities[0] : %02X, capabilities[1] : %02X, capabilities[2] : %02X, capabilities[3] :  %02X, capabilities[4] : %02X ", out_Capabilities[0], out_Capabilities[1], out_Capabilities[2], out_Capabilities[3], out_Capabilities[4]);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getRMCapabilities operation failed");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRMCapabilities ---->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRMCapabilities ---->Exiting\n");
    return;
}


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApSecurity
 * Description          : This function invokes WiFi hal get api wifi_getApSecurity()
 * @param [in] req-     : apIndex - Access Point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApSecurity(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApSecurity ----->Entry\n");
    wifi_vap_security_t security;
    int apIndex = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    char output[2000] = {'\0'};

    if (&req["apIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);
    return_status = wifi_getApSecurity(apIndex, &security);

    if(return_status == SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetApSecurity::Success; AP Security details : Security Mode : 0x%04x, Encrytion Method : %d, WPA3 Transition : %s, Rekey Interval : %d, Strict Rekey : %s, Eapol Key Timeout : %d, Eapol Key Retries : %d, Eap Identity Timeout : %d, Eap Identity Retries : %d, Eap Timeout : %d, Eap Retries : %d, PMKSA Cashing : %s, Security Key Type : %d", security.mode, security.encr, security.wpa3_transition_disable ? "Disabled" : "Enabled", security.rekey_interval, security.strict_rekey ? "Disabled" : "Enabled", security.eapol_key_timeout, security.eapol_key_retries, security.eap_identity_req_timeout, security.eap_identity_req_retries, security.eap_req_timeout, security.eap_req_retries, security.disable_pmksa_caching ? "Disabled" : "Enabled", security.u.key.type);

        sprintf(output, "AP Security details : Security Mode : 0x%04x, Encrytion Method : %d, WPA3 Transition : %s, Rekey Interval : %d, Strict Rekey : %s, Eapol Key Timeout : %d, Eapol Key Retries : %d, Eap Identity Timeout : %d, Eap Identity Retries : %d, Eap Timeout : %d, Eap Retries : %d, PMKSA Cashing : %s, Security Key Type : %d", security.mode, security.encr, security.wpa3_transition_disable ? "Disabled" : "Enabled", security.rekey_interval, security.strict_rekey ? "Disabled" : "Enabled", security.eapol_key_timeout, security.eapol_key_retries, security.eap_identity_req_timeout, security.eap_identity_req_retries, security.eap_req_timeout, security.eap_req_retries, security.disable_pmksa_caching ? "Disabled" : "Enabled", security.u.key.type);
        strcat(details, output);

        if (security.u.key.type == wifi_security_key_type_psk)
        {
            printf(", WPA PSK : 0x%s", security.u.key.key);
            sprintf(output, ", WPA PSK : 0x%s", security.u.key.key);
            strcat(details, output);
        }
        else
        {
            printf(", WPA Passphrase : %s", security.u.key.key);
            sprintf(output, ", WPA Passphrase : %s", security.u.key.key);
            strcat(details, output);
        }

        #if defined(WIFI_HAL_VERSION_3)
        printf(", MFP : %d", security.mfp);
        sprintf(output, ", MFP : %d", security.mfp);
        strcat(details, output);
        #endif
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getApSecurity not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApSecurity  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApSecurity ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_SetApSecurity
 * Description          : This function invokes WiFi hal get api wifi_setApSecurity()
 * @param [in] req-     : apIndex - Access Point index
 *                        mode - Access Point security mode
 *                        mfp - MFP value disabled, optional or required
 *                        encr - Access Point encryption method
 *                        key_type - Access Point key type
 *                        key - Access Point key according to the key type
 *                        wpa3_transition_disable - If Access Point mode is WPA3-Personal-Transition,
 *                        then wpa3_transition_enable will hold its enable state
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SetApSecurity(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApSecurity ----->Entry\n");
    wifi_vap_security_t security;
    int apIndex = 0;
    int mode = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};

    if (&req["apIndex"] == NULL || &req["mode"] == NULL || &req["mfp"] == NULL || &req["encr"] == NULL || &req["key_type"] == NULL || &req["key"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);

    mode = req["mode"].asInt();
    switch(mode)
    {
        case 1 :
                security.mode = wifi_security_mode_none;
                break;
        case 2 :
                security.mode = wifi_security_mode_wep_64;
                break;
        case 4 :
                security.mode = wifi_security_mode_wep_128;
                break;
        case 8 :
                security.mode = wifi_security_mode_wpa_personal;
                break;
        case 16 :
                security.mode = wifi_security_mode_wpa2_personal;
                break;
        case 32 :
                security.mode = wifi_security_mode_wpa_wpa2_personal;
                break;
        case 64 :
                security.mode = wifi_security_mode_wpa_enterprise;
                break;
        case 128 :
                security.mode = wifi_security_mode_wpa2_enterprise;
                break;
        case 256 :
                security.mode = wifi_security_mode_wpa_wpa2_enterprise;
                break;
        case 512 :
                security.mode = wifi_security_mode_wpa3_personal;
                break;
        case 1024 :
                security.mode = wifi_security_mode_wpa3_transition;

                if (&req["wpa3_transition_disable"] == NULL)
                {
                    response["result"]="FAILURE";
                    response["details"]="WPA3 Transition Disable parameter is not received when security mode is WPA3-Personal-Transition";
                    return;
                }
                else
                {
                    security.wpa3_transition_disable = req["wpa3_transition_disable"].asBool();
                    DEBUG_PRINT(DEBUG_TRACE,"\n WPA3 Transition Disable : %s", security.wpa3_transition_disable ? "true" : "false");
                }
                break;
        case 2048 :
                security.mode = wifi_security_mode_wpa3_enterprise;
                break;
        default :
               response["result"]="FAILURE";
               response["details"]="Invalid Mode";
               return;
    }
    DEBUG_PRINT(DEBUG_TRACE,"\n Security Mode : 0x%04x", security.mode);

#if defined(WIFI_HAL_VERSION_3)
    security.mfp = (wifi_mfp_cfg_t)req["mfp"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n MFP : %d", security.mfp);
#endif

    security.encr = (wifi_encryption_method_t)req["encr"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Encryption Method : %d", security.encr);

    security.u.key.type = (wifi_security_key_type_t)req["key_type"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Key Type : %d", security.u.key.type);

    strcpy(security.u.key.key, req["key"].asCString());
    DEBUG_PRINT(DEBUG_TRACE,"\n Key : %s", security.u.key.key);

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;

    printf("is sock api\n");
    strncpy(apiInfo.api_name, "wifi_setApSecurity", 1024);
    memcpy(apiInfo.api_data, &security, sizeof(wifi_vap_security_t));
    apiInfo.radioIndex = apIndex;
    return_status = wifi_api_send_msg(&apiInfo);
    #else
    return_status = wifi_setApSecurity(apIndex, &security);
    #endif
    printf("\n wifi_setApSecurity ret:status %d \n", return_status);

    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_setApSecurity invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_setApSecurity not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApSecurity  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApSecurity ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApWpsConfiguration
 * Description          : This function invokes WiFi hal get api wifi_getApWpsConfiguration()
 * @param [in] req-     : apIndex - Access Point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetApWpsConfiguration(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApWpsConfiguration ----->Entry\n");
    wifi_wps_t wpsConfig;
    int apIndex = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    char output[2000] = {'\0'};
    int wps_method = 0;

    if (&req["apIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);
    return_status = wifi_getApWpsConfiguration(apIndex, &wpsConfig);

    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_getApWpsConfiguration invoked successfully; Details : ");
        printf("WIFIHALGetApWpsConfiguration Success :: WPS Mode : %s\n", (wpsConfig.enable ? "Enabled" : "Disabled"));
        sprintf(output, "WPS Mode : %s", (wpsConfig.enable ? "Enabled" : "Disabled"));
        strcat(details, output);

        if (wpsConfig.enable)
        {
            printf("WPS device PIN: %s\n", wpsConfig.pin);
            sprintf(output, ", WPS device PIN: %s", wpsConfig.pin);
            strcat(details, output);

            printf("WPS enabled configuration methods : ");
            sprintf(output, ", WPS enabled configuration methods : ");
            strcat(details, output);

            for(wps_method = WIFI_ONBOARDINGMETHODS_USBFLASHDRIVE; wps_method <= WIFI_ONBOARDINGMETHODS_EASYCONNECT; wps_method = wps_method * 2)
            {

                if (wpsConfig.methods & wps_method)
                {
                    printf("0x%04x ", wps_method);
                    sprintf(output, "0x%04x ", wps_method);
                    strcat(details, output);
                }
            }
        }

        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getApWpsConfiguration not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApWpsConfiguration  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetApWpsConfiguration ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_SetApWpsConfiguration
 * Description          : This function invokes WiFi hal get api wifi_setApWpsConfiguration()
 * @param [in] req-     : apIndex - Access Point index
 *                        enable - Access Point WPS enable status
 *                        pin - Access Point WPS PIN
 *                        num_methods - Number of WPS configuration methods
 *                        methods - Access Point WPS methods
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SetApWpsConfiguration(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApWpsConfiguration ----->Entry\n");
    wifi_wps_t wpsConfig;
    int apIndex = 0;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    char detailsAdd[1000] = {'\0'};
    int wps_method = 0;

    if (&req["apIndex"] == NULL || &req["enable"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);

    wpsConfig.enable = req["enable"].asBool();
    DEBUG_PRINT(DEBUG_TRACE,"\n WPS Mode : %d", wpsConfig.enable);

    if (wpsConfig.enable)
    {
        if (&req["pin"] == NULL || &req["methods"] == NULL || &req["radioIndex"] == NULL)
        {
            response["result"]="FAILURE";
            response["details"]="If WPS mode is set to enable, WPS PIN and WPS Configuration methods cannot be NULL parameters";
            return;
        }

        radioIndex = req["radioIndex"].asInt();
        DEBUG_PRINT(DEBUG_TRACE,"\n radioIndex : %d", radioIndex);

        strcpy(wpsConfig.pin, req["pin"].asCString());
        DEBUG_PRINT(DEBUG_TRACE,"\n WPS PIN : %s", wpsConfig.pin);

        wpsConfig.methods = (wifi_onboarding_methods_t)req["methods"].asInt();
        DEBUG_PRINT(DEBUG_TRACE,"\n WPS Methods : 0x%04x", wpsConfig.methods);
        printf("WPS enabled configuration methods list : ");

        for(wps_method = WIFI_ONBOARDINGMETHODS_USBFLASHDRIVE; wps_method <= WIFI_ONBOARDINGMETHODS_EASYCONNECT; wps_method = wps_method * 2)
        {
            if (wpsConfig.methods & wps_method)
            {
                printf("0x%04x ", wps_method);
            }
        }
    }

    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;

    printf("is sock api\n");
    strncpy(apiInfo.api_name, "wifi_setApWpsConfiguration", 1024);
    memcpy(apiInfo.api_data, &wpsConfig, sizeof(wpsConfig));
    apiInfo.radioIndex = apIndex;
    return_status = wifi_api_send_msg(&apiInfo);
    #else
    return_status = wifi_setApWpsConfiguration(apIndex, &wpsConfig);
    #endif

    if(return_status == SSP_SUCCESS)
    {
        sprintf(detailsAdd, "wifi_setApWpsConfiguration operation success;");
        DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
        strcat(details, detailsAdd);

        return_status = ssp_WIFIHALApplySettings(radioIndex, (char *)"setApWpsConfiguration");

        if(return_status == SSP_SUCCESS)
        {
            sprintf(detailsAdd, " applyRadioSettings operation success");
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            strcat(details, detailsAdd);
            response["result"]="SUCCESS";
        }
        else
        {
            sprintf(detailsAdd, " applyRadioSettings operation failed");
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            strcat(details, detailsAdd);
            response["result"]="FAILURE";
        }

        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_setApWpsConfiguration not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApWpsConfiguration  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetApWpsConfiguration ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetOrSetFTR1KeyHolderID
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
 *                        get /set is related to FTR1KeyHolderID
 * @param [in] req-     : methodName - HAL API name (wifi_getFTR1KeyHolderID or wifi_setFTR1KeyHolderID)
 *                        apIndex - Access Point index
 *                        radioIndex - WiFi Radio Index
 *                        KeyHolderID - Value of the FTR1 Key Holder ID for this AP to get/set
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetOrSetFTR1KeyHolderID(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTR1KeyHolderID  ----->Entry\n");
    char methodName[50] = {'\0'};
    int apIndex = 0;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    unsigned char keyId[64] = {'\0'};
    char keyHolderID[64] = {'\0'};
    char detailsAdd[1000] = {'\0'};

    if(&req["apIndex"]==NULL || &req["methodName"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    strcpy(methodName, req["methodName"].asCString());

    if(!strncmp(methodName, "set",3))
    {
        printf("wifi_setFTR1KeyHolderID operation to be done\n");

        if(&req["KeyHolderID"]==NULL || &req["radioIndex"]==NULL)
        {
            response["result"]="FAILURE";
            response["details"]="NULL parameter as input argument";
            return;
        }

        strcpy(keyHolderID, req["KeyHolderID"].asCString());
        memcpy(&keyId[0], keyHolderID, strlen(keyHolderID));

        radioIndex = req["radioIndex"].asInt();

        DEBUG_PRINT(DEBUG_TRACE,"\n apIndex : %d", apIndex);
        DEBUG_PRINT(DEBUG_TRACE,"\n Key Holder ID : %s", keyHolderID);
        DEBUG_PRINT(DEBUG_TRACE,"\n Key_ID : %p\n", &keyId[0]);

        if(keyId[0] == '\0')
        {
            DEBUG_PRINT(DEBUG_TRACE, "Key Holder ID : 0x%x", keyId[0]);
        }
        else
        {
            for(int index = 0; index < 64 && keyId[index] != '\0'; index++)
            {
                DEBUG_PRINT(DEBUG_TRACE, "Key Holder ID[%d] : 0x%x", index, keyId[index]);
            }
        }

        return_status = wifi_setFTR1KeyHolderID(apIndex, &keyId[0]);

        if(return_status == SSP_SUCCESS)
        {
            sprintf(detailsAdd, "wifi_%s operation success;", methodName);
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            strcat(details, detailsAdd);
            return_status = ssp_WIFIHALApplySettings(radioIndex,methodName);

            if(return_status == SSP_SUCCESS)
            {
                sprintf(detailsAdd, " applyRadioSettings operation success");
                DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
                strcat(details, detailsAdd);
                response["result"]="SUCCESS";
            }
            else
            {
                sprintf(detailsAdd, " applyRadioSettings operation failed");
                DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
                strcat(details, detailsAdd);
                response["result"]="FAILURE";
            }

            response["details"]=details;
        }
        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTR1KeyHolderID --->Error in execution\n");
        }
    }
    else
    {
        printf("wifi_getFTR1KeyHolderID operation to be done\n");
        return_status = wifi_getFTR1KeyHolderID(apIndex, &keyId[0]);

        if(return_status == SSP_SUCCESS)
        {
	    DEBUG_PRINT(DEBUG_TRACE,"\n wifi_getFTR1KeyHolderID returned success");
            sprintf(detailsAdd, "FTR1 Key Holder ID Details -");
            strcat(details, detailsAdd);

            if(keyId[0] == '\0')
            {
                sprintf(detailsAdd, " Key Holder ID[0] : 0x%x", keyId[0]);
                strcat(details, detailsAdd);
            }
            else
            {
                for(int index = 0; index < 64 && keyId[index] != '\0' ; index++)
                {
                    sprintf(detailsAdd, " Key Holder ID[%d] : 0x%x", index, keyId[index]);
                    strcat(details, detailsAdd);
                }
            }

            DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
            response["result"]="SUCCESS";
            response["details"]=details;
        }
        else
        {
            sprintf(details, "wifi_%s operation failed", methodName);
            DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
            response["result"]="FAILURE";
            response["details"]=details;
            DEBUG_PRINT(DEBUG_TRACE,"\n WiFiCallMethodForGetOrSetFTR1KeyHolderID --->Error in execution\n");
        }
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetOrSetFTR1KeyHolderID ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_SetBSSColor
 * Description          : This function invokes WiFi hal's wifi_setBSSColor() api
 * @param [in] req-     : radioIndex - radio index value of wifi
 *                        color - color value to be set
 * @param [out] response - filled with SUCCESS or FAILURE based on the output staus of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_SetBSSColor(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetBSSColor --->Entry\n");
    int radioIndex = 0;
    unsigned char color = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    char detailsAdd[1000] = {'\0'};

    if(&req["radioIndex"]==NULL || &req["color"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["radioIndex"].asInt();
    color = req["color"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n radioIndex : %d, color : %d", radioIndex, color);
    #if defined BCM_COMMON_WIFIHAL
    wifi_api_info_t apiInfo;

    printf("is sock api\n");
    strncpy(apiInfo.api_name, "wifi_setBSSColor", 1024);
    snprintf (apiInfo.api_data, sizeof(apiInfo.api_data), "%d", color);
    apiInfo.radioIndex = radioIndex;
    return_status = wifi_api_send_msg(&apiInfo);
    #else
    return_status = wifi_setBSSColor(radioIndex, color);
    #endif

    if(return_status == SSP_SUCCESS)
    {
        sprintf(detailsAdd, "wifi_setBSSColor operation success;");
        DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
        strcat(details, detailsAdd);

        return_status = ssp_WIFIHALApplySettings(radioIndex, (char *)"setBSSColor");

        if(return_status == SSP_SUCCESS)
        {
            sprintf(detailsAdd, " applyRadioSettings operation success");
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            strcat(details, detailsAdd);
            response["result"]="SUCCESS";
        }
        else
        {
            sprintf(detailsAdd, " applyRadioSettings operation failed");
            DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            strcat(details, detailsAdd);
            response["result"]="FAILURE";
        }

        response["details"]=details;
    }
    else
    {
        sprintf(details, "WIFIHAL_SetBSSColor operation failed");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetBSSColor --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_SetBSSColor ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_PushApFastTransitionConfig
 * Description          : This function invokes WiFi hal's Push FT API
 * @param [in] req-     : apIndex - Access Point index
 *                        radioIndex - WiFi Radio Index
 *                        support - FT support(Disabled/Full/Adaptive)
 *                        mobilityDomain - Value of the FT Mobility Domain for this AP to set
 *                        overDS - FT Over DS activated(Enabled/Disabled)
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_PushApFastTransitionConfig(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApFastTransitionConfig  ----->Entry\n");
    int apIndex = 0;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    wifi_FastTransitionConfig_t ftCfg;
    char detailsAdd[200] = {'\0'};
    char details[200] = {'\0'};

    if(&req["apIndex"]==NULL || &req["support"]==NULL || &req["mobilityDomain"]==NULL || &req["overDS"]==NULL || &req["radioIndex"]==NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n apIndex : %d", apIndex);

    ftCfg.support = (wifi_fastTrasitionSupport_t)req["support"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n FT Support : %d", ftCfg.support);

    ftCfg.mobilityDomain = req["mobilityDomain"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Mobility Domain ID : 0x%04x", ftCfg.mobilityDomain);

    ftCfg.overDS = req["overDS"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n FT Over DS : %d", ftCfg.overDS);

    radioIndex = req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n radioIndex : %d", radioIndex);

    return_status = wifi_pushApFastTransitionConfig(apIndex, &ftCfg);

    if(return_status == SSP_SUCCESS)
    {
        sprintf(detailsAdd, "wifi_PushApFastTransitionConfig operation success;");
        strcat(details, detailsAdd);
        return_status = ssp_WIFIHALApplySettings(radioIndex, (char *)"PushApFastTransitionConfig");

        if(return_status == SSP_SUCCESS)
        {
            sprintf(detailsAdd, " applyRadioSettings operation success");
            strcat(details, detailsAdd);
	    DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            response["result"]="SUCCESS";
        }
        else
        {
            sprintf(detailsAdd, " applyRadioSettings operation failed");
            strcat(details, detailsAdd);
	    DEBUG_PRINT(DEBUG_TRACE,"\n%s", detailsAdd);
            response["result"]="FAILURE";
        }

        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_PushApFastTransitionConfig operation failed");
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApFastTransitionConfig --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_PushApFastTransitionConfig ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetMuEdca
 * Description          : This function invokes WiFi hal get api wifi_getMuEdca()
 * @param [in] req-     : radioIndex - radio index
 * @param [in] req-     : accessCategory - Access Category for MU (Multi-User) EDCA
 *                        (Enhanced Distributed Channel Access) includes background, best effort,
 *                        video, voice
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetMuEdca(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetMuEdca ----->Entry\n");
    wifi_edca_t edca;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    wifi_access_category_t accessCategory = wifi_access_category_background;
    char details[2000] = {'\0'};

    if (&req["radioIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Radio Index : %d", radioIndex);

    accessCategory = (wifi_access_category_t)req["accessCategory"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Access Category : %d", accessCategory);

    return_status = wifi_getMuEdca(radioIndex, accessCategory, &edca);

    if(return_status == SSP_SUCCESS)
    {
        sprintf(details, "wifi_getMuEdca invoked successfully; Details : MuEdca for Access Category = %d : aifsn=%d, cw_min=%d, cw_max=%d, timer=%d", accessCategory, edca.aifsn, edca.cw_min, edca.cw_max, edca.timer);
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getMuEdca not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetMuEdca  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetMuEdca ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRadioOperatingParameters
 * Description          : This function invokes WiFi hal get api wifi_getRadioOperatingParameters()
 * @param [in] req-     : radioIndex - radio index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioOperatingParameters(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioOperatingParameters ----->Entry\n");
    wifi_radio_operationParam_t operationParams;
    int radioIndex = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};
    char output[2000] = {'\0'};
    int rates = 0;
    int bands = 0;
    int iteration = 0;
    int chanWidth = 0;
    int variant = 0;

    if (&req["radioIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = (wifi_radio_index_t)req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Radio Index : %d", radioIndex);

    return_status = wifi_getRadioOperatingParameters(radioIndex, &operationParams);

    if(return_status == SSP_SUCCESS)
    {
        printf("Radio Enable: %d\n", operationParams.enable);
        printf("AutoChannel Enabled: %d\n", operationParams.autoChannelEnabled);
        printf("Channel: %d\n", operationParams.channel);
        printf("CSA Beacon Count: %d\n", operationParams.csa_beacon_count);
        printf("DCS Enabled: %d\n", operationParams.DCSEnabled);
        printf("DTIM Period: %d\n", operationParams.dtimPeriod);
        printf("Beacon Interval: %d\n", operationParams.beaconInterval);
        printf("Operating Class: %d\n", operationParams.operatingClass);
        printf("Fragmentation Threshold: %d\n", operationParams.fragmentationThreshold);
        printf("Guard Interval: %d\n", operationParams.guardInterval);
        printf("Transmit Power: %d\n", operationParams.transmitPower);
        printf("RTS Threshold: %d\n", operationParams.rtsThreshold);
        printf("Radio Country Code: 0x%04x\n", operationParams.countryCode);
        printf("Number of Secondary Channels: %d\n", operationParams.numSecondaryChannels);

        sprintf(details, "wifi_getRadioOperatingParameters invoked successfully; Details : ");
        sprintf(output, "Radio Enable: %d, AutoChannel Enabled: %d, Channel: %d, CSA Beacon Count: %d, DCS Enabled: %d, DTIM Period: %d, Beacon Interval: %d, Operating Class: %d, Fragmentation Threshold: %d, Guard Interval: %d, Transmit Power: %d, RTS Threshold: %d, Radio Country Code : 0x%04x, Number of Secondary Channels: %d,", operationParams.enable,operationParams.autoChannelEnabled, operationParams.channel, operationParams.csa_beacon_count, operationParams.DCSEnabled,operationParams.dtimPeriod, operationParams.beaconInterval, operationParams.operatingClass, operationParams.fragmentationThreshold,operationParams.guardInterval, operationParams.transmitPower, operationParams.rtsThreshold, operationParams.countryCode, operationParams.numSecondaryChannels);
        strcat(details, output);

        printf("Secondary Channels - \n");
        sprintf(output, " Channel Secondary: ");
        strcat(details, output);
        for (iteration = 0; iteration < operationParams.numSecondaryChannels; iteration++)
        {
            printf("channelSecondary[%d]: %d ", iteration, operationParams.channelSecondary[iteration]);
            sprintf(output, " %d", operationParams.channelSecondary[iteration]);
            strcat(details, output);
        }
        if(operationParams.numSecondaryChannels == 0)
        {
            printf("None\n");
            sprintf(output, "None");
            strcat(details, output);
        }

        printf("\nBands: 0x%04x", operationParams.band);
        sprintf(output, ", Bands: 0x%04x", operationParams.band);
        strcat(details, output);
        for(bands = WIFI_FREQUENCY_2_4_BAND; bands <= WIFI_FREQUENCY_60_BAND; bands = bands * 2)
        {
            if (operationParams.band & bands)
            {
                printf("0x%04x ", bands);
                sprintf(output, " 0x%04x", bands);
		strcat(details, output);
            }
        }

        printf("\nChannel Width: 0x%04x", operationParams.channelWidth);
        sprintf(output, ", Channel Width: 0x%04x", operationParams.channelWidth);
	strcat(details, output);
        for(chanWidth = WIFI_CHANNELBANDWIDTH_20MHZ; chanWidth <= WIFI_CHANNELBANDWIDTH_80_80MHZ; chanWidth = chanWidth * 2)
        {
            if (operationParams.channelWidth & chanWidth)
            {
                printf("0x%04x ", chanWidth);
                sprintf(output, " 0x%04x", chanWidth);
		strcat(details, output);
            }
        }

        printf("\n80211 Variants: 0x%04x \n", operationParams.variant);
        sprintf(output, ", 80211 Variants: 0x%04x", operationParams.variant);
	strcat(details, output);
        for(variant = WIFI_80211_VARIANT_A; variant <= WIFI_80211_VARIANT_AX; variant = variant * 2)
        {
            if (operationParams.variant & variant)
            {
                printf("0x%04x ", variant);
                sprintf(output, " 0x%04x", variant);
		strcat(details, output);
            }
        }

        printf("\nBasic Data Transmit Rates: 0x%04x", operationParams.basicDataTransmitRates);
        sprintf(output, ", Basic Data Transmit Rates: 0x%04x", operationParams.basicDataTransmitRates);
	strcat(details, output);
        for(rates = WIFI_BITRATE_DEFAULT; rates <= WIFI_BITRATE_54MBPS; rates = rates * 2)
        {
            if (operationParams.basicDataTransmitRates & rates)
            {
                printf("0x%04x ", rates);
                sprintf(output, " 0x%04x", rates);
                strcat(details, output);
            }
        }

        printf("\nOperational Data Transmit Rates: 0x%04x", operationParams.operationalDataTransmitRates);
        sprintf(output, ", Operational Data Transmit Rates: 0x%04x", operationParams.operationalDataTransmitRates);
	strcat(details, output);
        for(rates = WIFI_BITRATE_DEFAULT; rates <= WIFI_BITRATE_54MBPS; rates = rates * 2)
        {
            if (operationParams.operationalDataTransmitRates & rates)
            {
                printf("0x%04x ", rates);
                sprintf(output, " 0x%04x", rates);
		strcat(details, output);
            }
        }

        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getRadioOperatingParameters not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioOperatingParameters  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioOperatingParameters ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetRadioChannels
 * Description          : This function invokes WiFi hal get api wifi_getRadioChannels()
 * @param [in] req-     : radioIndex - radio index
 * @param [in] req-     : numberOfChannels - Number of channels available for each radio
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetRadioChannels(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioChannels ----->Entry\n");
    int numChAll = 165;
    wifi_channelMap_t radioChannels[165], *chan = NULL;
    memset(&radioChannels, 0, sizeof(radioChannels));
    int radioIndex = 0;
    int numberOfChannels = 0;
    int return_status = SSP_FAILURE;
    char details[4000] = {'\0'};
    char output[4000] = {'\0'};
    int channel = 0;

    if (&req["radioIndex"] == NULL || &req["numberOfChannels"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    radioIndex = req["radioIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Radio Index : %d", radioIndex);

    numberOfChannels = req["numberOfChannels"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n Number of channels : %d", numberOfChannels);

    return_status = wifi_getRadioChannels(radioIndex, radioChannels, numChAll);

    if(return_status == SSP_SUCCESS)
    {
        printf("ssp_WIFIHALGetRadioChannels Success");
        sprintf(details, "wifi_getRadioChannels invoked successfully; Details : ");
        sprintf(output, "Channel Details -- ");
        strcat(details, output);

        for(channel = 0; channel < numberOfChannels; channel++)
        {
            chan = &radioChannels[channel];
            printf("\nChannel %d : State %d", chan->ch_number, chan->ch_state);
            sprintf(output, "Channel %d : State %d ", chan->ch_number, chan->ch_state);
            strcat(details, output);
        }

        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getRadioChannels not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioChannels  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetRadioChannels ---->Exiting\n");
    return;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetEAPParam
 * Description          : This function invokes WiFi hal get api wifi_getEAP_Param()
 * @param [in] req-     : apIndex - Access Point index
 * @param [out] response - filled with SUCCESS or FAILURE based on the output status of operation
 *
 ********************************************************************************************/
void WIFIHAL::WIFIHAL_GetEAPParam(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetEAPParam ----->Entry\n");
    wifi_eap_config_t eapConfig;
    memset(&eapConfig, 0, sizeof(eapConfig));
    int apIndex = 0;
    int return_status = SSP_FAILURE;
    char details[2000] = {'\0'};

    if (&req["apIndex"] == NULL)
    {
        response["result"]="FAILURE";
        response["details"]="NULL parameter as input argument";
        return;
    }

    apIndex = req["apIndex"].asInt();
    DEBUG_PRINT(DEBUG_TRACE,"\n ApIndex : %d", apIndex);

    return_status = wifi_getEAP_Param(apIndex, &eapConfig);

    if(return_status == SSP_SUCCESS)
    {
        printf("ssp_WIFIHALGetEAPParam Success :: EAP Congiguration -- ");
        printf("EAPOL Key Timeout: %u\n", eapConfig.uiEAPOLKeyTimeout);
        printf("EAPOL Key Retries: %u\n", eapConfig.uiEAPOLKeyRetries);
        printf("EAP Identity Request Timeout: %u\n", eapConfig.uiEAPIdentityRequestTimeout);
        printf("EAP Identity Request Retries: %u\n", eapConfig.uiEAPIdentityRequestRetries);
        printf("EAP Request Timeout: %u\n", eapConfig.uiEAPRequestTimeout);
        printf("EAP Request Retries: %u\n", eapConfig.uiEAPRequestRetries);

        sprintf(details, "wifi_getEAP_Param invoked successfully; Details : EAP Congiguration -- EAPOL Key Timeout: %u, EAPOL Key Retries: %u, EAP Identity Request Timeout: %u, EAP Identity Request Retries: %u, EAP Request Timeout: %u, EAP Request Retries: %u", eapConfig.uiEAPOLKeyTimeout, eapConfig.uiEAPOLKeyRetries, eapConfig.uiEAPIdentityRequestTimeout, eapConfig.uiEAPIdentityRequestRetries, eapConfig.uiEAPRequestTimeout, eapConfig.uiEAPRequestRetries);

        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="SUCCESS";
        response["details"]=details;
    }
    else
    {
        sprintf(details, "wifi_getEAP_Param not invoked successfully");
        DEBUG_PRINT(DEBUG_TRACE,"\n %s", details);
        response["result"]="FAILURE";
        response["details"]=details;
        DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetEAPParam  --->Error in execution\n");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n WIFIHAL_GetEAPParam ---->Exiting\n");
    return;
}

/**************************************************************************
 * Function Name        : CreateObject
 * Description  : This function will be used to create a new object for the
 *                class "WIFIHAL".
*
 **************************************************************************/
extern "C" WIFIHAL* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new WIFIHAL(ptrtcpServer);
}

/**************************************************************************
 * Function Name : cleanup
 * Description   : This function will be used to clean the log details.
 *
 **************************************************************************/
bool WIFIHAL::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_LOG,"WIFIHAL shutting down\n");
    return TEST_SUCCESS;
}

/**************************************************************************
 * Function Name : DestroyObject
 * Description   : This function will be used to destroy the object.
 *
 **************************************************************************/
extern "C" void DestroyObject(WIFIHAL *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG,"Destroying WIFIHAL object\n");
    delete stubobj;
}

