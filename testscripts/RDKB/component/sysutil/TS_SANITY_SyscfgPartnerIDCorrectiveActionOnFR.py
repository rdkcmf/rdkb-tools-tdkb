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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>7</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_SyscfgPartnerIDCorrectiveActionOnFR</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if the Partner ID set to "Unknown" in syscfg reverted to default value after factory reset even when apply system default script is executed prior to factory reset.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>20</execution_time>
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
    <test_case_id>TC_SANITY_76</test_case_id>
    <test_objective>To check if the Partner ID set to "Unknown" in syscfg reverted to default value after factory reset even when apply system default script is executed prior to factory reset.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the sysutil and pam modules
2. Get the initial Partner ID stored in syscfg.
3. If the initial Partner ID is not "Unknown", set to "Unknown" and validate with get.
4. Ensure that /nvram/.partner_ID file is not present. If it is present, remove it.
5. Get the location of APPLY SYSTEM DEFAULTS script from platform property file.
6. Check if the script file exists in the location retrieved.
7. Execute the script to use the PartnerID "Unknown".
8. Upon successful execution, factory reset the DUT.
9. After FR, get the syscfg Partner ID and check if the value is NOT "Unknown".
10. Revert the syscfg Partner ID to the initial value if required.
11. Unload the sysutil and pam modules.</automation_approch>
    <expected_output>Partner ID set to "Unknown" in syscfg should be reverted to default value after factory reset even when apply system default script is executed prior to factory reset.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_SyscfgPartnerIDCorrectiveActionOnFR</test_script>
    <skipped>No</skipped>
    <release_version>M105</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
