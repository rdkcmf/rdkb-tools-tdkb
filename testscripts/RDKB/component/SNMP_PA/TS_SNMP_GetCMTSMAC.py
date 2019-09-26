##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SNMP_GetCMTSMAC</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>GetCommString</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>With snmpget retrieve the Device CMTS MAC Address</synopsis>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SNMP_PA_19</test_case_id>
    <test_objective>With snmpget retrieve the Device CMTS MAC Address</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB6</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>GetCommString
ExecuteCmd</api_or_interface_used>
    <input_parameters>SnmpMethod : snmpget
SnmpVersion : v2c
OID : 1.3.6.1.2.1.10.127.1.2.1.1.1.2

dmcli eRT getv Device.DeviceInfo.X_RDKCENTRAL-COM_CMTS_MAC</input_parameters>
    <automation_approch>1.TM will load the snmp_pa and sysutil library via Test agent
2.From python script, invoke SnmpExecuteCmd function in snmplib to get the value of given OID 
3. GetCommString function in the SNMP_PA stub  will be called from snmplib to get the community string. 
4. Get CMTS MAC using TR-181 parameter and compare with snmpget output
4.Responses from the snmplib and TR-181 parameter will be logged in Script log.
6. Validation of  the result is done within the python script and send the result status to Test Manager.
7.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from snmplib.</automation_approch>
    <except_output>CheckPoint 1:
Response of snmp command should be logged in the script log

CheckPoint 2:
Stub and lib function result should be success and should see corresponding log in the script log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>snmp_pa, sysutil,tdkbtr181</test_stub_interface>
    <test_script>TS_SNMP_GetCMTSMAC</test_script>
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

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SNMP_GetCMTSMAC');
obj1.configureTestCase(ip,port,'TS_SNMP_GetCMTSMAC');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Get the Community String
    communityString = snmplib.getCommunityString(obj,"snmpget");
    #Get the IP Address
    ipaddress = snmplib.getIPAddress(obj);
    actResponse =snmplib.SnmpExecuteCmd("snmpget", communityString, "-v 2c", "1.3.6.1.2.1.10.127.1.2.1.1.1.2", ipaddress);
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.executeTestCase("SUCCESS");

    if "SNMPv2-SMI" in actResponse:
        mac = actResponse.split("STRING:")[1].strip()
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1:Execute snmpget for CMTS mac";
        print "EXPECTED RESULT 1: snmpget should return CMTS mac";
        print "ACTUAL RESULT 1: CMTS MAC Address retrieved from snmp is %s" %mac;
        #Set the test execution result
        print "[TEST EXECUTION RESULT] : SUCCESS";

	tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_CMTS_MAC")
        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
	if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            CMTS_MAC = details;
	    print "TEST STEP 2: Get CMTS MAC Address using TR-181 parameter";
	    print "EXPECTED RESULT 2: Should get CMTS MAC Address";
            print "ACTUAL RESULT 2: CMTS MAC Address retrieved from TR-181 parameter is %s" %CMTS_MAC;
            print "[TEST EXECUTION RESULT] : SUCCESS";
    	    if mac.replace(" ",":")==CMTS_MAC.upper():
	        tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Compare CMTS MAC Address retrieved from snmpget and TR-181 parameter";
                print "EXPECTED RESULT 3: CMTS MAC Address retrieved from snmpget and TR-181 parameter should be same";
                print "ACTUAL RESULT 3 : CMTS MAC Address retrieved from snmpget and TR-181 parameter are same";
                print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
		tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Compare CMTS MAC Address retrieved from snmpget and TR-181 parameter";
                print "EXPECTED RESULT 3: CMTS MAC Address retrieved from snmpget and TR-181 parameter should be same";
                print "ACTUAL RESULT 3 : CMTS MAC Address retrieved from snmpget and TR-181 parameter are not same";
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get CMTS MAC Address using TR-181 parameter";
            print "EXPECTED RESULT 2: Should get CMTS MAC Address";
	    print "ACTUAL RESULT 2: Couldn't get CMTS MAC from TR-181 parameter";
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        details = tdkTestObj.getResultDetails();
        print "TEST STEP 1:Execute snmpget for CMTS mac";
        print "EXPECTED RESULT 1: snmpget should return CMTS mac";
        print "ACTUAL RESULT 1: %s" %actResponse;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("sysutil");
    obj1.unloadModule("tdkbtr181");
else:
    print "FAILURE to load SNMP_PA module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
