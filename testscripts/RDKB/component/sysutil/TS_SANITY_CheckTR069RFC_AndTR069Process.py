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
  <name>TS_SANITY_CheckTR069RFC_AndTR069Process</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the TR181 parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable and EnableTR69Binary from syscfg.db are equal. If the RFC is enabled, toggle to false and check if the process is not running and vice-versa.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_SYSUTIL_43</test_case_id>
    <test_objective>Check if the TR181 parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable and EnableTR69Binary from syscfg.db are equal. If the RFC is enabled, toggle to false and check if the process is not running and vice-versa.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>pam_SetParams
ExecuteCmd</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable
ParamValue : true/false
Type : bool
</input_parameters>
    <automation_approch>1. Load the modules
2. Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable and check if the value is the same as EnableTR69Binary from syscfg.db.
3. If the RFC parameter is enabled check if the TR069 Process is running. If not enabled the Process should not be running in the device.
4. Toggle the value of the TR-181 parameter and check if the value is set properly in syscfg.db file.
5. If disabled the TR069 should stop running or if enabled TR069 should start running.
6. Revert back to the initial state
7. Unload the module.</automation_approch>
    <expected_output>The values retrieved from the TR181 parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable and the TR069Enable from should be matching and the TR069 CCSP process should run when the RFC is enabled and not run when the RFC is disabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckTR069RFC_AndTR069Process</test_script>
    <skipped>No</skipped>
    <release_version>M91</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def syscfg_get_EnableTR069(sysobj, step):
    status = 1;
    syscfg_enable = "";
    expectedresult = "SUCCESS";
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    command= "syscfg get EnableTR69Binary";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "\nTEST STEP %d : Get the value of EnableTR69Binary from syscfg.db" %step;
    print "EXPECTED RESULT %d : Should get the value of EnableTR69Binary from syscfg.db" %step;

    if expectedresult in actualresult and details != "":
        status = 0;
        syscfg_enable = details.strip().replace("\\n", "");
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : EnableTR69Binary from syscfg.db is : %s" %(step, syscfg_enable);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : EnableTR69Binary from syscfg.db is : %s" %(step, syscfg_enable);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status, syscfg_enable;


