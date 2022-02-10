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
  <name>TS_WIFIHAL_5GHzSetFTMobilityDomainID</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetFTMobilityDomainID</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set the FT Mobility Domain ID by invoking the HAL API wifi_setFTMobilityDomainID() and validate the SET using the GET API wifi_getFTMobilityDomainID() for 5G private AP.</synopsis>
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
    <test_case_id>TC_WIFIHAL_727</test_case_id>
    <test_objective>Set the FT Mobility Domain ID by invoking the HAL API wifi_setFTMobilityDomainID() and validate the SET using the GET API wifi_getFTMobilityDomainID() for 5G private AP.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getFTMobilityDomainID()
wifi_setFTMobilityDomainID()</api_or_interface_used>
    <input_parameters>methodName : getFTMobilityDomainID()
methodName : setFTMobilityDomainID()
apIndex : 5G Private AP index
radioIndex : 5G radio index
mobilityDomain : setvalue(dynamically passed)</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getFTMobilityDomainID() for 5G Private AP and check if the API invocation is success and the FT Mobility Domain ID retrieved is a pair of Hexadecimal values.
3. Combine the Hex value and obtain the equivalent decimal value for FT Mobility Domain ID and store the initial value.
4. Invoke the HAL API wifi_setFTMobilityDomainID() for 5G private AP with a dynamically selected Mobility Domain ID. Check if the SET API returns success.
5. Invoke the GET API, retrieve the Hexadecimal values and convert to the equivalent decimal.
6. Check if the GET value matches with the SET value.
7. Revert the FT Mobility Domain ID to initial value.
8. Unload the modules
</automation_approch>
    <expected_output>Should successfully set the FT Mobility Domain ID by invoking the HAL API wifi_setFTMobilityDomainID() and the FT Mobility Domain ID set should reflect in the GET API wifi_getFTMobilityDomainID() for 5G Private AP.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetFTMobilityDomainID</test_script>
    <skipped>No</skipped>
    <release_version>M98</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
def getMobilityDomain(tdkTestObj, apIndex):
    expectedresult = "SUCCESS";
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetFTMobilityDomainID");
    tdkTestObj.addParameter("methodName","getFTMobilityDomainID");
    tdkTestObj.addParameter("apIndex",apIndex);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return tdkTestObj, actualresult, details;

def setMobilityDomain(tdkTestObj, apIndex, radioIndex, setValue):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("methodName","setFTMobilityDomainID");
    tdkTestObj.addParameter("apIndex",apIndex);
    tdkTestObj.addParameter("radioIndex", radioIndex);
    tdkTestObj.addParameter("mobilityDomain", setValue);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return tdkTestObj, actualresult, details;

def HextoIntConversion(hex_value0, hex_value1):
    #Covert the Hex value to corresponding integer value
    hex0 = hex_value0.split("0x")[1];
    hex1 = hex_value1.split("0x")[1];
    #Ensure that 0xf is considered as 0x0f
    if len(hex0) == 1:
        hex0 = "0" + hex0;
    if len(hex1) == 1:
        hex1 = "0" + hex1;
    #Concatenate the two Hex parts to get the full hex value
    hex_value = hex1 + hex0;
    mobility_id = int(hex_value, 16);
    print "\nThe Hex value after combining the Mobility Domain IDs is : 0x%s" %hex_value;
    print "The Equivalent integer value of the Mobility Domain ID is : %d" %mobility_id;
    return mobility_id;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
