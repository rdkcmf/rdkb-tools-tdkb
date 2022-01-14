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
  <version>3</version>
  <name>TS_PAM_EnableRFC_AdvSecOTMEnable</name>
  <primitive_test_id/>
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set the Advanced Security OTM Enable RFC to enabled state and check if the set value is reflecting in the TR181 get and syscfg get. Also check if the required logging pattern for RFC change is getting logged in agent.txt file.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_241</test_case_id>
    <test_objective>Set the Advanced Security OTM Enable RFC to enabled state and check if the set value is reflecting in the TR181 get and syscfg get. Also check if the required logging pattern for RFC change is getting logged in agent.txt file.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable
ParamValue : setValue (true/false)</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable and store it.
3. If initially value is "true" set to "false" and check if the SET operation returns success.
4. Get the initial line count of the string "ADVANCE_SECURITY_OTM_EANBLED" in /rdklogs/logs/agent.txt.
5. Now toggle the RFC back to true and cross check if SET is reflected in GET.
6. Get the syscfg value of "Adv_AdvSecOTMRFCEnable" and cross check with the TR181 GET.
7. Get the final log line count of the string "ADVANCE_SECURITY_OTM_EANBLED" and check if its incremented by 1 on toggling the RFC to enabled state.
8. If the revert flag is set, perform revert operation of the RFC
9. Unload the modules.
</automation_approch>
    <expected_output>The set operation of Advanced Security OTM Enable RFC to enabled state should be success and the set value should reflect in the TR181 get and syscfg get. Also, the required logging pattern for RFC change should get logged in agent.txt file.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_EnableRFC_AdvSecOTMEnable</test_script>
    <skipped>No</skipped>
    <release_version>M97</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def get_parameter(tdkTestObj, paramName, expectedresult):
    tdkTestObj.addParameter("ParamName",paramName);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    initial_value = tdkTestObj.getResultDetails().strip();
    return initial_value, actualresult;

def set_parameter(tdkTestObj, paramName, setValue, expectedresult):
    tdkTestObj.addParameter("ParamName",paramName);
    tdkTestObj.addParameter("ParamValue",setValue);
    tdkTestObj.addParameter("Type","boolean");
    #Execute testcase on DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    result = tdkTestObj.getResultDetails();
    return result, actualresult;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *;
