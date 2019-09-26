##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SNMP_SetFirewallProtection</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>GetCommString</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set the firewall protection as low/medium/high/custom</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <box_type>Emulator</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SNMP_PA_05</test_case_id>
    <test_objective>To set the firewall protection to High</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,XB3</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>snmpMethod :snmpget
snmpVersion : -v 2c
OID : 1.3.6.1.4.1.17270.50.2.4.1.1.0</input_parameters>
    <automation_approch>1.Function which needs to be tested will be configured in Test Manager GUI.
2.Python Script will be generated by Test Manager with provided arguments in configure page. 
3.TM will load the snmp_pa library via Test agent
4.From python script, invoke SnmpExecuteCmd function in snmplib to get the value of given OID 
5. GetCommString function in the SNMP_PA stub  will be called from snmplib to get the community string. 
6.Responses from the snmplib will be logged in Script log.
7. Validation of  the result is done within the python script and send the result status to Test Manager.
8.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from pam stub.</automation_approch>
    <except_output>CheckPoint 1:
  Response of snmp command should be logged in the script log

CheckPoint 2:
Stub and lib function result should be success and should see corresponding log in the script log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>GetCommString</test_stub_interface>
    <test_script>TS_SNMP_SetFirewallProtection</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import snmplib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SNMP_SetFirewallProtection');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    
    #Get the Community String
    commGetStr = snmplib.getCommunityString(obj,"snmpget");
    commSetStr = snmplib.getCommunityString(obj,"snmpset");
    #Get the IP Address
    ipaddress = snmplib.getIPAddress(obj);
    ########## Script to Execute the snmp command ###########
    actResponse =snmplib.SnmpExecuteCmd("snmpget", commGetStr, "-v 2c", "1.3.6.1.4.1.17270.50.2.4.1.1.0", ipaddress);
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.executeTestCase("SUCCESS");

    if "=" in actResponse :
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: snmpget request to get current firewall protection level";
        print "EXPECTED RESULT 1: Command should return current firewall protection level";
        print "ACTUAL RESULT 1: %s" %actResponse;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        org_value = actResponse.rsplit(None, 1)[-1];
        print "Current firewall protection level is %s " %org_value;
        #Set the status of MocaDevice as true
        actResponse =snmplib.SnmpExecuteCmd("snmpset", commSetStr, "-v 2c", "1.3.6.1.4.1.17270.50.2.4.1.1.0 i 2", ipaddress);
        sleep(5);
        actResponse =snmplib.SnmpExecuteCmd("snmpget", commGetStr, "-v 2c", "1.3.6.1.4.1.17270.50.2.4.1.1.0", ipaddress);
        act_value=actResponse.rsplit(None, 1)[-1];
        if act_value and "2" in act_value:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: snmpget request to get firewall protection level";
            print "EXPECTED RESULT 2: Command should return firewall protection level as 2";
            print "ACTUAL RESULT 2: %s" %actResponse;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
            actResponse =snmplib.SnmpExecuteCmd("snmpset", commSetStr, "-v 2c", "1.3.6.1.4.1.17270.50.2.4.1.1.0 i %s" %org_value, ipaddress);
            sleep(5);
            actResponse =snmplib.SnmpExecuteCmd("snmpget", commGetStr, "-v 2c", "1.3.6.1.4.1.17270.50.2.4.1.1.0", ipaddress);
            def_value=actResponse.rsplit(None, 1)[-1];
            if def_value and org_value in def_value:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: snmpget request to get firewall protection level";
                print "EXPECTED RESULT 3: Command should return firewall protection level";
                print "ACTUAL RESULT 3: %s" %actResponse;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
	    else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: snmpget request to get firewall protection level";
                print "EXPECTED RESULT 3: Command should return firewall protection level";
                print "ACTUAL RESULT 3: %s" %actResponse;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: snmpget request to get firewall protection level";
            print "EXPECTED RESULT 2: Command should return firewall protection level as 3";
            print "ACTUAL RESULT 2: %s" %actResponse;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: snmpget request to get current firewall protection level";
        print "EXPECTED RESULT 1: Command should return current firewall protection level";
        print "ACTUAL RESULT 1: %s" %actResponse;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("sysutil");
else:
        print "FAILURE to load SNMP_PA module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading FAILURE";

