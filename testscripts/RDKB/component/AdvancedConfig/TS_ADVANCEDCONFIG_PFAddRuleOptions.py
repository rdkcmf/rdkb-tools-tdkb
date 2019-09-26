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
  <version>14</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ADVANCEDCONFIG_PFAddRuleOptions</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>AdvancedConfig_Set</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis></synopsis>
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
    <test_case_id>TC_ADVANCEDCONFIG_5</test_case_id>
    <test_objective>To Validate "Parental Control &gt; ADD rule must have options to configure port forwarding" functionality</test_objective>
    <test_type>Possitive</test_type>
    <test_setup>Emulator,
XB3</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Json Interface:
API Name
AdvancedConfig_Set
AdvancedConfig_AddObject
AdvancedConfig_Get
AdvancedConfig_GetNames

Input
1.PathName ("paramName")
( eg: "Device.NAT.X_Comcast_com_EnablePortMapping" )
Type: bool  Value : true

2.PathName ("paramName")
( eg: "Device.NAT.PortMapping." )

3. PathName ("paramName")
( eg: "Device.NAT.PortMapping.1.Alias" )

4. PathName ("paramName")
( eg: "Device.NAT.PortMapping.1.Protocol" )

5. PathName ("paramName")
( eg: "Device.NAT.PortMapping.1.ExternalPort" )

6. PathName ("paramName")
( eg: "Device.NAT.PortMapping.1.ExternalPortEndRange" )

