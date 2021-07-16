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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>2</version>
  <name>TS_WIFIHAL_2.4GHzEnableCSIEngine_WithInvalidMAC</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_EnableCSIEngine</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Enable CSI monitoring for an invalid MAC address(no connected client) by invoking wifi_enableCSIEngine() and check if the CSI frame info is not retrieved for the invalid MAC.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIHAL_587</test_case_id>
    <test_objective>Enable CSI monitoring for an invalid MAC address(no connected client) by invoking wifi_enableCSIEngine() and check if the CSI frame info is not retrieved for the invalid MAC.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_EnableCSIEngine</api_or_interface_used>
    <input_parameters>apIndex : 0
MacAddress : randomly generated
enable : 1</input_parameters>
    <automation_approch>1. Load the wifihal and sysutil module.
2. Invoke the function WIFIHAL_EnableCSIEngine which in turn invokes the HAL API wifi_enableCSIEngine() with a randomly generated MAC and enable as true. The API invocation should be success.
3. Query the CSI frame info with the invalid MAC and check if the frame info is received. Frame info should not be received for invalid MAC.
4. Unload the modules.</automation_approch>
    <expected_output>The HAL API wifi_enableCSIEngine() should be invoked successfully with invalid MAC but the corresponding frame info should not be retrieved.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzEnableCSIEngine_WithInvalidMAC</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from time import sleep;
from random import randint
from tdkbVariables import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzEnableCSIEngine_WithInvalidMAC');
obj1.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzEnableCSIEngine_WithInvalidMAC');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

def get_csi_info_query(obj1):
    #Getting CSI_INFO_QUERY value from tdk_platform_properties"
    cmd= "sh %s/tdk_utility.sh parseConfigFile CSI_INFO_QUERY" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj = obj1.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    cmd = tdkTestObj.getResultDetails().replace("\\n", "");
    status = 1;

    if expectedresult in actualresult and cmd!= "":
        status = 0;
        print "\nTEST STEP 2: Get CSI_INFO_QUERY from property file";
        print "EXPECTED RESULT 2: Should  get CSI_INFO_QUERY from property file"
        print "ACTUAL RESULT 2: CSI_INFO_QUERY from property file :", cmd ;
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");
    else:
        print "\nTEST STEP 2: Get CSI_INFO_QUERY from property file";
        print "EXPECTED RESULT 2: Should  get CSI_INFO_QUERY from property file"
        print "ACTUAL RESULT 2: CSI_INFO_QUERY from property file :", cmd ;
        print "TEST EXECUTION RESULT :FAILURE";
        tdkTestObj.setResultStatus("FAILURE");
    return status, cmd;


def check_csi_frame_info(obj1, mac, cmd):
    tdkTestObj = obj1.createTestStep('ExecuteCmd');
    query = cmd + " | grep -i " + mac;
    print "Query : %s" %query;
    tdkTestObj.addParameter("command", query);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "Details : %s" %details;

    if expectedresult in actualresult and details != "":
        status = 0;
    else :
        status = 1;
    return status;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Enable CSI parameter for invalid MAC
        csi_enable = 1;
        #Generate a random MAC Address
        mac_partial = "7a:36:76:41:9a:";
        x = str(randint(10,99));
        mac = mac_partial + x;

        #Enable the CSI data collection for the given MAC
        tdkTestObj = obj.createTestStep('WIFIHAL_EnableCSIEngine');
        tdkTestObj.addParameter("apIndex", idx);
        tdkTestObj.addParameter("MacAddress", mac);
        tdkTestObj.addParameter("enable",csi_enable);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "\nTEST STEP 1: Enable CSI monitoring using wifi_enableCSIEngine() for the invalid client MAC Address : %s" %mac;
        print "EXPECTED RESULT 1: wifi_enableCSIEngine() should be invoked successfully";

        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1 : wifi_enableCSIEngine() invoked successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Get the CSI FRAME INFO Query from platform properties
            status, cmd = get_csi_info_query(obj1);

            if status == 0:
                #Check if the CSI monitoring is not enabled with invalid MAC
                sleep(60);
                print "\nTEST STEP 3: Get the CSI Frame Info for the invalid client MAC";
                print "EXPECTED RESULT 3: Should not get the CSI Frame Info for the invalid client MAC";
                status = check_csi_frame_info(obj1, mac, cmd);

                if status == 1 :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3 : CSI Frame Info is not retrieved for invalid client MAC";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3 : CSI Frame Info is retrieved for invalid client MAC";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "CSI FRAME INFO Query not fetched from platform properties";
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1 : wifi_enableCSIEngine() not invoked successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

