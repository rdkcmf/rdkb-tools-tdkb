##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <version>9</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzSetBandSteeringRSSIThreshold</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>5</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set and get the BandSteeringRSSIThreshold for 2.4GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_147</test_case_id>
    <test_objective>To set and get the BandSteering RSSIThreshold for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getBandSteeringCapability()
wifi_getBandSteeringRSSIThreshold()
wifi_setBandSteeringRSSIThreshold()</api_or_interface_used>
    <input_parameters>methodName : getBandSteeringCapability
methodName : getBandSteeringRSSIThreshold
methodName : setBandSteeringRSSIThreshold
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamBoolValue invoke wifi_getBandSteeringCapability() to see if the BandSteering Capability is available or not. If available proceed to next step, else return SUCCESS and exit.
3. Using  WIFIHAL_GetOrSetParamStringValue invoke wifi_getBandSteeringRSSIThreshold()
4. Using WIFIHAL_GetOrSetParamStringValue
 invoke wifi_setBandSteeringRSSIThreshold  and set a valid value
5. Invoke wifi_getBandSteeringRSSIThreshold() to get the previously set value.
6. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
7. Revert the RSSIThreshold back to initial value
8. Unload wifihal module</automation_approch>
    <expected_output>Set and get values of RSSIThreshold should be the same</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetBandSteeringRSSIThreshold</test_script>
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
import random;
from tdkbVariables import *;
radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetBandSteeringRSSIThreshold');
obj1.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetBandSteeringRSSIThreshold');

loadmodulestatus =obj.getLoadModuleResult();
sysyutilmodulestatus =obj1.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %sysyutilmodulestatus

if "SUCCESS" in (loadmodulestatus.upper() and  sysyutilmodulestatus.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");


    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:

	    expectedresult="SUCCESS";
	    getMethod = "getBandSteeringCapability"
	    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
	    radioIndex = idx;
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

	    if expectedresult in actualresult:
		enable = details.split(":")[1].strip()
		tdkTestObj.setResultStatus("SUCCESS");
		if "Enabled" in enable:

		    getMethod = "getBandSteeringRSSIThreshold"
		    primitive = 'WIFIHAL_GetOrSetParamIntValue'
		    radioIndex = idx;
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
		    initGetValue = details.split(":")[1].strip()

		    if expectedresult in actualresult:
			tdkTestObj.setResultStatus("SUCCESS");
			setMethod = "setBandSteeringRSSIThreshold"
			radioIndex = idx;
			primitive = 'WIFIHAL_GetOrSetParamIntValue'

                        #Get the Range of the value to set
                        tdkTestObj1 = obj1.createTestStep('ExecuteCmd');
                        cmd = "sh %s/tdk_utility.sh parseConfigFile RSSI_RANGE" %TDK_PATH;
                        print cmd;
                        expectedresult="SUCCESS";
                        tdkTestObj1.addParameter("command", cmd);
                        tdkTestObj1.executeTestCase(expectedresult);
                        actualresult = tdkTestObj1.getResult();
                        details = ""
                        details = tdkTestObj1.getResultDetails().strip();
                        Range = ""
                        Range = details.replace("\\n", "");
                        if Range != ""  and (expectedresult in actualresult):
			   Range = Range.split(",");
                           tdkTestObj1.setResultStatus("SUCCESS");
                           print "TEST STEP 1: Get the RSSI range value";
                           print "EXPECTED RESULT 1: Should Get RSSI range value";
                           print "ACTUAL RESULT 1:The RSSI range value : %s" % Range;
                           #Get the result of execution
                           print "[TEST EXECUTION RESULT] : SUCCESS"

                           #min_rssi and max_rssi are the random numbers range
                           #coeffecient gives wether the range is negative or positive
                           coeffecient = int (Range[2])
                           min_rssi= int (Range[0])
                           print"min_rssi: ",min_rssi*coeffecient
                           max_rssi = int (Range[1])
                           print"max_rssi:", max_rssi*coeffecient
		           setValue= random.randint(min_rssi,max_rssi)
                           value = coeffecient* setValue
                           setValue = value
                           print"RSSI value to be set:",setValue
			   tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

			   if expectedresult in actualresult:
                              tdkTestObj.setResultStatus("SUCCESS");
                              print "setBandSteeringRSSIThreshold() call success"
                              print "TEST EXECUTION RESULT :SUCCESS"

			      getMethod = "getBandSteeringRSSIThreshold"
			      radioIndex = idx;
			      primitive = 'WIFIHAL_GetOrSetParamIntValue'
                              details = ""
			      tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

			      if expectedresult in actualresult:
                                 tdkTestObj.setResultStatus("SUCCESS");
                                 print "getBandSteeringRSSIThreshold() call success"
                                 print "TEST EXECUTION RESULT :SUCCESS"

                                 finalGetValue = ""
				 finalGetValue = details.split(":")[1].strip()

				 if setValue == int(finalGetValue):
				    print "TEST STEP2: Comparing set and get values of BandSteeringRSSIThreshold"
				    print "EXPECTED RESULT2: Set and get values should be the same"
				    print "ACTUAL RESULT 2: Set and get values are the same"
				    print "Set value: %s"%setValue
				    print "Get value: %s"%finalGetValue
				    print "TEST EXECUTION RESULT :SUCCESS"
				    tdkTestObj.setResultStatus("SUCCESS");
				 else:
				     print "TEST STEP2: Comparing set and get values of BandSteeringRSSIThreshold"
				     print "EXPECTED RESULT2: Set and get values should be the same"
				     print "ACTUAL RESULT 2: Set and get values are NOT the same"
				     print "Set value: %s"%setValue
				     print "Get value: %s"%finalGetValue
				     print "TEST EXECUTION RESULT :FAILURE"
				     tdkTestObj.setResultStatus("FAILURE");
			      else:
			   	  tdkTestObj.setResultStatus("FAILURE");
				  print "getBandSteeringRSSIThreshold() call failed after set operation"
			      #Revert back to initial value
			      setMethod = "setBandSteeringRSSIThreshold"
			      primitive = 'WIFIHAL_GetOrSetParamIntValue'
			      setValue = int(initGetValue)
			      tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

	         	      if expectedresult in actualresult:
	                         tdkTestObj.setResultStatus("SUCCESS");
                                 print "Successfully reverted back to inital value"
		              else:
			          tdkTestObj.setResultStatus("FAILURE");
		                  print "Unable to revert to initial value"
		           else:
			        tdkTestObj.setResultStatus("FAILURE");
			        print "setBandSteeringRSSIThreshold() call failed"
                        else:
                            tdkTestObj1.setResultStatus("FAILURE");
                            print "TEST STEP 1: Get the RSSI range value";
                            print "EXPECTED RESULT 1: Should Get RSSI range value";
                            print "ACTUAL RESULT 1: Failed to get  the RSSI range value : %s" % Range;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE"

		    else:
			tdkTestObj.setResultStatus("FAILURE");
			print "getBandSteeringRSSIThreshold() call failed"
		else:
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "BandSteeringCapability is disabled"
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "getBandSteeringCapability() call failed"
    obj.unloadModule("wifihal");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load wifi/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
