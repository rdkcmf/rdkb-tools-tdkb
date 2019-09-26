##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzSetRadioFragmentationThreshold</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set the radio fragmentation threshold using wifi_setRadioFragmentationThreshold() API for 2.4GHz.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_241</test_case_id>
    <test_objective>To set the Radio Fragmentation Threshold using wifi_setRadioFragmentationThreshold API for 2.4GHz.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioFragmentationThreshold()</api_or_interface_used>
    <input_parameters>methodName : setRadioFragmentationThreshold
ApIndex : 0</input_parameters>
    <automation_approch>1.Load the module.
2.Set the Radio Fragmentation Threshold using wifi_setRadioFragmentationThreshold() API
3.Return SUCCESS if set operation is successful,else FAILURE.
4.Unload the module</automation_approch>
    <except_output>To set the Radio Fragmentation Threshold for 2.4GHz</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetRadioFragmentationThreshold</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import random;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetRadioFragmentationThreshold');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetRadioFragmentationThreshold');

loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    expectedresult="SUCCESS";
    FragmentationThresholdRange = "sh %s/tdk_utility.sh parseConfigFile FRAGMENTATION_THRESHOLD_RANGE" %TDK_PATH;
    tdkTestObj.addParameter("command", FragmentationThresholdRange);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    FragmentationThresholdRange = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    FragmentationThresholdRangeList= FragmentationThresholdRange.split("-");

    if FragmentationThresholdRange and expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP : Get the FragmentationThresholdRange to be set from /etc/tdk_platform.properties file";
        print "EXPECTED RESULT : Should get the FragmentationThresholdRange to be set";
        print "ACTUAL RESULT : Got the FragmentationThresholdRange as %s" %FragmentationThresholdRange;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        mini = int(FragmentationThresholdRangeList[0]);
        maxi = int(FragmentationThresholdRangeList[1]);
        expectedresult="SUCCESS";
        radioIndex = 0
        setMethod = "setRadioFragmentationThreshold"
        primitive = 'WIFIHAL_GetOrSetParamUIntValue'
        setThreshold = random.randint(mini,maxi);
        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setThreshold, setMethod)

        if expectedresult in actualresult:
            print "setRadioFragmentationThreshold function successful: %s"%details
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Set the Radio Fragmentation Threshold value for 2.4GHz";
            print "EXPECTED RESULT 1: Function Should set a Radio Fragmentation Threshold value";
            print "ACTUAL RESULT 1: Radio Fragmentation Threshold value set Successfully: %d"%setThreshold;
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            print "setRadioFragmentationThreshold function failed: %s"%details
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Set the Radio Fragmentation Threshold value for 2.4GHz";
            print "EXPECTED RESULT 1: Function Should set a Radio Fragmentation Threshold value";
            print "ACTUAL RESULT 1: Failed to set Radio Fragmentation Threshold value: %d"%setThreshold;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Get the FragmentationThresholdRange to be set from /etc/tdk_platform.properties file";
        print "EXPECTED RESULT : Should get the FragmentationThresholdRange to be set";
        print "ACTUAL RESULT : Failed to get the FragmentationThresholdRange from /etc/tdk_platform.properties file";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
