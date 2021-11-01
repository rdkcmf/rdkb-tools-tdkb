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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WANMANAGER_CheckERouterAndWANSubnetIP_Equals</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Check eRouter subnet masks equals to WAN Subnet mask  in a WAN_MANAGER Enabled build</synopsis>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WANMANAGER_111</test_case_id>
    <test_objective>This test case is to Check eRouter subnet masks equals to WAN Subnet mask  in a WAN_MANAGER Enabled build </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.WAN Manager should be enabled</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>none</input_parameters>
    <automation_approch>1.Load the module
2.Get the WAN subent mask and erouter subnet mask
3.The subnet mask are expected to be present and equal
4.Unload the module</automation_approch>
    <expected_output>Subnet mask are expected to be present and equal for WAN and erouter</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_CheckERouterAndWANSubnetIP_Equals</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from WanManager_Utility import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_CheckERouterAndWANSubnetIP_Equals');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    query="sysevent get ipv4_wan_subnet";
    print "query:%s" %query
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", query)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult1 = tdkTestObj.getResult();
    wan_mask = tdkTestObj.getResultDetails().strip().replace("\\n","");

    query="sysevent get ipv4_erouter0_subnet";
    print "query:%s" %query
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", query)
    expectedresult2="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult2 = tdkTestObj.getResult();
    erouter_mask = tdkTestObj.getResultDetails().strip().replace("\\n","");
    if expectedresult in (actualresult1 and actualresult2):
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 :Get th subnet mask for wan and erouter0";
        print "EXPECTED RESULT 1: Should get subnet mask for wan and erouter0 ";
        print "ACTUAL RESULT 1: wan_mask : %s,erouter_mask :%s"%(wan_mask,erouter_mask);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        if wan_mask != "" and erouter_mask != "" and (wan_mask == erouter_mask):
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2:check if subnet mask for wan and erouter0 are non empty and equal";
            print "EXPECTED RESULT 2: Should get subnet mask for wan and erouter0 non empty and equal";
            print "ACTUAL RESULT 2: wan_mask : %s,erouter_mask :%s"%(wan_mask,erouter_mask);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2:check if ipv4 subnet address for wan and erouter0 are non-empty and equal";
            print "EXPECTED RESULT 2: Should get ipv4 subnet address for wan and erouter0 are non-empty and equal";
            print "ACTUAL RESULT 2: wan_mask : %s,erouter_mask :%s"%(wan_mask,erouter_mask);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        print "TEST STEP 1 :Get th ipv4 subnet address for wan and erouter0";
        print "EXPECTED RESULT 1: Should get ipv4 subnet address for wan and erouter0";
        print "ACTUAL RESULT 1: wan_mask : %s,erouter_mask :%s,ifconfig erouter ip :%s"%(wan_mask,erouter_mask,ifconfig_ip);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
