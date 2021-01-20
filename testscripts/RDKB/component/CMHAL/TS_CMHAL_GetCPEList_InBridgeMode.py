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
  <version>1</version>
  <name>TS_CMHAL_GetCPEList_InBridgeMode</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_GetCPEList</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the list of CPEs connected to the CM using cm_hal_GetCPEList() with bridge mode enabled</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_CMHAL_111</test_case_id>
    <test_objective>To get the list of CPEs connected to the CM using cm_hal_GetCPEList() with bridge mode enabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.LAN client should be connected to the DUT</pre_requisite>
    <api_or_interface_used>cm_hal_GetCPEList()</api_or_interface_used>
    <input_parameters>lan mode of the device  - lanMode</input_parameters>
    <automation_approch>1. Load  cmhal module
2. Check if the LAN client is connected from Device.Host. Table ,check if the connected client is Ethernet and active
3. Get the current lan mode and set the lan mode to bridge static
4. From script invoke CMHAL_GetCPEList()
5. Check if no client details is received and instance is 0
6. Validation of  the result is done within the python script and send the result status to Test Manager.
7. Test Manager will publish the result in GUI as PASS/FAILURE based on the response .
8. Revert the lan mode to previous </automation_approch>
    <expected_output>The api should not return the ip address and mac address of CPEs connected when in bridge mode</expected_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_GetCPEList_InBridgeMode</test_script>
    <skipped>No</skipped>
    <release_version>M85</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");
obj2 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_GetCPEList_InBridgeMode');
obj2.configureTestCase(ip,port,'TS_CMHAL_GetCPEList_InBridgeMode');
ip = "";
mac ="";
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus2 =obj2.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus2 ;
def GetLanOperationalMode(tdkTestObj):
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    curlanMode = tdkTestObj.getResultDetails().strip();
    return actualresult,curlanMode;

def SetLanOperationalMode(tdkTestObj,setValue):
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    tdkTestObj.addParameter("ParamValue",setValue);
    tdkTestObj.addParameter("Type","string");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult,details;

