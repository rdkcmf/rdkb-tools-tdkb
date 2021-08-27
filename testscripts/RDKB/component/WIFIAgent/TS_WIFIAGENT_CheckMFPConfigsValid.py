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
  <version>1</version>
  <name>TS_WIFIAGENT_CheckMFPConfigsValid</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if MFP Security Config  holds accepted values</synopsis>
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
    <test_case_id>TC_WIFIAGENT_139</test_case_id>
    <test_objective>This test case is to check if MFP Security Config  holds accepted values</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Set
WIFIAgent_Get</api_or_interface_used>
    <input_parameters>Device.WiFi.AccessPoint.{i}.Security.MFPConfig</input_parameters>
    <automation_approch>1.Load the module
2.Get the MFP Security Access point values for instance  1 to 16
3. The acceptable values for MFP Security Access point are Optional , Disabled and Required
4.Mark the script as SUCCESS if the values are one among the acceptable values else mark the script as FAILURE
5.Unload the module</automation_approch>
    <expected_output>All the security access point values for MFP Config are expected to be one among  Optional , Disabled and Required</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckMFPConfigsValid</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckMFPConfigsValid');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    statusFlag = 0;
    noOfEntries = 16;
    print "TEST STEP 1:Checking if CPE MFP Configs Access Points has acceptable values";
    acceptableValues = ["Disabled", "Optional", "Required"];
    while noOfEntries > 0:
          expectedresult="SUCCESS";
          tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
          tdkTestObj.addParameter("ParamName","Device.WiFi.AccessPoint.%i.Security.MFPConfig" %noOfEntries);
          #Execute the test case in DUT
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails();
          if expectedresult in actualresult  and details in acceptableValues:
             tdkTestObj.setResultStatus("SUCCESS");
             print"Device.WiFi.AccessPoint.%i.Security.MFPConfig is %s" %(noOfEntries,details);
             print "[TEST EXECUTION RESULT] : SUCCESS";
          else:
              statusFlag = 1;
              tdkTestObj.setResultStatus("FAILURE");
              print"Device.WiFi.AccessPoint.%i.Security.MFPConfig is %s" %(noOfEntries,details);
              print "[TEST EXECUTION RESULT] :FAILURE";
          noOfEntries = noOfEntries -1;

    #setitng the script status
    if  statusFlag == 1:
         tdkTestObj.setResultStatus("FAILURE");
         print "ACTUAL RESULT2: The MFP Configs Access Points donot have the acceptable values";
         print "[TEST EXECUTION RESULT] :FAILURE";
    else:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT2: The MFP Configs Access Points have the acceptable values";
        print "[TEST EXECUTION RESULT] :SUCCESS";
    obj.unloadModule("tdkbtr181");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
