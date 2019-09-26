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
  <name>TS_XDNS_EnableXDNS_CheckXdnsProcess</name>
  <primitive_test_id/>
  <primitive_test_name>XDNS_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if on enabling XDNS, CcspXdnsSsp is crashing or not</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_XDNS_13</test_case_id>
    <test_objective>Check if on enabling XDNS, CcspXdnsSsp is crashing or not</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS</input_parameters>
    <automation_approch>1. Load tdkbtr181 and  pam modules
2. Get the current enable status of XDNS
3. Enable XDNS and check if it is success
4. Check if after enabling Xdns, CcspXdnsSsp process went down or not
5. Revert the XDNS enable status
6. Unload tdkbtr181 and  pam modules</automation_approch>
    <except_output>Enabling Xdns should not cause CcspXdnsSsp to crash</except_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181
pam</test_stub_interface>
    <test_script>TS_XDNS_EnableXDNS_CheckXdnsProcess</test_script>
    <skipped>No</skipped>
    <release_version>M66</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_XDNS_EnableXDNS_CheckXdnsProcess');
sysObj.configureTestCase(ip,port,'TS_XDNS_SelfHeal_DnsmasqProcess');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
sysloadmodulestatus =sysObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    sysObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    xdnsEnable = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the enable status of XDNS";
        print "EXPECTED RESULT 1: Should get the enable status of XDNS";
        print "ACTUAL RESULT 1: XDNS Enable status is %s" %xdnsEnable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_XDNS.DefaultDeviceDnsIPv4");
	#Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult1 = tdkTestObj.getResult();
        defIPV4 = tdkTestObj.getResultDetails();
	defIPV4 = defIPV4.replace("\\n", "");

        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_XDNS.DefaultDeviceDnsIPv6");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult2 = tdkTestObj.getResult();
        defIPV6 = tdkTestObj.getResultDetails();
	defIPV6 = defIPV6.replace("\\n", "");

        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_XDNS.DefaultDeviceTag");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult3 = tdkTestObj.getResult();
        defTag = tdkTestObj.getResultDetails();
	defTag = defTag.replace("\\n", "");

	if expectedresult in (actualresult1 and actualresult2 and actualresult3):
	    #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the default params of XDNS";
            print "EXPECTED RESULT 2: Should get the default params of XDNS";
            print "ACTUAL RESULT 2: Default params values %s %s %s" %(defIPV4,defIPV6,defTag);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    if '' in (defIPV4,defIPV6,defTag):
		tdkTestObj = obj.createTestStep('TDKB_TR181Stub_SetMultiple');
		tdkTestObj.addParameter("paramList","Device.X_RDKCENTRAL-COM_XDNS.DefaultDeviceDnsIPv4|%s|string|Device.X_RDKCENTRAL-COM_XDNS.DefaultDeviceDnsIPv6|%s|string|Device.X_RDKCENTRAL-COM_XDNS.DefaultDeviceTag|empty|string"%(XDNS_DEFAULT_IPV4,XDNS_DEFAULT_IPV6));	
		tdkTestObj.executeTestCase(expectedresult);
                setresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

	    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS");
            tdkTestObj.addParameter("ParamValue","true");
            tdkTestObj.addParameter("Type","bool");
            expectedresult="SUCCESS";

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

	    if expectedresult  and actualresult:
	        #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Set the enable status of XDNS as true";
                print "EXPECTED RESULT 3: Should enable XDNS";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                # Check whether the process CcspXdnsSsp went down on enabling XDns
                query="sh %s/tdk_platform_utility.sh checkProcess CcspXdnsSsp" %TDK_PATH
                print "query:%s" %query
                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", query)
                expectedresult="SUCCESS";

                #Execute the test case in DUT
                tdkTestObj.executeTestCase("SUCCESS");
                actualresult = tdkTestObj.getResult();
                pid = tdkTestObj.getResultDetails().strip()
                print "CcspXdnsSsp PID: %s" %pid

                if expectedresult in actualresult and pid:
                    print "TEST STEP 4:Check if CcspXdnsSsp process went down on enabling Xdns"
                    print "EXPECTED RESULT 4: CcspXdnsSsp should be running";
                    print "ACTUAL RESULT 4: CcspXdnsSsp process is running"
                    tdkTestObj.setResultStatus("SUCCESS");
                else:
                    print "TEST STEP 4:Check if CcspXdnsSsp process went down on enabling Xdns"
                    print "EXPECTED RESULT 4: CcspXdnsSsp should be running";
                    print "ACTUAL RESULT 4: CcspXdnsSsp process is not running"
                    tdkTestObj.setResultStatus("FAILURE");
	    else:
	        #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Set the enable status of XDNS as true";
                print "EXPECTED RESULT 3: Should enable XDNS";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

	    #Revert the value of XDNS Enable
	    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS");
            tdkTestObj.addParameter("ParamValue",xdnsEnable);
            tdkTestObj.addParameter("Type","bool");
            expectedresult="SUCCESS";

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP : Revert the enable status of XDNS ";
                print "EXPECTED RESULT : Should revert XDNS status to previous value";
                print "ACTUAL RESULT : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : Revert the enable status of XDNS";
                print "EXPECTED RESULT : Should revert XDNS status to previous value";
                print "ACTUAL RESULT : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the default params of XDNS";
            print "EXPECTED RESULT 2: Should get the default params of XDNS";
            print "ACTUAL RESULT 2: Default params values %s %s %s" %(defIPV4,defIPV6,defTag);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the enable status of XDNS";
        print "EXPECTED RESULT 1: Should get the enable status of XDNS";
        print "ACTUAL RESULT 1: XDNS Enable status is %s" %xdnsEnable
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
    obj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
