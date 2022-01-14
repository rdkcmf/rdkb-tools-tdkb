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
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_6GHzSetRadioDcsScanning</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Invoke the HAL API wifi_setRadioDcsScanning() to toggle DCS scanning for 6G radio and cross check if the new enable value set is reflected in wifi_getRadioDcsScanning().</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIHAL_721</test_case_id>
    <test_objective>Invoke the HAL API wifi_setRadioDcsScanning() to toggle DCS scanning for 6G radio and cross check if the new enable value set is reflected in wifi_getRadioDcsScanning().</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioDcsScanning()
wifi_setRadioDcsScanning()</api_or_interface_used>
    <input_parameters>methodname : getRadioDcsScanning
methodname : setRadioDcsScanning
radioIndex : 6G radio index
param : 0 or 1 (Disabled or Enabled)</input_parameters>
    <automation_approch>1. Load the wifihal module
2. Invoke the HAL API wifi_geRadioDcsScanning() to get the initial DCS Scanning enable for 6G radio.
3. Toggle the enable status using the HAL API wifi_setRadioDcsScanning() and check if the set operation returns success.
4. Cross check the SET using the GET API wifi_geRadioDcsScanning().
5. Revert to initial enable state
6. Unload the module</automation_approch>
    <expected_output>The DCS Scanning enable state should be toggled successfully using the HAL API wifi_setRadioDcsScanning() and it should be reflected in the GET API wifi_getRadioDcsScanning() for 6G radio.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetRadioDcsScanning</test_script>
    <skipped>No</skipped>
    <release_version>M97</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetRadioDcsScanning');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    expectedresult = "SUCCESS";

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
        tdkTestObj.addParameter("methodName","getRadioDcsScanning");
        tdkTestObj.addParameter("radioIndex",idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Get the current enable state of Radio DCS scanning using the HAL API wifi_getRadioDcsScanning() for 6G radio";
        print "EXPECTED RESULT 1: Should get current enable state of Radio DCS scanning for 6G radio successfully";

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: API invocation success; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            currState = details.split(":")[1].strip();

            if "Enabled" in currState:
                newValue= 0;
                oldValue = 1;
                newState = "Disabled"
            else:
                newValue = 1;
                oldValue = 0;
                newState = "Enabled"

            print "Initial DCS Scanning enable state is : %s" %currState;

            #Toggle Dcs scanning
            tdkTestObj.addParameter("methodName","setRadioDcsScanning");
            tdkTestObj.addParameter("radioIndex",idx);
            tdkTestObj.addParameter("param",newValue);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP 2: Toggle the DCS Scanning enable to %s state using the HAL API wifi_setDcsScanning() for 6G radio" %newState;
            print "EXPECTED RESULT 2: Should toggle the DCS Scanning enable state successfully";

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: API invocation success; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"

                #Cross check the set with get
                tdkTestObj.addParameter("methodName","getRadioDcsScanning");
                tdkTestObj.addParameter("radioIndex",idx);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP 3 : Invoke wifi_getDcsScanning() after the set operation";
                print "EXPECTED RESULT 3 : The HAL API should be invoked  successfully";

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: API invocation success; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    new_enable = details.split(":")[1].strip();
                    print "\nTEST STEP 4 : Cross check if the Dcs Scanning enable SET is reflected in GET";
                    print "EXPECTED RESULT 4 : The Dcs Scanning enable SET should be reflected in GET";
                    print "DCS Scanning set : %s" %newState;
                    print "DCS Scanning get : %s" %new_enable;

                    if new_enable == newState:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 4: The SET matches with GET";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 4: The SET does not match with GET";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: API invocation failed; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert operation
                tdkTestObj.addParameter("methodName","setRadioDcsScanning");
                tdkTestObj.addParameter("radioIndex",idx);
                tdkTestObj.addParameter("param",oldValue);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Successfully reverted DCS Scanning to initial enable state";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Reverting DCS Scanning to initial enable state failed";

            else:
                #Set the result status of execution
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
    tdkTestObj.setResultStatus("FAILURE");
    print "Module loading failed";
