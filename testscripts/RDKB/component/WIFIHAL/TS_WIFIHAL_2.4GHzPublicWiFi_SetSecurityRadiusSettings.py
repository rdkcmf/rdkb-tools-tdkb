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
  <name>TS_WIFIHAL_2.4GHzPublicWiFi_SetSecurityRadiusSettings</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetSecurityRadiusSettings</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get and set the SecurityRadiusSetting parameters for 2.4GHz for public wifi</synopsis>
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
    <test_case_id>TC_WIFIHAL_584</test_case_id>
    <test_objective>To get and set the SecurityRadiusSetting parameters for 2.4GHz for public wifi</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurityRadiusSettings()
wifi_setApSecurityRadiusSettings()</api_or_interface_used>
    <input_parameters>methodName : getApSecurityRadiusSettings
methodName : setApSecurityRadiusSettings
radioIndex : (2Gpublicwifiindex) </input_parameters>
    <automation_approch>1.Load the module
2.Get the 2G public wifi apindex from platform property file
3.Using WIFIHAL_GetOrSetSecurityRadiusSettings, call the api wifi_getApSecurityRadiusSettings() to get the initial radius settings.
4. Using WIFIHAL_GetOrSetSecurityRadiusSettings, call the api wifi_setApSecurityRadiusSettings() and set the parameters to a different value
5. Call wifi_getApSecurityRadiusSettings() and get the values again.
6. Check if the set and get values are the same.
7.If get and set values are same,return SUCCESS else FAILURE.
8.Unload the module.</automation_approch>
    <expected_output>Set and get values of SecurityRadiusSettings parameters should be the same</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzPublicWiFi_SetSecurityRadiusSettings</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase scrip
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetSecurityRadiusSettings');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzPublicWiFi_SetSecurityRadiusSettings');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

