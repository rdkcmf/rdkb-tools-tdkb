##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##########################################################################
'''
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>5</version>
  <name>TS_WIFIHAL_5GHzGetRadioOperatingParameters</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetRadioOperatingParameters</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getRadioOperatingParameters() and retrieve all the radio operating parameters for 5G radio.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_791</test_case_id>
    <test_objective>Invoke the HAL API wifi_getRadioOperatingParameters() and retrieve all the radio operating parameters for 5G radio.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioOperatingParameters()</api_or_interface_used>
    <input_parameters>radioIndex : 5G radio index</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getRadioOperatingParameters() for 5G radio and check if the invocation success.
3. If API successfully invoked, get the values of the following and check if the values are valid:
Radio Enable : valid enable state ,
Auto Channel Enable : valid enable state ,
Radio Channel : valid integer ,
CSA Beacon Count : valid integer ,
DCS Enabled : valid enable state ,
DTIM Period : valid integer ,
Beacon Interval : valid integer ,
Operating Class : valid integer ,
Fragmentation Threshold : valid integer ,
Guard Interval : valid integer ,
Transmit Power : valid integer ,
RTS Threshold : valid integer ,
Country Code : non-empty value ,
Number of secondary channels : valid integer ,
Secondary Channels : non-empty if number of secondary channels greater than 0 ,
Radio Bands : The Hex values should be one among {'0x0001' : "WIFI_FREQUENCY_2_4_BAND", '0x0002' : "WIFI_FREQUENCY_5_BAND", '0x0004' : "WIFI_FREQUENCY_5L_BAND", '0x0008' : "WIFI_FREQUENCY_5H_BAND", '0x0010' : "WIFI_FREQUENCY_6_BAND", '0x0020' : "WIFI_FREQUENCY_60_BAND"} ,
Channel Width : The Hex values should be one among {'0x0001' : "WIFI_CHANNELBANDWIDTH_20MHZ", '0x0002' : "WIFI_CHANNELBANDWIDTH_40MHZ", '0x0004' : "WIFI_CHANNELBANDWIDTH_80MHZ", '0x0008' : "WIFI_CHANNELBANDWIDTH_160MHZ", '0x0010' : "WIFI_CHANNELBANDWIDTH_80_80MHZ"} ,
80211 Variants : The Hex values should be one among {'0x0001' : "WIFI_80211_VARIANT_A", '0x0002' : "WIFI_80211_VARIANT_B", '0x0004' : "WIFI_80211_VARIANT_G", '0x0008' : "WIFI_80211_VARIANT_N", '0x0010' : "WIFI_80211_VARIANT_H", '0x0020' : "WIFI_80211_VARIANT_AC", '0x0040' : "WIFI_80211_VARIANT_AD", '0x0080' : "WIFI_80211_VARIANT_AX"} ,
Basic data transmit rate and operational data rate : The Hex values should be one among {'0x0001' : "WIFI_BITRATE_DEFAULT", '0x0002' : "WIFI_BITRATE_1MBPS", '0x0004' : "WIFI_BITRATE_2MBPS", '0x0008' : "WIFI_BITRATE_5_5MBPS", '0x0010' : "WIFI_BITRATE_6MBPS", '0x0020' : "WIFI_BITRATE_9MBPS", '0x0040' : "WIFI_BITRATE_11MBPS", '0x0080' : "WIFI_BITRATE_12MBPS", '0x0100' : "WIFI_BITRATE_18MBPS", '0x0200' : "WIFI_BITRATE_24MBPS", '0x0400' : "WIFI_BITRATE_36MBPS", '0x0800' : "WIFI_BITRATE_48MBPS", '0x1000' : "WIFI_BITRATE_54MBPS"}.
4. Unload the module</automation_approch>
    <expected_output>The HAL API wifi_getRadioOperatingParameters() should be invoked successfully and all the radio operating parameters retrieved for 5G radio should be valid values.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioOperatingParameters</test_script>
    <skipped>No</skipped>
    <release_version>M101</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioOperatingParameters');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep("WIFIHAL_GetRadioOperatingParameters");
        tdkTestObj.addParameter("radioIndex", idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Invoke the HAL API wifi_getRadioOperatingParameters() to retrieve the 5G Radio operating parameter values";
        print "EXPECTED RESULT 1: Should invoke the HAL API wifi_getRadioOperatingParameters() successfully";

        if expectedresult in actualresult and "Details" in details:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Retrieve the operating parameters and validating
            invalid_flag = 0;
            print "\nTEST STEP 2: Check if the operating parameters for the 5G radio are valid";
            print "EXPECTED RESULT 2: The operating parameters for the 5G radio should be valid";

            radio_enable = details.split("Radio Enable: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nRadio Enable : ", radio_enable;

            autoChannel_enable = details.split("AutoChannel Enabled: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nAuto Channel Enable : ", autoChannel_enable;

            channel = details.split("Channel: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nRadio Channel : ", channel;

            csa_beacon_count = details.split("CSA Beacon Count: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nCSA Beacon Count : ", csa_beacon_count;

            dcs_enabled = details.split("DCS Enabled: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nDCS Enabled : ", dcs_enabled;

            dtim_period = details.split("DTIM Period: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nDTIM Period : ", dtim_period;

            beacon_interval = details.split("Beacon Interval: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nBeacon Interval : ", beacon_interval;

            operating_class = details.split("Operating Class: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nOperating Class : ", operating_class;

            fragmentation_threshold = details.split("Fragmentation Threshold: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nFragmentation Threshold : ", fragmentation_threshold;

            guard_interval = details.split("Guard Interval: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nGuard Interval : ", guard_interval;

            transmit_power = details.split("Transmit Power: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nTransmit Power : ", transmit_power;

            rts_threshold = details.split("RTS Threshold: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nRTS Threshold : ", rts_threshold;

            radio_country_code = details.split("Radio Country Code : ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nCountry Code : ", radio_country_code;

            num_secondary_channels = details.split("Number of Secondary Channels: ")[1].strip().split(", ")[0].split(" ")[0];
            print "\nNumber of secondary channels : ", num_secondary_channels;

            secondary_channels = [];
            secondary_channels = details.split("Channel Secondary: ")[1].strip().split(", ")[0].split(" ");
            if num_secondary_channels.isdigit() and int(num_secondary_channels) > 0:
                for iteration in range(0, int(num_secondary_channels)):
                    if secondary_channels[iteration] != "":
                        print "Secondary Channel[%d] : %s" %(iteration, secondary_channels[iteration]);
                    else:
                        invalid_flag = 1;
                        print "Secondary Channel[%d] : Not retrieved" %(iteration - 1);
            else :
                print "Secondary Channels : ", secondary_channels;

            bands = details.split("Bands: ")[1].strip().split(", ")[0].split(" ");
            print "\nRadio Bands : ", bands[0];
            #Remove the initial element as it is the combined hex value
            bands.remove(bands[0]);
            #Map the Bands Hexadecimal values to corresponding radio bands
            bands_dict = {'0x0001' : "WIFI_FREQUENCY_2_4_BAND", '0x0002' : "WIFI_FREQUENCY_5_BAND", '0x0004' : "WIFI_FREQUENCY_5L_BAND", '0x0008' : "WIFI_FREQUENCY_5H_BAND", '0x0010' : "WIFI_FREQUENCY_6_BAND", '0x0020' : "WIFI_FREQUENCY_60_BAND"};
            if len(bands) > 0:
                for band in bands :
                    if band in bands_dict :
                        radio_band = bands_dict[band];
                    else :
                        invalid_flag = 1;
                        radio_band = "Invalid Radio Band";
                    print "%s : %s" %(band, radio_band);

            channel_width = details.split("Channel Width: ")[1].strip().split(", ")[0].split(" ");
            print "\nChannel Width : ", channel_width[0];
            #Remove the initial element as it is the combined hex value
            channel_width.remove(channel_width[0]);
            #Map the channel width Hexadecimal values to corresponding width
            width_dict = {'0x0001' : "WIFI_CHANNELBANDWIDTH_20MHZ", '0x0002' : "WIFI_CHANNELBANDWIDTH_40MHZ", '0x0004' : "WIFI_CHANNELBANDWIDTH_80MHZ", '0x0008' : "WIFI_CHANNELBANDWIDTH_160MHZ", '0x0010' : "WIFI_CHANNELBANDWIDTH_80_80MHZ"};
            if len(channel_width) > 0:
                for width in channel_width :
                    if width in width_dict :
                        chan_width = width_dict[width];
                    else :
                        invalid_flag = 1;
                        chan_width = "Invalid Channel Width";
                    print "%s : %s" %(width, chan_width);

            variants = details.split("Variants: ")[1].strip().split(", ")[0].split(" ");
            print "\n80211 Variants : ", variants[0];
            #Remove the initial element as it is the combined hex value
            variants.remove(variants[0]);
            #Map the 80211 Variant Hexadecimal values to corresponding width
            variant_dict = {'0x0001' : "WIFI_80211_VARIANT_A", '0x0002' : "WIFI_80211_VARIANT_B", '0x0004' : "WIFI_80211_VARIANT_G", '0x0008' : "WIFI_80211_VARIANT_N", '0x0010' : "WIFI_80211_VARIANT_H", '0x0020' : "WIFI_80211_VARIANT_AC", '0x0040' : "WIFI_80211_VARIANT_AD", '0x0080' : "WIFI_80211_VARIANT_AX"};
            if len(variants) > 0:
                for var in variants :
                    if var in variant_dict :
                        var_80211 = variant_dict[var];
                    else :
                        invalid_flag = 1;
                        var_80211 = "Invalid 80211 Variant";
                    print "%s : %s" %(var, var_80211);

            basic_data_rate = details.split("Basic Data Transmit Rates: ")[1].strip().split(", ")[0].split(" ");
            print "\nBasic Data Transmit Rates : ", basic_data_rate[0];
            #Remove the initial element as it is the combined hex value
            basic_data_rate.remove(basic_data_rate[0]);
            #Map the basic data rate Hexadecimal values to corresponding bitrates
            bitrate_dict = {'0x0001' : "WIFI_BITRATE_DEFAULT", '0x0002' : "WIFI_BITRATE_1MBPS", '0x0004' : "WIFI_BITRATE_2MBPS", '0x0008' : "WIFI_BITRATE_5_5MBPS", '0x0010' : "WIFI_BITRATE_6MBPS", '0x0020' : "WIFI_BITRATE_9MBPS", '0x0040' : "WIFI_BITRATE_11MBPS", '0x0080' : "WIFI_BITRATE_12MBPS", '0x0100' : "WIFI_BITRATE_18MBPS", '0x0200' : "WIFI_BITRATE_24MBPS", '0x0400' : "WIFI_BITRATE_36MBPS", '0x0800' : "WIFI_BITRATE_48MBPS", '0x1000' : "WIFI_BITRATE_54MBPS"};
            if len(basic_data_rate) > 0:
                for rate in basic_data_rate :
                    if rate in bitrate_dict :
                        bitrate = bitrate_dict[rate];
                    else :
                        invalid_flag = 1;
                        bitrate = "Invalid Basic Data Rate";
                    print "%s : %s" %(rate, bitrate);

            operation_data_rate = details.split("Operational Data Transmit Rates: ")[1].strip().split(" ");
            print "\nOperational Data Rate : ", operation_data_rate[0];
            #Remove the initial element as it is the combined hex value
            operation_data_rate.remove(operation_data_rate[0]);
            if len(operation_data_rate) > 0:
                for rate in operation_data_rate :
                    if rate in bitrate_dict :
                        bitrate = bitrate_dict[rate];
                    else :
                        invalid_flag = 1;
                        bitrate = "Invalid Operational Data Rate";
                    print "%s : %s" %(rate, bitrate);

            if (radio_enable == '0' or radio_enable == '1') and (autoChannel_enable == '0' or autoChannel_enable == '1') and channel.isdigit() and csa_beacon_count.isdigit() and (dcs_enabled == '0' or dcs_enabled == '1') and dtim_period.isdigit() and beacon_interval.isdigit() and operating_class.isdigit() and fragmentation_threshold.isdigit() and guard_interval.isdigit() and num_secondary_channels.isdigit() and bands[0] != "" and variants[0] != "" and basic_data_rate[0] != "" and operation_data_rate[0] != "" and invalid_flag != 1:
                print "ACTUAL RESULT 2: The Operating parameter details are retrieved and all values are valid";
                print "TEST EXECUTION RESULT 2: SUCCESS";
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "ACTUAL RESULT 2: All Operating parameter details are not valid";
                print "TEST EXECUTION RESULT 2: FAILURE";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
