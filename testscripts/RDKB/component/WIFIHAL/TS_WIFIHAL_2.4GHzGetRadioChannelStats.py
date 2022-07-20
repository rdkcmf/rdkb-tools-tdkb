##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <version>1</version>
  <name>TS_WIFIHAL_2.4GHzGetRadioChannelStats</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetRadioChannelStats</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>This test script is to find the radichannelstats of wifi_getRadioChannelStats() of 2.4ghz</synopsis>
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
    <test_case_id>TC_WIFIHAL_315</test_case_id>
    <test_objective>This test script is to find the radichannelstats of wifi_getRadioChannelStats() of 2.4ghz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioChannelStats()</api_or_interface_used>
    <input_parameters>methodName =getRadioChannelStats
radioIndex = 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getRadioPossibleChannels() to retrieve the possible radio channels list
3. Invoke wifi_getRadioChannelStats() to retrieve the channel stats for each radio channels and check if the stats are valid
4. Unload wifihal module</automation_approch>
    <except_output>It should return the wifihal radiochannel stats</except_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetRadioChannelStats</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetRadioChannelStats');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the possible radio channels list
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
        tdkTestObj.addParameter("methodName","getRadioPossibleChannels");
        tdkTestObj.addParameter("radioIndex",idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1 : Invoke the HAL API wifi_getRadioPossibleChannels() to get the possible radio channels for 2.4G radio";
        print "EXPECTED RESULT 1 : The HAL API wifi_getRadioPossibleChannels() should be invoked successfully";

        if expectedresult in actualresult and details != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: API invocation is success; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #if possible channels are given as a range eg: 1-11
            if "-" in details:
                #get the possible channels as a list of integers
                PossibleChannelRange = [int(x) for x in details.split(":")[1].split("-")];
                PossibleChannels = range(PossibleChannelRange[0],PossibleChannelRange[1]+1);
                print "Possible channels are ", PossibleChannels;
                #if possible channels are given as values eg:1,2,3,4,5
            else:
                #get the possible channels as a list of integers
                PossibleChannels = [int(x) for x in details.split(":")[1].split(",")];
                print "Possible channels are ", PossibleChannels;

            #Get the channel stats for each of the possible radio channels
            return_status = 0;
            failed_channels = [];
            valid_values = 0;
            failed_stats = [];
            print "\nTEST STEP 2 : Get the Radio channel statistics info for 2.4GHz using the HAL API wifi_getRadioChannelStats()";
            print "EXPECTED RESULT 2: wifi_getRadioChannelStats should return the radio channel statistics for 2.4GHz";

            primitive = 'WIFIHAL_GetRadioChannelStats'
            tdkTestObj = obj.createTestStep(primitive);
            tdkTestObj.addParameter("radioIndex",idx);

            for channel in PossibleChannels:
                print "\n*********For radio channel : %d*********" %channel;
                tdkTestObj.addParameter("channel", channel);
                tdkTestObj.addParameter("inPool", 1);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                if "wifi_getRadioChannelStats returned success" in details :
                    channel = details.split("ch_number=")[1].split(",")[0];
                    channel_in_pool = details.split("ch_in_pool=")[1].split(",")[0];
                    channel_noise = details.split("ch_noise=")[1].split(",")[0];
                    channel_radar_noise = details.split("ch_radar_noise=")[1].split(",")[0];
                    channel_max_80211_rssi = details.split("ch_max_80211_rssi=")[1].split(",")[0];
                    channel_non_80211_noise = details.split("ch_non_80211_noise=")[1].split(",")[0];
                    channel_utilisation = details.split("ch_utilization=")[1].split(",")[0];
                    channel_utilisation_total = details.split("ch_utilization_total=")[1].split(",")[0];
                    channel_utilisation_busy = details.split("ch_utilization_busy=")[1].split(",")[0];
                    channel_utilisation_busy_tx = details.split("ch_utilization_busy_tx=")[1].split(",")[0];
                    channel_utilisation_busy_rx = details.split("ch_utilization_busy_rx=")[1].split(",")[0];
                    channel_utilisation_busy_self = details.split("ch_utilization_busy_self=")[1].split(",")[0];
                    channel_utilisation_busy_ext = details.split("ch_utilization_busy_ext=")[1].split(",")[0];

                    #Print the channel stats values
                    print "\nFor Channel : %s, Channel in Pool : %s, Channel Noise : %s, Channel Radar Noise : %s, Channel Max 80211 RSSI : %s, Channel Non 80211 Noise : %s, Channel Utilization : %s, Channel Utilization Total: %s, Channel Utilization Busy: %s, Channel Utilization Busy Tx: %s, Channel Utilization Busy Rx: %s, Channel Utilization Busy Self: %s, Channel Utilization Busy Ext: %s" %(channel, channel_in_pool, channel_noise, channel_radar_noise, channel_max_80211_rssi, channel_non_80211_noise, channel_utilisation, channel_utilisation_total, channel_utilisation_busy, channel_utilisation_busy_tx, channel_utilisation_busy_rx, channel_utilisation_busy_self, channel_utilisation_busy_ext);

                    if channel.isdigit() and channel_in_pool.isdigit() and channel_noise.lstrip('-').isdigit() and channel_radar_noise.lstrip('-').isdigit() and channel_max_80211_rssi.lstrip('-').isdigit() and channel_non_80211_noise.lstrip('-').isdigit() and channel_utilisation.isdigit() and channel_utilisation_total.isdigit() and channel_utilisation_busy.isdigit() and channel_utilisation_busy_tx.isdigit() and channel_utilisation_busy_rx.isdigit() and channel_utilisation_busy_self.isdigit() and channel_utilisation_busy_ext.isdigit():
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "For Channel %s, the Channel Stats are valid" %channel;
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "For Channel %s, the Channel Stats are NOT valid" %channel;
                        valid_values = 1;
                        failed_stats.append(channel);
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "For Channel %s, the Channel Stats are NOT retrieved" %channel;
                    return_status = 1;
                    failed_channels.append(channel);

            if return_status == 0 and valid_values == 0:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: wifi_getRadioChannelStats() API invoked successfully for all possible radio channels and channel stats are valid";
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: wifi_getRadioChannelStats() operation returned FAILURE or channel stats are not valid";
                print "wifi_getRadioChannelStats() operation returned FAILURE for the channels : ", failed_channels;
                print "Channel Stats retrieved are not valid values for the channels : ", failed_stats;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: API invocation failed; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");

