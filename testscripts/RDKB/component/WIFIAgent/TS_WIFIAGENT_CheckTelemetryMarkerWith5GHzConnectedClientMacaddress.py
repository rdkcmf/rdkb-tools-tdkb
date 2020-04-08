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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_CheckTelemetryMarkerWith5GHzConnectedClientMacaddress</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Validate the macaddresses obtained from telemetry marker and host table are same</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_94</test_case_id>
    <test_objective>compare the MAC address obtained from telemetry marker matches with the host table mac address</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Connect a WiFi cilent to 5Ghz private SSID of DUT</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.Hosts.HostNumberOfEntries, Device.Hosts.Host.{i}.Active, Device.Hosts.Host.{i}.PhysAddress</input_parameters>
    <automation_approch>1.Load the module.
2.Grep "WIFI_MAC_2" in wifihealth.txt file and get the MAC address value
3.Compare the Mac address with Host table connected client MAC address
4.MAC Address obtained from Telemetry Marker should match with Host table MAC Address
5.Unload module</automation_approch>
    <expected_output>MAC Address obtained from Telemetry Marker should match with Host table MAC Address</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckTelemetryMarkerWith5GHzConnectedClientMacaddress</test_script>
    <skipped>No</skipped>
    <release_version>M75</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("lmlite","RDKB");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerWith5GHzConnectedClientMacaddress');
sysObj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerWith5GHzConnectedClientMacaddress');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
sysutilloadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Check for wifihealth log file presence";
        print "EXPECTED RESULT 1:wifihealth log file should be present";
        print "ACTUAL RESULT 1:wifihealth log file is present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        markerfound = 0;
        for i in range(1,15):
            if markerfound == 1:
                break;
            else:
	        #Query for the Telemetry Marker
	        query="cat /rdklogs/logs/wifihealth.txt | grep -i \"WIFI_MAC_2:\""
	        print "query:%s" %query
		tdkTestObj = sysObj.createTestStep('ExecuteCmd');
		tdkTestObj.addParameter("command", query)
		expectedresult="SUCCESS";
		tdkTestObj.executeTestCase(expectedresult);
		actualresult = tdkTestObj.getResult();
		details = tdkTestObj.getResultDetails().strip().replace("\\n","");
        	print "Marker Detail Found fromLog file is: %s "%details;

 	        if (len(details) == 0) or details.endswith(":") or "WIFI_MAC_2" not in details:
		    markerfound = 0;
                    sleep(60);
		else:
            	    telemetryMacaddress = details.split("WIFI_MAC_2:")[1].split(',')[0];
	            markerfound = 1;

	if expectedresult in actualresult and markerfound == 1:
            tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP 2: WIFI_MAC_2 Marker should be present";
	    print "EXPECTED RESULT 2: WIFI_MAC_2 Marker should be present";
	    print "ACTUAL RESULT 2:WIFI_MAC_2 Marker is %s" %telemetryMacaddress
	    #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj = obj.createTestStep('LMLiteStub_Get');
            tdkTestObj.addParameter("paramName","Device.Hosts.HostNumberOfEntries");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            NoOfHosts = tdkTestObj.getResultDetails();
            macaddressFound = 0;

            if expectedresult in actualresult and int(NoOfHosts)>0:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the number of hosts";
                print "EXPECTED RESULT 3: Should get the number of hosts";
                print "ACTUAL RESULT31: Number of hosts :%s" %NoOfHosts;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                #Find the active hosts amoung the listed Hosts. List will contains the ids of active hosts
                List=[];

                for i in range(1,int(NoOfHosts)+1):
                    if int(macaddressFound) == 1:
			break;
	            tdkTestObj.addParameter("paramName","Device.Hosts.Host.%d.Active" %i);
	            #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
	            Status = tdkTestObj.getResultDetails();

	            if "true" in Status:
	                List.extend(str(i));
		        if expectedresult in actualresult:
		            #Set the result status of execution
		            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 4: Get the active LAN clients";
                            print "EXPECTED RESULT 4: Should get the active LAN clients";
    	        	    print "ACTUAL RESULT 4: Active LAN clients are :",List;
		            #Get the result of execution
		            print "[TEST EXECUTION RESULT] : SUCCESS";

                            for i in range(0,len(List)):
				if int(macaddressFound) == 1:
				    break;
			        n = int(List[i]);
			        tdkTestObj.addParameter("paramName","Device.Hosts.Host.%d.PhysAddress" %n);
			        #Execute the test case in DUT
			        tdkTestObj.executeTestCase(expectedresult);
			        actualresult = tdkTestObj.getResult();
			        hostMacAddress = tdkTestObj.getResultDetails();
			        print "MAC address Found in host table: %s" %hostMacAddress;

			        if expectedresult in actualresult:
    			            #Set the result status of execution
			            tdkTestObj.setResultStatus("SUCCESS");
			            print "TEST STEP 5: Get the MAC address of the LAN Client	";
			            print "EXPECTED RESULT 5: Get the MAC address of the device";
			            print "ACTUAL RESULT 5: Get MAC address : Success";
			            #Get the result of execution
			            print "[TEST EXECUTION RESULT] : SUCCESS";

                                    if hostMacAddress.upper() == telemetryMacaddress.upper():
				        print "MAC Address Matched successfully"
				    	macaddressFound = 1;
				    else:
				        print "MAC Address Not Matched"
			        else:
			            #Set the result status of execution
			            tdkTestObj.setResultStatus("FAILURE");
			            print "TEST STEP 5: Get the MAC address of the LAN Client	";
			            print "EXPECTED RESULT 5: Get the MAC address of the device";
			            print "ACTUAL RESULT 5: Get MAC address : Failed"
			            #Get the result of execution
			            print "[TEST EXECUTION RESULT] : FAILURE";
		        else:
		            #Set the result status of execution
		            tdkTestObj.setResultStatus("FAILURE");
		            print "TEST STEP 4: Get the active LAN clients";
	        	    print "EXPECTED RESULT 4: Should get the active cleints";
		            print "ACTUAL RESULT 4: FAiled to get the active LAN clients";
		            #Get the result of execution
		            print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the number of hosts";
                print "EXPECTED RESULT 3: Should get the number of hosts";
                print "ACTUAL RESULT31: Number of hosts :%s" %NoOfHosts;
                #Get the result of execution
	        print "[TEST EXECUTION RESULT] : FAILURE";

            if macaddressFound == 1:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 6: Compare the Host table MAC address with Telemetry MAC address"
                print "EXPECTED RESULT 6: Both MAC Addresses should match";
                print "ACTUAL RESULT 6: Host table and Telemetry Marker MAC addresses are matching";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 6: Compare the MAC address with Telemetry MAC address";
                print "EXPECTED RESULT 6: Both MAC Addresses should match";
                print "ACTUAL RESULT 6: MAC Address Found in Telemetry Marker is not matching with Host Table MAC Address";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
	    print "TEST STEP 2: WIFI_MAC_2 Marker should be present";
	    print "EXPECTED RESULT 2: WIFI_MAC_2 Marker should be present";
	    print "ACTUAL RESULT 2:WIFI_MAC_2 Marker is  Not Present";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Check for wifihealth log file presence";
        print "EXPECTED RESULT 1:wifihealth log file should be present";
        print "ACTUAL RESULT 1:wifihealth log file is NOT present";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("lmlite")
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load lmlite/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
