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
  <version>2</version>
  <name>TS_WANMANAGER_CheckWANTypeForListedInterfaces</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if all the interface's have a valid WAN Type</synopsis>
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
    <test_case_id>TC_WANMANAGER_02</test_case_id>
    <test_objective>This test case is to check if all the interface's have a valid WAN Type</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub</api_or_interface_used>
    <input_parameters>Device.X_RDK_WanManager.CPEInterfaceNumberOfEntries
Device.X_RDK_WanManager.CPEInterface.{i}.Wan.Type</input_parameters>
    <automation_approch>1] Load the module
2]Get the number of CPE Interfaces present
3]Get WAN Type for each of the CPE interfaces
4] Check if WAN Type is one among UNCONFIGURED, PRIMARY, SECONDARY
5]Unload the module
</automation_approch>
    <expected_output>All the CPE interfaces should have a valid WAN Type</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_CheckWANTypeForListedInterfaces</test_script>
    <skipped>No</skipped>
    <release_version>M87</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_CheckWANTypeForListedInterfaces');

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
        if noOfEntries> 0 :
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 1 :Get the number of CPE Interfaces";
           print "EXPECTED RESULT 1: Should get the no of CPE Interfaces greater than zero";
           print "ACTUAL RESULT 1: The value received is :",noOfEntries;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";

           statusFlag = 0;
           print "TEST STEP 2:Checking if CPE interfaces has a valid WAN Type";
           expectedWANType = ["UNCONFIGURED", "PRIMARY", "SECONDARY"];
           while noOfEntries > 0:
                 expectedresult="SUCCESS";
                 tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                 tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.%i.Wan.Type" %noOfEntries);
                 #Execute the test case in DUT
                 tdkTestObj.executeTestCase(expectedresult);
                 actualresult = tdkTestObj.getResult();
                 details = tdkTestObj.getResultDetails();
                 if expectedresult in actualresult  and details.upper() in expectedWANType:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print"Device.X_RDK_WanManager.CPEInterface.%i.Wan.Type is %s" %(noOfEntries,details);
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                 else:
                     statusFlag = 1;
                     tdkTestObj.setResultStatus("FAILURE");
                     print"Device.X_RDK_WanManager.CPEInterface.%i.Wan.Type is %s" %(noOfEntries,details);
                     print "[TEST EXECUTION RESULT] :FAILURE";
                 noOfEntries = noOfEntries -1;

           #setitng the script status
           if  statusFlag == 1:
               tdkTestObj.setResultStatus("FAILURE");
               print "ACTUAL RESULT2: The interfaces donot have the expected WAN type";
               print "[TEST EXECUTION RESULT] :FAILURE";
           else:
               tdkTestObj.setResultStatus("SUCCESS");
               print "ACTUAL RESULT2: The interfaces have the expected WAN type";
               print "[TEST EXECUTION RESULT] :SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1 :Get the number of CPE Interfaces";
            print "EXPECTED RESULT 1: Should get the no of CPE Interfaces greater than zero";
            print "ACTUAL RESULT 1: The value received is :",noOfEntries;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1 :Get the number of CPE Interfaces";
        print "EXPECTED RESULT 1: Should get the no of CPE Interfaces";
        print "ACTUAL RESULT 1: Get operation failed";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tdkbtr181");
else:
     print "Failed to load module";
     obj.setLoadModuleStatus("FAILURE");
