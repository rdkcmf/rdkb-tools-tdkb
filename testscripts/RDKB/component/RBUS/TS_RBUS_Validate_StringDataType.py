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
  <name>TS_RBUS_Validate_StringDataType</name>
  <primitive_test_id/>
  <primitive_test_name>RBUS_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Get the value of string data using Device.SampleProvider.AllTypes.StringData and set a new value of string data type and check if the value is getting set properly while the rbusSampleProvider App is running.</synopsis>
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
    <test_case_id>TC_RBUS_83</test_case_id>
    <test_objective>Get the value of string data using Device.SampleProvider.AllTypes.StringData and set a new value of string data type and check if the value is getting set properly while the rbusSampleProvider App is running.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>set_value : setstringdata</input_parameters>
    <automation_approch>1. Load the modules
2. Check if the Device is in RBUS mode, if it not in RBUS mode enable Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable and reboot the device.
3. Once the device comes up, run the rbusSampleProvider App to obtain the sample provider namespace
4. When the App is running, fetch the value of Device.SampleProvider.AllTypes.StringData and store it.
5. Set the set_value of string type and check if the set operation is success.
6. Fetch the value of Device.SampleProvider.AllTypes.StringData and confirm whether the set operation is success.
7. Wait 60s for the rbusSampleProvider App to complete
8. Revert to the initial RBUS enable state if revert flag is set.</automation_approch>
    <expected_output>Set operation of Device.SampleProvider.AllTypes.StringData should be success and the get operation should reflect the set value when rbusSampleProvider App is running.</expected_output>
    <priority>High</priority>
    <test_stub_interface>rbus</test_stub_interface>
    <test_script>TS_RBUS_Validate_StringDataType</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbRBUS_Utility import *;
from tdkutility import *;
from time import sleep;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_RBUS_Validate_StringDataType');
tr181obj.configureTestCase(ip,port,'TS_RBUS_Validate_StringDataType');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=tr181obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() :
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    revert_flag = 0;
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    tdkTestObj_Tr181_Get = tr181obj.createTestStep('TDKB_TR181Stub_Get');
    tdkTestObj_Tr181_Set = tr181obj.createTestStep('TDKB_TR181Stub_SetOnly');
    print "\nTEST STEP 1: Execute the Pre Requisite for RBUS"
    print "EXPECTED RESULT 1: Pre Requisite of RBUS should be success"

    #Execute the PreRequisite of RBUS
    rbus_set,revert_flag = rbus_PreRequisite(sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,tdkTestObj);

    if rbus_set == 1:
        print "ACTUAL RESULT 1: PreRequisite of RBUS was Success"
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");

        print "\n******************************************************************"
        #Run the rbusSampleProvider App
        actualresult,details = doSysutilExecuteCommand(tdkTestObj,"/usr/bin/rbusSampleProvider > /tmp/rbusSampleProvider1.log &");
        print "\nTEST STEP 2: Execute the Sample Provider Test App";
        print "EXPECTED RESULT 2: Sample Provider Test App should be running";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: Sample Provider Test App Running successfully"
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Get the data type of String data
            cmd = "rbuscli get Device.SampleProvider.AllTypes.StringData | grep -i value";
            print "Command : %s" %cmd;
            tdkTestObj.addParameter("command",cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip();
            print "\nTEST STEP 3: Get the String Data type value of Device.SampleProvider.AllTypes.StringData";
            print "EXPECTED RESULT 3: Should get the String data type value of Device.SampleProvider.AllTypes.StringData";

            if expectedresult in actualresult and "Value" in details:
                initial_value = details.split("Value : ")[1].replace("\\n", "");
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: Value : %s" %initial_value;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Set value to Device.SampleProvider.AllTypes.StringData
                set_value = "setstringdata";
                cmd = "rbuscli set Device.SampleProvider.AllTypes.StringData string " + set_value + " | grep -i succeeded";
                print "Command : %s" %cmd;
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip();
                print "\nTEST STEP 4: Set the String Data type value of Device.SampleProvider.AllTypes.StringData to %s" %set_value;
                print "EXPECTED RESULT 4: Should set the String data type value of Device.SampleProvider.AllTypes.StringData successfully";

                if expectedresult in actualresult and "succeeded" in details:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: Set operation is success";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Get the value and check if the set operation was proper
                    cmd = "rbuscli get Device.SampleProvider.AllTypes.StringData | grep -i value";
                    print "Command : %s" %cmd;
                    tdkTestObj.addParameter("command",cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip();
                    print "\nTEST STEP 5: Get the String Data type value of Device.SampleProvider.AllTypes.StringData";
                    print "EXPECTED RESULT 5: Should get the String data type value of Device.SampleProvider.AllTypes.StringData";

                    if expectedresult in actualresult and "Value" in details:
                        get_value = details.split("Value : ")[1].replace("\\n", "");
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 5: Value : %s" %get_value;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Cross check if both the set and get values are equal
                        print "\nTEST STEP 6: Compare the set and get values";
                        print "EXPECTED RESULT 6: The set and get values should be equal";
                        print "Set Value : %s" %set_value;
                        print "Get Value : %s" %get_value;

                        if set_value == get_value:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 6: The set and get values are equal";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                            print "\nWaiting 60 seconds for rbusSampleProvider App to complete....."
                            sleep(60);
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 6: The set and get values are equal";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 5: Details : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: Set operation failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: Sample Provider Test App not Running successfully"
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: PreRequisite of RBUS was FAILED"
        print "[TEST EXECUTION RESULT] : FAILURE";

    print "\n******************************************************************";
    print "\nTEST STEP 7: Execute the Post process of RBUS"
    print "EXPECTED RESULT 7: Post process of RBUS should be success"
    post_process_value = rbus_PostProcess(sysobj,tdkTestObj_Tr181_Get,tdkTestObj_Tr181_Set,tdkTestObj,revert_flag);

    if post_process_value == 1:
        tdkTestObj_Tr181_Get.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 7: Post process of RBUS was Success"
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj_Tr181_Get.setResultStatus("FAILURE");
        print "ACTUAL RESULT 7: Post process of RBUS was FAILED"
        print "[TEST EXECUTION RESULT] : FAILURE";

    tr181obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    tr181obj.setLoadModuleStatus("FAILURE");

