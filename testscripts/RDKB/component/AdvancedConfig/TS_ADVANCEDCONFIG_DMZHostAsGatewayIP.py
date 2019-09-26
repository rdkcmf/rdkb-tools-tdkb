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
  <version>5</version>
  <name>TS_ADVANCEDCONFIG_DMZHostAsGatewayIP</name>
  <primitive_test_id/>
  <primitive_test_name>AdvancedConfig_Set</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis/>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>RPI</box_type>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_ADVANCEDCONFIG_2</test_case_id>
    <test_objective>To validate "DMZ host as Gateway IP address" functionality</test_objective>
    <test_type>Possitive</test_type>
    <test_setup>Emulator,
XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name
AdvancedConfig_Set

Input
1.PathName ("paramName")
( eg: "Device.NAT.X_CISCO_COM_DMZ.Enable" )
Type: bool, Value: True

2. PathName ("paramName")
( eg. "Device.NAT.X_CISCO_COM_DMZ.InternalIP")
Type: String, Value: 10.0.0.1</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested  
(AdvancedConfig_Set - func name - "If not exists already"
 advancedconfig - module name
 Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automically by Test Manager with provided arguments in configure page (TS_ADVANCEDCONFIG_DMZHostAsGatewayIP.py)
3.Execute the generated Script(TS_ADVANCEDCONFIG_DMZHostAsGatewayIP.py) using execution page of  Test Manager GUI
4.advancedconfigstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named AdvancedConfig_Set through registered TDK advancedconfigstub function along with necessary Entry Values as arguments
5.AdvancedConfig_Set function will call ssp_setParameterValue,that inturn will call CCSP Base Interface Function named CcspBaseIf_setParameterValues.
6.Responses(printf) from TDK Component,Ccsp Library function and advancedcongifstub would be logged in Agent Console log based on the debug info redirected to agent console   
7.advancedconfigstub will validate the available result (from ssp_setParameterValue as zero) with expected result (zero) and the result is updated in agent console log and json output variable
8.TestManager will publish the result in GUI as SUCCESS/FAILURE based on the response from AdvancedConfig_Set function</automation_approch>
    <except_output>Checkpoint 1:
Check the Failure in Setting DMZ host as Gateway IP address.
CheckPoint 2:
Success log should be available in Agent Console Log
CheckPoint 3:
TDK agent Test Function will log the test case result as SUCCESS based on API response 
CheckPoint 4:
TestManager GUI will publish the result as SUCCESS in Execution page</except_output>
    <priority>High</priority>
    <test_stub_interface>none</test_stub_interface>
    <test_script>TS_ADVANCEDCONFIG_DMZHostAsGatewayIP</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("advancedconfig","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ADVANCEDCONFIG_DMZHostAsGatewayIP');

#Get the result of connection with test component and STB
loadModuleresult =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadModuleresult;

if "SUCCESS" in loadModuleresult.upper():
        obj.setLoadModuleStatus("SUCCESS");
        tdkTestObj = obj.createTestStep("AdvancedConfig_Set");

        #Input Parameters
        tdkTestObj.addParameter("paramName","Device.NAT.X_CISCO_COM_DMZ.Enable");
        tdkTestObj.addParameter("paramValue","true");
        tdkTestObj.addParameter("paramType","boolean");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();

        if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                details = tdkTestObj.getResultDetails();
		print "[TEST STEP 1]: Enabling DMZ";
                print "[EXPECTED RESULT 1]: Should enable DMZ";
                print "[ACTUAL RESULT 1]: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "DMZ is Enabled\n"
                tdkTestObj = obj.createTestStep("AdvancedConfig_Set");
                tdkTestObj.addParameter("paramName","Device.NAT.X_CISCO_COM_DMZ.InternalIP");
                tdkTestObj.addParameter("paramValue","10.0.0.1");
                tdkTestObj.addParameter("paramType","string");
                expectedresult = "FAILURE";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        details = tdkTestObj.getResultDetails();
                        print "[TEST STEP 2]: Setting DMZ internalIP";
                        print "[EXPECTED RESULT 2]: Should not set the DMZ internal IP";
                        print "[ACTUAL RESULT 2]: %s" %details;
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                        print "DMZ host ip cannot be set as the gateway ip 10.0.0.1\n"
                else:
                        tdkTestObj.setResultStatus("FAILURE");
                        details = tdkTestObj.getResultDetails();
                        print "[TEST STEP 2]: Setting DMZ internalIP";
                        print "[EXPECTED RESULT 2]: Should not set the DMZ internal IP";
                        print "[ACTUAL RESULT 2]: %s" %details;
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                        print "DMZ host should not be set as gateway ip, but it is set and hence a failure\n"


        else:
                tdkTestObj.setResultStatus("FAILURE");
                details = tdkTestObj.getResultDetails();
                print "[TEST STEP 1]: Enabling DMZ";
                print "[EXPECTED RESULT 1]: Should enable DMZ";
                print "[ACTUAL RESULT 1]: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Failure in setting the DMZ as true\n "

        obj.unloadModule("advancedconfig");
else:
        print "FAILURE to load Advancedconfig module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading FAILURE";
