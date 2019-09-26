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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>6</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_LMLite_CheckHostNumberOfEntries_InBridgeMode</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>LMLiteStub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>If gateway is in bridge mode, Device.Hosts.HostNumberOfEntries should be zero</synopsis>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_LMLite_11</test_case_id>
    <test_objective>If getway is in bridge mode, Device.Hosts.HostNumberOfEntries should be zero</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>LMLiteStub_Get</api_or_interface_used>
    <input_parameters>Device.Hosts.HostNumberOfEntries
Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode</input_parameters>
    <automation_approch>1. Load Lmlite modules
2. From script invoke LMLiteStub_Get to get the number of hosts.
3. Check if the device is in bridge mode or not
4.if it is bridge mode number of hosts should be zero
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from lmlite stub.</automation_approch>
    <except_output>CheckPoint 1:
 The output  should be logged in the Agent console/Component log

CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_LMLite_CheckHostNumberOfEntries_IfBridgeMode</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("lmlite","1");
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LMLite_CheckHostNumberOfEntries_InBridgeMode');
wifiobj.configureTestCase(ip,port,'TS_LMLite_CheckHostNumberOfEntries_InBridgeMode');
#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
wifiloadmodulestatus=wifiobj.getLoadModuleResult();

if "SUCCESS" in (loadmodulestatus.upper() and wifiloadmodulestatus.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    #Disable WiFi before testing LMLite features
    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.WiFi.SSID.1.Enable");
    tdkTestObj.addParameter("paramValue","false");
    tdkTestObj.addParameter("paramType","boolean");

    expectedresult="SUCCESS"
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult1 = tdkTestObj.getResult();
    Details = tdkTestObj.getResultDetails();

    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.WiFi.SSID.2.Enable");
    tdkTestObj.addParameter("paramValue","false");
    tdkTestObj.addParameter("paramType","boolean");

    expectedresult="SUCCESS"
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult2 = tdkTestObj.getResult();
    Details = tdkTestObj.getResultDetails();
    if expectedresult in (actualresult1 and actualresult2):
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP : Disable WiFi before testing LMLite features";
        print "EXPECTED RESULT : Should disable WiFi";
        print "ACTUAL RESULT :%s" %Details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check if device is in bridge mode or not
        tdkTestObj = obj.createTestStep('LMLiteStub_Get');
        tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode");
        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        Current_Mode = tdkTestObj.getResultDetails();
        if "router" not in Current_Mode:
            Mode = "bridge mode";
        else:
            Mode = "Router mode"

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Check if the device is in bridge mode or not";
            print "EXPECTED RESULT 1: Should get the mode of device";
            print "ACTUAL RESULT 1:  :LanMode is %s" %Mode;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            if "bridge mode" not in Mode:
                tdkTestObj = obj.createTestStep('LMLiteStub_Set');
                tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode");
                tdkTestObj.addParameter("ParamValue","bridge-static");
                tdkTestObj.addParameter("Type","string");
                expectedresult="SUCCESS";

                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Set the LanMode as bridge ";
                    print "EXPECTED RESULT 2: Should set the LanMode as bridge mode";
                    print "ACTUAL RESULT 2:  : %s" %details;
                    Mode = "bridge mode";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 2: Set the LanMode as bridge ";
                    print "EXPECTED RESULT 2: Should set the LanMode as bridge mode";
                    print "ACTUAL RESULT 2:  : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    obj.unloadModule("lmlite");
                    exit();

            #Wait for few seconds for the Lan mode to get reflected
	    sleep(30);

            tdkTestObj = obj.createTestStep('LMLiteStub_Get');
            tdkTestObj.addParameter("paramName","Device.Hosts.HostNumberOfEntries");
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            NoOfHosts = tdkTestObj.getResultDetails();
	    print "Lan Mode retrieved is: %s" %Mode;
            if expectedresult in actualresult:
                if "bridge mode" in Mode and int(NoOfHosts) == 0:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3:Check the number of hosts";
                    print "EXPECTED RESULT 3: The number of hosts should be zero if device is in bridge mode";
                    print "ACTUAL RESULT 3:  :No of hosts is %s" %NoOfHosts;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3:Check the number of hosts";
                    print "EXPECTED RESULT 3: The number of hosts should be zero if device is in bridge mode";
                    print "ACTUAL RESULT 3:  :No of hosts is %s" %NoOfHosts;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2:Get the number of hosts";
                print "EXPECTED RESULT 2: Should get the number of hosts";
                print "ACTUAL RESULT 2:  :No of Hosts is %s" %NoOfHosts;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
            #set default LanMode
            tdkTestObj = obj.createTestStep('LMLiteStub_Set');
            tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode");
            tdkTestObj.addParameter("ParamValue",Current_Mode);
            tdkTestObj.addParameter("Type","string");
            expectedresult="SUCCESS";

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP : Set the LanMode to default ";
                print "EXPECTED RESULT : Should set the LanMode as default value";
                print "ACTUAL RESULT : %s" %details;
                Mode = "bridge mode";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                #Wait for few seconds for the Lan mode to get reflected
                sleep(70);
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : Set the LanMode to default ";
                print "EXPECTED RESULT : Should set the LanMode as default value";
                print "ACTUAL RESULT : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Check if the device is in bridge mode or not";
            print "EXPECTED RESULT 1: Should get the mode of device";
            print "ACTUAL RESULT 1:  :LanMode is %s" %Current_Mode;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        #Enabling WiFi before exiting the test
        tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
        tdkTestObj.addParameter("paramName","Device.WiFi.SSID.1.Enable");
        tdkTestObj.addParameter("paramValue","true");
        tdkTestObj.addParameter("paramType","boolean");

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult1 = tdkTestObj.getResult();
        Details = tdkTestObj.getResultDetails();

	tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
        tdkTestObj.addParameter("paramName","Device.WiFi.SSID.2.Enable");
        tdkTestObj.addParameter("paramValue","true");
        tdkTestObj.addParameter("paramType","boolean");

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult2 = tdkTestObj.getResult();
        Details = tdkTestObj.getResultDetails();

        if expectedresult in (actualresult1 and actualresult2):
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP : Enable WiFi before exiting test";
            print "EXPECTED RESULT : Should enable WiFi";
            print "ACTUAL RESULT :%s" %Details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Enable WiFi before exiting test";
            print "EXPECTED RESULT : Should enable WiFi";
            print "ACTUAL RESULT :%s" %Details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Disable WiFi before testing LMLite features";
        print "EXPECTED RESULT : Should disable WiFi";
        print "ACTUAL RESULT :%s" %Details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("lmlite");
    wifiobj.unloadModule("wifiagent");

else:
    print "Failed to load lmlite module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
