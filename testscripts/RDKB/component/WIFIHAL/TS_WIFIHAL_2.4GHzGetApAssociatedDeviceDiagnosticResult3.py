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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzGetApAssociatedDeviceDiagnosticResult3</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetApAssociatedDeviceDiagnosticResult3</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>This test script is to find the AP associated device details of 2.4ghz using wifi_getApAssociatedDeviceDiagnosticResult3()</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_340</test_case_id>
    <test_objective>This test script is to find the AP associated device details of 2.4ghz using wifi_getApAssociatedDeviceDiagnosticResult3()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script
3.At least one device should be connected to get details.</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDeviceDiagnosticResult3()</api_or_interface_used>
    <input_parameters>apIndex = 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Get the Ap Associated Device Diagnostic Result3 of wifihal
3. Print the  Device Diagnostic Result3 details
4. Unload wifihal module</automation_approch>
    <expected_output>It should return output_array_size, which will give the no associated device and the Device Diagnostic Result3 details</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetApAssociatedDeviceDiagnosticResult3</test_script>
    <skipped>No</skipped>
    <release_version>M69</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
radio2 = "2.4G"
#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetApAssociatedDeviceDiagnosticResult3');

#Get the result of connection with test component and STB

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Validate wifi_getApAssociatedDeviceDiagnosticResult2() for 2.4GHZ
    tdkTestObjTemp, idx = getIndex(obj, radio2);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio2;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Prmitive test case which is associated to this Script
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDeviceDiagnosticResult3');
        tdkTestObj.addParameter("apIndex", idx);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "Details: %s"%details

        if expectedresult in actualresult :
           details = details.split(":")[1].strip();
           output_array_size = details.split("=")[1].split(",")[0].strip();
           if int(output_array_size) > 0:
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP : Get the ApAssociatedDeviceDiagnosticResult3"
              print "EXPECTED RESULT : Should successfully get the ApAssociatedDeviceDiagnosticResult3"
              print "ACTUAL RESULT : Successfully gets the ApAssociatedDeviceDiagnosticResult3"
              print "output_array_size=",output_array_size
              #print "Identified %s neighboring access points"%output_array_size
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "EXPECTED RESULT : Should successfully get the ApAssociatedDeviceDiagnosticResult3"
               print "ACTUAL RESULT : No associated device found";
               print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Get the ApAssociatedDeviceDiagnosticResult3"
            print "EXPECTED RESULT : Should successfully get the ApAssociatedDeviceDiagnosticResult3"
            print "ACTUAL RESULT : Failed to get the ApAssociatedDeviceDiagnosticResult3"
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