7. PathName ("paramName")
( eg: "Device.NAT.PortMapping.1.InternalClient" )</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested  
(AdvancedConfig_Set, AdvancedConfig_AddObject, AdvancedConfig_Get  - func name - "If not exists already"
 advancedconfig - module name
 Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automically by Test Manager with provided arguments in configure page (TS_ADVANCEDCONFIG_PFAddRuleOptions.py)
3.Execute the generated Script(TS_ADVANCEDCONFIG_PFAddRuleOptions.py) using execution page of  Test Manager GUI
4.advancedconfigstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named AdvancedConfig_Set,AdvancedConfig_AddObject and AdvancedConfig_Get  through registered TDK advancedconfigstub function along with necessary Entry Values as arguments
5.AdvancedConfig_Set function will call ssp_setParameterValue,that inturn will call CCSP Base Interface Function named CcspBaseIf_setParameterValues.
6. AdvancedConfig_AddObject function will call ssp_addTableRow, that inturn will call CCSP Base Interface Function named CcspBaseIf_AddTblRow and AdvancedConfig_GetNames Will find the instance number of the row added and will process the function for the instance number generated.
7. AdvancedConfig_Get function will call ssp_getParameterValue, that inturn will call CCSP Base Interface Function named CcspBaseIf_getParameterValues.
8.Responses(printf) from TDK Component,Ccsp Library function and advancedcongifstub would be logged in Agent Console log based on the debug info redirected to agent console   
9.advancedconfigstub will validate the available result (from ssp_setParameterValue as zero) with expected result (zero) and the result is updated in agent console log and json output variable
10.TestManager will publish the result in GUI as SUCCESS/FAILURE based on the response from AdvancedConfig_Set, AdvancedConfig_Get and AdvancedConfig_Addbject functions.</automation_approch>
    <except_output>Checkpoint 1:
Check if ADD rule have options to configure port forwarding
CheckPoint 2:
Success log should be available in Agent Console Log
CheckPoint 3:
TDK agent Test Function will log the test case result as SUCCESS based on API response 
CheckPoint 4:
TestManager GUI will publish the result as SUCCESS in Execution page</except_output>
    <priority>High</priority>
    <test_stub_interface>none</test_stub_interface>
    <test_script>TS_ADVANCEDCONFIG_PFAddRuleOptions</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
																								#use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import tdkutility;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("advancedconfig","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ADVANCEDCONFIG_PFAddRuleOptions');

#Get the result of connection with test component and STB
loadModuleresult =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadModuleresult;

if "SUCCESS" in loadModuleresult.upper():
        obj.setLoadModuleStatus("SUCCESS");
	instance ="";
        #Enabling port forwarding - setting the port mapping as true
        tdkTestObj = obj.createTestStep("AdvancedConfig_Set");
        tdkTestObj.addParameter("paramName","Device.NAT.X_Comcast_com_EnablePortMapping");
        tdkTestObj.addParameter("paramValue","true");
        tdkTestObj.addParameter("paramType","boolean");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                details = tdkTestObj.getResultDetails();
                print "[TEST STEP 1]: Enabling Port Trigger";
                print "[EXPECTED RESULT 1]: Should enable Port Trigger";
                print "[ACTUAL RESULT 1]: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Port triggering is enabled\n"

                # Adding a new row to the port forwarding table
                tdkTestObj = obj.createTestStep("AdvancedConfig_AddObject");
                tdkTestObj.addParameter("paramName","Device.NAT.PortMapping.");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                if expectedresult in actualresult:
                #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        details = tdkTestObj.getResultDetails();
                        print "[TEST STEP 2]: Adding new rule to Port Trigger";
                        print "[EXPECTED RESULT 2]: Should add new rule to Port Trigger";
                        print "[ACTUAL RESULT 2]: %s" %details;
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                        print "Add service option is selected and a new table is created\n"
			temp = details.split(':');
                        instance = temp[1];

                        if (instance > 0):
                            print "INSTANCE VALUE: %s" %instance
                            # Getting the service name
                            tdkTestObj = obj.createTestStep("AdvancedConfig_Get");
                            tdkTestObj.addParameter("paramName","Device.NAT.PortMapping.%s.Alias" %instance);
                            expectedresult="SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                details = tdkTestObj.getResultDetails();
                                print "[TEST STEP 3]: Getting external port values";
                                print "[EXPECTED RESULT 3]: Should get external port value successfully";
                                print "[ACTUAL RESULT 3]: %s" %details;
                                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                print "Retrieved port mapping rule value successfully\n"

                                # Getting the protocol type
                                tdkTestObj = obj.createTestStep("AdvancedConfig_Get");
                                tdkTestObj.addParameter("paramName","Device.NAT.PortMapping.%s.Protocol"%instance);
                                expectedresult="SUCCESS";
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                if expectedresult in actualresult:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    details = tdkTestObj.getResultDetails();
                                    print "[TEST STEP 4]: Getting external port values";
                                    print "[EXPECTED RESULT 4]: Should get external port values successfully";
                                    print "[ACTUAL RESULT 4]: %s" %details;
                                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                    print "Retrieved port mapping rule value successfully\n"
                                    #getting the start port
                                    tdkTestObj = obj.createTestStep("AdvancedConfig_Get");
                                    tdkTestObj.addParameter("paramName","Device.NAT.PortMapping.%s.ExternalPort"%instance);
                                    expectedresult="SUCCESS";
                                    tdkTestObj.executeTestCase(expectedresult);
                                    actualresult = tdkTestObj.getResult();
                                    if expectedresult in actualresult:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        details = tdkTestObj.getResultDetails();
	                                print "[TEST STEP 5]: Getting external port values";
        	                        print "[EXPECTED RESULT 5]: Should get external port value successfully";
                	                print "[ACTUAL RESULT 5]: %s" %details;
                        	        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                	print "Retrieved port mapping rule value successfully\n"
                                        #getting the end port
                                        tdkTestObj = obj.createTestStep("AdvancedConfig_Get");
                                        tdkTestObj.addParameter("paramName","Device.NAT.PortMapping.%s.ExternalPortEndRange" %instance) ;
                                        expectedresult="SUCCESS";
                                        tdkTestObj.executeTestCase(expectedresult);
                                        actualresult = tdkTestObj.getResult();
                                        if expectedresult in actualresult:
                                            #Set the result status of execution
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            details = tdkTestObj.getResultDetails();
	                                    print "[TEST STEP 6: Getting external port values";
        	                            print "[EXPECTED RESULT 6: Should get external port values successfully";
                	                    print "[ACTUAL RESULT 6: %s" %details;
                        	            print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                	    print "Retrieved port mapping rule value successfully\n"
                                            #getting the ip
                                            tdkTestObj = obj.createTestStep("AdvancedConfig_Get");
                                            tdkTestObj.addParameter("paramName","Device.NAT.PortMapping.%s.InternalClient" %instance);
                                            expectedresult="SUCCESS";
                                            tdkTestObj.executeTestCase(expectedresult);
                                            actualresult = tdkTestObj.getResult();
                                            if expectedresult in actualresult:

                                                #Set the result status of execution
                                                tdkTestObj.setResultStatus("SUCCESS");
                                                details = tdkTestObj.getResultDetails();
	                                        print "[TEST STEP 7]: Getting external port values";
        	                                print "[EXPECTED RESULT 7]: Should get external port value successfully";
                	                        print "[ACTUAL RESULT 7]: %s" %details;
                        	                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                	        print "Retrieved port mapping rule value successfully\n"
                                            else:
                                                tdkTestObj.setResultStatus("FAILURE");
                                                details = tdkTestObj.getResultDetails();
                                                print "[TEST STEP 7]: Getting external port values";
                                                print "[EXPECTED RESULT 7]: Should get external port value successfully";
                                                print "[ACTUAL RESULT 7]: %s" %details;
                                                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                                print "Failure in getting the IP option\n"

                                        else:
                                            tdkTestObj.setResultStatus("FAILURE");
                                            details = tdkTestObj.getResultDetails();
                                            print "[TEST STEP 6: Getting external port values";
                                            print "[EXPECTED RESULT 6: Should get external port values successfully";
                                            print "[ACTUAL RESULT 6: %s" %details;
                                            print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                            print "Failure in getting the end port\n"
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        details = tdkTestObj.getResultDetails();
                                        print "[TEST STEP 5]: Getting external port values";
                                        print "[EXPECTED RESULT 5]: Should get external port value successfully";
                                        print "[ACTUAL RESULT 5]: %s" %details;
                                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                        print "Failure in getting the start port\n"
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    details = tdkTestObj.getResultDetails();
                                    print "[TEST STEP 4]: Getting external port values";
                                    print "[EXPECTED RESULT 4]: Should get external port values successfully";
                                    print "[ACTUAL RESULT 4]: %s" %details;
                                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                    print "Failure in getting the protocol type\n"
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                details = tdkTestObj.getResultDetails();
                                print "[TEST STEP 3]: Getting external port values";
                                print "[EXPECTED RESULT 3]: Should get external port value successfully";
                                print "[ACTUAL RESULT 3]: %s" %details;
                                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                print "Failure in getting the service name\n"
                                
                        else:
                            print "Instance value should be greater than 0\n"
                            print "Wrong instance value\n"
               
                else:
                        tdkTestObj.setResultStatus("FAILURE");
                        details = tdkTestObj.getResultDetails();
                        print "[TEST STEP 2]: Adding new rule to Port Trigger";
                        print "[EXPECTED RESULT 2]: Should add new rule to Port Trigger";
                        print "[ACTUAL RESULT 2]: %s" %details;
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                        print "Failure in adding the new port forwarding row\n"
        else:
                tdkTestObj.setResultStatus("FAILURE");
                details = tdkTestObj.getResultDetails();
                print "[TEST STEP 1]: Enabling Port Trigger";
                print "[EXPECTED RESULT 1]: Should enable Port Trigger";
                print "[ACTUAL RESULT 1]: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Failure in setting the port forwarding as true\n "

        #To delete the added table
        if instance:
            tdkTestObj = obj.createTestStep("AdvancedConfig_DelObject");
            tdkTestObj.addParameter("paramName","Device.NAT.PortMapping.%s." %instance);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                details = tdkTestObj.getResultDetails();
                print "[TEST STEP ]: Deleting the added rule";
                print "[EXPECTED RESULT ]: Should delete the added rule";
                print "[ACTUAL RESULT]: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Added table is deleted successfully\n"
            else:
                print "[TEST STEP ]: Deleting the added rule";
                print "[EXPECTED RESULT ]: Should delete the added rule";
                print "[ACTUAL RESULT]: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Added table could not be deleted\n"
            
        obj.unloadModule("advancedconfig");
else:
        print "FAILURE to load Advancedconfig module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading FAILURE";

					

					

					

					

					
