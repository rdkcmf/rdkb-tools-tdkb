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
  <name>TS_WIFIHAL_5GHzSetSecurityRadiusServer</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetSecurityRadiusServer</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the SecurityRadiusServer details  for 5GHz</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_181</test_case_id>
    <test_objective>To set and get the SecurityRadiusServer details  for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurityRadiusServer()
wifi_setApSecurityRadiusServer()
wifi_getApSecurityModeEnabled()
wifi_setApSecurityModeEnabled()</api_or_interface_used>
    <input_parameters>methodName : getApSecurityRadiusServer
methodName : setApSecurityRadiusServer
methodName : getApSecurityModeEnabled
methodName : setApSecurityModeEnabled
ApIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamStringValue invoke wifi_getApSecurityModeEnabled() and save the get value
3. If the mode is Enterprise type go to step 5
4. If mode is not Enterprise mode, invoke wifi_setApSecurityModeEnabled using  WIFIHAL_GetOrSetParamStringValue and set any Enterprise mode
5. Using  WIFIHAL_GetOrSetSecurityRadiusServer invoke wifi_getApSecurityRadiusServer() and save the value
6. Using  WIFIHAL_GetOrSetSecurityRadiusServer invoke wifi_setApSecurityRadiusServer() and set any values for IPaddress, port and RadiusSecret
7. Invoke wifi_getApSecurityRadiusServer() to get the previously set value. 
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
6. Revert the RadiusServer and ModeEnabled back to initial value
7. Unload wifihal module</automation_approch>
    <except_output>Set and get values of RadiusServer (IP address, port and RadiusSecret) should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetSecurityRadiusServer</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetSecurityRadiusServer');

def GetorSetApSecurityRadiusServer(obj, primitive, radioIndex, IPAddress, port, RadiusSecret, methodname):
    #Prmitive test case which associated to this Script
    tdkTestObj = obj.createTestStep(primitive);
    #Radio index is 0 for 2.4GHz and 1 for 5GHz
    tdkTestObj.addParameter("radioIndex",radioIndex);
    tdkTestObj.addParameter("methodName", methodname);
    tdkTestObj.addParameter("IPAddress", IPAddress);
    tdkTestObj.addParameter("port", port);
    tdkTestObj.addParameter("RadiusSecret", RadiusSecret);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    return (tdkTestObj, actualresult, details);

