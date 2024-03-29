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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_6GHzSetRadio11nGreenfieldEnabled</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check 11nGreenfield enable status of Radio 6GHz using wifi_getRadio11nGreenfieldEnable HAL API.</synopsis>
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
    <test_case_id>TC_WIFIHAL_661</test_case_id>
    <test_objective>To check 11nGreenfield enable status of Radio 6GHz using wifi_getRadio11nGreenfieldEnable HAL API</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadio11nGreenfieldEnable()
wifi_getRadio11nGreenfieldSupported()
wifi_setRadio11nGreenfieldEnable()</api_or_interface_used>
    <input_parameters>methodName   :   getRadio11nGreenfieldSupported
methodName   :   getRadio11nGreenfieldEnable
methodName   :   setRadio11nGreenfieldEnable</input_parameters>
    <automation_approch>1.Load the module
2.Check whether Radio 11nGreenfield is
 Supported   using wifi_getRadio11nGreenfieldSupported
3.If supported get its current status using wifi_getRadio11nGreenfieldEnable
4.Toggle the value using wifi_setRadio11nGreenfieldEnable
5.Verify set with subsequent get
6.Revert the set value
7.Unload the module</automation_approch>
    <expected_output>if  Radio 11nGreenfield is Supported  get and set operation for Radio 11nGreenfield should be sucessful</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetRadio11nGreenfieldEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
radio = "6G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetRadio11nGreenfieldEnabled');
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
	    expectedresult="SUCCESS";
	    radioIndex = idx
	    getMethod = "getRadio11nGreenfieldSupported"
	    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
	    if expectedresult in actualresult :
		tdkTestObj.setResultStatus("SUCCESS");
		enable = details.split(":")[1].strip()
		if "Enabled" in enable:
		    expectedresult="SUCCESS";
		    radioIndex = idx
		    getMethod = "getRadio11nGreenfieldEnable"
		    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
		    #Getting the default enable mode
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
		    if expectedresult in actualresult :
			tdkTestObj.setResultStatus("SUCCESS");
			enable = details.split(":")[1].strip()
			if "Enabled" in enable:
			    print "11nGreenfield is Enabled for Radio 5GHz"
			    oldEnable = 1
			    newEnable = 0
			else:
			    print "11nGreenfield is Disabled for Radio 5GHz "
			    oldEnable = 0
			    newEnable = 1
			setMethod = "setRadio11nGreenfieldEnable"
			#Toggle the enable status using set
			tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, newEnable, setMethod)
			if expectedresult in actualresult :
			    print "Enable state toggled using set"
			    # Get the New enable status
			    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
			    if expectedresult in actualresult and enable not in details.split(":")[1].strip():
				print "getRadio11nGreenfieldEnable Success, verified along with setRadio11nGreenfieldEnable() api"
				#Revert back to original Enable status
				tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, oldEnable, setMethod)
				if expectedresult in actualresult :
				    print "Enable status reverted back";
				else:
				    print "Couldn't revert enable status"
				    tdkTestObj.setResultStatus("FAILURE");
			    else:
				print "getRadio11nGreenfieldEnable() failed after set function"
				tdkTestObj.setResultStatus("FAILURE");
			else:
			    print "setRadio11nGreenfieldEnable() failed"
			    tdkTestObj.setResultStatus("FAILURE");
		    else:
			print "getRadio11nGreenfieldEnable() failed"
			tdkTestObj.setResultStatus("FAILURE");
		else:
		    print "Radio11nGreenfield is not supported"
		    tdkTestObj.setResultStatus("SUCCESS");
	    else:
		print "getRadio11nGreenfieldSupported() call failed"
		tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
