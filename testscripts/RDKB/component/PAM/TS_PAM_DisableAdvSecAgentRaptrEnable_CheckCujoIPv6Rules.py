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
  <name>TS_PAM_DisableAdvSecAgentRaptrEnable_CheckCujoIPv6Rules</name>
  <primitive_test_id/>
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the number of Cujo IPv6 rules present in firewall is the same before and after disabling the Advanced Security Raptr Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvSecAgentRaptr.Enable.</synopsis>
  <groups_id/>
  <execution_time>3</execution_time>
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
    <test_case_id>TC_PAM_249</test_case_id>
    <test_objective>Check if the number of Cujo IPv6 rules present in firewall is the same before and after disabling the Advanced Security Raptr Enable RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvSecAgentRaptr.Enable.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvSecAgentRaptr.Enable
ParamValue : true/false
Type : boolean
</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial state of the RFC Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvSecAgentRaptr.Enable
3. If its not enabled initially, set to enable
4. Check the number of Cujo IPv6 rules present in the firewall when the Raptr RFC is in enabled state.
5. Copy the Cujo IPv6 rules to a temporary location
6. Now, disable the Raptr Enable RFC using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvSecAgentRaptr.Enable
7. Check the number of Cujo IPv6 rules present in the firewall, it should be the same as the number of rules present before Raptr RFC is disabled
8. Redirect the current Cujo IPv6 rules to another temporary location
9. Perform the diff operation of the files storing the Cujo IPv6 rules before and after Raptr RFC was disabled.
10. Check if the Cujo IPv6 rules remain unchanged.
11. Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvSecAgentRaptr.Enable if required
12. Unload the modules</automation_approch>
    <expected_output>The number of Cujo IPv6 rules present in the firewall should remain unchanged before and after the Raptr RFC parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvSecAgentRaptr.Enable is disabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_DisableAdvSecAgentRaptrEnable_CheckCujoIPv6Rules</test_script>
    <skipped>No</skipped>
    <release_version>M103</release_version>
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
pamobj.configureTestCase(ip,port,'TS_PAM_DisableAdvSecAgentRaptrEnable_CheckCujoIPv6Rules');
sysobj.configureTestCase(ip,port,'TS_PAM_DisableAdvSecAgentRaptrEnable_CheckCujoIPv6Rules');

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

    #Get the initial enable status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvSecAgentRaptr.Enable
    paramName ="Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvSecAgentRaptr.Enable";
    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
    initial_value, actualresult = get_parameter(tdkTestObj, paramName, expectedresult);

    print "\nTEST STEP 1: Get the initial value of RFC Advanced Security Raptr Enable using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvSecAgentRaptr.Enable";
    print "EXPECTED RESULT 1: Should successfully get the initial value of RFC Advanced Security Raptr Enable";

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Initial value is : %s" %initial_value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check if the RFC is enabled, if not enable it
        flag = 0;
        step = 2;

        if initial_value == "false":
            setValue ="true";
            tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
            result, actualresult = set_parameter(tdkTestObj, paramName, setValue, expectedresult);

            print "\nTEST STEP %d: Set RFC Advanced Security Raptr Enable to %s before disabling the RFC again" %(step, setValue);
            print "EXPECTED RESULT %d: Should successfully set RFC Advanced Security Raptr Enable status to %s before disabling the RFC again" %(step, setValue);

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
            print "RFC Advanced Security Raptr Enable is already in enabled state initially";

        if flag == 1:
            #Get the number of Cujo rules present in firewall before Raptr RFC is disabled
            cmd= "ip6tables-save | grep CUJO | wc -l";
            print "\nCommand : ", cmd;
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            actualresult, ipv6rules_initial = doSysutilExecuteCommand(tdkTestObj,cmd);

            print "\nTEST STEP %d : Get the number of Cujo IPv6 rules present in firewall before Advanced Security Raptr RFC is disabled" %step;
            print "EXPECTED RESULT %d : Should get the number of Cujo IPv6 rules present in firewall before Advanced Security Raptr RFC is disabled successfully" %step;

            if expectedresult in actualresult and ipv6rules_initial.isdigit():
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Number of Cujo IPv6 rules present in firewall before Advanced Security Raptr RFC is disabled is : %s" %(step, ipv6rules_initial);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #If Cujo IPv6 firewall rules are present then copy them to a log file
                if int(ipv6rules_initial) > 0:
                    #Copy the rules to a log file under /tmp
                    step = step + 1;
                    cmd= "ip6tables-save | grep CUJO >> /tmp/Raptr_initial.log";
                    print "\nCommand : ", cmd;
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                    print "\nTEST STEP %d : Copy Cujo IPv6 rules present in firewall before Advanced Security Raptr RFC is disabled to a log file" %step;
                    print "EXPECTED RESULT %d : Should copy the Cujo IPv6 rules present in firewall before Advanced Security Raptr successfully to a log file" %step;

                    if expectedresult in actualresult and details == "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Cujo IPv6 rules present in firewall before Advanced Security Raptr RFC is disabled is copied successfully" %(step);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Disable the Raptr Enable RFC
                        step = step + 1;
                        setValue ="false";
                        tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
                        result, actualresult = set_parameter(tdkTestObj, paramName, setValue, expectedresult);

                        print "\nTEST STEP %d: Set RFC Advanced Security Raptr Enable to %s" %(step, setValue);
                        print "EXPECTED RESULT %d: Should successfully set RFC Advanced Security Raptr Enable status to %s" %(step, setValue);

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: The RFC value set successfully; Details : %s" %(step, result);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Sleep for 10s
                            print "Sleep for 10s before checking the CUJO IPv6 rules";
                            sleep(10);

                            #Get the number of Cujo rules present in firewall after Raptr RFC is disabled
                            step = step + 1;
                            cmd= "ip6tables-save | grep CUJO | wc -l";
                            print "\nCommand : ", cmd;
                            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                            actualresult, ipv6rules_final = doSysutilExecuteCommand(tdkTestObj,cmd);

                            print "\nTEST STEP %d : Get the number of Cujo IPv6 rules present in firewall after Advanced Security Raptr RFC is disabled" %step;
                            print "EXPECTED RESULT %d : Should get the number of Cujo IPv6 rules present in firewall after Advanced Security Raptr RFC is disabled successfully" %step;

                            if expectedresult in actualresult and ipv6rules_final.isdigit():
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: Number of Cujo IPv6 rules present in firewall after Advanced Security Raptr RFC is disabled is : %s" %(step, ipv6rules_final);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                #If Cujo IPv6 firewall rules are present then copy them to a log file
                                if int(ipv6rules_final) > 0:
                                    #Copy the rules to a log file under /tmp
                                    step = step + 1;
                                    cmd= "ip6tables-save | grep CUJO >> /tmp/Raptr_final.log";
                                    print "\nCommand : ", cmd;
                                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                                    actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                                    print "\nTEST STEP %d : Copy Cujo IPv6 rules present in firewall after Advanced Security Raptr RFC is disabled to a log file" %step;
                                    print "EXPECTED RESULT %d : Should copy the Cujo IPv6 rules present in firewall after Advanced Security Raptr successfully to a log file" %step;

                                    if expectedresult in actualresult and details == "":
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT %d: Cujo IPv6 rules present in firewall after Advanced Security Raptr RFC is disabled is copied successfully" %(step);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS";

                                        #Check if the number of Cujo IPv6 rules before and after Advanced Security Raptr RFC is disabled is the same
                                        step = step + 1;
                                        print "\nTEST STEP %d : Check if the number of Cujo IPv6 rules before and after Advanced Security Raptr RFC is disabled is the same" %step;
                                        print "EXPECTED RESULT %d : Cujo IPv6 rules before and after Advanced Security Raptr RFC is disabled should be the same" %step;
                                        print "Number of Cujo IPv6 rules before Rapt RFC is disabled : ", ipv6rules_initial;
                                        print "Number of Cujo IPv6 rules after Rapt RFC is disabled : ", ipv6rules_final;

                                        if ipv6rules_final == ipv6rules_initial :
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "ACTUAL RESULT %d: Cujo IPv6 rules before and after Advanced Security Raptr RFC is disabled is the same" %(step);
                                            #Get the result of execution
                                            print "[TEST EXECUTION RESULT] : SUCCESS";
                                        else :
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "ACTUAL RESULT %d: Cujo IPv6 rules before and after Advanced Security Raptr RFC is disabled is NOT the same" %(step);
                                            #Get the result of execution
                                            print "[TEST EXECUTION RESULT] : FAILURE";

                                        #Compare the Cujo IPv6 rules after and before Advanced Security Raptr RFC is disabled after sorting the rules
                                        step = step + 1;
                                        cmd= "sort -o /tmp/Raptr_final.log /tmp/Raptr_final.log; sort -o /tmp/Raptr_initial.log /tmp/Raptr_initial.log; diff /tmp/Raptr_final.log /tmp/Raptr_initial.log | wc -l";
                                        print "\nCommand : ", cmd;
                                        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                                        actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                                        print "\nTEST STEP %d : Check if there is any difference in the Cujo IPv6 rules before and after Advanced Security Raptr RFC is disabled" %step;
                                        print "EXPECTED RESULT %d : There should not be any difference in the Cujo IPv6 rules before and after Advanced Security Raptr RFC is disabled" %step;

                                        if expectedresult in actualresult and details.isdigit():
                                            #Check the number of lines for the diff output, if it is 0 then the rules are the same before and after RFC is disabled
                                            if int(details) == 0:
                                                tdkTestObj.setResultStatus("SUCCESS");
                                                print "ACTUAL RESULT %d: No difference in the Cujo IPv6 rules before and after Advanced Security Raptr RFC is disabled" %(step);
                                                #Get the result of execution
                                                print "[TEST EXECUTION RESULT] : SUCCESS";
                                            else :
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print "ACTUAL RESULT %d: Cujo IPv6 rules before and after Advanced Security Raptr RFC is disabled is NOT the same" %(step);
                                                #Get the result of execution
                                                print "[TEST EXECUTION RESULT] : FAILURE";
                                        else :
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "ACTUAL RESULT %d: Command not executed properly" %(step);
                                            #Get the result of execution
                                            print "[TEST EXECUTION RESULT] : FAILURE";

                                        #Delete the log file created
                                        cmd= "rm -rf /tmp/Raptr_final.log";
                                        print "\nCommand : ", cmd;
                                        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                                        actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                                        if expectedresult in actualresult and details == "":
                                            #Set the result status of execution
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "Log file deleted successfully";
                                        else:
                                            #Set the result status of execution
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "Log file is NOT deleted successfully";
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT %d: Cujo IPv6 rules present in firewall after Advanced Security Raptr RFC is disabled is NOT copied successfully" %(step);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "No Cujo IPv6 rules are present in the DUT";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: Number of Cujo IPv6 rules present in firewall before Advanced Security Raptr RFC is disabled is : %s" %(step, ipv6rules_final);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: The RFC value NOT set successfully; Details : %s" %(step, result);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";

                        #Delete the log file created
                        cmd= "rm -rf /tmp/Raptr_initial.log";
                        print "\nCommand : ", cmd;
                        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                        actualresult, details = doSysutilExecuteCommand(tdkTestObj,cmd);

                        if expectedresult in actualresult and details == "":
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "Log file deleted successfully";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "Log file is NOT deleted successfully";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Cujo IPv6 rules present in firewall before Advanced Security Raptr RFC is disabled is NOT copied successfully" %(step);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "No Cujo IPv6 rules are present in the DUT";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Number of Cujo IPv6 rules present in firewall before Advanced Security Raptr RFC is disabled is : %s" %(step, ipv6rules_initial);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert Operation
            if initial_value != setValue:
                step = step + 1;
                tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
                result, actualresult = set_parameter(tdkTestObj, paramName, initial_value, expectedresult);

                print "\nTEST STEP %d : Revert RFC Advanced Security Raptr Enable to the initial state %s" %(step, initial_value);
                print "EXPECTED RESULT %d : RFC Advanced Security Raptr Enable should be reverted successfully" %step;

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : Revert operation is success; Details : %s" %(step, result);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : Revert operation failed; Details : %s" %(step, result);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else :
               print "\nRevert operation of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.AdvSecAgentRaptr.Enable not required";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "RFC Advanced Security Raptr Enable could not be enabled";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Initial value is : %s" %initial_value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam/sysutil module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
