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
  <name>TS_ETHWAN_Check_DeviceIPAddress</name>
  <primitive_test_id/>
  <primitive_test_name>EthWAN_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Enable ETHWAN mode and check if the erouter0 interface has both ipv4 vand ipv6 addresses.</synopsis>
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
    <test_case_id>TC_ETHWAN_01</test_case_id>
    <test_objective>Enable ETHWAN mode and check if the erouter0 interface has both ipv4 vand ipv6 addresses.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. The broadband device should be in ETHWAN setup
2. The EthWAN mode should be enabled
3. TDK Agent must be up and running

</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled
</input_parameters>
    <automation_approch>1. Load module
2. Get the ethwan mode and check if it true or not
3. If ethwan is enabled, get the ipv6 and ipv4 addresses of the devices.
4. Unload module</automation_approch>
    <except_output>The device should get ipv4 and ipv6 addresses in ethwan mode</except_output>
    <priority>High</priority>
    <test_stub_interface>ETHWAN</test_stub_interface>
    <test_script>TS_ETHWAN_Check_DeviceIPAddress</test_script>
    <skipped>No</skipped>
    <release_version>M68</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ETHWAN_Check_DeviceIPAddress');
obj1.configureTestCase(ip,port,'TS_ETHWAN_Check_DeviceIPAddress');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.Ethernet.X_RDKCENTRAL-COM_WAN.Enabled");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    ethwanEnable = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the enable status of Ethwan";
        print "EXPECTED RESULT 1: Should get the enable status of Ethwan";
        print "ACTUAL RESULT 1: Ethwan Enable status is %s" %ethwanEnable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	if "true" == ethwanEnable:
	    tdkTestObj.setResultStatus("SUCCESS");
	    print "The device is in ethwan mode."

	    tdkTestObj = obj1.createTestStep('ExecuteCmd');
	    tdkTestObj.addParameter("command", "ifconfig -a erouter0 | grep \"inet6 addr\" | tr -s \" \" |  grep -v Link | cut -d \" \" -f4 | cut -d \"/\" -f1");
#ifconfig erouter0 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1
	    #Execute the test case in STB
     	    tdkTestObj.executeTestCase(expectedresult);
     	    actualresult = tdkTestObj.getResult();
     	    ipv6Address = tdkTestObj.getResultDetails().strip();
	    ipv6Address = ipv6Address.replace("\\n","");

     	    if expectedresult in actualresult and ipv6Address:
		tdkTestObj.setResultStatus("SUCCESS");
        	print "TEST STEP 2: Get the ipv6 address of device";
        	print "EXPECTED RESULT 2: Should get the ipv6 address of device";
        	print "ACTUAL RESULT 2: ipv6 address of device is %s" %ipv6Address;
        	#Get the result of execution
        	print "[TEST EXECUTION RESULT] : SUCCESS";

		tdkTestObj.addParameter("command", "ifconfig erouter0 | grep \"inet addr\" | cut -d ':' -f 2 | cut -d ' ' -f 1");

		#Execute the test case in STB
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                ipv4Address = tdkTestObj.getResultDetails().strip();
                ipv4Address = ipv4Address.replace("\\n","");

                if expectedresult in actualresult and ipv4Address:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Get the ipv4 address of device";
                    print "EXPECTED RESULT 3: Should get the ipv4 address of device";
                    print "ACTUAL RESULT 3: ipv4 address of device is %s" %ipv4Address;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
		else:
		    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Get the ipv4 address of device";
                    print "EXPECTED RESULT 3: Should get the ipv4 address of device";
                    print "ACTUAL RESULT 3: ipv4 address of device is %s" %ipv4Address;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
		tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Get the ipv6 address of device";
                print "EXPECTED RESULT 2: Should get the ipv6 address of device";
                print "ACTUAL RESULT 2: ipv6 address of device is %s" %ipv6Address;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
	    print "The device is not in ethwan mode. Please check the device setup"
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the enable status of Ethwan";
        print "EXPECTED RESULT 1: Should get the enable status of Ethwan";
        print "ACTUAL RESULT 1: Ethwan Enable status is %s" %ethwanEnable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
