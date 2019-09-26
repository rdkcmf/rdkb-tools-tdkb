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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SNMP_SetSSIDEnableWithRadioDisabled</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>GetCommString</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check for SSID enable when Radio is disabled</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_SNMP_PA_38</test_case_id>
    <test_objective>Check for SSID enable when Radio is disabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3, Emulator</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>GetCommString
WIFIAgent_Set</api_or_interface_used>
    <input_parameters>Device.WiFi.Radio.1.Enable
Device.WiFi.SSID.1.Enable

"snmpget", "-v 2c", "1.3.6.1.4.1.17270.50.2.2.2.1.1.2.10001"</input_parameters>
    <automation_approch>1.TM will load the snmp_pa library via Test agent
2.From python script, invoke SnmpExecuteCmd function in snmplib to get the value of given OID 
3. GetCommString function in the SNMP_PA stub  will be called from snmplib to get the community string. 
4.With WIFIAgent_Set disable wifi.Radio
5.With WIFIAgent_Set enable wifi.SSID
5.Check with snmpget that wifi.SSID is enabled or not
6. Validation of  the result is done within the python script and send the result status to Test Manager.
7.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from wifiagent stub.</automation_approch>
    <except_output>CheckPoint 1:
  Response of snmp command should be logged in the script log

CheckPoint 2:
Stub and lib function result should be success and should see corresponding log in the script log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>snmp_pa
wifiagent</test_stub_interface>
    <test_script>TS_SNMP_SetSSIDEnableWithRadioDisabled</test_script>
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
wifiObj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SNMP_SetSSIDEnableWithRadioDisabled');
wifiObj.configureTestCase(ip,port,'TS_SNMP_SetSSIDEnableWithRadioDisabled');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
wifiagentloadmodulestatus =wifiObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in wifiagentloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    wifiObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = wifiObj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.WiFi.Radio.1.Enable");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Radio status get SUCCESS";
        orgRadio = tdkTestObj.getResultDetails().split("VALUE:")[1].split(' ')[0];

        tdkTestObj.addParameter("paramName","Device.WiFi.SSID.1.Enable");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();        
    
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: SSID status get SUCCESS";
            orgSsid = tdkTestObj.getResultDetails().split("VALUE:")[1].split(' ')[0];

            #Disable Radio
            tdkTestObj = wifiObj.createTestStep('WIFIAgent_Set');
            tdkTestObj.addParameter("paramName","Device.WiFi.Radio.1.Enable");
            tdkTestObj.addParameter("paramValue","false");
            tdkTestObj.addParameter("paramType","boolean");
            expectedresult="SUCCESS";

            #Execute the test case in Gateway
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1:Disable WiFi.Radio";
                print "EXPECTED RESULT 1: Should Disable WiFi.Radio";
                print "ACTUAL RESULT 1: SUCCESS, Disabled";

		#Enable Wifi.SSID
                tdkTestObj.addParameter("paramName","Device.WiFi.SSID.1.Enable");
                tdkTestObj.addParameter("paramValue","true");
                tdkTestObj.addParameter("paramType","boolean");
                expectedresult="SUCCESS";

                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
		    sleep(30)
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 1:Enable Wifi.SSID";
                    print "EXPECTED RESULT 1: Should ENable wifi.SSID";
                    print "ACTUAL RESULT 1: SUCCESS, enabled";

	    	    #Get the Community String
                    communityString = snmplib.getCommunityString(obj,"snmpget");
                    #Get the IP Address
                    ipaddress = snmplib.getIPAddress(obj);
                    ########## Script to Execute the snmp command ###########
	            get_details =snmplib.SnmpExecuteCmd("snmpget", communityString, "-v 2c", "1.3.6.1.4.1.17270.50.2.2.2.1.1.2.10001", ipaddress);
	            tdkTestObj = obj.createTestStep('ExecuteCmd');
                    tdkTestObj.executeTestCase("SUCCESS");
                    print "TEST STEP 1:get Wifi.SSID with snmpget";
                    print "EXPECTED RESULT 1: Should get the value as enabled"
		    if "=" in get_details:
		        snmpStatus = get_details.rsplit(None, 1)[-1].strip('"');
	    		if snmpStatus != '1':
                    	    print "ACTUAL RESULT 1: SUCCESS, SSID is disabled with radio disable"
		            tdkTestObj.setResultStatus("SUCCESS");
			else:
			    print "ACTUAL RESULT 1: FAILURE, SSID is not disabled with radio disable"
			    tdkTestObj.setResultStatus("FAILURE");
		    else:
		        tdkTestObj.setResultStatus("FAILURE");
			print "ACTUAL RESULT 1: FAILURE, snmpget failed"

		    #restore previous state of wifi.SSID
                    tdkTestObj = wifiObj.createTestStep('WIFIAgent_Set');
                    tdkTestObj.addParameter("paramName","Device.WiFi.SSID.1.Enable");
                    tdkTestObj.addParameter("paramValue",orgSsid);
	            tdkTestObj.addParameter("paramType","boolean");
        	    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 1: SUCCESS, WiFi.SSID restored"
		    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 1: FAILURE, WiFi.SSID not restored"
		else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 1:Enable Wifi.SSID";
                    print "EXPECTED RESULT 1: Should ENable Wifi.SSID";
                    print "ACTUAL RESULT 1: FAILURE, not enabled";

                #Restore WiFi.Radio
                tdkTestObj = wifiObj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.WiFi.Radio.1.Enable");
                tdkTestObj.addParameter("paramValue",orgRadio);
                tdkTestObj.addParameter("paramType","boolean");
                expectedresult="SUCCESS";

                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 1: SUCCESS, WiFi.Radio restored"
		else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 1: FAILURE, WiFi.Radio not restored"
    	    else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1:Disable WiFi.Radio";
                print "EXPECTED RESULT 1: Should Disable WiFi.Radio";
                print "ACTUAL RESULT 1: FAILURE, not Disabled";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: SSID status get FAILED";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Radio status get FAILED";
    obj.unloadModule("sysutil");
    wifiObj.unloadModule("wifiagent");
else:
    print "FAILURE to load SNMP_PA module";
    obj.setLoadModuleStatus("FAILURE");
    wifiObj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";

