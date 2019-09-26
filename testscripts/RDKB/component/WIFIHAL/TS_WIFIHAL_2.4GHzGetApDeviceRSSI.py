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
  <version>16</version>
  <name>TS_WIFIHAL_2.4GHzGetApDeviceRSSI</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApDeviceRSSI</primitive_test_name>
  <primitive_test_version>10</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the RSSI value set in device for 2.4GHz radio using wifi_getApDeviceRSSI API ..</synopsis>
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
    <test_case_id>TC_WIFIHAL_323</test_case_id>
    <test_objective>To get the RSSI value set in device for 2.4GHz radio using wifi_getApDeviceRSSI API .</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApDeviceRSSI()</api_or_interface_used>
    <input_parameters>methodName : getApDeviceRSSI()
apindex :0
Before running the script we should connect the device and should give MAC address</input_parameters>
    <automation_approch>1.Load the module.
2.Get the RSSI value of the device attached to the AP by using wifi_getApDeviceRSSI() by invoking WIFIHAL_GetApDeviceRSSI
3. If RSSI is extracted from the details , it is counted as SUCCESS or else FAILURE
4.Unload the module.</automation_approch>
    <except_output>Should successfully get the RSSI value from the device for 2.4GHz radio using WIFIHAL_GetApDeviceRSSI HAL API</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetApDeviceRSSI</test_script>
    <skipped>No</skipped>
    <release_version>M68</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import re;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetApDeviceRSSI');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    print "TEST STEP1: Get AssociatedDevice details"
    tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDevice');
    tdkTestObj.addParameter("apIndex",0);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "Entire Details:",details;
    if expectedresult in actualresult:
        outputList = details.split("=")[1].strip()
        if "," in outputList:
            outputValue = outputList.split(",")[0].strip()
        else:
            outputValue = outputList.split(":Value")[0].strip()
        
        print "test step: get the associateddevice"
        print "expected result: should get the number of associated devices"
        print "Associated Device's MAC address:",outputValue
        
        #check if outputvalue is a mac address
        if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", outputValue.lower()):
            #prmitive test case which associated to this script
            tdkTestObj = obj.createTestStep("WIFIHAL_GetApDeviceRSSI");
            tdkTestObj.addParameter("methodName","getApDeviceRSSI");
            tdkTestObj.addParameter("apIndex", 0);
            #Connect a device and add MAC Address
            tdkTestObj.addParameter("MAC",outputValue);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print"details",details;
            if expectedresult in actualresult :
                print "TEST STEP : Get the ApDeviceRSSI"
                print "EXPECTED RESULT : Should successfully get the ApDeviceRSSI"
                print "ACTUAL RESULT : Successfully gets the ApDeviceRSSI"
                RSSI_details = int(details.split(":")[1].strip());
                if RSSI_details<0:               
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP : Check the ApDeviceRSSI"
                    print "EXPECTED RESULT : ApDeviceRSSI should be less than 0"
                    print "ACTUAL RESULT : ApDeviceRSSI is less than 0"
                    print " RSSI_details=", RSSI_details

                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    print "RSSI value is greater than 0"
                    tdkTestObj.setResultStatus("FAILURE") 
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : Get the ApDeviceRSSI"
                print "EXPECTED RESULT : Should successfully get the ApDeviceRSSI"
                print "ACTUAL RESULT : Failed to get the ApDeviceRSSI"
                print "Details: %s"%details
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
             tdkTestObj.setResultStatus("FAILURE");
             print "Not able to  Get the ApDeviceRSSI as no device is connected or Invalid Format"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP: get the associateddevice"
        print "EXPECTED RESULT: should get the number of associated devices"
        print "ACTUAL RESULT : Failed to get the number of associated devices"
    obj.unloadModule("wifihal");

else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
