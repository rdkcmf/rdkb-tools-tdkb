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
  <version>2</version>
  <name>TS_WiFiMesh_CheckEnableStatus_WithBridgeMode</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if on enabling bridge mode the mesh enable state changes to disable</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_WIFIAGENT_75</test_case_id>
    <test_objective>Check if on enabling bridge mode the mesh enable state changes to disable</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable

Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode</input_parameters>
    <automation_approch>1. Load wifiagent module
2. Get and save the current LanMode
3. If it is bridge-static, change it to router, as while in bridge mode mesh cannot be enabled
4. Get and save current Mesh enable status
5. If mesh is not enabled, enable it
6. Enable bridge mode
7. Check if mesh got disabled on enabling bridge mode
8. Disable bridge mode to do the set operation to revert mesh state to its original value
9. Revert the mesh enable state to original value
10. Revert lanmode to its original value
11. Unload wifiagent module</automation_approch>
    <expected_output>On enabling bridge mode the mesh enable state should change to disable</expected_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_WiFiMesh_CheckEnableStatus_WithBridgeMode</test_script>
    <skipped>No</skipped>
    <release_version>M74</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

def setLanMode(mode, obj):

    expectedresult = "SUCCESS"
    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    tdkTestObj.addParameter("paramValue", mode)
    tdkTestObj.addParameter("paramType","string")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP : Change lanmode to %s" %mode
        print "EXPECTED RESULT : Should change lanmode to %s" %mode
        print "ACTUAL RESULT : Details: %s " %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        sleep(90)

        tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        newValue = details.split("VALUE:")[1].split(' ')[0];

        if expectedresult in actualresult and newValue==mode:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP : Get the current lanMode"
            print "EXPECTED RESULT : Should retrieve the current lanMode"
            print "ACTUAL RESULT : Lannmode is %s" %newValue;
            print "[TEST EXECUTION RESULT] : SUCCESS";
	    return "SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Get the current lanMode"
            print "EXPECTED RESULT : Should retrieve the current lanMode"
            print "ACTUAL RESULT : Lanmode is %s" %newValue;
            print "[TEST EXECUTION RESULT] : FAILURE";
	    return "FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Change lanmode to %s" %mode
        print "EXPECTED RESULT : Should change lanmode to %s" %mode
        print "ACTUAL RESULT : Details: %s " %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
	return "FAILURE"

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WiFiMesh_CheckEnableStatus_WithBridgeMode');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    orgLanMode = details.split("VALUE:")[1].split(' ')[0];

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the current lanMode"
        print "EXPECTED RESULT 1: Should retrieve the current lanMode"
        print "ACTUAL RESULT 1: Lanmode is %s" %orgLanMode;
        print "[TEST EXECUTION RESULT] : SUCCESS";

	#if bridge mode is enabled, disable it before trying to enable mesh
	if "bridge-static" == orgLanMode:
	    actualresult = setLanMode("router", obj)
            if expectedresult not in actualresult:
                print "Failed to disable bridge mode, cannot enable mesh in bridge mode, exiting script..."
                obj.unloadModule("wifiagent");
                exit()

        tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")

        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the Mesh enable state";
            print "EXPECTED RESULT 2: Should get the Mesh enable state";
            orgState = details.split("VALUE:")[1].split(' ')[0];
            print "ACTUAL RESULT 2: Initial mesh state is %s" %orgState;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    #if mesh status is not enabled now, enable it first and see if it gets disabled in bridge mode
            if orgState == "false":
                #Enable Mesh and check its status
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
                tdkTestObj.addParameter("paramValue","true")
                tdkTestObj.addParameter("paramType","boolean")
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Enable Mesh";
                    print "EXPECTED RESULT 3: Should enable Mesh"
                    print "ACTUAL RESULT 3: Mesh state is %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

		    sleep(40);
                    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                    tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
                    tdkTestObj.executeTestCase("expectedresult");
	            actualresult = tdkTestObj.getResult();
        	    details = tdkTestObj.getResultDetails();
                    status = details.split("VALUE:")[1].split(' ')[0];

	            if expectedresult in actualresult and "true" == status:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4: Check if Mesh status is enabled";
                        print "EXPECTED RESULT 4: Mesh status should be enabled";
                        print "ACTUAL RESULT 4: Mesh Status is %s" %status;
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Check if Mesh status is enabled";
                        print "EXPECTED RESULT 4: Mesh status should be enabled";
                        print "ACTUAL RESULT 4: Mesh Status is %s " %status;
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Enable Mesh";
                    print "EXPECTED RESULT 3: Should enable Mesh"
                    print "ACTUAL RESULT 3: Mesh state is %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            	    obj.unloadModule("wifiagent");
                    exit()

	    #Enable bridge mode and check if mesh gets disabled
	    status = setLanMode("bridge-static", obj);
	    if expectedresult in status:
                #check if Mesh got disabled
                tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                status = details.split("VALUE:")[1].split(' ')[0];

                if expectedresult in actualresult and "false" in status:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Check if Mesh is in disabled state"
                    print "EXPECTED RESULT 5: Mesh should be in disabled state"
                    print "ACTUAL RESULT 5: Mesh Status is %s " %status;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Check if Mesh status is in disabled state"
                    print "EXPECTED RESULT 5: Mesh should be in disabled state"
                    print "ACTUAL RESULT 5: Status is %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

		print"Disable Bridge mode to revert the Mesh enable state to its original value"
		status = setLanMode("router", obj);
		if expectedresult in status:
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
                        print "TEST STEP 6: Restore Enable state of Mesh";
                        print "EXPECTED RESULT 6: Should Restore Enable state of Mesh";
                        print "ACTUAL RESULT 6: Details: %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 6: Restore Enable state of Mesh";
                        print "EXPECTED RESULT 6: Should Restore Enable state of Mesh";
                        print "ACTUAL RESULT 6: Details: %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
		else:
		    print "Failed to disable bridge mode. Cannot revert mesh enable state"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the state of Mesh"
            print "EXPECTED RESULT 2: Failure in getting the state of Mesh"
            print "ACTUAL RESULT 2: Initial mesh state is %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";

        if orgLanMode == "bridge-static":
            print "Revert lanmode to original value"
            status = setLanMode('bridge-static', obj)
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current lanMode"
        print "EXPECTED RESULT 1: Should retrieve the current lanMode"
        print "ACTUAL RESULT 1: Lanmode is %s" %orgLanMode;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
else:
        print "Failed to load wifi module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
