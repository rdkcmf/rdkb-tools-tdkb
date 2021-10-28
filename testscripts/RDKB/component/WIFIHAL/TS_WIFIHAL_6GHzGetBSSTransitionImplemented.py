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
  <name>TS_WIFIHAL_6GHzGetBSSTransitionImplemented</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check whether the BSSTransition is implemented using the HAL API wifi_getBSSTransitionImplemented() for 6GHz radio.</synopsis>
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
    <test_case_id>TC_WIFIHAL_650</test_case_id>
    <test_objective>To check whether the BSSTransition is implemented using the HAL API wifi_getBSSTransitionImplemented() for 6GHz radio.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getBSSTransitionImplemented()</api_or_interface_used>
    <input_parameters>method : getBSSTransitionImplemented
apIndex : fetched from platform property file</input_parameters>
    <automation_approch>1.Load the module.
2. Get the 6GHz access point index from platform property file.
3.Get the getBSSTransitionImplemented using   wifi_getBSSTransitionImplemented API.
4. Get the  IS_BTM_CAPABLE value from platform properties file.
5.Compare the value from api and from the value received from properties file.
6.Return SUCCESS for non empty value,else FAILURE.
7.Unload module.</automation_approch>
    <expected_output>The BSS Transition Implemented value should be successfully retrieved using the HAL API wifi_getBSSTransitionImplemented() and it should match with the value in the platform property file.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetBSSTransitionImplemented</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
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
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetBSSTransitionImplemented');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetBSSTransitionImplemented');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

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
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        #Getting  IS_BTM_CAPABLE value from tdk_platform_properties"
        cmd= "sh %s/tdk_utility.sh parseConfigFile BTM_CAPABILITY" %TDK_PATH;
        print cmd;
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        platformValue = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        print "\nTEST STEP 2: Get the BSS capability from property file"
        print "EXPECTED RESULT 2: Should get the BSS capability from property file"
        print"IS_BTM_CAPABLE:",platformValue

        if expectedresult in actualresult and platformValue!= "":
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2:BSS capability from property file :",platformValue ;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] :SUCCESS";

            tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamBoolValue');
            tdkTestObj.addParameter("methodName","getBSSTransitionImplemented");
            tdkTestObj.addParameter("radioIndex", apIndex);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            details = details.split(':')[1].strip();
            print "Details : ",details

            print "\nTEST STEP 3:check whether wifi_getBSSTransitionImplemented() returns the BSS capability of device"
            print "EXPECTED RESULT 3: Should check wether the BSSTransition Implemented "

            if expectedresult in actualresult and platformValue == details:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: BSSTransition Implemented in the device"
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3:difference in api return and property file entry"
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2:BSS capability from property file :",platformValue ;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] :FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

