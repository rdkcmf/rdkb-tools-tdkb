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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzSetApBasicAuthenticationMode</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>8</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set access point BasicAuthenticationMode and verify it by getting it</synopsis>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_135</test_case_id>
    <test_objective>To set and get the BasicAuthenticationMode for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApBasicAuthenticationMode()
wifi_setApBasicAuthenticationMode()</api_or_interface_used>
    <input_parameters>methodName : getApBasicAuthenticationMode()
methodName : setApBasicAuthenticationMode()
ApIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getApBasicAuthenticationMode() and save the get value
3. Choose a BasicAuthenticationMode from supported BasicAuthenticationMode  list and using  WIFIHAL_GetOrSetParamStringValue invoke wifi_setApBasicAuthenticationMode()
4. Invoke wifi_getApBasicAuthenticationMode() to get the previously set value.
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
6. Revert the AuthenticationMode back to initial value
7. Unload wifihal module</automation_approch>
    <except_output>Set and get values of AuthenticationMode should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetApBasicAuthenticationMode</test_script>
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

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetApBasicAuthenticationMode');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetApBasicAuthenticationMode');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

def setApBeaconType(obj,apIndex):

    expectedresult="SUCCESS";
    #apIndex = 0
    getMethod = "getApBeaconType"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method to execute wifi_getApBeaconType()
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

    if expectedresult in actualresult:
            initialBeaconType = details.split(":")[1].strip()
            tdkTestObj.setResultStatus("SUCCESS");
            expectedresult = "SUCCESS";
            #apIndex = 0
            setMethod = "setApBeaconType"
            setBeaconType = 'None'
            primitive = 'WIFIHAL_GetOrSetParamStringValue'

            #Calling the method to execute wifi_setApBeaconType()
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setBeaconType, setMethod)

            if expectedresult in actualresult:
                expectedresult="SUCCESS";
                #apIndex = 0
                getMethod = "getApBeaconType"
                primitive = 'WIFIHAL_GetOrSetParamStringValue'

                #Calling the method to execute wifi_getApBeaconType()
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
                finalBeaconType = details.split(":")[1].strip()

                if expectedresult in actualresult:
                    if finalBeaconType == setBeaconType:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP: Compare the set and get values of ApBeaconType"
                        print "EXPECTED RESULT: Set and get values of ApBeaconType should be same"
                        print "ACTUAL RESULT: Set and get values of ApBeaconType are the same"
                        print "setBeaconType = ",setBeaconType
                        print "getBeaconType = ",finalBeaconType
                        print "TEST EXECUTION RESULT : SUCCESS"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP: Compare the set and get values of ApBeaconType"
                        print "EXPECTED RESULT: Set and get values of ApBeaconType should be same"
                        print "ACTUAL RESULT: Set and get values of ApBeaconType are NOT the same"
                        print "setBeaconType = ",setBeaconType
                        print "getBeaconType = ",finalBeaconType
                        print "TEST EXECUTION RESULT : FAILURE"

                else:
                    print "wifi_getApBeaconType() call failed"
                    tdkTestObj.setResultStatus("FAILURE");

            else:
                print "wifi_setApBeaconType() call failed"
                tdkTestObj.setResultStatus("FAILURE");

    #break;
    return (initialBeaconType);

