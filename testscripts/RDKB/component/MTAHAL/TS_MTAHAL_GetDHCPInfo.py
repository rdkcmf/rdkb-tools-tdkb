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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>1</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_MTAHAL_GetDHCPInfo</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>MTAHAL_GetDHCPInfo</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Retrieve all the relevant DHCP info for MTA.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TC_MTAHAL_1</test_case_id>
    <test_objective>To get the all the relevant DHCP info for MTA.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>mta_hal_GetDHCPInfo()</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1. Load mtahal module
2. Using TS_MTAHAL_GetDHCPInfo invoke mta_hal_GetDHCPInfo() to see if all the relevant DHCP info for MTA are getting or not. If available return SUCCESS and exit else return FAILURE and exit.
3. convert the ipv4 address to the dot-decimal notation.
4. Unload mtahal module</automation_approch>
    <except_output>Get all the relevant DHCP info for MTA.</except_output>
    <priority>High</priority>
    <test_stub_interface>MTAHAL</test_stub_interface>
    <test_script>TS_MTAHAL_GetDHCPInfo</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib
import socket, struct

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("mtahal","1")

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MTAHAL_GetDHCPInfo')

#Get the result of connection with test component and DUT 
loadmodulestatus =obj.getLoadModuleResult()
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus 

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("MTAHAL_GetDHCPInfo")
    expectedresult="SUCCESS"
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    resultDetails = " "
    resultDetails = tdkTestObj.getResultDetails()

    if expectedresult in actualresult and resultDetails != " ":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS")
        print "TEST STEP 1: Get the DHCP Info"
        print "EXPECTED RESULT 1: Should get the DHCP Info successfully"
        print "ACTUAL RESULT 1: The DHCP Info:"
        print ""
        for x in resultDetails.split(";"):
            if "IPAddress" in x:
                print "IPAddress=%s" %socket.inet_ntoa(struct.pack('<L', (int(x.split("=")[-1]) % 2**32) ))
            elif "SubnetMask" in x:
                print "SubnetMask=%s" %socket.inet_ntoa(struct.pack('<L', (int(x.split("=")[-1]) % 2**32) ))
            elif "Gateway" in x:
                print "Gateway=%s" %socket.inet_ntoa(struct.pack('<L', (int(x.split("=")[-1]) % 2**32) ))
            elif "PrimaryDNS" in x:
                print "PrimaryDNS=%s" %socket.inet_ntoa(struct.pack('<L', (int(x.split("=")[-1]) % 2**32) ))
            elif "SecondaryDNS" in x:
                print "SecondaryDNS=%s" %socket.inet_ntoa(struct.pack('<L', (int(x.split("=")[-1]) % 2**32) ))
            elif "PrimaryDHCPServer" in x:
                print "PrimaryDHCPServer=%s" %socket.inet_ntoa(struct.pack('<L', (int(x.split("=")[-1]) % 2**32) ))
            elif "SecondaryDHCPServer" in x:
                print "SecondaryDHCPServer=%s" %socket.inet_ntoa(struct.pack('<L', (int(x.split("=")[-1]) % 2**32) ))
            else:
                print x
        print ""
        #Get the result of execution        
        print "[TEST EXECUTION RESULT] : SUCCESS"
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print "TEST STEP 1: Get the DHCP Info"
        print "EXPECTED RESULT 1: Should get the DHCP Info successfully"
        print "ACTUAL RESULT 1: Failed to get the DHCP Info:"
        print "%s" %resultDetails
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("mtahal")
else:
    print "Failed to load the module"
    obj.setLoadModuleStatus("FAILURE")
    print "Module loading failed"
