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
  <version>15</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIAGENT_CheckNonRootSupport</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if CcspWifiSsp process is running with non-root privileges when the RFC parameter  Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is enabled.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>30</execution_time>
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
    <test_case_id>TC_WIFIAGENT_151</test_case_id>
    <test_objective>To check if CcspWifiSsp process is running with non-root privileges when the RFC parameter  Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable</input_parameters>
    <automation_approch>1. Load the modules
2. Get the RFC parameter value Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable and check if the value is true
3. If the RFC is enabled check if the CCSP process CcspWifiSsp is running in the device with non-root privileges. If the RFC is disabled, enable the paramter and reboot the device for RFC to take effect.
4. Revert the RFC parameter is required.
5. Unload the modules.</automation_approch>
    <expected_output>CcspWifiSSp process should be running with non-root privileges when the RFC parameter      Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckNonRootSupport</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
def set_EnableNonRootRFC(pamobj, value, step):
    status = 1;
    expectedresult = "SUCCESS";
    tdkTestObj = pamobj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable");
    tdkTestObj.addParameter("ParamValue",value);
    tdkTestObj.addParameter("Type","bool");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Set Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable to %s" %(step, value);
    print "EXPECTED RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable should be set to %s successfully" %(step, value);

    if expectedresult in actualresult and details != "":
        status = 0;
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is set to %s successfully; Details : %s" %(step, value, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        print "Reboot the device for the RFC to take effect";
        pamobj.initiateReboot();
        sleep(300);
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is not set to %s successfully; Details : %s" %(step, value, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status, tdkTestObj;

def get_EnableNonRootRFC(pamobj, step):
    status = 1;
    expectedresult = "SUCCESS";

    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Get the non-root support parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable" %step;
    print "EXPECTED RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable should be retrieved successfully" %step;

    if expectedresult in actualresult and details != "":
        status = 0;
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is retrieved successfully; Details : %s" %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is not retrieved successfully; Details : %s" %(step, value, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status, details, tdkTestObj;

def check_WiFiProcess(sysobj, step):
    status = 1;
    expectedresult = "SUCCESS";
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    command= "ps  | grep -i \"CcspWifiSsp\" | grep -v \"grep\"";
    tdkTestObj.addParameter("command", command);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Get the CcspWifiSsp proccess details" %step;
    print "EXPECTED RESULT %d:  Should get the CcspWifiSsp proccess details" %step;

    if expectedresult in actualresult and "CcspWifiSsp" in details:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: CcspWifiSsp is running in the device ; Details : %s" %(step, details);
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check if CcspWifiSSp has non-root privilage
        step = step + 1;
        print "\nTEST STEP %d: Check if the user-type is non-root" %step;
        print "EXPECTED RESULT %d: Should get the user type as non-root" %step;

        if "non-root" in details:
            status = 0;
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: The user type is non-root" %(step);
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: The user type is not non-root" %(step);
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: CcspWifiSsp is not running in the device; Details : %s" %(step, details);
        print "[TEST EXECUTION RESULT] : FAILURE";
    return tdkTestObj, status;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;

#Test component to be tested
pamobj = tdklib.TDKScriptingLibrary("pam","RDKB");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
pamobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckNonRootSupport');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckNonRootSupport');

#Get the result of connection with test component and DUT
pamloadmodulestatus=pamobj.getLoadModuleResult();
sysloadmodulestatus=sysobj.getLoadModuleResult();

if "SUCCESS" in sysloadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper():
    #Set the result status of execution
    pamobj.setLoadModuleStatus("SUCCESS")
    sysobj.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    #Get the RFC non-root support parameter
    step = 1;
    status, details, tdkTestObj = get_EnableNonRootRFC(pamobj, step);

    if status == 0 and details == "true":
        print "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is enabled";

        #Get the CcspWifiSsp process details
        step = step + 1;
        tdkTestObj, status = check_WiFiProcess(sysobj, step);

        if status == 0:
            tdkTestObj.setResultStatus("SUCCESS");
            print "The CcspWifiSsp process is running as non-root";
        else:
            tdkTestObj.setResultStatus("SUCCESS");
            print "The CcspWifiSsp process is not running as non-root";

    elif status == 0 and details == "false":
        print "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is disabled";

        #Set non-root support RFC Enable to true
        step = step + 1;
        value = "true";
        status, tdkTestObj = set_EnableNonRootRFC(pamobj, value, step);

        if status == 0:
            #Check if the RFC is set properly
            step = step + 1;
            status, details, tdkTestObj = get_EnableNonRootRFC(pamobj, step)

            if status == 0 and details == "true":
                print "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is Enabled";
                #Get the CcspWifiSsp process details
                step = step + 1;
                tdkTestObj, status = check_WiFiProcess(sysobj, step);

                if status == 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "The CcspWifiSsp process is running as non-root";

                    #Revert back to initial state
                    #Set the Enable parameter to false
                    step = step + 2;
                    value = "false";
                    status = set_EnableNonRootRFC(pamobj, value, step);

                    if status == 0:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Revert operation is successful";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Revert operation is not successful";
                else:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "The CcspWifiSsp process is not running as non-root";
            else:
                print "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is not set successfully";
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is not retrieved successfully";
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.Enable is not retrieved successfully";
        tdkTestObj.setResultStatus("FAILURE");

    pamobj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    pamobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
