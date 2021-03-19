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
  <version>3</version>
  <name>TS_WANMANAGER_CheckCPEInterfaceNameAndDisplayName</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check the Wan Manager CPE Interfaces name and Display Name have the expected values</synopsis>
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
    <test_case_id>TC_WANMANAGER_03</test_case_id>
    <test_objective>This test case is to check the Wan Manager CPE Interfaces name and Display Name have the expected values</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub</api_or_interface_used>
    <input_parameters>Device.X_RDK_WanManager.CPEInterfaceNumberOfEntries
Device.X_RDK_WanManager.CPEInterface.{i}.Name
Device.X_RDK_WanManager.CPEInterface.{i}.DisplayName</input_parameters>
    <automation_approch>1]Load the module
2] Get the number of CPE interfaces
3] Get the CPE interface Name and Display Name and check if the value associated are as expected
interfaceName - dsl0, eth3, veip0
displayName  -  DSL,WANOE,GPON
4]Unload the module</automation_approch>
    <expected_output>CPE interface Name and Display Name should be associated with names as expected</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_CheckCPEInterfaceNameAndDisplayName</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from WanManager_Utility import *;
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_CheckCPEInterfaceNameAndDisplayName');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterfaceNumberOfEntries");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        noOfEntries = int(details);
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 :Get the number of CPE Interfaces";
        print "EXPECTED RESULT 1: Should get the no of CPE Interfaces";
        print "ACTUAL RESULT 1: The value received is :",noOfEntries;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        print "TEST STEP 2:Check if CPE interface name and display name are as expected";

        print "Expected CPE interface names is %s" %interfaceName;
        print "Expected CPE display names is %s" %displayName;
        n = noOfEntries;
        flag = 0;
        for interface in range(1,noOfEntries+1):
            i=0;
            for inter in range(0,noOfEntries):
                expectedresult="SUCCESS";
                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.%i.Name" %interface);
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and details == interfaceName[inter]:
                    flag =1;
                    tdkTestObj.setResultStatus("SUCCESS");
                    print"Device.X_RDK_WanManager.CPEInterface.%i.Name is %s" %(interface,details);
                    break;
            if flag == 1:
                intr =inter+1;
                expectedresult="SUCCESS";
                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.%i.DisplayName" %intr);
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and details == displayName[inter]:
                    flag = 1;
                    tdkTestObj.setResultStatus("SUCCESS");
                    print"Device.X_RDK_WanManager.CPEInterface.%i.DisplayName is %s which is a expected value" %(intr,details);
                else:
                    flag = 0;
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Display Name of CPE interace Device.X_RDK_WanManager.CPEInterface.%i.DisplayName is %s but expected is %s"%(intr,details,displayName[i]);
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "The CPE interface name is %s which is not among the listed interface name" %details;
        # setting the script status
        if flag ==1:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Listed CPE interfaces have expected Display name and interafce name";
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: Listed CPE interfaces does not have expected Display name and interafce name";
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1 :Get the number of CPE Interfaces";
        print "EXPECTED RESULT 1: Should get the no of CPE Interfaces";
        print "ACTUAL RESULT 1: The value received is :",noOfEntries;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
