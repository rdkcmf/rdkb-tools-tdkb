##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <version>17</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_MOCA_SetCurrOperFreq_OnScanMode</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>Mocastub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check whether the current operating frequency is changing or not when channel selection mode is true. ie, scan mode. The current operating frequency is expected to be changed only when channel selection is false. ie, manual mode</synopsis>
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
    <test_case_id>TC_MOCA_12</test_case_id>
    <test_objective>To check whether the current operating frequency is changing or not when channel selection mode is true. ie, scan mode. The current operating frequency is expected to be changed only when channel selection is false. ie, manual mode</test_objective>
    <test_type>Negative</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>Mocastub_Set, Mocastub_Get</api_or_interface_used>
    <input_parameters>Device.MoCA.Interface.1.X_CISCO_COM_ChannelScanning
Device.MoCA.Interface.1.CurrentOperFreq
Device.MoCA.Interface.1.FreqCurrentMaskSetting</input_parameters>
    <automation_approch>1. Load MOCA modules
2. Get the initial Scan Mode value and store it
3. If the initial Scan Mode is not true , then set the value to true
4. Get the Current Operating Frequency and Current Frequency Mask values
5. Change the Frequency Mask to new value and set operation should be success
6. Check the Operating Frequency value, the value should be unchanged, since Scan Mode was true (Auto Mode)
7. Revert the Frequency Mask value to its initial value
8. Revert the Scan Mode value if it was changed in step 3
9. Unload MOCA modules
</automation_approch>
    <expected_output>The operating frequency should not change if channel selection mode is set to true</expected_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_MOCA_SetCurrOperFreq_OnScanMode</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("moca","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MOCA_SetCurrOperFreq_OnScanMode');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

def Mocastub_Get_Function(tdkTestObj,parameter_name):
    tdkTestObj.addParameter("paramName",parameter_name);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult,details;

def Mocastub_Set_Function(tdkTestObj,parameter_name,parameter_value,parameter_type):
    tdkTestObj.addParameter("ParamName",parameter_name);
    tdkTestObj.addParameter("ParamValue",parameter_value);
    tdkTestObj.addParameter("Type",parameter_type);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details= tdkTestObj.getResultDetails();
    return actualresult,details;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    scanMode_true = 0;
    revert_flag = 0;
    tdkTestObj_get = obj.createTestStep('Mocastub_Get');
    tdkTestObj_set = obj.createTestStep('Mocastub_Set');
    tdkTestObj_setonly = obj.createTestStep('Mocastub_SetOnly');

    print "\n********** Get the Initial value of Channel ScanMode ********** "
    actualresult_get,cur_scan_mode = Mocastub_Get_Function(tdkTestObj_get,"Device.MoCA.Interface.1.X_CISCO_COM_ChannelScanning");
    if expectedresult in actualresult_get:
        #Set the result status of execution
        tdkTestObj_get.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the initial channel ScanMode value";
        print "EXPECTED RESULT 1: Should Get initial channel ScanMode value";
        print "ACTUAL RESULT 1: channel ScanMode value Get operation was successful"
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if cur_scan_mode == "true":
            print "Channel ScanMode value is true (Auto mode), No need to Set the value again"
            scanMode_true = 1;
        else:
            print "\n********** Set the Channel ScanMode to True ********** "
            actualresult_set,scan_mode = Mocastub_Set_Function(tdkTestObj_set,"Device.MoCA.Interface.1.X_CISCO_COM_ChannelScanning","true","bool");
            if actualresult_set in expectedresult:
                scanMode_true = 1;
                revert_flag = 1;
                #Set the result status of execution
                tdkTestObj_set.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set the channel ScanMode value to true";
                print "EXPECTED RESULT 2: Should set channel ScanMode value to true";
                print "ACTUAL RESULT 2: channel ScanMode value Set operation was successful"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                scanMode_true = 0;
                #Set the result status of execution
                tdkTestObj_set.setResultStatus("FAILURE");
                print "TEST STEP 2: Set the channel ScanMode value to true";
                print "EXPECTED RESULT 2: Should set channel ScanMode value to true";
                print "ACTUAL RESULT 2: channel ScanMode value Set operation was Failed"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        sleep(30);

        if scanMode_true == 1:
            print "\n********** Get the Initial value of Current Operating Frequency and Current Frequency Mask **********"
            actualresult_freq,cur_freq = Mocastub_Get_Function(tdkTestObj_get,"Device.MoCA.Interface.1.CurrentOperFreq");
            actualresult_fremask,cur_freq_mask = Mocastub_Get_Function(tdkTestObj_get,"Device.MoCA.Interface.1.FreqCurrentMaskSetting");

            if expectedresult in (actualresult_freq and actualresult_fremask):
                #Set the result status of execution
                tdkTestObj_get.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the initial value of Current Operating Frequency and Current Frequency Mask";
                print "EXPECTED RESULT 3: Should get the initial value of Current Operating Frequency and Current Frequency Mask";
                print "ACTUAL RESULT 3: Current Operating Frequency and Current Frequency Mask Get operation was successful"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                print "\nInitial value of ScanMode is: ",cur_scan_mode
                print "Initial value of CurrentOperFreq is: ",cur_freq
                print "Initial value of FreqCurrentMaskSetting is:",cur_freq_mask

                print "\n********** Set the FreqCurrentMaskSetting to a different value **********"
                if "0000000000008000" in cur_freq_mask:
                    Freq_Mask1 = "0000000000020000";
                else:
                    Freq_Mask1 = "0000000000008000";
                print "FreqCurrentMaskSetting value to be set is ",	Freq_Mask1

                actualresult_freq_set,scan_mode = Mocastub_Set_Function(tdkTestObj_setonly,"Device.MoCA.Interface.1.FreqCurrentMaskSetting",Freq_Mask1,"string");
                if actualresult_freq_set in expectedresult:
                    #Set the result status of execution
                    tdkTestObj_setonly.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Set the current frequency mask value";
                    print "EXPECTED RESULT 4: Should set current frequency mask";
                    print "ACTUAL RESULT 4: Frequency Mask set operation was successful"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    sleep(30);

                    print "\n********** Check whether the CurrentOperFreq is changed or not **********"
                    actualresult_freq,new_freq= Mocastub_Get_Function(tdkTestObj_get,"Device.MoCA.Interface.1.CurrentOperFreq");
                    print "New Freq value is ",new_freq

                    if expectedresult in actualresult_freq and int(new_freq) == int(cur_freq):
                        #Set the result status of execution
                        tdkTestObj_get.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Get the current operating frequency and check with previous frequency";
                        print "EXPECTED RESULT 5: Current operating frequency should NOT change";
                        print "ACTUAL RESULT 5: The current operating frequency and new operating frequency are :%s and %s" %(cur_freq,new_freq);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj_get.setResultStatus("FAILURE");
                        print "TEST STEP 5: Get the current operating frequency and check with previous frequency";
                        print "EXPECTED RESULT 5: Current operating frequency should NOT change";
                        print "ACTUAL RESULT 5: The current operating frequency and new operating frequency were NOT same "
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";


                    print "\n********** Revert the Frequency Mask value to its original value ********** "
                    actualresult_freq_set,scan_mode = Mocastub_Set_Function(tdkTestObj_set,"Device.MoCA.Interface.1.FreqCurrentMaskSetting",cur_freq_mask,"string");
                    if actualresult_freq_set in expectedresult:
                        #Set the result status of execution
                        tdkTestObj_set.setResultStatus("SUCCESS");
                        print "TEST STEP 6: Set the initial frequency mask";
                        print "EXPECTED RESULT 6: Should set initial frequency mask";
                        print "ACTUAL RESULT 6: Frequency Mask set operation was successful"
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj_set.setResultStatus("FAILURE");
                        print "TEST STEP 6: Set the initial frequency mask";
                        print "EXPECTED RESULT 6: Should set initial frequency mask";
                        print "ACTUAL RESULT 6: Frequency Mask set operation was Failed"
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj_setonly.setResultStatus("FAILURE");
                    print "TEST STEP 4: Set the current frequency mask value";
                    print "EXPECTED RESULT 4: Should set current frequency mask";
                    print "ACTUAL RESULT 4: Frequency Mask set operation was failed"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj_get.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the initial value of Current Operating Frequency and Current Frequency Mask";
                print "EXPECTED RESULT 3: Should get the initial value of Current Operating Frequency and Current Frequency Mask";
                print "ACTUAL RESULT 3: Current Operating Frequency and Current Frequency Mask Get operation was Failed"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";


            print "\n********** Revert the channel selection mode to initial value **********"
            if revert_flag == 1:
                actualresult,scan_mode = Mocastub_Set_Function(tdkTestObj_set,"Device.MoCA.Interface.1.X_CISCO_COM_ChannelScanning","true","bool");
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj_set.setResultStatus("SUCCESS");
                    print "TEST STEP 7: Set the channel selection mode";
                    print "EXPECTED RESULT 7: Should set channel selection mode as default";
                    print "ACTUAL RESULT 7: channel selection mode set operation was successful";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj_set.setResultStatus("FAILURE");
                    print "TEST STEP 7: Set the channel selection mode";
                    print "EXPECTED RESULT 7: Should set channel selection mode as default";
                    print "ACTUAL RESULT 7: channel selection mode set operation was failed";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                print "ChannelScanning value not changed, no need for revert operation"
        else:
            #Set the result status of execution
            tdkTestObj_set.setResultStatus("FAILURE");
            print "Not able to set Channel ScanMode to true"
    else:
        #Set the result status of execution
        tdkTestObj_get.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the initial channel ScanMode value";
        print "EXPECTED RESULT 1: Should Get initial channel ScanMode value";
        print "ACTUAL RESULT 1: channel ScanMode value Get operation was Failed"
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("moca");
else:
    print "Failed to load moca module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