def checkApSecurityRadiusServer():
    expectedresult = "SUCCESS";
    radioIndex = 1
    getMethod = "getApSecurityRadiusServer"
    primitive = "WIFIHAL_GetOrSetSecurityRadiusServer"

    #Calling the method to execute wifi_getApSecurityRadiusServer()
    tdkTestObj, actualresult, details = GetorSetApSecurityRadiusServer(obj, primitive, radioIndex, "0", 0, "0", getMethod)

    if expectedresult in actualresult:
        output  = details.split(":")[1].strip()
        initDetails = output.split(",")
        initValues = [i.split("=",1)[1] for i in initDetails]
        #Checking if all the output values are non emtpy
        if all(initValues):
            print "TEST STEP 1: Get the ApSecurityRadiusServer details"
            print "EXPECTED RESULT 1: Should get the IPAddress, port and RadiusSecret as non empty values"
            print "ACTUAL RESULT 1: Obtained the IPAddress, port and RadiusSecret as a NON EMPTY values"
            print "ApSecurityRadiusServer details : %s"%output
            tdkTestObj.setResultStatus("SUCCESS");

            expectedresult = "SUCCESS";
            radioIndex = 1
            setMethod = "setApSecurityRadiusServer"
            primitive = "WIFIHAL_GetOrSetSecurityRadiusServer"
            IPAddress = "1.1.2.2"
            port = 1234
            RadiusSecret = "12345"

            #Calling the method to execute wifi_setApSecurityRadiusServer()
            tdkTestObj, actualresult, details = GetorSetApSecurityRadiusServer(obj, primitive, radioIndex, IPAddress, port, RadiusSecret, setMethod)

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set the ApSecurityRadiusServer details"
                print "EXPECTED RESULT 2: Should set the IPAddress, port and RadiusSecret"
                print "ACTUAL RESULT 2: Successfully set the IPAddress, port and RadiusSecret"
                print "Set values: IPAddress = 1.1.2.2, port = 1234, RadiusSecret = 12345"

                expectedresult = "SUCCESS";
                radioIndex = 1
                getMethod = "getApSecurityRadiusServer"
                primitive = "WIFIHAL_GetOrSetSecurityRadiusServer"

                #Calling the method to execute wifi_getApSecurityRadiusServer()
                tdkTestObj, actualresult, details = GetorSetApSecurityRadiusServer(obj, primitive, radioIndex, "0", 0, "0", getMethod)

                if expectedresult in actualresult:
                    output  = details.split(":")[1].strip()
                    outputDetails = output.split(",")
                    outputValues = [i.split("=",1)[1] for i in outputDetails]
                    if outputValues == [IPAddress, str(port), RadiusSecret]:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3: Comparing the set and get values of ApSecurityRadiusServer deatils"
                        print "EXPECTED RESULT 3: Set and get values should be the same"
                        print "ACTUAL RESULT 3: Set and get values are the same"
                        print "Set values: IPAddress = 1.1.2.2, port = 1234, RadiusSecret = 12345"
                        print "Get values: IPAddress = ",outputValues[0],"port = ",outputValues[1],"RadiusSecret = ",outputValues[2]
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Comparing the set and get values of ApSecurityRadiusServer deatils"
                        print "EXPECTED RESULT 3: Set and get values should be the same"
                        print "ACTUAL RESULT 3: Set and get values are NOT the same"
                        print "Set values: IPAddress = 1.1.2.2, port = 1234, RadiusSecret = 12345"
                        print "Get values: IPAddress = ",outputValues[0],"port = ",outputValues[1],"RadiusSecret = ",outputValues[2]
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "wifi_getApSecurityRadiusServer() call failed"

                #Reverting the values to previous value
                expectedresult = "SUCCESS";
                radioIndex = 1
                setMethod = "setApSecurityRadiusServer"
                primitive = "WIFIHAL_GetOrSetSecurityRadiusServer"
                IPAddress = initValues[0];
                port = int(initValues[1]);
                RadiusSecret = initValues[2];

                #Calling the method to execute wifi_setApSecurityRadiusServer()
                tdkTestObj, actualresult, details = GetorSetApSecurityRadiusServer(obj, primitive, radioIndex, IPAddress, port, RadiusSecret, setMethod)

                if expectedresult in actualresult:
                    print "Successfully reverted to initial values"
                    tdkTestObj.setResultStatus("SUCCESS");
                else:
                    print " Unable to revert to initial value"
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Set the ApSecurityRadiusServer details"
                print "EXPECTED RESULT 2: Should set the IPAddress, port and RadiusSecret"
                print "ACTUAL RESULT 2: Failed to set the IPAddress, port and RadiusSecret"
        else:
            print "TEST STEP 1: Get the ApSecurityRadiusServer details"
            print "EXPECTED RESULT 1: Should get the IPAddress, port and RadiusSecret as non empty values"
            print "ACTUAL RESULT 1: Obtained the IPAddress, port and RadiusSecret as an EMPTY values"
            print "ApSecurityRadiusServer details : %s"%output
            tdkTestObj.setResultStatus("FAILURE");

    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "wifi_getApSecurityRadiusServer() call failed"

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    compatibleModes = ["WPA-Enterprise", "WPA2-Enterprise", "WPA-WPA2-Enterprise"]

    expectedresult="SUCCESS";
    apIndex = 1
    getMethod = "getApSecurityModeEnabled"
    primitive = 'WIFIHAL_GetOrSetParamStringValue'

    #Calling the method to execute wifi_getApSecurityModeEnabled()
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)

    if expectedresult in actualresult:
        initMode = details.split(":")[1].strip()
        if initMode not in compatibleModes:
            expectedresult="SUCCESS";
            apIndex = 1
            setMethod = "setApSecurityModeEnabled"
            primitive = 'WIFIHAL_GetOrSetParamStringValue'
            setMode = compatibleModes[0]

            #Calling the method to execute wifi_setApSecurityModeEnabled()
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ModeEnabled is changed to an Enterprise type"

                #Calling the function to perform the settings and getting and verification of SecurityRadiusServer
                checkApSecurityRadiusServer();

                #Revert to initial mode
                apIndex = 1
                setMethod = "setApSecurityModeEnabled"
                primitive = 'WIFIHAL_GetOrSetParamStringValue'
                setMode = initMode

                #Calling the method to execute wifi_setApSecurityModeEnabled()
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setMode, setMethod)

                if expectedresult in actualresult:
                    print "Successfully reverted the SecurityMode to initial value"
                    tdkTestObj.setResultStatus("SUCCESS");
                else:
                    print "Unable to revert the SecurityMode to initial value"
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Unable to change ModeEnabled to Enterprise type"
        else:
	    #Calling the function to perform the settings and getting and verification of SecurityRadiusServer
            checkApSecurityRadiusServer();
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "wifi_getApSecurityModeEnabled()call failed"

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

