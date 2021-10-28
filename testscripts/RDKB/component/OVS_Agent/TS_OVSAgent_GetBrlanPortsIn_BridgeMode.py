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
  <name>TS_OVSAgent_GetBrlanPortsIn_BridgeMode</name>
  <primitive_test_id/>
  <primitive_test_name>OVS_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if  all expected brlan ports are present after enabling ovs in bridge-static mode</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_OVSAGENT_12</test_case_id>
    <test_objective>To check if  all expected brlan ports are present after enabling ovs in bridge mode</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.CodeBigFirst.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable</input_parameters>
    <automation_approch>1.Load the module
2.Disable code big and enable mesh as pre-requisite
3.Check if ovs is enabled else enable it
4.Get the expected configured values for brlan ports
5.Check if the device is in bridge mode , else bring it to bridge mode
6.Get brlan interfaces using (ovs-vsctl list-ports brlan0) command and verify all the expected entries are present
7.Revert the set values
8.Unload the module</automation_approch>
    <expected_output>with ovs enabled and device in bridge mode all the expected brlan entries needs to be present</expected_output>
    <priority>High</priority>
    <test_stub_interface>OVS_Agent</test_stub_interface>
    <test_script>TS_OVSAgent_GetBrlanPortsIn_BridgeMode</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkutility import *;
from tdkbVariables import *;
#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_OVSAgent_GetBrlanPortsIn_BridgeMode');
tr181obj.configureTestCase(ip,port,'TS_OVSAgent_GetBrlanPortsIn_BridgeMode');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();
revert_flag =0;
orgLanMode="";

def setLanMode(mode, obj):
    expectedresult = "SUCCESS"
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_SetOnly');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    tdkTestObj.addParameter("ParamValue", mode)
    tdkTestObj.addParameter("Type","string")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP : Change lanmode to %s" %mode
        print "EXPECTED RESULT : Should change lanmode to %s" %mode
        print "ACTUAL RESULT : Details: %s " %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        sleep(90)
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        newValue= tdkTestObj.getResultDetails();
        if expectedresult in actualresult and newValue==mode:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP : Get the current lanMode"
            print "EXPECTED RESULT : Should retrieve the current lanMode"
            print "ACTUAL RESULT : Lannmode is %s" %newValue;
            print "[TEST EXECUTION RESULT] : SUCCESS";
            return "SUCCESS"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : Get the current lanMode"
            print "EXPECTED RESULT : Should retrieve the current lanMode"
            print "ACTUAL RESULT : Lanmode is %s" %newValue;
            print "[TEST EXECUTION RESULT] : FAILURE";
            return "FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP : Change lanmode to %s" %mode
        print "EXPECTED RESULT : Should change lanmode to %s" %mode
        print "ACTUAL RESULT : Details: %s " %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
        return "FAILURE"

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_Set = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');

    result,default = ovs_PreRequisite(tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set);

    if expectedresult in result:
        print "TEST STEP 1:  Get the Code Big and Mesh status as disabled and enabled respectively else set it to expected value";
        print "EXPECTED RESULT 1: Should get the Code Big and Mesh status as disabled and enabled respectively else set it to expected value";
        print "ACTUAL RESULT 1 : The Code Big and Mesh status are as expected";
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

        print "\n\n";
        print "TEST STEP 2: Get the OVS status"
        print "EXPECTED RESULT 2: OVS Status should be enabled else enable it "

        ovs_set,revert_flag = doEnableDisableOVS("true",sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set);
        if ovs_set == 1:
            ovs_enabled = 1;
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: OVS Enable status set to true"
            print "[TEST EXECUTION RESULT] 2: SUCCESS";


            tdkTestObj = tdkTestObj_Sys_ExeCmd;
            cmd = "sh %s/tdk_utility.sh parseConfigFile OVS_Bridge_Port" %TDK_PATH;
            print cmd;
            expectedresult="SUCCESS";
            tdkTestObj.addParameter("command", cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            if expectedresult in actualresult  and details!= "":
                details = details.split(",");
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Execute the command";
                print "EXPECTED RESULT 2: Should execute the command successfully";
                print "ACTUAL RESULT 2: Details: %s" %details;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                print "TEST STEP 3: Get the Ovs vsctl br list";
                print "EXPECTED RESULT 3:  Should get the expected br lists";

                tdkTestObj = tdkTestObj_Tr181_Get;
                tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                orgLanMode= tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP : Get the current lanMode"
                    print "EXPECTED RESULT : Should retrieve the current lanMode"
                    print "ACTUAL RESULT : Lanmode is %s" %orgLanMode;
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if "bridge-static" != orgLanMode:
                        actualresult = setLanMode("bridge-static", tr181obj);

                if expectedresult in actualresult:
                    for item in details:
                        tdkTestObj=tdkTestObj_Sys_ExeCmd;
                        query="ovs-vsctl list-ports brlan0 | grep \"%s\""%item;
                        print "query:%s" %query
                        tdkTestObj.addParameter("command", query)
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                        if (len(details) != 0)  and  item in details:
                           tdkTestObj.setResultStatus("SUCCESS");
                           print "%s is present "%item;
                           print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            print "%s is not present " %item;
                            tdkTestObj.setResultStatus("FAILURE");
                            print "[TEST EXECUTION RESULT] : FAILURE";
                            break;
                else:
                     print "Failed to change LAN mode";
        else:
             ovs_enabled = 0
             print "ACTUAL RESULT 2: OVS status enable operation failed";
             print "[TEST EXECUTION RESULT] 2: FAILURE";
             tdkTestObj_Tr181_Get.setResultStatus("FAILURE");

        actualresult = ovs_PostProcess(tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,default);
        if expectedresult in actualresult:
            print "TEST STEP 4: Set Code Big and Mesh Enable Status value to initial value",;
            print "EXPECTED RESULT 4: Revert operation should be success";
            print "ACTUAL RESULT 4: REvert operation was success";
            print "[TEST EXECUTION RESULT] 7: SUCCESS";
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        else:
            print "TEST STEP 4: Set Code Big and Mesh Enable Status value to initial value",;
            print "EXPECTED RESULT 4: Revert operation should be success";
            print "ACTUAL RESULT 4: REvert operation was Failed";
            print "[TEST EXECUTION RESULT] 5: FAILURE";
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
    else:
        print "TEST STEP 1:  Get the Code Big and Mesh status as disabled and enabled respectively else set it to expected value";
        print "EXPECTED RESULT 1: Should get the Code Big and Mesh status as disabled and enabled respectively else set it to expected value";
        print "ACTUAL RESULT 1 : The Code Big and Mesh status are as expected";
        print "[TEST EXECUTION RESULT] : FAILURE";
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");


    #Revert Flag will set to 1 only when initial value was false, so disable the OVS using doEnableDisableOVS function
    if revert_flag == 1:
        ovs_set,revert_flag = doEnableDisableOVS("false",sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set);
        if ovs_set == 1:
            print "TEST STEP 5: Set the OVS enable status to False"
            print "EXPECTED RESULT 5: Should Set the OVS Enable Status of False"
            print "ACTUAL RESULT 5: OVS Enable Status set to False"
            print "[TEST EXECUTION RESULT] 1: SUCCESS";
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        else:
            print "TEST STEP 5: Set the OVS enable status to False"
            print "EXPECTED RESULT 5: Should Set the OVS Enable Status of False"
            print "ACTUAL RESULT 5: Failed to set OVS Enable Status to False"
            print "[TEST EXECUTION RESULT] 1: FAILURE";
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");


    if "bridge-static" != orgLanMode:
        actualresult = setLanMode("router", tr181obj)

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
