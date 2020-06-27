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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_PAM_SetFirewallSecurityIPv4PortScanProtect</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Validate whether iptable rules(Ipv4) associated with  PortScanProtect is added/removed into iptables for Enable/Disable on the PortScanProtect TR181 parameter</synopsis>
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
    <box_type>Broadband</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_191</test_case_id>
    <test_objective>
To Validate whether Iptable rules(Ipv4) associated with  PortScanProtect is added/removed into iptables for Enable/Disable the PortScanProtect TR181 parameter</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.Firewall.X_RDKCENTRAL-COM_Security.V4.PortScanProtect
</input_parameters>
    <automation_approch>1. Load the PAM Module
2. Get the current value of PortScanProtect parameter and store it
3. If the current value is True then Verify whether all iptables rules associated with PortScanProtect was added into iptables, if the verification was success, set the parameter value to False, then verify all iptables rules associated with PortScanProtect was removed from iptables
4. If the current value is false then verify whether all iptables rules associated with PortScanProtect was not added into iptables, if the verification was success, set the parameter value to true, then verify all iptables rules associated with PortScanProtect was added into iptables
5. Verification on Enabled/Disabled both cases should be success
6. Revert the value to the initial value
7. Unload the Module</automation_approch>
    <expected_output>The iptables rules associated with IPFloodDetect should be added into iptables on Enabled and should be removed on Disabled case of IPFloodDetect TR181 parameter
</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_SetFirewallSecurityIPv4PortScanProtect</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_SetFirewallSecurityIPv4PortScanProtect');
sysobj.configureTestCase(ip,port,'TS_PAM_SetFirewallSecurityIPv4PortScanProtect');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysutilloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus ;

def set_firewall_security_portscan(tdkTestObj,set_value):
    tdkTestObj.addParameter("ParamName","Device.Firewall.X_RDKCENTRAL-COM_Security.V4.PortScanProtect");
    tdkTestObj.addParameter("ParamValue",set_value);
    tdkTestObj.addParameter("Type","boolean");
    expectedresult="SUCCESS";
    #Execute testcase on DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    result = tdkTestObj.getResultDetails();
    return actualresult, result;

def verify_iptable_rules(tdkTestObj,enabled):
    iptable_list = ["-N PORT_SCAN_CHK","-N PORT_SCAN_DROP", "-A INPUT -j PORT_SCAN_CHK", "-A FORWARD -j PORT_SCAN_CHK","-A PORT_SCAN_CHK -i erouter0 -j RETURN", "-A PORT_SCAN_CHK -i lo -j RETURN", "-A PORT_SCAN_CHK -p udp -m recent --rcheck --seconds 86400 --name portscan --mask 255.255.255.255 --rsource -j PORT_SCAN_DROP", "-A PORT_SCAN_CHK -p tcp -m recent --rcheck --seconds 86400 --name portscan --mask 255.255.255.255 --rsource -j PORT_SCAN_DROP", "-A PORT_SCAN_DROP -j DROP"]
    for list in iptable_list:
	cmd = "iptables -S | grep -ire \"%s\"" %list;
	tdkTestObj.addParameter("command",cmd);
	tdkTestObj.executeTestCase(expectedresult);
	actualresult = tdkTestObj.getResult();
	details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if enabled == "true":
            if expectedresult in actualresult and details == list:
                rulesFound = 1;
            else:
                rulesFound = 0;
                print "Iptable Rule %s is NOT present"%list
                break;
        else:
            if expectedresult in actualresult and details == "":
                rulesFound = 0;
            else:
                rulesFound = 1;
                print "Iptable Rule %s is present"%list
                break;
    return rulesFound;

