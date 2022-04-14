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
  <version>2</version>
  <name>TS_WIFIHAL_5GHzSetFTR1KeyHolderID</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetFTR1KeyHolderID</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set the FTR1 Key Holder ID by invoking the HAL API wifi_setFTR1KeyHolderID() and validate the SET using the GET API wifi_getFTR1KeyHolderID() for 5G private AP</synopsis>
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
    <test_case_id>TC_WIFIHAL_774</test_case_id>
    <test_objective>Set the FTR1 Key Holder ID by invoking the HAL API wifi_setFTR1KeyHolderID() and validate the SET using the GET API wifi_getFTR1KeyHolderID() for 5G private AP</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setFTR1KeyHolderID()
wifi_getFTR1KeyHolderID()</api_or_interface_used>
    <input_parameters>methodName : getFTR1KeyHolderID
methodName : setFTR1KeyHolderID
apIndex : 5G private AP index
radioIndex : 5G radio index
KeyHolderID : string value assigned dynamically in MAC format</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial FTR1 Key Holder ID using the HAL API wifi_getFTR1KeyHolderID() for 5G private AP.
3. Get the corresponding unicode string representation of the initial Key Holder and store it.
4. Generate a new Key Holder ID randomly
5. Invoke the HAL API wifi_setFTR1KeyHolderID() and pass the newly generated Key Holder ID for 5G private API and check if the SET operation returns success.
6. Invoke the HAL API wifi_getFTR1KeyHolderID() and retrieve the current Key Holder ID after the set operation.
7. Compare if the Key Holder ID retrieved is same as the SET value.
8. Revert to initial state.
9. Unload the modules.</automation_approch>
    <expected_output>Should be able to set the FTR1 Key Holder ID by invoking the HAL API wifi_setFTR1KeyHolderID() and the SET value should be validated successfully using the GET API wifi_getFTR1KeyHolderID() for 5G private AP.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetFTR1KeyHolderID</test_script>
    <skipped>No</skipped>
    <release_version>M100</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def getKeyHolder(tdkTestObj, apIndex):
    expectedresult = "SUCCESS";
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetFTR1KeyHolderID");
    tdkTestObj.addParameter("methodName","getFTR1KeyHolderID");
    tdkTestObj.addParameter("apIndex",apIndex);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return tdkTestObj, actualresult, details;

def setKeyHolder(tdkTestObj, apIndex, radioIndex, setValue):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("methodName","setFTR1KeyHolderID");
    tdkTestObj.addParameter("apIndex",apIndex);
    tdkTestObj.addParameter("radioIndex", radioIndex);
    tdkTestObj.addParameter("KeyHolderID", setValue);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return tdkTestObj, actualresult, details;

