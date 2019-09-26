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
<?xml version="1.0" encoding="UTF-8"?>
<xml>
  <id/>
  <version>1</version>
  <name>TS_TAD_SelfHeal_CheckDefaultStatus</name>
  <primitive_test_id/>
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check whether the Self Heal feature is enabled by default</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_TAD_69</test_case_id>
    <test_objective>Check whether the Self Heal feature is enabled by default</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Get</api_or_interface_used>
    <input_parameters>Device.SelfHeal.X_RDKCENTRAL-COM_Enable
Device.X_CISCO_COM_DeviceControl.FactoryReset
</input_parameters>
    <automation_approch>1. Load TAD modules
2. Initiate factory reset to obtain the default values of all parameters
3. Get the default status of selfheal feature
4. Check if the selfheal feature is enabled by default
5.Unload module</automation_approch>
    <except_output>The self heal feature should be enabled by default</except_output>
    <priority>High</priority>
    <test_stub_interface>TAD</test_stub_interface>
    <test_script>TS_TAD_SelfHeal_CheckDefaultStatus</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
pamobj = tdklib.TDKScriptingLibrary("pam","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_SelfHeal_CheckDefaultStatus');
pamobj.configureTestCase(ip,port,'TS_TAD_SelfHeal_CheckDefaultStatus');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus =obj.getLoadModuleResult();
pamloadmodulestatus =pamobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %pamloadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    pamobj.setLoadModuleStatus("SUCCESS");

    #save device's current state before it goes for reboot
    obj.saveCurrentState();

    #Initiate Factory reset before checking the default value
    tdkTestObj = pamobj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("Type","string");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Initiate factory reset ";
        print "EXPECTED RESULT 1: Should inititate factory reset";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	#Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot();

	#Check the default status of selfheal
	tdkTestObj = obj.createTestStep('TADstub_Get');
        tdkTestObj.addParameter("paramName","Device.SelfHeal.X_RDKCENTRAL-COM_Enable");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
	details = tdkTestObj.getResultDetails();
	if "true" == details:
	    tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP 2: Selfheal feature is enabled by default"
	    print "EXPECTED RESULT 2: Selfheal feature should be enabled by default"
	    print "ACTUAL RESULT 2: Selfheal feature status :%s" %details
	    print "[TEST EXECUTION RESULT] : SUCCESS";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Selfheal feature is enabled by default"
            print "EXPECTED RESULT 2: Selfheal feature should be enabled by default"
            print "ACTUAL RESULT 2: Selfheal feature status :%s" %details
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
	print "TEST STEP 1: Initiate factory reset ";
        print "EXPECTED RESULT 1: Should inititate factory reset";
        print "ACTUAL RESULT 1: %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tad");
    pamobj.unloadModule("pam");

else:
        print "Failed to load tad module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

