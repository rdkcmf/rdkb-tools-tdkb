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
  <name>TS_WiFiMesh_EnableBandSteering_WithMeshEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if on enabling mesh, band steering parameter Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable gets disabled</synopsis>
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
    <test_case_id>TC_WIFIAGENT_77</test_case_id>
    <test_objective>Check if set operation to enable band steering parameter is failing when mesh is in enabled state</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable

Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode

Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable</input_parameters>
    <automation_approch>1. Load wifiagent module
2. Get and save the current LanMode
3. If it is bridge-static, change it to router, as while in bridge mode mesh cannot be enabled
4. Get and save current Mesh enable status
5. If mesh is not enabled, enable it
6. Try to enable band steering and check if the operation is failing
7. Revert the mesh enable state to original value
8. Revert lanmode to its original value
9. Unload wifiagent module</automation_approch>
    <expected_output>Set operation to enable band steering parameter should fail when mesh is in enabled state</expected_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_WiFiMesh_EnableBandSteering_WithMeshEnabled</test_script>
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
            print "ACTUAL RESULT : Lan mode is %s" %newValue;
            print "[TEST EXECUTION RESULT] : SUCCESS";
	    return "SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Get the current lanMode"
            print "EXPECTED RESULT : Should retrieve the current lanMode"
            print "ACTUAL RESULT :Lan mode is %s" %newValue;
            print "[TEST EXECUTION RESULT] : FAILURE";
	    return "FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Change lanmode to %s" %mode
        print "EXPECTED RESULT : Should change lanmode to %s" %mode
        print "ACTUAL RESULT :Details: %s " %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
	return "FAILURE"

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WiFiMesh_EnableBandSteering_WithMeshEnabled');

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
        print "ACTUAL RESULT 1:Lan mode is %s" %orgLanMode;
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
            print "ACTUAL RESULT 2: Initial Mesh State is %s" %orgState;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

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

            #Get the current band steering enable state
            tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable")
            tdkTestObj.executeTestCase("expectedresult");
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            orgBand = details.split("VALUE:")[1].split(' ')[0];

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 5: Get the current band steering enable state";
                print "EXPECTED RESULT 5: Should get the current band steering enable state";
                print "ACTUAL RESULT 5:  band steering status is %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Set the current band steering enable state as true and check if that operation is failing
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable")
                tdkTestObj.addParameter("paramValue","true")
                tdkTestObj.addParameter("paramType","boolean")
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult not in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 6: Enable Band steering when Mesh is in enabled state";
                    print "EXPECTED RESULT 6: Band steering enabling should fail when Mesh is in enabled state"
                    print "ACTUAL RESULT 6: Details: %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 6: Enable Band steering when Mesh is in enabled state";
                    print "EXPECTED RESULT 6: Band steering enabling should fail when Mesh is in enabled state"
                    print "ACTUAL RESULT 6: Details: %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                    #if band steering set was successful, revert the band steering enable state
                    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                    tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
                    tdkTestObj.addParameter("paramValue",orgBand)
                    tdkTestObj.addParameter("paramType","boolean")
                    tdkTestObj.executeTestCase("expectedresult");
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 7: Restore Enable state of Band steering";
                        print "EXPECTED RESULT 7: Should Restore Enable state of Band steering";
                        print "ACTUAL RESULT 7: Details %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 7: Restore Enable state of Band steering";
                        print "EXPECTED RESULT 7: Should Restore Enable state of Band steering";
                        print "ACTUAL RESULT 7: Details: %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 5: Get the current band steering enable state";
                print "EXPECTED RESULT 5: Should get the current band steering enable state";
                print "ACTUAL RESULT 5: Details %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            if orgState == "false":
                #Revert mesh state to previous one
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
                    print "TEST STEP 8: Restore Enable state of Mesh";
                    print "EXPECTED RESULT 8: Should Restore Enable state of Mesh";
                    print "ACTUAL RESULT 8: Details: %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 8: Restore Enable state of Mesh";
                    print "EXPECTED RESULT 8: Should Restore Enable state of Mesh";
                    print "ACTUAL RESULT 8: Details: %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the state of Mesh"
            print "EXPECTED RESULT 2: Failure in getting the state of Mesh"
            print "ACTUAL RESULT 2: Initial Mesh State is %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";

        if orgLanMode == "bridge-static":
            print "Revert lanmode to original value"
            status = setLanMode('bridge-static', obj)
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current lanMode"
        print "EXPECTED RESULT 1: Should retrieve the current lanMode"
        print "ACTUAL RESULT 1: Lan mode is %s" %orgLanMode;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
else:
        print "Failed to load wifi module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
