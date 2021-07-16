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
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzEnableCSIEngine_DisableAll</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_EnableCSIEngine</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Invoke the HAL API wifi_enableCSIEngine() to enable the CSI monitoring for the connected client and then disable CSI monitoring for all using the MAC "00:00:00:00:00:00". In both cases check if the frame info is retrieved as expected</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIHAL_586</test_case_id>
    <test_objective>Invoke the HAL API wifi_enableCSIEngine() to enable the CSI monitoring for the connected client and then disable CSI monitoring for all using the MAC "00:00:00:00:00:00". In both cases check if the frame info is retrieved as expected</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Connect a wifi client to 5GHz radio</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetApAssociatedDeviceDiagnosticResult3
WIFIHAL_EnableCSIEngine</api_or_interface_used>
    <input_parameters>apIndex : 1
MacAddress : client mac address(for enabling)
MacAddress : 00:00:00:00:00:00(for disabling)
enable : csi_enable</input_parameters>
    <automation_approch>1. Load the wifihal and sysutil module.
2. Invoke the function WIFIHAL_GetApAssociatedDeviceDiagnosticResult3 which in turn will invoke the HAL API wifi_getApAssociatedDeviceDiagnosticResult to fetch the connected client details.
3. Once the connected client MAC address is retrieved, invoke the function WIFIHAL_EnableCSIEngine which will invoke the HAL API wifi_enableCSIEngine() to enable the CSI monitoring for the connected client. The API should return success.
4. Check if the CSI frame is properly updated with the connected client details.
5. Invoke WIFIHAL_EnableCSIEngine to disable the CSI monitoring of the connected client by passing the MAC Address as "00:00:00:00:00:00". The API should return success.
6. Check if the CSI frame is properly updated and the client info is not retrieved.
7. Unload the wifihal and sysutil module.</automation_approch>
    <expected_output>Invocation of the HAP API wifi_enableCSIEngine() to enable the CSI monitoring for the connected client and then to disable CSI monitoring by passing the MAC : "00:00:00:00:00:00" should be success. In both cases the frame info should be retrieved as expected.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzEnableCSIEngine_DisableAll</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from time import sleep;
from tdkbVariables import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzEnableCSIEngine_DisableAll');
obj1.configureTestCase(ip,port,'TS_WIFIHAL_5GHzEnableCSIEngine_DisableAll');

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
        print "\nTEST STEP 4: Get CSI_INFO_QUERY from property file";
        print "EXPECTED RESULT 4: Should  get CSI_INFO_QUERY from property file"
        print "ACTUAL RESULT 4: CSI_INFO_QUERY from property file :", cmd ;
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");
    else:
        print "\nTEST STEP 4: Get CSI_INFO_QUERY from property file";
        print "EXPECTED RESULT 4: Should  get CSI_INFO_QUERY from property file"
        print "ACTUAL RESULT 4: CSI_INFO_QUERY from property file :", cmd ;
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
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDeviceDiagnosticResult3');
        tdkTestObj.addParameter("apIndex", idx);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "Details: %s"%details
        print "\nTEST STEP 1: Invoke the HAL API wifi_getApAssociatedDeviceDiagnosticResult3()";
        print "EXPECTED RESULT 1: Should successfully invoke wifi_getApAssociatedDeviceDiagnosticResult3()";

        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1 : wifi_getApAssociatedDeviceDiagnosticResult3() invoked successfully";
            size = details.split(":")[1].strip();
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            output_array_size = size.split("=")[1].split(",")[0].strip();
            print "\nTEST STEP 2: The number of associated clients should be greater than 0";
            print "EXPECTED RESULT 2: The number of associated clients should be greater than 0";

            if int(output_array_size) != 0:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Number of associated clients : %d" %(int(output_array_size));
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Get the MAC address of the client
                mac = details.split("MAC")[1].split(",")[0].split("=")[1].strip();
                if mac != " ":
                    print "MAC Address of the client : %s" %mac;
                    csi_enable = 1;
                    #Enable the CSI data collection for the given MAC
                    tdkTestObj = obj.createTestStep('WIFIHAL_EnableCSIEngine');
                    tdkTestObj.addParameter("apIndex", idx);
                    tdkTestObj.addParameter("MacAddress", mac);
                    tdkTestObj.addParameter("enable",csi_enable);
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    print "\nTEST STEP 3: Enable CSI monitoring using wifi_enableCSIEngine() for the connected client with MAC Address : %s" %mac;
                    print "EXPECTED RESULT 3: wifi_enableCSIEngine() should be invoked successfully";

                    if expectedresult in actualresult :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 3 : wifi_enableCSIEngine() invoked successfully";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Get the query to retrieve the CSI FRAME INFO from platfrom properties file
                        status, cmd = get_csi_info_query(obj1);

                        if status == 0 :
                            #Check if the CSI monitoring is properly enabled
                            sleep(60);
                            print "\nTEST STEP 5: Get the CSI Frame Info for the connected client";
                            print "EXPECTED RESULT 5: Should successfully get the CSI Frame Info for the connected client";
                            status = check_csi_frame_info(obj1, mac, cmd);

                            if status == 0 :
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT 5 : CSI Frame Info is successfully retrieved";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                #Disable the CSI monitoring
                                csi_enable = 0;
                                #Disabling for all
                                mac = "00:00:00:00:00:00";
                                tdkTestObj = obj.createTestStep('WIFIHAL_EnableCSIEngine');
                                tdkTestObj.addParameter("apIndex", idx);
                                tdkTestObj.addParameter("MacAddress", mac);
                                tdkTestObj.addParameter("enable",csi_enable);
                                expectedresult="SUCCESS";
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();
                                print "\nTEST STEP 6: Diasble CSI monitoring using wifi_enableCSIEngine() for all the connected client with MAC Address : %s" %mac;
                                print "EXPECTED RESULT 6: wifi_enableCSIEngine() should be invoked successfully";

                                if expectedresult in actualresult :
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT 6 : wifi_enableCSIEngine() invoked successfully";
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

                                    #Check if the CSI monitoring is properly disabled
                                    print "\nTEST STEP 7: Check if the CSI monitoring is properly disabled";
                                    print "EXPECTED RESULT 7: Should not get the frame info as CSI is disabled";
                                    status = check_csi_frame_info(obj1, mac, cmd);

                                    if status == 1 :
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT 7 : CSI monitoring is disabled successfully";
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS";
                                    else :
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT 7 : CSI monitoring is not disabled successfully";
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE";
                                else :
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT 6 : wifi_enableCSIEngine() not invoked successfully";
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else :
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT 5 : CSI Frame Info is not successfully retrieved";
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else :
                            tdkTestObj.setResultStatus("FAILURE");
                            print "CSI FRAME INFO Query is not fetched from platform properties";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 3 : wifi_enableCSIEngine() not invoked successfully";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "MAC Address is not fetched successfully";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: Number of associated clients : %d" %(int(output_array_size));
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: Failed to invoke wifi_getApAssociatedDeviceDiagnosticResult3()";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

