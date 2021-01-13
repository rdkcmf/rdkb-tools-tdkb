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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>3</version>
  <name>TS_CMHAL_SetHTTPDownloadUrl</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_SetHTTP_Download_Url</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set http download url using cm_hal_Set_HTTP_Download_Url() and validate set using cm_hal_Get_HTTP_Download_Url ()</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_CMHAL_108</test_case_id>
    <test_objective>Set http download url using cm_hal_Set_HTTP_Download_Url() and validate set using cm_hal_Get_HTTP_Download_Url ()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Should add firmware name in xconfVariables.py file</pre_requisite>
    <api_or_interface_used>cm_hal_Set_HTTP_Download_Url
cm_hal_Get_HTTP_Download_Url</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  cmhal module
2. Get  the firmware name to be set from xconfVariables.py
3. Set the firmware name to be downloaded and the download url using cm_hal_Set_HTTP_Download_Url()
4. Invoke cm_hal_Get_HTTP_Download_Url() and verify if values set in step 5 is returned
5. cm_hal_Get_HTTP_Download_Url() doesn't have default value, hence no need to revert
6. Unload  cmhal module</automation_approch>
    <expected_output>cm_hal_Set_HTTP_Download_Url() should successfully set download url and firmware name</expected_output>
    <priority>High</priority>
    <test_stub_interface>cmhal</test_stub_interface>
    <test_script>TS_CMHAL_SetHTTPDownloadUrl</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from xconfVariables import *;
import xconfUtilityLib;
from xconfUtilityLib import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_SetHTTPDownloadUrl');
obj1.configureTestCase(ip,port,'TS_CMHAL_SetHTTPDownloadUrl');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    FirmwareVersion, FirmwareFilename = xconfUtilityLib.getFirmwareDetails(obj1)
    print FirmwareFilename;
    if FirmwareFilename:
        #since CMHAL_GetHTTP_Download_Url() doesn't have an initial value, not saving it for revert
        tdkTestObj = obj.createTestStep("CMHAL_SetHTTP_Download_Url");
        tdkTestObj.addParameter("httpURL",FIRMWARELOCATION);
        tdkTestObj.addParameter("filename",FirmwareFilename);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the Download url and filename";
            print "EXPECTED RESULT 2: Should set the Download url: %s and filename: %s" %(FIRMWARELOCATION, FirmwareFilename);
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = obj.createTestStep("CMHAL_GetHTTP_Download_Url");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the download url and filename";
                print "EXPECTED RESULT 3: Should get the download url and filename";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                url=details.split(" ")[2]
                url = url[:-1]
                fwName=details.split(" ")[5]
                if url == FIRMWARELOCATION and fwName == FirmwareFilename:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Verify the download url and filename";
                    print "EXPECTED RESULT 4: Should get the download url and filename same as the set value";
                    print " download url is %s and filename is %s" %(url , fwName )
                    print "ACTUAL RESULT 4: The download url and filename are same as the set value"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Verify the download url and filename";
                    print "EXPECTED RESULT 4: Should get the download url and filename same as the set value";
                    print "download url is %s and filename is %s" %(url , fwName )
                    print "ACTUAL RESULT 4: The download url and filename are not the same as the set value"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the download url and filename";
                print "EXPECTED RESULT 3: Should get the download url and filename";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the Download url and filename";
            print "EXPECTED RESULT 2: Should set the Download url: %s and filename: %s" %(FIRMWARELOCATION, FirmwareFilename);
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	print "Failed to get the firmware details"
    obj.unloadModule("cmhal");
    obj1.unloadModule("sysutil");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        obj1.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
