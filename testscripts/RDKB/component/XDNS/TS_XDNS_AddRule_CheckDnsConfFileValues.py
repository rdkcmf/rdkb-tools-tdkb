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
  <name>TS_XDNS_AddRule_CheckDnsConfFileValues</name>
  <primitive_test_id/>
  <primitive_test_name>XDNS_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To verify if dnsmasq_servers.conf is created with the values of the table entries</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_XDNS_06</test_case_id>
    <test_objective>To verify if dnsmasq_servers.conf is created with the values of the table entries</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.X_RDKCENTRAL-COM_XDNS.DNSMappingTable.</input_parameters>
    <automation_approch>1. Load tdkbtr181 module
2. Add a new rule to the DNS table
3. Set values to all the fields in the new row
4. Check the values in dns config file 
5. Delete the added rule</automation_approch>
    <except_output>The dns config file should be updated with the values in the new rule</except_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TS_XDNS_AddRule_CheckDnsConfFileValues</test_script>
    <skipped>No</skipped>
    <release_version>M60</release_version>
    <remarks>none</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_XDNS_AddRule_CheckDnsConfFileValues');
sysobj.configureTestCase(ip,port,'TS_XDNS_AddRule_CheckDnsConfFileValues');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")

    expectedresult="SUCCESS";
    #add a new device to be blocked
    tdkTestObj = obj.createTestStep("TDKB_TR181Stub_AddObject");
    tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_XDNS.DNSMappingTable.");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Adding new rule for XDNS";
        print "EXPECTED RESULT 1: Should add new rule";
        print "ACTUAL RESULT 1: added new rule %s" %details;
        print "TEST EXECUTION RESULT : %s" %actualresult;
        temp = details.split(':');
        instance = temp[1];
        if (instance > 0):
            print "INSTANCE VALUE: %s" %instance

            #Set dummy values to each namespace in the table
            tdkTestObj = obj.createTestStep("TDKB_TR181Stub_SetMultiple");
            tdkTestObj.addParameter("paramList","Device.X_RDKCENTRAL-COM_XDNS.DNSMappingTable.%s.MacAddress|A:B:C:D|string|Device.X_RDKCENTRAL-COM_XDNS.DNSMappingTable.%s.DnsIPv4|x.y.z.a|string|Device.X_RDKCENTRAL-COM_XDNS.DNSMappingTable.%s.DnsIPv6|p:q:r:s|string|Device.X_RDKCENTRAL-COM_XDNS.DNSMappingTable.%s.Tag|Default|string" %(instance, instance, instance, instance));
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set all the values of the added row"
                print "EXPECTED RESULT 2: Should set all the values"
                print "ACTUAL RESULT 2: %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS";

		#Check if the conf file created with the added values
		tdkTestObj = sysobj.createTestStep('ExecuteCmd');
	        cmd= "sh %s/tdk_utility.sh parseConfigFile DNS_CONF_PATH" %TDK_PATH;
		print cmd;
    		tdkTestObj.addParameter("command", cmd);
    		tdkTestObj.executeTestCase(expectedresult);
    		actualresult = tdkTestObj.getResult();
    		conf_path = tdkTestObj.getResultDetails().strip();
    		conf_path = conf_path.replace("\\n", "");
    		if "Invalid Argument passed" not in conf_path and conf_path:
    		    tdkTestObj.setResultStatus("SUCCESS");
    		    print "TEST STEP 3: Get the location of dnsmasq conf file";
    		    print "EXPECTED RESULT 3: Should get the location of dnsmasq conf file";
    		    print "ACTUAL RESULT 3: %s" %conf_path;
    		    #Get the result of execution
    		    print "[TEST EXECUTION RESULT] : SUCCESS"

		    cmd = "cat %s/dnsmasq_servers.conf" %conf_path
		    print cmd;
                    tdkTestObj.addParameter("command", cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    dns_conf_value = tdkTestObj.getResultDetails().strip();
		    dns_conf_value = dns_conf_value.replace("\\n", "");
		    print dns_conf_value;

		    if "a:b:c:d x.y.z.a p:q:r:s Default" in dns_conf_value:
		        tdkTestObj.setResultStatus("SUCCESS");
		        print "TEST STEP 4: Get dnsmasq conf and validate"
                        print "EXPECTED RESULT 4: dnsmasq conf file should contain the valid values"
                        print "ACTUAL RESULT 4: %s" %details;
                        print "TEST EXECUTION RESULT :SUCCESS";
		    else:
		        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Get dnsmasq conf and validate"
                        print "EXPECTED RESULT 4: dnsmasq conf file should contain the valid values"
                        print "ACTUAL RESULT 4: %s" %details;
                        print "TEST EXECUTION RESULT :FAILURE";
		else:
		    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Get the location of dnsmasq conf file";
                    print "EXPECTED RESULT 3: Should get the location of dnsmasq conf file";
                    print "ACTUAL RESULT 3: %s" %conf_path;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
	    else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Set all the values of the added row"
                print "EXPECTED RESULT 2: Should set all the values"
                print "ACTUAL RESULT 2: %s" %details;
                print "TEST EXECUTION RESULT :FAILURE";
            #Delete the added row
            tdkTestObj = obj.createTestStep("TDKB_TR181Stub_DelObject");
            tdkTestObj.addParameter("paramName","Device.X_RDKCENTRAL-COM_XDNS.DNSMappingTable.%s." %instance);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "[TEST STEP ]: Deleting the added rule";
                print "[EXPECTED RESULT ]: Should delete the added rule";
                print "[ACTUAL RESULT]: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Added table is deleted successfully\n"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "[TEST STEP ]: Deleting the added rule";
                print "[EXPECTED RESULT ]: Should delete the added rule";
                print "[ACTUAL RESULT]: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Added table could not be deleted\n"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Adding new rule for XDNS";
        print "EXPECTED RESULT 1: Should add new rule";
        print "ACTUAL RESULT 1: added new rule %s" %details;
        print "TEST EXECUTION RESULT : FAILURE";
    obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
