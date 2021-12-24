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
  <version>7</version>
  <name>TS_RBUS_CloseWithActiveSubscription</name>
  <primitive_test_id/>
  <primitive_test_name>RBUS_Close</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if invocation of rbus_close is success when there is an active subscription on an event.</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_RBUS_92</test_case_id>
    <test_objective>To check if invocation of rbus_close is success when there is an active subscription on an event.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbus_open()
rbus_close()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the modules
2. Open the rbus connection using rbus_open API
3. Using rbuscli register a new event
4. Subscribe to the new event registered
5. Close the rbus_connection using rbus_close API and check if it is success when there is an active subscription on an event</automation_approch>
    <expected_output>Invocation of rbus_close should be success when there is an active subscription on an event.</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_CloseWithActiveSubscription</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("rbus","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_RBUS_CloseWithActiveSubscription');
sysobj.configureTestCase(ip,port,'TS_RBUS_CloseWithActiveSubscription');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Open RBUS connection
    step = 1;
    string_to_print = "without active subscription";
    tdkTestObj = obj.createTestStep('RBUS_Open');
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Open the RBUS connection" %step;
    print "EXPECTED RESULT %d: rbus_open Should be success" %step;
    print "RBUS Open Details : ",details;

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: rbus_open was success" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS" ;
        print "RBUS status is %s" %details;

        #Register a event "sample_prop" using rbuscli
        step = step + 1;
        event_name = "sample_prop";
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        cmd = "rbuscli reg prop " + event_name;
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\n Command : %s" %cmd;
        print "TEST STEP %d: Register an event %s using rbuscli" %(step, event_name);
        print "EXPECTED RESULT %d: Should register the event successfully" %step;

        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Registered successfully" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Subscribe to the registered event
            step = step + 1;
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            cmd = "rbuscli sub " + event_name;
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\n Command : %s" %cmd;
            print "TEST STEP %d: Subscribe to the event %s using rbuscli" %(step, event_name);
            print "EXPECTED RESULT %d: Should subscribe to the event successfully" %step;

            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Subscribed successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                string_to_print = "with active subscription";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Not subscribed successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Not registered successfully" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        #Check if RBUS close connection is success
        step = step + 1;
        tdkTestObj = obj.createTestStep('RBUS_Close');
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP %d: Close the RBUS connection %s" %(step, string_to_print);
        print "EXPECTED RESULT %d: rbus_close should be success" %step;
        print "RBUS close Details : ",details;

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: rbus_close was success" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS" ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: rbus_close was Failed" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE" ;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: rbus_open was Failed" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE" ;

    obj.unloadModule("rbus");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
