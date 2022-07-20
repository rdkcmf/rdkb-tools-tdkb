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
  <version>3</version>
  <name>TS_SANITY_CheckBrlan0MACAddress_WithBridgeUtilsEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the Mac Address of Brlan0 interface remains unchanged when the BridgeUtils Enable is toggled using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable.</synopsis>
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
    <test_case_id>TC_SANITY_73</test_case_id>
    <test_objective>To check if the Mac Address of Brlan0 interface remains unchanged when the BridgeUtils Enable is toggled using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable
paramValue : true/false
paramType : boolean</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial BridgeUtils enable status using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable
3. Get the brlan0 interface mac address in the initial BridgeUtils enable state
4. Toggle the BridgeUtils enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable
5. Reboot the DUT for the BridgeUtils enable RFC to take effect
6. Once the DUT is up, check if the BridgeUtils enable is toggled successfully
7. Get the current brlan0 interface mac address
8. Compare the brlan0 mac address when the BridgeUtils is enabled and disabled. It should be the same
9. Revert the enable state using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable and reboot the DUT for the RFC to take effect.
10. Unload the modules</automation_approch>
    <expected_output>The Mac Address of Brlan0 interface should remain unchanged when the BridgeUtils Enable is toggled using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckBrlan0MACAddress_WithBridgeUtilsEnabled</test_script>
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
sysobj.configureTestCase(ip,port,'TS_SANITY_CheckBrlan0MACAddress_WithBridgeUtilsEnabled');
tr181obj.configureTestCase(ip,port,'TS_SANITY_CheckBrlan0MACAddress_WithBridgeUtilsEnabled');

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

    #Get the initial Bridge Utils enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable
    step = 1;
    paramName ="Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable";
    tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    actualresult, initial_enable = getTR181Value(tdkTestObj, paramName);

    print "\nTEST STEP %d: Get the initial Bridge Utils Enable state using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable" %step;
    print "EXPECTED RESULT %d: Should successfully get the initial value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable" %step;

    if expectedresult in actualresult and initial_enable != "":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Initial Enable state is : %s" %(step, initial_enable);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Get the brlan0 MAC address
        step = step + 1;
        cmd= "ifconfig brlan0 | grep \"HWaddr\"";
        print "\nCommand : ", cmd;
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

        print "\nTEST STEP %d : Get the Brlan0 Mac Address when the Bridge Utils enable state is %s" %(step, initial_enable);
        print "EXPECTED RESULT %d : Should get the Brlan0 Mac Address successfully when Bridge Utils enable state is %s" %(step, initial_enable);

        if expectedresult in actualresult and details != "":
            brlan0_mac_initial = details.strip().split("HWaddr ")[1];
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Brlan0 Mac Address is : %s" %(step, brlan0_mac_initial);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Toggle the Bridge Utils Enable status
            step = step + 1;
            setValue = "";
            if initial_enable == "true":
                setValue = "false";
            else :
                setValue = "true";

            tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
            actualresult, details = setTR181Value(tdkTestObj, paramName, setValue, "boolean");
            print "\nTEST STEP %d : Set Bridge Utils Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable to %s" %(step, setValue);
            print "EXPECTED RESULT %d : Should set the Bridge Utils Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable to %s" %(step, setValue);

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

                #Check if the Bridge Utils RFC is set successfully
                step = step + 1;
                tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_Get');
                actualresult, curr_enable = getTR181Value(tdkTestObj, paramName);

                print "\nTEST STEP %d: Get the current Bridge Utils Enable state using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable" %step;
                print "EXPECTED RESULT %d: Should successfully get the current value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable" %step;

                if expectedresult in actualresult and curr_enable != "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Current Enable state is : %s" %(step, curr_enable);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if curr_enable == setValue:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Bridge Utils Enable is successfully set to %s" %setValue;

                        #Get the MAC address for brlan0 interface
                        step = step + 1;
                        cmd= "ifconfig brlan0 | grep \"HWaddr\"";
                        print "\nCommand : ", cmd;
                        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                        actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                        print "\nTEST STEP %d : Get the Brlan0 Mac Address when the Bridge Utils enable state is set to %s" %(step, initial_enable);
                        print "EXPECTED RESULT %d : Should get the Brlan0 Mac Address successfully when Bridge Utils enable state is set to %s" %(step, initial_enable);

                        if expectedresult in actualresult and details != "":
                            brlan0_mac_final = details.strip().split("HWaddr ")[1];
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Brlan0 Mac Address is : %s" %(step, brlan0_mac_final);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Check if the MAC address for brlan0 interface remains unchanged
                            step = step + 1;
                            print "\nTEST STEP %d : Check if the Brlan0 Mac Address remain unchanged irrespective of the Bridge Utils Enable state" %(step);
                            print "EXPECTED RESULT %d : The Brlan0 Mac Address should remain unchanged irrespective of the Bridge Utils Enable state" %(step);
                            print "Brlan0 Mac Address when Bridge Utils is %s : %s" %(initial_enable, brlan0_mac_initial);
                            print "Brlan0 Mac Address when Bridge Utils is %s : %s" %(curr_enable, brlan0_mac_final);

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

                        #Revert operation
                        step = step + 1;
                        tdkTestObj = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
                        actualresult, details = setTR181Value(tdkTestObj, paramName, initial_enable, "boolean");
                        print "\nTEST STEP %d : Revert Bridge Utils Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable to %s" %(step, initial_enable);
                        print "EXPECTED RESULT %d : Should revert the Bridge Utils Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.BridgeUtilsEnable to %s" %(step, initial_enable);

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
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Bridge Utils Enable is NOT successfully set to %s" %setValue;
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
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Brlan0 Mac Address is : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
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
