##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_NotifyComp_CheckProcessCrash</name>
  <primitive_test_id/>
  <primitive_test_name>NotifyComp_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check whether notify comp is running after setting Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client to false</synopsis>
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
    <test_case_id>TC_NotifyComp_01</test_case_id>
    <test_objective>To check whether notify comp is running after setting Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client to false</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client</input_parameters>
    <automation_approch>1. Load module
2.Check if notify comp is running
3.Set Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client to false
4.Check if notify comp is running
5.Unload module</automation_approch>
    <except_output>notify comp should be running after setting Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client to false</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_NotifyComp_CheckProcessCrash</test_script>
    <skipped>No</skipped>
    <release_version>M68</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");


#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_NotifyComp_CheckProcessCrash');
obj1.configureTestCase(ip,port,'TS_NotifyComp_CheckProcessCrash');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

    #check whether the process is running or not
    query="sh %s/tdk_platform_utility.sh checkProcess notify_comp" %TDK_PATH
    print "query:%s" %query
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", query)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase("SUCCESS");
    actualresult = tdkTestObj.getResult();
    pid = tdkTestObj.getResultDetails().strip().replace("\\n","");
    if expectedresult in actualresult and pid:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1:Check notify_comp process";
        print "EXPECTED RESULT 1: notify_comp process should be running";
        print "ACTUAL RESULT 1: PID of notify_comp %s" %pid;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
        tdkTestObj.addParameter("ParamName","Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client");
        tdkTestObj.addParameter("ParamValue","false");
        tdkTestObj.addParameter("Type","string");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult1 = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        #check whether the process is running or not
        query="sh %s/tdk_platform_utility.sh checkProcess notify_comp" %TDK_PATH
        print "query:%s" %query
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.addParameter("command", query)
        tdkTestObj.executeTestCase("SUCCESS");
        newpid = tdkTestObj.getResultDetails().strip().replace("\\n","");
        actualresult2 = tdkTestObj.getResult();
        if expectedresult in actualresult2 and newpid:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2:Check notify_comp process after setting Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client to false";
            print "EXPECTED RESULT 2: notify_comp process should be running";
            print "ACTUAL RESULT 2: PID of notify_comp %s" %newpid;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            if expectedresult not in actualresult1:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:Check if setting Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client to false returns failure";
                print "EXPECTED RESULT 3: setting Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client to false should return failure";
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3:Check if setting Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client to false returns failure";
                print "EXPECTED RESULT 3: setting Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client to false should return failure";
                print "ACTUAL RESULT 3: Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client is set to false ";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2:Check notify_comp process after setting Device.NotifyComponent.X_RDKCENTRAL-COM_Connected-Client to false";
            print "EXPECTED RESULT 2: notify_comp process should be running";
            print "ACTUAL RESULT 2:notify_comp is not running" ;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:Check notify_comp process";
        print "EXPECTED RESULT 1: notify_comp process should be running";
        print "ACTUAL RESULT 1: notify_comp process is not running";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("sysutil");
    obj1.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

