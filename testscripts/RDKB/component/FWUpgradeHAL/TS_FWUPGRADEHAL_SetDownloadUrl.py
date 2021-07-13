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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>15</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_FWUPGRADEHAL_SetDownloadUrl</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>FWUPGRADEHAL_Set_Download_Url</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Set download URL using fwupgrade_hal_set_download_url() and validate set using fwupgrade_hal_get_download_url() APIs.</synopsis>
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
    <test_case_id>TC_FWUPGRADEHAL_01</test_case_id>
    <test_objective>Set download URL using fwupgrade_hal_set_download_url() and validate set using fwupgrade_hal_get_download_url() APIs.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>FWUPGRADEHAL_Set_Download_Url</api_or_interface_used>
    <input_parameters>FirmwareLocaition : http://dac15cdlserver.ae.ccp.xcal.tv:8080/Images
FirmwareFilename : fetched from Config file</input_parameters>
    <automation_approch>1. Load the fwupgradehal module
2. Invoke the function FWUPGRADEHAL_Set_Download_Url which invokes fwupgrade_hal_set_download_url() with the Firmware Location URL and the Firmware Filename. The SET API should return success.
3. Invoke the function FWUPGRADEHAL_Get_Download_Url which invokes fwupgrade_hal_get_download_url() and retrieve the URL and filename. The GET API should return success.
4. Check if the SET and GET values match.
5. Unload the fwupgradehal module</automation_approch>
    <expected_output>Setting download URL using fwupgrade_hal_set_download_url() should be success and validation using fwupgrade_hal_get_download_url() should match the set values.</expected_output>
    <priority>High</priority>
    <test_stub_interface>fwupgradehal</test_stub_interface>
    <test_script>TS_FWUPGRADEHAL_SetDownloadUrl</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from FWUpgradeUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("fwupgradehal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_FWUPGRADEHAL_SetDownloadUrl');
obj1.configureTestCase(ip,port,'TS_FWUPGRADEHAL_SetDownloadUrl');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";
    tdkTestObj, actualresult, FirmwareFilename = get_FirmwareFilename(obj1);

    if (expectedresult in actualresult) and (FirmwareFilename != " "):
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1 : Fetch the Firmware Filename and Firmware Location URL successfully from config file";
        print "EXPECTED RESULT 1 : Firmware Filename and Firmware Location URL should be fetched successfully";
        print "ACTUAL RESULT 1 : Firmware Details are fetched successfully";
        print "Firmware Location URL : %s" %FirmwareLocationURL;
        print "FirmwareFilename : %s" %FirmwareFilename;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep("FWUPGRADEHAL_Set_Download_Url");
        tdkTestObj.addParameter("URL",FirmwareLocationURL);
        tdkTestObj.addParameter("filename",FirmwareFilename);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the Download URL and Filename using the HAL API fwupgrade_hal_set_download_url()";
            print "EXPECTED RESULT 2: Should set the Download url: %s and Filename: %s" %(FirmwareLocationURL, FirmwareFilename);
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj = obj.createTestStep("FWUPGRADEHAL_Get_Download_Url");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the Download URL and Filename using the HAL API fwupgrade_hal_get_download_url()";
                print "EXPECTED RESULT 3: Should get the Download URL and Filename";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                url=details.split(" ")[2]
                url = url[:-1]
                fwName=details.split(" ")[5]

                if url == FirmwareLocationURL and fwName == FirmwareFilename:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Verify the Download URL and Filename";
                    print "EXPECTED RESULT 4: Should get the Download URL and Filename same as the set value";
                    print "Download URL is %s and Filename is %s" %(url , fwName )
                    print "ACTUAL RESULT 4: The Download URL and Filename are same as the set value"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Verify the Download URL and Filename";
                    print "EXPECTED RESULT 4: Should get the Download URL and Filename same as the set value";
                    print "Download URL is %s and Filename is %s" %(url , fwName )
                    print "ACTUAL RESULT 4: The Download URL and Filename are not the same as the set value"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the Download URL and Filename using the HAL API fwupgrade_hal_get_download_url()";
                print "EXPECTED RESULT 3: Should get the Download URL and Filename";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the Download URL and Filename using the HAL API fwupgrade_hal_set_download_url()";
            print "EXPECTED RESULT 2: Should set the Download url: %s and Filename: %s" %(FirmwareLocationURL, FirmwareFilename);
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1 : Fetch the Firmware Filename and Firmware Location URL successfully from config file";
        print "EXPECTED RESULT 1 : Firmware Filename and Firmware Location URL should be fetched successfully";
        print "ACTUAL RESULT 1 : Firmware Details are not fetched successfully";
        print "Firmware Location URL : %s" %FirmwareLocationURL;
        print "FirmwareFilename : %s" %FirmwareFilename;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("fwupgradehal");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
