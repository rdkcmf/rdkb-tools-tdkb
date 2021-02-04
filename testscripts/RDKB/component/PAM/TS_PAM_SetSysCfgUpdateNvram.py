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
  <version>19</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_PAM_SetSysCfgUpdateNvram</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate the Syscfg.UpdateNvram parameter set using syscfg files availablity</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
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
    <box_type></box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_197</test_case_id>
    <test_objective>To validate the Syscfg.UpdateNvram parameter set using syscfg files availablity </test_objective>
    <test_type>Positive</test_type>
    <test_setup></test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SysCfg.UpdateNvram</input_parameters>
    <automation_approch>1. Load the pam module
2. Get the secured location of syscfg file from platform properties file
3. Get the initial value of Syscfg.UpdateNvram parameter and store it
4. If the initial Syscfg.UpdateNvram value was true, then check both syscfg files (in nvram location and secured location) are present, if the initial Syscfg.UpdateNvram value was false then check syscfg file in temporary location(from nvram) is not present and secured location file only present
5. Toggle the UpdateNvram value and check the syscfg file availability based on the new set value
6. Revert the Syscfg.UpdateNvramvalue to initial value
7. Unload the pam module</automation_approch>
    <expected_output>Syscfg file in Nvram location should be deleted if SysCfg.UpdateNvram parameter set to false</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_SetSysCfgUpdateNvram</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#import statement
