##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <version>10</version>
  <name>TS_platform_stub_hal_SetDscp</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_SetDscp</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the HAL API platform_hal_SetDscp() returns success when the traffic count is started and then stopped for the given DSCP WAN values.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_HAL_PLATFORM_89</test_case_id>
    <test_objective>To check if the HAL API platform_hal_SetDscp() returns success when the traffic count is started and then stopped for the given DSCP WAN values.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_SetDscp()</api_or_interface_used>
    <input_parameters>interfaceType : 1(DOCSIS)
cmd : 1(TRAFFIC_CNT_START) or 2(TRAFFIC_CNT_STOP)
dscpVal : "10,24"</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API platform_hal_SetDscp() to start the traffic count for the DSCP WAN values "10,24". Check if the API invocation is success.
3. Invoke the HAL API platform_hal_SetDscp() to stop the traffic count for the DSCP WAN values "10,24". Check if the API invocation is success.
4. Unload the module</automation_approch>
    <expected_output>The invocation of the HAL API platform_hal_SetDscp() should return success when the traffic count is started and then stopped for the given DSCP WAN values.</expected_output>
    <priority>High</priority>
    <test_stub_interface>platformhal</test_stub_interface>
    <test_script>TS_platform_stub_hal_SetDscp</test_script>
    <skipped>No</skipped>
    <release_version>M104</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_SetDscp');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Start the DSCP WAN traffic count
    tdkTestObj = obj.createTestStep("platform_stub_hal_SetDscp");
    #For DOCSIS interface
    tdkTestObj.addParameter("interfaceType",1);
    #To start the traffic count
    tdkTestObj.addParameter("cmd",1);
    #DSCP WAN values to be set
    tdkTestObj.addParameter("dscpVal","10,24");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP 1: Invoke the HAL API platform_hal_SetDscp() to start the traffic counts for the DSCP WAN values 10,24";
    print "EXPECTED RESULT 1: platform_hal_SetDscp() should be invoked successfully to start the traffic counts for the DSCP WAN values 10,24";

    if expectedresult in actualresult and "platform_hal_setDscp() function invocation was successful" in details:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: %s"%details
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Stop the DSCP WAN traffic count
        tdkTestObj = obj.createTestStep("platform_stub_hal_SetDscp");
        #For DOCSIS interface
        tdkTestObj.addParameter("interfaceType",1);
        #To stop the traffic count
        tdkTestObj.addParameter("cmd",2);
        #DSCP WAN values to be set
        tdkTestObj.addParameter("dscpVal","10,24");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 2: Invoke the HAL API platform_hal_SetDscp() to stop the traffic counts for the DSCP WAN values 10,24";
        print "EXPECTED RESULT 2: platform_hal_SetDscp() should be invoked successfully to stop the traffic counts for the DSCP WAN values 10,24";

        if expectedresult in actualresult and "platform_hal_setDscp() function invocation was successful" in details:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: %s"%details
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: %s"%details
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: %s"%details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("halplatform");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
