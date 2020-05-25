##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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
  <name>TS_WIFIHAL_5GHzGetRadioIfName</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the Radio interface name for 5GHz and check whether it is "wifi1"</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_18</test_case_id>
    <test_objective>To get the Radio interface name for 5GHz and check whether it is "wifi1"</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioIfName()</api_or_interface_used>
    <input_parameters>methodName: getRadioIfName
radioIndex:1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke "WIFIHAL_GetOrSetParamStringValue" to get the interface name for 5GHz
3.Check if the value returned is valid or not
4. If not, return failure
5.Unload wifihal module</automation_approch>
    <except_output>The interface name should be wifi1 for 5GHz</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetRadioIfName</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from wifiUtility import *;
radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioIfName');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetRadioIfName');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else: 

	    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
	    expectedresult="SUCCESS";
	    print "Get the radio interface name for 5Ghz"
	    getRadioIf = "sh %s/tdk_utility.sh parseConfigFile RADIO_IF_5G" %TDK_PATH;
	    tdkTestObj.addParameter("command", getRadioIf);
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    radioIf= tdkTestObj.getResultDetails().strip();
	    radioIf = radioIf.replace("\\n", "");
	    if radioIf:
		#Script to load the configuration file of the component
		tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
		#Giving the method name to invoke the api wifi_getRadioIfName()
		tdkTestObj.addParameter("methodName","getRadioIfName")
		#Radio index is 0 for 2.4GHz and 1 for 5GHz
		tdkTestObj.addParameter("radioIndex",idx);
		tdkTestObj.executeTestCase(expectedresult);
		actualresult = tdkTestObj.getResult();
		details = tdkTestObj.getResultDetails();
		Ifvalue = details.split(":")[1]
		if expectedresult in actualresult and Ifvalue == radioIf:
		   #Set the result status of execution
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP 1: Get the Radio interface name";
		    print "EXPECTED RESULT 1: Should get the interface name ";
		    print "ACTUAL RESULT 1: %s" %details;
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] : SUCCESS";
		else:
		    #Set the result status of execution
		    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP 1: Get the Radio interface name";
		    print "EXPECTED RESULT 1: Should get the interface name ";
		    print "ACTUAL RESULT 1: %s" %details;
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "FAILURE: Failed to get the value of RadioIf from /etc/tdk_platform.properties file"
    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
