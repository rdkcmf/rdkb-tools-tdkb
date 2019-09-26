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
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_TAD_SetAvgMemoryThreshold</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if setting of a valid value to Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold is success</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <box_type>Emulator</box_type>
    <!--  -->
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TAD_62</test_case_id>
    <test_objective>Check if setting of a valid value to Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold is success</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI.</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Get, TADstub_Set</api_or_interface_used>
    <input_parameters>Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold</input_parameters>
    <automation_approch>1. Load TAD module
2. Get and save the value of Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold
3. Set a new positive valid value as AvgCPUThreshold
4. Get Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold and check if the set value is reflected or not
5. Revert the value of Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold
6. Unload the TAD module</automation_approch>
    <except_output>Set operation of a valid value on Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold should be success</except_output>
    <priority>High</priority>
    <test_stub_interface>tad</test_stub_interface>
    <test_script>TS_TAD_SetAvgMemoryThreshold</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_SetAvgMemoryThreshold');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    print "TEST STEP 1: Get the current average Memory threshold"
    print "EXPECTED RESULT 1: Should get the current average Memory threshold"
    tdkTestObj = obj.createTestStep('TADstub_Get');
    tdkTestObj.addParameter("paramName","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold")
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    orgValue = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
	print "ACTUAL RESULT 1: %s" %orgValue
	if int(orgValue) > 5:
	    newValue = int(orgValue) - 5
	else:
	    newValue = int(orgValue) + 5
	tdkTestObj = obj.createTestStep('TADstub_Set');
        tdkTestObj.addParameter("ParamName","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold")
        tdkTestObj.addParameter("ParamValue",str(newValue));
        tdkTestObj.addParameter("Type","unsignedint");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set a new value to AvgMemoryThreshold";
            print "EXPECTED RESULT 2: Should set a new value to AvgMemoryThreshold";
            print "ACTUAL RESULT 2: %s" %details;
	    print "[TEST EXECUTION RESULT] : SUCCESS";

	    #Using get check if the value is properly set or not
            print "TEST STEP 3: Get the current average Memory threshold and compare with set value"
            print "EXPECTED RESULT 3: Current average Memory threshold should be equal to the set value"
            tdkTestObj = obj.createTestStep('TADstub_Get');
            tdkTestObj.addParameter("paramName","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold")
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            getValue = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and int(getValue) == newValue:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: current average Memory threshold is %s" %getValue
	        print "[TEST EXECUTION RESULT] : SUCCESS";

	        #Revert Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold to its original value
	        print "TEST STEP 4: Revert to the original value of AvgMemoryThreshold";
                print "EXPECTED RESULT 4: Should revert to the original value of AvgMemoryThreshold"
                tdkTestObj = obj.createTestStep('TADstub_Set');
                tdkTestObj.addParameter("ParamName","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold")
                tdkTestObj.addParameter("ParamValue",orgValue);
                tdkTestObj.addParameter("Type","unsignedint");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: Successfully reverted AvgMemoryThreshold"
                    print "[TEST EXECUTION RESULT] : SUCCESS";
	        else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: Failed to revert AvgMemoryThreshold"
                    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: current average Memory threshold is %s" %getValue
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set a new value to AvgMemoryThreshold";
            print "EXPECTED RESULT 2: Should set a new value to AvgMemoryThreshold";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the current average Memory threshold"
        print "EXPECTED RESULT 1: Should get the current AvgMemoryThreshold"
        print "ACTUAL RESULT 1: %s" %orgValue;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tad");

else:
    print "Failed to load tad module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
