##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <name>TS_SANITY_Checkath12and13InterfacesUp</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if ath12 and ath13  interfaces are populating on Factory Reset</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>  
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_46</test_case_id>
    <test_objective>To check if ath12 and ath13  interfaces are populating on Factory Reset.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>ifconfig ath12
ifconfig ath13</input_parameters>
    <automation_approch>1.Load the module
2.Factory Reset the device
3.Once the DUT is up query ath12 and ath13 with ifconfig
4.interface should be fetched successfully without any errors
5.unload the module</automation_approch>
    <expected_output>on FR ath12 and ath13 interfaces are expected to be present</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_Checkath12and13InterfacesUp</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
from tdkbVariables import *;


#Test component to be tested
pamobj = tdklib.TDKScriptingLibrary("pam","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_SANITY_Checkath12and13InterfacesUp');
sysObj.configureTestCase(ip,port,'TS_SANITY_Checkath12and13InterfacesUp');

#Get the result of connection with test component and DUT
pamloadmodulestatus=pamobj.getLoadModuleResult();
sysloadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in sysloadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS")
    sysObj.setLoadModuleStatus("SUCCESS")
    #save device's current state before it goes for reboot
    sysObj.saveCurrentState();

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
        sysObj.restorePreviousStateAfterReboot();

        interfacename = ["ath12","ath13"];
        for interafces in interfacename:
            tdkTestObj = sysObj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", "ifconfig %s"%interafces);
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip();
            if expectedresult in actualresult and "error fetching interface information" not in details:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP : Check if %s is up"%interafces;
                print "EXPECTED RESULT : %s should be up"%interafces;
                print "ACTUAL RESULT : %s inteface is present"%interafces;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : Check if %s is up"%interafces;
                print "EXPECTED RESULT : %s should be up"%interafces;
                print "ACTUAL RESULT : %s inteface is not present"%interafces;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] :FAILURE";
                break;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "EXPECTED RESULT 1: Should inititate factory reset";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    pamobj.unloadModule("pam");
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
