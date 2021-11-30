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
  <version>7</version>
  <name>TS_PAM_CheckIPTableRules_InRouterMode_RemoteMgmtDisabled</name>
  <primitive_test_id/>
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the required ITPTABLE rules are present when the DUT is in router mode with Remote Management(HTTP Enable and HTTPS Enable) disabled.</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_216</test_case_id>
    <test_objective>To check if the required ITPTABLE rules are present when the DUT is in router mode with Remote Management(HHTP Enable and HTTPS Enable) disabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
paramName : Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable
paramName : Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpsEnable
lan_mode = router
http_enable = false
https_enable = false</input_parameters>
    <automation_approch>1. Load the modules
2. Check if the initial values of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode,
Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable and
Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpsEnable are router, false, false respectively. If not, perform a set operation to set them to the required values.
3. Cross verify SET operation with GET.
4. Retrieve the IPTABLE rules required to be present in the DUT when Lan Mode is router and the Remote Management is disabled from the platform properties file.
5. Check if the required IPTABLE rules are populated in DUT.
6. Revert to initial state if needed.
7. Unload the modules.</automation_approch>
    <expected_output>The required ITPTABLE rules should be present when the DUT is in router mode with Remote Management(HHTP Enable and HTTPS Enable) disabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_CheckIPTableRules_InRouterMode_RemoteMgmtDisabled</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def verify_iptable_rules(tdkTestObj, step):
    rulesFound = 0;
    cmd = "sh %s/tdk_utility.sh parseConfigFile IPTABLE_RULES_ROUTER_REMOTEDISABLED  | tr \"\n\" \"  \"" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj.addParameter("command", cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d: Get the IPTABLE rules from platform property file" %step;
    print "EXPECTED RESULT %d: Should successfully get the IPTABLE rules" %step;

    if expectedresult in actualresult and details!= "":
        iptable_list = details.split(",");
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: IPTABLE rules are fetched; Details: %s" %(step, details);
        print "[TEST EXECUTION RESULT] : SUCCESS";

        for list in iptable_list:
            cmd = "iptables-save | grep  -ire \"%s\"" %list;
            print "\n%s" %cmd;
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            if expectedresult in actualresult and details == list:
                rulesFound = 1;
                print "Iptable Rule %s is present"%list
            else:
                rulesFound = 0;
                print "Iptable Rule %s is NOT present"%list
                break;
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: IPTABLE rules are not fetched; Details: %s" %(step, details);
        print "[TEST EXECUTION RESULT] : FAILURE";
    return rulesFound,actualresult;

def checkIPTableRules(result, actualresult, expectedresult, step):
    print "\nTEST STEP %d: Verify IPTABLE rules for Router Mode with Remote Access Disabled" %step;
    print "EXPECTED RESULT %d: The IPTABLE rules specific to the scenario should be present" %step;

    if result == 1 and expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL TEST %d: Verification on the IPTABLE rules specific to the scenario is success" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL TEST %d: Verification on the IPTABLE rules specific to the scenario failed" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"
    return;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
import time;
from tdkbVariables import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj2 = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_CheckIPTableRules_InRouterMode_RemoteMgmtDisabled');
obj1.configureTestCase(ip,port,'TS_PAM_CheckIPTableRules_InRouterMode_RemoteMgmtDisabled');
obj2.configureTestCase(ip,port,'TS_PAM_CheckIPTableRules_InRouterMode_RemoteMgmtDisabled');

#Get the result of connection with test component and DUT
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();
loadmodulestatus3 =obj2.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() and "SUCCESS" in loadmodulestatus3.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    obj2.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    tdkTestObj = obj.createTestStep('TADstub_Get');
    paramList=["Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode", "Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable", "Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpsEnable"]
    tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)
    print "\nTEST STEP 1: Get the initial values of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode, Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable and Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpsEnable";
    print "EXPECTED RESULT 1 : The values should be retrieved successfully";

    if expectedresult in status and orgValue[0] != "" and orgValue[1] != "" and orgValue[2] != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: LanMode is : %s, HTTP Enable is : %s, HTTPS Enable is : %s " %(orgValue[0],orgValue[1], orgValue[2]) ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if orgValue[0] == "router" and orgValue[1] == "false" and orgValue[2] == "false":
            print "Set operation not required as Lan Mode, HTTP Enable and HTTPS Enable have expected values initially";
            #Verify IPTABLE rules
            step = 2;
            tdkTestObj = obj2.createTestStep('ExecuteCmd');
            rulesFound,actualresult = verify_iptable_rules(tdkTestObj, step);
            step = step + 1;
            checkIPTableRules(rulesFound, actualresult, expectedresult, step);
        else :
            #values to be set
            http_enable = "false";
            https_enable = "false";
            lan_mode = "router";

            tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
            tdkTestObj.addParameter("paramList", "Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable|%s|boolean|Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpsEnable|%s|boolean|Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode|%s|string"%(http_enable,https_enable,lan_mode));
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            sleep(10);
            print "\nTEST STEP 2 : Set Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable to %s, Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable to %s and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to %s" %(http_enable, https_enable, lan_mode);
            print "EXPECTED RESULT 2 : SET operations should be success";

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Set operation success; Details : %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS";

                #Validate the SET with GET
                tdkTestObj,status,setValue = getMultipleParameterValues(obj,paramList)
                print "\nTEST STEP 3: Get the values of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode, Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable and Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpsEnable";
                print "EXPECTED RESULT 3: The values should be retrieved successfully and should be the same as set values";

                if expectedresult in status and setValue[0] == lan_mode and setValue[1] == http_enable and setValue[2] == https_enable:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: Values after the GET are same as the SET values : %s, %s, %s" %(setValue[0],setValue[1],setValue[2]) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Verify IPTABLE rules
                    step = 4;
                    tdkTestObj = obj2.createTestStep('ExecuteCmd');
                    rulesFound,actualresult = verify_iptable_rules(tdkTestObj, step);
                    step = step + 1;
                    checkIPTableRules(rulesFound, actualresult, expectedresult, step);

                    #Revert to initial values
                    print "\nReverting to initial state...";
                    tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
                    tdkTestObj.addParameter("paramList", "Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable|%s|boolean|Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpsEnable|%s|boolean|Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode|%s|string"%(orgValue[1],orgValue[2], orgValue[0]));
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    sleep(60);
                    print "\nTEST STEP 6 : Set Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable to %s, Device.UserInterface.X_CISCO_COM_RemoteAccess.HttpEnable to %s and Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode to %s" %(orgValue[1],orgValue[2], orgValue[0]);
                    print "EXPECTED RESULT 6 : SET operations should be success";

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 6: Set operation success; Details : %s" %details;
                        print "TEST EXECUTION RESULT :SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 6:Set operation failed; Details : %s" %details;
                        print "TEST EXECUTION RESULT :FAILURE";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: Values after the GET are not same as the SET values : %s, %s, %s" %(setValue[0],setValue[1],setValue[2]) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2:Set operation failed; Details : %s" %details;
                print "TEST EXECUTION RESULT :FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: GET operation failed";
        print "TEST EXECUTION RESULT :FAILURE";

    obj.unloadModule("tad");
    obj1.unloadModule("tdkbtr181");
    obj2.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    obj2.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
