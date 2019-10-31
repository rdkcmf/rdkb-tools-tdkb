##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_XUPNP_B_ReceiveridValidation</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>XUPNPStub_CheckXDiscOutputFile</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get all the receiverid parameters in the output.json file from DUT and validate them by comparing with receiverid parameters in the output.json file from the clients connected.</synopsis>
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
    <test_case_id>TC_XUPNP_24</test_case_id>
    <test_objective>To get all the receiverid parameters in the output.json file from DUT and validate them by comparing with receiverid parameters in the output.json file from the clients connected.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>TDK Agent should be in running state for both DUT and clients connected or invoke it through StartTdk.sh script.</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load xupnp module.
2. Get the output.json file output from DUT and parse the output with bcastMacAddress:receiverid mapping and store it.
3. Get the output.json file output from clients and parse the output with bcastMacAddress:receiverid mapping and store it.
4. Compare the both the outputs.
5. If equal return SUCCESS, else FAILURE.
6.Unload xupnp module.</automation_approch>
    <expected_output>All receiverid parameters retrieved from DUT and clients should be equal.</expected_output>
    <priority>High</priority>
    <test_stub_interface>xupnp</test_stub_interface>
    <test_script>TS_XUPNP_B_ReceiveridValidation</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks></remarks>
  </test_cases>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from xupnplib import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("xupnp","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_XUPNP_B_ReceiveridValidation');

#Get the result of connection with test component and STB
loadmodulestatus=obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper() :
            #Set the result status of execution
            obj.setLoadModuleStatus("SUCCESS");
            tdkTestObj = obj.createTestStep("XUPNPStub_CheckXDiscOutputFile");
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                logpath = details.split(" ")[0];
                print "\n\n\n**************XUPNP DUT LOG TRANSFER - BEGIN*************\n\n"
                print "Transfering output log file : %s from DUT"%logpath;
                logpath = tdkTestObj.transferLogs(logpath, "false");
                print "Local file path of Testrunner output log : %s" %logpath;
                info = open(logpath,'r');
                output = info.read();
                dictionary = LogParser(output,"receiverid");
                info.close()
                print "\n**************XUPNP DUT LOG TRANSFER - END*************\n\n"
                clientip_logfile_dic,NO_OF_CLIENTS = TransferLogsParser(obj);
                if len(dictionary) == NO_OF_CLIENTS + 1 :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "All the connected clients data is populated in output.json file";
                    for key in clientip_logfile_dic :
                        print "\n********XUPNP CLIENT WITH IP : %s LOG TRANSFER - BEGIN********\n\n"%key;
                        print "Transfering output log file : %s from client with ip : %s"%(clientip_logfile_dic.get(key),key);
                        filepath = tdkTestObj.transferLogs_from_box(key,clientip_logfile_dic.get(key), "false")
                        print "Local file path of Testrunner output log : %s" %filepath;
                        data = open(filepath,'r');
                        message = data.read()
                        cli_dictionary = LogParser(message,"receiverid");
                        print "\n********XUPNP CLIENT WITH IP : %s LOG TRANSFER - END********\n\n"%key;
                        print "\n**************XUPNP OUTPUT - BEGIN*************\n\n"
                        for key in dictionary :
                            if dictionary.get(key) == cli_dictionary.get(key):
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP : Compare whether the receiverid parameters from DUT and connected client are equal";
                                print "EXPECTED RESULT : The receiverid parameters from DUT and connected client should be equal";
                                print "ACTUAL RESULT : The receiverid is %s for corresponding %s bcastMacAddress"%(dictionary.get(key),key);
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                                print "\n********************************************************************************************\n";
                            else :
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP : Compare whether the receiverid parameters from DUT and connected client are equal";
                                print "EXPECTED RESULT : The receiverid parameters from DUT and connected client should be equal";
                                print "ACTUAL RESULT : The receiverid is %s for corresponding %s bcastMacAddress"%(dictionary.get(key),key);
                                print "[TEST EXECUTION RESULT] : FAILURE";
                                print "\n********************************************************************************************\n";
                        data.close()
                        print "\n**************XUPNP OUTPUT - END*************\n\n"
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "All the connected clients data is NOT populated in output.json file";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "Failed to get output.json file path from DUT";
                print "DETAILS :",details;
            #Unload upnp module
            obj.unloadModule("xupnp");
else:
    print "Failed to load upnp module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
