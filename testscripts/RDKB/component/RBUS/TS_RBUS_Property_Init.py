##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_RBUS_Property_Init</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>RBUS_PropertyCommands</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Validate the RBUS 2.0 API rbusProperty_Init</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_RBUS_51</test_case_id>
    <test_objective>To Validate the RBUS 2.0 API rbusProperty_Init </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script
3. The DUT should be in RBUS mode</pre_requisite>
    <api_or_interface_used>rbusProperty_Init</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Open the RBUS connection using rbus_open API
2. Initiate the RBUS Property using rbusProperty_Init API and return status should be success
3. Release the RBUS Property using rbusProperty_Release API and return status should be success
4. Close the RBUS connection using rbus_close API</automation_approch>
    <expected_output>Should be able to initiate the rbus Property using rbusProperty_Init API </expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_Property_Init</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("rbus","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_RBUS_Property_Init');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");

    print "\n********** Start of RBUS Open ****************"
    tdkTestObj = obj.createTestStep('RBUS_Open');
    expectedresult = "SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "RBUS Open Detail is ",details

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Open the RBUS connection";
        print "EXPECTED RESULT 1: rbus_open Should be success";
        print "ACTUAL RESULT 1: rbus_open was success";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "RBUS Open status is %s" %details;

        print "\n********** Start of RBUS Property Init (Prop1) ****************"
        tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
        tdkTestObj.addParameter("operation","rbusProperty_Init");
        tdkTestObj.addParameter("prop_count",1); #Prop1 to be initialized
        tdkTestObj.addParameter("property_name","Device.rbusPropertyTest1");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Initiate rbusProperty_Init function";
            print "EXPECTED RESULT 2: rbusProperty_Init should be success";
            print "ACTUAL RESULT 2: rbusProperty_Init was Success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Initiate rbusProperty_Init function";
            print "EXPECTED RESULT 2: rbusProperty_Init should be success";
            print "ACTUAL RESULT 2: rbusProperty_Init was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "********** End of RBUS Property Init (Prop1) ****************"

        print "\n********** Start of RBUS Property Release (Prop1) ****************"
        #Release the property, even step 2 was failed
        tdkTestObj = obj.createTestStep('RBUS_PropertyCommands');
        tdkTestObj.addParameter("operation","rbusProperty_Release");
        tdkTestObj.addParameter("prop_count",1); #Prop1 to be Released
        tdkTestObj.addParameter("property_name","Device.rbusPropertyTest1");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Initiate rbusProperty_Release function";
            print "EXPECTED RESULT 3: rbusProperty_Release should be success";
            print "ACTUAL RESULT 3: rbusProperty_Release  was Success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 3: Initiate rbusProperty_Release function";
            print "EXPECTED RESULT 3: rbusProperty_Release should be success";
            print "ACTUAL RESULT 3: rbusProperty_Release was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "********** End of RBUS Property Release (Prop1) ****************\n"

        print "********** Start of RBUS Close ****************"
        tdkTestObj = obj.createTestStep('RBUS_Close');
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "RBUS close Detail is ",details

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 4: Close the RBUS connection";
            print "EXPECTED RESULT 4: rbus_close should be success";
            print "ACTUAL RESULT 4: rbus_close was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 4: Close the RBUS connection";
            print "EXPECTED RESULT 4: rbus_close should be success";
            print "ACTUAL RESULT 4: rbus_close was Failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        print "********** End of RBUS Close ****************"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Open the RBUS connection";
        print "EXPECTED RESULT 1: rbus_open Should be success";
        print "ACTUAL RESULT 1: rbus_open was Failed";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    print "********** Close of RBUS Open ****************\n"
    obj.unloadModule("rbus");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";