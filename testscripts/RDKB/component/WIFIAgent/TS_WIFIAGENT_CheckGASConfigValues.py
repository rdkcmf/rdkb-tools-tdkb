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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_CheckGASConfigValues</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if Generic Advertising Service Configurations are within the range of expected values</synopsis>
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
    <test_case_id>TC_WIFIAGENT_122</test_case_id>
    <test_objective>This test case is to check if Generic Advertising Service Configurations are within the range of expected values</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIAgent_Get</api_or_interface_used>
    <input_parameters>Device.WiFi.X_RDKCENTRAL-COM_GASConfiguration</input_parameters>
    <automation_approch>1. Load the module
2. Query Device.WiFi.X_RDKCENTRAL-COM_GASConfiguration
3. Check  if the configs are within the below mentioned range
Advertisement Identifier - unsigned 0..255
Pause for Server response - boolean
Response Timeout - unsigned (1000..65535)
Comeback Delay - unsigned (0..65535)
Response Buffering Time - unsigned (0..65535);
Query Response Length Limit - unsigned (1..127);
4. mark the script as success if the values are within the range else mark them as failure
5.Unload the module</automation_approch>
    <expected_output>All the GAS configuration must be in the expected range of value</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIAGENT</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckGASRange</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckGASConfigValues');
#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
flag =1;
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")

    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.WiFi.X_RDKCENTRAL-COM_GASConfiguration");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and details:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the GAS Configuration";
        print "EXPECTED RESULT 1: Should get GAS Configuration";
        print "ACTUAL RESULT 1: GAS Configuration retreived successful";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        advertId = int(details.split("AdvertisementId")[1].split(":")[1].split(",")[0].strip().replace("\\n", ""));
        pauseForServerResp = details.split("PauseForServerResp")[1].split(":")[1].split(",")[0].strip().replace("\\n", "");
        respTimeout = int(details.split("RespTimeout")[1].split(":")[1].split(",")[0].strip().replace("\\n", ""));
        comebackDelay = int(details.split("ComebackDelay")[1].split(":")[1].split(",")[0].strip().replace("\\n", ""));
        respBufferTime = int(details.split("RespBufferTime")[1].split(":")[1].split(",")[0].strip().replace("\\n", ""));
        queryRespLengthLimit=int(details.split("QueryRespLengthLimit")[1].split(":")[1].split("}")[0].strip().replace("\\n", ""));

        print "*** Checking if the Configurations are within the expected range***";
        if 0<= advertId <= 255:
           print "advertId:",advertId;
           print "advertId is within the expected range from 0 to 255";
        else:
            flag =0;
            print "advertId:",advertId;
            print "advertId is not within the expected range 0 to 255";

        if "true" in pauseForServerResp or "false" in pauseForServerResp:
           print "pauseForServerResp:",pauseForServerResp;
           print "pauseForServerResp should be either true or false";
        else:
            flag =0;
            print "pauseForServerResp:",pauseForServerResp;
            print "pauseForServerResp doesnot hold a boolean value";

        if 1000<= respTimeout <= 65535:
           print "respTimeout:",respTimeout
           print "respTimeout is within the expected range of 1000 to 65535";
        else:
            flag =0;
            print "respTimeout is not within the expected range of 1000 to 65535";

        if 0<= comebackDelay <= 65535:
           print "comebackDelay:" ,comebackDelay
           print "comebackDelay is within the expected range of to 0 to 65535";
        else:
            flag =0;
            print "comebackDelay:" ,comebackDelay
            print "comebackDelay is not within the expected range of to 0 to 65535";

        if 0<=respBufferTime <= 65535:
           print "respBufferTime:",respBufferTime;
           print"respBufferTime is within the expected range of  0 to 65535";
        else:
            flag =0;
            print "respBufferTime:",respBufferTime;
            print "respBufferTime is not within the expected range of  0 to 65535";

        if 1<= queryRespLengthLimit <= 127:
           print "queryRespLengthLimit: ",queryRespLengthLimit;
           print "queryRespLengthLimit is within the expected range of 1 to 127";
        else:
            flag =0;
            print "queryRespLengthLimit: ",queryRespLengthLimit;
            print "queryRespLengthLimit is not within the expected range of 1 to 127";

        if flag == 1:
           tdkTestObj.setResultStatus("SUCCESS");
           print "********All the GAS Configurations are within the expected range*****";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "*****All the GAS Configurations are not within the expected range*****";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the GAS Configuration";
        print "EXPECTED RESULT 1: Should get GAS Configuration";
        print "ACTUAL RESULT 1: Failed to  retrieve GAS Configuration";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifiagent");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
