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
<?xml version="1.0" encoding="UTF-8"?>
<xml>
  <id/>
  <version>1</version>
  <name>TS_WIFIAGENT_2.4GHZ_PublicWiFi_SetInvalidSecurityMode</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Try to set the security mode of 2.4GHZ public wifi to an invalid value. The only supported security mode is None.</synopsis>
  <groups_id/>
  <execution_time>4</execution_time>
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
    <test_case_id>TC_WIFIAGENT_59</test_case_id>
    <test_objective>Try to set the security mode of 2.4GHZ public wifi to an invalid value. The only supported security mode is None.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>"Device.WiFi.AccessPoint.5.Security.ModeEnabled"</input_parameters>
    <automation_approch>1. Load wifiagent module
2. Using WIFIAgent_Get, get and save Device.WiFi.AccessPoint.5.Security.ModeEnabled
3. Set Device.WiFi.AccessPoint.5.Security.ModeEnabled to an invalid value
</automation_approch>
    <except_output>Set invalid value security  mode should fail</except_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_WIFIAGENT_2.4GHZ_PublicWiFi_SetInvalidSecurityMode</test_script>
    <skipped>No</skipped>
    <release_version>M58</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from xfinityWiFiLib import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_2.4GHZ_PublicWiFi_SetInvalidSecurityMode');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Get current values of public wifi params
    expectedresult="SUCCESS";
    tdkTestObj,actualresult,orgValue = getPublicWiFiParamValues(obj);
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1:Get values of PublicWiFi params"
        print "TEST STEP 1 : Should get values of PublicWiFi params"
        print "ACTUAL RESULT 1:%s" %orgValue
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Set values to enable public wifi
        setvalues = ["44","68.86.15.199","68.86.15.171","true","true","true"];
        tdkTestObj, actualresult, details = setPublicWiFiParamValues(obj,setvalues);
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Enable public wifi"
            print "TEST STEP 2 : Should enable PublicWiFi"
            print "ACTUAL RESULT 2:%s" %details
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    #Get the current value of ModeEnabled
	    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.5.Security.ModeEnabled")
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            mode = details.split("VALUE:")[1].split(' ')[0];

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the current mode";
                print "EXPECTED RESULT 3: Should get the current mode";
                print "ACTUAL RESULT 3: Current security mode is %s" %mode;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

		#Set the security mode to an invalid value
		tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.5.Security.ModeEnabled")
                tdkTestObj.addParameter("paramValue","WEP-WPA2")
                tdkTestObj.addParameter("paramType","string")
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult not in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Set the security mode to an invalid value";
                    print "EXPECTED RESULT 4: Should fail to set the invalid security mode"
                    print "ACTUAL RESULT 4: %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
		else:
		    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Set the security mode to an invalid value";
                    print "EXPECTED RESULT 4: Should fail to set the invalid security mode"
                    print "ACTUAL RESULT 4: %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"

		    #Revert the security mode if the invalid value is set
		    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.5.Security.ModeEnabled")
                    tdkTestObj.addParameter("paramValue",mode)
                    tdkTestObj.addParameter("paramType","string")
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Revert the value of security mode";
                        print "EXPECTED RESULT 5: Should revert the value of security mode"
                        print "ACTUAL RESULT 5: %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS"
		    else:
			#Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Revert the value of security mode";
                        print "EXPECTED RESULT 5: Should revert the value of security mode"
                        print "ACTUAL RESULT 5: %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE"
  	    else:
	        tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the current mode";
                print "EXPECTED RESULT 3: Should get the current mode";
                print "ACTUAL RESULT 3: Current security mode is %s" %mode;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
            #Revert the values of public wifi params
            tdkTestObj, actualresult, details = setPublicWiFiParamValues(obj,orgValue);
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 6:Revert the PublicWiFi param values"
                print "TEST STEP 6 : Should revert the PublicWiFi values"
                print "ACTUAL RESULT 6:%s" %details
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 6:Revert the PublicWiFi param values"
                print "TEST STEP 6 : Should revert the PublicWiFi param values"
                print "ACTUAL RESULT 6:%s" %details
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Enable public wifi"
            print "TEST STEP 2 : Should enable PublicWiFi"
            print "ACTUAL RESULT 2:%s" %details
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:Get values of PublicWiFi params"
        print "TEST STEP 1 : Should get values of PublicWiFi params"
        print "ACTUAL RESULT 1:%s" %orgValue
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent");

else:
        print "Failed to load wifi module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
