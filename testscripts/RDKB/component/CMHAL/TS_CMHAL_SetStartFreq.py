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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>3</version>
  <name>TS_CMHAL_SetStartFreq</name>
  <primitive_test_id/>
  <primitive_test_name>CMHAL_SetStartFreq</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Validate docsis_SetStartFreq() api by setting a new start frequency value</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_CMHAL_110</test_case_id>
    <test_objective>Validate docsis_SetStartFreq() api by setting a new start frequency value</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_SetStartFreq
docsis_GetDownFreq
Device.X_CISCO_COM_CableModem.DownstreamChannelNumberOfEntries
Device.X_CISCO_COM_CableModem.DownstreamChannel.i.Frequency</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  cmhal module
2. Get the current startFrequency using docsis_GetDownFreq() and save it
3. Get Device.X_CISCO_COM_CableModem.DownstreamChannelNumberOfEntries and check if it is greater than 0
4. Chose a new frequency from Device.X_CISCO_COM_CableModem.DownstreamChannel.i.Frequency, which is not equal to the initial start frequency
5. Set the chosen start frequency using docsis_SetStartFreq()
6. Wait for 60 seconds for set operation to reflect.
7. Invoke docsis_GetDownFreq() and check if previous set value is saved
8. Revert back to the initial start frequency
9. Unload  cmhal module

</automation_approch>
    <expected_output>docsis_SetStartFreq() api should successfully set a new start frequency value</expected_output>
    <priority>High</priority>
    <test_stub_interface>cmhal</test_stub_interface>
    <test_script>TS_CMHAL_SetStartFreq</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_SetStartFreq');
obj1.configureTestCase(ip,port,'TS_CMHAL_SetStartFreq');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():

    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
    tdkTestObj.addParameter("paramName","DownFreq");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    startFreq = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the start frequency";
        print "EXPECTED RESULT 1: Should get the start frequency";
        print "ACTUAL RESULT 1: Start frequency is %s" %startFreq;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_CableModem.DownstreamChannelNumberOfEntries");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        DSChannelCount = tdkTestObj.getResultDetails();

        print "TEST STEP 2: Get the DownstreamChannelNumberOfEntries";
        print "EXPECTED RESULT 2: Should get the DownstreamChannelNumberOfEntries";
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: DownstreamChannelNumberOfEntries is %s" %DSChannelCount
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if int(DSChannelCount) > 1:
                flag = 0
                print "Find a new start frequency value from DSChannel details"
                for i in range (1,3):
                    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
                    param = "Device.X_CISCO_COM_CableModem.DownstreamChannel."+str(i)+".Frequency"
                    tdkTestObj.addParameter("ParamName", param);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    print "TEST STEP 3: Get the DownstreamChannel.%d.Frequency" %i;
                    print "EXPECTED RESULT 3: Should get the DownstreamChannel.%d.Frequency" %i;
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 3: DownstreamChannel.%d.Frequency is %s" %(i,details)
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        if "MHz" in details:
                            details=details.split(" ")[0]
                            if '.' in details:
			        details=float(details)
                            newFreq=(int(details))*1000000
                        else:
                            newFreq = int(details)
                        if newFreq != int(startFreq):
                            flag = 1
                            break;
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 3:  %s" %details;
                        print "[TEST EXECUTION RESULT] : FAILURE";
                if flag == 1:
                    tdkTestObj = obj.createTestStep("CMHAL_SetStartFreq");
                    tdkTestObj.addParameter("Value",newFreq);
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    if expectedresult in actualresult :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4: Set the Start frequency to a new value ", newFreq;
                        print "EXPECTED RESULT 4: Should successfully set the Start frequency to a new value";
                        print "ACTUAL RESULT 4:  ",details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Wait for the set operation to reflect
                        sleep(60)
	                #validate the set function using get
                        tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
                        tdkTestObj.addParameter("paramName","DownFreq");
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        newStartFreq = tdkTestObj.getResultDetails();
    	                if expectedresult in actualresult and int(newStartFreq) == newFreq:
    	                    #Set the result status of execution
    	                    tdkTestObj.setResultStatus("SUCCESS");
    	                    print "TEST STEP 5: Get the start frequency and check if it became the new value set";
    	                    print "EXPECTED RESULT 5: Start frequency should change to the new value: ",newFreq;
    	                    print "ACTUAL RESULT 5: New Start frequency is %s" %newStartFreq;
    	                    #Get the result of execution
    	                    print "[TEST EXECUTION RESULT] : SUCCESS";
	                else:
	                    #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
    	                    print "TEST STEP 5: Get the start frequency and check if it became the new value set";
    	                    print "EXPECTED RESULT 5: Start frequency should change to the new value: ",newFreq;
                            print "ACTUAL RESULT 5: New Start frequency is %s" %newStartFreq;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE"
	                #Revert the start freq
	                tdkTestObj = obj.createTestStep("CMHAL_SetStartFreq");
                        tdkTestObj.addParameter("Value",int(startFreq));
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult :
                            #Wait for the set operation to reflect
                            sleep(60)
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP : Revert the value of Start frequency";
                            print "EXPECTED RESULT : Should revert the start frequency";
                            print "ACTUAL RESULT :  ",details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
	                else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP : Revert the value of Start frequency";
                            print "EXPECTED RESULT : Should revert the start frequency";
                            print "ACTUAL RESULT :  ",details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
	            else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Set the Start frequency to a new value", newFreq;
                        print "EXPECTED RESULT 4: Should successfully set the Start frequency to a new value";
                        print "ACTUAL RESULT 4:  ",details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "ERROR: Failed to get new start frequency to validate set api"
                    tdkTestObj.setResultStatus("FAILURE");
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                    print "ERROR: Not enough DSChannelCount. Count retreived is ", DSChannelCount
                    tdkTestObj.setResultStatus("FAILURE");
                    print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2:  %s" %DSChannelCount
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	#Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the start frequency";
        print "EXPECTED RESULT 1: Should get the start frequency";
        print "ACTUAL RESULT 1: Start frequency is %s" %StartFreq;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("cmhal");
    obj1.unloadModule("tdkbtr181");

else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
