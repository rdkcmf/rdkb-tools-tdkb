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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_CMHAL_GetIPAddress</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_GetParamCharValue</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the IPaddress and check if it is valid or not</synopsis>
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
    <test_case_id>TC_CMHAL_26</test_case_id>
    <test_objective>To get the IPAddress and check if it is valid or not</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>cm_hal_GetIPv6DHCPInfo</api_or_interface_used>
    <input_parameters>paramName: Ipv6DhcpIPAddress</input_parameters>
    <automation_approch>1. Load  cmhal module
2. From script invoke CMHAL_GetParamCharValue() 
3. The buffer is already filled with an invalid value (invalid.ipaddress). So check whether the ipaddress is getting updated in the buffer successfully.
4. Validation of  the result is done within the stub and send the result status to Test Manager.
5.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <except_output>The ipaddress should be retrieved successfully</except_output>
    <priority>High</priority>
    <test_stub_interface>CosaCM</test_stub_interface>
    <test_script>TS_CMHAL_GetIPAddress</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_GetIPAddress');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("CMHAL_GetParamCharValue");
    tdkTestObj.addParameter("paramName","ProvIpType");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    IPType = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the provisioned wan0 iptype";
        print "EXPECTED RESULT 1: Should get the provisioned wan0 iptype successfully";
        print "ACTUAL RESULT 1: IPType is %s" %IPType;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
	IP =" ";
        if "IPv6" or "IPV6" in IPType:
    	    tdkTestObj = obj.createTestStep("CMHAL_GetParamCharValue");
    	    tdkTestObj.addParameter("paramName","Ipv6DhcpIPAddress");
    	    expectedresult="SUCCESS";
    	    tdkTestObj.executeTestCase(expectedresult);
    	    actualresult = tdkTestObj.getResult();
    	    IP = tdkTestObj.getResultDetails();

	elif "IPv4" or "IPV4" in IPType:
            tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
            tdkTestObj.addParameter("paramName","Ipv4DhcpIPAddress");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            IP = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and IP != " ":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the IPAddress";
            print "EXPECTED RESULT 2: Should get the IPAddress successfully";
            print "ACTUAL RESULT 2: The IP address is %s" %IP;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the IPAddress";
            print "EXPECTED RESULT 2: Should get the IPAddress successfully";
            print "ACTUAL RESULT 2: Failed to get the IP Address, Details :%s" %IP;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the provisioned wan0 iptype";
        print "EXPECTED RESULT 1: Should get the provisioned wan0 iptype successfully";
        print "ACTUAL RESULT 1: Failed to get the IPType, Details :%s" %IPType;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("cmhal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
