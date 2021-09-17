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
  <name>TS_WIFIHAL_2.4GHzPublicWiFi_SetApSecurityReset</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_ParamRadioIndex</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To invoke the api wifi_setApSecurityReset() and check whether the ap security mode enabled  value is equal to the default value for 2.4GHz public wifi</synopsis>
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
    <test_case_id>TC_WIFIHAL_586</test_case_id>
    <test_objective>To invoke the api wifi_setApSecurityReset() and check whether the ap security mode enabled  value is equal to the default value for 2.4GHz public wifi</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApSecurityReset()
wifi_getApSecurityModeSupported()
wifi_getApSecurityModeEnabled()
wifi_setApSecurityModeEnabled()</api_or_interface_used>
    <input_parameters>methodName : setApSecurityReset
methodName : getApSecurityModeSupported
methodName : getApSecurityModeEnabled
methodName : setApSecurityModeEnabled
radioIndex : (2Gpublicwifiindex)</input_parameters>
    <automation_approch>1. Load the module.
2.Get the 2G public wifi index from platform property file
3. Get the supported ap security modes by invoking  wifi_getApSecurityModeSupported() api.
4. Get the initial ap security mode enabled by invoking wifi_getApSecurityModeEnabled() api.
5. If the initial ap security mode enabled value is equal to the default value then set the ap security mode enabled to another value by invoking wifi_setApSecurityModeEnabled() api.
6. Invoke wifi_setApSecurityReset() to reset security parameters.
7. Get the security mode enabled by invoking wifi_getApSecurityModeEnabled() api after reset and it should be equal to default value.
8. If the value is equal to default value, return SUCCESS, else FAILURE.
9. Unload wifihal module.</automation_approch>
    <expected_output>After invoking wifi_setApSecurityReset() api ap security mode enabled value should be changed to default value.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPublicWiFi_SetApSecurityReset</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
import time;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetApSecurityReset');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetApSecurityReset');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;
DefaultMode="";

def GetSetApSecurityMode(obj,param,Method, apIndex):
    apIndex = apIndex;
    primitive = 'WIFIHAL_GetOrSetParamStringValue';
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("radioIndex", apIndex);
    #'param' is valid for only set operations. It isdummy attribute for get functions
    tdkTestObj.addParameter("param", param);
    tdkTestObj.addParameter("methodName", Method);
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return (tdkTestObj,actualresult,details);

