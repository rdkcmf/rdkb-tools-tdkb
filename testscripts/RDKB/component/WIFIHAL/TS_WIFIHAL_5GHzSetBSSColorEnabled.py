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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzSetBSSColorEnabled</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Validate wifi_setBSSColorEnabled() using wifi_getBSSColorEnabled()</synopsis>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_479</test_case_id>
    <test_objective>Validate wifi_setBSSColorEnabled() using wifi_getBSSColorEnabled()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setBSSColorEnabled
wifi_getBSSColorEnabled</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getBSSColorEnabled for 5GHz and save the current BSSColorEnabled status
3. Toggle the BSSColorEnabled value using wifi_setBSSColorEnabled()
4. Invoke wifi_getBSSColorEnabled and verify if set value is reflecting
5. Revert back to initial BSSColorEnabled value using wifi_setBSSColorEnabled()
6. Unload wifi hal module</automation_approch>
    <expected_output>wifi_setBSSColorEnabled() should successfully set BSSColorEnabled() status</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetBSSColorEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M85</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetBSSColorEnabled');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        print "TEST STEP 1: Invoke the wifi_getBSSColorEnabled api";
        print "EXPECTED RESULT 1:Invocation of wifi_getBSSColorEnabled should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
        tdkTestObj.addParameter("methodName","getBSSColorEnabled")
        tdkTestObj.addParameter("radioIndex", idx)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: Invocation of wifi_getBSSColorEnabled was success. %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    enable = details.split(":")[1].strip()
	    if "Enabled" in enable:
	        oldEnable = 1
	        newEnable = 0
                newStatus = "Disabled"
	    else:
	        oldEnable = 0
	        newEnable = 1
                newStatus = "Enabled"

            print "TEST STEP 2: Toggle the enabled state using wifi_setBSSColorEnabled api";
            print "EXPECTED RESULT 2: wifi_setBSSColorEnabled should successfully toggle BSSColorEnabled status to ",newStatus ;
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
            tdkTestObj.addParameter("methodName","setBSSColorEnabled")
            tdkTestObj.addParameter("radioIndex", idx)
            tdkTestObj.addParameter("param", newEnable)
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2:  %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                print "TEST STEP 3: Invoke  wifi_getBSSColorEnabled  to verify toggling done by wifi_setBSSColorEnabled api";
                print "EXPECTED RESULT 3: wifi_getBSSColorEnabled   should return the value set by wifi_setBSSColorEnabled";
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                tdkTestObj.addParameter("methodName","getBSSColorEnabled")
                tdkTestObj.addParameter("radioIndex", idx)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and enable not in details.split(":")[1].strip():
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "wifi_getBSSColorEnabled() returned enable state same as the set value"
                    print "ACTUAL RESULT 3:  Invocation of wifi_getBSSColorEnabled was success. %s" %details;
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3:  %s" %details;
                    print "[TEST EXECUTION RESULT] : FAILURE";
                #Revert BSSColorEnabled to initial value
                print "TEST STEP 4: Revert the enabled state to %s using wifi_setBSSColorEnabled api" %enable;
                print "EXPECTED RESULT 4: wifi_setBSSColorEnabled should successfully revert BSSColorEnabled status";
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                tdkTestObj.addParameter("methodName","setBSSColorEnabled")
                tdkTestObj.addParameter("radioIndex", idx)
                tdkTestObj.addParameter("param", oldEnable)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4:  %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4:  %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2:  %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
