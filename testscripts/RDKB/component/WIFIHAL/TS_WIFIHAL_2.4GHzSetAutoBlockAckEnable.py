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
  <version>1</version>
  <name>TS_WIFIHAL_2.4GHzSetAutoBlockAckEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Toggle AutoBlockActEnable and verify the set operation</synopsis>
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
    <test_case_id>TS_WIFIHAL_519</test_case_id>
    <test_objective>Toggle AutoBlockActEnable and verify the set operation</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>getAutoBlockAckEnable
setAutoBlockAckEnable</api_or_interface_used>
    <input_parameters>methodname : getAutoBlockAckEnable
methodname : setAutoBlockAckEnable
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke getAutoBlockAckEnable() and get the initial AutoBlockActEnable status
3. If initially True, set to false using setAutoBlockAckEnable and vice-versa
4. Check if the Set operation is success. If success revert the value to initial value.
5. If Set operation fails, return failure.
6. Unload wifihal module</automation_approch>
    <expected_output>Should be able to successfully toggle AutoBlockActEnable</expected_output>
    <priority>High</priority>
    <test_stub_interface>Wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetAutoBlockAckEnable</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
radio = "2.4G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetAutoBlockAckEnable');
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
        print "TEST STEP 1: Invoke the wifi_getAutoBlockAckEnable api";
        print "EXPECTED RESULT 1:Invocation of wifi_getAutoBlockAckEnable should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
        tdkTestObj.addParameter("methodName","getAutoBlockAckEnable")
        tdkTestObj.addParameter("radioIndex", idx)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: Invocation of wifi_getAutoBlockAckEnable was success. %s" %details;
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
            print "TEST STEP 2: Toggle the enabled state using wifi_setAutoBlockAckEnable api";
            print "EXPECTED RESULT 2: wifi_setAutoBlockAckEnable should successfully toggle AutoBlockAckEnable status to ",newStatus ;
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
            tdkTestObj.addParameter("methodName","setAutoBlockAckEnable")
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
                print "TEST STEP 3: Invoke  wifi_getAutoBlockAckEnable  to verify toggling done by wifi_setAutoBlockAckEnable api";
                print "EXPECTED RESULT 3: wifi_getAutoBlockAckEnable should be successfully invoked after set";
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                tdkTestObj.addParameter("methodName","getAutoBlockAckEnable")
                tdkTestObj.addParameter("radioIndex", idx)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                enable = details.split(":")[1].strip();
                if expectedresult in actualresult :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: Invocation of wifi_getAutoBlockAckEnable was success";
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    if enable == newStatus :
                        print "TEST STEP 4 : Verify if AutoBlockAckEnable set value and get value are same"
                        print "EXPECTED RESULT 4 : wifi_getAutoBlockAckEnable() returned enable state same as the set value"
                        print "ACTUAL RESULT 4:  %s" %details;
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        tdkTestObj.setResultStatus("SUCCESS");
                        #Revert AutoBlockAckEnable to initial value
                        print "TEST STEP 5: Revert the enabled state to %s using wifi_setAutoBlockAckEnable api" %enable;
                        print "EXPECTED RESULT 5: wifi_setAutoBlockAckEnable should successfully revert AutoBlockAckEnable status";
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                        tdkTestObj.addParameter("methodName","setAutoBlockAckEnable")
                        tdkTestObj.addParameter("radioIndex", idx)
                        tdkTestObj.addParameter("param", oldEnable)
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 5:  %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 5:  %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        print "TEST STEP 4 : Verify if AutoBlockAckEnable set value and get value are same"
                        print "EXPECTED RESULT 4 : wifi_getAutoBlockAckEnable() returned enable state different from the set value"
                        print "ACTUAL RESULT 4:  %s" %details;
                        tdkTestObj.setResultStatus("FAILURE");
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: Invocation of wifi_getAutoBlockAckEnable was failure";
                    print "[TEST EXECUTION RESULT] : FAILURE"
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