if "SUCCESS" in (loadmodulestatus.upper() and sysutilloadmodulestatus.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    revertFlag = 0;

    tdkTestObj = obj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.Firewall.X_RDKCENTRAL-COM_Security.V4.PortScanProtect");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    initial_value = tdkTestObj.getResultDetails().strip();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get current value of IPv4 PortScanProtect"
        print "EXPECTED RESULT 1: Should get current value of  IPv4 PortScanProtect"
        print "ACTUAL RESULT 1: current value is %s" %initial_value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        if initial_value == "true":
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            enable_verify = verify_iptable_rules(tdkTestObj,"true");

            if enable_verify == 1:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Verify iptables rules for IPv4 PortScanProtect for True"
                print "EXPECTED RESULT 2: The iptables rules specific to IPv4 PortScanProtect should be present"
                print "ACTUAL TEST 2: Verification on the iptables rules specific to IPv4 PortScanProtect - Enabled is success"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"

                #set to False
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                set_disable_res,set_disable_details = set_firewall_security_portscan (tdkTestObj,"false");
                #wait upto 1 min to complete firewall restart
                sleep(60);

                if expectedresult in set_disable_res:
                    revertFlag = 1;
    		    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Set IPv4 PortScanProtect value to False"
                    print "EXPECTED RESULT 3: The Set Operation should be success"
                    print "ACTUAL TEST 3: The set operation to make IPv4 PortScanProtect as False was success"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"

                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    disable_verify = verify_iptable_rules(tdkTestObj,"false");

                    if disable_verify == 0:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4: Verify iptables rules for IPv4 PortScanProtect for False"
                        print "EXPECTED RESULT 4: The iptables rules specific to IPv4 PortScanProtect should not be present"
                        print "ACTUAL TEST 4: Verification on the iptables rules specific to IPv4 PortScanProtect Disabled is success"
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS"

                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Verify iptables rules for IPv4 PortScanProtect for False"
                        print "EXPECTED RESULT 4: The iptables rules specific to IPv4 PortScanProtect should not be present"
                        print "ACTUAL TEST 4: Verification on the iptables rules specific to IPv4 PortScanProtect Disabled  is failed"
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Set IPv4 PortScanProtect value to False"
                    print "EXPECTED RESULT 3: The Set Operation should be success"
                    print "ACTUAL TEST 3: The set operation to make IPv4 PortScanProtect as False was Failed"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Verify iptables rules for IPv4 PortScanProtect for True"
                print "EXPECTED RESULT 2: The iptables rules specific to IPv4 PortScanProtect should be present"
                print "ACTUAL TEST 2: Verification on the iptables rules specific to IPv4 PortScanProtect Enabled is failed"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"

        else:
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            disable_verify = verify_iptable_rules(tdkTestObj,"false");

            if disable_verify == 0:
                print "Iptables Rules are verified for False"
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Verify iptables rules for IPv4 PortScanProtect for False"
                print "EXPECTED RESULT 2: The iptables rules specific to IPv4 PortScanProtect should not be present"
                print "ACTUAL TEST 2: Verification on the iptables rules specific to IPv4 PortScanProtect Disabled is success"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"

                #set to True
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                set_enable_res,set_enable_details = set_firewall_security_portscan (tdkTestObj,"true");
                # wait upto 1 min to complete firewall restart
                sleep(60);

                if expectedresult in set_enable_res:
                    revertFlag = 1;
    		    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Set IPv4 PortScanProtect value to True"
                    print "EXPECTED RESULT 3: The Set Operation should be success"
                    print "ACTUAL TEST 3: The set operation to make IPv4 PortScanProtect as True was success"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"

                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    enable_verify = verify_iptable_rules(tdkTestObj,"true");

                    if enable_verify == 1:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4: Verify iptables rules for IPv4 PortScanProtect for False"
                        print "EXPECTED RESULT 4: The iptables rules specific to IPv4 PortScanProtect should be present"
                        print "ACTUAL TEST 4: Verification on the iptables rules specific to IPv4 PortScanProtect Enabled is success"
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Verify iptables rules for IPv4 PortScanProtect for False"
                        print "EXPECTED RESULT 4: The iptables rules specific to IPv4 PortScanProtect should be present"
                        print "ACTUAL TEST 4: Verification on the iptables rules specific to IPv4 PortScanProtect Enabled is failed"
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE"

                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Set IPv4 PortScanProtect value to True"
                    print "EXPECTED RESULT 3: The Set Operation should be success"
                    print "ACTUAL TEST 3: The set operation to make IPv4 PortScanProtect as True was Failed"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"

            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Verify iptables rules for IPv4 PortScanProtect for False"
                print "EXPECTED RESULT 2: The iptables rules specific to IPv4 PortScanProtect should not be present"
                print "ACTUAL TEST 2: Verification on the iptables rules specific to IPv4 PortScanProtect Disabled is failed"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"

        #Revert the Value
        if revertFlag ==1:
            if initial_value == "true":
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                revert_set_result,revert_set_details = set_firewall_security_portscan (tdkTestObj,"true");

                if expectedresult in revert_set_result:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Revert the value to True"
                    print "EXPECTED RESULT 5: The Set Operation for revert  should be success"
                    print "ACTUAL TEST 5: The Revert set operation was success"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP 5: Revert the value to True"
                    print "EXPECTED RESULT 5: The Set Operation for revert  should be success"
                    print "ACTUAL TEST 5: The Revert set operation was Failed"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
	    else:
                tdkTestObj = obj.createTestStep('pam_SetParameterValues');
                revert_set_result,revert_set_details = set_firewall_security_portscan (tdkTestObj,"false");

                if expectedresult in revert_set_result:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Revert the value to False"
                    print "EXPECTED RESULT 5: The Set Operation for revert  should be success"
                    print "ACTUAL TEST 5: The Revert set operation was success"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Revert the value to False"
                    print "EXPECTED RESULT 5: The Set Operation for revert  should be success"
                    print "ACTUAL TEST 5: The Revert set operation was Failed"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            print "Revert flag was not enabled, No need to revert the value"

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get current value of PortScanProtect"
        print "EXPECTED RESULT 1: Should get current value of PortScanProtect"
        print "ACTUAL RESULT 1: Status is %s" %actualresult;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("pam");
    sysobj.unloadModule("sysutil");

else:
    print "Failed to load pam/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

