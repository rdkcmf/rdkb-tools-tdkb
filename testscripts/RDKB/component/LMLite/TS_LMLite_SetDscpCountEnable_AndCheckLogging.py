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
  <version>18</version>
  <name>TS_LMLite_SetDscpCountEnable_AndCheckLogging</name>
  <primitive_test_id/>
  <primitive_test_name>LMLiteStub_Set_Get</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable can be set to a comma separated valid list of DSCP WAN values and if the required log lines are present in LM.txt.0 upon successful set operation.</synopsis>
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
    <test_case_id>TC_LMLite_24</test_case_id>
    <test_objective>To check if Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable can be set to a comma separated valid list of DSCP WAN values and if the required log lines are present in LM.txt.0 upon successful set operation.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable
paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
paramName/ParamName  : Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable
ParamValue : "0,8,28,24,44"
ParamType : string</input_parameters>
    <automation_approch>1. Load the modules
2. As pre-requisite, check if the DUT is in RBUS enabled mode. Also check if the Lan Mode is router, if not set to router and validate the set operation.
3. Get the initial DSCP enabled values for WAN traffic counts using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable and store it.
4. Set the DSCP enabled values to the comma separated list "0,8,28,24,44" using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable and validate with get operation.
5. Check if the log file LM.txt.0 is present under /rdklogs/logs/
6. Check if "CheckIfValidDscp - Valid dscp = [DSCP];" is present in LM.txt.0 for each of the DSCP enabled values.
7. Then check if "CosaSetCfg - syscfg_set DscpEnabledList_1:0,8,28,24,44 success" is present in LM.txt.0.
8. Revert Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable to initial values and validate with get operation.
9. Revert the pre-requisites set if required.
10. Unload the modules</automation_approch>
    <expected_output>Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable should be set to a comma separated valid list of DSCP WAN values the required log lines should be present in LM.txt.0 upon successful set operation.</expected_output>
    <priority>High</priority>
    <test_stub_interface>lmlite</test_stub_interface>
    <test_script>TS_LMLite_SetDscpCountEnable_AndCheckLogging</test_script>
    <skipped>No</skipped>
    <release_version>M104</release_version>
    <remarks/>
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
obj = tdklib.TDKScriptingLibrary("lmlite","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_LMLite_SetDscpCountEnable_AndCheckLogging');
obj.configureTestCase(ip,port,'TS_LMLite_SetDscpCountEnable_AndCheckLogging');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if  "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Check the Pre-requisites for WAN Traffic Counts
    step = 1;
    pre_req_set, tdkTestObj, step, revert_flag, initial_lanmode = CheckWANTrafficCountsPre_requisite(obj, step);

    if pre_req_set == 1:
        print "\n*************RFC Pre-requisite set for the DUT*****************";

        #Get the initial DscpCountEnable value
        step = step + 1;
        print "\nTEST STEP %d : Get the initial DSCP Count Enable using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable" %(step);
        print "EXPECTED RESULT %d : DSCP count enable should be retrieved successfully" %step;

        tdkTestObj = obj.createTestStep("LMLiteStub_Get");
        tdkTestObj.addParameter("paramName","Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        initial_dscp = tdkTestObj.getResultDetails();

        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d : DSCP count enable retrieved successfully" %step;
            print "Initial DSCP Count Enable : %s" %initial_dscp;
            print "TEST EXECUTION RESULT : SUCCESS";

            #Set DscpCountEnable to a comma separarted string of valid DSCP values in the range 0-63
            step = step + 1;
            dscpCountEnable = ["0", "8", "28", "24", "44"];
            dscpCountEnable_str = "0,8,28,24,44";
            print "\nTEST STEP %d : Set the DSCP Count Enable using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable to %s and validate the operation" %(step, dscpCountEnable_str);
            print "EXPECTED RESULT %d : DSCP count enable set validation should be success" %step;

            tdkTestObj = obj.createTestStep("LMLiteStub_Set_Get");
            tdkTestObj.addParameter("ParamName","Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable");
            tdkTestObj.addParameter("ParamValue",dscpCountEnable_str);
            tdkTestObj.addParameter("ParamType","string");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : DSCP count enable set operation success; Details : %s" %(step, details);
                print "TEST EXECUTION RESULT : SUCCESS";

                #Check if LM.txt.0 is present under /rdklogs/logs
                step = step + 1;
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                cmd = "[ -f /rdklogs/logs/LM.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                print "\nTEST STEP %d: Check for LM.txt.0 log file presence under /rdklogs/logs" %step;
                print "EXPECTED RESULT %d: LM.txt.0 log file should be present under /rdklogs/logs" %step;

                if details == "File exist":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: LM.txt.0 log file is present" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Check if "CheckIfValidDscp" logs are present in LM.txt.0
                    sleep(10);
                    step = step + 1;
                    flag = 0;
                    print "\nTEST STEP %d: Check if \"CheckIfValidDscp\" logs are present in LM.txt.0 for each of the DSCP values" %step;
                    print "EXPECTED RESULT %d: \"CheckIfValidDscp\" logs should be present in LM.txt.0 for each of the DSCP values" %step;

                    for dscpCount in dscpCountEnable:
                        print "\n-----For the DSCP value %s-----" %dscpCount;
                        log = "CheckIfValidDscp - Valid dscp = " + dscpCount;
                        cmd = "grep -ire " + "\"" + log + "\"" + " /rdklogs/logs/LM.txt.0";
                        print cmd;
                        tdkTestObj.addParameter("command",cmd);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                        if expectedresult in actualresult and details != "":
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "Log found : %s" %details;
                        else:
                            flag = 1;
                            tdkTestObj.setResultStatus("FAILURE");
                            print "Log NOT found : %s" %details;

                    if flag == 0:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: \"CheckIfValidDscp\" logs are present in LM.txt.0 for each of the DSCP values" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Check if "CosaSetCfg - syscfg_set DscpEnabledList_1" log is present in LM.txt.0
                        step = step + 1;
                        print "\nTEST STEP %d: Check if \"CosaSetCfg - syscfg_set DscpEnabledList_1\" log is present in LM.txt.0" %step;
                        print "EXPECTED RESULT %d: \"CosaSetCfg - syscfg_set DscpEnabledList_1\" log should be present in LM.txt.0" %step;

                        log = "CosaSetCfg - syscfg_set DscpEnabledList_1:" + dscpCountEnable_str + " success";
                        cmd = "grep -ire " + "\"" + log + "\"" + " /rdklogs/logs/LM.txt.0";
                        print cmd;
                        tdkTestObj.addParameter("command",cmd);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                        if expectedresult in actualresult and details != "":
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Log present : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Log NOT present : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: \"CheckIfValidDscp\" logs are NOT present in LM.txt.0 for each of the DSCP values" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: LM.txt.0 log file is NOT present" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert DscpCountEnable to initial value
                step = step + 1;
                print "\nTEST STEP %d : Revert the DSCP Count Enable using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable" %step;
                print "EXPECTED RESULT %d : DSCP count enable revert operation should be success" %step;

                tdkTestObj = obj.createTestStep("LMLiteStub_Set_Get");
                tdkTestObj.addParameter("ParamName","Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable");
                tdkTestObj.addParameter("ParamValue",initial_dscp);
                tdkTestObj.addParameter("ParamType","string");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : DSCP count enable revert operation success; Details : %s" %(step, details);
                    print "TEST EXECUTION RESULT : SUCCESS";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : DSCP count enable revert operation failed; Details : %s" %(step, details);
                    print "TEST EXECUTION RESULT : FAILURE";
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : DSCP count enable set operation failed; Details : %s" %(step, details);
                print "TEST EXECUTION RESULT : FAILURE";
        else :
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d : DSCP count enable NOT retrieved successfully" %step;
            print "TEST EXECUTION RESULT : FAILURE";

        #Revert the Pre-requisites for WAN Traffic Counts
        step = step + 1;
        status = RevertWANTrafficCountsPre_requisite(obj, step, revert_flag, initial_lanmode)

        if status == 1:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "Revert operations completed successfully";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "Revert operations NOT completed successfully";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "Pre-Requisite is not set successfully";

    sysobj.unloadModule("sysutil");
    obj.unloadModule("lmlite");
else:
    print "Failed to load sysutil/lmlite module";
    sysobj.setLoadModuleStatus("FAILURE");
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
