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
  <name>TS_PAM_ReinitMacThreshold_PersistentOnReboot</name>
  <primitive_test_id/>
  <primitive_test_name>pam_Setparams</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold to a new value and check if the set operation is success and whether the value is persisting after reboot.</synopsis>
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
    <test_case_id>TC_PAM_210</test_case_id>
    <test_objective>Set Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold to a new value and check if the set operation is success and whether the value is persisting after reboot.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>pam_Setparams</api_or_interface_used>
    <input_parameters>ParamName : Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold
ParamValue : setValue
Type : unsignedInt</input_parameters>
    <automation_approch>1. Load the PAM module
2. Get the initial value of Device.X_CISCO_COM_DeviceControl.ReinitMac and store it
3. Set Device.X_CISCO_COM_DeviceControl.ReinitMac to 5.
4. Verify the Set operation with Get.
5. Reboot the DUT
6. Once the device comes up, check if Device.X_CISCO_COM_DeviceControl.ReinitMac value persists.
7. Revert to initial value
8. Unload the module</automation_approch>
    <expected_output>Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold should persist on reboot</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_ReinitMacThreshold_PersistentOnReboot</test_script>
    <skipped>No</skipped>
    <release_version>M88</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def get_ReinitMacThreshold(tdkTestObj, step):
    return_val = -1;
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();

    if expectedresult in actualresult :
        initial_value = int(tdkTestObj.getResultDetails());
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP %d: Get the value of Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold" %step;
        print "EXPECTED RESULT %d: Should get the value of Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold" %step;
        print "ACTUAL RESULT %d: %d"%(step, initial_value);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        return_val = initial_value;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP %d: Get the value of Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold" %step;
        print "EXPECTED RESULT %d: Should get the value of Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold" %step;
        print "ACTUAL RESULT %d: Get operation failed"%step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return return_val;

def set_ReinitMacThreshold(tdkTestObj, setValue, step):
    return_val = -1;
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold");
    tdkTestObj.addParameter("ParamValue",setValue);
    tdkTestObj.addParameter("Type","unsignedInt");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();

    if expectedresult in actualresult :
        details = tdkTestObj.getResultDetails();
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP %d Set Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold to the new ReinitMacThreshold" %step;
        print "EXPECTED RESULT %d: Should set Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold to the new ReinitMacThreshold" %step;
        print "ACTUAL RESULT %d:  %s" %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        return_val = 0;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP %d: Set Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold to the new ReinitMacThreshold" %step;
        print "EXPECTED RESULT %d: Should set Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold to the new ReinitMacThreshold" %step;
        print "ACTUAL RESULT %d:  Set Operation failed" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return return_val;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_ReinitMacThreshold_PersistentOnReboot');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("pam_GetParameterValues");
    #Get the value
    step = 1;
    initial = get_ReinitMacThreshold(tdkTestObj, step);

    if initial != -1:
        #Set ReinitMacThreshold to 5
        setValue = '5';
        print "The ReinitMacThreshold to set is %d" %int(setValue);
        tdkTestObj = obj.createTestStep("pam_Setparams");
        step = step + 1;
        status = set_ReinitMacThreshold(tdkTestObj, setValue, step);

        if status == 0:
            #Validation of set function using get
            tdkTestObj = obj.createTestStep("pam_GetParameterValues");
            step = step + 1;
            get_value =  get_ReinitMacThreshold(tdkTestObj, step);

            if get_value == int(setValue) :
                tdkTestObj.setResultStatus("SUCCESS");
                print "The Get value and Set value are the same";
                #Check persistence on reboot
                #rebooting the device
                obj.initiateReboot();
                sleep(300);
                step = step + 1;
                value_reboot = get_ReinitMacThreshold(tdkTestObj, step);

                if value_reboot == int(setValue) :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold is persistent on reboot";
                    #Revert Operation
                    print "Reverting to initial value";
                    step = step + 1;
                    tdkTestObj = obj.createTestStep("pam_Setparams");
                    initial_value = str(initial);
                    status = set_ReinitMacThreshold(tdkTestObj, initial_value, step);
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Device.X_CISCO_COM_DeviceControl.ReinitMacThreshold is not persistent on reboot";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "The Get value and Set value are not the same";
        else:
            print "Set Operation Failed";
    else:
        print "The Get Operation did not retrieve the value"

    obj.unloadModule("pam");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

