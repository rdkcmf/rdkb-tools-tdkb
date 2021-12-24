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
  <name>TS_WIFIHAL_6GHzSetApAuthMode_Open</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>5</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the authorization mode as open for 6GHz and check if it is success.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_698</test_case_id>
    <test_objective>To set the authorization mode as open for 6GHz and check if it is success</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApAuthMode()</api_or_interface_used>
    <input_parameters>methodName : setApAuthMode
ApIndex : 6gindex
param : 2</input_parameters>
    <automation_approch>1. Load wifihal module
2. From Platform properities file, obtain the value for AP_AUTH_MODE_OPEN
3. Using WIFIHAL_GetOrSetParamIntValue invoke wifi_setApAuthMode()
4. Depending upon the output, return SUCCESS or FAILURE
5. Unload wifihal module</automation_approch>
    <expected_output>wifi_setApAuthMode() should return SUCCESS</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetApAuthMode_Open</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks>None</remarks>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_SetApAuthMode_Open');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_SetApAuthMode_Open');
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper() and sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    #Getting AP_AUTH_MODE_OPEN value from tdk_platform_properties"
    cmd= "sh %s/tdk_utility.sh parseConfigFile AP_AUTH_MODE_OPEN" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    setMode = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if expectedresult in actualresult and setMode!= "":
        print "TEST STEP : Should  get AP_AUTH_MODE_OPEN  from property file"
        print "ACTUAL RESULT :AP_AUTH_MODE_OPEN from property file :",setMode ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] :SUCCESS";

        expectedresult = "SUCCESS";
        #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
        tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);
        if apIndex != -1:
            primitive = 'WIFIHAL_GetOrSetParamIntValue'
            expectedresult="SUCCESS";
            setMethod = "setApAuthMode"
            setMode = int(setMode)
            #Calling the method to execute wifi_setApAuthMode()
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)
            if expectedresult in actualresult:
                print "TEST STEP : Set the authorization mode as Open for apIndex %s"%apIndex
                print "EXPECTED RESULT : Should successfully set the authorization mode as Open"
                print "ACTUAL RESULT : Successfully sets the authorization mode as Open"
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "TEST STEP : Set the authorization mode as Open for apIndex %s"%apIndex
                print "EXPECTED RESULT : Should successfully set the authorization mode as Open"
                print "ACTUAL RESULT : Failed to set the authorization mode as Open"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "Failed to get the Access Point index";
            tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Should  get AP_AUTH_MODE_OPEN  from property file"
        print "ACTUAL RESULT :AP_AUTH_MODE_OPEN from property file :",setMode ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] :FAILURE";
    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