obj1 = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_SyscfgPartnerIDCorrectiveActionOnFR');
obj1.configureTestCase(ip,port,'TS_SANITY_SyscfgPartnerIDCorrectiveActionOnFR');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    expectedresult="SUCCESS";
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    #Get the Syscfg Partner ID
    step = 1;
    proceed_flag = 0;
    revert_flag = 0;
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    cmd = "syscfg get PartnerID";
    print "\nCommand : ", cmd;
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    initial_id = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d : Retrieve the Partner ID in Syscfg" %step;
    print "EXPECTED RESULT %d : Partner ID should be retrieved from Syscfg successfully" %step;

    if expectedresult in actualresult and initial_id != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : Syscfg Partner ID retrieved successfully : %s" %(step, initial_id);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        #If Partner ID is not unknown, set to unknown partner ID
        if initial_id != "Unknown":
            step = step + 1;
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            cmd = "syscfg set PartnerID \"Unknown\"";
            print "\nCommand : ", cmd;
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            print "\nTEST STEP %d : Set the Partner ID in Syscfg to Unknown" %step;
            print "EXPECTED RESULT %d : Partner ID should be set successfully" %step;

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : Partner ID set successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"

                #Cross check the Partner ID with GET
                step = step + 1;
                tdkTestObj = obj.createTestStep('ExecuteCmd');
                cmd = "syscfg get PartnerID";
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                set_id = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                print "\nTEST STEP %d : Retrieve the Partner ID in Syscfg and the value should be \"Unknown\"" %step;
                print "EXPECTED RESULT %d : Partner ID should be retrieved from Syscfg successfully and the value should be \"Unknown\"" %step;

                if expectedresult in actualresult and set_id == "Unknown":
                    revert_flag = 1;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : Syscfg Partner ID retrieved successfully : %s" %(step, set_id);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    proceed_flag = 1;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : Syscfg Partner ID not as expected : %s" %(step, set_id);
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : Partner ID NOT set successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            print "Partner ID is Unknown initially, SET operation not required";

        #Check if /nvram/.partner_ID file exists
        if proceed_flag == 0:
            #Check if .partner_ID file is present under /nvram
            step = step + 1;
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            cmd = "[ -f /nvram/.partner_ID ] && echo \"File exist\" || echo \"File does not exist\""
            print "\nCommand : ", cmd;
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            print "\nTEST STEP %d : Check if the file .partner_ID is present under nvram, if present remove it" %step;
            print "EXPECTED RESULT %d : The .partner_ID should be removed from nvram" %step;

            if expectedresult in actualresult and details == "File does not exist" :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : File not present" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                print "\nFile exists under nvram, removing the file...";
                tdkTestObj = obj.createTestStep('ExecuteCmd');
                cmd = "rm -rf /nvram/.partner_ID";
                print "Command : ", cmd;
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : File is removed from nvram" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: File is NOT removed from nvram" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "Unable to set the Partner ID to unknown, cannot proceed...";

        #Get the location of apply_system_defaults script from platform properties
        step = step + 1;
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        cmd = "sh %s/tdk_utility.sh parseConfigFile APPLY_SYSTEM_DEFAULTS" %TDK_PATH;
        print "\nCommand : ", cmd;
        tdkTestObj.addParameter("command", cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        file = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        print "\nTEST STEP %d: Get the Apply System Defaults file location from platform property file" %step;
        print "EXPECTED RESULT %d: Should successfully get the Apply System Defaults file location from platform property file" %step;

        if expectedresult in actualresult and details != "" :
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: File location is retrieved successfully" %step;
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if the required file exists in the DUT at that location
            step = step + 1;
            cmd = "[ -f " + file + " ] && echo \"File exist\" || echo \"File does not exist\"";
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            print "\nTEST STEP %d: Check for Apply System Defaults script presence in the DUT" %(step);
            print "EXPECTED RESULT %d: The Apply System Defaults script should be present in the DUT" %(step);

            if expectedresult in actualresult and details == "File exist":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Apply System Defaults script is present" %(step);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Run apply_system_defaults to use the PartnerID "Unknown"
                step = step + 1;
                tdkTestObj.addParameter("command",file);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                print "\nTEST STEP %d: Execute the Apply System Defaults script to use the PartnerID \"Unknown\"" %step;
                print "EXPECTED RESULT %d: The Apply System Defaults script should be executed successfully" %step;

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Apply System Defaults script executed successfully" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Restore the device state saved before reboot
                    obj.saveCurrentState();

                    #Initiate Factory reset before checking the default value
                    step = step + 1;
                    tdkTestObj = obj1.createTestStep('pam_Setparams');
                    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
                    tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
                    tdkTestObj.addParameter("Type","string");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    print "\nTEST STEP %d: Initiate factory reset" %step;
                    print "EXPECTED RESULT %d : DUT should be factory resetted successfully" %step;

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Restore the device state saved before reboot
                        obj.restorePreviousStateAfterReboot();

                        #Check the Partner ID in Syscfg - It should NOT be "Unknown"
                        step = step + 1;
                        tdkTestObj = obj.createTestStep('ExecuteCmd');
                        cmd = "syscfg get PartnerID";
                        print "\nCommand : ", cmd;
                        tdkTestObj.addParameter("command",cmd);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        final_id = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                        print "\nTEST STEP %d : Get the Partner ID value in Syscfg and check if it is not \"Unknown\"" %step;
                        print "EXPECTED RESULT %d : Should retrieve the value present under in Syscfg and it should not be \"Unknown\"" %step;

                        if expectedresult in actualresult and final_id != "" :
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d : Partner ID retrieved from Syscfg is : %s" %(step, final_id);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            if final_id != "Unknown":
                                revert_flag = 0;
                                print "The Partner ID is not retrieved as \"Unknown\" from Syscfg";
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                            else:
                                revert_flag = 1;
                                print "The Partner ID is retrieved as \"Unknown\" from Syscfg";
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                        else :
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d : Partner ID retrieved from Syscfg is : %s" %(step, final_id);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Apply System Defaults script NOT executed successfully" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Apply System Defaults script is NOT present" %(step);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: File location : %s" %(step, file);
            print "[TEST EXECUTION RESULT] : FAILURE";

        #Revert to initial value
        if revert_flag == 1:
            step = step + 1;
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            cmd = "syscfg set PartnerID " + initial_id;
            print "\nCommand : ", cmd;
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            print "\nTEST STEP %d : Set the Partner ID in Syscfg to %s" %(step, initial_id);
            print "EXPECTED RESULT %d : Partner ID should be set successfully" %step;

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : Partner ID set successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"

                #Run apply_system_defaults to use the initial PartnerID
                step = step + 1;
                tdkTestObj.addParameter("command",file);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                print "\nTEST STEP %d: Execute the Apply System Defaults script to use the PartnerID %s" %(step, initial_id);
                print "EXPECTED RESULT %d: The Apply System Defaults script should be executed successfully" %step;

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Apply System Defaults script executed successfully" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Apply System Defaults script NOT executed successfully" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : Partner ID NOT set successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "Revert operation not required";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : Syscfg Partner ID is NOT retrieved successfully : %s" %(step, initial_id);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("sysutil");
    obj1.unloadModule("pam");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
