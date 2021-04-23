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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WANMANAGER_FileExists_PhylinkWanStateUp</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>check if phylink_wan_state_up file is created in tmp folder when WAN Manager is Enabled</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WANMANAGER_18</test_case_id>
    <test_objective>check if phylink_wan_state_up file is created in tmp folder when WAN Manager is Enabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>none</input_parameters>
    <automation_approch>1.Load the module
2.Check if WAN Manager is enabled
3.Check if file phylink_wan_state_up exist
4.Unload the module</automation_approch>
    <expected_output>phylink_wan_state_up file is expected to be present in wan manager enabled</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_FileExists_PhylinkWanStateUp</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
obj1= tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_FileExists_PhylinkWanStateUp');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_FileExists_PhylinkWanStateUp');
#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1 = obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.Enable");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and details == "true":
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 : Check if WAN Manager is enabled";
        print "EXPECTED RESULT 1: WAN Manager should be enabled";
        print "ACTUAL RESULT 1: wan manager enable status is :",details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        query="ls /tmp/phylink_wan_state_up";
        print "query:%s" %query
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter("command", query)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n","");
        if expectedresult in actualresult and "No such file or directory" not in details:
            details = details.replace("\\t","");
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Checking if phylink_wan_state_up file is present";
            print "EXPECTED RESULT 2:phylink_wan_state_up file should be presented for reverse ssh to work";
            print "ACTUAL RESULT 2:",details;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Checking if phylink_wan_state_up file is present";
            print "EXPECTED RESULT 2:phylink_wan_state_up file should be presented for reverse ssh to work";
            print "ACTUAL RESULT 2:",details;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1 : Check if WAN Manager is enabled";
        print "EXPECTED RESULT 1: WAN Manager should be enabled";
        print "ACTUAL RESULT 1: wan manager enable status is :",details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("sysutil");
    obj1.unloadModule("tdkbtr181");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
