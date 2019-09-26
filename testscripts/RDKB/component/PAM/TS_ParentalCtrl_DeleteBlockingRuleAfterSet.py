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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ParentalCtrl_DeleteBlockingRuleAfterSet</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Test whether a rule can be deleted after setting its attributes</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks>Currently this test case scenario is under discussion against the product design/requirement</remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_PAM_130</test_case_id>
    <test_objective>Test to delete a rule after setting its attribute</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3, Emulator</test_setup>
    <pre_requisite>TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>pam_GetParameterValues
AdvancedConfig_Set
AdvancedConfig_AddObject
AdvancedConfig_SetMultiple
AdvancedConfig_DelObject</api_or_interface_used>
    <input_parameters>Device.X_Comcast_com_ParentalControl.ManagedSites.Enable
Device.X_Comcast_com_ParentalControl.ManagedSites.BlockedSite.
Device.X_Comcast_com_ParentalControl.ManagedSites.BlockedSite.%s.BlockMethod|URL|string|Device.X_Comcast_com_ParentalControl.ManagedSites.BlockedSite.%s.Site|http://www.google.com|string|Device.X_Comcast_com_ParentalControl.ManagedSites.BlockedSite.%s.AlwaysBlock|true|bool" %(instance, instance, instance)</input_parameters>
    <automation_approch>1.Function which needs to be tested will be configured in Test Manager GUI.
2.Python Script will be generated by Test Manager with provided arguments in configure page.
3.TM will load the pamstub lib via Test agent
5.with pamstub's getparamvalue() get Device.X_Comcast_com_ParentalControl.ManagedSites.Enablestore it and set it as true
4. With AdvancedConfig_AddObject add new blockedsite instance
5. With AdvancedConfig_SetMultiple, set mode of blocking and url
6. With AdvancedConfig_DelObject delete the added instance
7.pam stub will validate the actual result with the expected result and send the result status to Test Manager.
8.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from pam stub.</automation_approch>
    <except_output>CheckPoint 1:
 The output  should be logged in the Agent console/Component log

CheckPoint 2:
Stub function result should be success and should see corresponding log in the agent console log

CheckPoint 3:
TestManager GUI will publish the result as PASS in Execution/Console page of Test Manager</except_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_ParentalCtrl_DeleteBlockingRuleAfterSet</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
																								# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");
