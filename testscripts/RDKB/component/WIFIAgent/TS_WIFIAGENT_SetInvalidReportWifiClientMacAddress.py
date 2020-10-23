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
  <name>TS_WIFIAGENT_SetInvalidReportWifiClientMacAddress</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the WIFI Client Mac Address with a Invalid Value</synopsis>
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
    <test_case_id>TC_WIFIAGENT_119</test_case_id>
    <test_objective>This test case is to set the WIFI Client Mac Address with a Invalid Value</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDKCENTRAL-COM_Report.WifiClient.MacAddress</input_parameters>
    <automation_approch>1.Load the module
2. Get the current value of WifiClient Mac Address
3. Set a invalid mac of length less than 12 Character
4. Check if the set operation is success then mark script as failure else mark as success
5. Unload the module</automation_approch>
    <expected_output>The set operation for  WifiClient Mac Address
 should fail with invalid mac of length less than 12 Character</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_SetInvalidReportWifiClientMacAddress</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_SetInvalidReportWifiClientMacAddress');

loadmodulestatus = obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.WiFi.X_RDKCENTRAL-COM_Report.WifiClient.MacAddress");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    default = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the WifiClient Mac Address";
        print "EXPECTED RESULT 1: Should get WifiClient Mac Address";
        print "ACTUAL RESULT 1: WifiClient current Mac Address:%s" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter("ParamName","Device.WiFi.X_RDKCENTRAL-COM_Report.WifiClient.MacAddress");
        expectedresult="FAILURE";
        tdkTestObj.addParameter("ParamValue","FFFFFFFFFF");
        tdkTestObj.addParameter("Type","unsignedint");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        Setresult = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Set the WifiClient Mac Address  to a invalid MAC: FFFFFFFFFF";
           print "EXPECTED RESULT 2: Should not set WifiClient Mac Address to a invalid MAC";
           print "ACTUAL RESULT 2: set operation failed for the WifiClient Mac Address with a invalid MAC" ;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
           #Set the result status of execution
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Set the WifiClient Mac Address to a invalid MAC :FFFFFFFFFF";
           print "EXPECTED RESULT 2: Should not set WifiClient Mac Address to a invalid MAC";
           print "ACTUAL RESULT 2: set operation was success for WifiClient Mac Address with a invalid MAC" ;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] :FAILURE";

           #Reverting to default in case set operation was success
           tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
           tdkTestObj.addParameter("ParamName","Device.WiFi.X_RDKCENTRAL-COM_Report.WifiClient.MacAddress");
           expectedresult="SUCCESS";
           tdkTestObj.addParameter("ParamValue",default);
           tdkTestObj.addParameter("Type","unsignedint");
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           result = tdkTestObj.getResultDetails();

           if expectedresult in  expectedresult:
              #Set the result status of execution
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP 3: Revert the Mac Address WifiClient to its default:",default;
              print "EXPECTED RESULT 3: Revert  Mac Address WifiClient to previous value";
              print "ACTUAL RESULT 3: Revert Operation sucesss:",result ;
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS"
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3: Revert the Mac Address WifiClient to its default:",default;
               print "EXPECTED RESULT 3: Revert  Mac Address WifiClient to previous value";
               print "ACTUAL RESULT 3: Revert Operation failed:",result ;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the WifiClient Mac Address";
        print "EXPECTED RESULT 1: Should get WifiClient Mac Address";
        print "ACTUAL RESULT 1: WifiClient current Mac Address  :%s" %default;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
