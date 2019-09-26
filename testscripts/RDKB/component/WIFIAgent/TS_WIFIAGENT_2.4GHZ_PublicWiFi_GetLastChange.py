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
  <name>TS_WIFIAGENT_2.4GHZ_PublicWiFi_GetLastChange</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Toggle the SSID status of 2.4GHZ public wifi and check whether the value of LastChange 	is changed or not</synopsis>
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
    <test_case_id>TC_WIFIAGENT_62</test_case_id>
    <test_objective>Toggle the SSID status of 2.4GHZ public wifi and check whether the value of LastChange 	is changed or not</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>"Device.WiFi.SSID.5.LastChange"
"Device.WiFi.SSID.5.Enable"</input_parameters>
    <automation_approch>1. Load wifiagent module
2. Using WIFIAgent_Get, get and save Device.WiFi.SSID.5.LastChange and Device.WiFi.SSID.5.Enable
3. Toggle the value of Device.WiFi.SSID.5.Enable
4. Using WIFIAgent_Get, get Device.WiFi.SSID.5.LastChange and check if it is changed
5. Restore value of Device.WiFi.SSID.5.Enable</automation_approch>
    <except_output>The Last Change must be changed to a lower value when enable status is changed</except_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_WIFIAGENT_2.4GHZ_PublicWiFi_GetLastChange</test_script>
    <skipped>No</skipped>
    <release_version>M58</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from xfinityWiFiLib import *
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_2.4GHZ_PublicWiFi_GetLastChange');

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

	    sleep(60);
	    #Get the value of LastChange
	    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.WiFi.SSID.5.LastChange")
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            LastChange = details.split("VALUE:")[1].split(' ')[0];

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the Last Change";
                print "EXPECTED RESULT 3: Should get the Last Change";
                print "ACTUAL RESULT 3: Last Change is %s" %LastChange;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

		#Get the current status of SSID5
		tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                tdkTestObj.addParameter("paramName","Device.WiFi.SSID.5.Enable")
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                Status = details.split("VALUE:")[1].split(' ')[0];

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Get the SSID Status";
                    print "EXPECTED RESULT 4: Should get the SSID Status";
                    print "ACTUAL RESULT 4: Status is %s" %Status;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
		    if "true" in Status:
			value = "false";
		    else:
			value = "true";

		    #Toggle the SSID5 Status
		    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                    tdkTestObj.addParameter("paramName","Device.WiFi.SSID.5.Enable")
                    tdkTestObj.addParameter("paramValue",value)
                    tdkTestObj.addParameter("paramType","boolean")
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Toggle the SSID status";
                        print "EXPECTED RESULT 5: SSID status should change"
                        print "ACTUAL RESULT 5: %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

			#Get the current LastChange and check if it is less than previous value
			tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            		tdkTestObj.addParameter("paramName","Device.WiFi.SSID.5.LastChange")
            		tdkTestObj.executeTestCase(expectedresult);
            		actualresult = tdkTestObj.getResult();
            		details = tdkTestObj.getResultDetails();
            		NewLastChange = details.split("VALUE:")[1].split(' ')[0];

            		if expectedresult in actualresult and int(NewLastChange) < int(LastChange):
            		    tdkTestObj.setResultStatus("SUCCESS");
            		    print "TEST STEP 6: Get the Last Change";
            		    print "EXPECTED RESULT 6: Current Last change must be less than the previous value";
            		    print "ACTUAL RESULT 6: Last Change is %s" %NewLastChange;
            		    #Get the result of execution
            		    print "[TEST EXECUTION RESULT] : SUCCESS";

			else:
			    tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6: Get the Last Change";
                            print "EXPECTED RESULT 6: Current Last change must be less than the previous value";
                            print "ACTUAL RESULT 6: Last Change is %s" %NewLastChange;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
			#Revert the SSID Status
			tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                        tdkTestObj.addParameter("paramName","Device.WiFi.SSID.5.Enable")
                        tdkTestObj.addParameter("paramValue",Status)
                        tdkTestObj.addParameter("paramType","boolean")
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 7: Revert the SSID status";
                            print "EXPECTED RESULT 7: SSID status should revert"
                            print "ACTUAL RESULT 7: %s " %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
			else:
			    #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 7: Revert the SSID status";
                            print "EXPECTED RESULT 7: SSID status should revert"
                            print "ACTUAL RESULT 7: %s " %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
		    else:
			tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Toggle the SSID status";
                        print "EXPECTED RESULT 5: SSID status should change"
                        print "ACTUAL RESULT 5: %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
		else:
		    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Get the SSID Status";
                    print "EXPECTED RESULT 4: Should get the SSID Status";
                    print "ACTUAL RESULT 4: Status is %s" %Status;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
		tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the Last Change";
                print "EXPECTED RESULT 3: Should get the Last Change";
                print "ACTUAL RESULT 3: Last Change is %s" %LastChange;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
            #Revert the values of public wifi params
            tdkTestObj, actualresult, details = setPublicWiFiParamValues(obj,orgValue);
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 8:Revert the PublicWiFi param values"
                print "TEST STEP 8 : Should revert the PublicWiFi values"
                print "ACTUAL RESULT 8:%s" %details
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 8:Revert the PublicWiFi param values"
                print "TEST STEP 8 : Should revert the PublicWiFi param values"
                print "ACTUAL RESULT 8:%s" %details
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
