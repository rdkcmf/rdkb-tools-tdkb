##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <version>10</version>
  <name>TS_TAD_AddandDeleteIPv4PingServerTable</name>
  <primitive_test_id/>
  <primitive_test_name>TADstub_Set</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if adding a new IPv4 Ping Server table using Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTable. is success and the the IPv4 Ping Server URI parameter of the newly created instance has the default value as empty. Verify if setting an IPv4 address to the Ping Server URI is success and check if the deletion of the created instance is successful.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TAD_82</test_case_id>
    <test_objective>Check if adding a new IPv4 Ping Server table using Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTable. is success and the the IPv4 Ping Server URI parameter of the newly created instance has the default value as empty. Verify if setting an IPv4 address to the Ping Server URI is success and check if the deletion of the created instance is successful.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTable.
ParamName : Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTable.{instance}.X_RDKCENTRAL-COM_Ipv4PingServerURI
ParamValue : 8.8.8.8
Type : string</input_parameters>
    <automation_approch>1.Load the modules
2. Create a new IPv4 Ping Server instance using Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTable.
3. Verify if the instance created is valid
4. Check if the default value of the IPv4 Ping Server URI created is empty using Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTable.{instance}.X_RDKCENTRAL-COM_Ipv4PingServerURI
5. Set Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTable.{instance}.X_RDKCENTRAL-COM_Ipv4PingServerURI to a new IPv4 value and cross check with the GET
6. Delete the newly created instance
7. Unload the modules</automation_approch>
    <expected_output>IPv4 Ping Server table should be created successfully, URIs set should reflect in GET and the created instance should be deleted successfully.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_TAD_AddandDeleteIPv4PingServerTable</test_script>
    <skipped>No</skipped>
    <release_version>M102</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *
from tdkutility import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1 = tdklib.TDKScriptingLibrary("tad","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_AddandDeleteIPv4PingServerTable');
obj1.configureTestCase(ip,port,'TS_TAD_AddandDeleteIPv4PingServerTable');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    #Add a new IPv4 Ping Server Table Object
    step = 1;
    tdkTestObj = obj.createTestStep("TDKB_TR181Stub_AddObject");
    tdkTestObj.addParameter("paramName","Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTable.");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Add a new IPv4 Ping Server Table instance" %step;
    print "EXPECTED RESULT %d: Should add a new IPv4 Ping Server Table instance successfully" %step;

    if expectedresult in actualresult and details != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Added a new IPv4 Ping Server Table instance successfully; Details : %s" %(step, details);
        print "TEST EXECUTION RESULT : %s" %actualresult;
        instance = details.split(':')[1];

        if instance.isdigit() and int(instance) > 0:
            tdkTestObj.setResultStatus("SUCCESS");
            print "INSTANCE VALUE : %s" %instance;

            #Check default value of the newly added entry Ipv4 Ping Serve URI
            step = step + 1;
            sleep(5);
            ping_uri = "Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTable." + instance + ".X_RDKCENTRAL-COM_Ipv4PingServerURI";

            tdkTestObj = obj1.createTestStep("TADstub_Get");
            tdkTestObj.addParameter("paramName",ping_uri);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult1 = tdkTestObj.getResult();
            details1 = tdkTestObj.getResultDetails();

            print "\nTEST STEP %d : Get the default value of %s and check if it is empty" %(step, ping_uri);
            print "EXPECTED RESULT %d : The default value retrived should be empty" %step;

            if expectedresult in actualresult1:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : The default value of the newly added instance retrieved successfully" %step;
                print "%s : %s" %(ping_uri, details1);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                if details1 == "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "The default value of the new IPv4 Ping Server Table instance - %s is empty as expected" %(ping_uri);

                    #Check if are able to set a new IPV4 value
                    ipv4_addr = "8.8.8.8";
                    step = step + 1;
                    tdkTestObj = obj.createTestStep("TDKB_TR181Stub_SetOnly");
                    tdkTestObj.addParameter("ParamName",ping_uri);
                    tdkTestObj.addParameter("ParamValue",ipv4_addr);
                    tdkTestObj.addParameter("Type","string");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult1 = tdkTestObj.getResult();
                    details1 = tdkTestObj.getResultDetails();

                    print "\nTEST STEP %d : Set value for %s to %s" %(step, ping_uri, ipv4_addr);
                    print "EXPECTED RESULT %d : The value should be set successfully" %step;

                    if expectedresult in actualresult1:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : The IPv4 Ping Server URI of the newly added instance set successfully" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Cross check the SET value with GET
                        step = step + 1;
                        tdkTestObj = obj1.createTestStep("TADstub_Get");
                        tdkTestObj.addParameter("paramName",ping_uri);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult1 = tdkTestObj.getResult();
                        details1 = tdkTestObj.getResultDetails();

                        print "\nTEST STEP %d : Get the value of %s and check if it is same as set value" %(step, ping_uri);
                        print "EXPECTED RESULT %d : The value should be retrieved successfully and it should be the same as set value" %step;

                        if expectedresult in actualresult1:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d : The value of the newly added instance retrieved successfully" %step;
                            print "%s : %s" %(ping_uri, details1);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            if details1 == ipv4_addr:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "The value of the new IPv4 ping Server Table instance - %s is %s as expected" %(ping_uri, details1);
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "The GET value of the new IPv4 ping Server instance is not as expected";
                        else :
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d : Failed to retrieve the newly added Table instance value" %step;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : The IPv4 Ping Server URI of the newly added instance NOT set successfully" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "The default value of the new IPv4 Ping Server Table instance is not as expected";
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : Failed to retrieve the new IPv4 Ping Server Table instance value" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            #Delete the added instance from the CSI Table
            step = step + 1;
            tdkTestObj = obj.createTestStep("TDKB_TR181Stub_DelObject");
            tdkTestObj.addParameter("paramName","Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTable.%s." %instance);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP %d : Delete the newly added IPv4 Ping Server Table instance" %step;
            print "EXPECTED RESULT %d: Should delete the newly added IPv4 Ping Server Table instance successfully" %step;

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : New instance deleted successfully; Details : %s" %(step, details);
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Added instance is deleted successfully";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : New instance NOT deleted successfully; Details : %s" %(step, details);
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Added instance could not be deleted";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "INSTANCE VALUE : %s is not a valid value" %instance
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Unable to add a new instance to IPv4 Ping Server Table; Details : %s" %(step, details);
        print "TEST EXECUTION RESULT : FAILURE";

    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("tad");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
