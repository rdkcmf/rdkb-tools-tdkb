##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <version>8</version>
  <name>TS_WiFiMesh_CheckOVSAndOpensync_WithOVSDisabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if OVS enable, Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable, and Opensync enable, Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Opensync is disabled after Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable alone is disabled from enabled state and rebooted.</synopsis>
  <groups_id/>
  <execution_time>20</execution_time>
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
    <test_case_id>TC_WIFIAGENT_225</test_case_id>
    <test_objective>To check if OVS enable, Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable, and Opensync enable, Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Opensync is disabled after Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable alone is disabled from enabled state and rebooted.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Ensure the OVS enable and Mesh Opensync enable are enabled as pre-requisite and device rebooted after that.</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable
paramValue : true/false
paramType : boolean
paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Opensync
paramValue : true/false
paramType : boolean</input_parameters>
    <automation_approch>1. Load the wifiagent module
2. Get the initial values of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable and Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Opensync and check if they are enabled initially as a pre-requisite.
3. Disable the OVS parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable alone.
4. Reboot the DUT.
5. Once the DUT comes up check the enable status of OVS enable and Mesh Opensync. Both should be in disabled state.
6. Revert operation is not required as the initial state before setting the pre-requisites is not known.
7. Unload the wifiagent module.</automation_approch>
    <expected_output>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable, and Opensync enable, Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Opensync should be disabled after Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable alone is disabled from enabled state and rebooted.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WiFiMesh_CheckOVSAndOpensync_WithOVSDisabled</test_script>
    <skipped>No</skipped>
    <release_version>M105</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkutility import *;

#Test component to be tested
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
wifiobj.configureTestCase(ip,port,'TS_WiFiMesh_CheckOVSAndOpensync_WithOVSDisabled');

#Get the result of connection with test component and DUT
loadmodulestatus1=wifiobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    wifiobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    print "\n**********Pre-Requites Check Start**********";
    #Get the initial OVS enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable and Opensync Enable using Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Opensync
    step = 1;
    initial_enable = [];
    status = 0;
    paramList =["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable", "Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Opensync"];
    print "\nTEST STEP %d: Get the initial OVS and Opensync enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable and Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Opensync" %step;
    print "EXPECTED RESULT %d: Should successfully get the initial value of OVS and Opensync enable" %step;

    for param in paramList:
        tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
        tdkTestObj.addParameter("paramName",param)
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        if expectedresult in actualresult and details != "":
            tdkTestObj.setResultStatus("SUCCESS");
            enable = details.split("VALUE:")[1].split(" ")[0].strip();
            initial_enable.append(enable);
            print "\n%s : %s" %(param, enable);
        else:
            status = 1;
            tdkTestObj.setResultStatus("FAILURE");
            print "\n%s : %s" %(param, details);

    if status == 0 :
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Initial enable state for OVS : %s, Opensync : %s" %(step, initial_enable[0], initial_enable[1]);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check if OVS and Opensync and enabled initially
        step = step + 1;
        print "\nTEST STEP %d: Check if OVS and Opensync are enabled as pre-requisite" %step;
        print "EXPECTED RESULT %d: OVS and Opensync should be enabled as pre-requisite" %step;

        if initial_enable[0] == "true" and initial_enable[1] == "true":
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: OVS and Opensync are enabled as pre-requisites" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            print "\n**********Pre-Requites Check Complete**********";

            #Disable OVS
            step = step + 1;
            setValue = "false";
            print "\nTEST STEP %d: Disable OVS using %s" %(step, paramList[0]);
            print "EXPECTED RESULT %d: %s should be disabled successfully" %(step, paramList[0]);

            tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set_Get');
            tdkTestObj.addParameter("paramName",paramList[0]);
            tdkTestObj.addParameter("paramValue",setValue);
            tdkTestObj.addParameter("paramType","boolean");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: OVS disabled successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Reboot the DUT for the RFC to take effect
                print "\nInitiating Reboot...";
                wifiobj.initiateReboot();
                print "Sleeping for 300s..."
                sleep(300);

                #Get the current OVS and Opensync enable status
                final_enable = [];
                status = 0;
                print "\nTEST STEP %d: Get the current OVS and Opensync enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable and Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Opensync" %step;
                print "EXPECTED RESULT %d: Should successfully get the current value of OVS and Opensync enable" %step;

                for param in paramList:
                    tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
                    tdkTestObj.addParameter("paramName",param)
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    if expectedresult in actualresult and details != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        enable = details.split("VALUE:")[1].split(" ")[0].strip();
                        final_enable.append(enable);
                        print "\n%s : %s" %(param, enable);
                    else:
                        status = 1;
                        tdkTestObj.setResultStatus("FAILURE");
                        print "\n%s : %s" %(param, details);

                if status == 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Current enable state for OVS : %s, Opensync : %s" %(step, final_enable[0], final_enable[1]);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Check if both OVS and Opensync are in disabled state after OVS is disabled and DUT is rebooted
                    if final_enable[0] == "false" and final_enable[1] == "false":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "OVS and Opensync are in disabled state post reboot";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "OVS and Opensync are NOT in disabled state post reboot";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Current enable state for OVS and Opensync NOT retrieved successfully" %(step);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: OVS NOT disabled successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: OVS and Opensync are NOT enabled as pre-requisites" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
            print "\n**********Pre-Requites Check Complete**********";
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Initial enable states for OVS and Opensync NOT retrieved successfully" %(step);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    wifiobj.unloadModule("wifiagent")
else:
    print "Failed to load module";
    wifiobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
