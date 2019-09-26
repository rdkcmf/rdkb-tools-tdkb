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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TDKB_TR181_GetAllParameterValues</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TDKB_TR181Stub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get and validate all basic tr181 parameters with respect to each module</synopsis>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TDKB_TR181_01</test_case_id>
    <test_objective>To get and validate all basic tr181 parameters with respect to each module</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,Emulator</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load tdkbtr181 module and sysutil module
2. Get the device type of DUT
3. Get the factory reset flag from the config file
4. If it is true, do a factory reset of device
5. Get the list of modules applicable for the respective device type
6. Get the values of all params configured in config file for each module and validate it
7. Unload modules</automation_approch>
    <except_output>Should get the correct values for all tr181 params</except_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TDKB_TR181_GetAllParameterValues</test_script>
    <skipped>No</skipped>
    <release_version>M63</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import tdkbtr181Utility;
from tdkbVariables import *;
import os;
import ConfigParser;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TDKB_TR181_GetAllParameterValues');
obj1.configureTestCase(ip,port,'TDKB_TR181_GetAllParameterValues');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    moduleStatus = {};
    tdkTestObj = obj1.createTestStep('ExecuteCmd');
    deviceType= "sh %s/tdk_utility.sh parseConfigFile DEVICETYPE" %TDK_PATH
    print deviceType;

    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", deviceType);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    deviceType = tdkTestObj.getResultDetails().strip();
    deviceType = deviceType.replace("\\n", "");
    if "Invalid Argument passed" not in deviceType:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the device type";
        print "EXPECTED RESULT 1: Should Get the device type";
        print "ACTUAL RESULT 1: Device Type: %s" %deviceType;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        #Get the device configuration file name
        ModuleListFile= "tdkbModuleList.config"

        #Get the current directory path
        configFilePath = os.path.dirname(os.path.realpath(__file__))
        configFilePath = configFilePath + "/tdkbModuleConfig"

        #Parse the device configuration file
        config = ConfigParser.ConfigParser()
        config.read(configFilePath+'/'+ModuleListFile)

        #Variable containing the list of applicable modules for the device
        moduleVariable = deviceType+ "_MODULE_LIST"

        #Get the list of applicable modules
        moduleList = config.get(ModuleListFile, moduleVariable);
        moduleList = moduleList.split(",");
        print "The modules to test are: ", moduleList;

        #Variable containing the setup type. It can be TDK/WEBPA
        setupTypeVariable = deviceType +"_SETUP_TYPE"
        setup_type = config.get(ModuleListFile,setupTypeVariable);

        factory_reset_flag = config.get(ModuleListFile,"FACTORY_RESET_FLAG")
        if factory_reset_flag == "True":
            tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Set")
            tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset")
            tdkTestObj.addParameter("ParamValue","router")
            tdkTestObj.addParameter("Type","string")

            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails()
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Factory reset the device"
                print "TEST STEP 2: Should factory reset the device"
                print "ACTUAL RESULT 2: ", actualresult
                print "TEST EXECUTION RESULT: SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Factory reset the device"
                print "TEST STEP 2: Should factory reset the device"
                print "ACTUAL RESULT 2: ", actualresult
                print "TEST EXECUTION RESULT: FAILURE"
        #Invoke the utility function to get and validate the values for all configured tr181 params
        result, failedParams= tdkbtr181Utility.getAllParamValues(moduleList,setup_type,deviceType,factory_reset_flag,obj);

        for i in range(len(moduleList)):
            moduleStatus[moduleList[i]]= result[i];

        print "\n overall module status ", moduleStatus, "\n";

        for module in moduleList:
            print "Status of ",module, " is : ",moduleStatus[module], "\n";
            if moduleStatus[module] == "FAILURE":
                print "The failed params are ", failedParams[module], "\n";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the device type";
        print "EXPECTED RESULT 1: Should Get the device type";
        print "ACTUAL RESULT 1: Device Type: %s" %deviceType;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