from time import sleep;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
pamobj = tdklib.TDKScriptingLibrary("pam","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_PAM_EnableRFC_AdvSecOTMEnable');
sysobj.configureTestCase(ip,port,'TS_PAM_EnableRFC_AdvSecOTMEnable');

#Get the result of connection with test component and DUT
pamloadmodulestatus =pamobj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %pamloadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

if  "SUCCESS" in pamloadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    paramName ="Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable";
    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
    initial_value, actualresult = get_parameter(tdkTestObj, paramName, expectedresult);

    print "\nTEST STEP 1: Get the initial value of RFC Advanced Security OTM Enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable"
    print "EXPECTED RESULT 1: Should successfully get the initial value of RFC Advanced Security OTM Enable"

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Initial value is : %s" %initial_value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check if the RFC is disabled, if not disable it
        flag = 0;
        step = 2;

        if initial_value == "true":
            setValue ="false";
            tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
            result, actualresult = set_parameter(tdkTestObj, paramName, setValue, expectedresult);

            print "\nTEST STEP %d: Set RFC Advanced Security OTM Enable to %s before enabling the RFC again" %(step, setValue);
            print "EXPECTED RESULT %d: Should successfully set RFC Advanced Security Enable status to %s before enabling the RFC again" %(step, setValue);

            if expectedresult in actualresult :
                flag = 1;
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: The RFC value set successfully; Details : %s" %(step, result);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: The RFC value not set successfully; Details : %s" %(step, result);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
            step = step + 1;
        else:
            flag = 1;

        if flag == 1:
            #Get the initial line count of "ADVANCE_SECURITY_OTM_EANBLED"
            sysTestObj = sysobj.createTestStep('ExecuteCmd');
            print "\nGet the current number of log lines of \"ADVANCE_SECURITY_OTM_ENABLED\"";
            file = "/rdklogs/logs/agent.txt"
            search_string = "ADVANCE_SECURITY_OTM_ENABLED";
            count_initial = getLogFileTotalLinesCount(sysTestObj, file, search_string, step);

            #Enable the RFC
            step = step + 1;
            setValue ="true";
            tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
            result, actualresult = set_parameter(tdkTestObj, paramName, setValue, expectedresult);

            print "\nTEST STEP %d: Set RFC Adcanced Security OTM Enable to %s" %(step, setValue);
            print "EXPECTED RESULT %d: Should successfully set RFC Advanced Security Enable status to %s" %(step, setValue);

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: The RFC value set successfully; Details : %s" %(step, result);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Cross check the set operation with syscfg_get and TR181 Get
                step = step + 1;
                tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
                tdkTestObj.addParameter("ParamName",paramName);
                #Execute the test case in DUT
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                curr_value = tdkTestObj.getResultDetails().strip();

                print "\nTEST STEP %d: Get the current value of RFC Advanced Security OTM Enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvancedSecurityOTM.Enable" %step;
                print "EXPECTED RESULT %d: Should successfully get the current value of RFC Advanced Security OTM Enable" %step;

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Current TR181 value is : %s" %(step, curr_value);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    step = step + 1;
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    cmd= "syscfg get Adv_AdvSecOTMRFCEnable";
                    print "\nCommand : ", cmd;
                    tdkTestObj.addParameter("command", cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult1 = tdkTestObj.getResult();
                    syscfgGet = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    print "TEST STEP %d : Get the Adv_AdvSecOTMRFCEnable from syscfg.db" %step;
                    print "EXPECTED RESULT %d : Should get the Adv_AdvSecOTMRFCEnable value from syscfg.db successfully" %step;

                    if expectedresult in actualresult and syscfgGet != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Current syscfg get value is : %s" %(step, syscfgGet);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Need to convert syscfg get value  0/1 to false/true
                        enable = syscfgGet;
                        if syscfgGet == "1":
                            enable = "true";
                        elif syscfgGet == "0":
                            enable = "false";

                        step = step + 1;
                        print "\nTEST STEP %d : Cross check the RFC Advanced Security OTM Enable via syscfg and TR181 with the set value" %step;
                        print "EXPECTED RESULT %d: RFC Advanced Security OTM Enable status should be equal to that of set value" %step;
                        print "TR181 get value : %s" %curr_value;
                        print "syscfg get value : %s" %syscfgGet;
                        print "RFC value set : %s" %setValue

                        if enable == setValue and curr_value == setValue :
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: The value set is reflected in TR181 and syscfg get" %step;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Check if the required logging pattern is seen in agent.txt when RFC is disabled
                            sleep(10);
                            #Get the final line count of "ADVANCE_SECURITY_OTM_ENABLED"
                            print "\nGet the current number of log lines of \"ADVANCE_SECURITY_OTM_ENABLED\"";
                            step = step + 1;
                            count_final = getLogFileTotalLinesCount(sysTestObj, file, search_string, step);

                            step = step + 1;
                            print "\nTEST STEP %d: Check if the expected log line is incremented by 1 after the RFC disable" %step;
                            print "EXPECTED RESULT %d: The expected log line should be incremented by 1 after the RFC disable" %step;

                            if (count_final - count_initial) == 1:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print"ACTUAL RESULT %d: The required logging pattern in found in agent.txt after RFC change" %step;
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print"ACTUAL RESULT %d:The required logging pattern in not found in agent.txt after RFC change" %step;
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: The value set is not reflected in get" %step;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Current syscfg get value is : %s" %(step, syscfgGet);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Get operation failed after set; Details : %s" %(step, curr_value);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: The RFC value not set successfully; Details : %s" %(step, result);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            if initial_value != setValue:
                tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
                result, actualresult = set_parameter(tdkTestObj, paramName, initial_value, expectedresult);

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Revert operation is success";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Revert operation failed";
            else :
                print "Revert operation not required";
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "Unable to enable RFC Advanced Security OTM Enable initially";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Get operation failed; Details : %s" %initial_value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam/sysutil module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
