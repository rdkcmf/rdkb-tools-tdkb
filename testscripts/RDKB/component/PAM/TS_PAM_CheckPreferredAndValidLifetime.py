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
  <name>TS_PAM_CheckPreferredAndValidLifetime</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the TR181 values of Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_PreferredLifetime and Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_ValidLifetime match with the values of preferred-lifetime and valid-lifetime from dibbler server.conf file.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_PAM_222</test_case_id>
    <test_objective>To check if the TR181 values 	of Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_PreferredLifetime and Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_ValidLifetime match with the values of preferred-lifetime and valid-lifetime from dibbler server.conf file.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_PreferredLifetime
ParamName : Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_ValidLifetime</input_parameters>
    <automation_approch>1. Load the modules.
2. Get the TR181 values of Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_PreferredLifetime and Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_ValidLifetime.
3. Cross check if the lifetime values retrieved are the same as the values stored in dibbler server.conf file.
4. Unload the modules</automation_approch>
    <expected_output>The TR181 values 	of Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_PreferredLifetime and Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_ValidLifetime should match with the values of preferred-lifetime and valid-lifetime from dibbler server.conf file.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_CheckPreferredAndValidLifetime</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
obj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_PAM_CheckPreferredAndValidLifetime');
obj.configureTestCase(ip,port,'TS_PAM_CheckPreferredAndValidLifetime');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Check if the /etc/dibbler/server.conf is present in the device
    step = 1;
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    cmd = "[ -f /etc/dibbler/server.conf ] && echo \"File exist\" || echo \"File does not exist\"";
    print "Command : ",cmd;
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP 1: Check for /etc/dibbler/server.conf file presence";
    print "EXPECTED RESULT 1: /etc/dibbler/server.conf file should be present";

    if expectedresult in actualresult and details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: /etc/dibbler/server.conf file is present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Get the TR181 value of Preferred Lifetime and Valid Lifetime
        Params = ["Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_PreferredLifetime", "Device.IP.Interface.1.IPv6Prefix.1.X_CISCO_COM_ValidLifetime"];
        search_words = ["prefered-lifetime", "valid-lifetime"];

        for index in range(0,2):
            step = step + 1;
            tdkTestObj = obj.createTestStep("pam_GetParameterValues");
            tdkTestObj.addParameter("ParamName",Params[index]);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP %d: Get the value of %s" %(step, Params[index]);
            print "EXPECTED RESULT %d: Should successfully get the value of %s" %(step, Params[index]);

            if expectedresult in actualresult:
                tr181_value = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Parameter value retrieved successfully; Details : %s" %(step, tr181_value);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the parameter value is non-empty and valid
                if tr181_value != "" and tr181_value.isdigit():
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "The parameter value is non-empty and valid";

                    #Verify the TR181 value with the value in /etc/dibbler/server.conf file
                    step = step + 1;
                    print "\nTEST STEP %d: Get the value of %s from /etc/dibbler/server.conf" %(step, search_words[index]);
                    print "EXPECTED RESULT %d: The value of %s should be retrieved from /etc/dibbler/server.conf" %(step, search_words[index]);

                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    cmd = "cat /etc/dibbler/server.conf | grep " + search_words[index];
                    print "Command : ", cmd;
                    tdkTestObj.addParameter("command",cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details != "":
                        value = details.split("lifetime ")[1].strip().replace("\\n", "");

                        if value.isdigit():
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Value of %s from /etc/dibbler/server.conf is %s" %(step, search_words[index], value);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            step = step + 1;
                            print "\nTEST STEP %d: Check if the TR181 value matches with the value in /etc/dibbler/server.conf" %step;
                            print "EXPECTED RESULT %d: The TR181 value should match with the value in /etc/dibbler/server.conf" %step;
                            print "TR181 value : %s"%tr181_value;
                            print "Value from /etc/dibbler/server.conf : %s"%value;

                            if value == tr181_value:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: Both the values match" %step;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: Both the values do not match" %step;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Value of %s from /etc/dibbler/server.conf is %s" %(step, search_words[index], value);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Value of %s from /etc/dibbler/server.conf is %s" %(step, search_words[index], details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "The parameter value is invalid";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Parameter value not retrieved successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: /etc/dibbler/server.conf file is not present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