obj = tdklib.TDKScriptingLibrary("advancedconfig","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ParentalCtrl_DeleteBlockingRuleAfterSet');
pamObj.configureTestCase(ip,port,'TS_ParentalCtrl_DeleteBlockingRuleAfterSet');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
pamloadmodulestatus =pamObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper():
    #get the orinal status and store it
    obj.setLoadModuleStatus("SUCCESS");
    pamObj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.X_Comcast_com_ParentalControl.ManagedSites.Enable");
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");

	org_status = details;
        print "TEST STEP 1: Get ManagedSites Enable status";
        print "EXPECTED RESULT 1: Should get the Enable status";
        print "ACTUAL RESULT 1: ManagedSites Enable status is %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        tdkTestObj = obj.createTestStep('AdvancedConfig_Set');
        tdkTestObj.addParameter("paramName","Device.X_Comcast_com_ParentalControl.ManagedSites.Enable");
        tdkTestObj.addParameter("paramValue","true");
        tdkTestObj.addParameter("paramType","boolean");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP 2: Set ManagedSites Enable status as true";
            print "EXPECTED RESULT 2: Should set the Enable status as true";
	    print "ACTUAL RESULT 2: ManagedSites Enable status is %s" %details;
            #Get the result of execution
	    print "[TEST EXECUTION RESULT] : SUCCESS";

	    #add a new site to be blocked
	    tdkTestObj = obj.createTestStep("AdvancedConfig_AddObject");
            tdkTestObj.addParameter("paramName","Device.X_Comcast_com_ParentalControl.ManagedSites.BlockedSite.");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
    	        #Set the result status of execution
		tdkTestObj.setResultStatus("SUCCESS");
		print "[TEST STEP 3]: Adding new rule for site blocking";
	        print "[EXPECTED RESULT 3]: Should add new rule";
                print "[ACTUAL RESULT 3]: added new rule %s" %details;
        	print "[TEST EXECUTION RESULT] : %s" %actualresult;
		temp = details.split(':');
                instance = temp[1];

                if (instance > 0):
                    print "INSTANCE VALUE: %s" %instance
                    tdkTestObj = obj.createTestStep("AdvancedConfig_SetMultiple");
                    tdkTestObj.addParameter("paramList","Device.X_Comcast_com_ParentalControl.ManagedSites.BlockedSite.%s.BlockMethod|URL|string|Device.X_Comcast_com_ParentalControl.ManagedSites.BlockedSite.%s.Site|http://google.com|string|Device.X_Comcast_com_ParentalControl.ManagedSites.BlockedSite.%s.AlwaysBlock|true|bool" %(instance, instance, instance));
		    expectedresult="SUCCESS";
	            tdkTestObj.executeTestCase(expectedresult);
            	    actualresult = tdkTestObj.getResult();
	            details = tdkTestObj.getResultDetails();
        	    if expectedresult in actualresult:
	                tdkTestObj.setResultStatus("SUCCESS");
                	print "[TEST STEP 4]: Setting attrributes to rule"
	                print "[EXPECTED RESULT 4]: Should be able to set attributes to rule"
            	        print "[ACTUAL RESULT 4]: SUCESS: able to set attributes to rule %s" %details;
	                print "[TEST EXECUTION RESULT] : %s" %actualresult;

		    else:
		        tdkTestObj.setResultStatus("FAILURE");
                        print "[TEST STEP 4]: Setting attrributes to rule"
                        print "[EXPECTED RESULT 4]: Should be able to set attributes to rule"
                        print "[ACTUAL RESULT 4]: FAILURE: Couldnot add url in rule";
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;

		    #Delete the created table entry
	            tdkTestObj = obj.createTestStep("AdvancedConfig_DelObject");
	            tdkTestObj.addParameter("paramName","Device.X_Comcast_com_ParentalControl.ManagedSites.BlockedSite.%s." %instance);
	            expectedresult = "SUCCESS";
        	    tdkTestObj.executeTestCase(expectedresult);
	            actualresult = tdkTestObj.getResult();
        	    print "[TEST EXECUTION RESULT] : %s" %actualresult ;
	            details = tdkTestObj.getResultDetails();
	            if expectedresult in actualresult:
        	        #Set the result status of execution
                	tdkTestObj.setResultStatus("SUCCESS");
  		        print "[TEST STEP ]: Deleting the added rule";
	       	        print "[EXPECTED RESULT ]: Should delete the added rule";
        	        print "[ACTUAL RESULT]: %s" %details;
                	print "[TEST EXECUTION RESULT] : %s" %actualresult;
	                print "Added table is deleted successfully\n"
        	    else:
			tdkTestObj.setResultStatus("FAILURE");
	        	print "[TEST STEP ]: Deleting the added rule";
	                print "[EXPECTED RESULT ]: Should delete the added rule";
        	        print "[ACTUAL RESULT]: %s" %details;
                	print "[TEST EXECUTION RESULT] : %s" %actualresult;
	                print "Added table could not be deleted\n"

   	        else:
		    print "Table add returned invalid instance"
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "[TEST STEP 3]: Adding new rule for site blocking";
                print "[EXPECTED RESULT 3]: Should add new rule";
                print "[ACTUAL RESULT 3]: failed to add new rule %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;

            #set enable status to its original value
            tdkTestObj = obj.createTestStep('AdvancedConfig_Set');
            tdkTestObj.addParameter("paramName","Device.X_Comcast_com_ParentalControl.ManagedSites.Enable");
            tdkTestObj.addParameter("paramValue",org_status.strip());
            tdkTestObj.addParameter("paramType","boolean");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Set ManagedSites Enable status as its initial value";
                print "EXPECTED RESULT 2: Should set the Enable status as its initial value";
                print "ACTUAL RESULT 2: ManagedSites Enable status set success"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Set ManagedSites Enable status as its initial value";
                print "EXPECTED RESULT 2: Should set the Enable status as its initial value";
                print "ACTUAL RESULT 2: ManagedSites Enable status set failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    	else:
	    tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Set ManagedSites Enable status as true";
            print "EXPECTED RESULT 1: Should set the Enable status as true";
            print "ACTUAL RESULT 1: ManagedSites Enable status set failed";
	    print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get ManagedSites Enable status";
        print "EXPECTED RESULT 1: Should get the status";
        print "ACTUAL RESULT 1: ManagedSites Enable status is %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("advancedconfig");
    pamObj.unloadModule("pam");

else:
        print "Failed to load pam module";
        obj.setLoadModuleStatus("FAILURE");
        pamObj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";







