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
  <name>TS_EPONHAL_GetDeviceSysDescrInfo</name>
  <primitive_test_id/>
  <primitive_test_name>EPONHAL_GetDeviceSysDescrInfo</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check the value of VendorName, ModelNumber, HardwareVersion using dpoe_getDeviceSysDescrInfo()</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_EPONHAL_8</test_case_id>
    <test_objective>Get and check the value of VendorName, ModelNumber, HardwareVersion using dpoe_getDeviceSysDescrInfo()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>dpoe_getDeviceSysDescrInfo</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load eponhal module
2. Invoke dpoe_getDeviceSysDescrInfo() and get the DeviceSysDescrInfo
3. In DeviceSysDescrInfo check if the values for VendorName, ModelNumber, HardwareVersion are non-empty
3. Unload eponhal module</automation_approch>
    <expected_output>Check if the VendorName, ModelNumber, HardwareVersion are non-empty</expected_output>
    <priority>High</priority>
    <test_stub_interface>EPONHAL</test_stub_interface>
    <test_script>TS_EPONHAL_GetDeviceSysDescrInfo</test_script>
    <skipped>No</skipped>
    <release_version>M73</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("eponhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_EPONHAL_GetDeviceSysDescrInfo');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep('EPONHAL_GetDeviceSysDescrInfo');
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    resultDetails = " ";
    resultDetails = tdkTestObj.getResultDetails();

    if expectedresult in actualresult  :
        #From the dpoe_getDeviceSysDescrInfo() output, retrieve VendorName, ModelNumber, HardwareVersion
        vendorName = resultDetails.split(':')[1].split(',')[0].strip()
        modelNumber=resultDetails.split(':')[2].split(',')[0].strip()
        hardwareVersion=resultDetails.split(':')[3].strip()

        #Check if VendorName, ModelNumber, HardwareVersion are non-empty
        if vendorName and modelNumber and hardwareVersion:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1 : Get the VendorName, ModelNumber, HardwareVersion and check if they are non-empty";
            print "EXPECTED RESULT 1 : Should get the VendorName, ModelNumber, HardwareVersion value as non-empty";
            print "ACTUAL RESULT 1:  %s" %resultDetails;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] 1: SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the VendorName, ModelNumber, HardwareVersion and check if they are non-empty";
            print "EXPECTED RESULT 1: Should get the VendorName, ModelNumber, HardwareVersion value are non-empty";
            print "ACTUAL RESULT 1:  %s" %resultDetails;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] 1: FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Get the DeviceSysDescrInfo";
        print "EXPECTED RESULT : Should get the DeviceSysDescrInfo successfully";
        print "ACTUAL RESULT : Failed to get the DeviceSysDescrInfo, Details : %s" %resultDetails;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("eponhal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
