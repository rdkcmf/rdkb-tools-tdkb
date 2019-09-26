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
  <name>TS_MOCA_CheckInterfaceStatus</name>
  <primitive_test_id/>
  <primitive_test_name>MocaStub_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Enable the Moca interface and check whether the status is "down" for standalone setup and "up" otherwise.</synopsis>
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
    <test_case_id>TC_MOCA_01</test_case_id>
    <test_objective>Enable the Moca interface and check whether the status is "down" for standalone setup and "up" otherwise.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>Mocastub_Set, Mocastub_Get</api_or_interface_used>
    <input_parameters>Device.MoCA.Interface.1.X_CISCO_COM_NumberOfConnectedClients
Device.MoCA.Interface.1.Enable
Device.MoCA.Interface.1.Status</input_parameters>
    <automation_approch>1. Load MOCA modules
2. From script invoke Mocastub_Get to get the number of clients connected
3. Enable the interface by invoking Mocastub_Set
4. Get the status and check whether it is "Down" for standalone setup and "Up" otherwise.
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from Moca stub.</automation_approch>
    <except_output>CheckPoint 1:
 The output  should be logged in the Agent console/Component log

CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_MOCA_CheckInterfaceStatus</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("moca","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MOCA_CheckInterfaceStatus');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('Mocastub_Get');
    tdkTestObj.addParameter("paramName","Device.MoCA.Interface.1.X_CISCO_COM_NumberOfConnectedClients");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    NoOfClients= tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
	#Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the number of connected clients";
        print "EXPECTED RESULT 1: Should get the number of connected clients";
        print "ACTUAL RESULT 1: Number of connected clients is :%s" %NoOfClients;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj = obj.createTestStep('Mocastub_Set');
	tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.Enable");
	tdkTestObj.addParameter("ParamValue","true");
	tdkTestObj.addParameter("Type","bool");
        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details= tdkTestObj.getResultDetails();
	if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Enable Moca Interface";
            print "EXPECTED RESULT 2: Should enable Moca Interface";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
	    tdkTestObj = obj.createTestStep('Mocastub_Get');
            tdkTestObj.addParameter("paramName","Device.MoCA.Interface.1.Status");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            Status = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
   	        if int(NoOfClients) == 0:
		    if "Down" in Status:
			#Set the result status of execution
                	tdkTestObj.setResultStatus("SUCCESS");
                	print "TEST STEP 3: Check if status is Down for standalone setup";
                	print "EXPECTED RESULT 3:Status should be Down for standalone setup";
                	print "ACTUAL RESULT 3: %s" %Status;
                	#Get the result of execution
                	print "[TEST EXECUTION RESULT] : SUCCESS";
		    else:
			#Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Check if status is Down for standalone setup";
                        print "EXPECTED RESULT 3:Status should be Down for standalone setup";
                        print "ACTUAL RESULT 3: %s" %Status;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
		else:
		    if "Up" in Status:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3: Check if status is Up if clients are connected";
                        print "EXPECTED RESULT 3:Status should be Up if clients are connected";
                        print "ACTUAL RESULT 3: %s" %Status;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Check if status is Up if clients are connected";
                        print "EXPECTED RESULT 3:Status should be Up if clients are connected";
                        print "ACTUAL RESULT 3: %s" %Status;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
		#Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the Moca Interface Status";
                print "EXPECTED RESULT 3:Should get the Moca Interface Status";
                print "ACTUAL RESULT 3: %s" %Status;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Enable Moca Interface";
            print "EXPECTED RESULT 2: Should enable Moca Interface";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the number of connected clients";
        print "EXPECTED RESULT 1: Should get the number of connected clients";
        print "ACTUAL RESULT 1: Number of connected clients is :%s" %NoOfClients;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("moca");
else:
        print "Failed to load moca module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