def HextoUnicodeConversion(num_hex_values, hex_values):
    #Covert the Hex value to corresponding unicode value
    unicode_string = [];
    unicode_key_id = "";
    for iteration in range(0, num_hex_values) :
        hex_to_integer = int(hex_values[iteration], 0);
        unicode_string.append(chr(hex_to_integer));
        #Concatenate the string parts to get the full unicode string value
        unicode_key_id = unicode_key_id + unicode_string[iteration];

    print "The Equivalent unicode string value of the FTR1 Key Holder ID is : %s" %unicode_key_id;
    return unicode_key_id

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
from random import randint;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetFTR1KeyHolderID');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObjTemp, idx = getIndex(obj, radio);
    #Check if an invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetFTKeyHolderID");
        tdkTestObj, actualresult, details = getKeyHolder(tdkTestObj, idx);

        print "\nTEST STEP 1: Invoke the HAL API wifi_getFTR1KeyHolderID() to retrieve the FTR1 Key Holder ID for 5G private AP";
        print "EXPECTED RESULT 1: Should get the FTR1 Key Holder ID using the HAL API successfully";

        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: API was invoked successfully; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if proper Hex values are retrieved and convert them to corresponding string value
            print "\nTEST STEP 2 : Check if the FTR1 Key Holder ID is retrieved as one or more Hex Values";
            print "EXPECTED RESULT 2 : FTR1 Key Holder ID should be retrieved as one or more Hex Values";
            details = details.split("Key Holder ID");

            #Compute the number of Hex values by subtracting the first two list elements as they are debug prints
            details.remove(details[0]);
            details.remove(details[0]);
            num_hex_values = len(details);
            print "Number of Hex values : %d" %num_hex_values;
            #Retrieve each of the value separately in a list
            hex_values = [];

            for iteration in range(0, num_hex_values):
                hex_values.append(details[iteration].split(" : ")[1]);
                print "FTR1 Key Holder ID[%d] : %s" %(iteration, hex_values[iteration]);

            if num_hex_values >= 1:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: FTR1 Key Holder ID is retrieved as the Hex values : ", hex_values;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Covert to corresponding unicode string
                initial_KeyHolder = HextoUnicodeConversion(num_hex_values, hex_values);

                #Set to new Key Holder ID(in MAC format)
                radioIndex = idx;
                apIndex = idx;
                setValue = str(randint(0, 9)) + str(randint(0, 9)) + ":" + str(randint(0, 9)) + str(randint(0, 9)) + ":" + str(randint(0, 9)) + str(randint(0, 9)) + ":" + str(randint(0, 9)) + str(randint(0, 9)) + ":" + str(randint(0, 9)) + str(randint(0, 9)) + ":" + str(randint(0, 9)) + str(randint(0, 9));
                tdkTestObj, actualresult, details = setKeyHolder(tdkTestObj, apIndex, radioIndex, setValue);

                print "\nTEST STEP 3: Invoke the HAL API wifi_setFTR1KeyHolderID() to set the FTR1 Key Holder ID for 5G private AP";
                print "EXPECTED RESULT 3: Should set the FTR1 Key Holder ID to %s using the HAL API successfully" %setValue;

                if expectedresult in actualresult :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: API was invoked successfully; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Cross check the SET with GET API
                    tdkTestObj, actualresult, details = getKeyHolder(tdkTestObj, apIndex);
                    print "\nTEST STEP 4: Invoke the HAL API wifi_getFTR1KeyHolderID() to retrieve the FTR1 Key Holder ID Set operation";
                    print "EXPECTED RESULT 4: Should get the FTR1 Key Holder ID using the HAL API successfully";

                    if expectedresult in actualresult :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 4: API was invoked successfully after SET operation; Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Check if proper Hex values are retrieved and convert them to corresponding string value
                        print "\nTEST STEP 5 : Check if the FTR1 Key Holder ID is retrieved as one or more Hex Values after set operation";
                        print "EXPECTED RESULT 5 : FTR1 Key Holder ID should be retrieved as one or more Hex Values after set operation";
                        details = details.split("Key Holder ID");

                        #Compute the number of Hex values by subtracting the first two list elements as they are debug prints
                        details.remove(details[0]);
                        details.remove(details[0]);
                        num_hex_values = len(details);
                        print "Number of Hex values : %d" %num_hex_values;
                        #Retrieve each of the value separately in a list
                        hex_values_final = [];

                        for iteration in range(0, num_hex_values):
                            hex_values_final.append(details[iteration].split(" : ")[1]);
                            print "FTR1 Key Holder ID[%d] : %s" %(iteration, hex_values_final[iteration]);

                        if num_hex_values >= 1:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 5: FTR1 Key Holder ID is retrieved as the Hex values : ", hex_values_final;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Covert to corresponding unicode string
                            final_KeyHolder = HextoUnicodeConversion(num_hex_values, hex_values_final);
                            print "\nTEST STEP 6 : Check if the SET value and GET value of FTR1 Key Holder ID match";
                            print "EXPECTED RESULT 6 :Tthe SET value and GET value of FTR1 Key Holder ID should match";
                            print "SET FTR1 Key Holder ID : %s" %setValue;
                            print "GET FTR1 Key Holder ID : %s" %final_KeyHolder;

                            if setValue == final_KeyHolder:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT 6: The SET value and GET value of FTR1 Key Holder ID match";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                #Revert to initial FT Key Holder ID
                                tdkTestObj, actualresult, details = setKeyHolder(tdkTestObj, apIndex, radioIndex, initial_KeyHolder);
                                print "\nTEST STEP 7: Invoke the HAL API wifi_setFTR1KeyHolderID() to revert to initial value";
                                print "EXPECTED RESULT 7: Should set the Key Holder ID to %s using the HAL API successfully" %initial_KeyHolder;

                                if expectedresult in actualresult :
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT 7: Revert operation success; Details : %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else :
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT 7: Revert operation failed; Details : %s" %details;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT 6: The SET value and GET value of FT Key Holder ID does not match";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 5: FTR1 Key Holder ID is not retrieved as two Hex values";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 4: API was not invoked successfully after SET operation; Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: API was not invoked successfully; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: FTR1 Key Holder ID is not retrieved as one or more Hex values";
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
