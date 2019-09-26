##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <name>TS_MOCA_GetLastOperFreq</name>
  <primitive_test_id/>
  <primitive_test_name>Mocastub_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Change the current operating frequency by setting current frequency mask. Then check whether the last operating frequency is changed to previous current operating frequency.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_MOCA_13</test_case_id>
    <test_objective>Change the current operating frequency by setting current frequency mask. Then check whether the last operating frequency is changed to previous current operating frequency.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>Mocastub_Set, Mocastub_Get</api_or_interface_used>
    <input_parameters>Device.MoCA.Interface.1.X_CISCO_COM_ChannelScanning
Device.MoCA.Interface.1.CurrentOperFreq
Device.MoCA.Interface.1.FreqCurrentMaskSetting
Device.MoCA.Interface.1.LastOperFreq</input_parameters>
    <automation_approch>1. Load MOCA modules
2. From script invoke Mocastub_Set to set the frequency mask
3. Get the current operating frequency and check whether the last operating frequency is same as the previous current operating frequency
4. Validation of  the result is done within the python script and send the result status to Test Manager.
5.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from Moca stub.</automation_approch>
    <except_output>CheckPoint 1:
 The output  should be logged in the Agent console/Component log

CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>None</test_stub_interface>
    <test_script>TS_MOCA_GetLastOperFreq</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("moca","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MOCA_GetLastOperFreq');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('Mocastub_Get');
    tdkTestObj.addParameter("paramName","Device.MoCA.Interface.1.X_CISCO_COM_ChannelScanning");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    ScanMode= tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the channel selection mode";
        print "EXPECTED RESULT 1: Should get the channel selection mode";
        print "ACTUAL RESULT 1: The channel selection mode is :%s" %ScanMode;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj = obj.createTestStep('Mocastub_Get');
        tdkTestObj.addParameter("paramName","Device.MoCA.Interface.1.CurrentOperFreq");
        expectedresult="SUCCESS";

        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        Curr_Freq= tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the current operating frequency";
            print "EXPECTED RESULT 2: Should get the current operating frequency";
            print "ACTUAL RESULT 2: The current operating frequency is :%s" %Curr_Freq;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj = obj.createTestStep('Mocastub_Get');
            tdkTestObj.addParameter("paramName","Device.MoCA.Interface.1.FreqCurrentMaskSetting");
            expectedresult="SUCCESS";

            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            Freq_Mask= tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the current frequency mask";
                print "EXPECTED RESULT 3: Should get the current frequency mask";
                print "ACTUAL RESULT 3: The current operating frequency is :%s" %Freq_Mask;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj = obj.createTestStep('Mocastub_Set');
                tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.X_CISCO_COM_ChannelScanning");
                tdkTestObj.addParameter("ParamValue","false");
                tdkTestObj.addParameter("Type","bool");
                expectedresult="SUCCESS";

                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details= tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Set the channel selection mode";
                    print "EXPECTED RESULT 4: Should set channel selection mode as false";
                    print "ACTUAL RESULT 4: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    tdkTestObj = obj.createTestStep('Mocastub_Set');
                    tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.FreqCurrentMaskSetting");
                    if "0000000000010000" in Freq_Mask:
                        Freq_Mask1 = "0000000000004000";
                    else:
                        Freq_Mask1 = "0000000000010000";
                    tdkTestObj.addParameter("ParamValue",Freq_Mask1);
                    tdkTestObj.addParameter("Type","string");
                    expectedresult="SUCCESS";

                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details= tdkTestObj.getResultDetails();
                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Set the current frequency mask";
                        print "EXPECTED RESULT 5: Should set current frequency mask";
                        print "ACTUAL RESULT 5: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        tdkTestObj = obj.createTestStep('Mocastub_Get');
                        tdkTestObj.addParameter("paramName","Device.MoCA.Interface.1.LastOperFreq");
                        expectedresult="SUCCESS";

                        #Execute the test case in DUT
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        Last_Freq= tdkTestObj.getResultDetails();

                        if expectedresult in actualresult and Curr_Freq in Last_Freq:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Get the last operating frequency and check with previous frequency";
                            print "EXPECTED RESULT 6: Last operating frequency must be previous operating frequency";
                            print "ACTUAL RESULT 6: The previous operating frequency and last operating frequency are :%s and %s" %(Curr_Freq,Last_Freq);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6: Get the last operating frequency and check with previous frequency";
                            print "EXPECTED RESULT 6: Last operating frequency must be previous operating frequency";
                            print "ACTUAL RESULT 6: The previous operating frequency and last operating frequency are :%s and %s" %(Curr_Freq,Last_Freq);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Set the current frequency mask";
                        print "EXPECTED RESULT 5: Should set current frequency mask";
                        print "ACTUAL RESULT 5: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                    #set default frequency mask
                    tdkTestObj = obj.createTestStep('Mocastub_Set');
                    tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.FreqCurrentMaskSetting");
                    tdkTestObj.addParameter("ParamValue",Freq_Mask);
                    tdkTestObj.addParameter("Type","string");
                    expectedresult="SUCCESS";

                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details= tdkTestObj.getResultDetails();
                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP : Set the current frequency mask";
                        print "EXPECTED RESULT : Should set current frequency mask";
                        print "ACTUAL RESULT : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP : Set the current frequency mask";
                        print "EXPECTED RESULT : Should set current frequency mask";
                        print "ACTUAL RESULT : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Set the channel selection mode";
                    print "EXPECTED RESULT 4: Should set channel selection mode as false";
                    print "ACTUAL RESULT 4: %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
                #set default channel selection mode
                tdkTestObj = obj.createTestStep('Mocastub_Set');
                tdkTestObj.addParameter("ParamName","Device.MoCA.Interface.1.X_CISCO_COM_ChannelScanning");
                tdkTestObj.addParameter("ParamValue",ScanMode);
                tdkTestObj.addParameter("Type","bool");
                expectedresult="SUCCESS";

                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details= tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP : Set the channel selection mode";
                    print "EXPECTED RESULT : Should set channel selection mode as false";
                    print "ACTUAL RESULT : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP : Set the channel selection mode";
                    print "EXPECTED RESULT : Should set channel selection mode as false";
                    print "ACTUAL RESULT : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the current frequency mask";
                print "EXPECTED RESULT 3: Should get the current frequency mask";
                print "ACTUAL RESULT 3: The current operating frequency is :%s" %_Freq_Mask;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the current operating frequency";
            print "EXPECTED RESULT 2: Should get the current operating frequency";
            print "ACTUAL RESULT 2: The current operating frequency is :%s" %Curr_Freq;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the channel selection mode";
        print "EXPECTED RESULT 1: Should get the channel selection mode";
        print "ACTUAL RESULT 1: The channel selection mode is :%s" %ScanMode;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("moca");
else:
        print "Failed to load moca module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
