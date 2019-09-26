##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_SNMP_Check_NotifyComp_OnBridgeMode</name>
  <primitive_test_id/>
  <primitive_test_name>GetCommString</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Enable bridge mode via snmpset and check if notify_comp app is not crashed</synopsis>
  <groups_id/>
  <execution_time>0</execution_time>
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
    <test_case_id>TC_SNMP_PA_41</test_case_id>
    <test_objective>Enable bridge mode via snmpset and check if notify_comp app is not crashed</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>snmpMethod : snmpset, snmpget
snmpVersion : -v 2c
OID : 1.3.6.1.4.1.17270.50.2.3.2.1.1.32</input_parameters>
    <automation_approch>1. Load SNMP module
2. Check if notify_comp process is running or not
3. Get the lanmode of the device
4. If lan mode is router, change it to bridge static
5. check if the notify_comp process is running or not
6. Revert the lanmode to router
7. Unload module</automation_approch>
    <except_output>Notify_comp process should be running even after enabling bridge-mode via snmp</except_output>
    <priority>High</priority>
    <test_stub_interface>SNMP_PA</test_stub_interface>
    <test_script>TS_SNMP_Check_NotifyComp_OnBridgeMode</test_script>
    <skipped>No</skipped>
    <release_version>M67</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import snmplib;
from tdkbVariables import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SNMP_Check_NotifyComp_OnBridgeMode');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #check whether the process is running or not
    query="sh %s/tdk_platform_utility.sh checkProcess notify_comp" %TDK_PATH
    print "query:%s" %query
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", query)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase("SUCCESS");
    actualresult = tdkTestObj.getResult();
    pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
    if expectedresult in actualresult and pid:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1:Check notify_comp process";
        print "EXPECTED RESULT 1: notify_comp process should be running";
        print "ACTUAL RESULT 1: pid of notify_comp %s" %pid;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Get the Community String
        communityString = snmplib.getCommunityString(obj,"snmpget");
        commSetStr = snmplib.getCommunityString(obj,"snmpset");
        #Get the IP Address
        ipaddress = snmplib.getIPAddress(obj);
        actResponse =snmplib.SnmpExecuteCmd("snmpget", communityString, "-v 2c", "1.3.6.1.4.1.17270.50.2.3.2.1.1.32", ipaddress);
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.executeTestCase("SUCCESS");

        if "SNMPv2-SMI" in actResponse:
	    lanmode = actResponse.split("INTEGER:")[1].strip()
	    if lanmode == "2":
	        lanMode = "router";
	    elif lanmode == "1":
	        lanMode = "bridge-static";
	    else:
	        lanMode = "Invalid lan Mode";

	    if lanMode != "Invalid lan Mode":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2:Execute snmpget for lanmode";
                print "EXPECTED RESULT 2: snmpget should get the lanmode";
                print "ACTUAL RESULT 2: lanmode is %s" %lanMode;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

	        #set lanmode as bridge-static
	        if lanMode != "bridge-static":
		    actResponse =snmplib.SnmpExecuteCmd("snmpset", commSetStr, "-v 2c", "1.3.6.1.4.1.17270.50.2.3.2.1.1.32 i 1", ipaddress);
		    sleep(5);
		    actResponse =snmplib.SnmpExecuteCmd("snmpget", communityString, "-v 2c", "1.3.6.1.4.1.17270.50.2.3.2.1.1.32", ipaddress);
		    if "SNMPv2-SMI" in actResponse:
			lanmode_new = actResponse.split("INTEGER:")[1].strip()
			if lanmode_new == "1":
			    tdkTestObj.setResultStatus("SUCCESS");
                	    print "TEST STEP 3:Set the lanmode as bridge-static";
                	    print "EXPECTED RESULT 3: Should the lanmode as bridge-static";
                	    #Get the result of execution
                	    print "[TEST EXECUTION RESULT] : SUCCESS";

			    #check whether the process is running or not
            		    query="sh %s/tdk_platform_utility.sh checkProcess notify_comp" %TDK_PATH
            		    print "query:%s" %query
            		    tdkTestObj = obj.createTestStep('ExecuteCmd');
            		    tdkTestObj.addParameter("command", query)
            		    expectedresult="SUCCESS";
            		    tdkTestObj.executeTestCase("SUCCESS");
            		    actualresult = tdkTestObj.getResult();
            		    pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
            		    if expectedresult in actualresult and pid:
            		        tdkTestObj.setResultStatus("SUCCESS");
            		        print "TEST STEP 4:Check notify_comp process";
            		        print "EXPECTED RESULT 4: notify_comp process should be running";
            		        print "ACTUAL RESULT 4: pid of notify_comp %s" %pid;
            		        #Get the result of execution
            		        print "[TEST EXECUTION RESULT] : SUCCESS";
			    else:
				tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 4:Check notify_comp process";
                                print "EXPECTED RESULT 4: notify_comp process should be running";
                                print "ACTUAL RESULT 4: pid of notify_comp %s" %pid;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
			else:
			    tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 3:Set the lanmode as bridge-static";
                            print "EXPECTED RESULT 3: Should set the lanmode as bridge-static";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
			#Reset the value of lan mode
                        actResponse =snmplib.SnmpExecuteCmd("snmpset", commSetStr, "-v 2c", "1.3.6.1.4.1.17270.50.2.3.2.1.1.32 i 2", ipaddress);
                        sleep(5);
                        actResponse =snmplib.SnmpExecuteCmd("snmpget", communityString, "-v 2c", "1.3.6.1.4.1.17270.50.2.3.2.1.1.32", ipaddress);
                        if "SNMPv2-SMI" in actResponse:
                            lanmode_revert = actResponse.split("INTEGER:")[1].strip()
                            if lanmode_revert == lanmode:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 5:Set the lanmode to previous value";
                                print "EXPECTED RESULT 5: Should set the lanmode to previous value";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 5:Set the lanmode to previous value";
                                print "EXPECTED RESULT 5: Should set the lanmode to previous value";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
			else:
			    tdkTestObj.setResultStatus("FAILURE");
			    print "Failed to execute snmp command to set lanmode"
		    else:
			tdkTestObj.setResultStatus("FAILURE");
			print "Failed to set the lanmode through snmp"
			print "Details: %s" %actResponse
		else:
		    print "\nLanmode is already bridge-static and notify_comp process is running\n"

	    else:
		tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2:Execute snmpget for lanmode";
                print "EXPECTED RESULT 2: snmpget should get the lanmode";
                print "ACTUAL RESULT 2: lanmode is %s" %lanMode;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
	    print "Failed to execute snmp command to get the lan mode"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:Check notify_comp process";
        print "EXPECTED RESULT 1: notify_comp process should be running";
        print "ACTUAL RESULT 1: %s" %pid;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("sysutil");
else:
        print "FAILURE to load SNMP_PA module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading FAILURE";				