from random import randint;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetFTMobilityDomainID');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetFTMobilityDomainID');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetFTMobilityDomainID");
        tdkTestObj, actualresult, details = getMobilityDomain(tdkTestObj, idx);

        print "\nTEST STEP 1: Invoke the HAL API wifi_getFTMobilityDomainID() to retrieve the Mobility Domain ID for 5G private AP";
        print "EXPECTED RESULT 1: Should get the Mobility Domain ID using the HAL API successfully";

        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: API was invoked successfully; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if proper Hex values are retrieved and convert them to integer value
            print "\nTEST STEP 2 : Check if the FT Mobility Domain ID is retrieved as two Hex Values";
            print "EXPECTED RESULT 2 : FT Mobility Domain ID should be retrieved as two Hex Values";

            hex_value0 = details.split("ID[0] : ")[1].split(",")[0];
            hex_value1 = details.split("ID[1] : ")[1];
            print "Mobility Domain ID[0] : %s" %hex_value0;
            print "Mobility Domain ID[1] : %s" %hex_value1;

            if "0x" in hex_value0 and "0x" in hex_value1:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: FT Mobility Domain ID is retrieved as two Hex values";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Covert to corresponding Integer values
                initial_FTMDID = HextoIntConversion(hex_value0, hex_value1);

                #Set to new Mobility Domain ID
                radioIndex = idx;
                apIndex = idx;
                setValue = randint(0, 10000);
                tdkTestObj, actualresult, details = setMobilityDomain(tdkTestObj, apIndex, radioIndex, setValue)

                print "\nTEST STEP 3: Invoke the HAL API wifi_setFTMobilityDomainID() to set the Mobility Domain ID for 5G private AP";
                print "EXPECTED RESULT 3: Should set the Mobility Domain ID to %d using the HAL API successfully" %setValue;

                if expectedresult in actualresult :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: API was invoked successfully; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Cross check the SET with GET API
                    tdkTestObj, actualresult, details = getMobilityDomain(tdkTestObj, idx);

                    print "\nTEST STEP 4: Invoke the HAL API wifi_getFTMobilityDomainID() to retrieve the Mobility Domain ID Set operation";
                    print "EXPECTED RESULT 4: Should get the Mobility Domain ID using the HAL API successfully";

                    if expectedresult in actualresult :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 4: API was invoked successfully after SET operation; Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Check if proper Hex values are retrieved and convert them to integer value
                        print "\nTEST STEP 5 : Check if the FT Mobility Domain ID is retrieved as two Hex Values after Set operation";
                        print "EXPECTED RESULT 5 : FT Mobility Domain ID should be retrieved as two Hex Values";

                        hex_value0_final = details.split("ID[0] : ")[1].split(",")[0];
                        hex_value1_final = details.split("ID[1] : ")[1];
                        print "Mobility Domain ID[0] : %s" %hex_value0_final;
                        print "Mobility Domain ID[1] : %s" %hex_value1_final;

                        if "0x" in hex_value0 and "0x" in hex_value1:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 5: FT Mobility Domain ID is retrieved as two Hex values";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Covert to corresponding Integer values
                            final_FTMDID = HextoIntConversion(hex_value0_final, hex_value1_final);
                            print "\nTEST STEP 6 : Check if the SET value and GET value of FT Mobility Domain ID match";
                            print "EXPECTED RESULT 6 :Tthe SET value and GET value of FT Mobility Domain ID should match";
                            print "SET FT Mobility Domain ID : %d" %setValue;
                            print "GET FT Mobility Domain ID : %d" %final_FTMDID;

                            if setValue == final_FTMDID:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT 6: The SET value and GET value of FT Mobility Domain ID match";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                #Revert to initial FT Mobility Domain ID
                                tdkTestObj, actualresult, details = setMobilityDomain(tdkTestObj, apIndex, radioIndex, initial_FTMDID);

                                print "\nTEST STEP 7: Invoke the HAL API wifi_setFTMobilityDomainID() to revert to initial value";
                                print "EXPECTED RESULT 7: Should set the Mobility Domain ID to %d using the HAL API successfully" %initial_FTMDID;

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
                                print "ACTUAL RESULT 6: The SET value and GET value of FT Mobility Domain ID does not match";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 5: FT Mobility Domain ID is not retrieved as two Hex values";
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
                print "ACTUAL RESULT 2: FT Mobility Domain ID is not retrieved as two Hex values";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: API invocation failed; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
