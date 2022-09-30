##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <version>1</version>
  <name>TS_WIFIAGENT_5GHzOffChannelNchannelValidation_WithDFSEnabled</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the number of channels being scanned, Device.WiFi.Radio.2.X_RDK_OffChannelNchannel,  returns the value 24 when DFS is enabled using Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable and Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OffChannelScan.Enable is enabled.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIAGENT_222</test_case_id>
    <test_objective>To check if the number of channels being scanned, Device.WiFi.Radio.2.X_RDK_OffChannelNchannel,  returns the value 24 when DFS is enabled using Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable and Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OffChannelScan.Enable is enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OffChannelScan.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.Radio.2.X_RDK_OffChannelNchannel</input_parameters>
    <automation_approch>1. Load the wifiagent module
2. As pre-requisite enable the off channel scan controlling RFC parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OffChannelScan.Enable if not already enabled.
3. Get the initial DFS enable state using Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable.
4. If the DFS is not already enabled, enable it and validate with get.
5. Get the value of Device.WiFi.Radio.2.X_RDK_OffChannelNchannel.
6. When DFS is enabled the expected N channel value is "24". Check if the value returned is 24.
7. Revert Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable if required.
8. Revert the controlling RFC if required.
9. Unload the wifiagent module.</automation_approch>
    <expected_output>Device.WiFi.Radio.2.X_RDK_OffChannelNchanne should return the value 24 when DFS is enabled using Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable and Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OffChannelScan.Enable is enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_5GHzOffChannelNchannelValidation_WithDFSEnabled</test_script>
    <skipped>No</skipped>
    <release_version>M105</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
def getParameter(obj, param, expectedresult):
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName", param);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details;

def setParameter(obj, param, setValue, type, expectedresult):
    tdkTestObj = obj.createTestStep('WIFIAgent_Set_Get');
    tdkTestObj.addParameter("paramName",param);
    tdkTestObj.addParameter("paramValue",setValue);
    tdkTestObj.addParameter("paramType",type);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;
from tdkutility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHzOffChannelNchannelValidation_WithDFSEnabled');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Set the pre-requisites
    step = 1;
    print "\n*************Set Pre-requisite Start*****************";
    tdkTestObj, pre_req_set, revert_flag, step = WiFiOffChannelScanEnable_PreReq(obj, step);

    if pre_req_set == 0:
        print "\n*************Set Pre-requisite Complete*****************";
        #Get the initial DFS Enable status
        step = step + 1;
        param = "Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable"

        print "\nTEST STEP %d: Get the initial DFS enable status using Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable" %step;
        print "EXPECTED RESULT %d: Should get the value of Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable successfully" %step;
        actualresult, details = getParameter(obj, param, expectedresult);

        if expectedresult in actualresult and details != "":
            dfs_initial = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Initial DFS Enable : %s" %(step, dfs_initial);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if the DFS enabled is "true", else set to "true"
            proceed_flag = 0;
            if dfs_initial != "true":
                step = step + 1;
                set_val = "true"
                print "\nTEST STEP %d: Set Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable to %s" %(step, set_val);
                print "EXPECTED RESULT %d: Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable should be enabled successfully" %step;
                actualresult, details = setParameter(obj, param, set_val, "boolean", expectedresult);

                if expectedresult in actualresult and details != "":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: DFS Enable set is success; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    proceed_flag = 1;
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: DFS Enable set failed; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                print "Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable is already disabled, set operation not required";

            #Check the N channel value if DFS is enabled
            if proceed_flag == 0:
                step = step + 1;
                param = "Device.WiFi.Radio.2.X_RDK_OffChannelNchannel"

                print "\nTEST STEP %d: Get the number of channels that are scanned using Device.WiFi.Radio.2.X_RDK_OffChannelNchannel" %step;
                print "EXPECTED RESULT %d: Should get the value of Device.WiFi.Radio.2.X_RDK_OffChannelNchannel successfully" %step;
                actualresult, details = getParameter(obj, param, expectedresult);

                if expectedresult in actualresult and details != "":
                    n_channel = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: N channel value : %s" %(step, n_channel);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Check if the value is 24 when DFS is in enabled state
                    step = step + 1;
                    print "\nTEST STEP %d: Check if the number of channels that are scanned using Device.WiFi.Radio.2.X_RDK_OffChannelNchannel returns 24 with DFS disabled" %step;
                    print "EXPECTED RESULT %d: Should get the value of Device.WiFi.Radio.2.X_RDK_OffChannelNchannel as 24 with DFS in enabled state" %step;

                    if n_channel.isdigit() and int(n_channel) == 24:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: The N channel value is 24 as expected" %(step);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: The N channel value is NOT 24 as expected" %(step);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: N channel value : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert DFS Enable state
                if dfs_initial != "true":
                    step = step + 1;
                    set_val = "false"
                    paramName = "Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable";
                    print "\nTEST STEP %d: Revert Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable to %s" %(step, set_val);
                    print "EXPECTED RESULT %d: Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable should be reverted successfully" %step;
                    actualresult, details = setParameter(obj, paramName, set_val, "boolean", expectedresult);

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: DFS Enable revert is success; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: DFS Enable set failed; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable revert operation not required";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "Unable to enable Device.WiFi.Radio.2.X_COMCAST_COM_DFSEnable, cannot proceed..."
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Initial DFS Enable : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        #Revert the pre-requisites
        step = step + 1;
        print "\n*************Revert Pre-requisite Start*****************";
        WiFiOffChannelScanEnable_Revert(obj, revert_flag, step);
        print "\n*************Revert Pre-requisite Complete*****************";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "Unable to enable the pre-requisites, cannot proceed..";

    obj.unloadModule("wifiagent")
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
