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
  <name>TS_WIFIHAL_6GHzGetRadioBeaconPeriod</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the Beacon Period value (Time interval between transmitting beacons) for 6GHz radio using wifi_getRadioBeaconPeriod HAL API and validate the same.</synopsis>
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
    <test_case_id>TC_WIFIHAL_607</test_case_id>
    <test_objective>To get the Beacon Period value (Time interval between transmitting beacons) for 6GHz radio using wifi_getRadioBeaconPeriod HAL API and validate the same</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioBeaconPeriod()</api_or_interface_used>
    <input_parameters>methodName   :   getRadioBeaconPeriod</input_parameters>
    <automation_approch>1.Load the wifihal module
2.Get the expected beacon period configured in platform property file
3.Get the Beacon period using wifi_getRadioBeaconPeriod
4.Check if the received and configured value are equal and set the result status accordingly
5.Unload the module</automation_approch>
    <expected_output>value received from wifi_getRadioBeaconPeriod  must be equal to configured expected value</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetRadioBeaconPeriod</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
radio = "6G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetRadioBeaconPeriod');
obj1.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetRadioBeaconPeriod');
loadmodulestatus =obj.getLoadModuleResult();
sysutilmodulestatus =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[SYSUTIL  LOAD STATUS]  :  %s" %sysutilmodulestatus
if "SUCCESS" in (loadmodulestatus.upper() and  sysutilmodulestatus.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
	radioIndex = idx
	getMethod = "getRadioBeaconPeriod"
	primitive = 'WIFIHAL_GetOrSetParamUIntValue'
        #Get the default value from properties file
    	tdkTestObj1 = obj1.createTestStep('ExecuteCmd');
    	cmd = "sh %s/tdk_utility.sh parseConfigFile DEFAULT_BEACON_PERIOD" %TDK_PATH;
    	print cmd;
    	expectedresult="SUCCESS";
        tdkTestObj1.addParameter("command", cmd);
        tdkTestObj1.executeTestCase(expectedresult);
        actualresult = tdkTestObj1.getResult();
    	details = ""
    	details = tdkTestObj1.getResultDetails().strip();
    	defaultValue = ""
        defaultValue = details.replace("\\n", "");
    	print "Default Beacon Period:",defaultValue
    	if defaultValue != "" and ( expectedresult in  actualresult):
       	    tdkTestObj1.setResultStatus("SUCCESS");
       	    print "TEST STEP 1: Get the default beacon period from tdk_platfrom properties file";
            print "EXPECTED RESULT 1: Should Get the default beacon period form platform properties file";
            print "ACTUAL RESULT 1:The default beacon period from tdk_platform properties file is : %s" % defaultValue;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
            expectedresult="SUCCESS";

            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
            if expectedresult in actualresult:
            	print "getRadioBeaconPeriod function successful: %s"%details
          	tdkTestObj.setResultStatus("SUCCESS");
          	beaconPeriodValue = details.split(":")[1].strip();
                if beaconPeriodValue.isdigit() :
             	    if int(beaconPeriodValue) == int(defaultValue):
                       tdkTestObj.setResultStatus("SUCCESS");
             	       print "TEST STEP 2: Compare the default value with received beacon period";
             	       print "EXPECTED RESULT 2:Default value and  Received beacon period should be equal";
             	       print "ACTUAL RESULT 2: Default value and  Received beacon period are equal: %s"%beaconPeriodValue;
                       print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 2: Compare the default value with received beacon period";
              	        print "EXPECTED RESULT 2:Default value and  Received beacon period should be equal";
              	        print "ACTUAL RESULT 2: Default value and  Received beacon period are not equal:  %s"%beaconPeriodValue;
              	        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                     tdkTestObj.setResultStatus("FAILURE");
                     print "a non-digit value is received";
            else:
                print "getRadioBeaconPeriod function failed";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            tdkTestObj1.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the default beacon period from tdk_platfrom properties file";
            print "EXPECTED RESULT 1: Should Get the default beacon period form platform properties file";
            print "ACTUAL RESULT 1: Failed to get the default beacon period : %s" % defaultValue;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("wifihal");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load wifi module/ sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
