##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <name>TS_WIFIHAL_5GHZGetApAssociatedDeviceTidStatsResult</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApAssociatedDeviceTidStatsResult</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check for the successful invocation of ac,tid,sum_time_ms using wifi_getApAssociatedDeviceTidStatsResult</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_354</test_case_id>
    <test_objective>To check for the successful invocation of sum_time_ms,tid,sum_time_m using wifi_getApAssociatedDeviceTidStatsResult</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Connect a wifi client</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDeviceTidStatsResult</api_or_interface_used>
    <input_parameters>methodName :'WIFIHAL_GetApAssociatedDeviceTidStatsResult
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the module.
2.Get the  getApAssociatedDeviceTidStatsResult using  wifi_getApAssociatedDeviceTidStatsResult API.
3.Return SUCCESS for non empty value,else FAILURE.
4.Unload module.</automation_approch>
    <expected_output>Api should be invoked successfully and the values received from the api should be non empty</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHZGetApAssociatedDeviceTidStatsResult</test_script>
    <skipped>No</skipped>
    <release_version>M73</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import re ;
import time;
from wifiUtility import *;
from xfinityWiFiLib import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
radio = "5G"
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHZGetApAssociatedDeviceTidStatsResult');

wifiobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHZGetApAssociatedDeviceTidStatsResult');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
sysloadmodulestatus = wifiobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus

if "SUCCESS" in loadmodulestatus.upper() and sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    wifiobj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the list of supported security modes
        tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
        tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.AssociatedDevice.1.MACAddress");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            MAC = details.split("VALUE:")[1].split(' ')[0];
            print "TEST STEP: Get the MAC of the connected client ";
            print "ACTUAL RESULT: Should get the mac of connected client ";
            print "EXPECTED RESULT:",MAC;
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if MAC :
               tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDeviceTidStatsResult');
               tdkTestObj.addParameter("radioIndex", 1);
               tdkTestObj.addParameter("MAC", MAC);
               expectedresult="SUCCESS";
               tdkTestObj.executeTestCase(expectedresult);
               actualresult = tdkTestObj.getResult();
               resultDetails = tdkTestObj.getResultDetails();
               if expectedresult in actualresult :
                  ac = resultDetails.split(':')[1].split(',')[0].strip();
                  tid = resultDetails.split(':')[2].split(',')[0].strip();
                  sum_time_ms = resultDetails.split(':')[3].strip();
                  if ac  !=  "(null)"  and tid != "(null)" and sum_time_ms != 0 :
                     tdkTestObj.setResultStatus("SUCCESS");
                     print "TEST STEP : Get the ac,tid,sum_time_ms"
                     print "EXPECTED RESULT : Should successfuly get ac,tid,sum_time_ms"
                     print "ACTUAL RESULT : %s"%resultDetails;
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : SUCCESS";
                  else:
                      tdkTestObj.setResultStatus("FAILURE");
                      print "TEST STEP : Get the ac,tid,sum_time_ms"
                      print "EXPECTED RESULT : Should successfuly get ac,tid,sum_time_ms"
                      print "ACTUAL RESULT : Failed to invoke %s"%resultDetails;
                      print "[TEST EXECUTION RESULT] : FAILURE";
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print " ApAssociatedDeviceTidStatsResult Failed "
                   print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "MAC received form TR181 param is empty"
                print "[TEST EXECUTION RESULT] : FAILURE";


        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP: Get the MAC of the connected client ";
            print "ACTUAL RESULT: Should get the mac of connected client "
            print "EXPECTED RESULT:",details;
            print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
    wifiobj.unloadModule("wifiagent");

else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

