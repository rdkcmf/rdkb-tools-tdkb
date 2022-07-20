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
  <version>4</version>
  <name>TS_SANITY_CheckBrlan0MACAddressOnLanModeTransition_WithOVSEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the Brlan0 interface Mac Address remains unchanged when the Lan Mode is transitioned from router to bridge-static or vice-versa when the OVS Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable is enabled.</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_SANITY_72</test_case_id>
    <test_objective>To check if the Brlan0 interface Mac Address remains unchanged when the Lan Mode is transitioned from router to bridge-static or vice-versa when the OVS Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable is enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable
paramValue : true/false
paramType : boolean
paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
paramValue : router/bridge-static
paramType : string</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial enable state of OVS enable Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable.
3. If its not enabled initially, set Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable to true.
4. Reboot the DUT for the OVS Enable RFC to take effect
5. Once the DUT is up, check if the OVS RFC is successfully enabled
6. Get the initial Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
7. Get the brlan0 interface mac address
8. Toggle the lan mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode and validate with GET operation.
9. Get the brlan0 interface mac address in the new lan mode
10. Compare the mac addresses, it should remain same.
11. Revert the lan mode to initial value
12. Revert the OVS enable state and reboot the DUT if required.
13. Unload the modules</automation_approch>
    <expected_output>The Brlan0 interface Mac Address should remain unchanged when the Lan Mode is transitioned from router to bridge-static or vice-versa when the OVS Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable is enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckBrlan0MACAddressOnLanModeTransition_WithOVSEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M103</release_version>
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
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_SANITY_CheckBrlan0MACAddressOnLanModeTransition_WithOVSEnabled');
tr181obj.configureTestCase(ip,port,'TS_SANITY_CheckBrlan0MACAddressOnLanModeTransition_WithOVSEnabled');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if  "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Get the initial OVS enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable
    step = 1;
    paramName ="Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable";
    tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    actualresult, initial_enable = getTR181Value(tdkTestObj, paramName);

    print "\nTEST STEP %d: Get the initial OVS Enable state using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable" %step;
    print "EXPECTED RESULT %d: Should successfully get the initial value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable" %step;

    if expectedresult in actualresult and initial_enable != "":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Initial Enable state is : %s" %(step, initial_enable);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #If OVS is not enabled initially, enable it
        proceed_flag = 0;
        revert_flag = 0;
        setValue = "true";

        if initial_enable != "true":
            step = step + 1;
            tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
            actualresult, details = setTR181Value(tdkTestObj, paramName, setValue, "boolean");
            print "\nTEST STEP %d : Set OVS Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable to %s" %(step, setValue);
            print "EXPECTED RESULT %d : Should set the OVS Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable to %s" %(step, setValue);

            if expectedresult in actualresult and details != "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Reboot the DUT for the RFC to take effect
                print "\nInitiating Reboot...";
                sysobj.initiateReboot();
                print "Sleeping for 300s..."
                sleep(300);

                #Check if the OVS RFC is set successfully
                step = step + 1;
                tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get');
                actualresult, curr_enable = getTR181Value(tdkTestObj, paramName);

                print "\nTEST STEP %d: Get the current OVS Enable state using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable" %step;
                print "EXPECTED RESULT %d: Should successfully get the current value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable" %step;

                if expectedresult in actualresult and curr_enable != "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Current Enable state is : %s" %(step, curr_enable);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if curr_enable == setValue:
                        proceed_flag = 1;
                        revert_flag = 1;
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "OVS Enable is successfully set to %s" %setValue;
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "OVS Enable is NOT successfully set to %s" %setValue;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Current Enable state is : %s" %(step, curr_enable);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else :
            print "OVS is already in enabled state, SET operation not required";
            proceed_flag = 1;

        if proceed_flag == 1:
            #Check the Lan Mode
            step = step + 1;
            paramName1 ="Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode";
            tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get');
            actualresult, initial_mode = getTR181Value(tdkTestObj, paramName1);

            print "\nTEST STEP %d: Get the initial Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
            print "EXPECTED RESULT %d: Should successfully get the initial value of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;

            if expectedresult in actualresult and initial_mode != "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Initial Lan mode is : %s" %(step, initial_mode);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Get the brlan0 MAC address
                step = step + 1;
                cmd= "ifconfig brlan0 | grep \"HWaddr\"";
                print "\nCommand : ", cmd;
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                print "\nTEST STEP %d : Get the Brlan0 Mac Address when the Lan Mode is %s" %(step, initial_mode);
                print "EXPECTED RESULT %d : Should get the Brlan0 Mac Address successfully when the Lan Mode is %s" %(step, initial_mode);

                if expectedresult in actualresult and details != "":
                    brlan0_mac_initial = details.strip().split("HWaddr ")[1];
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Brlan0 Mac Address is : %s" %(step, brlan0_mac_initial);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Change the Lan Mode
                    step = step + 1;
                    setmode = "";
                    if initial_mode == "router":
                        setmode = "bridge-static";
                    else :
                        setmode = "router";

                    print "\nTEST STEP %d : Set Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to %s" %(step, setmode);
                    print "EXPECTED RESULT %d : Should set Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to %s" %(step, setmode);
                    tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
                    actualresult, details = setTR181Value(tdkTestObj, paramName1, setmode, "string");
                    sleep(120);

                    if expectedresult in actualresult and details != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Cross check with GET operation
                        step = step + 1;
                        sleep(20);
                        tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get');
                        actualresult, curr_mode = getTR181Value(tdkTestObj, paramName1);

                        print "\nTEST STEP %d: Get the current Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
                        print "EXPECTED RESULT %d: Should successfully get the current value of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;

                        if expectedresult in actualresult and curr_mode != "":
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Current Lan mode is : %s" %(step, curr_mode);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            if curr_mode == setmode :
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "Lan Mode changed successfully";

                                #Get the brlan0 MAC address
                                step = step + 1;
                                cmd= "ifconfig brlan0 | grep \"HWaddr\"";
                                print "\nCommand : ", cmd;
                                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                                actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                                print "\nTEST STEP %d : Get the Brlan0 Mac Address when the Lan Mode is %s" %(step, curr_mode);
                                print "EXPECTED RESULT %d : Should get the Brlan0 Mac Address successfully when the Lan Mode is %s" %(step, curr_mode);

                                if expectedresult in actualresult and details != "":
                                    brlan0_mac_final = details.strip().split("HWaddr ")[1];
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: Brlan0 Mac Address is : %s" %(step, brlan0_mac_final);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

                                    #Compare the mac addresses and see if they are the same
                                    step = step + 1;
                                    print "\nTEST STEP %d : Check if the Brlan0 Mac Address remain unchanged irrespective of the Lan Mode" %(step);
                                    print "EXPECTED RESULT %d : The Brlan0 Mac Address should remain unchanged irrespective of the Lan Mode" %(step);
                                    print "Brlan0 Mac Address when Lan Mode is %s with OVS Enabled : %s" %(initial_mode, brlan0_mac_initial);
                                    print "Brlan0 Mac Address when Lan Mode is %s with OVS Enabled : %s" %(curr_mode, brlan0_mac_final);

                                    if brlan0_mac_final == brlan0_mac_initial:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT %d: Brlan0 Mac Address remians unchanged" %(step);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS";
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT %d: Brlan0 Mac Address is NOT the same" %(step);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: Brlan0 Mac Address is : %s" %(step, details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";

                                #Revert Lan Mode
                                step = step + 1;
                                print "\nTEST STEP %d : Revert Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to %s" %(step, initial_mode);
                                print "EXPECTED RESULT %d : Should set Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to %s" %(step, initial_mode);
                                tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
                                actualresult, details = setTR181Value(tdkTestObj, paramName1, initial_mode, "string");
                                sleep(120);

                                if expectedresult in actualresult and details != "":
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step, details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step, details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else :
                                tdkTestObj.setResultStatus("FAILURE");
                                print "Lan Mode NOT changed";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Current Lan mode is : %s" %(step, curr_mode);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Brlan0 Mac Address is : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Initial Lan mode is : %s" %(step, initial_mode);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "Unable to enable OVS, cannot proceed further...";

        #Revert operation
        if revert_flag == 1:
            step = step + 1;
            tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
            actualresult, details = setTR181Value(tdkTestObj, paramName, initial_enable, "boolean");
            print "\nTEST STEP %d : Set OVS Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable to %s" %(step, initial_enable);
            print "EXPECTED RESULT %d : Should set the OVS Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable to %s" %(step, initial_enable);

            if expectedresult in actualresult and details != "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Reboot the DUT for the RFC to take effect
                print "\nInitiating Reboot...";
                sysobj.initiateReboot();
                print "Sleeping for 300s..."
                sleep(300);
                print "Revert operation completed";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "\nOVS Enable revert operation not required";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Initial Enable state is : %s" %(step, initial_enable);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysobj.unloadModule("sysutil");
    tr181obj.unloadModule("tdkbtr181");
else:
    print "Failed to load sysutil/tr181 module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