import tdklib;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_SetSysCfgUpdateNvram');
sysobj.configureTestCase(ip,port,'TS_PAM_SetSysCfgUpdateNvram');

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
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    revertflag = 0;
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
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        initialValue = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the SysCfg UpdateNvram Value";
            print "EXPECTED RESULT 1: Should get the SysCfg UpdateNvram Value";
            print "ACTUAL RESULT 1: Initial Value is %s" %initialValue;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if initialValue == "true":
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                tmp_result, tmp_details, secure_result, secure_details = verify_SysCfgUpdateNvram(tdkTestObj);

                if tmp_result in actualresult and tmp_details == tmpLocation:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Verify temporary location syscfg File is present with update nvram value True";
                    print "EXPECTED RESULT 2: The temporary location syscfg file should be present with update nvram value True";
                    print "ACTUAL RESULT 2: The temporarty location syscfg file is present with update nvram value True"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if secure_result in actualresult and secure_details == secureLocation:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3: Verify Secured location syscfg File is present with update nvram value True";
                        print "EXPECTED RESULT 3: The Secured  location syscfg file should be present with update nvram value True";
                        print "ACTUAL RESULT 3: The Secured location syscfg file is present with update nvram value True"
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                        set_disable_res,set_disable_details = set_SysCfgUpdateNvram (tdkTestObj,"false");

                        if set_disable_res in actualresult:
                            revertflag = 1;
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 4: Set Operation to make update Nvram as false";
                            print "EXPECTED RESULT 4: set operation should success";
                            print "ACTUAL RESULT 4: Set operation was success"
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                            tmp_result, tmp_details, secure_result, secure_details = verify_SysCfgUpdateNvram(tdkTestObj);

                            if tmp_result in actualresult and tmp_details == "":
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 5: Verify temporary location syscfg File is present with update nvram value False";
                                print "EXPECTED RESULT 5: The temporary location syscfg file should not be present with update nvram value False";
                                print "ACTUAL RESULT 5: The temporarty location syscfg file is not present with update nvram value False";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                if secure_result in actualresult and secure_details == secureLocation:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "TEST STEP 6: Verify Secured location syscfg File is present with update nvram value False";
                                    print "EXPECTED RESULT 6: The Securedlocation syscfg file should be present with update nvram value False";
                                    print "ACTUAL RESULT 6: The Secured location syscfg file is present with update nvram value False";
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "TEST STEP 6: Verify Secured location syscfg File is present with update nvram value False";
                                    print "EXPECTED RESULT 6: The Secured location syscfg file should be present with update nvram value False";
                                    print "ACTUAL RESULT 6: The Secured location syscfg file is NOT present with update nvram value False";
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 5: Verify temporary location syscfg File is present with update nvram value False";
                                print "EXPECTED RESULT 5: The temporary location syscfg file should be present with update nvram value False";
                                print "ACTUAL RESULT 5: The temporarty location syscfg file is present with update nvram value False";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 4: Set Operation to make update Nvram as false";
                            print "EXPECTED RESULT 4: set operation should success";
                            print "ACTUAL RESULT 4: Set operation was Failed";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Verify Secured location syscfg File is present with update nvram value True";
                        print "EXPECTED RESULT 3: The Secured  location syscfg file should be present with update nvram value True";
                        print "ACTUAL RESULT 3: The Secured location syscfg file is NOT present with update nvram value True"
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 2: Verify temporary location syscfg File is present with update nvram value True";
                    print "EXPECTED RESULT 2: The temporary location syscfg file should be present with update nvram value True";
                    print "ACTUAL RESULT 2: The temporarty location syscfg file is NOT present with update nvram value True"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                tmp_result, tmp_details, secure_result, secure_details = verify_SysCfgUpdateNvram(tdkTestObj);

                if tmp_result in actualresult and tmp_details =="" :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Verify temporary location syscfg File is present with update nvram value False";
                    print "EXPECTED RESULT 2: The temporary location syscfg file should NOT be present with update nvram value False";
                    print "ACTUAL RESULT 2: The temporarty location syscfg file is NOT present with update nvram value False";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if secure_result in actualresult and secure_details == secureLocation:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3: Verify Secured location syscfg File is present with update nvram value False";
                        print "EXPECTED RESULT 3: The Secured  location syscfg file should be present with update nvram value False";
                        print "ACTUAL RESULT 3: The Secured location syscfg file is present with update nvram value False";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                        set_disable_res,set_disable_details = set_SysCfgUpdateNvram (tdkTestObj,"true");
                        if set_disable_res in actualresult:
                            revertflag = 1;
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 4: Set Operation to make update Nvram as false";
                            print "EXPECTED RESULT 4: set operation should success";
                            print "ACTUAL RESULT 4: Set operation was success"
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                            tmp_result, tmp_details, secure_result, secure_details = verify_SysCfgUpdateNvram(tdkTestObj);

                            if tmp_result in actualresult and tmp_details == tmpLocation:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 5: Verify temporary location syscfg File is present with update nvram value True";
                                print "EXPECTED RESULT 5: The temporary location syscfg file should be present with update nvram value True";
                                print "ACTUAL RESULT 5: The temporary location syscfg file is present with update nvram value True"
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                if secure_result in actualresult and secure_details == secureLocation:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "TEST STEP 6: Verify Secured location syscfg File is present with update nvram value True";
                                    print "EXPECTED RESULT 6: The Secured location syscfg file should be present with update nvram value True";
                                    print "ACTUAL RESULT 6: The  Secured location syscfg file is present with update nvram value True"
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "TEST STEP 6: Verify Secured location syscfg File is present with update nvram value True";
                                    print "EXPECTED RESULT 6: The Secured location syscfg file should be present with update nvram value True";
                                    print "ACTUAL RESULT 6: The  Secured location syscfg file is NOT present with update nvram value True"
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 5: Verify temporary location syscfg File is present with update nvram value True";
                                print "EXPECTED RESULT 5: The temporary location syscfg file should be present with update nvram value True";
                                print "ACTUAL RESULT 5: The temporary location syscfg file is NOT present with update nvram value True"
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 4: Set Operation to make update Nvram as false";
                            print "EXPECTED RESULT 4: set operation should success";
                            print "ACTUAL RESULT 4: Set operation was success"
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Verify Secured location syscfg File is present with update nvram value False";
                        print "EXPECTED RESULT 3: The Secured  location syscfg file should be present with update nvram value False";
                        print "ACTUAL RESULT 3: The Secured location syscfg file is NOT present with update nvram value False";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 2: Verify temporary location syscfg File is present with update nvram value False";
                    print "EXPECTED RESULT 2: The temporary location syscfg file should NOT be present with update nvram value False";
                    print "ACTUAL RESULT 2: The temporary location syscfg file is present with update nvram value False";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert The values
            if revertflag == 1:
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                revert_set_res,revert_set_details = set_SysCfgUpdateNvram (tdkTestObj,initialValue);

                if revert_set_res in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 7: Revert the values to initial value";
                    print "EXPECTED RESULT 7: Revert Operation should success";
                    print "ACTUAL RESULT 7: Revert Operation was success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 7: Revert the values to initial value";
                    print "EXPECTED RESULT 7: Revert Operation should success";
                    print "ACTUAL RESULT 7: Revert Operation was success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                print "Revert Flag was not set, No need for Revert Operation";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the SysCfg UpdateNvram Value";
            print "EXPECTED RESULT 1: Should get the SysCfg UpdateNvram Value";
            print "ACTUAL RESULT 1: Failed to get the SysCfg UpdateNvram Value";
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the SysCfg Secure location from Platform properties file";
        print "EXPECTED RESULT 1: Should get the SysCfg Secure location from Platform properties file";
        print "ACTUAL RESULT 1: SysCfg Secure location found from platform properties file";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

    obj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