def set_EnableTR069(pamobj, value, step):
    status = 1;
    expectedresult = "SUCCESS";
    tdkTestObj = pamobj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable");
    tdkTestObj.addParameter("ParamValue",value);
    tdkTestObj.addParameter("Type","bool");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "\nTEST STEP %d: Set Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable to %s" %(step, value);
    print "EXPECTED RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable should be set to %s successfully" %(step, value);

    if expectedresult in actualresult and details != "":
        status = 0;
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is set to %s successfully; Details : %s" %(step, value, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is not set to %s successfully; Details : %s" %(step, value, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status;


def check_TR069Process(sysobj):
    expectedresult = "SUCCESS";
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    command= "pidof CcspTr069PaSsp";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return tdkTestObj, actualresult, details;


def compare_values(value1, value2, step):
    status = 1;
    print "\nTEST STEP %d : Check the TR069 Enable values queried via TR181 and syscfg get are same" %step;
    print "EXPECTED RESULT %d : TR069 Enable values queried via TR181 and syscfg get should be the same" %step;
    print "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable : %s" %value1;
    print "syscfg get EnableTR69Binary : %s" %value2;

    if value1 == value2:
        status = 0;
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : TR069 Enable values queried via TR181 and syscfg are the same" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : TR069 Enable values queried via TR181 and syscfg are not the same" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status;



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
pamobj.configureTestCase(ip,port,'TS_SANITY_CheckTR069RFC_AndTR069Process');
sysobj.configureTestCase(ip,port,'TS_SANITY_CheckTR069RFC_AndTR069Process');

#Get the result of connection with test component and DUT
pamloadmodulestatus=pamobj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();

if "SUCCESS" in sysloadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    #Get TR069 RFC Parameter
    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "\nTEST STEP 1 : Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable";
    print "EXPECTED RESULT 1 : Should get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable";

    if expectedresult in actualresult and details != "":
        enable = details.strip().replace("\\n", "");
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1 : Enable Status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is : %s" %enable;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Get the syscfg.db value of the TR069 RFC
        step = 2;
        status, syscfg_enable = syscfg_get_EnableTR069(sysobj, step);

        if status == 0:
            #Check if both the values are equal
            step = step + 1;
            status = compare_values(enable, syscfg_enable, step);

            if status == 0:
                #If TR069 RFC is enabled, then check if TR069 process is running or not
                step = step + 1;

                if enable == "true" and syscfg_enable == "true":
                    print "\nTEST STEP %d: Check if CcspTr069PaSsp is running in the device" %step;
                    print "EXPECTED RESULT %d : CcspTr069PaSsp should be running in the device" %step;
                    tdkTestObj, actualresult, details = check_TR069Process(sysobj);

                    if expectedresult in actualresult and details != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : CcspTr069PaSsp is running with PID : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Set the Enable parameter to false
                        step = step + 1;
                        value = "false";
                        status = set_EnableTR069(pamobj, value, step);

                        if status == 0:
                            sleep(15);
                            #Get the syscfg.db value of the TR069 RFC
                            step = step + 1;
                            status, syscfg_enable_set = syscfg_get_EnableTR069(sysobj, step);

                            if status == 0:
                                #Check if both the values are equal
                                step = step + 1;
                                status = compare_values(value, syscfg_enable_set, step);

                                if status == 0:
                                    #check if TR069 process is running or not
                                    tdkTestObj, actualresult, details = check_TR069Process(sysobj);
                                    step = step + 1;
                                    print "\nTEST STEP %d: Check if CcspTr069PaSsp is running in the device" %step;
                                    print "EXPECTED RESULT %d : CcspTr069PaSsp should not be running in the device" %step;

                                    if expectedresult in actualresult and details == "":
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT %d : CcspTr069PaSsp is not running in the device : %s" %(step, details);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS";

                                        #Revert back to initial state
                                        #Set the Enable parameter to true
                                        step = step + 1;
                                        value = "true";
                                        status = set_EnableTR069(pamobj, value, step);

                                        if status == 0:
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "Revert operation is successful";
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "Revert operation is not successful";
                                    else:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT %d : CcspTr069PaSsp is running with PID : %s" %(step, details);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE";
                                else:
                                    print "The values are not equal";
                                    tdkTestObj.setResultStatus("FAILURE");
                            else:
                                print "TR069 Enable value not retrieved from syscfg.db";
                                tdkTestObj.setResultStatus("FAILURE");
                        else:
                            print "Set operation failed";
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : CcspTr069PaSsp is not running in the device : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the Enable parameter to true
                    value = "true";
                    status = set_EnableTR069(pamobj, value, step);

                    if status == 0:
                        sleep(15);
                        #Get the syscfg.db value of the TR069 RFC
                        step = step + 1;
                        status, syscfg_enable_set = syscfg_get_EnableTR069(sysobj, step);

                        if status == 0:
                            #Check if both the values are equal
                            step = step + 1;
                            status = compare_values(value, syscfg_enable_set, step)

                            if status == 0:
                                #check if TR069 process is running or not
                                tdkTestObj, actualresult, details = check_TR069Process(sysobj);
                                print "\nTEST STEP %d: Check if CcspTr069PaSsp is running in the device" %step;
                                print "EXPECTED RESULT %d : CcspTr069PaSsp should be running in the device" %step;

                                if expectedresult in actualresult and details != "":
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d : CcspTr069PaSsp is running with PID : %s" %(step, details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

                                    #Revert back to initial state
                                    #Set the Enable parameter to false
                                    step = step + 1;
                                    value = "false";
                                    status = set_EnableTR069(pamobj, value, step);

                                    if status == 0:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "Revert operation is successful";
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "Revert operation is not successful";
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d : CcspTr069PaSsp is not running in the device : %s" %(step, details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                print "The values are not equal";
                                tdkTestObj.setResultStatus("FAILURE");
                        else:
                            print "TR069 Enable value not retrieved from syscfg.db";
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "Set operation failed";
                        tdkTestObj.setResultStatus("FAILURE");
            else:
                print "The values are not equal";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "TR069 Enable value not retrieved from syscfg.db";
            tdkTestObj.setResultStatus("FAILURE");
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1 : Enable Status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is not retrieved";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");


