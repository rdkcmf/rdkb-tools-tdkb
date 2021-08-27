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
  <version>3</version>
  <name>TS_OVSAgent_OVSDisabled_Check_OVSAndLinuxBridgeControls</name>
  <primitive_test_id/>
  <primitive_test_name>OVS_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if  brlan entries are present in brctl show and not in ovs-vsctl show  with ovs disabled</synopsis>
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
    <test_case_id>TC_OVSAGENT_05</test_case_id>
    <test_objective>To check if  brlan entries are present in brctl show and not in ovs-vsctl show  with ovs disabled</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.CodeBigFirst.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable
Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable</input_parameters>
    <automation_approch>1.Load the module
2.Disable code big and enable mesh as pre-requisite
3.Disable ovs and device will go for reboot
4.Query ovs-vsctl show and brctl show
5.brlan entries should not be present in ovs-vsctl show and present  in brctl show
6.Revert the set values
7.Unload the module</automation_approch>
    <expected_output>brlan entries should not be present in ovs-vsctl show and present  in brctl show  with ovs disabled</expected_output>
    <priority>High</priority>
    <test_stub_interface>OVS_AGENT</test_stub_interface>
    <test_script>TS_OVSAgent_OVSDisabled_Check_OVSAndLinuxBridgeControls</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkutility import *;
#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_OVSAgent_OVSDisabled_Check_OVSAndLinuxBridgeControls');
tr181obj.configureTestCase(ip,port,'TS_OVSAgent_OVSDisabled_Check_OVSAndLinuxBridgeControls');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

def ovs_PreRequisite(tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set):
    paramlist =["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.CodeBigFirst.Enable","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable"];
    default =[];
    result ="SUCCESS";
    for item in paramlist:
        def_result,default_value = getTR181Value(tdkTestObj_Tr181_Get,item);
        if expectedresult in def_result:
           default.append(default_value);
        else:
             result ="FAILURE";
             print "get operation failed for %s "%item;
             break;

    setValue = ["false","true"];
    print "\nThe default Values of CodeBig First and  Mesh are ",default;

    print "\n*****As a Pre-requisite Disabling CodeBig First and Enabling Mesh****";

    index =0;
    for item in paramlist:
        set_result, set_details = setTR181Value(tdkTestObj_Tr181_Set,item,setValue[index],"bool");
        if expectedresult in set_result:
           print "%s set %s successfully\n" %(item,setValue[index]);
           index = index + 1;
        else:
             result ="FAILURE";
             print "%s set %s  failed \n" %(item,setValue[index]);
             break;
    return result,default;

def ovs_PostProcess(tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,setValue):
    result ="SUCCESS";
    paramlist =["Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.CodeBigFirst.Enable","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable"];
    index = 0;
    for item in paramlist:
        set_result, set_details = setTR181Value(tdkTestObj_Tr181_Set,item,setValue[index],"bool");
        if expectedresult in set_result:
           print "%s set %s successfully\n" %(item,setValue[index]);
           index = index + 1;
        else:
             result ="FAILURE";
             print "%s set %s  failed \n" %(item,setValue[index]);
             break;
    return result;


def isOVSEnabled(tdkTestObj_Tr181_Get):
    expectedresult="SUCCESS";
    parameter_Name = "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable";
    def_result,default_value = getTR181Value(tdkTestObj_Tr181_Get,parameter_Name);
    return def_result,default_value;