if "SUCCESS" in loadmodulestatus.upper()and "SUCCESS" in sysloadmodulestatus.upper():
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
	    supportedAuthModes = "sh %s/tdk_utility.sh parseConfigFile SUPPORTED_AUTH_MODES" %TDK_PATH;
	    tdkTestObj.addParameter("command", supportedAuthModes);
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    supportedAuthModes = tdkTestObj.getResultDetails().strip();
	    supportedAuthModes = supportedAuthModes.replace("\\n", "");

	    if supportedAuthModes and expectedresult in actualresult:
		tdkTestObj.setResultStatus("SUCCESS");
		supportedModes = supportedAuthModes.split(",");
		print "TEST STEP : Get the list of supported Authentication Modes from /etc/tdk_platform.properties file";
		print "EXPECTED RESULT : Should get the list of supported Authentication Modes";
		print "ACTUAL RESULT : Got the list of supported Authentication Modes as %s" %supportedModes;
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : SUCCESS";

		expectedresult="SUCCESS";
		apIndex = idx;
		getMethod = "getApBasicAuthenticationMode"
		primitive = 'WIFIHAL_GetOrSetParamStringValue'

		#Calling the method to execute wifi_getApBasicAuthenticationMode()
		tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
		initialMode = details.split(":")[1].strip()

		if expectedresult in actualresult and initialMode in supportedModes:
		    tdkTestObj.setResultStatus("SUCCESS");

		    for setMode in supportedModes:
			if initialMode == setMode:
			    continue;
			else:
			    if (setMode == 'None'):
				#Calling the function to perform the settings and getting and verification of becon type to be none.
				initialBeaconType = setApBeaconType(obj,idx);


			    expectedresult = "SUCCESS";
			    apIndex = idx;
			    setMethod = "setApBasicAuthenticationMode"
			    primitive = 'WIFIHAL_GetOrSetParamStringValue'


			    #Calling the method to execute wifi_setApBasicAuthenticationMode()
			    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)

			    if expectedresult in actualresult:
				expectedresult="SUCCESS";
				apIndex = idx;
				getMethod = "getApBasicAuthenticationMode"
				primitive = 'WIFIHAL_GetOrSetParamStringValue'

				#Calling the method to execute wifi_getApBasicAuthenticationMode()
				tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
				finalMode = details.split(":")[1].strip()

				if expectedresult in actualresult:
				    if finalMode == setMode:
					tdkTestObj.setResultStatus("SUCCESS");
					print "TEST STEP: Compare the set and get values of ApBasicAuthenticationMode"
					print "EXPECTED RESULT: Set and get values of ApBasicAuthenticationMode should be same"
					print "ACTUAL RESULT: Set and get values of ApBasicAuthenticationMode are the same"
					print "setBasicAuthenticationMode = ",setMode
					print "getBasicAuthenticationMode = ",finalMode
					print "TEST EXECUTION RESULT : SUCCESS"
				    else:
					tdkTestObj.setResultStatus("FAILURE");
					print "TEST STEP: Compare the set and get values of ApBasicAuthenticationMode"
					print "EXPECTED RESULT: Set and get values of ApBasicAuthenticationMode should be same"
					print "ACTUAL RESULT: Set and get values of ApBasicAuthenticationMode are NOT the same"
					print "setBasicAuthenticationMode = ",setMode
					print "getBasicAuthenticationMode = ",finalMode
					print "TEST EXECUTION RESULT : FAILURE"

				    #Revert the BasicAuthenticationMode back to initial value
				    setMethod = "setApBasicAuthenticationMode"
				    primitive = 'WIFIHAL_GetOrSetParamStringValue'
				    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initialMode, setMethod)
				    if expectedresult in actualresult:
					print "Successfully reverted the BasicAuthenticationMode to initial value"
					tdkTestObj.setResultStatus("SUCCESS");
				    else:
					print "Unable to revert the BasicAuthenticationMode"
					tdkTestObj.setResultStatus("FAILURE");
				else:
				    print "wifi_getApBasicAuthenticationMode() call failed"
				    tdkTestObj.setResultStatus("FAILURE");
			    else:
				print "wifi_setApBasicAuthenticationMode() call failed"
				tdkTestObj.setResultStatus("FAILURE");

			    if (setMode == 'None'):
				expectedresult="SUCCESS";
				apIndex = idx;
				setMethod = "setApBeaconType"
				primitive = 'WIFIHAL_GetOrSetParamStringValue'

				#Revert the BeaconType back to initial value
				tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initialBeaconType, setMethod)
				if expectedresult in actualresult:
				    print "Successfully reverted the BeaconType to initial value"
				    tdkTestObj.setResultStatus("SUCCESS");
				else:
				    print "Unable to revert the BeaconType"
				    tdkTestObj.setResultStatus("FAILURE");
			    break;

		else:
		    tdkTestObj.setResultStatus("FAILURE");
	    else :
		 tdkTestObj.setResultStatus("FAILURE");
		 print "TEST STEP : Get the list of supported Authentication Modes from /etc/tdk_platform.properties file";
		 print "EXPECTED RESULT : Should get the list of supported Authentication Modes";
		 print "ACTUAL RESULT : Failed to get the list of supported AuthenticationModes from /etc/tdk_platform.properties file";
		 #Get the result of execution
		 print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
