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
  <name>TS_PAM_CheckSyscfgFilesAfterReboot_WithUpdateNvramFalse</name>
  <primitive_test_id/>
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To Check syscfg files in nvram location and secured location are restored after deleting in reboot scenario with UpdateNvram as False</synopsis>
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
    <test_case_id>TC_PAM_199</test_case_id>
    <test_objective>To Check syscfg files in nvram location and secured location are restored after deleting in reboot scenario with UpdateNvram as False</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SysCfg.UpdateNvram</input_parameters>
    <automation_approch>1. Load the pam module
2. Get the secured location of syscfg file from platform properties file
3. Get the initial value of Syscfg.UpdateNvram parameter and store it
4. If the initial Syscfg.UpdateNvram value was false set flag as 1 if not set the Syscfg.UpdateNvram value as false then check temporary syscfg file is not present and only secured location syscfg file is present
5. Remove the the syscfg files from nvram and secured location and make sure files got removed successfully
6. Reboot the DUT then check syscfg files got restored in secured location and temporary location since UpdateNvram value was true after reboot
7. Revert the Syscfg.UpdateNvramvalue to initial value
8. Unload the pam module</automation_approch>
    <expected_output>The Syscfg files should get restored in reboot scenarios if the files got deleted before</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_CheckSyscfgFilesAfterReboot_WithUpdateNvramFalse</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>none</remarks>
  </test_cases>
</xml>

