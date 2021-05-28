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
  <version>8</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WANMANAGER_SetWanManagerPolicy_PrimaryPriority_OnBootup</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set Device.X_RDK_WanManager.Policy to PRIMARY_PRIORITY_ON_BOOTUP and check if the required logs are found in WANMANAGERlog.txt on bootup.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
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
    <test_case_id>TC_WANMANAGER_11</test_case_id>
    <test_objective>To set Device.X_RDK_WanManager.Policy to PRIMARY_PRIORITY_ON_BOOTUP and check if the required logs are found in WANMANAGERlog.txt on bootup.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub
Sysutil_Stub</api_or_interface_used>
    <input_parameters>Device.X_RDK_WanManager.Policy : PRIMARY_PRIORITY_ON_BOOTUP</input_parameters>
    <automation_approch>1. Load the module
2. Get the value of Device.X_RDK_WanManager.Policy
3. Set Device.X_RDK_WanManager.Policy to PRIMARY_PRIORITY_ON_BOOTUP. The device is expected to go for a reboot after the set operation
4. Once the device comes up, query Device.X_RDK_WanManager.Policy and verify the set value is same as get value
5. In /rdklogs/logs/WANMANAGERLog.txt.0 check if all the required logs are present
6. Unload the module</automation_approch>
    <expected_output>Setting Device.X_RDK_WanManager.Policy to PRIMARY_PRIORITY_ON_BOOTUP should be success and the required logs are found in WANMANAGERlog.txt on bootup.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_SetWanManagerPolicy_PrimaryPriority_OnBootup</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from WanManager_Utility import *
from tdkbVariables import *;
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_SetWanManagerPolicy_PrimaryPriority_OnBootup');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_SetWanManagerPolicy_PrimaryPriority_OnBootup');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    step = 1;
    status, policy_initial = get_policy(tdkTestObj, step);
    if status == 0:
        step = step + 1;
        status = is_policy_expected(tdkTestObj, policy_initial, step);
        if status == 0:
            #Set the Wan Manager Policy to PRIMARY_PRIORITY_ON_BOOTUP
            new_policy = "PRIMARY_PRIORITY_ON_BOOTUP"
            expectedresult="SUCCESS";
            print "Setting the wanmanager policy to :%s"%new_policy
            revert = 0
            set_policy(new_policy, policy_initial, obj1, revert);
            #Get the WANMANAGER POLICY and cross check with the Set value
            step = step + 1;
            status, policy = get_policy(tdkTestObj, step);
            if status == 0:
                if policy == new_policy:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "The wanmanager policy is set successfully"
                    #check if the required logs are present
                    log_file = "/rdklogs/logs/WANMANAGERLog.txt.0"
                    log = "Primary Priority On Bootup Policy Thread Starting"
                    result = [];
                    print "\n***Checking if %s message is present in WANMANAGERLog.txt.0***" %log;
                    query="grep -rin \"%s\" \"%s\"" %(log,log_file);
                    print "query:%s" %query
                    tdkTestObj2 = obj1.createTestStep('ExecuteCmd');
                    tdkTestObj2.addParameter("command", query)
                    expectedresult="SUCCESS";
                    tdkTestObj2.executeTestCase(expectedresult);
                    actualresult = tdkTestObj2.getResult();
                    details = tdkTestObj2.getResultDetails().strip().replace("\\n","");
                    step = step + 1;
                    print "TEST STEP %d : Check if the expected log is present in /rdklogs/logs/WANMANAGERLog.txt.0" %step;
                    print "EXPECTED RESULT %d : The expected log is present in /rdklogs/logs/WANMANAGERLog.txt.0 " %step;
                    result.append(details);
                    revert = 1;
                    if (len(details) != 0)  and  log in details:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : The expected log is present in /rdklogs/logs/WANMANAGERLog.txt.0 :%s"%(step, result);
                        print "[TEST EXECUTION RESULT]  : SUCCESS";
                        set_policy(new_policy, policy_initial, obj1, revert);
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : The expected log is not present in /rdklogs/logs/WANMANAGERLog.txt.0 :%s"%(step, result);
                        print "[TEST EXECUTION RESULT] : FAILURE";
                        set_policy(new_policy, policy_initial, obj1, revert);
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "The wanmanager policy is not set successfully"
            else:
                pass;
        else:
            pass;
    else:
        pass;
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
