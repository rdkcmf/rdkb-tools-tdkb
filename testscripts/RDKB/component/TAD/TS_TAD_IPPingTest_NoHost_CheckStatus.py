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
  <name>TS_TAD_IPPingTest_NoHost_CheckStatus</name>
  <primitive_test_id/>
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the diagnostic state is set as Error_CannotResolveHostName for the ping test done with an empty hostname</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_TAD_55</test_case_id>
    <test_objective>Check if the diagnostic state is set as Error_CannotResolveHostName for the ping test done with an empty hostname</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI.</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Get, TADstub_Set</api_or_interface_used>
    <input_parameters>Device.IP.Diagnostics.IPPing.Host
Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run
Device.IP.Diagnostics.TraceRoute.DiagnosticsState</input_parameters>
    <automation_approch>1. Load TAD module
2. Set Device.IP.Diagnostics.TraceRoute.Host as an empty string
3. Set Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run as true to start the ping test
4. After ping test, check if the value of Device.IP.Diagnostics.IPPing.DiagnosticsState is Error_CannotResolveHostName 
5. Unload the TAD module</automation_approch>
    <except_output>On ping test with host name as empty, value of Device.IP.Diagnostics.IPPing.DiagnosticsState should be Error_CannotResolveHostName </except_output>
    <priority>High</priority>
    <test_stub_interface>tad</test_stub_interface>
    <test_script>TS_TAD_IPPingTest_NoHost_CheckStatus</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib;
import time;
import tdkutility;
from tdkutility import * 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_IPPingTest_NoHost_CheckStatus');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('TADstub_Set');
    tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.IPPing.Host");
    tdkTestObj.addParameter("ParamValue","");
    tdkTestObj.addParameter("Type","string");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 2: Set the host of IPPing as an empty URI";
        print "EXPECTED RESULT 2: Should set an empty host for IPPing";
        print "ACTUAL RESULT 2: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #start the ping test after setting host value
	tdkTestObj = obj.createTestStep('TADstub_Set');
        tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.X_RDKCENTRAL-COM_PingTest.Run")
        tdkTestObj.addParameter("ParamValue","true");
        tdkTestObj.addParameter("Type","boolean");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Set PingTest.Run of IPPing as true";
            print "EXPECTED RESULT 3: Should set PingTest.Run of IPPing as true";
            print "ACTUAL RESULT 3: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            time.sleep(40);

            print "TEST STEP 4:  Check the DiagnosticsState value after ping"
            print "EXPECTED RESULT 4: DiagnosticsState value should be Error_CannotResolveHostName";
  	    tdkTestObj = obj.createTestStep('TADstub_Get');
	    tdkTestObj.addParameter("paramName","Device.IP.Diagnostics.IPPing.DiagnosticsState");
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    diagState =  tdkTestObj.getResultDetails();
	    if expectedresult in actualresult and diagState == "Error_CannotResolveHostName":
	        tdkTestObj.setResultStatus("SUCCESS");
	        print "ACTUAL RESULT 4: DiagnosticsState value is %s" %diagState
	        print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 4: %s" %diagState
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 3: Set PingTest.Run of IPPing as true";
            print "EXPECTED RESULT 3: Should set PingTest.Run of IPPing as true";
            print "ACTUAL RESULT 3: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 2: Set the host of IPPing as an empty string";
        print "EXPECTED RESULT 2: Should set the host of IPPing";
        print "ACTUAL RESULT 2: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tad");

else:
    print "Failed to load tad module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
