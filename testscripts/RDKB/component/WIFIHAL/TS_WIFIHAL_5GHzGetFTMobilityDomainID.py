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
  <version>6</version>
  <name>TS_WIFIHAL_5GHzGetFTMobilityDomainID</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetFTMobilityDomainID</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getFTMobilityDomainID() for 5G private AP to retrieve the Fast Transition Mobility Domain ID and cross check with the fbt_mdid value stored in nvram.</synopsis>
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
    <test_case_id>TC_WIFIHAL_724</test_case_id>
    <test_objective>Invoke the HAL API wifi_getFTMobilityDomainID() for 5G private AP to retrieve the Fast Transition Mobility Domain ID and cross check with the fbt_mdid value stored in nvram.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getFTMobilityDomainID()</api_or_interface_used>
    <input_parameters>methodName : getFTMobilityDomainID
apIndex : 5G private AP index</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getFTMobilityDomainID() for 5G Private AP and check if the API invocation is success and the FT Mobility Domain ID retrieved is a pair of Hexadecimal values.
3. Combine the Hex value and obtain the equivalent decimal value for FT Mobility Domain ID.
4. From Platform properties file retrieve the command for checking the fbt_mdid value in nvram.
5. Execute the command and retrieve the FT Mobility Domain ID decimal value.
6. Compare the GET API value with the nvram value to validate the output of the GET API.
7. Unload modules.</automation_approch>
    <expected_output>The HAL API wifi_getFTMobilityDomainID() for 5G private AP to retrieve the Fast Transition Mobility Domain ID should be invoked successfully and should match with the fbt_mdid value stored in nvram.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetFTMobilityDomainID</test_script>
    <skipped>No</skipped>
    <release_version>M98</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetFTMobilityDomainID');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetFTMobilityDomainID');

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
        tdkTestObj.addParameter("methodName","getFTMobilityDomainID");
        tdkTestObj.addParameter("apIndex",idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Invoke the HAL API wifi_getFTMobilityDomainID() to retrieve the Mobility Domain ID for 5G private AP";
        print "EXPECTED RESULT 1: Should get the Mobility Domain ID using the HAL API successfully";

        if expectedresult in actualresult and details != "":
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

                #Get the command to compare the FT Mobility Domain from platform property file
                cmd= "sh %s/tdk_utility.sh parseConfigFile FT_MOBILITY_DOMAIN_ID_5G" %TDK_PATH;
                print cmd;
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                check_cmd = tdkTestObj.getResultDetails().replace("\\n", "");

                print "\nTEST STEP 3: Get the command to cross check the FT Mobility Domain ID from property file";
                print "EXPECTED RESULT 3: Should get the FT Mobility Domain ID check command from property file"

                if expectedresult in actualresult and check_cmd!= "":
                    print "ACTUAL RESULT 3: FT Mobility Domain ID check command from property file :", check_cmd ;
                    print "TEST EXECUTION RESULT :SUCCESS";
                    tdkTestObj.setResultStatus("SUCCESS");

                    #Get the Mobility Domain ID using the command
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    tdkTestObj.addParameter("command",check_cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().replace("\\n", "");

                    print "\nTEST STEP 4: Execute the command in the DUT to obtian the Mobility Domain ID";
                    print "EXPECTED RESULT 4: Should successfully execute the FT Mobility Domain ID check command"

                    if expectedresult in actualresult :
                        print "ACTUAL RESULT 4: FT Mobility Domain ID :", details ;
                        print "TEST EXECUTION RESULT :SUCCESS";
                        tdkTestObj.setResultStatus("SUCCESS");

                        #check if the FT Mobility Domain ID value from the HAL API is same as the value retrieved using the command
                        if "mdid=" in details and details.split("mdid=")[1] != "":
                            fbt_mdid_value = details.split("mdid=")[1];
                        #if no value is received from nvram, consider the value as 0
                        else :
                            fbt_mdid_value = "0";

                        if fbt_mdid_value.isdigit() :
                            fbt_mdid_value = int(fbt_mdid_value);
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "FT Mobility Domain ID from HAL API : %d" %mobility_id;
                            print "Expected FT Mobility Domain ID : %d" %fbt_mdid_value;

                            if fbt_mdid_value == mobility_id:
                                print "ACTUAL RESULT 5: The values are the same";
                                print "TEST EXECUTION RESULT :SUCCESS";
                                tdkTestObj.setResultStatus("SUCCESS");
                            else:
                                print "ACTUAL RESULT 5: The values are not the same";
                                print "TEST EXECUTION RESULT :FAILURE";
                                tdkTestObj.setResultStatus("FAILURE");
                        else :
                            tdkTestObj.setResultStatus("FAILURE");
                            print "FT Mobility Domain ID is not of the expected type";

                    else:
                        print "ACTUAL RESULT 4: FT Mobility Domain ID :", details ;
                        print "TEST EXECUTION RESULT :FAILURE";
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "ACTUAL RESULT 3: FT Mobility Domain ID check command from property file :", check_cmd ;
                    print "TEST EXECUTION RESULT :FAILURE";
                    tdkTestObj.setResultStatus("FAILURE");
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