def CheckAndSetDeviceToRouterMode():
    revertflag = 0;
    tdkTestObj = obj2.createTestStep('TDKB_TR181Stub_Get');
    expectedresult = "SUCCESS";
    actualresult,deflanMode = GetLanOperationalMode(tdkTestObj);
    if expectedresult in actualresult  and deflanMode == "router":
        tdkTestObj.setResultStatus("SUCCESS");
        print "The device is in router mode and no Lan mode change required";
    else:
        print "The device is not in router mode hence setting device to router mode to check for connected clients";
        setValue = "router";
        tdkTestObj = obj2.createTestStep('TDKB_TR181Stub_Set');
        actualresult,details =SetLanOperationalMode(tdkTestObj,setValue);
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            revertflag =  1;
            print "The device set to router mode successfully";
            time.sleep(90);
        else:
             tdkTestObj.setResultStatus("FAILURE");
             print "The device is not in router mode and failed to set it to router mode";

    return actualresult ,deflanMode,revertflag;
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj2.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    actualresult ,deflanMode,revertflag  = CheckAndSetDeviceToRouterMode();
    if expectedresult in actualresult :
        tdkTestObj = obj2.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.Hosts.HostNumberOfEntries");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        NoOfHost=tdkTestObj.getResultDetails().strip().replace("\\n", "");
        if expectedresult in actualresult and int(NoOfHost) >0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the no of clients connected";
            print "EXPECTED RESULT 1: Should get the no of clients connected"
            print "ACTUAL RESULT 1:%s" %NoOfHost
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            clientfound = 0;
            for i in range (1,int(NoOfHost)+1):
                expectedresult="SUCCESS";
                tdkTestObj = obj2.createTestStep('TDKB_TR181Stub_Get');
                tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.Layer1Interface"%(i));
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details=tdkTestObj.getResultDetails().strip().replace("\\n", "");
                print "Device.Hosts.Host.%s.Layer1Interface value is %s" %(i,details);
                if expectedresult in actualresult and details == "Ethernet":
                    tdkTestObj = obj2.createTestStep('TDKB_TR181Stub_Get');
                    tdkTestObj.addParameter("ParamName","Device.Hosts.Host.%s.Active"%(i));
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details=tdkTestObj.getResultDetails().strip().replace("\\n", "");
                    print "Device.Hosts.Host.%s.Active value is %s" %(i,details);
                    if expectedresult in actualresult and details == "true":
                        clientfound = 1;
                        instance = i;
                        break;
            if clientfound == 1:
                tdkTestObj = obj2.createTestStep('TDKB_TR181Stub_Get');
                expectedresult = "SUCCESS";
                actualresult,curlanMode = GetLanOperationalMode(tdkTestObj);
                if expectedresult in actualresult :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Get the LAN  mode";
                    print "EXPECTED RESULT 2: Should get the lan-mode"
                    print "ACTUAL RESULT 2:%s" %curlanMode
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    flag = 1;
                    if curlanMode != "bridge-static":
                        setValue = "bridge-static";
                        tdkTestObj = obj2.createTestStep('TDKB_TR181Stub_Set');
                        actualresult,details =SetLanOperationalMode(tdkTestObj,setValue);
                        if expectedresult in actualresult:
                            revertflag =1;
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP : Set the lanMode to bridge-static";
                            print "EXPECTED RESULT : Should set the lanMode to bridge-static";
                            print "ACTUAL RESULT : %s" %details;
                            print "[TEST EXECUTION RESULT] : SUCCESS" ;
                            time.sleep(90);
                        else:
                            flag =0 ;
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP : Set the lanMode to bridge-static";
                            print "EXPECTED RESULT : Should set the lanMode to bridge-static";
                            print "ACTUAL RESULT : %s" %details;
                            print "[TEST EXECUTION RESULT] : FAILURE" ;
                    if flag == 1:
                        #Script to load the configuration file of the component
                        tdkTestObj = obj.createTestStep("CMHAL_GetCPEList");
                        tdkTestObj.addParameter("lanMode","bridge-static")
                        expectedresult="FAILURE";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        instNum= details.split("InstNum :")[-1];
                        print details;
                        if expectedresult in actualresult and int(instNum) == 0:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 3: Get the cpe list";
                            print "EXPECTED RESULT 3: Should not get cpe list successfully";
                            print "ACTUAL RESULT 3: Instance number is:", instNum;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 3: Get the cpe list";
                            print "EXPECTED RESULT 3: Should not get cpe list successfully";
                            print "ACTUAL RESULT 3: Instance number is:", instNum;
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "****The LAN mode was not bridge-static  and failed on setting the mode to bridge-static";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 2: Get the LAN  mode";
                    print "EXPECTED RESULT 2: Should get the lan-mode"
                    print "ACTUAL RESULT 2:%s" %curlanMode
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "********No Ethernet client connected to DUT********";
            if revertflag == 1:
                 tdkTestObj = obj2.createTestStep('TDKB_TR181Stub_Set');
                 expectedresult ="SUCCESS";
                 actualresult,details =SetLanOperationalMode(tdkTestObj,deflanMode);
                 if expectedresult in actualresult:
                     tdkTestObj.setResultStatus("SUCCESS");
                     print "TEST STEP 4: Revert the lan mode to previous";
                     print "EXPECTED RESULT 4: Should revert lan mode to %s" %deflanMode;
                     print "ACTUAL RESULT 4: %s" %details;
                     print "[TEST EXECUTION RESULT] : SUCCESS";
                     time.sleep(90);
                 else:
                     tdkTestObj.setResultStatus("FAILURE");
                     print "TEST STEP 4: Revert the lan mode to previous";
                     print "EXPECTED RESULT 4: Should revert lan mode to %s" %deflanMode;
                     print "ACTUAL RESULT 4: %s" %details;
                     print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the no of clients connected";
            print "EXPECTED RESULT 1: Should get the no of clients connected greater than zero"
            print "ACTUAL RESULT 1:%s" %NoOfHost
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        print "The device was not in router mode setting device to router mode to check for connected clients failed";
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("cmhal");
    obj2.unloadModule("tdkbtr181");
else:
     print "Failed to load the module";
     obj.setLoadModuleStatus("FAILURE");
     obj2.setLoadModuleStatus("FAILURE");
     print "Module loading failed";