def GetorSetApSecurityRadiusSettings(obj, primitive, radioIndex, RadiusServerRetries, RadiusServerRequestTimeout, PMKLifetime, PMKCaching, PMKCacheInterval, MaxAuthenticationAttempts, BlacklistTableTimeout, IdentityRequestRetryInterval, QuietPeriodAfterFailedAuthentication, methodname):
    #Prmitive test case which associated to this Script
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("radioIndex",radioIndex);
    tdkTestObj.addParameter("methodName", methodname);
    tdkTestObj.addParameter("RadiusServerRetries", RadiusServerRetries);
    tdkTestObj.addParameter("RadiusServerRequestTimeout", RadiusServerRequestTimeout);
    tdkTestObj.addParameter("PMKCaching", PMKCaching);
    tdkTestObj.addParameter("PMKLifetime", PMKLifetime);
    tdkTestObj.addParameter("PMKCacheInterval", PMKCacheInterval);
    tdkTestObj.addParameter("MaxAuthenticationAttempts", MaxAuthenticationAttempts);
    tdkTestObj.addParameter("BlacklistTableTimeout", BlacklistTableTimeout);
    tdkTestObj.addParameter("IdentityRequestRetryInterval", IdentityRequestRetryInterval);
    tdkTestObj.addParameter("QuietPeriodAfterFailedAuthentication", QuietPeriodAfterFailedAuthentication);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return (tdkTestObj, actualresult, details);

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
    if expectedresult not in actualresult and details == "":
        print "TEST STEP 0: Get APINDEX_2G_PUBLIC_WIFI  from property file";
        print "EXPECTED RESULT 0: Should  get APINDEX_2G_PUBLIC_WIFI  from property file"
        print "ACTUAL RESULT 0: APINDEX_2G_PUBLIC_WIFI from properties file : ", details;
        print "TEST EXECUTION RESULT : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");
    else:
            apIndex = int(details);
            print "TEST STEP 0: Get APINDEX_2G_PUBLIC_WIFI  from property file";
            print "EXPECTED RESULT 0: Should  get APINDEX_2G_PUBLIC_WIFI  from property file"
            print "ACTUAL RESULT 0: APINDEX_2G_PUBLIC_WIFI from property file :", apIndex ;
            print "TEST EXECUTION RESULT :SUCCESS";
            tdkTestObj.setResultStatus("SUCCESS");

	    expectedresult = "SUCCESS";
	    radioIndex = apIndex
	    getMethod = "getApSecurityRadiusSettings"
	    primitive = "WIFIHAL_GetOrSetSecurityRadiusSettings"
	    #Calling the method to execute wifi_getApSecurityRadiusSettings()
	    tdkTestObj, actualresult, details = GetorSetApSecurityRadiusSettings(obj, primitive, radioIndex, 0,0,0,0,0,0,0,0,0, getMethod)
	    if expectedresult in actualresult:
		output  = details.split(":")[1].strip()
		initDetails = output.split(",")
		initValues = [i.split("=",1)[1] for i in initDetails]
		#Checking if all the output values are non emtpy
		if all(initValues):
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP 1: Get the ApSecurityRadiusSettings details"
		    print "EXPECTED RESULT 1: Should get the ApSecurityRadiusSettings parameters as non empty values"
		    print "ACTUAL RESULT 1: Obtained the ApSecurityRadiusSettings parameters as a NON EMPTY values"
		    print "Initial ApSecurityRadiusSettings details : "
                    print "TEST EXECUTION RESULT :SUCCESS ";
		    for values in initDetails:
			print values
		    expectedresult = "SUCCESS";
		    radioIndex = apIndex
		    setMethod = "setApSecurityRadiusSettings"
		    primitive = "WIFIHAL_GetOrSetSecurityRadiusSettings"
		    RadiusServerRetries = 0
		    RadiusServerRequestTimeout = 0
		    PMKLifetime = 1900
		    PMKCaching = 1
		    PMKCacheInterval = 0
		    MaxAuthenticationAttempts = 0
		    BlacklistTableTimeout = 0
		    IdentityRequestRetryInterval = 0
		    QuietPeriodAfterFailedAuthentication = 0
		    #Calling the method to execute wifi_setApSecurityRadiusSettings()
		    tdkTestObj, actualresult, details = GetorSetApSecurityRadiusSettings(obj, primitive, radioIndex, RadiusServerRetries, RadiusServerRequestTimeout, PMKLifetime, PMKCaching, PMKCacheInterval, MaxAuthenticationAttempts, BlacklistTableTimeout, IdentityRequestRetryInterval, QuietPeriodAfterFailedAuthentication, setMethod)
		    if expectedresult in actualresult:
			tdkTestObj.setResultStatus("SUCCESS");
			print "TEST STEP 2: Set the ApSecurityRadiusSettings details"
			print "EXPECTED RESULT 2: Should set the ApSecurityRadiusSettings parameters"
			print "ACTUAL RESULT 2: Successfully sets the ApSecurityRadiusSettings parameters"
                        print "TEST EXECUTION RESULT :SUCCESS ";

			expectedresult = "SUCCESS";
			radioIndex = apIndex
			getMethod = "getApSecurityRadiusSettings"
			primitive = "WIFIHAL_GetOrSetSecurityRadiusSettings"
			#Calling the method to execute wifi_getApSecurityRadiusSettings()
			tdkTestObj, actualresult, details = GetorSetApSecurityRadiusSettings(obj, primitive, radioIndex, 0,0,0,0,0,0,0,0,0, getMethod)
			if expectedresult in actualresult and details != "":
			    output  = details.split(":")[1].strip()
			    outputDetails = output.split(",")
			    outputValues = [int(i.split("=",1)[1]) for i in outputDetails]
			    if outputValues == [RadiusServerRetries,RadiusServerRequestTimeout,PMKLifetime,PMKCaching,PMKCacheInterval,MaxAuthenticationAttempts,BlacklistTableTimeout,IdentityRequestRetryInterval,QuietPeriodAfterFailedAuthentication]:
				tdkTestObj.setResultStatus("SUCCESS");
				print "TEST STEP 3: Comparing the set and get values of ApSecurityRadiusSettings details"
				print "EXPECTED RESULT 3: Set and get values should be the same"
				print "ACTUAL RESULT 3: Set and get values are the same"
				print "Set values: RadiusServerRetries = %s\nRadiusServerRequestTimeout = %s\nPMKLifetime = %s\nPMKCaching =%s\nPMKCacheInterval=%s\nMaxAuthenticationAttempts =%s\nBlacklistTableTimeout=%s\nIdentityRequestRetryInterval=%s\nQuietPeriodAfterFailedAuthentication=%s\n"%(RadiusServerRetries,RadiusServerRequestTimeout,PMKLifetime,PMKCaching,PMKCacheInterval,MaxAuthenticationAttempts,BlacklistTableTimeout,IdentityRequestRetryInterval,QuietPeriodAfterFailedAuthentication)
				print "Get values: RadiusServerRetries = %s\nRadiusServerRequestTimeout = %s\nPMKLifetime = %s\nPMKCaching =%s\nPMKCacheInterval=%s\nMaxAuthenticationAttempts =%s\nBlacklistTableTimeout=%s\nIdentityRequestRetryInterval=%s\nQuietPeriodAfterFailedAuthentication=%s\n"%(outputValues[0],outputValues[1],outputValues[2],outputValues[3],outputValues[4],outputValues[5],outputValues[6],outputValues[7],outputValues[8]);
                                print "TEST EXECUTION RESULT :SUCCESS ";
			    else:
				tdkTestObj.setResultStatus("FAILURE");
				print "TEST STEP 3: Comparing the set and get values of ApSecurityRadiusSettings details"
				print "EXPECTED RESULT 3: Set and get values should be the same"
				print "ACTUAL RESULT 3: Set and get values are NOT the same"
				print "Set values: RadiusServerRetries = %s\nRadiusServerRequestTimeout = %s\nPMKLifetime = %s\nPMKCaching =%s\nPMKCacheInterval=%s\nMaxAuthenticationAttempts =%s\nBlacklistTableTimeout=%s\nIdentityRequestRetryInterval=%s\nQuietPeriodAfterFailedAuthentication=%s\n"%(RadiusServerRetries,RadiusServerRequestTimeout,PMKLifetime,PMKCaching,PMKCacheInterval,MaxAuthenticationAttempts,BlacklistTableTimeout,IdentityRequestRetryInterval,QuietPeriodAfterFailedAuthentication)
				print "Get values: RadiusServerRetries = %s\nRadiusServerRequestTimeout = %s\nPMKLifetime = %s\nPMKCaching =%s\nPMKCacheInterval=%s\nMaxAuthenticationAttempts =%s\nBlacklistTableTimeout=%s\nIdentityRequestRetryInterval=%s\nQuietPeriodAfterFailedAuthentication=%s\n"%(outputValues[0],outputValues[1],outputValues[2],outputValues[3],outputValues[4],outputValues[5],outputValues[6],outputValues[7],outputValues[8]);
                                print "TEST EXECUTION RESULT : FAILURE";
			else:
			    tdkTestObj.setResultStatus("FAILURE");
			    print "wifi_getApSecurityRadiusSettings() call failed"
			#Reverting the values to previous value
			expectedresult = "SUCCESS";
			radioIndex = apIndex
			setMethod = "setApSecurityRadiusSettings"
			primitive = "WIFIHAL_GetOrSetSecurityRadiusSettings"
			RadiusServerRetries = int(initValues[0]);
			RadiusServerRequestTimeout = int(initValues[1]);
			PMKLifetime = int(initValues[2]);
			PMKCaching = int(initValues[3]);
			PMKCacheInterval = int(initValues[4]);
			MaxAuthenticationAttempts = int(initValues[5]);
			BlacklistTableTimeout = int(initValues[6]);
			IdentityRequestRetryInterval = int(initValues[7]);
			QuietPeriodAfterFailedAuthentication = int(initValues[8]);
			#Calling the method to execute wifi_setApSecurityRadiusSettings()
			tdkTestObj, actualresult, details = GetorSetApSecurityRadiusSettings(obj, primitive, radioIndex, RadiusServerRetries, RadiusServerRequestTimeout, PMKLifetime, PMKCaching, PMKCacheInterval, MaxAuthenticationAttempts, BlacklistTableTimeout, IdentityRequestRetryInterval, QuietPeriodAfterFailedAuthentication, setMethod)
			if expectedresult in actualresult:
			    print "Successfully reverted to initial values"
			    tdkTestObj.setResultStatus("SUCCESS");
			else:
			    print " Unable to revert to initial value"
			    tdkTestObj.setResultStatus("FAILURE");
		    else:
			tdkTestObj.setResultStatus("FAILURE");
			print "TEST STEP 2: Set the ApSecurityRadiusSettings details"
			print "EXPECTED RESULT 2: Should set the ApSecurityRadiusSettings parameters"
			print "ACTUAL RESULT 2: Successfully sets the ApSecurityRadiusSettings parameters"
                        print "TEST EXECUTION RESULT : FAILURE";
		else:
		    print "TEST STEP 1: Get the ApSecurityRadiusSettings details"
		    print "EXPECTED RESULT 1: Should get the ApSecurityRadiusSettings parameters as non empty values"
		    print "ACTUAL RESULT 1: Obtained the ApSecurityRadiusSettings parameters as a NON EMPTY values"
		    print "ApSecurityRadiusSettings details : %s"%output
                    print "TEST EXECUTION RESULT : FAILURE";
		    tdkTestObj.setResultStatus("FAILURE");
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "wifi_getApSecurityRadiusSettings() call failed"
    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
