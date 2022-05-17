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
#include "ssp_tdk_WiFi_wrp.h"


/*******************************************************************************************
 *
 * Function Name        : ssp_wifi_init
 * Description          : This function invokes WiFi hal's init api *
 * @param [in]  N/A
 * @param [out] N/A
 ********************************************************************************************/
int ssp_wifi_init()
{
    printf("\n ssp_wifi_init-----> Entry\n");

    int return_status=0;
#if defined(_COSA_BCM_MIPS_)
    printf("Invoking wifi_init HAL API\n");

    return_status = wifi_init();

    printf("return value from wifi_init is %d\n",return_status);

    if(return_status == SSP_SUCCESS)
    {
         printf("\nssp_wifi_init::WIFI HAL Initialization success\n");
    }
    else
    {
        printf("\nssp_wifi_init::Failed to initialize the WIFI HAL\n");
    }
#endif
    printf("\n ssp_wifi_init----> Exit\n");

    return return_status;
}

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
    int return_status = 0;


    #if defined (_XB7_PRODUCT_REQ_) && defined (_COSA_BCM_ARM_)
        return_status =  wifi_apply(radioIndex);
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
    int return_status = 0;

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
    else if(!strcmp(method, "setRadioDFSEnable"))
        return_status = wifi_setRadioDfsEnable(radioIndex, *enable);
    else if(!strcmp(method, "getAutoChannelRefreshPeriodSupported"))
        return_status = wifi_getRadioAutoChannelRefreshPeriodSupported(radioIndex, enable);
    else if(!strcmp(method, "setAutoChannelEnable"))
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
    else if(!strcmp(method, "getAtmBandEnable"))
    {
        if(enable)
           return_status = wifi_getAtmBandEnable(radioIndex, enable);
        else
            return_status = wifi_getAtmBandEnable(radioIndex, NULL);
    }
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
    int return_status = 0;

    if(!strcmp(method, "getRadioChannel"))
        return_status = wifi_getRadioChannel(radioIndex, uLongVar);
    else if(!strcmp(method, "setRadioChannel"))
        return_status = wifi_setRadioChannel(radioIndex, *uLongVar);
    else if(!strcmp(method, "getAutoChannelRefreshPeriod"))
        return_status = wifi_getRadioAutoChannelRefreshPeriod(radioIndex, uLongVar);
    else if(!strcmp(method, "setAutoChannelRefreshPeriod"))
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
    int return_status = 0;
    wifi_device_t dev;
    memset(&dev, 0, sizeof(wifi_device_t));
    char mac[64] = {'\0'};
    char *token = NULL;
    int count = 0;

    if(!strcmp(method, "getRadioChannelsInUse"))
        return_status = wifi_getRadioChannelsInUse(radioIndex, output);
    else if(!strcmp(method, "getRadioPossibleChannels"))
        return_status = wifi_getRadioPossibleChannels(radioIndex, output);
    else if(!strcmp(method, "getChannelBandwidth"))
        return_status = wifi_getRadioOperatingChannelBandwidth(radioIndex, output);
    else if(!strcmp(method, "setChannelBandwidth"))
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
 * Function Name        : ssp_WiFiHalCallMethodForRadioStandard
 * Description          : This function invokes WiFi hal's get/set apis, when the value to be
                          get /set is a radio standard
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : gOnly,nOnly,acOnly - the values to be get/set
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetRadioStandard(int radioIndex, char* output, char* method, unsigned char *gOnly, unsigned char *nOnly, unsigned char *acOnly)
{
    printf("\n ssp_WIFIHALGetOrSetParamStringValue----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    printf("GetorSetParam: %s\n" , output);
    printf("MethodName: %s\n", method);
    printf("gOnly: %d\n",*gOnly);
    printf("nOnly: %d\n",*nOnly);
    printf("acOnly: %d\n",*acOnly);

    int return_status = 0;

    if(!strcmp(method, "getRadioStandard"))
        return_status = wifi_getRadioStandard(radioIndex, output, gOnly, nOnly, acOnly);
    else if(!strcmp(method, "setRadioChannelMode"))
        return_status = wifi_setRadioChannelMode(radioIndex, output, *gOnly, *nOnly, *acOnly);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForRadioStandard: Invalid methodName\n");
    }

    printf("ssp_WiFiHalCallMethodForRadioStandard: return value is %s %d %d %d\n", output, *gOnly, *nOnly, *acOnly);
    printf("\n ssp_WiFiHalCallMethodForRadioStandard--> Exit\n");
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
    int return_status = 0;


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
    else if(!strcmp(method, "setApSecurityReset"))
        return_status = wifi_setApSecurityReset(radioIndex);
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
            return_status = wifi_getDownlinkMuType(radioIndex, (void *)output);
        else
            return_status = wifi_getDownlinkMuType(radioIndex, NULL);
    }
    else if(!strcmp(method, "getUplinkMuType"))
    {
        if(output)
            return_status = wifi_getUplinkMuType(radioIndex, (void *)output);
        else
            return_status = wifi_getUplinkMuType(radioIndex, NULL);
    }
    else if(!strcmp(method, "getGuardInterval"))
    {
        if(output)
            return_status = wifi_getGuardInterval(radioIndex, (void *)output);
        else
            return_status = wifi_getGuardInterval(radioIndex, NULL);
    }
    else if(!strcmp(method, "setDownlinkMuType"))
          return_status = wifi_setDownlinkMuType(radioIndex, *output);
    else if(!strcmp(method, "setUplinkMuType"))
          return_status = wifi_setUplinkMuType(radioIndex, *output);
    else if(!strcmp(method, "setGuardInterval"))
          return_status = wifi_setGuardInterval(radioIndex, *output);
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
    int return_status = 0;

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
    else if(!strcmp(method, "getAtmBandMode"))
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
    }
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


