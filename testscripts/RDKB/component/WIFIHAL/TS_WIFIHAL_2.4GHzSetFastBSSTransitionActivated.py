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
  <version>2</version>
  <name>TS_WIFIHAL_2.4GHzSetFastBSSTransitionActivated</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_setFastBSSTransitionActivated() to toggle the Fast BSS Transition Activated enable status and verify the SET with wifi_getBSSTransitionActivated() HAL API for 2.4G private AP.</synopsis>
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
    <test_case_id>TC_WIFIHAL_799</test_case_id>
    <test_objective>Invoke the HAL API wifi_setFastBSSTransitionActivated() to toggle the Fast BSS Transition Activated enable status and verify the SET with wifi_getBSSTransitionActivated() HAL API for 2.4G private AP.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getBSSTransitionActivated()
wifi_setFastBSSTransitionActivated()</api_or_interface_used>
    <input_parameters>radioIndex : 2.4G Private AP index
param : enable/disable(1/0)</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getBSSTransitionActivated() for 2.4G private AP to retrieve the initial FBT enable status.
3. Toggle the current FBT enable status using the HAL API wifi_setFastBSSTransitionActivated() for 2.4G and check if the API returns success.
4. Invoke wifi_getBSSTransitionActivated() to cross check the SET with GET.
5. Revert to initial FBT enable state
6. Unload module</automation_approch>
    <expected_output>The HAL API wifi_setFastBSSTransitionActivated() should successfully toggle the FBT enable status for 2.4G private AP and the SET should reflect in the GET API wifi_getBSSTransitionActivated().</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetFastBSSTransitionActivated</test_script>
    <skipped>No</skipped>
    <release_version>M101</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetFastBSSTransitionActivated');

#Get the result of connection with test component and DUT
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
        print "\nTEST STEP 1: Invoke the HAL API wifi_getBSSTransitionActivated() for 2.4G Private AP";
        print "EXPECTED RESULT 1:Invocation of wifi_getBSSTransitionActivated() should be success";

        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
        tdkTestObj.addParameter("methodName","getBSSTransitionActivated")
        tdkTestObj.addParameter("radioIndex", idx)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: Invocation of wifi_getBSSTransitionActivated() was success. Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            initial_enable = details.split(":")[1].strip();
            print "Initial Enable status : ", initial_enable;
            if "Enabled" in initial_enable:
                oldEnable = 1
                newEnable = 0
                newStatus = "Disabled"
            else:
                oldEnable = 0
                newEnable = 1
                newStatus = "Enabled"

            print "\nTEST STEP 2: Toggle the enabled state using the HAL API wifi_setFastBSSTransitionActivated() for 2.4G Private AP";
            print "EXPECTED RESULT 2: wifi_setFastBSSTransitionActivated() should successfully toggle FastBSSTransitionActivated status to ",newStatus ;

            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
            tdkTestObj.addParameter("methodName","setFastBSSTransitionActivated")
            tdkTestObj.addParameter("radioIndex", idx)
            tdkTestObj.addParameter("param", newEnable)
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2:  wifi_setFastBSSTransitionActivated() invocation success; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                print "\nTEST STEP 3: Invoke the HAL API wifi_getBSSTransitionActivated() to verify toggling done by wifi_setFastBSSTransitionActivated()";
                print "EXPECTED RESULT 3: wifi_getBSSTransitionActivated() should return the value set by wifi_setFastBSSTransitionActivated()";

                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                tdkTestObj.addParameter("methodName","getBSSTransitionActivated")
                tdkTestObj.addParameter("radioIndex", idx)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult :

                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: Invocation of wifi_getBSSTransitionActivated() was success. Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    print "\nTEST STEP 4 : Verify if BSSTransitionActivated set value and get value are same";
                    print "EXPECTED RESULT 4 : wifi_getBSSTransitionActivated() should enable state same as the set value";
                    final_enable = details.split(":")[1].strip();
                    print "SET value : ", newStatus;
                    print "GET value : ", final_enable;

                    if final_enable == newStatus :
                        print "ACTUAL RESULT 4:  SET matches with the GET";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        tdkTestObj.setResultStatus("SUCCESS");

                        #Revert FTOverDSActivated to initial value
                        print "\nTEST STEP 5: Revert the enabled state to %s using wifi_setFastBSSTransitionActivated() api" %initial_enable;
                        print "EXPECTED RESULT 5: wifi_setFastBSSTransitionActivated() should successfully revert BSSTransitionActivated status";

                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                        tdkTestObj.addParameter("methodName","setFastBSSTransitionActivated")
                        tdkTestObj.addParameter("radioIndex", idx)
                        tdkTestObj.addParameter("param", oldEnable)
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 5: Revert operation success; Details : %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 5: Revert operation failed; Details : %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        print "ACTUAL RESULT 4: SET not reflected in GET";
                        tdkTestObj.setResultStatus("FAILURE");
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: API invocation failed; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: API invocation failed; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: API invocation failed; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
