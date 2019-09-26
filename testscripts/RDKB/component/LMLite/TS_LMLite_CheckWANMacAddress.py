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
  <name>TS_LMLite_CheckWANMacAddress</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>LMLiteStub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check whether the WAN Mac address is same as the value of Device.Hosts.Host.1.X_RDKCENTRAL-COM_Parent</synopsis>
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
    <test_case_id>TC_LMLite_13</test_case_id>
    <test_objective>To check whether the WAN Mac address is same as the value of Device.Hosts.Host.1.X_RDKCENTRAL-COM_Parent</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>LMLiteStub_Get,LMLiteStub_Set, ExecuteCmd</api_or_interface_used>
    <input_parameters>Device.Hosts.X_CISCO_COM_ConnectedDeviceNumber
Device.Hosts.HostNumberOfEntries
Device.Hosts.Host.%d.Active
Device.Hosts.Host.%d.X_RDKCENTRAL-COM_Parent</input_parameters>
    <automation_approch>1. Load Lmlite modules
2. From script invoke LMLiteStub_Get to get the number of connected devices.
3. If it is greater than zero get the wan address from box and through namespace
4.both should be same
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
    <test_script>TS_LMLite_CheckWANMacAddress</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import snmplib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("lmlite","1");
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LMLite_CheckWANMacAddress');
wifiobj.configureTestCase(ip,port,'TS_LMLite_CheckWANMacAddress');
sysObj.configureTestCase(ip,port,'TS_LMLite_CheckWANMacAddress');

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
        print "TEST STEP 1: Disable WiFi before testing LMLite features";
        print "EXPECTED RESULT 1: Should disable WiFi";
        print "ACTUAL RESULT 1:%s" %Details;
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
            print "TEST STEP 2: Get the number of active clients connected";
            print "EXPECTED RESULT 2: Should get the number of active clients connected as greater than zero";
            print "ACTUAL RESULT 2: Number of active clients connected :%s" %NoOfClients;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Get the wan MAC Address from DUT
            macaddress = " ";
            macaddress = snmplib.getMACAddress(sysObj);
            if macaddress != " " :
                macaddress = macaddress.strip().upper();
                print "TEST STEP 3:Get WAN mac from DUT";
                print "EXPECTED RESULT 3: Should get WAN mac from DUT";
                print "ACTUAL RESULT 3: WAN mac is %s" %macaddress;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS" ;

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
                    print "TEST STEP 4: Get the number of hosts";
                    print "EXPECTED RESULT 4: Should get the number of hosts";
                    print "ACTUAL RESULT 4: Number of hosts :%s" %NoOfHosts;
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
                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Get the active clients";
                        print "EXPECTED RESULT 5: Should get the active clients";
                        print "ACTUAL RESULT 5: Active clients are :",List;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        #compare the MACs obtained
                        ret =0;
                        for i in range(0,len(List)):
                            n = int(List[i]);
                            tdkTestObj.addParameter("paramName","Device.Hosts.Host.%d.X_RDKCENTRAL-COM_Parent" %n);
                            #Execute the test case in DUT
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            wanMac = tdkTestObj.getResultDetails();
                            wanMac = wanMac.upper();
                            print "WAN Address in Device.Hosts.: %s" %wanMac;
			    print "WAN Address retrieved via Cable Modem: %s" %macaddress;
                            if wanMac == macaddress:
                                print "Wan MAC of host instance ",n," matches";
                            else:
                                print "Wan MAC of host instance ",n," doesnt match";
                                ret = 1
                        if expectedresult in actualresult and ret ==0:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 5: Compare the WAN MACs obtained";
                            print "EXPECTED RESULT 5: Both MACs should match";
                            print "ACTUAL RESULT 5: The WAN MACs matched successfully";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 5: Compare the WAN MACs obtained";
                            print "EXPECTED RESULT 5: Both MACs should match";
                            print "ACTUAL RESULT 5: The WAN MACs are not matching";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Get the active clients";
                        print "EXPECTED RESULT 4: Should get the active cleints";
                        print "ACTUAL RESULT 4: FAiled to get the active clients";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 2: Get the number of hosts";
                    print "EXPECTED RESULT 1: Should get the number of hosts";
                    print "ACTUAL RESULT 1: Number of hosts :%s" %NoOfHosts;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                details = tdkTestObj.getResultDetails();
                print "TEST STEP 3:Should get the WAN MAC address";
                print "EXPECTED RESULT 3: Should get the WAN MAC address";
                print "ACTUAL RESULT 3: %s" %macaddress;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the number of active clients connected";
            print "EXPECTED RESULT 2: Should get the number of active clients connected as greater than zero";
            print "ACTUAL RESULT 2: Number of active clients connected :%s" %NoOfClients;
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
        print "TEST STEP 1: Disable WiFi before testing LMLite features";
        print "EXPECTED RESULT 1: Should disable WiFi";
        print "ACTUAL RESULT 1:%s" %Details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("lmlite");
    wifiobj.unloadModule("wifiagent");
else:
    print "Failed to load lmlite module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

