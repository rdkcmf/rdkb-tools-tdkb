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
  <version>8</version>
  <name>TS_WIFIHAL_2.4GHzSetBSSColor</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_SetBSSColor</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_setBSSColor() to set a BSS Color in the acceptable range of 1-63 and check if the value set is reflected in the GET API wifi_getBSSColor() for 2.4G radio.</synopsis>
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
    <test_case_id>TC_WIFIHAL_782</test_case_id>
    <test_objective>Invoke the HAL API wifi_setBSSColor() to set a BSS Color in the acceptable range of 1-63 and check if the value set is reflected in the GET API wifi_getBSSColor() for 2.4G radio.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getBSSColor()
wifi_setBSSColor()</api_or_interface_used>
    <input_parameters>radioIndex : 2.4G radio index
color : BSS Color value in the range 1-63</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getBSSColor() to retrieve the initial BSS Color value and check if it is within the valid range of 1-63
3. Invoke the HAL API wifi_setBSSColor() to set a new BSS color in the valid range excluding the initial value.
4. Cross check if the SET BSS Color is reflected in the GET.
5. Revert to the initial state
6. Unload the module</automation_approch>
    <expected_output>The HAL API wifi_setBSSColor() should be successfully invoked to set BSS Color in the acceptable range of 1-63 and value set should be reflected in the GET API wifi_getBSSColor() for 2.4G radio.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetBSSColor</test_script>
    <skipped>No</skipped>
    <release_version>M100</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from random import choice;
from time import sleep;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetBSSColor');

#Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep("WIFIHAL_GetBSSColorValue");
        tdkTestObj.addParameter("radioIndex", idx)
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Invoke the HAL API wifi_getBSSColor() for 2.4G radio";
        print "EXPECTED RESULT 1:Invocation of wifi_getBSSColor() should be success";

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: Invocation of wifi_getBSSColor() was success; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            bssColor = details.split(":")[1].strip()
            print "\nTEST STEP 2: Check if value returned by wifi_getBSSColor() api is between 0 and 63";
            print "EXPECTED RESULT 2 : The value returned by wifi_getBSSColor() api should be between 0 and 63";

            if bssColor.isdigit() and 1 <= int(bssColor) and int(bssColor) <= 63:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: BssColor = %s. Value is in the expected range" %bssColor
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Set a random BSSColor value in the acceptable range of 1-63 excluding the initial BSS color
                set_bsscolor =  choice([i for i in range(1,63) if i not in [int(bssColor)]]);
                tdkTestObj = obj.createTestStep("WIFIHAL_SetBSSColor");
                tdkTestObj.addParameter("radioIndex", idx);
                tdkTestObj.addParameter("color", set_bsscolor);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP 3: Invoke the HAL API wifi_setBSSColor() with BSS Color value %d" %set_bsscolor;
                print "EXPECTED RESULT 3: wifi_setBSSColor() should be invoked successfully";

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: Invocation of wifi_setBSSColor() was success; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Invoke the GET API and cross check the SET
                    sleep(5);
                    tdkTestObj = obj.createTestStep("WIFIHAL_GetBSSColorValue");
                    tdkTestObj.addParameter("radioIndex", idx)
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    print "\nTEST STEP 4: Invoke the HAL API wifi_getBSSColor() for 2.4G radio after the SET operation";
                    print "EXPECTED RESULT 4:Invocation of wifi_getBSSColor() should be success";

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 4: Invocation of wifi_getBSSColor() was success; Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        new_bsscolor = details.split(":")[1].strip();
                        if new_bsscolor.isdigit():
                            new_bsscolor = int(new_bsscolor);

                            print "\nTEST STEP 5: Check if BSS color SET matches with GET";
                            print "EXPECTED RESULT 5: The BSS color SET should match with GET";
                            print "BSS Color Set : %d" %set_bsscolor;
                            print "BSS Color Get : %d" %new_bsscolor;

                            if new_bsscolor == set_bsscolor:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT 5: BSS color SET matches with GET";
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT 5: BSS color SET does not match with GET";
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            print "The BSS Color received is not a valid integer value";
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 4: Invocation of wifi_getBSSColor() was failed; Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";

                    #Revert operation
                    bssColor = int(bssColor);
                    tdkTestObj = obj.createTestStep("WIFIHAL_SetBSSColor");
                    tdkTestObj.addParameter("radioIndex", idx);
                    tdkTestObj.addParameter("color", bssColor);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    print "\nTEST STEP 6: Invoke the HAL API wifi_setBSSColor() with BSS Color value %d" %bssColor;
                    print "EXPECTED RESULT 6: wifi_setBSSColor() should be invoked successfully";

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 3: Revert operation was success; Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 3: Revert operation failed; Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: Invocation of wifi_setBSSColor() was failed; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "ACTUAL RESULT 2: BssColor = %s. Value is not within the expected range" %bssColor
                 print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: Invocation of wifi_getBSSColor() failed; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
