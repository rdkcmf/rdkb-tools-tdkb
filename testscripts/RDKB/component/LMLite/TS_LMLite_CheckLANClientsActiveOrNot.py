##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_LMLite_CheckLANClientsActiveOrNot</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>LMLiteStub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>If the Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber is greater than zero, then clients connected should be active</synopsis>
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

  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_LMLite_09</test_case_id>
    <test_objective>If the Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber is greater than zero, then clients connected should be active</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>LMLiteStub_Get,LMLiteStub_Set</api_or_interface_used>
    <input_parameters>Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber
"Device.Hosts.HostNumberOfEntries"
Device.Hosts.Host.%d.Active</input_parameters>
    <automation_approch>1. Load Lmlite modules
2. From script invoke LMLiteStub_Get to get the number of connected devices.
3. if it is greater than zero , check whether the clients are active or not
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from lmlite stub</automation_approch>
    <except_output>CheckPoint 1:
 The output  should be logged in the Agent console/Component log

CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_LMLite_CheckClientsActiveOrNot</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("lmlite","1");
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LMLite_CheckLANClientsActiveOrNot');
wifiobj.configureTestCase(ip,port,'TS_LMLite_CheckLANClientsActiveOrNot');

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

        #Get the number of clients connected. Should be greater than zero
        tdkTestObj = obj.createTestStep('LMLiteStub_Get');
        tdkTestObj.addParameter("paramName","Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber");
        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        NoOfClients = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and int(NoOfClients)>0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the number of active clients connected";
            print "EXPECTED RESULT 1: Should get the number of active clients connected as greater than zero";
            print "ACTUAL RESULT 1: Number of active clients connected :%s" %NoOfClients;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj.createTestStep('LMLiteStub_Get');
            tdkTestObj.addParameter("paramName","Device.Hosts.HostNumberOfEntries");
            expectedresult="SUCCESS";

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            NoOfHosts = tdkTestObj.getResultDetails();

            if expectedresult in actualresult and int(NoOfHosts)>0:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Get the number of hosts";
                print "EXPECTED RESULT 2: Should get the number of hosts";
                print "ACTUAL RESULT 2: Number of hosts:%s" %NoOfHosts;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                #Find the active hosts amoung the listed Hosts. List will contains the ids of active hosts
                List=[];
                for i in range(1,int(NoOfHosts)+1):
                    tdkTestObj.addParameter("paramName","Device.Hosts.Host.%d.Active" %i);
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    Status = tdkTestObj.getResultDetails();
                    if "true" in Status:
                        List.extend(str(i));
                if expectedresult in actualresult and len(List)== int(NoOfClients):
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Get the active clients List";
                    print "EXPECTED RESULT 3: The number of items in the active client list should be same as ConnectedDeviceNumber";
                    print "ACTUAL RESULT 3: Active clients are :",List;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
	        else:
	            #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Get the active clients List";
                    print "EXPECTED RESULT 3: The number of items in the active client list should be same as ConnectedDeviceNumber";
                    print "ACTUAL RESULT 3: Active clients are :",List;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Get the number of hosts";
                print "EXPECTED RESULT 2: Should get the number of hosts";
                print "ACTUAL RESULT 2: Number of hosts:%s" %NoOfHosts;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the number of hosts";
            print "EXPECTED RESULT 1: Should get the number of hosts";
            print "ACTUAL RESULT 1: Number of hosts:%s" %NoOfClients;
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

