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
  <name>TS_WiFiMesh_CheckDisableStatus</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>On disabling Mesh check if the value of Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Status becomes Off</synopsis>
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
    <test_case_id>TC_WIFIAGENT_73</test_case_id>
    <test_objective>On disabling Mesh check if the value of Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Status becomes Off</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable

Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Status</input_parameters>
    <automation_approch>1. Load wifiagent module
2. Get and save current Mesh enable status
3. If mesh is not disabled, disable it
4. Check if the mesh status has become Off
5. Revert the mesh enable state to original value
6. Unload wifiagent module</automation_approch>
    <expected_output>On disabling Mesh, the value of Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Status should become Off</expected_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_WiFiMesh_CheckDisableStatus</test_script>
    <skipped>No</skipped>
    <release_version>M74</release_version>
    <remarks>None</remarks>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_WiFiMesh_CheckDisableStatus');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Prmitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Mesh enable state";
        print "EXPECTED RESULT 1: Should get the Mesh enable state";
        orgState = details.split("VALUE:")[1].split(' ')[0];
        print "ACTUAL RESULT 1: Initial mesh state is %s" %orgState;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if orgState == "true":
            #Disable Mesh and check its status
            tdkTestObj = obj.createTestStep('WIFIAgent_Set');
            tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
            tdkTestObj.addParameter("paramValue","false")
            tdkTestObj.addParameter("paramType","boolean")
            tdkTestObj.executeTestCase("expectedresult");
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Disable Mesh";
                print "EXPECTED RESULT 2: Should disable Mesh"
                print "ACTUAL RESULT 2: Mesh state is %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
		sleep(30)

            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Disable Mesh";
                print "EXPECTED RESULT 2: Should disable Mesh"
                print "ACTUAL RESULT 2: Mesh state is %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
		obj.unloadModule("wifiagent");
                exit()

        #check if Mesh status is Off
        tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Status")
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        status = details.split("VALUE:")[1].split(' ')[0];

        if expectedresult in actualresult and "Off" in status:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Check if Mesh status is Off";
            print "EXPECTED RESULT 3: Mesh status should be Off";
            print "ACTUAL RESULT 3: Mesh Status is %s " %status;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 3: Check if Mesh status is Off";
            print "EXPECTED RESULT 3: Mesh status should be Off";
            print "ACTUAL RESULT 3: Status is %s " %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        if orgState == "true":
            #change mesh state to previous one
            tdkTestObj = obj.createTestStep('WIFIAgent_Set');
            tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
            tdkTestObj.addParameter("paramValue",orgState)
            tdkTestObj.addParameter("paramType","boolean")
            tdkTestObj.executeTestCase("expectedresult");
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Restore Enable state of Mesh";
                print "EXPECTED RESULT 4: Should Restore Enable state of Mesh";
                print "ACTUAL RESULT 4: Detail: %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Restore Enable state of Mesh";
                print "EXPECTED RESULT 4: Should Restore Enable state of Mesh";
                print "ACTUAL RESULT 4: Details: %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the state of Mesh"
        print "EXPECTED RESULT 1: Failure in getting the state of Mesh"
        print "ACTUAL RESULT 1: Initial mesh state is %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
else:
        print "Failed to load wifi module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
