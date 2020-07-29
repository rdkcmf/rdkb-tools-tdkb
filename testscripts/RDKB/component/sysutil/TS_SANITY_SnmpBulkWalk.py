##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_SnmpBulkWalk</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check for successful snmpwalk on the OID's.</synopsis>
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
    <test_case_id>TC_SYSUTIL_35</test_case_id>
    <test_objective>This test case is to check for successful snmpwalk on the OID's </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>OIDs  to be queried</input_parameters>
    <automation_approch>1.Load the module
2.From the listed OIDs do a snmpwalk on each of them one after the another.
3.Check if any errors like No Such Object available, No Such Instance, Timeout are found on the snmpwalk
4.If such errors found print the failure message else print the success message .
4.Unload the Module
</automation_approch>
    <expected_output>snmpwalk on  the OIDs should be successful without any errors</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_SnmpBulkWalk</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import snmplib;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_SnmpBulkWalk');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();


def SnmpQuery (Oid,ipaddress,communityString):
    #Get the Community String
    communityString = snmplib.getCommunityString(obj,"snmpget");
    #Get the IP Address
    ipaddress = snmplib.getIPAddress(obj);
    ########## Script to Execute the snmp command ###########
    actResponse = snmplib.SnmpExecuteCmd("snmpwalk", communityString, "-v 2c",Oid,ipaddress);
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.executeTestCase("SUCCESS");
    if "" in actResponse :
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP : snmpwalk request to get all the values";
        print "EXPECTED RESULT : Command should return all values";
        print "ACTUAL RESULT : snmpwalk was successfull";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : snmpwalk request to get all the values";
        print "EXPECTED RESULT : Command should return all values";
        print "ACTUAL RESULT : snmpwalk failed";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return actResponse;

if "SUCCESS" in loadmodulestatus.upper() :
    flag =1;
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    #Get the Community String
    communityString = snmplib.getCommunityString(obj,"snmpget");
    #Get the IP Address
    ipaddress = snmplib.getIPAddress(obj);

    oidlist = ["1.3.6.1.4.1.17270.43.1.2","1.3.6.1.4.1.31621.1.1.1"];
    length = len(oidlist);
    tdkTestObj.executeTestCase("SUCCESS");
    for i in range(length):
        print "Doing a snmpwalk on :",oidlist[i];
        actResponse = SnmpQuery(oidlist[i],ipaddress,communityString);
        checklist = ["No Such Object available", "No Such Instance", "Timeout"];

        print "Checking if No Such Object available, No Such Instance, Timeout are found on the snmpwalk";

        for list in checklist :
            result = actResponse.find(list);
            if result != -1:
               flag =0
               break;
            else:
                flag =1;
        if flag == 1:
           tdkTestObj.setResultStatus("SUCCESS");
           print "The snmpwalk on the OID was Sucess no such instance of message was seen";
           print "[TEST EXECUTION RESULT]:SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "The snmpwalk failed because :",list;
            print "[TEST EXECUTION RESULT]:FAILURE";

    obj.unloadModule("sysutil");
else:
    print "FAILURE to load SNMP_PA module";
    obj.setLoadModuleStatus("FAILURE");
