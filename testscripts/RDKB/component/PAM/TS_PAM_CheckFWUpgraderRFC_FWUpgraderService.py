##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <name>TS_PAM_CheckFWUpgraderRFC_FWUpgraderService</name>
  <primitive_test_id/>
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if rdkfwupgrader.service is running or in dead state depending on whether or not Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable is enabled and device rebooted.</synopsis>
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
    <test_case_id>TC_PAM_211</test_case_id>
    <test_objective>To check if rdkfwupgrader.service is running or in dead state depending on whether or not Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable is enabled and device rebooted.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable
command : input command to check the service status
ParamValue : value
PramType : bool
</input_parameters>
    <automation_approch>1. Load the pam and sysutil modules.
2. Get the initial enable state of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable
3. If the enable status is true, check if rdkfwupgrader.service is running else it should be in dead state
4. Toggle the enable value
5. Reboot the device
6. After the device comes up, check if the enable value persists on reboot
7. If the enable status is true, check if rdkfwupgrader.service is running else it should be in dead state
8. Revert to initial state
9. Unload the module</automation_approch>
    <expected_output>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable parameter value should persist on reboot and rdkfwupgrader.service should be running or dead state in the device depending on whether the RFC is enabled or disabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_CheckFWUpgraderRFC_FWUpgraderService</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def check_FwupgraderService(sysobj, command):
    expectedresult = "SUCCESS";
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return tdkTestObj, actualresult, details;

def get_EnableFWUpgraderRFC(tdkTestObj, step):
    expectedresult = "SUCCESS";
    status = 1;
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "\nTEST STEP %d : Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable" %step;
    print "EXPECTED RESULT %d : Should get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable" %step;

    if expectedresult in actualresult and details != "":
        status = 0;
        enable = details.strip().replace("\\n", "");
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : Enable Status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable is : %s" %(step,enable);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : Enable Status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is not retrieved" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return enable, status;

