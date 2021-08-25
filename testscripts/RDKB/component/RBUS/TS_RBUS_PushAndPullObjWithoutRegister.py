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
  <version>2</version>
  <name>TS_RBUS_PushAndPullObjWithoutRegister</name>
  <primitive_test_id/>
  <primitive_test_name>RBUS_RegisterOperation</primitive_test_name>
  <primitive_test_version>4</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate the RBUS APIs rbus_pullObj and rbus_pushObj without registering the object</synopsis>
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
    <test_case_id>TC_RBUS_54</test_case_id>
    <test_objective>To validate the RBUS APIs rbus_pullObj and rbus_pushObj without registering the object</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbus_pullObj
rbus_pushObj</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load the rbus module
2. Open the rbus broker connection using rbus_openBrokerConnection API
3. The rbus_openBrokerConnection should be success
4. Try to pull the object value without registering the object in the bus using rbus_pullObj API
5. The return status should be failure
6. Try to push the new object value without registering the object in the bus using rbus_pushObj API
7. The return status should be failure
8. Close the rbus broker connection using rbus_closeBrokerConnection API
9. The rbus_closeBrokerConnection should be success
10.Unload the rbus module</automation_approch>
    <expected_output>rbus_pullObj and rbus_pushObj API call should be failed if object was not registered</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_PushAndPullObjWithoutRegister</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkbRBUS_Utility import *;
from tdkutility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("rbus","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

obj.configureTestCase(ip,port,'TS_RBUS_PushAndPullObjWithoutRegister');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[RBUS LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    print "\n*************Start of Broker Connection*******************************";
    tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
    tdkTestObj.addParameter("operation","openBrokerConnection");
    tdkTestObj.addParameter("objectName","tdkb_method"); #This Will be converted to Component name in Wrapper code
    tdkTestObj.addParameter("methodName","CloseConnectionBeforeOpen");#Close the connection before open if any
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "RBUS openBrokerConnection Detail is ",details

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Open the RBUS Broker connection";
        print "EXPECTED RESULT 1: rbus_openBrokerConnection Should be success";
        print "ACTUAL RESULT 1: rbus_openBrokerConnection was success";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

        print "\n*************Start of PULL Object without object Register*****************************"
        tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
        tdkTestObj.addParameter("operation","rbus_pullObj");
        tdkTestObj.addParameter("objectName","test_server_3.obj1");
        tdkTestObj.addParameter("methodName","rbus_client_test_string");         #Dummy Value
        expectedresult="FAILURE";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS PUSH Obj Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: PULL the object from RBUS ";
            print "EXPECTED RESULT 2: rbus_pullObj should be Failed, since object is not registered";
            print "ACTUAL RESULT 2: rbus_pullObj was Failed as expected";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            print "\n*************Start of PUSH Object without object Register*****************************"
            tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
            tdkTestObj.addParameter("operation","rbus_pushObj");
            tdkTestObj.addParameter("objectName","test_server_3.obj1");
            tdkTestObj.addParameter("methodName","rbus_client_test_string");     #Dummy Value
            expectedresult="FAILURE";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print "RBUS PUSH Obj Detail is ",details

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: PUSH the object with RBUS ";
                print "EXPECTED RESULT 3: rbus_pushObj should be Failed, since object is not regsitered";
                print "ACTUAL RESULT 3: rbus_pushObj was Failed as expected";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: PUSH the object with RBUS ";
                print "EXPECTED RESULT 3: rbus_pushObj should be Failed, since object is not regsitered";
                print "ACTUAL RESULT 3: rbus_pushObj was NOT Failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
            print "*************End of PUSH Object*******************************\n"

        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: PULL the object from RBUS ";
            print "EXPECTED RESULT 2: rbus_pullObj should be Failed, since object is not regsitered";
            print "ACTUAL RESULT 2: rbus_pullObj was NOT Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
        print "*************End of PULL Object*******************************\n"

        tdkTestObj = obj.createTestStep('RBUS_RegisterOperation');
        tdkTestObj.addParameter("operation","closeBrokerConnection");
        tdkTestObj.addParameter("objectName","tdkb_method"); #This Will be converted to Component name in Wrapper code
        tdkTestObj.addParameter("methodName","dummy");   #Dummy Value
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS closeBrokerConnection Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 4: Close the RBUS Broker connection";
            print "EXPECTED RESULT 4: rbus_closeBrokerConnection should be success";
            print "ACTUAL RESULT 4: rbus_closeBrokerConnection was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 4: Close the RBUS Broker connection";
            print "EXPECTED RESULT 4: rbus_closeBrokerConnection should be success";
            print "ACTUAL RESULT 4: rbus_closeBrokerConnection was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Open the RBUS Broker connection";
        print "EXPECTED RESULT 1: rbus_openBrokerConnection Should be success";
        print "ACTUAL RESULT 1: rbus_openBrokerConnection was Failed";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;

    print "*************End of Broker Connection*******************************\n"
    obj.unloadModule("rbus");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

