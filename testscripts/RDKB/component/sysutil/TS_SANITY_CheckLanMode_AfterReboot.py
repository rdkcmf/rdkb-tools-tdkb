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
<?xml version="1.0" encoding="UTF-8"?>
<xml>
  <id/>
  <version>4</version>
  <name>TS_SANITY_CheckLanMode_AfterReboot</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set bridge mode and reboot the device and check whether bridge mode is persistent after reboot.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_10</test_case_id>
    <test_objective>Set bridge mode and reboot the device and check whether bridge mode is persistent after reboot.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Emulator,Broadband,RPI</test_setup>
    <pre_requisite>TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>"Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode"</input_parameters>
    <automation_approch>1. Get the current lanMode
2. Set the lanmode to bridge-static
3. Reboot the device
4. Get the current lanmode again
5. Revert the lanmode to original value</automation_approch>
    <except_output>The lanmode should persists</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckLanMode_AfterReboot</test_script>
    <skipped>No</skipped>
    <release_version>M59</release_version>
    <remarks/>
  </test_cases>
  <script_tags>
    <script_tag>BASIC</script_tag>
  </script_tags>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckLanMode_AfterReboot');
pamObj.configureTestCase(ip,port,'TS_SANITY_CheckLanMode_AfterReboot');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =pamObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and loadmodulestatus2.upper:
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    pamObj.setLoadModuleStatus("SUCCESS");

    #Get the current Lan mode
    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    lanMode = tdkTestObj.getResultDetails().strip();

    if expectedresult in actualresult and lanMode:
	tdkTestObj.setResultStatus("SUCCESS");
        #Set the result status of execution
        print "TEST STEP 2: Get the current lanMode"
        print "EXPECTED RESULT 2: Should get the current lanMode"
        print "ACTUAL RESULT 2: Current lanMode is %s" %lanMode;
	print "[TEST EXECUTION RESULT] : SUCCESS";

	#Set the lanMode to bridge-static
	tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
	tdkTestObj.addParameter("ParamValue","bridge-static");
        tdkTestObj.addParameter("Type","string");
        expectedresult="SUCCESS";

        #Execute the test case in STB
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

	if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Set the lanMode to bridge-static";
            print "EXPECTED RESULT 1: Should set the lanMode to bridge-static";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : SUCCESS" ;

	    #rebooting the device
            obj.initiateReboot();
            sleep(300);

	    #Check if the lanMode persists
	    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    	    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    	    expectedresult="SUCCESS";

    	    #Execute the test case in STB
    	    tdkTestObj.executeTestCase(expectedresult);
    	    actualresult = tdkTestObj.getResult();
    	    lanMode1 = tdkTestObj.getResultDetails().strip();

    	    if expectedresult in actualresult and lanMode1 == "bridge-static":
    	        tdkTestObj.setResultStatus("SUCCESS");
    	        #Set the result status of execution
    	        print "TEST STEP 2: Get the current lanMode"
    	        print "EXPECTED RESULT 2: Should get the current lanMode as bridge-static"
    	        print "ACTUAL RESULT 2: Current lanMode is %s" %lanMode1;
    	        print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
		tdkTestObj.setResultStatus("FAILURE");
                #Set the result status of execution
                print "TEST STEP 2: Get the current lanMode"
                print "EXPECTED RESULT 2: Should get the current lanMode as bridge-static"
                print "ACTUAL RESULT 2: Current lanMode is %s" %lanMode1;
                print "[TEST EXECUTION RESULT] : FAILURE";
	    #Revert the value of lanMode
	    tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
            tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
            tdkTestObj.addParameter("ParamValue",lanMode);
            tdkTestObj.addParameter("Type","string");
            expectedresult="SUCCESS";

            #Execute the test case in STB
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 1:Revert the value of lanMode";
                print "EXPECTED RESULT 1: Should revert the lanMode";
                print "ACTUAL RESULT 1: %s" %details;
                print "[TEST EXECUTION RESULT] : SUCCESS" ;
	    else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 1:Revert the value of lanMode";
                print "EXPECTED RESULT 1: Should revert the lanMode";
                print "ACTUAL RESULT 1: %s" %details;
                print "[TEST EXECUTION RESULT] : FAILURE" ;
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Set the lanMode to bridge-static";
            print "EXPECTED RESULT 1: Should set the lanMode to bridge-static";
            print "ACTUAL RESULT 1: %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE" ;
    else:
	tdkTestObj.setResultStatus("FAILURE");
        #Set the result status of execution
        print "TEST STEP 2: Get the current lanMode"
        print "EXPECTED RESULT 2: Should get the current lanMode"
        print "ACTUAL RESULT 2: Current lanMode is %s" %lanMode;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("sysutil");
    pamObj.unloadModule("pam");

else:
        print "Failed to load sysutil module";
        sysObj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
