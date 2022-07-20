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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_WIFIHAL_5GHzSetSecurityRadiusSettings</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetSecurityRadiusSettings</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get and set the SecurityRadiusSetting parameters for 5GHz</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_277</test_case_id>
    <test_objective>To get and set the SecurityRadiusSetting parameters for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurityRadiusSettings()
wifi_setApSecurityRadiusSettings()
</api_or_interface_used>
    <input_parameters>methodName : getApSecurityRadiusSettings
methodName : setApSecurityRadiusSettings
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the module
2.Using WIFIHAL_GetOrSetSecurityRadiusSettings, call the api wifi_getApSecurityRadiusSettings() to get the initial radius settings.
3. Using WIFIHAL_GetOrSetSecurityRadiusSettings, call the api wifi_setApSecurityRadiusSettings() and set the parameters to a different value
4. Call wifi_getApSecurityRadiusSettings() and get the values again.
5. Check if the set and get values are the same.
6.If get and set values are same,return SUCCESS else FAILURE.
7.Unload the module.</automation_approch>
    <except_output>Set and get values of SecurityRadiusSettings parameters should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetSecurityRadiusSettings</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetSecurityRadiusSettings');

def GetorSetApSecurityRadiusSettings(obj, primitive, radioIndex, RadiusServerRetries, RadiusServerRequestTimeout, PMKLifetime, PMKCaching, PMKCacheInterval, MaxAuthenticationAttempts, BlacklistTableTimeout, IdentityRequestRetryInterval, QuietPeriodAfterFailedAuthentication, methodname):
    #Prmitive test case which associated to this Script
    tdkTestObj = obj.createTestStep(primitive);
    #Radio index is 0 for 2.4GHz and 1 for 5GHz
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

#Get the result of connection with test component and DUT
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

	    expectedresult = "SUCCESS";
	    radioIndex = idx
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
		    print "TEST STEP 1: Get the ApSecurityRadiusSettings details"
		    print "EXPECTED RESULT 1: Should get the ApSecurityRadiusSettings parameters as non empty values"
		    print "ACTUAL RESULT 1: Obtained the ApSecurityRadiusSettings parameters as a NON EMPTY values"
		    print "Initial ApSecurityRadiusSettings details : "
		    for values in initDetails:
			print values

		    tdkTestObj.setResultStatus("SUCCESS");

		    expectedresult = "SUCCESS";
		    radioIndex = idx
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

			expectedresult = "SUCCESS";
			radioIndex = idx
			getMethod = "getApSecurityRadiusSettings"
			primitive = "WIFIHAL_GetOrSetSecurityRadiusSettings"

			#Calling the method to execute wifi_getApSecurityRadiusSettings()
			tdkTestObj, actualresult, details = GetorSetApSecurityRadiusSettings(obj, primitive, radioIndex, 0,0,0,0,0,0,0,0,0, getMethod)

			if expectedresult in actualresult:
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

			    else:
				tdkTestObj.setResultStatus("FAILURE");
				print "TEST STEP 3: Comparing the set and get values of ApSecurityRadiusSettings details"
				print "EXPECTED RESULT 3: Set and get values should be the same"
				print "ACTUAL RESULT 3: Set and get values are NOT the same"
				print "Set values: RadiusServerRetries = %s\nRadiusServerRequestTimeout = %s\nPMKLifetime = %s\nPMKCaching =%s\nPMKCacheInterval=%s\nMaxAuthenticationAttempts =%s\nBlacklistTableTimeout=%s\nIdentityRequestRetryInterval=%s\nQuietPeriodAfterFailedAuthentication=%s\n"%(RadiusServerRetries,RadiusServerRequestTimeout,PMKLifetime,PMKCaching,PMKCacheInterval,MaxAuthenticationAttempts,BlacklistTableTimeout,IdentityRequestRetryInterval,QuietPeriodAfterFailedAuthentication)
				print "Get values: RadiusServerRetries = %s\nRadiusServerRequestTimeout = %s\nPMKLifetime = %s\nPMKCaching =%s\nPMKCacheInterval=%s\nMaxAuthenticationAttempts =%s\nBlacklistTableTimeout=%s\nIdentityRequestRetryInterval=%s\nQuietPeriodAfterFailedAuthentication=%s\n"%(outputValues[0],outputValues[1],outputValues[2],outputValues[3],outputValues[4],outputValues[5],outputValues[6],outputValues[7],outputValues[8]);

			else:
			    tdkTestObj.setResultStatus("FAILURE");
			    print "wifi_getApSecurityRadiusSettings() call failed"

			#Reverting the values to previous value
			expectedresult = "SUCCESS";
			radioIndex = idx
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
		else:
		    print "TEST STEP 1: Get the ApSecurityRadiusSettings details"
		    print "EXPECTED RESULT 1: Should get the ApSecurityRadiusSettings parameters as non empty values"
		    print "ACTUAL RESULT 1: Obtained the ApSecurityRadiusSettings parameters as a NON EMPTY values"
		    print "ApSecurityRadiusSettings details : %s"%output
		    tdkTestObj.setResultStatus("FAILURE");

	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "wifi_getApSecurityRadiusSettings() call failed"

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
