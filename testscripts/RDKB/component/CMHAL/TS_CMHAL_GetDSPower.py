##########################################################################
#If not stated otherwise in this file or this component's Licenses.txt
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
  <version>1</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_CMHAL_GetDSPower</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>CMHAL_GetParamCharValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get the Power Levels of downstream channels and check whether it is  valid or not.</synopsis>
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
    <test_case_id>TC_CMHAL_22</test_case_id>
    <test_objective>To get the Power Levels of downstream channels and check whether it is valid or not.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_GetDSChannel</api_or_interface_used>
    <input_parameters>paramName : DS_Power</input_parameters>
    <automation_approch>1. Load  cmhal module
2. Invoke docsis_GetDSChannel to get the power levels of downstream channels.
3. The test should return FAILURE if the power levels are not in permissible range.
4. Unload cmhal module</automation_approch>
    <except_output>The Power Level must be within the permissible range</except_output>
    <priority>High</priority>
    <test_stub_interface>CM_HAL</test_stub_interface>
    <test_script>TS_CMHAL_GetDSPower</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_GetDSPower');
obj1.configureTestCase(ip,port,'TS_CMHAL_GetDSPower');

#Get the result of connection with test component and DUT 
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
 
    tdkTestObj1 = obj1.createTestStep("ExecuteCmd");
    cmd = "sh %s/tdk_utility.sh parseConfigFile CM_DS_POWER_LEVELS" %TDK_PATH;
    tdkTestObj1.addParameter("command", cmd);
    expectedresult1="SUCCESS"
    tdkTestObj1.executeTestCase(expectedresult1);
    actualresult1=tdkTestObj1.getResult();
    Details1 = tdkTestObj1.getResultDetails().replace("\\n", "");

    if expectedresult1 in actualresult1 and Details1.strip():
        tdkTestObj1.setResultStatus("SUCCESS");
        print "TEST STEP 0: Execute the command";
        print "EXPECTED RESULT 0: Should execute the command successfully";
        print "ACTUAL RESULT 0: Details: %s" %Details1;
        print "[TEST EXECUTION RESULT] : SUCCESS";
        powerlevels = Details1.split(",");
        print "CM DS Power Levels : %s" %powerlevels;

        #This method invokes the HAL API docsis_GetDSChannel and retrieves the  powerlevels of downstream channels.
        tdkTestObj = obj.createTestStep("CMHAL_GetParamCharValue");
        tdkTestObj.addParameter("paramName","DS_Power");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        Details = tdkTestObj.getResultDetails();
        power = Details.split(",");
        print power;
        Min_power = float(powerlevels[0]);
        Max_power = float(powerlevels[1]);
        for item in power:
            if "dBmV" in item:
                if Min_power <= float(item.split(" ")[0]) <= Max_power:
                    status = "Success";
                else:
                    status = "Failure";
                    break; 
            else :
                if Min_power <= float(item) <= Max_power:
                    status = "Success";
                else:
                    status = "Failure";
                    break; 
        if expectedresult in actualresult and "Success" in status:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the Downstream power";
            print "EXPECTED RESULT 1: Should get the Downstream power successfully";
            print "ACTUAL RESULT 1: Downstream power is within range";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the Downstream power";
            print "EXPECTED RESULT 1: Should get the Downstream power successfully";
            print "ACTUAL RESULT 1: Failed to get the downstream power";
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj1.setResultStatus("FAILURE");
        print "TEST STEP 0: Execute the command";
        print "EXPECTED RESULT 0: Should execute the command successfully";
        print "ACTUAL RESULT 0: Failed to execute the command, Details :%s" %Details1;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("cmhal");
    obj1.unloadModule("sysutil");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        obj1.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

