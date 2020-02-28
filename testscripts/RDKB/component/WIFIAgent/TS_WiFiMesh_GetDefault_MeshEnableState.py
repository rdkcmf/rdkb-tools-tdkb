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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WiFiMesh_GetDefault_MeshEnableState</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if the default value of mesh enable state is false</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <test_case_id>TC_WIFIAGENT_79</test_case_id>
    <test_objective>Check if the default value of mesh enable state is false</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.FactoryReset

Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable

Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode</input_parameters>
    <automation_approch>1. Load wifiagent module
2. Get and save the current LanMode
3. If it is bridge-static, change it to router, as while in bridge mode mesh cannot be enabled
4. Get and save current Mesh enable status
5. If mesh is not enabled, enable it
6. Do factory reset of the device
7. After factory reset check if mesh enable status became false
8. Revert the mesh enable state to original value
9. Revert lanmode to its original value
10. Unload wifiagent module</automation_approch>
    <expected_output>The default value of mesh enable state should be false</expected_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_WiFiMesh_GetDefault_MeshEnableState</test_script>
    <skipped>No</skipped>
    <release_version>M74</release_version>
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
            print "ACTUAL RESULT : Lanmode is %s" %newValue;
            print "[TEST EXECUTION RESULT] : SUCCESS";
	    return "SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Get the current lanMode"
            print "EXPECTED RESULT : Should retrieve the current lanMode"
            print "ACTUAL RESULT :Lanmode is %s" %newValue;
            print "[TEST EXECUTION RESULT] : FAILURE";
	    return "FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Change lanmode to %s" %mode
        print "EXPECTED RESULT : Should change lanmode to %s" %mode
        print "ACTUAL RESULT : Details: %s " %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
	return "FAILURE"

obj.configureTestCase(ip,port,'TS_WiFiMesh_GetDefault_MeshEnableState');

#Get the result of connection with test component and DUT
result =obj.getLoadModuleResult();
loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
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
        print "ACTUAL RESULT 1:Lanmode is %s" %orgLanMode;
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

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        meshOrg = tdkTestObj.getResultDetails().split("VALUE:")[1].split(' ')[0];

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the enable status of WiFi Mesh";
            print "EXPECTED RESULT 2: Should get the enable status of WiFi Mesh";
            print "ACTUAL RESULT 2: Initial Mesh Enable is %s" %meshOrg;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if meshOrg == "false":
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
                tdkTestObj.addParameter("paramValue", "true");
                tdkTestObj.addParameter("paramType","boolean");

                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                newMesh = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: If current enable state is false, set it as true";
                    print "EXPECTED RESULT 3: Should set the enable status of WiFi Mesh as true";
                    print "ACTUAL RESULT 3: WiFi Mesh set is success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: If current enable state is false, set it as true";
                    print "EXPECTED RESULT 3: Should set the enable status of WiFi Mesh as true";
                    print "ACTUAL RESULT 3: WiFi Mesh set is success"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
             	    obj.unloadModule("wifiagent");
                    exit();

            #save device's current state before it goes for reboot
            obj.saveCurrentState();

            #Initiate Factory reset before checking the default value
            tdkTestObj = obj.createTestStep('WIFIAgent_Set');
            tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
            tdkTestObj.addParameter("paramValue","Router,Wifi,VoIP,Dect,MoCA");
            tdkTestObj.addParameter("paramType","string");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Initiate factory reset ";
                print "EXPECTED RESULT 4: Should inititate factory reset";
                print "ACTUAL RESULT 4: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Restore the device state saved before reboot
                obj.restorePreviousStateAfterReboot();

                tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        	tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")

          	tdkTestObj.executeTestCase(expectedresult);
        	actualresult = tdkTestObj.getResult();
        	newMesh = tdkTestObj.getResultDetails().split("VALUE:")[1].split(' ')[0];

        	if expectedresult in actualresult and newMesh == "false":
        	    #Set the result status of execution
        	    tdkTestObj.setResultStatus("SUCCESS");
        	    print "TEST STEP 5: Get the enable status of WiFi Mesh after factory reset";
        	    print "EXPECTED RESULT 5: Should get the default enable status of WiFi Mesh as false"
        	    print "ACTUAL RESULT 5: Default WiFi Mesh Enable status is %s" %newMesh;
        	    #Get the result of execution
        	    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
            	#Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Get the enable status of WiFi Mesh after factory reset";
                    print "EXPECTED RESULT 5: Should get the default enable status of WiFi Mesh as false";
                    print "ACTUAL RESULT 5: Default WiFi Mesh Enable status is %s" %newMesh;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
                tdkTestObj.addParameter("paramValue",meshOrg);
                tdkTestObj.addParameter("paramType","boolean");

                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 6: Revert  enable status of WiFi Mesh same as previous status";
                    print "EXPECTED RESULT 6: Should revert the enable status of WiFi Mesh same as previous status";
                    print "ACTUAL RESULT 6: WiFi Mesh revert is success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 6: Revert  enable status of WiFi Mesh same as previous status";
                    print "EXPECTED RESULT 6: Should revert the enable status of WiFi Mesh same as previous status";
                    print "ACTUAL RESULT 6: WiFi Mesh revert failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Initiate factory reset ";
                print "EXPECTED RESULT 3: Should inititate factory reset";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the enable status of WiFi Mesh";
            print "EXPECTED RESULT 2: Should get the enable status of WiFi Mesh";
            print "ACTUAL RESULT 2: Initial Mesh status is %s" %meshOrg;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

            if orgLanMode == "bridge-static":
                print "Revert LanMode to original value"
                status = setLanMode('bridge-static', obj)
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current lanMode"
        print "EXPECTED RESULT 1: Should retrieve the current lanMode"
        print "ACTUAL RESULT 1:Lanmode is %s" %orgLanMode;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