def doEnableDisableOVS(enableFlag,sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set):
    expectedresult="SUCCESS";
    ovs_set = 0;
    revert_flag = 0;
    parameter_Name = "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable";
    def_result,default_value = isOVSEnabled(tdkTestObj_Tr181_Get);

    if  expectedresult in def_result:
        if default_value == enableFlag:
            ovs_set = 1;
            print "OVS Enable status is already ",enableFlag
        else:
            set_result, set_details = setTR181Value(tdkTestObj_Tr181_Set,parameter_Name,enableFlag,"bool");

            if expectedresult  in set_result:
                revert_flag = 1;
                print "TEST STEP : Set the OVS Enable status to ",enableFlag;
                print "EXPECTED RESULT :  Set Operation should be success";
                print "ACTUAL RESULT : Set operation was success";
                print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj_Tr181_Set.setResultStatus("SUCCESS");

                doRebootDUT(sysobj);

                get_result,get_details = getTR181Value(tdkTestObj_Tr181_Get,parameter_Name);

                if expectedresult  in get_result and get_details == enableFlag:
                    ovs_set = 1;
                    print "TEST STEP : Get the Enable Status of OVS ";
                    print "EXPECTED RESULT : Get operation should be success";
                    print "ACTUAL RESULT : OVS Enable status %s" %get_details;
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
                else:
                    revert_flag  = 0;
                    print "TEST STEP : Get the Enable Status of OVS ";
                    print "EXPECTED RESULT : Get operation should be success";
                    print "ACTUAL RESULT : Failed to get OVS Enable status";
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
            else:
                ovs_set = 0;
                print "TEST STEP : Set the OVS Enable status to ",enableFlag;
                print "EXPECTED RESULT :  Set Operation should be success";
                print "ACTUAL RESULT : Set operation Failed";
                print "[TEST EXECUTION RESULT] : FAILURE";
                tdkTestObj_Tr181_Set.setResultStatus("FAILURE");
    else:
        ovs_set = 0;
        print "[TEST EXECUTION RESULT] : FAILURE";
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");

    #ovs_set = 1 - Successful operation and revert_flag = 1 - initial OVS enable value was disabled
    return ovs_set,revert_flag;


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
        print "EXPECTED RESULT 2: OVS Status should be disable else disable it "

        ovs_set,revert_flag = doEnableDisableOVS("false",sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set);
        if ovs_set == 1:
            ovs_enabled = 1;
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: OVS Enable status set to false"
            print "[TEST EXECUTION RESULT] 2: SUCCESS";

            query="ovs-vsctl show | grep -i \"brlan\"";
            print "query:%s" %query
            tdkTestObj = tdkTestObj_Sys_ExeCmd;
            tdkTestObj.addParameter("command", query)
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult1 = tdkTestObj.getResult();
            ovs = tdkTestObj.getResultDetails().strip().replace("\\n","");

            query="brctl show | grep -i \"brlan\"";
            print "query:%s" %query
            tdkTestObj = tdkTestObj_Sys_ExeCmd;
            tdkTestObj.addParameter("command", query)
            expectedresult2="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult2 = tdkTestObj.getResult();
            brctl = tdkTestObj.getResultDetails().strip().replace("\\n","");
            if expectedresult in (actualresult1 and actualresult2):
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3 : Check for brlan entries in OVS  and Linux bridge controls";
                print "EXPECTED RESULT 3: Should get  brlan entries in OVS  and Linux bridge controls";
                print "ACTUAL RESULT 3: ovs : %s,brctl :%s"%(ovs,brctl);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                if ovs == "" and brctl!= "" :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4 : Check for brlan entries in OVS  and Linux bridge controls";
                    print "EXPECTED RESULT 4: Should get  brlan entries in OVS  and Linux bridge controls as empty and non-empty respectively";
                    print "ACTUAL RESULT 4: ovs : %s,brctl :%s"%(ovs,brctl);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Check for brlan entries in OVS  and Linux bridge controls";
                    print "EXPECTED RESULT 4: Should get  brlan entries in OVS  and Linux bridge controls as empty and non-empty respectively";
                    print "ACTUAL RESULT 4: ovs : %s,brctl :%s"%(ovs,brctl);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3 : Check for brlan entries in OVS  and Linux bridge controls";
                print "EXPECTED RESULT 3: Should get  brlan entries in OVS  and Linux bridge controls";
                print "ACTUAL RESULT 3: ovs : %s,brctl :%s"%(ovs,brctl,ifconfig_ip);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
             ovs_enabled = 0
             print "ACTUAL RESULT 2: OVS status disable operation failed";
             print "[TEST EXECUTION RESULT] 2: FAILURE";
             tdkTestObj_Tr181_Get.setResultStatus("FAILURE");

        actualresult = ovs_PostProcess(tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,default);
        if expectedresult in actualresult:
            print "TEST STEP 5: Set Code Big and Mesh Enable Status value to initial value",;
            print "EXPECTED RESULT 5: Revert operation should be success";
            print "ACTUAL RESULT 5: REvert operation was success";
            print "[TEST EXECUTION RESULT] 7: SUCCESS";
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        else:
            print "TEST STEP 5: Set Code Big and Mesh Enable Status value to initial value",;
            print "EXPECTED RESULT 5: Revert operation should be success";
            print "ACTUAL RESULT 5: REvert operation was Failed";
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
            print "TEST STEP 6: Set the OVS enable status to False"
            print "EXPECTED RESULT 6: Should Set the OVS Enable Status of False"
            print "ACTUAL RESULT 6: OVS Enable Status set to False"
            print "[TEST EXECUTION RESULT] 1: SUCCESS";
            tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        else:
            print "TEST STEP 6: Set the OVS enable status to False"
            print "EXPECTED RESULT 6: Should Set the OVS Enable Status of False"
            print "ACTUAL RESULT 6: Failed to set OVS Enable Status to False"
            print "[TEST EXECUTION RESULT] 1: FAILURE";
            tdkTestObj_Tr181_Get.setResultStatus("FAILURE");

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");