/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetIndexFromName
 * Description          : This function invokes WiFi hal api wifi_getIndexFromName()

 * @param [in]          : param     - the ssid name to be passed
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALGetIndexFromName(char* ssidName, int *output)
{
    printf("\n ssp_WIFIHALGetIndexFromName ----> Entry\n");
    printf("ssidName: %s\n", ssidName);
    int return_status = 0;

    return_status = wifi_getIndexFromName(ssidName, output);
    printf("return value from ssp_WIFIHALGetIndexFromName is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetIndexFromName::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALGetIndexFromName::Success\n");
    }
    printf("\n ssp_WIFIHALGetIndexFromName ----> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_ClearRadioResetCount
 * Description          : This function invokes WiFi hal api wifi_clearRadioResetCount()

 * @param [in]          : NIL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALClearRadioResetCount()
{
    printf("\n ssp_WIFIHALClearRadioResetCount ----> Entry\n");
    int return_status = 0;

    return_status = wifi_clearRadioResetCount();
    printf("return value from ssp_WIFIHALClearRadioResetCount is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALClearRadioResetCount::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALClearRadioResetCount::Success\n");
    }
    printf("\n ssp_WIFIHALClearRadioResetCount ----> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_Reset
 * Description          : This function invokes WiFi hal api wifi_reset()

 * @param [in]          : NIL
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALReset()
{
    printf("\n ssp_WIFIHALReset ----> Entry\n");
    int return_status = 0;

    return_status = wifi_reset();
    printf("return value from ssp_WIFIHALReset is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALReset::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALReset::Success\n");
    }
    printf("\n ssp_WIFIHALReset ----> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetOrSetSecurityRadiusServer
 * Description          : This function invokes WiFi hal's get/set api's which are
                          related to SecurityRadiusServer
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [in]          : IPAddress - IP Address of the RADIUS server used for WLAN security
 * @param [in]          : port - port  number of the RADIUS server used for WLAN security
 * @param [in]          : RadiusSecret - RadiusSecret of the RADIUS server used for WLAN security
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetSecurityRadiusServer(int radioIndex, char* IPAddress, unsigned int* port, char* RadiusSecret, char* method)
{
    printf("\n ssp_WIFIHALGetOrSetSecurityRadiusServer ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    printf("IPAddress : %s\n",IPAddress);
    printf("Port : %u\n" ,*port);
    printf("RadiusSecret : %s\n",RadiusSecret);
    printf("MethodName: %s\n", method);
    int return_status = 0;

    if(!strcmp(method, "getApSecurityRadiusServer"))
        return_status = wifi_getApSecurityRadiusServer(radioIndex, IPAddress, port, RadiusSecret);
    else if(!strcmp(method, "setApSecurityRadiusServer"))
        return_status = wifi_setApSecurityRadiusServer(radioIndex, IPAddress, *port, RadiusSecret);
    else if(!strcmp(method, "getApSecuritySecondaryRadiusServer"))
        return_status = wifi_getApSecuritySecondaryRadiusServer(radioIndex, IPAddress, port, RadiusSecret);
    else if(!strcmp(method, "setApSecuritySecondaryRadiusServer"))
        return_status = wifi_setApSecuritySecondaryRadiusServer(radioIndex, IPAddress, *port, RadiusSecret);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForSecurityRadiusServer: Invalid methodName\n");
    }
    printf("\n ssp_WiFiHalCallMethodForSecurityRadiusServer--> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHAL_GetOrSetApBridgeInfo
 * Description          : This function invokes WiFi hal's get/set api's which are
                          related to ApBridgeInfo
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [in]          : bridgeName
 * @param [in]          : IP
 * @param [in]          : subnet
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetApBridgeInfo(int radioIndex, char* bridgeName, char* IP, char* subnet, char* method)
{
    printf("\n ssp_WIFIHALGetOrSetApBridgeInfo ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    printf("IPAddress : %s\n",IP);
    printf("bridgeName : %s\n" ,bridgeName);
    printf("subnet : %s\n",subnet);
    printf("MethodName: %s\n", method);
    int return_status = 0;

    if(!strcmp(method, "getApBridgeInfo"))
        return_status = wifi_getApBridgeInfo(radioIndex, bridgeName, IP, subnet);
    else if(!strcmp(method, "setApBridgeInfo"))
        return_status = wifi_setApBridgeInfo(radioIndex, bridgeName, IP, subnet);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForApBridgeInfo: Invalid methodName\n");
    }
    printf("\n ssp_WiFiHalCallMethodForApBridgeInfo--> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHAL_GetOrSetRadioDCSScanTime
 * Description          : This function invokes WiFi hal's get/set api's which are
                          related to RadioDCSScanTime
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [in]          : output_interval_seconds
 * @param [in]          : output_dwell_milliseconds
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetRadioDCSScanTime(int radioIndex, int* output_interval_seconds, int* output_dwell_milliseconds,char* method)
{
    printf("\n ssp_WIFIHALGetOrSetRadioDCSScanTime----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    printf("output_interval_seconds : %d\n", *output_interval_seconds);
    printf("output_dwell_milliseconds : %d\n", *output_dwell_milliseconds);
    printf("MethodName: %s\n", method);
    int return_status = 0;

    if(!strcmp(method, "getRadioDCSScanTime"))
        return_status = wifi_getRadioDCSScanTime(radioIndex, output_interval_seconds, output_dwell_milliseconds);
    else if(!strcmp(method, "setRadioDCSScanTime"))
        return_status = wifi_setRadioDCSScanTime(radioIndex, *output_interval_seconds, *output_dwell_milliseconds);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForRadioDCSScanTime: Invalid methodName\n");
    }
    printf("\n ssp_WiFiHalCallMethodForRadioDCSScanTime--> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHAL_AddorDelApAclDevice
 * Description          : This function invokes WiFi hal's add/delete apis, when the value to be
                          added/deleted is related to ApAclDevice
 *
 * @param [in]          : apIndex - WiFi ap index value
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [in]          : DeviceMacAddress - MacAddress of the device to be added/deleted
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALAddorDelApAclDevice(int apIndex, char* DeviceMacAddress, char* method)
{
    printf("\n ssp_WIFIHALAddorDelApAclDevice ----> Entry\n");
    printf("ap index:%d\n",apIndex);
    printf("DeviceMacAddress : %s\n",DeviceMacAddress);
    printf("MethodName: %s\n", method);
    int return_status = 0;

    if(!strcmp(method, "addApAclDevice"))
        return_status = wifi_addApAclDevice(apIndex, DeviceMacAddress);
    else if(!strcmp(method, "delApAclDevice"))
        return_status = wifi_delApAclDevice(apIndex, DeviceMacAddress);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForAddorDelApAclDevice: Invalid methodName\n");
    }
    printf("\n ssp_WiFiHalCallMethodForAddorDelApAclDevice--> Exit\n");
    return return_status;
}
/*******************************************************************************************
*
 * Function Name        : ssp_WIFIHAL_IfConfigUporDown
 * Description          : This function invokes WiFi hal api's wifi_ifConfigDown() or wifi_ifConfigUp()
 *
 * @param [in]          : apIndex - WiFi ap index value
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALIfConfigUporDown(int apIndex, char* method)
{
    printf("\n ssp_WIFIHALIfConfigUporDown ----> Entry\n");
    printf("ap index:%d\n",apIndex);
    printf("MethodName: %s\n", method);
    int return_status = 0;

    if(!strcmp(method, "ifConfigUp"))
        return_status = wifi_ifConfigUp(apIndex);
    else if(!strcmp(method, "ifConfigDown"))
        return_status = wifi_ifConfigDown(apIndex);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForIfConfigUporDown: Invalid methodName\n");
    }
    printf("\n ssp_WiFiHalCallMethodForIfConfigUporDown ---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHAL_ParamradioIndex
 * Description          : This function invokes WiFi hal api's which require radioIndex as input
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALParamRadioIndex(int radioIndex, char* method)
{
    printf("\n ssp_WIFIHALParamRadioIndex ----> Entry\n");
    printf("radio index:%d\n",radioIndex);
    printf("MethodName: %s\n", method);
    int return_status = 0;
    if(!strcmp(method, "cancelApWPS"))
        return_status = wifi_cancelApWPS(radioIndex);
    else if(!strcmp(method, "setApSecurityReset"))
        return_status = wifi_setApSecurityReset(radioIndex);
    else if(!strcmp(method, "resetApVlanCfg"))
	return_status = wifi_resetApVlanCfg(radioIndex);
    else if(!strcmp(method,"disableApEncryption"))
	return_status = wifi_disableApEncryption(radioIndex);
    else if(!strcmp(method,"removeApSecVaribles"))
	return_status = wifi_removeApSecVaribles(radioIndex);
    else if(!strcmp(method, "initRadio"))
        return_status = wifi_initRadio(radioIndex);
    else if(!strcmp(method, "factoryResetRadio"))
        return_status = wifi_factoryResetRadio(radioIndex);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForParamRadioIndex: Invalid methodName\n");
    }
    printf("\n ssp_WiFiHalCallMethodForParamRadioIndex ---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHAL_StartorStopHostApd
 * Description          : This function invokes WiFi hal api's wifi_startHostApd() and wifi_stopHostApd()
 *
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALStartorStopHostApd(char* method)
{
    printf("\n ssp_WIFIHALStartorStopHostApd ----> Entry\n");
    printf("MethodName: %s\n", method);
    int return_status = 0;
    if(!strcmp(method, "startHostApd"))
        return_status = wifi_startHostApd();
    else if(!strcmp(method, "stopHostApd"))
        return_status = wifi_stopHostApd();
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForStartorStopHostApd: Invalid methodName\n");
    }
    printf("\n ssp_WiFiHalCallMethodForStartorStopHostApd ---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHAL_FactoryReset
 * Description          : This function invokes WiFi hal api's wifi_factoryResetRadios() and wifi_factoryReset()
 *
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALFactoryReset(char* method)
{
    printf("\n ssp_WIFIHALFactoryReset ----> Entry\n");
    printf("MethodName: %s\n", method);
    int return_status = 0;
    if(!strcmp(method, "factoryReset"))
        return_status = wifi_factoryReset();
    else if(!strcmp(method, "factoryResetRadios"))
        return_status = wifi_factoryResetRadios();
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForFactoryReset: Invalid methodName\n");
    }
    printf("\n ssp_WiFiHalCallMethodForFactoryReset ---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetOrSetSecurityRadiusSettings
 * Description          : This function invokes WiFi hal's get/set api's which are
                          related to SecurityRadiusSettings
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [in]          : wifi_radius_setting_t - structure with radius settings parameters
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetSecurityRadiusSettings(int radioIndex,  wifi_radius_setting_t *radiusSetting, char* method)
{
    printf("\n ssp_WIFIHALGetOrSetSecurityRadiusSettings ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    printf("MethodName: %s\n", method);
    int return_status = 0;

    if(!strcmp(method, "getApSecurityRadiusSettings"))
        return_status = wifi_getApSecurityRadiusSettings(radioIndex, radiusSetting);
    else if(!strcmp(method, "setApSecurityRadiusSettings"))
        return_status = wifi_setApSecurityRadiusSettings(radioIndex, radiusSetting);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForSecurityRadiusSettings: Invalid methodName\n");
    }
    printf("\n ssp_WiFiHalCallMethodForSecurityRadiusSettings---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetSSIDTrafficStats2
 * Description          : This function invokes WiFi HAL api wifi_getSSIDTrafficStats2
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : wifi_ssidTrafficStats2_t- structure with ssid traffic static info
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetSSIDTrafficStats2(int radioIndex,  wifi_ssidTrafficStats2_t *ssidTrafficStats2)
{
    printf("\n ssp_WIFIHALGetSSIDTrafficStats2 ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    int return_status = 0;

    return_status = wifi_getSSIDTrafficStats2(radioIndex, ssidTrafficStats2);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetSSIDTrafficStats2::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALGetSSIDTrafficStats2::Success\n");
    }
    printf("\n ssp_WIFIHALGetSSIDTrafficStats2 ---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetRadioTrafficStats2
 * Description          : This function invokes WiFi hal's get api's which are
                          related to GetRadioTrafficStats2
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [in]          : wifi_radioTrafficStats2_t - structure with radio stat Measure parameters
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetRadioTrafficStats2(int radioIndex,  wifi_radioTrafficStats2_t *TrafficStats2)
{
    printf("\n ssp_WIFIHALGetRadioTrafficStats2 ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    int return_status = 0;

    return_status = wifi_getRadioTrafficStats2(radioIndex, TrafficStats2);
    printf("return value from ssp_WIFIHALGetRadioTrafficStats2 is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetRadioTrafficStats2::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALGetRadioTrafficStats2::Success\n");
    }
    printf("\n ssp_WiFiHalCallMethodForGetRadioTrafficStats2---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult
 * Description          : This function invokes WiFi HAL api wifi_getApAssociatedDeviceDiagnosticResult
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : associated_dev - double pointer to a structure of type wifi_associated_dev_t
 * @param [in]          : output_array_size - pointer to a variable storing the number of access points identified
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult(int radioIndex, wifi_associated_dev_t **associated_dev, unsigned int *output_array_size)
{
    printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    int return_status = 0;
    return_status = wifi_getApAssociatedDeviceDiagnosticResult(radioIndex, associated_dev, output_array_size);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetApAssociatedDeviceDiagnosticResult::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult::Success\n");
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult ---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_Down
 * Description          : This function invokes WiFi hal api wifi_down()

 * @param [in]          : NIL
 * @param [out]         : return status as integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALDown()
{
    printf("\n ssp_WIFIHALDown ----> Entry\n");
    int return_status = 0;

    return_status = wifi_down();
    printf("return value from ssp_WIFIHALDown is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALDown::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALDown::Success\n");
    }
    printf("\n ssp_WIFIHALDown ----> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALCreateInitialConfigFiles
 * Description          : This function invokes WiFi hal api wifi_createInitialConfigFiles()

 * @param [in]          : NIL
 * @param [out]         : return status as integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALCreateInitialConfigFiles()
{
    printf("\n ssp_WIFIHALCreateInitialConfigFiles ----> Entry\n");
    int return_status = 0;

    return_status = wifi_createInitialConfigFiles();
    printf("return value from ssp_WIFIHALCreateInitialConfigFiles is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALCreateInitialConfigFiles::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALCreateInitialConfigFiles::Success\n");
    }
    printf("\n ssp_WIFIHALCreateInitialConfigFiles ----> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetNeighboringWiFiDiagnosticResult2
 * Description          : This function invokes WiFi HAL api wifi_getNeighboringWiFiDiagnosticResult2
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : neighbor_ap2 - double pointer to a structure of type wifi_neighbor_ap2_t
 * @param [in]          : output_array_size - pointer to a variable storing the number of access points identified
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetNeighboringWiFiDiagnosticResult2(int radioIndex, wifi_neighbor_ap2_t **neighbor_ap2, unsigned int *output_array_size)
{
    printf("\n ssp_WIFIHALGetNeighboringWiFiDiagnosticResult2 ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    int return_status = 0;

    return_status = wifi_getNeighboringWiFiDiagnosticResult2(radioIndex, neighbor_ap2, output_array_size);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetNeighboringWiFiDiagnosticResult2::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetNeighboringWiFiDiagnosticResult2::Success\n");
    }
    printf("\n ssp_WIFIHALGetNeighboringWiFiDiagnosticResult2 ---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetNeighboringWiFiStatus
 * Description          : This function invokes WiFi HAL api wifi_getNeighboringWiFiStatus
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : neighbor_ap2 - double pointer to a structure of type wifi_neighbor_ap2_t
 * @param [in]          : output_array_size - pointer to a variable storing the number of access points identified
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetNeighboringWiFiStatus(int radioIndex, wifi_neighbor_ap2_t **neighbor_ap2, unsigned int *output_array_size)
{
    printf("\n ssp_WIFIHALGetNeighboringWiFiStatus ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    int return_status = 0;

    return_status = wifi_getNeighboringWiFiStatus(radioIndex, neighbor_ap2, output_array_size);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetNeighboringWiFiStatus::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetNeighboringWiFiStatus::Success\n");
    }
    printf("\n ssp_WIFIHALGetNeighboringWiFiStatus ---> Exit\n");
    return return_status;
}
/********************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetBSSColorValue
 * Description          : This function invokes WiFi hal's wifi_getBSSColor() api
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [out]         : color - color value returned by the HAL api
                          return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetBSSColorValue(int radioIndex, unsigned char *color)
{
    printf("\n ssp_WIFIHALGetBSSColorValue----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    int return_status = 0;

    if(color)
    {
        return_status = wifi_getBSSColor(radioIndex, color);
    }
    else
    {
        printf("Validation with NULL buffer\n");
        return_status = wifi_getBSSColor(radioIndex, NULL);
    }
    if(color)
        printf("ssp_WIFIHALGetBSSColorValue: return value is %d\n", *color);
    if(return_status != SSP_SUCCESS)
        printf("\nssp_WIFIHALGetBSSColorValue::Failed\n");
    else
        printf("\nssp_WIFIHALGetBSSColorValue::Success\n");
    printf("ssp_WIFIHALGetBSSColorValue: ret:status %d\n", return_status);
    printf("\n ssp_WIFIHALGetBSSColorValue--> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALApplyGASConfiguration
 * Description          : This function invokes WiFi hal api wifi_applyGASConfiguration
 * @param [in]          : wifi_GASConfiguration_t - structure with GAS configuration parameters
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALApplyGASConfiguration(wifi_GASConfiguration_t *GASConfiguration)
{
    printf("\n ssp_WIFIHALapplyGASConfiguration ----> Entry\n");
    int return_status = 0;
    return_status = wifi_applyGASConfiguration(GASConfiguration);
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALApplyGASConfiguration::Failed\n");
    }
    else
    {
        printf("\nssp_WIFIHALApplyGASConfiguration::Success\n");
    }
    printf("\n ssp_WIFIHALapplyGASConfiguration ---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALPushRadioChannel2
 * Description          : This function invokes WiFi HAL api wifi_pushRadioChannel2()
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : channel - net channel
 * @param [in]          : channel_width_MHz - channel frequency
 * @param [in]          : csa_beacon_count - Specifies how long CSA need to be announced
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALPushRadioChannel2(int radioIndex, unsigned int channel,unsigned int channel_width_MHz,unsigned int csa_beacon_count)
{
    printf("\n ssp_WIFIHALPushRadioChannel2 ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    int return_status = 0;

    return_status = wifi_pushRadioChannel2(radioIndex, channel, channel_width_MHz, csa_beacon_count);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALPushRadioChannel2::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALPushRadioChannel2::Success\n");
    }
    printf("\n ssp_WIFIHALPushRadioChannel2 ---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetRadioChannelStats
 * Description          : This function invokes WiFi hal's api wifi_getRadioChannelStats()
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : wifi_radioTrafficStats2_t - structure with radio stat Measure parameters
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetRadioChannelStats(int radioIndex,  wifi_channelStats_t *channelStats, int array_size)
{
    printf("\n ssp_WIFIHALGetRadioChannelStats ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    int return_status = 0;

    return_status = wifi_getRadioChannelStats(radioIndex, channelStats, array_size);
    printf("return value from ssp_WIFIHALGetRadioChannelStats is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetRadioChannelStats::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALGetRadioChannelStats::Success\n");
    }
    printf("\n ssp_WiFiHalCallMethodForGetRadioChannelStats---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHAL_ParamApIndex
 * Description          : This function invokes WiFi hal api's which require ApIndex as input
 *
 * @param [in]          : radioIndex - WiFi ap index value
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALParamApIndex(int apIndex, char* method)
{
    printf("\n ssp_WIFIHALParamApIndex ----> Entry\n");
    printf("ap index:%d\n",apIndex);
    printf("MethodName: %s\n", method);
    int return_status = 0;
    if(!strcmp(method, "deleteAp"))
        return_status = wifi_deleteAp(apIndex);
    else if(!strcmp(method, "factoryResetAP"))
        return_status = wifi_factoryResetAP(apIndex);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForParamApIndex: Invalid methodName\n");
    }
    printf("\n ssp_WiFiHalCallMethodForParamApIndex ---> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetApAssociatedDevice
 * Description          : This function invokes WiFi HAL api wifi_getApAssociatedDeviceDiagnosticResult
 *
 * @param [in]          : ap_index - WiFi radio index value
 * @param [in]          : associated_dev - List of devices associated with ap
 * @param [in]          : output_array_size - pointer to a variable storing the number of access points identified
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetApAssociatedDevice(int apIndex, char* associated_dev , unsigned int output_array_size)
{
    printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult ----> Entry\n");
    printf("ap index:%d\n",apIndex);
    int return_status = 0;
    return_status = wifi_getApAssociatedDevice(apIndex, associated_dev, output_array_size);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetApAssociatedDevice::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDevice::Success\n");
    }
    printf("\n ssp_WIFIHALGetApAssociatedDevice ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetApDeviceRSSI
 * Description          : This function invokes WiFi hal api wifi_getApDeviceRSSI
 * @param [in]          : apIndex          Access Point index
 * @param [in]          : MAC          Client MAC in upcase format
 * @param [in]          : output_RSSI  RSSI is in dbm
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALGetApDeviceRSSI(int ap_index, char *MAC, int *output_RSSI, char* method)
{
    printf("\n ssp_WIFIHALGetApDeviceRSSI ----> Entry\n");
    printf("ap index:%d\n",ap_index);
    printf("DeviceMacAddress : %s\n",MAC);
    printf("MethodName: %s\n", method);
    int return_status = 0;
    printf("return value from ssp_WIFIHALGetApDeviceRSSI is %d\n",return_status);
    if(!strcmp(method, "getApDeviceRSSI"))
        return_status = wifi_getApDeviceRSSI(ap_index, MAC, output_RSSI);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WIFIHALGetApDeviceRSSI: Invalid methodName\n");
    }
    printf("\n ssp_WIFIHALGetApDeviceRSSI--> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHAL_DelApAclDevices
 * Description          : This function invokes WiFi hal's delete apis ApAclDevices
 *
 * @param [in]          : apIndex - WiFi ap index value
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALDelApAclDevices(int apIndex)
{
    printf("\n ssp_WIFIHALDelApAclDevices ----> Entry\n");
    printf("ap index:%d\n",apIndex);
    int return_status = 0;
    return_status = wifi_delApAclDevices(apIndex);
    if(return_status == SSP_SUCCESS)
    {
        printf("\n ssp_WIFIHALDelApAclDevices function call is success");
    }
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForAddorDelApAclDevice failed");
    }
    printf("\n ssp_WiFiHalCallMethodForAddorDelApAclDevice--> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetApAclDevices
 * Description          : This function invokes WiFi HAL api wifi_getApAclDevices
 *
 * @param [in]          : apIndex - WiFi ap index value
 * @param [in]          : mac_array - string array of mac address
 * @param [in]          : output_array_size - pointer to a variable storing the number of devices identified
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetApAclDevices(int apIndex, char* mac_addr, unsigned int output_array_size)
{
    printf("\n ssp_WIFIHALGetApAclDevices ----> Entry\n");
    printf("Ap index:%d\n",apIndex);
    int return_status = 0;
    return_status = wifi_getApAclDevices(apIndex, mac_addr, output_array_size);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetApAclDevices::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAclDevices::Success\n");
    }
    printf("\n ssp_WIFIHALGetApAclDevices ---> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetApDeviceTxRxRate
 * Description          : This function invokes WiFi hal apis
 * @param [in]          : apIndex          Access Point index
 * @param [in]          : MAC          Client MAC in upcase format
 * @param [in]          : output_TxRxMb is in mbps
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALGetApDeviceTxRxRate(int apIndex, char *MAC, int *output_TxRxMb, char* method)
{
    printf("\n ssp_WIFIHALGetApDeviceTxRxRate ----> Entry\n");
    printf("ap index:%d\n",apIndex);
    printf("DeviceMacAddress : %s\n",MAC);
    printf("MethodName: %s\n", method);
    int return_status = 0;
    if(!strcmp(method, "getApDeviceRxrate"))
        return_status = wifi_getApDeviceRxrate(apIndex, MAC, output_TxRxMb);
    else if(!strcmp(method, "getApDeviceTxrate"))
        return_status = wifi_getApDeviceTxrate(apIndex, MAC, output_TxRxMb);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WIFIHALGetApDeviceTxRxRate: Invalid methodName\n");
    }

    printf("return value from ssp_WIFIHALGetApDeviceTxRxRate is %d\n",return_status);
    printf("\n ssp_WIFIHALGetApDeviceTxRxRate--> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetRadioChannelStats2
 * Description          : This function invokes WiFi hal's api wifi_getRadioChannelStats2()
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : wifi_radioTrafficStats2_t - structure with radio stat Measure parameters
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetRadioChannelStats2(int radioIndex, wifi_channelStats2_t *outputChannelStats2)
{
    printf("\n ssp_WIFIHALGetRadioChannelStats2 ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    int return_status = 0;

    return_status = wifi_getRadioChannelStats2(radioIndex, outputChannelStats2);
    printf("return value from ssp_WIFIHALGetRadioChannelStats2 is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
        printf("\n ssp_WIFIHALGetRadioChannelStats2::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\n ssp_WIFIHALGetRadioChannelStats2::Success\n");
    }
    printf("\n ssp_WIFIHALGetRadioChannelStats2---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHAL_CreateAp
 * Description          : This function invokes WiFi hal's api wifi_createAp
 * @param [in]          : apIndex      - Access Point index
 * @param [in]          : radioIndex  Radio index
 * @param [in]          : essid       SSID Name
 * @param [in]          : hideSsid    True/False, to SSID advertisement enable value
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHAL_CreateAp(int apIndex, int radioIndex, char *essid, unsigned char hideSsid)
{
    printf("\n ssp_WIFIHAL_CreateAp----> Entry\n");
    printf("Ap Index:%d\n",apIndex);
    printf("radioIndex:%d\n",radioIndex);
    printf("hideSsid: %d\n", hideSsid);
    printf("essid : %s\n", essid);
    int return_status = 0;
    return_status = wifi_createAp(apIndex, radioIndex, essid, hideSsid);
    printf("\n ssp_WIFIHAL_CreateAp--> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult3
 * Description          : This function invokes WiFi HAL api wifi_getApAssociatedDeviceDiagnosticResult3
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : associated_dev - double pointer to a structure of type wifi_associated_dev_t
 * @param [in]          : output_array_size - pointer to a variable storing the number of access points identified
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult3(int apIndex, wifi_associated_dev3_t **associated_dev_array, unsigned int *output_array_size)
{
    printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult3 ----> Entry\n");
    printf("ap index:%d\n",apIndex);
    int return_status = 0;
    return_status = wifi_getApAssociatedDeviceDiagnosticResult3(apIndex, associated_dev_array, output_array_size);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetApAssociatedDeviceDiagnosticResult3::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult3::Success\n");
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult3 ---> Exit\n");
    return return_status;
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
int ssp_WIFIHALGetApAssociatedDeviceStats(int apIndex, mac_address_t *clientMacAddress, wifi_associated_dev_stats_t *associated_dev_stats, unsigned long long *handle)
{
    printf("\n ssp_WIFIHALGetApAssociatedDeviceStats ----> Entry\n");
    printf("ap index:%d\n",apIndex);
    printf("MAC:%s\n",(char*)clientMacAddress);
    int return_status = 0;
    return_status = wifi_getApAssociatedDeviceStats(apIndex, clientMacAddress, associated_dev_stats, handle);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetApAssociatedDeviceStats::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceStats::Success\n");
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceStats ---> Exit\n");
    return return_status;
}

/*************************************************************************************************
 *
 * Function Name        : ssp_WIFIHAL_SetApScanFilter
 * Description          : This function invokes WiFi hal's set api which is related to ApScanFilter
 *
 * @param [in]          : apIndex - WiFi Ap index value
 * @param [in]          : mode
 * @param [in]          : essid
 * @param [in]          : method     - name of the wifi hal api to be invoked
 * @param [out]         : return status an integer value 0-success and 1-Failure
 * **************************************************************************************************/
int ssp_WIFIHALSetApScanFilter(int apIndex, int mode, char* essid, char *method)
{
    printf("\n ssp_WIFIHALSetApScanFilter ----> Entry\n");
    printf("Ap index:%d\n",apIndex);
    printf("Mode : %d\n",mode);
    printf("essid : %s\n" ,essid);
    printf("MethodName: %s\n", method);
    int return_status = 0;
    if(!strcmp(method, "setApScanFilter"))
        return_status = wifi_setApScanFilter(apIndex, mode, essid);
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForApSacnFilter: Invalid methodName\n");
    }
    printf("\n ssp_WiFiHalCallMethodForApSacnFilter--> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetApAssociatedDeviceTxStatsResult
 * Description          : This function invokes WiFi HAL api wifi_getApAssociatedDeviceTxStatsResult
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : MAC - MAC address of the device
 * @param [out]         : associated_dev - double pointer to a structure of type wifi_associated_dev_rate_info_tx_stats_t
 * @param [out]         : output_array_size - pointer to a variable storing the number of access points identified
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetApAssociatedDeviceTxStatsResult(int radioIndex, mac_address_t *clientMacAddress, wifi_associated_dev_rate_info_tx_stats_t **stats_array, unsigned int *output_array_size, unsigned long long *handle)
{
    printf("\n ssp_WIFIHALGetApAssociatedDeviceTxStatsResult ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    printf("MAC:%02x:%02x:%02x:%02x:%02x:%02x\n",(*clientMacAddress)[0],(*clientMacAddress)[1],(*clientMacAddress)[2],(*clientMacAddress)[3],(*clientMacAddress)[4],(*clientMacAddress)[5]);
//     printf("MAC:%s\n",clientMacAddress);
    int return_status = 0;
    return_status = wifi_getApAssociatedDeviceTxStatsResult(radioIndex, clientMacAddress, stats_array, output_array_size, handle);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetApAssociatedDeviceTxStatsResult::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceTxStatsResult::Success\n");
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceTxStatsResult ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetApAssociatedDeviceRxStatsResult
 * Description          : This function invokes WiFi HAL api wifi_getApAssociatedDeviceRxStatsResult
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : MAC - MAC address of the device
 * @param [out]         : associated_dev - double pointer to a structure of type wifi_associated_dev_rate_info_rx_stats_t
 * @param [out]         : output_array_size - pointer to a variable storing the number of access points identified
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetApAssociatedDeviceRxStatsResult(int radioIndex, mac_address_t *clientMacAddress, wifi_associated_dev_rate_info_rx_stats_t **stats_array, unsigned int *output_array_size, unsigned long long *handle)
{
    printf("\n ssp_WIFIHALGetApAssociatedDeviceRxStatsResult ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
       printf("MAC:%02x:%02x:%02x:%02x:%02x:%02x\n",(*clientMacAddress)[0],(*clientMacAddress)[1],(*clientMacAddress)[2],(*clientMacAddress)[3],(*clientMacAddress)[4],(*clientMacAddress)[5]);
    int return_status = 0;
    return_status = wifi_getApAssociatedDeviceRxStatsResult(radioIndex, clientMacAddress, stats_array, output_array_size, handle);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetApAssociatedDeviceRxStatsResult::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceRxStatsResult::Success\n");
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceRxStatsResult ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALStartNeighborScan
 * Description          : This function invokes WiFi hal's get/set api's which are
                          related to RadioDCSScanTime
 *
 * @param [in]          : apIndex - The index of access point array.
 * @param [in]          : scan_mode    - Scan modes
 * @param [in]          : dwell_time - Amount of time spent on each channel in the hopping sequence.
 * @param [in]          : chan_num - The channel number.
 * @param [in]          : chan_list - List of channels.
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALStartNeighborScan(int apIndex, wifi_neighborScanMode_t scan_mode, int dwell_time, unsigned int chan_num, unsigned int* chan_list)
{
    printf("\n ssp_WIFIHALStartNeighborScan----> Entry\n");
    printf("Ap Index:%d\n",apIndex);
    int return_status = 0;
    return_status = wifi_startNeighborScan(apIndex, scan_mode, dwell_time, chan_num, chan_list);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n::ssp_WIFIHALStartNeighborScan Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALStartNeighborScan::Success\n");
    }
    printf("\n ssp_WIFIHALGetNeighboringWiFiStatus ---> Exit\n");
    return return_status;
}
/*******************************************************************************************
 *
 * Function Name        :ssp_WIFIHALGetApAssociatedDeviceTidStatsResult
 * Description          : This function invokes WiFi HAL api wifi_getApAssociatedDeviceTidStatsResult
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : MAC - MAC address of the device
 * @param [out]         : associated_dev - double pointer to a structure of type wifi_associated_dev_rate_info_tx_stats_t
 * @param [out]         : handle - pointer to a variable storing the number of access points identified
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetApAssociatedDeviceTidStatsResult(int radioIndex,  mac_address_t *clientMacAddress, wifi_associated_dev_tid_stats_t *tid_stats,  unsigned long long *handle)
{
    printf("\n ssp_WIFIHALGetApAssociatedDeviceTidStatsResult ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    printf("MAC:%02x:%02x:%02x:%02x:%02x:%02x\n",(*clientMacAddress)[0],(*clientMacAddress)[1],(*clientMacAddress)[2],(*clientMacAddress)[3],(*clientMacAddress)[4],(*clientMacAddress)[5]);
    int return_status = 0;
    return_status = wifi_getApAssociatedDeviceTidStatsResult(radioIndex, clientMacAddress, tid_stats, handle);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetApAssociatedDeviceTidStatsResult::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceTidStatsResult::Success\n");
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceTidStatsResult ---> Exit\n");
    return return_status;
}




/*******************************************************************************************
 *
 * Function Name                  ssp_WIFIHALGetBandSteeringLog
 * Description                    This function invokes WiFi HAL api wifi_getBandSteeringLog
 * @param[in]  record_index       Record index
 * @param[out] pSteeringTime      Returns the UTC time in seconds
 * @param[in]  pClientMAC         pClientMAC is pre allocated as 64bytes
 * @param[in]  pSourceSSIDIndex   Source SSID index
 * @param[in]  pDestSSIDIndex     Destination SSID index
 * @param[out] pSteeringReason    Returns the predefined steering trigger reas
 ********************************************************************************************/
int ssp_WIFIHALGetBandSteeringLog(int record_index, unsigned long *pSteeringTime, char *pClientMAC, int *pSourceSSIDIndex, int *pDestSSIDIndex, int *pSteeringReason)
{
    printf("\n ssp_WIFIHALGetBandSteeringLog ----> Entry\n");
    printf("record index:%d\n",record_index);
    printf ("pClientMAC : %s\n", pClientMAC);
    int return_status = 0;
    return_status = wifi_getBandSteeringLog(record_index, pSteeringTime, pClientMAC,pSourceSSIDIndex,pDestSSIDIndex,pSteeringReason);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetBandSteeringLog::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetBandSteeringLog::Success\n");
    }
    printf("\n ssp_WIFIHALGetBandSteeringLog ---> Exit\n");
    return return_status;
}




/*******************************************************************************************
 *
 * Function Name                    :ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult2
 * Description                      : This function invokes WiFi HAL api wifi_getApAssociatedDeviceDiagnosticResult2
 *
 * @param[in] apIndex               : Access Point index
 * @param[out] dev_cnt               : Array size, to be returned
 * @param[out] associated_dev_array  : pointer to structure

 ********************************************************************************************/
int ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult2(int apIndex, wifi_associated_dev2_t **associated_dev_array, unsigned int *dev_cnt)
{
    printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult2 ----> Entry\n");
    printf("radio index:%d\n",apIndex);
    int return_status = 0;
    return_status = wifi_getApAssociatedDeviceDiagnosticResult2(apIndex,associated_dev_array,dev_cnt);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult2::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult2\n");
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult2 ---> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name                    : ssp_WIFIHALGetRadioMode
 * Description                      : This function invokes WiFi HAL api wifi_getRadioMode
 *
 * @param[in] radioIndex            : radio Index value
              output_string         : operation mode value

 * @param[out] return status        : WiFi HAL operation Success / Failure
 ********************************************************************************************/
int ssp_WIFIHALGetRadioMode(int radioIndex, char* output_string, unsigned int *puremode)
{
    printf("\n ssp_WIFIHALGetRadioMode ----> Entry\n");
    printf("radio index:%d\n",radioIndex);
    int return_status = 0;

    return_status = wifi_getRadioMode(radioIndex, output_string, puremode);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_WIFIHALGetRadioMode::Failed\n");
    }
    else
    {
     printf("\n ssp_WIFIHALGetRadioMode Success\n");
    }
    printf("\n ssp_WIFIHALGetRadioMode ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name                    : ssp_WIFIHALSetRadioMode
 * Description                      : This function invokes WiFi HAL api wifi_setRadioMode
 *
 * @param[in] radioIndex            : radio Index value
              output_string         : operation mode value
              puremode              : operational standard value

 * @param[out] return status        : WiFi HAL operation Success / Failure
 ********************************************************************************************/
int ssp_WIFIHALSetRadioMode(int radioIndex, char* output_string, unsigned int puremode)
{
    printf("\n ssp_WIFIHALSetRadioMode ----> Entry\n");
    printf("radio index:%d\n",radioIndex);
    int return_status = 0;

    return_status = wifi_setRadioMode(radioIndex, output_string, puremode);
    if(return_status != SSP_SUCCESS)
    {
     printf("\n ssp_WIFIHALSetRadioMode::Failed\n");
    }
    else
    {
     printf("\n ssp_WIFIHALSetRadioMode success\n");

    }
    printf("\n ssp_WIFIHALSetRadioMode ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : WIFIHAL_GetApIndexFromName
 * Description          : This function invokes WiFi hal api wifi_getApIndexFromName()
 * @param [in]          : param     - the ssid name to be passed
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALGetApIndexFromName(char* ssidName, int *output)
{
    printf("\n ssp_WIFIHALGetApIndexFromName ----> Entry\n");
    printf("ssidName: %s\n", ssidName);
    int return_status = 0;
    return_status = wifi_getApIndexFromName(ssidName, output);
    printf("return value from ssp_WIFIHALGetApIndexFromName is %d\n",return_status);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetApIndexFromName::Failed\n");
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALGetApIndexFromName::Success\n");
    }
    printf("\n ssp_WIFIHALGetApIndexFromName ----> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetAssociatedDeviceDetail
 * Description          : This function invokes WiFi hal api wifi_getAssociatedDeviceDetail()
 * @param [in]          : apIndex   - accesspoint index
                          devIndex - associated device index
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALGetAssociatedDeviceDetail(int apIndex, int devIndex, wifi_device_t *dev)
{
    printf("\n ssp_WIFIHALGetAssociatedDeviceDetail ----> Entry\n");
    printf("ap index:%d devIndex:%d \n",apIndex, devIndex);

    int return_status = 0;
    return_status = wifi_getAssociatedDeviceDetail(apIndex, devIndex, dev);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetAssociatedDeviceDetail::Failed. Ret:status %d\n", return_status);
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetAssociatedDeviceDetail::Success. Ret:status %d\n", return_status);
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceDetail ---> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetBasicTrafficStats
 * Description          : This function invokes WiFi hal api wifi_getBasicTrafficStats()
 * @param [in]          : apIndex   - accesspoint index
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALGetBasicTrafficStats(int apIndex, wifi_basicTrafficStats_t *output_struct)
{
    printf("\n ssp_WIFIHALGetBasicTrafficStats ----> Entry\n");
    printf("ap index:%d \n",apIndex);

    int return_status = 0;
    return_status = wifi_getBasicTrafficStats(apIndex, output_struct);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetBasicTrafficStats::Failed. Ret:status %d\n", return_status);
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetBasicTrafficStats::Success. Ret:status %d\n", return_status);
    }
    printf("\n ssp_WIFIHALGetBasicTrafficStats ---> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetWifiTrafficStats
 * Description          : This function invokes WiFi hal api wifi_getWifiTrafficStats()
 * @param [in]          : apIndex   - accesspoint index
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALGetWifiTrafficStats(int apIndex, wifi_trafficStats_t *output_struct)
{
    printf("\n ssp_WIFIHALGetWifiTrafficStats ----> Entry\n");
    printf("ap index:%d \n",apIndex);

    int return_status = 0;
    return_status = wifi_getWifiTrafficStats(apIndex, output_struct);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetWifiTrafficStats::Failed. Ret:status %d\n", return_status);
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetWifiTrafficStats::Success. Ret:status %d\n", return_status);
    }
    printf("\n ssp_WIFIHALGetWifiTrafficStats ---> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALSteeringClientDisconnect
 * Description          : This function invokes WiFi hal api wifi_steering_clientDisconnect()
 * @param [in]          : steeringgroupIndex - Wifi Steering Group index
			  apIndex   - accesspoint index
                          client_mac - The Client's MAC address
                          type - Disconnect Type
                          reason - Reason code to provide in deauth/disassoc frame
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALSteeringClientDisconnect(unsigned int steeringgroupIndex, int apIndex, mac_address_t client_mac, wifi_disconnectType_t type, unsigned int reason)
{
    printf("\n ssp_WIFIHALSteeringClientDisconnect ----> Entry\n");
    printf("ap index:%d \n",apIndex);

    int return_status = 0;
    return_status = wifi_steering_clientDisconnect(steeringgroupIndex, apIndex, client_mac, type, reason);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALSteeringClientDisconnect::Failed. Ret:status %d\n", return_status);
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALSteeringClientDisconnect::Success. Ret:status %d\n", return_status);
    }
    printf("\n ssp_WIFIHALSteeringClientDisconnect ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALSteeringClientDisconnect
 * Description          : This function invokes WiFi hal api wifi_steering_clientDisconnect()
 * @param [in]          : steeringgroupIndex - Wifi Steering Group index
                          apIndex   - accesspoint index
                          client_mac - The Client's MAC address
                          wifi_steering_clientConfig_t - Steering client config
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALSteeringClientSet(unsigned int steeringgroupIndex, int apIndex, mac_address_t client_mac, wifi_steering_clientConfig_t *cli_cfg)
{
    printf("\n ssp_WIFIHALSteeringClientSet ----> Entry\n");
    printf("ap index:%d \n",apIndex);

    int return_status = 0;
    return_status = wifi_steering_clientSet(steeringgroupIndex, apIndex, client_mac, cli_cfg);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALSteeringClientSet::Failed. Ret:status %d\n", return_status);
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALSteeringClientSet::Success. Ret:status %d\n", return_status);
    }
    printf("\n ssp_WIFIHALSteeringClientSet ---> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALSteeringClientRemove
 * Description          : This function invokes WiFi hal api wifi_steering_clientRemove()
 * @param [in]          : steeringgroupIndex - Wifi Steering Group index
                          apIndex   - accesspoint index
                          client_mac - The Client's MAC address
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALSteeringClientRemove(unsigned int steeringgroupIndex, int apIndex, mac_address_t client_mac)
{
    printf("\n ssp_WIFIHALSteeringClientRemove ----> Entry\n");
    printf("ap index:%d \n",apIndex);

    int return_status = 0;
    return_status = wifi_steering_clientRemove(steeringgroupIndex, apIndex, client_mac);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALSteeringClientRemove::Failed. Ret:status %d\n", return_status);
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALSteeringClientRemove::Success. Ret:status %d\n", return_status);
    }
    printf("\n ssp_WIFIHALSteeringClientRemove ---> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetBTMClientCapabilityList
 * Description          : This function invokes WiFi hal api wifi_getBTMClientCapabilityList()
 * @param [in]          : apIndex   - accesspoint index
                          btm_caps  - buffer to returm client capability
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALGetBTMClientCapabilityList(int apIndex, wifi_BTMCapabilities_t* btm_caps)
{
    printf("\n ssp_WIFIHALGetBTMClientCapabilityList ----> Entry\n");
    printf("ap index:%d \n",apIndex);

    int return_status = 0;
    return_status = wifi_getBTMClientCapabilityList(apIndex, btm_caps);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetBTMClientCapabilityList::Failed. Ret:status %d\n", return_status);
     return_status = SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetBTMClientCapabilityList::Success. Ret:status %d\n", return_status);
    }
    printf("\n ssp_WIFIHALGetBTMClientCapabilityList ---> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetApRoamingConsortiumElement
 * Description          : This function invokes WiFi hal api wifi_getApRoamingConsortiumElement()
 * @param [in]          : apIndex   - accesspoint index
                          roam  - buffer to returm ApRoamingConsortiumElement
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALGetApRoamingConsortiumElement(int apIndex, wifi_roamingConsortiumElement_t* roam)
{
    printf("\n ssp_WIFIHALGetApRoamingConsortiumElement ----> Entry\n");
    printf("ap index:%d \n",apIndex);

    int return_status = 0;
    return_status = wifi_getApRoamingConsortiumElement(apIndex, roam);
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetApRoamingConsortiumElement::Failed. Ret:status %d\n", return_status);
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\n ssp_WIFIHALGetApRoamingConsortiumElement::Success. Ret:status %d\n", return_status);
    }
    printf("\n ssp_WIFIHALGetApRoamingConsortiumElement ----> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALPushApRoamingConsortiumElement
 * Description          : This function invokes WiFi hal api wifi_pushApRoamingConsortiumElement()
 * @param [in]          : apIndex   - accesspoint index
                          roam  - ApRoamingConsortiumElement values to be pushed
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALPushApRoamingConsortiumElement(int apIndex, wifi_roamingConsortiumElement_t* roam)
{
    printf("\n ssp_WIFIHALPushApRoamingConsortiumElement ----> Entry\n");
    printf("ap index:%d \n",apIndex);

    int return_status = 0;
    return_status = wifi_pushApRoamingConsortiumElement(apIndex, roam);
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALPushApRoamingConsortiumElement::Failed. Ret:status %d\n", return_status);
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\n ssp_WIFIHALPushApRoamingConsortiumElement::Success. Ret:status %d\n", return_status);
    }
    printf("\n ssp_WIFIHALPushApRoamingConsortiumElement ----> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetApInterworkingElement
 * Description          : This function invokes WiFi HAL api wifi_getApInterworkingElement
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : wifi_InterworkingElement_t- structure with element info
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetApInterworkingElement(int radioIndex, wifi_InterworkingElement_t *element)
{
    printf("\n ssp_WIFIHALGetApInterworkingElement ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    int return_status = 0;
    return_status = wifi_getApInterworkingElement(radioIndex, element);
    if(return_status != SSP_SUCCESS)
    {
         printf("\nssp_WIFIHALGetApInterworkingElement::Failed\n");
         return_status = SSP_FAILURE;
    }
    else
    {
         printf("\nssp_WIFIHALGetApInterworkingElement::Success\n");
    }
    printf("\n ssp_WIFIHALGetApInterworkingElement ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALPushApInterworkingElement
 * Description          : This function invokes WiFi HAL api wifi_pushApInterworkingElement
 *
 * @param [in]          : radioIndex - WiFi radio index value
 * @param [in]          : wifi_InterworkingElement_t- structure with element info
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALPushApInterworkingElement(int radioIndex, wifi_InterworkingElement_t *element)
{
    printf("\n ssp_WIFIHALPushApInterworkingElement ----> Entry\n");
    printf("Radio index:%d\n",radioIndex);
    int return_status = 0;
    return_status = wifi_pushApInterworkingElement(radioIndex, element);
    if(return_status != SSP_SUCCESS)
    {
         printf("\nssp_WIFIHALPushApInterworkingElement::Failed\n");
         return_status = SSP_FAILURE;
    }
    else
    {
         printf("\nssp_WIFIHALPushApInterworkingElement::Success\n");
    }
    printf("\n ssp_WIFIHALPushApInterworkingElement ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALEnableCSIEngine
 * Description          : This function invokes WiFi HAL api wifi_enableCSIEngine
 *
 * @param [in]          : apIndex - WiFi Access Point Index value
                          sta - Mac Address of client device connected
                          enable - Whether CSI data collection is enabled or not
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALEnableCSIEngine(int apIndex, mac_address_t sta, unsigned char * enable)
{
    printf("\n ssp_WIFIHALEnableCSIEngine ----> Entry\n");
    printf("apIndex:%d\n",apIndex);
    printf("sta:%s\n",sta);
    printf("enable:%d\n",*enable);
    int return_status = 0;
    return_status = wifi_enableCSIEngine(apIndex, sta, *enable);

    if(return_status != SSP_SUCCESS)
    {
         printf("\nssp_WIFIHALEnableCSIEngine::Failed\n");
         return_status = SSP_FAILURE;
    }
    else
    {
         printf("\nssp_WIFIHALEnableCSIEngine::Success\n");
    }

    printf("\n ssp_WIFIHALEnableCSIEngine ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALSendDataFrame
 * Description          : This function invokes WiFi HAL api wifi_sendDataFrame
 *
 * @param [in]          : apIndex - Index of VAP
 *                        sta - MAC address of the station associated in this VAP
 *                        data - Pointer to the data buffer. The data does not have any layer 2 information but starts with layer 3.
 *                        length - length of data
 *                        insert_llc - whether LLC header should be inserted. If set to TRUE, HAL implementation MUST insert the following bytes before type field. DSAP =  0xaa, SSAP = 0xaa, Control = 0x03, followed by 3 bytes each = 0x00
 *                        protocol - ethernet protocol
 *                        priority - priority of the frame with which scheduler should transmit the frame
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALSendDataFrame(int apIndex, mac_address_t sta, unsigned char * data, unsigned int length, unsigned char * insert_llc, unsigned int protocol, wifi_data_priority_t prio)
{
    printf("\n ssp_WIFIHALSendDataFrame ----> Entry\n");
    printf("apIndex:%d\n",apIndex);
    printf("sta:%s\n",sta);
    printf("length:%d\n",length);
    printf("insert_llc:%d\n",*insert_llc);
    printf("protocol:%d\n",protocol);
    printf("priority:%d\n",prio);
    int return_status = 0;
    return_status = wifi_sendDataFrame(apIndex, sta, data, length, *insert_llc, protocol, prio);

    if(return_status != SSP_SUCCESS)
    {
         printf("\nssp_WIFIHALSendDataFrame::Failed\n");
         return_status = SSP_FAILURE;
    }
    else
    {
         printf("\nssp_WIFIHALSendDataFrame::Success\n");
    }

    printf("\n ssp_WIFIHALSendDataFrame ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALGetVAPTelemetry
 * Description          : This function invokes WiFi HAL api wifi_getVAPTelemetry
 * @param [in]          : apIndex - WiFi Access Point Index
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetVAPTelemetry(int apIndex, wifi_VAPTelemetry_t *VAPTelemetry)
{
    printf("\n ssp_WIFIHALGetVAPTelemetry ----> Entry\n");
    printf("apIndex:%d\n", apIndex);
    int return_status = 0;
    return_status = wifi_getVAPTelemetry(apIndex, VAPTelemetry);

    if(return_status != SSP_SUCCESS)
    {
         printf("\nssp_WIFIHALGetVAPTelemetry::Failed\n");
         return_status = SSP_FAILURE;
    }
    else
    {
         printf("\nssp_WIFIHALGetVAPTelemetry::Success; Tx Overflow : %d\n", VAPTelemetry->txOverflow);
    }

    printf("\n ssp_WIFIHALGetVAPTelemetry ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetRadioVapInfoMap
 * Description          : This function invokes WiFi hal api wifi_getRadioVapInfoMap()
 * @param [out]         : return status an integer value 0-success and 1-Failure
 *
 ********************************************************************************************/
int ssp_WIFIHALGetRadioVapInfoMap(wifi_radio_index_t radioIndex ,wifi_vap_info_map_t *map)
{
    printf("\n ssp_WIFIHALGetRadioVapInfoMap ----> Entry\n");

    int return_status = 0;
    return_status = wifi_getRadioVapInfoMap(radioIndex,map);
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetRadioVapInfoMap::Failed. Ret:status %d\n", return_status);
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\n sssp_WIFIHALGetRadioVapInfoMap::Success. Ret:status %d\n", return_status);
    }

    printf("\n ssp_WIFIHALGetRadioVapInfoMap ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALSetNeighborReports
 * Description          : This function invokes WiFi HAL api wifi_setNeighborReports
 * @param [in]          : apIndex - Index of VAP
 *                        reports - Number of reports
 *                        neighborReports - structure with Neighbor report details
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALSetNeighborReports(unsigned int apIndex, unsigned int reports, wifi_NeighborReport_t *neighborReports)
{
    printf("\n ssp_WIFIHALSetNeighborReports ----> Entry\n");
    printf("apIndex : %d\n", apIndex);
    printf("reports : %d\n", reports);
    printf("bssid : %s\n", neighborReports->bssid);
    printf("info : %d\n", neighborReports->info);
    printf("opClass : %d\n", neighborReports->opClass);
    printf("channel : %d\n", neighborReports->channel);
    printf("phyTable : %d\n", neighborReports->phyTable);
    int return_status = 0;
    return_status = wifi_setNeighborReports(apIndex, reports, neighborReports);

    if(return_status != SSP_SUCCESS)
    {
         printf("\nssp_WIFIHALSetNeighborReports::Failed\n");
         return_status = SSP_FAILURE;
    }
    else
    {
         printf("\nssp_WIFIHALSetNeighborReports::Success\n");
    }

    printf("\n ssp_WIFIHALSetNeighborReports ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetApAssociatedClientDiagnosticResult
 * Description          : This function invokes WiFi HAL api wifi_getApAssociatedClientDiagnosticResult
 * @param [in]          : apIndex - Index of VAP
 *                        mac_addr - MAC address of the client
 *                        dev_conn - structure with Client Diagnostic result
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetApAssociatedClientDiagnosticResult(int apIndex, char * mac_addr, wifi_associated_dev3_t *dev_conn)
{
    printf("\n ssp_WIFIHALGetApAssociatedClientDiagnosticResult ----> Entry\n");
    printf("apIndex : %d\n", apIndex);
    printf("mac : %s\n", mac_addr);
    int return_status = 0;

    return_status = wifi_getApAssociatedClientDiagnosticResult(apIndex, mac_addr, dev_conn);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nWIFIHALGetApAssociatedClientDiagnosticResult::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nWIFIHALGetApAssociatedClientDiagnosticResult::Success\n");
        printf("\nClient Diagnostic Result : MAC=%02x:%02x:%02x:%02x:%02x:%02x, IP=%s, AuthState=%d, LastDataDownlinkRate=%u, LastDataUplinkRate=%u, SignalStrength=%d, Retransmissions=%u, Active=%d, OperatingStd= %s, OperatingChBw=%s, SNR=%d, interferenceSources=%s, DataFramesSentAck=%lu, cli_DataFramesSentNoAck=%lu, cli_BytesSent=%lu, cli_BytesReceived=%lu, cli_RSSI=%d, cli_MinRSSI=%d, cli_MaxRSSI=%d, Disassociations=%u, AuthFailures=%u, cli_Associations=%llu, PacketsSent=%lu, PacketsReceived=%lu, ErrorsSent=%lu, RetransCount=%lu, FailedRetransCount=%lu, RetryCount=%lu, MultipleRetryCount=%lu, MaxDownlinkRate=%u, MaxUplinkRate=%u\n", dev_conn->cli_MACAddress[0], dev_conn->cli_MACAddress[1], dev_conn->cli_MACAddress[2], dev_conn->cli_MACAddress[3], dev_conn->cli_MACAddress[4], dev_conn->cli_MACAddress[5], dev_conn->cli_IPAddress, dev_conn->cli_AuthenticationState, dev_conn->cli_LastDataDownlinkRate, dev_conn->cli_LastDataUplinkRate, dev_conn->cli_SignalStrength, dev_conn->cli_Retransmissions, dev_conn->cli_Active, dev_conn->cli_OperatingStandard, dev_conn->cli_OperatingChannelBandwidth, dev_conn->cli_SNR, dev_conn->cli_InterferenceSources, dev_conn->cli_DataFramesSentAck, dev_conn->cli_DataFramesSentNoAck, dev_conn->cli_BytesSent, dev_conn->cli_BytesReceived, dev_conn->cli_RSSI, dev_conn->cli_MinRSSI, dev_conn->cli_MaxRSSI, dev_conn->cli_Disassociations, dev_conn->cli_AuthenticationFailures, dev_conn->cli_Associations, dev_conn->cli_PacketsSent, dev_conn->cli_PacketsReceived, dev_conn->cli_ErrorsSent, dev_conn->cli_RetransCount, dev_conn->cli_FailedRetransCount, dev_conn->cli_RetryCount, dev_conn->cli_MultipleRetryCount, dev_conn->cli_MaxDownlinkRate, dev_conn->cli_MaxUplinkRate);
    }

    printf("\n ssp_WIFIHALGetApAssociatedClientDiagnosticResult ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALGetAPCapabilities
 * Description          : This function invokes WiFi HAL api wifi_getAPCapabilities
 * @param [in]          : apIndex - WiFi Access Point Index
 *                        apCapabilities - structure with the access point capabilities details
 *                        output_string - To pass the formatted string containing the required structure parameter values
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetAPCapabilities(int apIndex, wifi_ap_capabilities_t *apCapabilities, char * output_string)
{
    printf("\n ssp_WIFIHALGetAPCapabilities ----> Entry\n");
    printf("apIndex : %d\n", apIndex);
    int return_status = 0;

    return_status = wifi_getAPCapabilities(apIndex, apCapabilities);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetAPCapabilities::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALGetAPCapabilities::Success; Access Point Capabilities : RTS Threshold Supported = %s, Security Modes Supported = 0x%04x, Onboarding Methods Supported = 0x%04x, WMM Supported = %s, UAPSD Supported = %s, Interworking Service Supported = %s, BSS Transition Implemented = %s\n", (apCapabilities->rtsThresholdSupported) ? "TRUE" : "FALSE", apCapabilities->securityModesSupported, apCapabilities->methodsSupported, (apCapabilities->WMMSupported) ? "TRUE" : "FALSE", (apCapabilities->UAPSDSupported) ? "TRUE" : "FALSE", (apCapabilities->interworkingServiceSupported) ? "TRUE" : "FALSE", (apCapabilities->BSSTransitionImplemented) ? "TRUE" : "FALSE");
        sprintf(output_string, "Access Point Capabilities : RTS Threshold Supported = %s, Security Modes Supported = 0x%04x, Onboarding Methods Supported = 0x%04x, WMM Supported = %s, UAPSD Supported = %s, Interworking Service Supported = %s, BSS Transition Implemented = %s\n", (apCapabilities->rtsThresholdSupported) ? "TRUE" : "FALSE", apCapabilities->securityModesSupported, apCapabilities->methodsSupported, (apCapabilities->WMMSupported) ? "TRUE" : "FALSE", (apCapabilities->UAPSDSupported) ? "TRUE" : "FALSE", (apCapabilities->interworkingServiceSupported) ? "TRUE" : "FALSE", (apCapabilities->BSSTransitionImplemented) ? "TRUE" : "FALSE");
    }

    printf("\n ssp_WIFIHALGetAPCapabilities ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALGetAvailableBSSColor
 * Description          : This function invokes WiFi HAL api wifi_getAvailableBSSColor
 * @param [in]          : radio_index - Radio Index
 *                        maxNumberColors - WL_COLOR_MAX_VALUE from wlioctl.h
 *                        colorList - List of available colors
 *                        numColorReturned - Number of colors returned in the list
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetAvailableBSSColor(int radio_index, int maxNumberColors, unsigned char* colorList, int *numColorReturned)
{
    printf("\n ssp_WIFIHALGetAvailableBSSColor ----> Entry\n");
    printf("radioIndex : %d\n", radio_index);
    printf("maxNumberColors : %d\n", maxNumberColors);
    int return_status = 0;
    int iteration = 0;

    return_status = wifi_getAvailableBSSColor(radio_index, maxNumberColors, colorList, numColorReturned);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetAvailableBSSColor::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALGetAvailableBSSColor::Success; NumColorReturned = %d\n", *numColorReturned);

        if (*numColorReturned > 0)
        {
            printf("Available BSSColor List = ");
            for (iteration = 0; iteration < *numColorReturned; iteration++)
            {
                printf("%d ", colorList[iteration]);
            }
        }
        else
        {
             printf("Available BSSColor List is Empty\n");
        }
    }

    printf("\n ssp_WIFIHALGetAvailableBSSColor ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetOrSetFTMobilityDomainID
 * Description          : This function invokes WiFi hal's get/set api's which are related to FTMobilityDomainID
 * @param [in]          : apIndex - Access Point index
 * @param [in]          : method - name of the wifi hal api to be invoked
 * @param [in]          : mobilityDomain - Value of the FT Mobility Domain for this AP
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetFTMobilityDomainID(int apIndex, unsigned char mobilityDomain[2], char * method)
{
    printf("\n ssp_WIFIHALGetOrSetFTMobilityDomainID ----> Entry\n");
    printf("Ap index : %d\n",apIndex);
    printf("MethodName : %s\n", method);

    int return_status = 0;

    if(!strcmp(method, "getFTMobilityDomainID"))
    {
        return_status = wifi_getFTMobilityDomainID(apIndex, mobilityDomain);

        if(return_status != SSP_SUCCESS)
        {
            printf("\n%s returned failure; ssp_WIFIHALGetOrSetFTMobilityDomainID::Failed\n", method);
            return_status = SSP_FAILURE;
        }
        else
        {
            printf("\n%s returned success; ssp_WIFIHALGetOrSetFTMobilityDomainID::Success; Mobility Domain ID[0] : 0x%x, Mobility Domain ID[1] : 0x%x\n", method, mobilityDomain[0], mobilityDomain[1]);
        }
    }
    else if(!strcmp(method, "setFTMobilityDomainID"))
    {
        printf("mobilityDomain : %s\n",mobilityDomain);
        return_status = wifi_setFTMobilityDomainID(apIndex, mobilityDomain);

        if(return_status != SSP_SUCCESS)
        {
            printf("\n%s returned failure; ssp_WIFIHALGetOrSetFTMobilityDomainID::Failed\n", method);
            return_status = SSP_FAILURE;
        }
        else
        {
            printf("\n%s returned success; ssp_WIFIHALGetOrSetFTMobilityDomainID::Success\n", method);
        }
    }
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForGetOrSetFTMobilityDomainID::Invalid Method Name\n");
    }

    printf("\n ssp_WiFiHalCallMethodForGetOrSetFTMobilityDomainID--> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetOrSetFTR0KeyHolderID
 * Description          : This function invokes WiFi hal's get/set api's which are related to FTR0KeyHolderID
 * @param [in]          : apIndex - Access Point index
 * @param [in]          : method - name of the wifi hal api to be invoked
 * @param [in]          : KeyHolderID - Value of the FTR0 Key Holder ID for this AP
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetFTR0KeyHolderID(int apIndex, unsigned char * KeyHolderID, char * method)
{
    printf("\n ssp_WIFIHALGetOrSetFTR0KeyHolderID ----> Entry\n");
    printf("Ap index : %d\n",apIndex);
    printf("MethodName : %s\n", method);
    int return_status = 0;
    int index = 0;

    if(!strcmp(method, "getFTR0KeyHolderID"))
    {
        return_status = wifi_getFTR0KeyHolderID(apIndex, KeyHolderID);
        if(return_status != SSP_SUCCESS)
        {
            printf("\n%s returned failure; ssp_WIFIHALGetOrSetFTR0KeyHolderID::Failed\n", method);
            return_status = SSP_FAILURE;
        }
        else
        {
            printf("\n%s returned success; ssp_WIFIHALGetOrSetFTR0KeyHolderID::Success", method);

            if(KeyHolderID[0] == '\0')
            {
                printf("\nKey Holder ID[0] : 0x%x", KeyHolderID[0]);
            }
            else
            {
                for(index = 0; KeyHolderID[index] != '\0'; index++)
                {
                    printf("\nKey Holder ID[%d] : 0x%x", index, KeyHolderID[index]);
                }
            }
        }
    }

    else if(!strcmp(method, "setFTR0KeyHolderID"))
    {
        if(KeyHolderID[0] == '\0')
        {
            printf("\nKey Holder ID[0] : 0x%x", KeyHolderID[0]);
        }
        else
        {
            for(index = 0; KeyHolderID[index] != '\0'; index++)
            {
                printf("\nKey Holder ID[%d] : 0x%x", index, KeyHolderID[index]);
            }
        }

        return_status = wifi_setFTR0KeyHolderID(apIndex, KeyHolderID);

        if(return_status != SSP_SUCCESS)
        {
            printf("\n%s returned failure; ssp_WIFIHALGetOrSetFTR0KeyHolderID::Failed\n", method);
            return_status = SSP_FAILURE;
        }
        else
        {
            printf("\n%s returned success; ssp_WIFIHALGetOrSetFTR0KeyHolderID::Success\n", method);
        }
    }

    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForGetOrSetFTR0KeyHolderID::Invalid Method Name\n");
    }

    printf("\n ssp_WiFiHalCallMethodForGetOrSetFTR0KeyHolderID--> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetRMCapabilities
 * Description          : This function invokes WiFi HAL api wifi_getRMCapabilities
 * @param [in]          : peer - MAC address of the client
 *                        out_Capabilities[5] - Array with RM capabilities details
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetRMCapabilities(mac_address_t peer, unsigned char out_Capabilities[5])
{
    printf("\n ssp_WIFIHALGetRMCapabilities ----> Entry\n");
    printf("Peer : %s\n", peer);
    int return_status = 0;

    return_status = wifi_getRMCapabilities(peer, out_Capabilities);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nWIFIHALGetRMCapabilities::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nWIFIHALGetRMCapabilities::Success\n");
        printf("\nRM Capabilities = capabilities[0] : %02X, capabilities[1] : %02X, capabilities[2] : %02X, capabilities[3] :  %02X, capabilities[4] : %02X ", out_Capabilities[0], out_Capabilities[1],out_Capabilities[2], out_Capabilities[3], out_Capabilities[4]);
    }

    printf("\n ssp_WIFIHALGetRMCapabilities ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALGetApSecurity
 * Description          : This function invokes WiFi HAL api wifi_getApSecurity
 * @param [in]          : apIndex - WiFi Access Point Index
 *                        security - structure with the AP security details
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetApSecurity(int apIndex, wifi_vap_security_t * security, char * output_string)
{
    printf("\n ssp_WIFIHALGetApSecurity ----> Entry\n");
    printf("apIndex : %d\n", apIndex);
    char output[1000] = {'\0'};
    int return_status = 0;

    return_status = wifi_getApSecurity(apIndex, security);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetApSecurity::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALGetApSecurity::Success; AP Security details : Security Mode : 0x%04x, Encrytion Method : %d, WPA3 Transition : %s, Rekey Interval : %d, Strict Rekey : %s, Eapol Key Timeout : %d, Eapol Key Retries : %d, Eap Identity Timeout : %d, Eap Identity Retries : %d, Eap Timeout : %d, Eap Retries : %d, PMKSA Cashing : %s, Security Key Type : %d", security->mode, security->encr, security->wpa3_transition_disable ? "Disabled" : "Enabled", security->rekey_interval, security->strict_rekey ? "Disabled" : "Enabled", security->eapol_key_timeout, security->eapol_key_retries, security->eap_identity_req_timeout, security->eap_identity_req_retries, security->eap_req_timeout, security->eap_req_retries, security->disable_pmksa_caching ? "Disabled" : "Enabled", security->u.key.type);
        sprintf(output, "AP Security details : Security Mode : 0x%04x, Encrytion Method : %d, WPA3 Transition : %s, Rekey Interval : %d, Strict Rekey : %s, Eapol Key Timeout : %d, Eapol Key Retries : %d, Eap Identity Timeout : %d, Eap Identity Retries : %d, Eap Timeout : %d, Eap Retries : %d, PMKSA Cashing : %s, Security Key Type : %d", security->mode, security->encr, security->wpa3_transition_disable ? "Disabled" : "Enabled", security->rekey_interval, security->strict_rekey ? "Disabled" : "Enabled", security->eapol_key_timeout, security->eapol_key_retries, security->eap_identity_req_timeout, security->eap_identity_req_retries, security->eap_req_timeout, security->eap_req_retries, security->disable_pmksa_caching ? "Disabled" : "Enabled", security->u.key.type);
        strcat(output_string, output);

        if (security->u.key.type == wifi_security_key_type_psk)
        {
            printf(", WPA PSK : 0x%s", security->u.key.key);
            sprintf(output, ", WPA PSK : 0x%s", security->u.key.key);
            strcat(output_string, output);
        }
        else
        {
            printf(", WPA Passphrase : %s", security->u.key.key);
            sprintf(output, ", WPA Passphrase : %s", security->u.key.key);
            strcat(output_string, output);
        }

#if defined(WIFI_HAL_VERSION_3)
        printf(", MFP : %d", security->mfp);
        sprintf(output, ", MFP : %d", security->mfp);
        strcat(output_string, output);
#endif
    }

    printf("\n ssp_WIFIHALGetApSecurity ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALSetApSecurity
 * Description          : This function invokes WiFi HAL api wifi_setApSecurity
 * @param [in]          : apIndex - WiFi Access Point Index
 *                        security - structure with the AP security details
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALSetApSecurity(int apIndex, wifi_vap_security_t * security)
{
    printf("\n ssp_WIFIHALGetApSecurity ----> Entry\n");
    printf("ApIndex : %d\n", apIndex);
    printf("Security Mode : 0x%04x\n", security->mode);
    printf("Encryption Method : %d\n", security->encr);
    printf("Key Type : %d\n", security->u.key.type);
    printf("Key : %s\n", security->u.key.key);

#if defined(WIFI_HAL_VERSION_3)
    printf("MFP : %d\n", security->mfp);
#endif

    if (security->mode == wifi_security_mode_wpa3_transition)
    {
        printf("WPA3 Transition Disable Status : %d\n", security->wpa3_transition_disable);
    }

    int return_status = 0;

    return_status = wifi_setApSecurity(apIndex, security);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALSetApSecurity::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALSetApSecurity::Success");
    }

    printf("\n ssp_WIFIHALSetApSecurity ---> Exit\n");
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALGetApWpsConfiguration
 * Description          : This function invokes WiFi HAL api wifi_getApWpsConfiguration
 * @param [in]          : apIndex - WiFi Access Point Index
 *                        wpsConfig - structure with the AP WPS configuration details
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetApWpsConfiguration(int apIndex, wifi_wps_t * wpsConfig, char * output_string)
{
    printf("\n ssp_WIFIHALGetApWpsConfiguration ----> Entry\n");
    printf("apIndex : %d\n", apIndex);
    char output[1000] = {'\0'};
    int wps_method = 0;
    int return_status = 0;

    return_status = wifi_getApWpsConfiguration(apIndex, wpsConfig);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetApWpsConfiguration :: Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        if(wpsConfig != NULL)
        {
            printf("ssp_WIFIHALGetApWpsConfiguration Success :: WPS Mode : %s\n", (wpsConfig->enable ? "Enabled" : "Disabled"));
            sprintf(output, "WPS Mode : %s", (wpsConfig->enable ? "Enabled" : "Disabled"));
            strcat(output_string, output);

            if (wpsConfig->enable)
            {
                printf("WPS device PIN: %s\n", wpsConfig->pin);
                sprintf(output, ", WPS device PIN: %s", wpsConfig->pin);
                strcat(output_string, output);

                printf("WPS enabled configuration methods : ");
                sprintf(output, ", WPS enabled configuration methods : ");
                strcat(output_string, output);

                for(wps_method = WIFI_ONBOARDINGMETHODS_USBFLASHDRIVE; wps_method <= WIFI_ONBOARDINGMETHODS_EASYCONNECT; wps_method = wps_method * 2)
                {

                    if (wpsConfig->methods & wps_method)
                    {
                        printf("0x%04x ", wps_method);
                        sprintf(output, "0x%04x ", wps_method);
                        strcat(output_string, output);
                    }
                }
            }
        }
        else
        {
            printf("\nssp_WIFIHALGetApWpsConfiguration::NULL Pointer::Failure");
            return_status = SSP_FAILURE;
        }
    }

    printf("\nReturn Status : %d :: ssp_WIFIHALGetApWpsConfiguration ---> Exit\n", return_status);
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALSetApWpsConfiguration
 * Description          : This function invokes WiFi HAL api wifi_setApWpsConfiguration
 * @param [in]          : apIndex - WiFi Access Point Index
 *                        wpsConfig - structure with the AP WPS configuration details
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALSetApWpsConfiguration(int apIndex, wifi_wps_t * wpsConfig)
{
    int return_status = 0;
    int wps_method = 0;
    printf("\n ssp_WIFIHALSetApWpsConfiguration ----> Entry\n");
    printf("ApIndex : %d\n", apIndex);

    if (wpsConfig != NULL)
    {
        printf("WPS Mode : %s\n", (wpsConfig->enable ? "Enabled" : "Disabled"));

        if(wpsConfig->enable)
        {
            printf("WPS Methods : 0x%04x\n", wpsConfig->methods);
            printf("WPS enabled configuration methods list : ");

            for(wps_method = WIFI_ONBOARDINGMETHODS_USBFLASHDRIVE; wps_method <= WIFI_ONBOARDINGMETHODS_EASYCONNECT; wps_method = wps_method * 2)
            {
                if (wpsConfig->methods & wps_method)
                {
                    printf("0x%04x ", wps_method);
                }
            }

            printf("WPS PIN : %s\n", wpsConfig->pin);
        }
    }
    else
    {
        printf("\nssp_WIFIHALSetApWpsConfiguration::NULL Pointer::Failure");
        return_status = SSP_FAILURE;
    }

    return_status = wifi_setApWpsConfiguration(apIndex, wpsConfig);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALSetApWpsConfiguration::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALSetApWpsConfiguration::Success");
    }

    printf("\nReturn Status : %d :: ssp_WIFIHALSetApWpsConfiguration ---> Exit\n", return_status);
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_WIFIHALGetOrSetFTR1KeyHolderID
 * Description          : This function invokes WiFi hal's get/set api's which are related to FTR1KeyHolderID
 * @param [in]          : apIndex - Access Point index
 * @param [in]          : method - name of the wifi hal api to be invoked
 * @param [in]          : KeyHolderID - Value of the FTR1 Key Holder ID for this AP
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetOrSetFTR1KeyHolderID(int apIndex, unsigned char * KeyHolderID, char * method)
{
    printf("\n ssp_WIFIHALGetOrSetFTR1KeyHolderID ----> Entry\n");
    printf("Ap index : %d\n",apIndex);
    printf("MethodName : %s\n", method);
    int return_status = 0;
    int index = 0;

    if(!strcmp(method, "getFTR1KeyHolderID"))
    {
        return_status = wifi_getFTR1KeyHolderID(apIndex, KeyHolderID);

        if(return_status != SSP_SUCCESS)
        {
            printf("\n%s returned failure; ssp_WIFIHALGetOrSetFTR1KeyHolderID::Failed\n", method);
            return_status = SSP_FAILURE;
        }
        else
        {
            printf("\n%s returned success; ssp_WIFIHALGetOrSetFTR1KeyHolderID::Success", method);

            if(KeyHolderID[0] == '\0')
            {
                printf("\nKey Holder ID[0] : 0x%x", KeyHolderID[0]);
            }
            else
            {
                for(index = 0; index < 64 && KeyHolderID[index] != '\0'; index++)
                {
                    printf("\nKey Holder ID[%d] : 0x%x", index, KeyHolderID[index]);
                }
            }
        }
    }
    else if(!strcmp(method, "setFTR1KeyHolderID"))
    {
        if(KeyHolderID[0] == '\0')
        {
            printf("\nKey Holder ID[0] : 0x%x", KeyHolderID[0]);
        }
        else
        {
            for(index = 0; index < 64 && KeyHolderID[index] != '\0'; index++)
            {
                printf("\nKey Holder ID[%d] : 0x%x", index, KeyHolderID[index]);
            }
        }

        return_status = wifi_setFTR1KeyHolderID(apIndex, KeyHolderID);

        if(return_status != SSP_SUCCESS)
        {
            printf("\n%s returned failure; ssp_WIFIHALGetOrSetFTR1KeyHolderID::Failed\n", method);
            return_status = SSP_FAILURE;
        }
        else
        {
            printf("\n%s returned success; ssp_WIFIHALGetOrSetFTR1KeyHolderID::Success\n", method);
        }
    }
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForGetOrSetFTR1KeyHolderID::Invalid Method Name\n");
    }

    printf("\nReturn Status : %d :: ssp_WiFiHalCallMethodForGetOrSetFTR1KeyHolderID--> Exit\n", return_status);
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALSetBSSColor
 * Description          : This function invokes WiFi HAL api wifi_setBSSColor
 * @param [in]          : radio_index - Radio Index
 *                        color - BSS color value to be set
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALSetBSSColor(int radio_index, unsigned char color)
{
    printf("\n ssp_WIFIHALSetBSSColor ----> Entry\n");
    printf("radioIndex : %d\n", radio_index);
    printf("color : %d\n", color);
    int return_status = 0;

    return_status = wifi_setBSSColor(radio_index, color);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALSetBSSColor::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALSetBSSColor::Success\n");
    }

    printf("\nReturn Status : %d :: ssp_WIFIHALSetBSSColor ---> Exit\n", return_status);
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALPushApFastTransitionConfig
 * Description          : This function invokes WiFi HAL api wifi_PushApFastTransitionConfig()
 * @param [in]          : apIndex - Access Point Index
 *                        ftCfg - Fast Transition Configuration structure
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALPushApFastTransitionConfig(int apIndex, wifi_FastTransitionConfig_t * ftCfg)
{
    printf("\n ssp_WIFIHALPushApFastTransitionConfig ----> Entry\n");
    int return_status = 0;

    if (ftCfg != NULL)
    {
        printf("apIndex : %d\n", apIndex);
        printf("FT Support : %d\n", ftCfg->support);
        printf("FT Mobility Domain ID : 0x%04x\n", ftCfg->mobilityDomain);
        printf("FT Over DS : %d\n", ftCfg->overDS);
    }
    else
    {
        printf("\nssp_WIFIHALPushApFastTransitionConfig::NULL Pointer::Failure");
        return_status = SSP_FAILURE;
    }

    return_status = wifi_pushApFastTransitionConfig(apIndex, ftCfg);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALPushApFastTransitionConfig::Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALPushApFastTransitionConfig::Success\n");
    }

    printf("\nReturn Status : %d :: ssp_WIFIHALPushApFastTransitionConfig ---> Exit\n", return_status);
    return return_status;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALGetMuEdca
 * Description          : This function invokes WiFi HAL api wifi_getMuEdca
 * @param [in]          : radioIndex - WiFi Radio Index
 *                        accessCategory - Access Category for MU (Multi-User) EDCA
 *                        (Enhanced Distributed Channel Access) includes background, best effort,
 *                        video, voice
 *                        edca - structure with the EDCA details for a given access category
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetMuEdca(int radioIndex, wifi_access_category_t accessCategory, wifi_edca_t *edca, char * output_string)
{
    printf("\n ssp_WIFIHALGetMuEdca ----> Entry\n");
    printf("radioIndex : %d\n", radioIndex);
    printf("Access Category : %d\n", accessCategory);
    int returnStatus = SSP_SUCCESS;

    returnStatus = wifi_getMuEdca(radioIndex, accessCategory, edca);

    if(returnStatus != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetMuEdca :: Failed\n");
        returnStatus = SSP_FAILURE;
    }
    else
    {
        if(edca != NULL)
        {
            printf("ssp_WIFIHALGetMuEdca Success :: MuEdca for Access Category = %d : aifsn=%d, cw_min=%d, cw_max=%d, timer=%d\n", accessCategory, edca->aifsn, edca->cw_min, edca->cw_max, edca->timer);
            sprintf(output_string, "MuEdca for Access Category = %d : aifsn=%d, cw_min=%d, cw_max=%d, timer=%d", accessCategory, edca->aifsn, edca->cw_min, edca->cw_max, edca->timer);
        }
        else
        {
            printf("\nssp_WIFIHALGetMuEdca::HAL API returned NULL Buffer::Failure");
            returnStatus = SSP_FAILURE;
        }
    }

    printf("\nReturn Status : %d :: ssp_WIFIHALGetMuEdca ---> Exit\n", returnStatus);
    return returnStatus;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALGetRadioOperatingParameters
 * Description          : This function invokes WiFi HAL api wifi_getRadioOperatingParameters
 * @param [in]          : radioIndex - WiFi Radio Index
 *                        operationParams - structure with the operating parameters details for
 *                        the given radio
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetRadioOperatingParameters(wifi_radio_index_t radioIndex, wifi_radio_operationParam_t *operationParams, char * output_string)
{
    printf("\n ssp_WIFIHALGetRadioOperatingParameters ----> Entry\n");
    printf("radioIndex : %d\n", radioIndex);
    char output[2000] = {'\0'};
    int bands = 0;
    int rates = 0;
    int iteration = 0;
    int chanWidth = 0;
    int variant = 0;
    int returnStatus = SSP_SUCCESS;

    returnStatus = wifi_getRadioOperatingParameters(radioIndex, operationParams);

    if(returnStatus != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetRadioOperatingParameters :: Failed\n");
        returnStatus = SSP_FAILURE;
    }
    else
    {
        if(operationParams != NULL)
        {
            printf("ssp_WIFIHALGetRadioOperatingParameters :: Success");
            printf("Radio Enable: %d\n", operationParams->enable);
            printf("AutoChannel Enabled: %d\n", operationParams->autoChannelEnabled);
            printf("Channel: %d\n", operationParams->channel);
            printf("CSA Beacon Count: %d\n", operationParams->csa_beacon_count);
            printf("DCS Enabled: %d\n", operationParams->DCSEnabled);
            printf("DTIM Period: %d\n", operationParams->dtimPeriod);
            printf("Beacon Interval: %d\n", operationParams->beaconInterval);
            printf("Operating Class: %d\n", operationParams->operatingClass);
            printf("Fragmentation Threshold: %d\n", operationParams->fragmentationThreshold);
            printf("Guard Interval: %d\n", operationParams->guardInterval);
            printf("Transmit Power: %d\n", operationParams->transmitPower);
            printf("RTS Threshold: %d\n", operationParams->rtsThreshold);
            printf("Radio Country Code: 0x%04x\n", operationParams->countryCode);
            printf("Number of Secondary Channels: %d\n", operationParams->numSecondaryChannels);

            sprintf(output, "Radio Enable: %d, AutoChannel Enabled: %d, Channel: %d, CSA Beacon Count: %d, DCS Enabled: %d, DTIM Period: %d, Beacon Interval: %d, Operating Class: %d, Fragmentation Threshold: %d, Guard Interval: %d, Transmit Power: %d, RTS Threshold: %d, Radio Country Code : 0x%04x, Number of Secondary Channels: %d,", operationParams->enable,operationParams->autoChannelEnabled, operationParams->channel, operationParams->csa_beacon_count, operationParams->DCSEnabled,operationParams->dtimPeriod, operationParams->beaconInterval, operationParams->operatingClass, operationParams->fragmentationThreshold,operationParams->guardInterval, operationParams->transmitPower, operationParams->rtsThreshold, operationParams->countryCode, operationParams->numSecondaryChannels);
            strcat(output_string, output);

            printf("Secondary Channels - \n");
            sprintf(output, " Channel Secondary: ");
            strcat(output_string, output);
            for (iteration = 0; iteration < operationParams->numSecondaryChannels; iteration++)
            {
                printf("channelSecondary[%d]: %d ", iteration, operationParams->channelSecondary[iteration]);
                sprintf(output, " %d", operationParams->channelSecondary[iteration]);
                strcat(output_string, output);
            }
            if(operationParams->numSecondaryChannels == 0)
            {
                printf("None\n");
                sprintf(output, "None");
                strcat(output_string, output);
            }

            printf("\nBands: 0x%04x", operationParams->band);
            sprintf(output, ", Bands: 0x%04x", operationParams->band);
            strcat(output_string, output);
            for(bands = WIFI_FREQUENCY_2_4_BAND; bands <= WIFI_FREQUENCY_60_BAND; bands = bands * 2)
            {
                if (operationParams->band & bands)
                {
                    printf("0x%04x ", bands);
                    sprintf(output, " 0x%04x", bands);
                    strcat(output_string, output);
                }
            }

            printf("\nChannel Width: 0x%04x", operationParams->channelWidth);
            sprintf(output, ", Channel Width: 0x%04x", operationParams->channelWidth);
            strcat(output_string, output);
            for(chanWidth = WIFI_CHANNELBANDWIDTH_20MHZ; chanWidth <= WIFI_CHANNELBANDWIDTH_80_80MHZ; chanWidth = chanWidth * 2)
            {
                if (operationParams->channelWidth & chanWidth)
                {
                    printf("0x%04x ", chanWidth);
                    sprintf(output, " 0x%04x", chanWidth);
                    strcat(output_string, output);
                }
            }

            printf("\n80211 Variants: 0x%04x \n", operationParams->variant);
            sprintf(output, ", 80211 Variants: 0x%04x", operationParams->variant);
            strcat(output_string, output);
            for(variant = WIFI_80211_VARIANT_A; variant <= WIFI_80211_VARIANT_AX; variant = variant * 2)
            {
                if (operationParams->variant & variant)
                {
                    printf("0x%04x ", variant);
                    sprintf(output, " 0x%04x", variant);
                    strcat(output_string, output);
                }
            }

            printf("\nBasic Data Transmit Rates: 0x%04x", operationParams->basicDataTransmitRates);
            sprintf(output, ", Basic Data Transmit Rates: 0x%04x", operationParams->basicDataTransmitRates);
            strcat(output_string, output);
            for(rates = WIFI_BITRATE_DEFAULT; rates <= WIFI_BITRATE_54MBPS; rates = rates * 2)
            {
                if (operationParams->basicDataTransmitRates & rates)
                {
                    printf("0x%04x ", rates);
                    sprintf(output, " 0x%04x", rates);
                    strcat(output_string, output);
                }
            }

            printf("\nOperational Data Transmit Rates: 0x%04x", operationParams->operationalDataTransmitRates);
            sprintf(output, ", Operational Data Transmit Rates: 0x%04x", operationParams->operationalDataTransmitRates);
            strcat(output_string, output);
            for(rates = WIFI_BITRATE_DEFAULT; rates <= WIFI_BITRATE_54MBPS; rates = rates * 2)
            {
                if (operationParams->operationalDataTransmitRates & rates)
                {
                    printf("0x%04x ", rates);
                    sprintf(output, " 0x%04x", rates);
                    strcat(output_string, output);
                }
            }
        }
        else
        {
            printf("\nssp_WIFIHALGetRadioOperatingParameters::HAL API returned NULL Buffer::Failure");
            returnStatus = SSP_FAILURE;
        }
    }

    printf("\nReturn Status : %d :: ssp_WIFIHALGetRadioOperatingParameters ---> Exit\n", returnStatus);
    return returnStatus;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALGetRadioChannels
 * Description          : This function invokes WiFi HAL api wifi_getRadioChannels
 * @param [in]          : radioIndex - WiFi Radio Index
 *                        outputMapSize - Size of radio channels buffer
 *                        outputMap - Structure with the Channel number and its corresponding state details
 *                        numberOfChannels - Number of possible radio channels for the radio
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetRadioChannels(int radioIndex, wifi_channelMap_t *outputMap, int outputMapSize, int numberOfChannels, char * output_string)
{
    printf("\n ssp_WIFIHALGetRadioChannels ----> Entry\n");
    printf("radioIndex : %d\n", radioIndex);
    printf("Size of the radio channels buffer : %d\n", outputMapSize);
    printf("Number of Channels : %d\n", numberOfChannels);
    int channel = 0;
    wifi_channelMap_t *chan;
    char output[4000] = {'\0'};
    int returnStatus = SSP_SUCCESS;

    returnStatus = wifi_getRadioChannels(radioIndex, outputMap, outputMapSize);

    if(returnStatus != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetRadioChannels :: Failed\n");
        returnStatus = SSP_FAILURE;
    }
    else
    {
        printf("ssp_WIFIHALGetRadioChannels Success");
        sprintf(output, "Channel Details -- ");
        strcat(output_string, output);

        if(outputMap != NULL)
        {

            for(channel = 0; channel < numberOfChannels; channel++)
            {
                chan = &outputMap[channel];
                printf("\nChannel %d : State %d", chan->ch_number, chan->ch_state);
                sprintf(output, "Channel %d : State %d ", chan->ch_number, chan->ch_state);
                strcat(output_string, output);
            }
        }
        else
        {
            printf("\nssp_WIFIHALGetRadioChannels::HAL API returned NULL Buffer::Failure");
            returnStatus = SSP_FAILURE;
        }
    }

    printf("\nReturn Status : %d :: ssp_WIFIHALGetRadioChannels ---> Exit\n", returnStatus);
    return returnStatus;
}

/*******************************************************************************************
 * Function Name        : ssp_WIFIHALGetEAPParam
 * Description          : This function invokes WiFi HAL api wifi_getEAP_Param
 * @param [in]          : apIndex - WiFi Access Point Index
 *                        eapConfig - structure with the EAP configuration details
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_WIFIHALGetEAPParam(int apIndex, wifi_eap_config_t * eapConfig, char * output_string)
{
    printf("\n ssp_WIFIHALGetEAPParam ----> Entry\n");
    printf("apIndex : %d\n", apIndex);
    int return_status = SSP_SUCCESS;

    return_status = wifi_getEAP_Param(apIndex, eapConfig);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_WIFIHALGetEAPParam :: Failed\n");
        return_status = SSP_FAILURE;
    }
    else
    {
        if(eapConfig != NULL)
        {
            printf("ssp_WIFIHALGetEAPParam Success :: EAP Congiguration -- ");
            printf("EAPOL Key Timeout: %u\n", eapConfig->uiEAPOLKeyTimeout);
            printf("EAPOL Key Retries: %u\n", eapConfig->uiEAPOLKeyRetries);
            printf("EAP Identity Request Timeout: %u\n", eapConfig->uiEAPIdentityRequestTimeout);
            printf("EAP Identity Request Retries: %u\n", eapConfig->uiEAPIdentityRequestRetries);
            printf("EAP Request Timeout: %u\n", eapConfig->uiEAPRequestTimeout);
            printf("EAP Request Retries: %u\n", eapConfig->uiEAPRequestRetries);

            sprintf(output_string, "EAP Congiguration -- EAPOL Key Timeout: %u, EAPOL Key Retries: %u, EAP Identity Request Timeout: %u, EAP Identity Request Retries: %u, EAP Request Timeout: %u, EAP Request Retries: %u", eapConfig->uiEAPOLKeyTimeout, eapConfig->uiEAPOLKeyRetries, eapConfig->uiEAPIdentityRequestTimeout, eapConfig->uiEAPIdentityRequestRetries, eapConfig->uiEAPRequestTimeout, eapConfig->uiEAPRequestRetries);
        }
        else
        {
            printf("\nssp_WIFIHALGetEAPParam::HAL API returned NULL Buffer::Failure");
            return_status = SSP_FAILURE;
        }
    }

    printf("\nReturn Status : %d :: ssp_WIFIHALGetEAPParam ---> Exit\n", return_status);
    return return_status;
}
