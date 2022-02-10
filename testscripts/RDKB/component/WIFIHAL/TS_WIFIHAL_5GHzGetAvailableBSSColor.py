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
  <name>TS_WIFIHAL_5GHzGetAvailableBSSColor</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetAvailableBSSColor</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getAvailableBSSColor for 5G radio and check if the color list is non-empty if number of colors returned is greater than 0 or empty if the colors returned is equal to 0.</synopsis>
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
    <test_case_id>TC_WIFIHAL_742</test_case_id>
    <test_objective>Invoke the HAL API wifi_getAvailableBSSColor for 5G radio and check if the color list is non-empty if number of colors returned is greater than 0 or empty if the colors returned is equal to 0.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getAvailableBSSColor()</api_or_interface_used>
    <input_parameters>radioIndex : radio index of 5G
maxNumberColors : 63</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getAvailableBSSColor() for 5G radio and check if the API returns success.
3. Retrieve the number of colors returned value and check if the color list is non-empty when the number of colors returned is more than 0 or if the color list is empty when the number of colors returned is 0.
4. Return failure if any of the above conditions are not satisfied or if the number of colors returned is an invalid value.
5. Unload the module.</automation_approch>
    <expected_output>The HAL API wifi_getAvailableBSSColor for 2.4G radio should be invoked successfully and the color list should be non-empty if number of colors returned is greater than 0 or empty if the colors returned is equal to 0.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetAvailableBSSColor</test_script>
    <skipped>No</skipped>
    <release_version>M98</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetAvailableBSSColor');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Maximum value to be passed
        maxNumberColors = 63;
        tdkTestObj = obj.createTestStep("WIFIHAL_GetAvailableBSSColor");
        tdkTestObj.addParameter("radioIndex", idx);
        tdkTestObj.addParameter("maxNumberColors", maxNumberColors);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Invoke the HAL API wifi_getAvailableBSSColor() to retrieve the Color List for 5G radio";
        print "EXPECTED RESULT 1: Should invoke the HAL API wifi_getAvailableBSSColor() successfully";

        if expectedresult in actualresult and details != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: API was invoked successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check the Number of Color returned and Color List conditions
            print "\nTEST STEP 2 : Check if the Color List is non-empty if the number of Colors returned is greater than 0 and empty if number of Colors returned is 0";
            print "EXPECTED RESULT 2 : The Color List should be non-empty if number of Colors returned is greater than 0 and empty if number of Colors returned is 0";
            numColorReturned = details.split("NumColorReturned : ")[1].split(",")[0];
            print "Number of Color returned : %s" %numColorReturned;
            print "Details : %s" %details;

            if numColorReturned.isdigit() and int(numColorReturned) > 0:
                Available_BSSColor_List = details.split("Available BSSColor List = ")[1];
                print "Color List : %s" %Available_BSSColor_List;

                if Available_BSSColor_List != "":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 2: The number of colors is greater than 0 and the color list is non-empty";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 2: The number of colors is greater than 0 but the color list is empty";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

            elif numColorReturned.isdigit() and int(numColorReturned) == 0 and "Available BSSColor List is Empty" in details :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: The number of colors is equal to 0 and the color list is empty";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: The number of colors returned is invalid";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: API invocation failed";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
