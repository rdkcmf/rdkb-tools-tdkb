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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>2</version>
  <name>TS_CMHAL_GetCPEList</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_GetCPEList</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the list of CPEs connected to the CM using cm_hal_GetCPEList()</synopsis>
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
    <test_case_id>TC_CMHAL_54</test_case_id>
    <test_objective>To get the list of CPEs connected to the CM using cm_hal_GetCPEList()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>cm_hal_GetCPEList()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  cmhal module
2. From script invoke CMHAL_GetCPEList()
3. Get the IP address and mac address of CPEs
4. Validate the value obtained
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <except_output>The api should return the ip address and mac address of CPEs connected</except_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_GetCPEList</test_script>
    <skipped>No</skipped>
    <release_version>M62</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_GetCPEList');
obj1.configureTestCase(ip,port,'TS_CMHAL_GetCPEList');
ip = "";
mac ="";
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("CMHAL_GetCPEList");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    instNum= details.split("InstNum :")[-1];
    details = details.split("InstNum :")[0];
    print details;
    if expectedresult in actualresult and int(instNum) > 0:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
	cpeList = details.split("::");
	print "cpeList",cpeList;
	for i in cpeList:
	    if i != cpeList[-1]:
	        val = i.split(",");
	        ip += val[0];
		ip += ","
	        mac += val[1];
		mac += ","
	    else:
		break;
        print "TEST STEP 1: Get the cpe list";
        print "EXPECTED RESULT 1: Should get cpe list successfully";
        print "ACTUAL RESULT 1: Instance number is", instNum ,",IP address ", ip, "MAC address ", mac;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	#validate the cpe list
	tdkTestObj = obj1.createTestStep('ExecuteCmd');
	cmd= "arp -a | grep brlan0 |tr '\n' ','";
	tdkTestObj.addParameter("command", cmd);

        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip();
	if expectedresult in actualresult:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the cpe list from DUT";
            print "EXPECTED RESULT 2: Should get cpe list from DUT successfully";
            print "ACTUAL RESULT 2: %s" %details;
            print "[TEST EXECUTION RESULT] : SUCCESS";
	    ipList = ip.split(",");
	    macList = mac.split(",");
	    for i in ipList:
		if i != ipList[-1]:
		    if i in details:
		       print "Validated the ip address: ", i;
		    else:
		       print "Validation failed for ",i
		       tdkTestObj.setResultStatus("FAILURE");
		       break;
	    for i in macList:
		if i != macList[-1]:
		    if i in details:
		       print "Validated the mac address: ", i;
		    else:
		       print "Validation failed for ",i
		       tdkTestObj.setResultStatus("FAILURE");
		       break;
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the cpe list from DUT";
            print "EXPECTED RESULT 2: Should get cpe list from DUT successfully";
            print "ACTUAL RESULT 2: %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the cpe list";
        print "EXPECTED RESULT 1: Should get cpe list successfully";
        print "ACTUAL RESULT 1: %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("cmhal");
    obj1.unloadModule("sysutil");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
