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
  <version>1</version>
  <name>TS_PAM_DisableRFC_DLCaStoreEnable</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterNames</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To disable the DLCa Store Enable and check if the same is logged in PAM log file</synopsis>
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
    <test_case_id>TC_PAM_209</test_case_id>
    <test_objective>To  Disable  the RFC  DLCA Store Enable and check if the set logging is present is PAMLog.txt.0</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>pam_SetParameterValues
pam_GetParameterValues</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable</input_parameters>
    <automation_approch>1.Load the module
2.Get the current RFC  DLCA Store Enable status
3.Disable the RFC  DLCA Store Enable status
4.Get the value via syscfg and tr181 parameter and check if set is reflected
5.Check if  DLCA enable logging is present in PAMLog.txt.0
6.Revert the value to previous
7.Unload the module</automation_approch>
    <expected_output>Disabling DLCA RFC should be successful and the same logging should take place in PAMLog.txt.0</expected_output>
    <priority>High</priority>
    <test_stub_interface>PAM</test_stub_interface>
    <test_script>TS_PAM_DisableRFC_DLCaStoreEnable</test_script>
    <skipped>No</skipped>
    <release_version>M88</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
pamobj = tdklib.TDKScriptingLibrary("pam","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_PAM_DisableRFC_DLCaStoreEnable');
sysobj.configureTestCase(ip,port,'TS_PAM_DisableRFC_DLCaStoreEnable');

#Get the result of connection with test component and DUT
pamloadmodulestatus =pamobj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %pamloadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

if  "SUCCESS" in pamloadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    paramName ="Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable";
    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName",paramName);
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    initial_value = tdkTestObj.getResultDetails().strip();

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get current value of RFC DLCaStore Enable"
        print "EXPECTED RESULT 1: Should get current value of RFC DLCaStore Enable"
        print "ACTUAL RESULT 1: current value is %s" %initial_value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        setValue ="false";
        tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
        tdkTestObj.addParameter("ParamName",paramName);
        tdkTestObj.addParameter("ParamValue",setValue);
        tdkTestObj.addParameter("Type","boolean");
        expectedresult="SUCCESS";
        #Execute testcase on DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        result = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set  RFC DLCaStore Enable status to %s"%setValue;
            print "EXPECTED RESULT 2: Should set  RFC DLCaStore Enable status to %s" %setValue;
            print "ACTUAL RESULT 2: %s" %result;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
            tdkTestObj.addParameter("ParamName",paramName);
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase("expectedresult");
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip();

            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            expectedresult="SUCCESS";
            cmd= "syscfg get DLCaStoreEnabled";
            print cmd;
            expectedresult="SUCCESS";
            tdkTestObj.addParameter("command", cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult1 = tdkTestObj.getResult();
            syscfGet = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            if expectedresult in (actualresult and actualresult1)and  syscfGet == details and details == setValue:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3 : Get the RFC DLCaStore Enable status via syscfg and tr181, check if its equal to set value";
                print "EXPECTED RESULT 3: RFC DLCaStore Enable status should be equal to that of set value";
                print "ACTUAL RESULT 3: getValue :%s ,setvalue:%s,syscfg get value %s"%(details,setValue,syscfGet);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                sleep(3);
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                expectedresult="SUCCESS";
                cmd= "cat /rdklogs/logs/PAMlog.txt.0 |  grep -rn \"ProcessRfcSet : paramFullName=Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.DLCaStore.Enable, value=false, clearDB=0\"";
                print cmd;
                expectedresult="SUCCESS";
                tdkTestObj.addParameter("command", cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult and details:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4 : Check if set operation is logged in PAM log file";
                    print "EXPECTED RESULT 4 : The log message for RFC set should be logged in log file ";
                    print"ACTUAL RESULT 4 :%s" %details;
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4 : Check if set operation is logged in PAM log file";
                    print "EXPECTED RESULT 4 : The log message for RFC set should be logged in log file ";
                    print"ACTUAL RESULT 4 :%s" %details;
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3 : Get the RFC DLCaStore Enable status via syscfg and tr181, check if its equal to set value";
                print "EXPECTED RESULT 3: RFC DLCaStore Enable status should be equal to that of set value";
                print "ACTUAL RESULT 3: getValue :%s ,setvalue:%s,syscfg get value %s"%(details,setValue,syscfGet);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            if setValue != initial_value:
                #Revert to previous value
                tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
                tdkTestObj.addParameter("ParamName",paramName);
                tdkTestObj.addParameter("ParamValue",initial_value);
                tdkTestObj.addParameter("Type","boolean");
                expectedresult="SUCCESS";
                #Execute testcase on DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                result = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Revert the RFC DLCaStoreEnable status to previous"
                    print "EXPECTED RESULT 5: Should revert RFC DLCaStore status to previous"
                    print "ACTUAL RESULT 5: %s" %result;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Revert RFC DLCaStore Enable status to previous"
                    print "EXPECTED RESULT 5: Should revert RFC DLCaStore Enable status to previous"
                    print "ACTUAL RESULT 5: %s" %result;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set  RFC DLCaStore Enable status to %s"%setValue;
            print "EXPECTED RESULT 2: Should set RFC DLCaStore Enable status to %s" %setValue;
            print "ACTUAL RESULT 2: %s" %result;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get current value of RFC DLCaStore Enable"
        print "EXPECTED RESULT 1: Should get current value of RFC DLCaStore Enable"
        print "ACTUAL RESULT 1: current value is %s" %initial_value;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam/sysutil module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
