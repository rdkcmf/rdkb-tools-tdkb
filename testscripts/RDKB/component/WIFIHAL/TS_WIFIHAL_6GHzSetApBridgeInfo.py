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
  <name>TS_WIFIHAL_6GHzSetApBridgeInfo</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetApBridgeInfo</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set the 6G private access point bridge info using the HAL API wifi_setApBridgeInfo() and cross check if the values are reflected in the get API wifi_getApBridgeInfo().</synopsis>
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
    <test_case_id>TC_WIFIHAL_685</test_case_id>
    <test_objective>Set the 6G private access point bridge info using the HAL API wifi_setApBridgeInfo() and cross check if the values are reflected in the get API wifi_getApBridgeInfo().</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApBridgeInfo()
wifi_setApBridgeInfo()</api_or_interface_used>
    <input_parameters>methodname : getApBridgeInfo
methodname : setApBridgeInfo
radioIndex : 6G private AP index fetched from platform property file
bridgeName : newBranch2
IP : 1.1.1.1
subnet : 255.255.255.1</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial 6G private AP bridge info using the HAL API wifi_getApBridgeInfo() and store the values.
3. Set the new bridge info using the HAL API wifi_setApBridgeInfo().
4. Cross check the SET with GET
5. Unload the modules</automation_approch>
    <expected_output>Should be able to set the 6G private access point bridge info using the HAL API wifi_setApBridgeInfo() and the values should be reflected in the get API wifi_getApBridgeInfo().</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetApBridgeInfo</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks/>
  </test_cases>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetApBridgeInfo');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetApBridgeInfo');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

    if apIndex == -1:
        print "Failed to get the Access Point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Prmitive test case which associated to this Script
        tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetApBridgeInfo');
        tdkTestObj.addParameter("methodName","getApBridgeInfo");
        tdkTestObj.addParameter("radioIndex",apIndex);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 2: Invoke the API wifi_ApBridgeInfo() for 6GHz";
        print "EXPECTED RESULT 2: Should successfully invoke the API wifi_ApBridgeInfo() for 6GHz";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: API invocation success; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            initial_bridgeName = details.split(":")[1].split(",")[0].split("=")[1];
            initial_ip = details.split(":")[1].split(",")[1].split("=")[1];
            initial_subnet = details.split(":")[1].split(",")[2].split("=")[1];
            print "Initial Bridgename : %s"%initial_bridgeName;
            print "Initial IP : %s"%initial_ip;
            print "Initial Subnet : %s"%initial_subnet;

            #Set new parameters to AP Bridge
            new_bridge = "newBranch2";
            new_ip = "1.1.1.1";
            new_subnet = "255.255.255.1";
            tdkTestObj.addParameter("methodName","setApBridgeInfo");
            tdkTestObj.addParameter("radioIndex",apIndex);
            tdkTestObj.addParameter("bridgeName",new_bridge);
            tdkTestObj.addParameter("IP",new_ip);
            tdkTestObj.addParameter("subnet",new_subnet);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP 3: Set the new bridge deatails using wifi_setApBridgeInfo for 6GHz";
            print "EXPECTED RESULT 3: Should set the new bridge deatails using wifi_setApBridgeInfo for 6GHz successfully";

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: API invocation success; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Get the bridge info after the set
                tdkTestObj.addParameter("methodName","getApBridgeInfo");
                tdkTestObj.addParameter("radioIndex",apIndex);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP 4: Get the previously set ApBridgeInfo for 5GHz";
                print "EXPECTED RESULT 4: Should get the previously set ApBridgeInfo for 6GHz";

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: API invocation success; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Compare the bridge info get with the set values
                    final_bridge = details.split(":")[1].split(",")[0].split("=")[1];
                    final_ip = details.split(":")[1].split(",")[1].split("=")[1];
                    final_subnet = details.split(":")[1].split(",")[2].split("=")[1];
                    print "Set Bridgename : %s, Get Bridgename : %s"%(new_bridge, final_bridge);
                    print "Set IP : %s, Get IP : %s"%(new_ip, final_ip);
                    print "Set Subnet : %s, Get Subnet : %s"%(new_subnet, final_subnet);

                    print "\nTEST STEP 5: Cross verify if the SET is reflected in the GET";
                    print "EXPECTED RESULT 5: The values SET should be reflected in the GET";

                    if new_bridge == final_bridge and new_ip == final_ip and new_subnet == final_subnet:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 5: All SET values match with the GET values";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 5: All SET values does NOT match with the GET values";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: API invocation failed; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert the ApBridgeInfo to intiial values
                tdkTestObj.addParameter("methodName","setApBridgeInfo");
                tdkTestObj.addParameter("radioIndex",apIndex);
                tdkTestObj.addParameter("bridgeName",initial_bridgeName);
                tdkTestObj.addParameter("IP",initial_ip);
                tdkTestObj.addParameter("subnet",initial_subnet);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP 6 : Revert to initial state";
                print "EXPECTED RESULT 6 : Revert operation should be success";

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 6 : Successfully reverted to initial values; Details : %s" %details;
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 6 : Revert operation failed; Details : %s" %details;
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: API invocation failed; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: API invocation failed; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

