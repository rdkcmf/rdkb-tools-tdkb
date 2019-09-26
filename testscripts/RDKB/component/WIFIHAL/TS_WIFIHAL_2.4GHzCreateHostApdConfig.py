##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzCreateHostApdConfig</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Test to create /nvram/etc/wpa2/WSC_ath0.conf or /tmp/secath0 using the api wifi_createHostApdConfig () for the radio 2.4GHz</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_290</test_case_id>
    <test_objective>Test to create /nvram/etc/wpa2/WSC_ath0.conf or /tmp/secath0 using the api wifi_createHostApdConfig () for the radio 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_createHostApdConfig()</api_or_interface_used>
    <input_parameters>methodName : createHostApdConfig
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Load sysutil module
3. Remove the existing WSC_ath0.conf and /tmp/secath0 files present inside the box.
4. Using WIFIHAL_GetOrSetParamBoolValue invoke wifi_createHostApdConfig ()
5. Check whether the files are created.
6. Revert back the changes to initial
7. Unload sysutil module
8. Unload wifihal module</automation_approch>
    <except_output>wifi_createHostApdConfig() api should create host apd configuration files</except_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzCreateHostApdConfig</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzCreateHostApdConfig');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzCreateHostApdConfig');
def createHostApdConfig():
    print "Entered to the Function"
    #calling the wifi api wifi_createHostApdConfig to create /tmp/secath0
    tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamBoolValue');
    tdkTestObj.addParameter("radioIndex", 0);
    tdkTestObj.addParameter("methodName","createHostApdConfig");
    tdkTestObj.addParameter("param", 0);
    expectedresult="SUCCESS";
    
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
     
    if expectedresult in actualresult :
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 2: Call the wifi_createHostApdConfig api to create hostapd config file /tmp/secath0 file for 2.4GHz";
        print "EXPECTED RESULT 2: Should create the file for the radio 2.4GHz";
        print "ACTUAL RESULT 2: Created the files and execution returns SUCCESS";
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #calling the wifi api wifi_createHostApdConfig to create hostapd config file /nvram/etc/wpa2/WSC_ath0.conf
        tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamBoolValue');
        tdkTestObj.addParameter("radioIndex", 0);
        tdkTestObj.addParameter("methodName","createHostApdConfig");
        tdkTestObj.addParameter("param", 1);
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Call the wifi_createHostApdConfig api to create hostapd config file /nvram/etc/wpa2/WSC_ath0.conf file for 2.4GHz";
            print "EXPECTED RESULT 1: Should create the file for the radio 2.4GHz";
            print "ACTUAL RESULT 1: Created the files and execution returns SUCCESS";
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Calling the Function checkHostApdConfig to check whether the file creation
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            query = "sh %s/tdk_platform_utility.sh checkHostApdConfig | tr \"\n\" \" \"" %TDK_PATH
            tdkTestObj.addParameter("command", query)
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Get the created files for the radio 2.4GHz";
                print "EXPECTED RESULT 4: Should get the files created for the radio 2.4GHz";
                print "ACTUAL RESULT 4: Operation returned SUCCESS";
                print "Created Files are:",details;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Revert back the changes
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                query="sh %s/tdk_platform_utility.sh removeHostApdConfig" %TDK_PATH
                tdkTestObj.addParameter("command", query);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and "Invalid Argument passed" not in details:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Remove the created hostapd config files for the radio 2.4GHz";
                    print "EXPECTED RESULT 5: Should remove the hostapd config files for the radio 2.4GHz";
                    print "ACTUAL RESULT 5: Successfully removed the hostapd config files";
                    print "details is :",details
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Remove the created hostapd config files for the radio 2.4GHz";
                    print "EXPECTED RESULT 5: Should remove the hostapd config files for the radio 2.4GHz";
                    print "ACTUAL RESULT 5: Failed to remove the files and execution returns FAILURE";
                    print "details is :",details
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Get the created files for the radio 2.4GHz";
                print "EXPECTED RESULT 4: Should get the files created for the radio 2.4GHz";
                print "ACTUAL RESULT 4: Failed to get the result",actualresult;
                print "Details is :",details;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 3: Call the function wifi_createHostApdConfig to create hostapd config file /nvram/etc/wpa2/WSC_ath0.conf for 2.4GHz";
            print "EXPECTED RESULT 3: Should create the file for the radio 2.4GHz";
            print "ACTUAL RESULT 3: Failed to create the file and api returns failure";
            print "Details is :",details;
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 2: Call the function wifi_createHostApdConfig to create hostapd config file /tmp/secath0 for 2.4GHz";
        print "EXPECTED RESULT 2: Should create the file for the radio 2.4GHz";
        print "ACTUAL RESULT 2: Failed to create the file and api returns failure";
        print "[TEST EXECUTION RESULT] : FAILURE";
        
#Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult();
sysloadmodulestatus = sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus;
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Removing the existing files 
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    query="sh %s/tdk_platform_utility.sh removeHostApdConfig" %TDK_PATH
    tdkTestObj.addParameter("command", query);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and "Invalid Argument passed" not in details:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Remove the existing hostapd config files for the radio 2.4GHz";
        print "EXPECTED RESULT 1: Should remove the file for the radio 2.4GHz";
        print "ACTUAL RESULT 1: Successfully removed the hostapd config files";
        print "details is :",details
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Calling the function to execute the functionality
        createHostApdConfig()
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Remove the existing hostapd config files for the radio 2.4GHz";
        print "EXPECTED RESULT 1: Should remove the files for the radio 2.4GHz";
        print "ACTUAL RESULT 1: Failed to remove  the existing files and execution returns FAILURE";
        print "details is :",details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    sysobj.unloadModule("sysutil");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

