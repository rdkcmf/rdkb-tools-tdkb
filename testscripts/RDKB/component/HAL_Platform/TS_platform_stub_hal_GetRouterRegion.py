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
  <name>TS_platform_stub_hal_GetRouterRegion</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>platform_stub_hal_GetRouterRegion</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Invoke platform_hal_GetRouterRegion() and check if it is returning expected value</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_HAL_Platform_75</test_case_id>
    <test_objective>Invoke platform_hal_GetRouterRegion() and check if it is returning expected value</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_GetRouterRegion</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load halplatform module
2. Get and save the list of possible router regions and its corresponding device serial no: info from platform property file
3. Invoke platform_hal_GetRouterRegion() and save the return value
4. Get the device's serial no: using hal api platform_hal_GetSerialNumber
5. From platform property data, find the region code corresponding to the device serial no: got from step4
6. Check if the region code found in step5 is matching with the value returned by platform_hal_GetRouterRegion()
7. Unload halplatform module</automation_approch>
    <expected_output>platform_hal_GetRouterRegion() api should return a value from expected list of regions</expected_output>
    <priority>High</priority>
    <test_stub_interface>halplatform</test_stub_interface>
    <test_script>TS_platform_stub_hal_GetRouterRegion</test_script>
    <skipped>No</skipped>
    <release_version>M82</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_GetRouterRegion');
sysObj.configureTestCase(ip,port,'TS_platform_stub_hal_GetRouterRegion');

#Get the result of connection with test component and DUT
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =sysObj.getLoadModuleResult();


if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    command= "sh %s/tdk_utility.sh parseConfigFile ROUTER_REGION" %TDK_PATH;
    print command;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    routerRegion = tdkTestObj.getResultDetails().strip().replace("\\n","");
    if expectedresult in actualresult and routerRegion != " ":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get value of ROUTER_REGION from property file"
        print "EXPECTED RESULT 1: Should get the value of ROUTER_REGION from property file"
        print "ACTUAL RESULT 1:ROUTER_REGION from property file  %s" %routerRegion ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        routerRegionList = routerRegion.split('-')

        tdkTestObj = obj.createTestStep('platform_stub_hal_GetRouterRegion');
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        routerRegion= tdkTestObj.getResultDetails();
        if expectedresult in actualresult and routerRegion != " ":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Retrieve the Platform_getRouterRegion";
            print "EXPECTED RESULT 2: Should retrieve the Platform_getRouterRegion successfully";
            print "ACTUAL RESULT 2: Platform_getRouterRegion value retrieved: %s" %routerRegion
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj.createTestStep("platform_stub_hal_GetSerialNumber");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult and details != " ":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Retrieve the Platform_GetSerialNumber";
                print "EXPECTED RESULT 3: Should retrieve the Platform_GetSerialNumber successfully";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Serial Number: %s" %details;
                slNoFromHal = details[0:2]

                regionCodes=[]
                slList=[]
                #Split the data from platform property into 2 lists of region codes and serial no:s
                for entry in routerRegionList:
                    regionCodes.append(entry.split(':')[0])
                    slList.append(entry.split(':')[1])
                print "------regionCodes-------", regionCodes
                print "-------------slList--------", slList

                listIndex = 0
                #find the index of serial no: list which matches device serial no:
                for entry in slList:
                    if slNoFromHal in entry:
                        break
                    listIndex = listIndex + 1

                if listIndex <= len(slList):
                    if routerRegion == regionCodes[listIndex]:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4: Check if the region code from Platform_getRouterRegion is as per the device serial no:";
                        print "EXPECTED RESULT 4: Should validate the Platform_getRouterRegion successfully";
                        print "ACTUAL RESULT 4: Region code from Platform_getRouterRegion() corresponds with the device serial no:";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Check if the region code from Platform_getRouterRegion is as per the device serial no:";
                        print "EXPECTED RESULT 4: Should validate the Platform_getRouterRegion successfully";
                        print "ACTUAL RESULT 4: Region code from Platform_getRouterRegion() is not as per the device serial no:";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "FAILURE: Device serail no: from hal api not matching with property file data"
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Retrieve the Platform_GetSerialNumber";
                print "EXPECTED RESULT 3: Should retrieve the Platform_GetSerialNumber successfully";
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "%s" %details;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Retrieve the Platform_getRouterRegion";
            print "EXPECTED RESULT 2: Should retrieve the Platform_getRouterRegion successfully";
            print "ACTUAL RESULT 2: Failed to retrieve Platform_getRouterRegion"
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get value of ROUTER_REGION from property file"
        print "EXPECTED RESULT 1: Should get the value of ROUTER_REGION from property file"
        print "ACTUAL RESULT 1: Failed to get ROUTER_REGION  from configuration file" ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("halplatform");
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
