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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_XHS2.4GHZ_EnableAdvertisement</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Test to enable XHS 2.4GHZ SSID's advertisement with SSID enabled</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIAGENT_90</test_case_id>
    <test_objective>Test to enable XHS 2.4GHZ SSID's advertisement with SSID enabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.WiFi.SSID.3.Enable
Device.WiFi.AccessPoint.3.SSIDAdvertisementEnabled</input_parameters>
    <automation_approch>1. Load wifiagent module
2.Get and save the enable state of XHS 2.4GHZ SSID
3. If not enabled, enable it
4. Get and save the SSID advertisement state of  XHS 2.4GHZ SSID
5. Enable the  SSID advertisement state of  XHS 2.4GHZ SSID using set
6. Verify the set operation was success using get
7. Revert enable state and Advertisement status of XHS 2.4GHZ SSID to its original values
8. Unload wifiagent module</automation_approch>
    <expected_output>Should successfully enable XHS 2.4 SSID advertisement after enabling that SSID</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_XHS2.4GHZ_EnableAdvertisement</test_script>
    <skipped>No</skipped>
    <release_version>M75</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_XHS2.4GHZ_EnableAdvertisement');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");
        expectedresult="SUCCESS";

        tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.WiFi.SSID.3.Enable")

        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the XHS enable state";
            print "EXPECTED RESULT 1: Should get the XHS enable state";
            orgState = details.split("VALUE:")[1].split(' ')[0];
            print "ACTUAL RESULT 1: Initial XHS state is %s" %orgState;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if orgState == "false":
                #Enable 2.4GHZ SSID
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.WiFi.SSID.3.Enable")
                tdkTestObj.addParameter("paramValue","true")
                tdkTestObj.addParameter("paramType","boolean")
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Enable XHS 2.4GHZ SSID";
                    print "EXPECTED RESULT 2: Should enable  XHS 2.4GHZ SSID";
                    print "ACTUAL RESULT 2: XHS 2.4GHZ SSID enable state is %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

		    sleep(20);
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 2: Enable XHS 2.4GHZ SSID";
                    print "EXPECTED RESULT 2: Should enable XHS 2.4GHZ SSID";
                    print "ACTUAL RESULT 2: XHS 2.4GHZ SSID state is %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    obj.unloadModule("wifiagent");
                    exit()

            tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.3.SSIDAdvertisementEnabled")
            tdkTestObj.executeTestCase("expectedresult");
	    actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            orgAdv = details.split("VALUE:")[1].split(' ')[0];

	    if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get XHS 2.4GHZ SSIDAdvertisement status";
                print "EXPECTED RESULT 3: Should get XHS 2.4GHZ SSIDAdvertisement status"
                print "ACTUAL RESULT 3: Status is %s" %orgAdv;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.3.SSIDAdvertisementEnabled")
                tdkTestObj.addParameter("paramValue","true")
                tdkTestObj.addParameter("paramType","boolean")
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Enable XHS 2.4GHZ SSIDAdvertisement";
                    print "EXPECTED RESULT 4: Should enable  XHS 2.4GHZ SSIDAdvertisement";
                    print "ACTUAL RESULT 4: XHS 2.4GHZ SSIDAdvertisement state is %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

	            sleep(20);
                    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.3.SSIDAdvertisementEnabled")
                    tdkTestObj.executeTestCase("expectedresult");
	            actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    newAdv = details.split("VALUE:")[1].split(' ')[0];

	            if expectedresult in actualresult and newAdv == "true":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Check if XHS 2.4GHZ SSIDAdvertisement is enabled";
                        print "EXPECTED RESULT 5: XHS 2.4GHZ SSIDAdvertisement should be enabled";
                        print "ACTUAL RESULT 5: XHS 2.4GHZ SSIDAdvertisement Status is %s" %newAdv;
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Check if XHS 2.4GHZ SSIDAdvertisement is enabled";
                        print "EXPECTED RESULT 5:  XHS 2.4GHZ SSIDAdvertisement should be enabled";
                        print "ACTUAL RESULT 5: XHS 2.4GHZ SSIDAdvertisement Status is %s" %newAdv;
                        print "[TEST EXECUTION RESULT] : FAILURE";

                    #change XHS SSID Advertisement to previous value
                    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.3.SSIDAdvertisementEnabled")
                    tdkTestObj.addParameter("paramValue",orgAdv)
                    tdkTestObj.addParameter("paramType","boolean")
                    tdkTestObj.executeTestCase("expectedresult");
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 6: Restore XHS 2.4GHZ SSIDAdvertisement state"
                        print "EXPECTED RESULT 6: Should Restore XHS 2.4GHZ SSIDAdvertisement state"
                        print "ACTUAL RESULT 6: Details: %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 6: Restore XHS 2.4GHZ SSIDAdvertisement state"
                        print "EXPECTED RESULT 6: Should Restore XHS 2.4GHZ SSIDAdvertisement state"
                        print "ACTUAL RESULT 6: Details: %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Enable XHS 2.4GHZ SSIDAdvertisement state"
                    print "EXPECTED RESULT 4: Should enable XHS 2.4GHZ SSIDAdvertisement state"
                    print "ACTUAL RESULT 4: XHS 2.4GHZ SSID Advertisement state is %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the XHS 2.4GHZ SSIDAdvertisement state"
                print "EXPECTED RESULT 3: Should Get the XHS 2.4GHZ SSIDAdvertisement state"
                print "ACTUAL RESULT 3: Failed to get XHS 2.4GHZ SSIDAdvertisement. State is %s" %details;
                print "[TEST EXECUTION RESULT] : FAILURE";

            #change XHS SSID state to previous one
            tdkTestObj = obj.createTestStep('WIFIAgent_Set');
            tdkTestObj.addParameter("paramName","Device.WiFi.SSID.3.Enable")
            tdkTestObj.addParameter("paramValue",orgState)
            tdkTestObj.addParameter("paramType","boolean")
            tdkTestObj.executeTestCase("expectedresult");
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Restore Enable state of XHS 2.4GHZ";
                print "EXPECTED RESULT 2: Should Restore Enable state of XHS 2.4GHZ";
                print "ACTUAL RESULT 2: Details: %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Restore Enable state of XHS 2.4GHZ";
                print "EXPECTED RESULT 2: Should Restore Enable state of XHS 2.4GHZ";
                print "ACTUAL RESULT 2: Details: %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the state of XHS 2.4GHZ SSID";
            print "EXPECTED RESULT 1: Should  Get the state of XHS 2.4GHZ SSID"
            print "ACTUAL RESULT 1: Failure in getting the enable state of XHS 2.4GHZ SSID. State is %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";


        obj.unloadModule("wifiagent");
else:
        print "Failed to load wifi module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
