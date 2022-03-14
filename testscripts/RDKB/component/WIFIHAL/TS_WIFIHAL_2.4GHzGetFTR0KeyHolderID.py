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
  <version>12</version>
  <name>TS_WIFIHAL_2.4GHzGetFTR0KeyHolderID</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetFTR0KeyHolderID</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getFTR0KeyHolderID() for 2.4G private AP to retrieve the Fast Transition R0 Key Holder ID and cross check with the R0 Key Holder ID value stored in nvram</synopsis>
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
    <test_case_id>TC_WIFIHAL_750</test_case_id>
    <test_objective>Invoke the HAL API wifi_getFTR0KeyHolderID() for 2.4G private AP to retrieve the Fast Transition R0 Key Holder ID and cross check with the R0 Key Holder ID value stored in nvram</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getFTR0KeyHolderID()</api_or_interface_used>
    <input_parameters>methodName : getFTR0KeyHolderID
apIndex : 2.4G private AP index</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getFTR0KeyHolderID() to get the FTR0 Key Holder ID for 2.4G private AP.
3. Convert the Hex values received to equivalent string representation.
4. Get the command to fetch the FTR0 Key Holder ID for 2.4G private AP from the platform property file.
5. Execute the command and get the FTR0 Key Holder ID from nvram in string format.
6. Compare the FTR0 Key Holder ID retrieved from HAL API and nvram and check if the values are same.
7. Unload the modules.</automation_approch>
    <expected_output>Invocation of the HAL API wifi_getFTR0KeyHolderID() for 2.4G private AP should be success and the FTR0 Key Holder ID retrieved should be the same as the value stored in nvram.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetFTR0KeyHolderID</test_script>
    <skipped>No</skipped>
    <release_version>M99</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetFTR0KeyHolderID');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetFTR0KeyHolderID');

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
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetFTR0KeyHolderID");
        tdkTestObj.addParameter("methodName","getFTR0KeyHolderID");
        tdkTestObj.addParameter("apIndex",idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Invoke the HAL API wifi_getFTR0KeyHolderID() to retrieve the FTR0 Key Holder ID for 2.4G private AP";
        print "EXPECTED RESULT 1: Should get the FTR0 Key Holder ID using the HAL API successfully";

        if expectedresult in actualresult and "FTR0 Key Holder ID Details -" in details:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: API was invoked successfully; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if proper Hex values are retrieved and convert them to corresponding string value
            print "\nTEST STEP 2 : Check if the FTR0 Key Holder ID is retrieved as one or more Hex Values";
            print "EXPECTED RESULT 2 : FTR0 Key Holder ID should be retrieved as one or more Hex Values";

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
                print "FTR0 Key Holder ID[%d] : %s" %(iteration, hex_values[iteration]);

            if num_hex_values >= 1:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: FTR0 Key Holder ID is retrieved as the Hex values : ", hex_values;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Covert the Hex values to corresponding unicode string
                unicode_string = [];
                unicode_key_id = "";
                for iteration in range(0, num_hex_values) :
                    hex_to_integer = int(hex_values[iteration], 0);
                    unicode_string.append(chr(hex_to_integer));
                    #Concatenate the string parts to get the full unicode string value
                    unicode_key_id = unicode_key_id + unicode_string[iteration];

                #Handle the condition when the Key Holder ID is 0x0, the unicode equivalent is '\x00'
                if unicode_key_id == '\x00':
                    unicode_key_id = "Null";
                print "The Equivalent unicode string value of the FTR0 Key Holder ID is : %s" %unicode_key_id;

                #Get the command to compare the FTR0 Key Holder ID from platform property file
                cmd= "sh %s/tdk_utility.sh parseConfigFile FTR0_KEY_HOLDER_ID_2G" %TDK_PATH;
                print cmd;
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                check_cmd = tdkTestObj.getResultDetails().replace("\\n", "");

                print "\nTEST STEP 3: Get the command to cross check the FTR0 Key Holder ID from property file";
                print "EXPECTED RESULT 3: Should get the FTR0 Key Holder ID check command from property file"

                if expectedresult in actualresult and check_cmd!= "":
                    print "ACTUAL RESULT 3: FTR0 Key Holder ID check command retrieved from property file";
                    print "TEST EXECUTION RESULT :SUCCESS";
                    tdkTestObj.setResultStatus("SUCCESS");

                    #Get the Key Holder ID using the command
                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    tdkTestObj.addParameter("command",check_cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().replace("\\n", "");

                    print "\nTEST STEP 4: Execute the command in the DUT to obtain the Key Holder ID";
                    print "EXPECTED RESULT 4: Should successfully execute the FTR0 Key Holder ID check command"

                    if expectedresult in actualresult :
                        #If nvram value received is not Null
                        if "id=" in details and details.split("id=")[1] != "":
                            fbt_key_id = details.split("id=")[1].strip();
                        #Null value representation in unicode - if no value is received from nvram, consider the value Null
                        else :
                            fbt_key_id = "Null";

                        print "ACTUAL RESULT 4: FTR0 Key Holder ID : ", fbt_key_id ;
                        print "TEST EXECUTION RESULT :SUCCESS";
                        tdkTestObj.setResultStatus("SUCCESS");

                        #check if the FTR0 Key Holder ID value from the HAL API is same as the value retrieved using the command
                        print "\nTEST STEP 5 : Validate the FTR0 Key Holder ID value retrieved using the HAL API";
                        print "EXPECTED RESULT 5 : The FTR0 Key Holder ID value from the HAL API should be the same as the value retrieved using the command";

                        print "FTR0 Key Holder ID from HAL API : %s" %unicode_key_id;
                        print "Expected FTR0 Key Holder ID : %s" %fbt_key_id;

                        if unicode_key_id == fbt_key_id:
                            print "ACTUAL RESULT 5: The values are the same";
                            print "TEST EXECUTION RESULT :SUCCESS";
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "ACTUAL RESULT 5: The values are not the same";
                            print "TEST EXECUTION RESULT :FAILURE";
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "ACTUAL RESULT 4: FTR0 Key Holder ID :", details ;
                        print "TEST EXECUTION RESULT :FAILURE";
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "ACTUAL RESULT 3: FTR0 Key Holder ID check command from property file :", check_cmd ;
                    print "TEST EXECUTION RESULT :FAILURE";
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: FTR0 Key Holder ID is not retrieved as one or more Hex values";
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
