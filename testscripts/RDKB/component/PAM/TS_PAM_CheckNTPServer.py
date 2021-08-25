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
  <version>12</version>
  <name>TS_PAM_CheckNTPServer</name>
  <primitive_test_id/>
  <primitive_test_name>pam_Setparams</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To retrieve the NTP Servers after enabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable and cross checking with the expected values.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_PAM_212</test_case_id>
    <test_objective>To retrieve the NTP Servers after enabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable and cross checking with the expected values.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable
ParamName : Device.Time.NTPServer1
ParamName : Device.Time.NTPServer2
ParamName : Device.Time.NTPServer3
ParamName : Device.Time.NTPServer4
ParamName : Device.Time.NTPServer5
</input_parameters>
    <automation_approch>1. Load the pam and sysutil modules
2. Check if the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable is true. If it is false, set it to true.
3. Get the expected values of NTPServer1, NTPServer2, NTPServer3, NTPServer4, NTPServer5 from platform properties file.
4. Get the TR181 values of Device.Time.NTPServer1, Device.Time.NTPServer2, Device.Time.NTPServer3, Device.Time.NTPServer4, Device.Time.NTPServer5
5. Compare the TR181 values with the expected values. They should match.
6. Revert to initial state
7. Unload the modules</automation_approch>
    <expected_output>The NTP Servers values retrieved should be same as the expected values after enabling Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_CheckNTPServer</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def get_NTPEnable(tdkTestObj, step):
    expectedresult = "SUCCESS";
    status = 1;
    enable = "";
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "\nTEST STEP %d : Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable" %step;
    print "EXPECTED RESULT %d : Should get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable" %step;

    if expectedresult in actualresult and details != "":
        status = 0;
        enable = details.strip().replace("\\n", "");
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : Enable Status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable is : %s" %(step,enable);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : Enable Status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable is not retrieved" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return enable, status;

def set_NTPEnable(pamobj, value, step):
    status = 1;
    expectedresult = "SUCCESS";
    tdkTestObj = pamobj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable");
    tdkTestObj.addParameter("ParamValue",value);
    tdkTestObj.addParameter("Type","bool");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "\nTEST STEP %d: Set Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable to %s" %(step, value);
    print "EXPECTED RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable should be set to %s successfully" %(step, value);

    if expectedresult in actualresult and details != "":
        status = 0;
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable is set to %s successfully; Details : %s" %(step, value, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable is not set to %s successfully; Details : %s" %(step, value, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status;

def get_NTPServer(sysobj, step, index):
    #Getting NTPServer value from tdk_platform_properties"
    cmd= "sh %s/tdk_utility.sh parseConfigFile NTPServer" %TDK_PATH + str(index);
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    if expectedresult in actualresult :
        print "\nTEST STEP %d: Get NTPServer from property file for index : %d" %(step, index);
        print "EXPECTED RESULT %d: Should  get NTPServer from property file" %step;
        print "ACTUAL RESULT %d: NTPServer from property file : %s" %(step, details);
        print "TEST EXECUTION RESULT :SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");
    else :
        print "\nTEST STEP %d: Get NTPServer from property file for index : %d" %(step, index);
        print "EXPECTED RESULT %d: Should  get NTPServer from property file" %step;
        print "ACTUAL RESULT %d: NTPServer from property file : %s" %(step, details);
        print "TEST EXECUTION RESULT : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");
    return details;

def cross_check(ntp_server, ntp_server_TR181, step):
    status = 1;
    print "\nTEST STEP %d : Cross verify the NTPServer value" %step;
    print "EXPECTED RESULT %d : The NTPServer values should be the same" %step;
    print "TR181 Value : %s" %ntp_server_TR181;
    print "Value from Platform Property file : %s" %ntp_server;

    if ntp_server == ntp_server_TR181 :
        status = 0;
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : NTPServer values are the same" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : NTPServer values are not the same" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status;

def get_NTPServerTR181(pamobj, step, index):
    value = "";
    expectedresult = "SUCCESS";
    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
    param = "Device.Time.NTPServer" + str(index);
    tdkTestObj.addParameter("ParamName",param);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "\nTEST STEP %d : Get the value of %s" %(step, param);
    print "EXPECTED RESULT %d : Should get the value of %s" %(step, param);

    if expectedresult in actualresult :
        value = details.strip().replace("\\n", "");
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : Value of %s is : %s" %(step, param, value);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : Value of %s is not retrieved" %(step, param);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return value;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
import tdkutility;
from time import sleep;

#Test component to be tested
pamobj = tdklib.TDKScriptingLibrary("pam","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_PAM_CheckNTPServer');
sysobj.configureTestCase(ip,port,'TS_PAM_CheckNTPServer');

#Get the result of connection with test component and DUT
pamloadmodulestatus=pamobj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();

if "SUCCESS" in sysloadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    print "\nGet the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.newNTP.Enable";
    step = 1;
    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
    init_enable, status = get_NTPEnable(tdkTestObj, step);
    enable = init_enable;

    print "\nIf NTP Enable initially is false, set it to true";
    if enable == "false" and status == 0:
        step = step + 1;
        value = "true";
        status = set_NTPEnable(pamobj, value, step);

        if status == 0:
            step = step + 1;
            enable, status = get_NTPEnable(tdkTestObj, step);
        else:
            print "Set operation failed";
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "Get operation failed";
        tdkTestObj.setResultStatus("FAILURE");

    if enable == "true" and status == 0:
        for index in range(1,6):
            ntp_server = get_NTPServer(sysobj, step, index);
            step = step + 1;
            ntp_server_TR181 = get_NTPServerTR181(pamobj, step, index);
            step = step + 1;
            status = cross_check(ntp_server, ntp_server_TR181, step);
            step = step + 1;

            if status == 0:
                print "Values are equal";
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "Values are not equal";
                tdkTestObj.setResultStatus("FAILURE");

        if init_enable != enable:
            #Revert NTP Server enable to initial value
            print "\nReverting to initial state";
            value = "false";
            status = set_NTPEnable(pamobj, value, step);

            if status == 0:
                print "Revert operation successful";
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "Revert operation not successful";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "Revert operation is not required";
    else:
        print "Get operation failed";
        tdkTestObj.setResultStatus("FAILURE");

    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");