def set_EnableFWUpgraderRFC(pamobj, value, step):
    status = 1;
    expectedresult = "SUCCESS";
    tdkTestObj = pamobj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable");
    tdkTestObj.addParameter("ParamValue",value);
    tdkTestObj.addParameter("Type","bool");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "\nTEST STEP %d: Set Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable to %s" %(step, value);
    print "EXPECTED RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable should be set to %s successfully" %(step, value);

    if expectedresult in actualresult and details != "":
        status = 0;
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable is set to %s successfully; Details : %s" %(step, value, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RDKFirmwareUpgrader.Enable is not set to %s successfully; Details : %s" %(step, value, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
import tdkutility;
from time import sleep;

#Test component to be tested
pamobj = tdklib.TDKScriptingLibrary("pam","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_PAM_CheckFWUpgraderRFC_FWUpgraderService');
sysobj.configureTestCase(ip,port,'TS_PAM_CheckFWUpgraderRFC_FWUpgraderService');

#Get the result of connection with test component and DUT
pamloadmodulestatus=pamobj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();

if "SUCCESS" in sysloadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    #Get FWUpgrader RFC Parameter
    step = 1;
    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
    enable, status = get_EnableFWUpgraderRFC(tdkTestObj, step);

    if enable == "true" and status == 0:
        print "\nInitial Enable Status : %s" %enable;
        step = step + 1;
        #If RFC Enable is true, then the service should be in running state
        command = "systemctl status rdkfwupgrader.service | grep -i running";
        print "\nTEST STEP %d: Check if rdkfwupgrader.service is running in the device" %step;
        print "EXPECTED RESULT %d : rdkfwupgrader.service should be running in the device" %step;
        tdkTestObj, actualresult, details = check_FwupgraderService(sysobj, command);

        if expectedresult in actualresult and details != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d : rdkfwupgrader.service is running in the device : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Toggle the enable to false
            step = step + 1;
            value = "false";
            status = set_EnableFWUpgraderRFC(pamobj, value, step);

            if status == 0:
                print "\nReboot the device, the RFC value should persist on reboot";
                print "Rebooting the device......";
                sysobj.initiateReboot();
                sleep(300);

                #Get the RFC value after reboot
                step = step + 1;
                tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
                enable, status = get_EnableFWUpgraderRFC(tdkTestObj, step);

                if enable == "false" and status == 0:
                    print "\nCurrent Enable Status : %s" %enable;
                    step = step + 1;
                    #If RFC Enable is false, then the service should be in dead state
                    command = "systemctl status rdkfwupgrader.service | grep -i dead";
                    print "\nTEST STEP %d: Check if rdkfwupgrader.service is in dead state in the device" %step;
                    print "EXPECTED RESULT %d : rdkfwupgrader.service should be in dead state in the device" %step;
                    tdkTestObj, actualresult, details = check_FwupgraderService(sysobj, command);

                    if expectedresult in actualresult and details != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : rdkfwupgrader.service is in dead state in the device : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Revert the RFC to initiable Enable status
                        print "Reverting to initial RFC enable state";
                        step = step + 1;
                        value = "true";
                        status = set_EnableFWUpgraderRFC(pamobj, value, step);

                        if status == 0:
                            print "\nReboot the device, the RFC value should persist on reboot";
                            print "Rebooting the device......";
                            sysobj.initiateReboot();
                            sleep(300);
                            print "Revert operation completed";
                        else:
                            print "Set operation failed";
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : rdkfwupgrader.service is not in dead state in the device : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "Get operation failed";
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "Set operation failed";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d : rdkfwupgrader.service is not running in the device : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    elif enable == "false" and status == 0:
        print "\nInitial Enable State : %s" %enable;
        step = step + 1;
        #If RFC Enable is false, then the service should be in dead state
        command = "systemctl status rdkfwupgrader.service | grep -i dead";
        print "\nTEST STEP %d: Check if rdkfwupgrader.service is in dead state in the device" %step;
        print "EXPECTED RESULT %d : rdkfwupgrader.service should be in dead state in the device" %step;
        tdkTestObj, actualresult, details = check_FwupgraderService(sysobj, command);

        if expectedresult in actualresult and details != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d : rdkfwupgrader.service is in dead state in the device : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Toggle the enable to true
            step = step + 1;
            value = "true";
            status = set_EnableFWUpgraderRFC(pamobj, value, step);

            if status == 0:
                print "\nReboot the device, the RFC value should persist on reboot";
                print "Rebooting the device......";
                sysobj.initiateReboot();
                sleep(300);

                #Get the RFC value after reboot
                step = step + 1;
                tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
                enable, status = get_EnableFWUpgraderRFC(tdkTestObj, step);

                if enable == "true" and status == 0:
                    print "\nCurrent Enable State : %s" %enable;
                    step = step + 1;
                    #If RFC Enable is true, then the service should be in running state
                    command = "systemctl status rdkfwupgrader.service | grep -i running";
                    print "\nTEST STEP %d: Check if rdkfwupgrader.service is in running state in the device" %step;
                    print "EXPECTED RESULT %d : rdkfwupgrader.service should be in running state in the device" %step;
                    tdkTestObj, actualresult, details = check_FwupgraderService(sysobj, command);

                    if expectedresult in actualresult and details != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : rdkfwupgrader.service is in running state in the device : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Revert the RFC to initiable Enable status
                        print "Reverting to initial RFC enable state";
                        step = step + 1;
                        value = "false";
                        status = set_EnableFWUpgraderRFC(pamobj, value, step);

                        if status == 0:
                            print "\nReboot the device, the RFC value should persist on reboot";
                            print "Rebooting the device......";
                            sysobj.initiateReboot();
                            sleep(300);
                            print "Revert operation completed";
                        else:
                            print "Set operation failed";
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : rdkfwupgrader.service is not in running state in the device : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "Get operation failed";
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "Set operation failed";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d : rdkfwupgrader.service is not in dead state in the device : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        print "Get operation failed";
        tdkTestObj.setResultStatus("FAILURE");

    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");

