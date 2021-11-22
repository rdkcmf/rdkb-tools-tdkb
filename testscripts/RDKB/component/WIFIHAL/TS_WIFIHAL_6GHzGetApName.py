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
  <name>TS_WIFIHAL_6GHzGetApName</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getApName to get the the 6GHz Private Access Point name and check if it is the same as the value in platform property file.</synopsis>
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
    <test_case_id>TC_WIFIHAL_665</test_case_id>
    <test_objective>Invoke the HAL API wifi_getApName to get the the 6GHz Private Access Point name and check if it is the same as the value in platform property file.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApName()</api_or_interface_used>
    <input_parameters>methodname : getApName
apIndex : fetched from platform property file</input_parameters>
    <automation_approch>1. Load the modules
2. Invoke the HAL API wifi_getApName() and retrieve the Access Point Name for 6Ghz private access point.
3. Retrieve the expected access point name from the platform property file
4. Compare both the values and check if they are same.
5. Unload the modules</automation_approch>
    <expected_output>The HAL API wifi_getApName() should retrieve the 6Ghz private access point index name successfully.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetApName</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApName');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetApName');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);
    if apIndex == -1:
        print "Failed to get the Access Point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else :
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        cmd = "sh %s/tdk_utility.sh parseConfigFile AP_IF_NAME_6G" %TDK_PATH;
        print "query:%s" %cmd
        tdkTestObj.addParameter("command", cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        accesspointname= tdkTestObj.getResultDetails().strip().replace("\\n", "");

        print "\nTEST STEP 2: Get the 6GHZ Private Access Point name from properties file";
        print "EXPECTED RESULT 2 : The 6GHZ Private Access Point name should be fetched successfully"

        if expectedresult in actualresult and accesspointname != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: AP_IF_NAME_6G : %s" %accesspointname;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Get the Access Point Name using the API wifi_getApName
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
            tdkTestObj.addParameter("methodName","getApName");
            tdkTestObj.addParameter("radioIndex",apIndex);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP 3 : Invoke the HAL API wifi_getApName and get the 6GHz Private Access Point Name";
            print "EXPECTED RESULT 3 : The HAL API wifi_getApName should be invoked successfully";

            if expectedresult in actualresult :
                apName = details.split(":")[1].strip();
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: wifi_getApName invoked successfully; 6GHZ Private Access Point Name : %s" %apName;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                print "\nTEST STEP 4 : Check if the 6GHZ Private ApName retrieved from HAL API matches with the value from platform property file";
                print "EXPECTED RESULT 4 : The values should match";
                print "From platform property file apName : %s" %accesspointname;
                print "From HAL API apName : %s" %apName;

                if accesspointname == apName:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: The 6GHZ Private ApName retrieved from HAL API matches with the value from platform property file";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: The 6GHZ Private ApName retrieved from HAL API does not match with the value from platform property file";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: wifi_getApName not invoked successfully; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: AP_IF_NAME_6G : %s" %accesspointname;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
