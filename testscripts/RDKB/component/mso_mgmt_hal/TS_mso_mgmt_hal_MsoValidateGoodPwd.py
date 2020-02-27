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
  <version>7</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_mso_mgmt_hal_MsoValidateGoodPwd</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>mso_mgmt_hal_MsoValidatePwd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate the password using mso_validatepwd()</synopsis>
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
    <test_case_id>TC_mso_mgmt_hal_2</test_case_id>
    <test_objective>To validate the valid password using mso_validatepwd()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>mso_validatepwd()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load mso_mgmt_hal module
2.Pass the valid password to mso_validatepwd()
3.Get the status of mso_validatepwd()
4.Check whether status of mso_validatepwd() is Good_PWD
5.Unload mso_mgmt_hal module</automation_approch>
    <expected_output>To get the status of mso validate password as good password</expected_output>
    <priority>High</priority>
    <test_stub_interface>MSO_MGMT_HAL</test_stub_interface>
    <test_script>TS_mso_mgmt_hal_MsoValidateGoodPwd</test_script>
    <skipped>No</skipped>
    <release_version>M74</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import ConfigParser;
from tdkbVariables import *;
import os;


#Test component to be tested
obj = tdklib.TDKScriptingLibrary("mso_mgmt_hal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_mso_mgmt_hal_MsoValidateGoodPwd');
sysobj.configureTestCase(ip,port,'TS_mso_mgmt_hal_MsoValidateGoodPwd');


def parseMsoConfig(obj):
        #Get the device name configured in test manager
        config = ConfigParser.ConfigParser()
        #Get the current directory path
        configFilePath = os.path.dirname(os.path.realpath(__file__))
        configFilePath = configFilePath + "/tdkbDeviceConfig"
        config.read(configFilePath+'/mso.config')
        deviceConfig = "mso" + ".config"
        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        deviceType= "sh %s/tdk_utility.sh parseConfigFile DEVICETYPE" %TDK_PATH
        expectedresult="SUCCESS";
        tdkTestObj.addParameter("command", deviceType);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        deviceType = tdkTestObj.getResultDetails().strip();
        deviceType = deviceType.replace("\\n", "");
        podVarName= deviceType+"_POD"
        pod=config.get(deviceConfig, podVarName)
        return pod

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    obj.setLoadModuleStatus("SUCCESS");
    pod = parseMsoConfig(obj)
    if pod != "":
        print "Value retrieved from config file:%s" %pod
        tdkTestObj = obj.createTestStep("mso_mgmt_hal_MsoValidatePwd");
        tdkTestObj.addParameter("paramValue",pod);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        Status = tdkTestObj.getResultDetails();

        if expectedresult in actualresult and Status == "Good_PWD":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Should validate the password";
            print "EXPECTED RESULT 1: Should get the status of password validation as good password";
            print "ACTUAL RESULT 1: Status of password validation is %s" %Status;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Should validate the password";
            print "EXPECTED RESULT 1:Should get the status of password validation as good password";
            print "ACTUAL RESULT 1: Status of password validation is %s" %Status;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        print "POD value is not configured/missing in config file"
        tdkTestObj.setResultStatus("FAILURE");

    sysobj.unloadModule("sysutil");
    obj.unloadModule("mso_mgmt_hal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