'''
#import statement
import tdklib;
from tdkbVariables import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_CheckSyscfgFilesAfterReboot_WithUpdateNvramFalse');
sysobj.configureTestCase(ip,port,'TS_PAM_CheckSyscfgFilesAfterReboot_WithUpdateNvramFalse');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysobjloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysobjloadmodulestatus ;

tmpLocation = "/nvram/syscfg.db"
secureLocation = ""

def isFilePresent(tdkTestObj,filename):
    query = "ls %s"%filename;
    tdkTestObj.addParameter("command", query);
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    return actualresult,details;

def set_SysCfgUpdateNvram(tdkTestObj,set_value):
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SysCfg.UpdateNvram");
    tdkTestObj.addParameter("ParamValue",set_value);
    tdkTestObj.addParameter("Type","boolean");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    result = tdkTestObj.getResultDetails();
    return actualresult, result;

def verify_SysCfgUpdateNvram(tdkTestObj):
    tmp_result, tmp_details = isFilePresent(tdkTestObj,tmpLocation);
    secure_result, secure_details = isFilePresent(tdkTestObj,secureLocation);
    return tmp_result, tmp_details, secure_result, secure_details;

if "SUCCESS" in (loadmodulestatus.upper() and sysobjloadmodulestatus.upper()):
    revertflag = 0;
    flag = 0;
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    expectedresult="SUCCESS";
    #Getting  SYSCFG_SEC_LOCATION value from tdk_platform_properties"
    cmd= "sh %s/tdk_utility.sh parseConfigFile SYSCFG_SEC_LOCATION" %TDK_PATH;
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    secLocation = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if expectedresult in actualresult and secLocation != "":
        secureLocation = secLocation;
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the SysCfg Secure location from Platform properties file";
        print "EXPECTED RESULT 1: Should get the SysCfg Secure location from Platform properties file";
        print "ACTUAL RESULT 1: SysCfg Secure location found from platfrom properties file";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SysCfg.UpdateNvram");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        initialValue = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the SysCfg UpdateNvram Value";
            print "EXPECTED RESULT 2: Should get the SysCfg UpdateNvram Value";
            print "ACTUAL RESULT 2: Initial Value is %s" %initialValue;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if initialValue == "false":
                print "Update Nvram initial value is False";
                flag = 1;
            else:
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                set_enable_res,set_enable_details = set_SysCfgUpdateNvram(tdkTestObj,"false");

                if expectedresult in actualresult:
                     flag = 1;
                     revertflag = 1;
                     tdkTestObj.setResultStatus("SUCCESS");
                     print "TEST STEP 3: Verify Update Nvram is set to False";
                     print "EXPECTED RESULT 3: Update Nvram should set to False";
                     print "ACTUAL RESULT 3: Set operations was success";
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                     flag = 0;
                     revertflag = 0;
                     tdkTestObj.setResultStatus("FAILURE");
                     print "TEST STEP 3: Verify Update Nvram is set to False";
                     print "EXPECTED RESULT 3: Update Nvram should set to False";
                     print "ACTUAL RESULT 3: Set operations was success";
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : FAILURE";

            if flag == 1:
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                tmp_result, tmp_details, secure_result, secure_details = verify_SysCfgUpdateNvram(tdkTestObj);

   	        if expectedresult in (tmp_result and secure_result) and tmp_details == "" and secure_details == secureLocation :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Verify Syscfg files present in Nvram location and secured location";
                    print "EXPECTED RESULT 4: Syscfg file in Temporary location should not be present";
                    print "ACTUAL RESULT 4: Syscfg files in temporary location was not present ";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

	            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    query = "rm %s %s"%(tmpLocation,secureLocation)
                    print query;
                    tdkTestObj.addParameter("command", query);
                    tdkTestObj.executeTestCase("expectedresult");
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

	            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    tmp_result, tmp_details, secure_result, secure_details = verify_SysCfgUpdateNvram(tdkTestObj);

	            if expectedresult in (tmp_result and secure_result) and tmp_details == "" and secure_details == "" :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Verify Syscfg files are removed";
                        print "EXPECTED RESULT 5: Both syscfg files should be Deleted";
                        print "ACTUAL RESULT 5: Syscfg files are deleted successfully ";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #rebooting the device
                        obj.initiateReboot();
                        sleep(300)

                        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                        tmp_result, tmp_details, secure_result, secure_details = verify_SysCfgUpdateNvram(tdkTestObj);

                        if expectedresult in (tmp_result and secure_result) and tmp_details == tmpLocation and secure_details == secureLocation :
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Verify Syscfg files present in Nvram location and secured location After Reboot";
                            print "EXPECTED RESULT 6: Both syscfg files should be present after reboot";
                            print "ACTUAL RESULT 6: Syscfg files are restored after reboot ";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6: Verify Syscfg files present in Nvram location and secured location After Reboot";
                            print "EXPECTED RESULT 6: Both syscfg files should be present after reboot";
                            print "ACTUAL RESULT 6: Syscfg files are NOT restored after reboot ";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
	            else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Verify Syscfg files are removed";
                        print "EXPECTED RESULT 5: Both syscfg files should be Deleted";
                        print "ACTUAL RESULT 5: Syscfg files are NOT removed successfully ";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
   	        else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Verify Syscfg files present in Nvram location and secured location";
                    print "EXPECTED RESULT 4: Syscfg file in Temporary location should not be present";
                    print "ACTUAL RESULT 4: Syscfg files in temporary location was still present ";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                print "Flag was not set, UpdateNvram Value was not set to False"
                tdkTestObj.setResultStatus("FAILURE");

            #Revert The values
            if revertflag ==1:
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
	        revert_set_res,revert_set_details = set_SysCfgUpdateNvram (tdkTestObj,initialValue);
                if revert_set_res in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Revert operation Success"
                    print "TEST STEP 10: Revert Update Nvram value to initial value";
                    print "EXPECTED RESULT 10: Revert operation should success";
                    print "ACTUAL RESULT 10: Revert Operation was success";
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 10: Revert Update Nvram value to initial value";
                    print "EXPECTED RESULT 10: Revert operation should success";
                    print "ACTUAL RESULT 10: Revert Operation was Failed";
                    print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the SysCfg UpdateNvram Value";
            print "EXPECTED RESULT 2: Should get the SysCfg UpdateNvram Value";
            print "ACTUAL RESULT 2: Failed to get initial syscfg updatenvram value";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the SysCfg Secure location from Platform properties file";
        print "EXPECTED RESULT 1: Should get the SysCfg Secure location from Platform properties file";
        print "ACTUAL RESULT 1: Failed to get SysCfg Secure location";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
