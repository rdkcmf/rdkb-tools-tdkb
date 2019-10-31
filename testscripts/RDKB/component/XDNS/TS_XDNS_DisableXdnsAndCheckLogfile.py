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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>4</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_XDNS_DisableXdnsAndCheckLogfile</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>XDNS_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To disable XDNS and check if DNS logs are present in log file</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_XDNS_14</test_case_id>
    <test_objective>To disable XDNS and check if DNS logs are present in log file</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS</input_parameters>
    <automation_approch>1. Load  module
2. Get the current enable status of XDNS and parental control features
3. Disable XDNS and parental control features
4. Check if xdns logs are present in logfile
5. Revert the XDNS enable status and parental control features
6. Unload module</automation_approch>
    <expected_output>XDNS warning messages should not be present in logfile after disabling XDNS</expected_output>
    <priority>High</priority>
    <test_stub_interface>tdkbtr181</test_stub_interface>
    <test_script>TS_XDNS_DisableXdnsAndCheckLogfile</test_script>
    <skipped>No</skipped>
    <release_version>M70</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import tdkutility
from tdkutility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_XDNS_DisableXdnsAndCheckLogfile');
obj1.configureTestCase(ip,port,'TS_XDNS_DisableXdnsAndCheckLogfile');
sysobj.configureTestCase(ip,port,'TS_XDNS_DisableXdnsAndCheckLogfile');


#Get the result of connection with test component and DUT
loadmodulestatus1=obj.getLoadModuleResult();
loadmodulestatus2=obj1.getLoadModuleResult();
loadmodulestatus3=sysobj.getLoadModuleResult();



if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() and "SUCCESS" in loadmodulestatus3.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    tdkTestObj = obj.createTestStep('TADstub_Get');

    expectedresult = "SUCCESS"
    paramList=["Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS", "Device.X_Comcast_com_ParentalControl.ManagedSites.Enable", "Device.X_Comcast_com_ParentalControl.ManagedServices.Enable", "Device.X_Comcast_com_ParentalControl.ManagedDevices.Enable"]
    print "TEST STEP 1: Should get the Enable status of XDNS,Parental Control ManagedSites, Parental Control ManagedServices,Parental Control ManagedDevices"
    tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)

    if expectedresult in status and orgValue[0] != "" and orgValue[1] != "" and orgValue[2] != "" and orgValue[3] != "":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1:Enable status of XDNS :%s,Parental Control ManagedSites : %s, Parental Control ManagedServices : %s ,Parental Control ManagedDevices: %s " %(orgValue[0],orgValue[1],orgValue[2],orgValue[3]);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Disable XDNS and parental control features
        tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
        tdkTestObj.addParameter("paramList","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS|false|bool|Device.X_Comcast_com_ParentalControl.ManagedSites.Enable|false|bool|Device.X_Comcast_com_ParentalControl.ManagedServices.Enable|false|bool|Device.X_Comcast_com_ParentalControl.ManagedDevices.Enable|false|bool");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Should disable XDNS and parental control features"
            print "ACTUAL RESULT 2: %s" %details;
            print "TEST EXECUTION RESULT :SUCCESS";
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            cmd = "[ -f /var/log/messages ] && echo \"File exist\" || echo \"File does not exist\"";
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if details == "File exist":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:Check if messages file is present";
                print "ACTUAL RESULT 3: messages file is present";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                cmd = "cat /var/log/messages  | grep -i \"override dns server not found\""
                tdkTestObj.addParameter("command", cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                xdns_details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult and xdns_details == "":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print "TEST STEP 4:Check XDNS related log messages are present in messages";
                    print "ACTUAL RESULT 4: XDNS related log messages are not present in messages";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print "TEST STEP 4:Check XDNS related log messages are present in messages";
                    print "ACTUAL RESULT 4: XDNS related log messages are  present in messages";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3:Check if messages file is present";
                print "ACTUAL RESULT 3: messages file is not present";
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                cmd = "journalctl | grep -i \"override dns server not found\"";
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                if expectedresult in actualresult and details == "":
                    tdkTestObj.setResultStatus("SUCCESS")
                    print "TEST STEP 4:Check XDNS related log messages are present in journalctl logs";
                    print "ACTUAL RESULT 4: XDNS related log messages are not present in journalctl logs";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print "TEST STEP 4:Check XDNS related log messages are present in journalctl logs";
                    print "ACTUAL RESULT 4: XDNS related log messages are present in journalctl logs";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

            tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
            tdkTestObj.addParameter("paramList","Device.DeviceInfo.X_RDKCENTRAL-COM_EnableXDNS|%s|bool|Device.X_Comcast_com_ParentalControl.ManagedSites.Enable|%s|bool|Device.X_Comcast_com_ParentalControl.ManagedServices.Enable|%s|bool|Device.X_Comcast_com_ParentalControl.ManagedDevices.Enable|%s|bool" %(orgValue[0],orgValue[1],orgValue[2],orgValue[3]))
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP : Should revert XDNS and parental control features"
                print "ACTUAL RESULT : %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP : Should revert XDNS and parental control features"
                print "ACTUAL RESULT : %s" %details;
                print "TEST EXECUTION RESULT :FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Should disable XDNS and parental control features"
            print "ACTUAL RESULT 2: %s" %details;
            print "TEST EXECUTION RESULT :FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Should get the Enable status of XDNS,Parental Control ManagedSites, Parental Control ManagedServices,Parental Control ManagedDevices"
        print "ACTUAL RESULT 1:Failed to get Enable status of XDNS,Parental Control ManagedSites , Parental Control ManagedServices ,Parental Control ManagedDevices ";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tad");
    obj1.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";




