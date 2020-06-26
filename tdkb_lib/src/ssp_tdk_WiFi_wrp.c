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
#if defined(_COSA_BCM_MIPS_) || defined(_XB7_PRODUCT_REQ_)
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
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALApplySettings::Success\n");
        return return_status;
    }

    printf("\n ssp_WIFIHALApplySettings----> Exit\n");
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
    printf("GetorSetParam: %d\n" , *enable);
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
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WIFIHALGetOrSetParamBoolValue: Invalid methodName\n");
    }

    printf("ssp_WIFIHALGetOrSetParamBoolValue: Enable status is %d, ret:status %d\n", *enable, return_status);
    printf("\n ssp_WIFIHALGetOrSetParamBoolValue----> Exit\n");
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
    printf("GetorSetParam: %s\n" , output);
    printf("MethodName: %s\n", method);
    int return_status = 0;

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
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForString: Invalid methodName\n");
    }

    printf("ssp_WiFiHalCallMethodForString: return value is %s, ret:status %d\n", output,return_status);
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
    printf("GetorSetParam: %d\n" , *output);
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
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForInt: Invalid methodName\n");
    }

    printf("ssp_WiFiHalCallMethodForInt: return value is %d, ret:status %d\n", *output, return_status);
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
    printf("GetorSetParam: %u\n" , *output);
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
    else
    {
        return_status = SSP_FAILURE;
        printf("\n ssp_WiFiHalCallMethodForUInt: Invalid methodName\n");
    }

    printf("ssp_WiFiHalCallMethodForUInt: return value is %d, ret:status %d\n", *output, return_status);
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALGetIndexFromName::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetIndexFromName ----> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALClearRadioResetCount::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALClearRadioResetCount ----> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALReset::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALReset ----> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALGetSSIDTrafficStats2::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetSSIDTrafficStats2 ---> Exit\n");
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
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALGetRadioTrafficStats2::Success\n");
        return return_status;
    }
    printf("\n ssp_WiFiHalCallMethodForGetRadioTrafficStats2---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult ---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALDown::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALDown ----> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\nssp_WIFIHALCreateInitialConfigFiles::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALCreateInitialConfigFiles ----> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetNeighboringWiFiDiagnosticResult2::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetNeighboringWiFiDiagnosticResult2 ---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetNeighboringWiFiStatus::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetNeighboringWiFiStatus ---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALPushRadioChannel2::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALPushRadioChannel2 ---> Exit\n");
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
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_WIFIHALGetRadioChannelStats::Success\n");
        return return_status;
    }
    printf("\n ssp_WiFiHalCallMethodForGetRadioChannelStats---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDevice::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetApAssociatedDevice ---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAclDevices::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetApAclDevices ---> Exit\n");
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
        printf("\ssp_WIFIHALGetRadioChannelStats2::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\ssp_WIFIHALGetRadioChannelStats2::Success\n");
        return return_status;
    }
    printf("\n ssp_WIFIHALGetRadioChannelStats2---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult3::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult3 ---> Exit\n");
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
    printf("MAC:%s\n",clientMacAddress);
    int return_status = 0;
    return_status = wifi_getApAssociatedDeviceStats(apIndex, clientMacAddress, associated_dev_stats, handle);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetApAssociatedDeviceStats::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceStats::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceStats ---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceTxStatsResult::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceTxStatsResult ---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceRxStatsResult::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceRxStatsResult ---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALStartNeighborScan::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetNeighboringWiFiStatus ---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceTidStatsResult::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceTidStatsResult ---> Exit\n");
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
    printf ("pClientMAC : %s\n",*pClientMAC);
    int return_status = 0;
    return_status = wifi_getBandSteeringLog(record_index, pSteeringTime, pClientMAC,pSourceSSIDIndex,pDestSSIDIndex,pSteeringReason);
    if(return_status != SSP_SUCCESS)
    {
     printf("\nssp_WIFIHALGetBandSteeringLog::Failed\n");
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetBandSteeringLog::Success\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetBandSteeringLog ---> Exit\n");
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
     return SSP_FAILURE;
    }
    else
    {
     printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult2\n");
     return return_status;
    }
    printf("\n ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult2 ---> Exit\n");
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

