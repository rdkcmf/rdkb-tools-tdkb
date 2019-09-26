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
  <version>2</version>
  <name>TS_COSAMTA_GetBatteryTotalCapacity</name>
  <primitive_test_id/>
  <primitive_test_name>CosaMTA_GetParamUlongValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the total capacity of the battery is greater than zero if battery is installed</synopsis>
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
    <test_case_id>TC_COSAMTA_35</test_case_id>
    <test_objective>Check if the total capacity of the battery is greater than zero if battery is installed</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CosaDmlMtaBatteryGetTotalCapacity</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load Cosamta module
2. Check if the battery is installed or not
3. Get the total capacity of the battery
4. Check if total capacity of the battery is 0 if battery is not installed or greater than 0 if installed
5. Unload Cosamta module</automation_approch>
    <except_output>Total capacity of the battery is 0 if battery is not installed or greater than 0 if installed</except_output>
    <priority>High</priority>
    <test_stub_interface>cosamta</test_stub_interface>
    <test_script>TS_COSAMTA_GetBatteryTotalCapacity</test_script>
    <skipped>No</skipped>
    <release_version>M67</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cosamta","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_COSAMTA_GetBatteryTotalCapacity');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("CosaMTA_GetParamUlongValue");
    tdkTestObj.addParameter("handleType",0);
    tdkTestObj.addParameter("paramName","BatteryInstalled");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    install = " ";
    install = tdkTestObj.getResultDetails();
    status = [ "FALSE", "TRUE" ];

    if expectedresult in actualresult and (install == '0' or install == '1'):
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the BatteryInstalled";
        print "EXPECTED RESULT 1: Should get the BatteryInstalled successfully";
        print "ACTUAL RESULT 1: The BatteryInstalled is %s" %status[int(install)];
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	tdkTestObj = obj.createTestStep("CosaMTA_GetParamUlongValue");
        tdkTestObj.addParameter("handleType",0);
        tdkTestObj.addParameter("paramName","BatteryTotalCapacity");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        resultDetails = " ";
        resultDetails = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the BatteryTotalCapacity";
            print "EXPECTED RESULT 2: Should get the BatteryTotalCapacity successfully";
            print "ACTUAL RESULT 2: The BatteryTotalCapacity is %s" %resultDetails;
            if (install == '0' and int(resultDetails) == 0) or (install == '1' and int(resultDetails) > 0):
		tdkTestObj.setResultStatus("SUCCESS");
		print "BatteryTotalCapacity is within the expected range"
                print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
                tdkTestObj.setResultStatus("FAILURE");
                print "BatteryTotalCapacity is not within the expected range"
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the BatteryTotalCapacity";
            print "EXPECTED RESULT 2: Should get the BatteryTotalCapacity successfully";
            print "ACTUAL RESULT 2: Failed to get the BatteryTotalCapacity, Details : %s" %resultDetails;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the BatteryInstalled";
        print "EXPECTED RESULT 1: Should get the BatteryInstalled successfully";
        print "ACTUAL RESULT 1: Failed to get the BatteryInstalled, Details : %s" %resultDetails;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("cosamta");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
