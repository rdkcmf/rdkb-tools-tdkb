##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <version>3</version>
  <name>TS_WIFIAGENT_GetWiFiInterworkingEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the RFC value of the parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable from rfc_configdata.txt is the same as the TR181 parameter value.</synopsis>
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
    <test_case_id>TC_WIFIAGENT_133</test_case_id>
    <test_objective>To check if the RFC value of the parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable from rfc_configdata.txt is the same as the TR181 parameter value.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Get</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable</input_parameters>
    <automation_approch>1. Load the wifiagent module
2. Fetch the RFC value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable from /tmp/rfc_configdata.txt
3. Get the TR181 value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable.
4. Compare both values and check if they are equal. If they are equal return Success else return Failure.
5. Unload the module</automation_approch>
    <expected_output>RFC value of the parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable from rfc_configdata.txt is the same as the TR181 parameter value.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_WIFIAGENT_GetWiFiInterworkingEnable</test_script>
    <skipped>No</skipped>
    <release_version>M88</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_GetWiFiInterworkingEnable');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_GetWiFiInterworkingEnable');

#Get the result of connection with test component and STB
loadmodulestatus=obj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();

if ("SUCCESS" in loadmodulestatus.upper()) and ("SUCCESS" in sysloadmodulestatus.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    expectedresult="SUCCESS"
    cmd= "cat /tmp/rfc_configdata.txt  | grep -i tr181.Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable#~";
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    print "details:",details

    if expectedresult in actualresult and details != "":
        enable = details.split("#~")[1].split(' ')[0].rstrip(" ");
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the RFC value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable from /tmp/rfc_configdata.txt";
        print "EXPECTED RESULT 1: the RFC value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable from /tmp/rfc_configdata.txt";
        print "ACTUAL RESULT 1: Successfully retrieved the value as: %s" %enable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Get the TR181 param value
        tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult :
            value = details.split("VALUE:")[1].split(' ')[0];
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the TR181 value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable";
            print "EXPECTED RESULT 2: Should get the TR181 value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable";
            print "ACTUAL RESULT 2: The TR181 value is fetched successfully : %s"%value;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if value == enable :
                tdkTestObj.setResultStatus("SUCCESS");
                print "The TR181 value is the same as the RFC value from /tmp/rfc_configdata.txt"
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "The TR181 value is not the same as the RFC value from /tmp/rfc_configdata.txt"
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the TR181 value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable";
            print "EXPECTED RESULT 2: Should get the TR181 value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable";
            print "ACTUAL RESULT 2: The TR181 value is not fetched successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the RFC value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable from /tmp/rfc_configdata.txt";
        print "EXPECTED RESULT 1: the RFC value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable from /tmp/rfc_configdata.txt";
        print "ACTUAL RESULT 1: Value not retrieved : %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