def setApSecurityReset(apIndex):
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("WIFIHAL_ParamRadioIndex");
    #Giving the method name to invoke the api wifi_setApSecurityReset()
    tdkTestObj.addParameter("methodName","setApSecurityReset")
    #Radio index is 8 for 2.4GHz and 9 for 5GHz
    tdkTestObj.addParameter("radioIndex",apIndex);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "**************************************************";
        print "TEST STEP : Invoke wifi_setApSecurityReset() api";
        print "EXPECTED RESULT : Should successfully invoke wifi_setApSecurityReset() api";
        print "ACTUAL RESULT :wifi_setApSecurityReset() OPERATION SUCCESS";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        print "**************************************************";
        time.sleep(3);
        tdkTestObj, actualresult, details = GetSetApSecurityMode(obj,"0","getApSecurityModeEnabled", apIndex);
        if expectedresult in actualresult :
	    tdkTestObj.setResultStatus("SUCCESS");
	    ResetMode = details.split(":")[1].strip();
            print "**************************************************";
            print "TEST STEP : To get the Ap Security Mode Enabled value after reset operation";
            print "EXPECTED RESULT : Should successfully get the Ap Security Mode Enabled value after reset operation";
            print "ACTUAL RESULT : Successfully got the Ap Security Enabled value as %s after reset operation" %ResetMode;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            print "**************************************************";
            print "The current ApSecurityMode and default values are %s and %s "%(ResetMode,DefaultMode);
            if ResetMode == DefaultMode :
                tdkTestObj.setResultStatus("SUCCESS");
                print "**************************************************";
                print "TEST STEP : To invoke the api wifi_setApSecurityReset and check whether the ApSecurityModeEnabled is equal to default mode and not equal to the set mode for 2.4GHz";
	        print "EXPECTED RESULT : The mode should be equal to the default mode for 2.4GHz";
	        print "ACTUAL RESULT : The mode is equal to the default mode for 2.4GHz";
	        #Get the result of execution
	        print "[TEST EXECUTION RESULT] : SUCCESS";
                print "**************************************************";
            else :
                print "**************************************************";
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : To invoke the api wifi_setApSecurityReset and check whether the ApSecurityModeEnabled is equal to default mode and not equal to the set mode for 2.4GHz";
                print "EXPECTED RESULT : The mode should be equal to the default mode for 2.4GHz";
                print "ACTUAL RESULT : The mode is NOT equal to the default mode for 2.4GHz";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
                print "**************************************************";
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "**************************************************";
            print "TEST STEP : To get the Ap Security Mode Enabled value after reset operation";
            print "EXPECTED RESULT : Should successfully get the Ap Security Mode Enabled value after reset operation";
            print "ACTUAL RESULT : Failed to get the Ap Security Enabled value as after reset operation";
            print "DETAILS :",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
            print "**************************************************";
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print "**************************************************";
        print "TEST STEP : Invoke wifi_setApSecurityReset() api";
        print "EXPECTED RESULT : Should successfully invoke wifi_setApSecurityReset() api";
        print "ACTUAL RESULT :wifi_setApSecurityReset() OPERATION FAILED";
        print "DETAILS:",details;
        #Get the result of execution^M
        print "[TEST EXECUTION RESULT] : FAILURE";
        print "**************************************************";

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";
    #Getting APINDEX_2G_PUBLIC_WIFI value from tdk_platform_properties"
    cmd= "sh %s/tdk_utility.sh parseConfigFile APINDEX_2G_PUBLIC_WIFI" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    if expectedresult in actualresult and details != "":
        apIndex = int(details);
        print "TEST STEP 1: Get APINDEX_2G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT 1: Should  get APINDEX_2G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT 1: APINDEX_2G_PUBLIC_WIFI from property file :", apIndex ;
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        expectedresult="SUCCESS";
        Mode = "sh %s/tdk_utility.sh parseConfigFile DEFAULT_AP_SECURITY_MODE_ENABLED" %TDK_PATH;
        tdkTestObj.addParameter("command", Mode);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        Mode = tdkTestObj.getResultDetails().strip();
        DefaultMode = Mode.strip().replace("\\n", "");
        if DefaultMode and expectedresult in actualresult :
       	    tdkTestObj.setResultStatus("SUCCESS");
	    print "**************************************************";
	    print "TEST STEP 2: Get the default ap security mode enabled value from /etc/tdk_platform.properties file";
	    print "EXPECTED RESULT 2: Should get the default ap security mode value";
            print "ACTUAL RESULT 2: Got the default ap security mode value as %s" %DefaultMode;
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] : SUCCESS";
	    print "**************************************************";
	    tdkTestObj, actualresult, details1 = GetSetApSecurityMode(obj,"0","getApSecurityModesSupported", apIndex);
	    if expectedresult in actualresult :
		tdkTestObj.setResultStatus("SUCCESS");
		supportedModes = details1.split(":")[1].strip();
		print "**************************************************";
		print "TEST STEP 3: Get list of Ap Security Modes Supported"
		print "EXPECTED RESULT 3: Should get the list of Ap Security Modes Supported successfully";
		print "ACTUAL RESULT 3: Successfully got the Ap Security Modes Supported as %s" %supportedModes;
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : SUCCESS";
		print "**************************************************";
		tdkTestObj, actualresult, details2 = GetSetApSecurityMode(obj,"0","getApSecurityModeEnabled", apIndex);
		if expectedresult in actualresult :
		    tdkTestObj.setResultStatus("SUCCESS");
	            initMode = details2.split(":")[1].strip();
		    print "**************************************************";
	            print "TEST STEP 4: Get the initial Ap Security Mode Enabled value";
	            print "EXPECTED RESULT 4: Should get the initial Ap Security Mode Enabled value successfully";
	            print "ACTUAL RESULT 4 : Successfully got the Ap Security Mode Enabled value as %s" %initMode;
		    #Get the result of execution
	            print "[TEST EXECUTION RESULT] : SUCCESS";
		    print "**************************************************";
		    if initMode in supportedModes.split(','):
			tdkTestObj.setResultStatus("SUCCESS");
			print "**************************************************";
			print "TEST STEP 5: To check whether the initial Ap Security Mode Enabled is from the list of Ap Security Modes Supported";
			print "EXPECTED RESULT 5: The initial Ap Security Mode Enabled value should be from the list of Ap Security Modes Supported";
			print "ACTUAL RESULT 5: Initial Ap Security Mode Enabled value is from the list of Ap Security Modes Supported";
			#Get the result of execution
			print "[TEST EXECUTION RESULT] : SUCCESS";
			print "**************************************************";
			if initMode == DefaultMode :
			    print "The initial Ap Security Mode Enabled value is equal to the default Mode";
			    print "Setting the Ap Security Mode Enabled value to another value before invoking wifi_setApSecurityReset() api";
			    for setMode in supportedModes.split(','):
				if setMode == initMode :
				   continue;
				else:
				    print "Ap Security Mode Enabled value to be set is %s" %setMode;
			            tdkTestObj, actualresult1, setresult = GetSetApSecurityMode(obj,setMode,"setApSecurityModeEnabled", apIndex);
				    time.sleep(10);
				    tdkTestObj, actualresult2, getresult = GetSetApSecurityMode(obj,"0","getApSecurityModeEnabled", apIndex);
				    if expectedresult in actualresult1 :
					tdkTestObj.setResultStatus("SUCCESS");
					print "**************************************************";
					print "TEST STEP 6: To set Ap Security Mode Enabled to another value";
					print "EXPECTED RESULT 6: Successfully set the Ap Security Mode Enabled to another value";
					print "ACTUAL RESULT 6: wifi_setApSecurityModeEnabled() operation SUCCESS";
					#Get the result of execution
					print "[TEST EXECUTION RESULT] : SUCCESS";
					print "**************************************************";
					if expectedresult in actualresult2 :
				            tdkTestObj.setResultStatus("SUCCESS");
					    finalMode = getresult.split(":")[1].strip();
					    print "**************************************************";
					    print "TEST STEP 7: To get the Ap Security Mode Enabled value after set operation";
					    print "EXPECTED RESULT 7: Should successfully get the Ap Security Mode Enabled value after set operation";
					    print "ACTUAL RESULT 7: Successfully got the Ap Security Enabled value as %s after set operation" %finalMode;
					    #Get the result of execution
					    print "[TEST EXECUTION RESULT] : SUCCESS";
					    print "**************************************************";
					    print "setMode = ",setMode;
					    print "getMode = ",finalMode;
					    if finalMode == setMode:
						tdkTestObj.setResultStatus("SUCCESS");
						print "**************************************************";
						print "TEST STEP 8: Compare the set and get values of ApSecurityModeEnabled"
						print "EXPECTED RESULT 8: Set and get values of ApSecurityModeEnabled should be same";
						print "ACTUAL RESULT 8: Set and get values of ApSecurityModeEnabled are the same";
						print "SUCCESSFULLY SET THE AP SECURITY MODE ENABLED TO ANOTHER VALUE AS %s" %setMode;
						print " SET and GET values are EQUAL";
						#Get the result of execution
						print "[TEST EXECUTION RESULT] : SUCCESS";
						print "**************************************************";
						print "======INVOKING wifi_setApSecurityReset() API======";
						setApSecurityReset(apIndex);
				            else :
						 tdkTestObj.setResultStatus("FAILURE");
						 print "**************************************************";
						 print "TEST STEP 8: Compare the set and get values of ApSecurityModeEnabled"
						 print "EXPECTED RESULT 8: Set and get values of ApSecurityModeEnabled should be same";
						 print "ACTUAL RESULT 8: Set and get values of ApSecurityModeEnabled are NOT the same";
						 print "FAILED TO SET THE AP SECURITY MODE ENABLED TO ANOTHER VALUE AS %s" %setMode;
						 print "SET and GET values are NOT EQUAL";
						 #Get the result of execution
						 print "[TEST EXECUTION RESULT] : FAILURE";
						 print "**************************************************";
				            #Revert the ApSecurityModeEnabled back to initial value
					    tdkTestObj, actualresult, details = GetSetApSecurityMode(obj,initMode,"setApSecurityModeEnabled", apIndex);
					    if expectedresult in actualresult:
					       print "Successfully reverted the ApSecurityModeEnabled to initial value"
					       tdkTestObj.setResultStatus("SUCCESS");
					    else:
					        print "Unable to revert the ApSecurityModeEnabled to initial value"
					        tdkTestObj.setResultStatus("FAILURE");
					else:
					     tdkTestObj.setResultStatus("FAILURE");
					     print "**************************************************";
					     print "TEST STEP 7: To get the Ap Security Mode Enabled value after set operation";
				             print "EXPECTED RESULT 7: Should successfully get the Ap Security Mode Enabled value after set operation";
					     print "ACTUAL RESULT 7: Failed to get the Ap Security Mode Enabled value after set operation";
					     print "wifi_getApSecurityModeEnabled() call failed after set operation";
					     #Get the result of execution
					     print "[TEST EXECUTION RESULT] : FAILURE";
					     print "**************************************************";
			            else:
				        tdkTestObj.setResultStatus("FAILURE");
			           	print "**************************************************";
					print "TEST STEP 6: To set Ap Security Mode Enabled to another value";
					print "EXPECTED RESULT 6: Successfully set the Ap Security Mode Enabled to another value";
					print "ACTUAL RESULT 6: wifi_setApSecurityModeEnabled() operation FAILED";
				        #Get the result of execution
					print "[TEST EXECUTION RESULT] : FAILURE";
					print "**************************************************";
		                break;
	                else:
			    print "The initial Ap Security Mode Enabled value is NOT equal to the default Mode";
			    print "======INVOKING wifi_setApSecurityReset() API======";
			    setApSecurityReset(apIndex);
			    #Revert the ApSecurityModeEnabled back to initial value
		            tdkTestObj, actualresult, details = GetSetApSecurityMode(obj,initMode,"setApSecurityModeEnabled", apIndex);
			    if expectedresult in actualresult:
				print "Successfully reverted the ApSecurityModeEnabled to initial value"
				tdkTestObj.setResultStatus("SUCCESS");
		            else:
				print "Unable to revert the ApSecurityModeEnabled to initial value"
				tdkTestObj.setResultStatus("FAILURE");
	            else:
			tdkTestObj.setResultStatus("FAILURE");
			print "**************************************************";
			print "TEST STEP 5: To check whether the initial Ap Security Mode Enabled is from the list of Ap Security Modes Supported";
			print "EXPECTED RESULT 5: The initial Ap Security Mode Enabled value should be from the list of Ap Security Modes Supported";
			print "ACTUAL RESULT 5: Initial Ap Security Mode Enabled value is NOT from the list of Ap Security Modes Supported";
			#Get the result of execution
			print "[TEST EXECUTION RESULT] : FAILURE";
			print "**************************************************";
		else:
	            tdkTestObj.setResultStatus("FAILURE");
	            print "**************************************************";
	            print "TEST STEP 4: Get the initial Ap Security Mode Enabled value";
		    print "EXPECTED RESULT 4: Should the initial Ap Security Mode Enabled value successfully";
		    print "ACTUAL RESULT 4: Failed to get the initial Ap Security Mode Enabled value";
		    print "wifi_getApSecurityModeEnabled() operation FAILED";
		    #Get the result of execution
		    print "[TEST EXECUTION RESULT] : FAILURE";
		    print "**************************************************";
            else:
		tdkTestObj.setResultStatus("FAILURE");
		print "**************************************************";
		print "TEST STEP 3: Get list of Ap Security Modes Supported"
		print "EXPECTED RESULT 3: Should get the list of Ap Security Modes Supported successfully";
		print "ACTUAL RESULT 3: Failed to get the list of Ap Security Modes Supported";
		print "wifi_getApSecurityModeSupported() operation FAILED";
	        #Get the result of execution
	        print "[TEST EXECUTION RESULT] : FAILURE";
		print "**************************************************";
        else :
	     tdkTestObj.setResultStatus("FAILURE");
	     print "**************************************************";
	     print "TEST STEP 2: Get the default ap security mode enabled value from /etc/tdk_platform.properties file";
	     print "EXPECTED RESULT 2: Should get the default ap security mode enabled value";
             #Get the result of execution
	     print "[TEST EXECUTION RESULT] : FAILURE";
	     print "**************************************************";
    else:
        print "TEST STEP 1: Get APINDEX_2G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT 1: Should  get APINDEX_2G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT 1: APINDEX_2G_PUBLIC_WIFI from properties file : ", details;
        print "TEST EXECUTION RESULT : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
