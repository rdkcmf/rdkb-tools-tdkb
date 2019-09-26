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
  <version>21</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_ADVANCEDCONFIG_PFDuplicateServiceName</name>
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
  <remarks>Currently this test scenario requirement is under discussion</remarks>
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
    <test_case_id>TC_ADVANCEDCONFIG_4</test_case_id>
    <test_objective>To Validate "Parental Control &gt; Service name option for port forwarding rule" functionality</test_objective>
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
AdvancedConfig_GetNames

Input
1.PathName ("paramName")
( eg: "Device.NAT.X_Comcast_com_EnablePortMapping" )
Type: bool, Value: true

2.PathName ("paramName")
( eg: "Device.NAT.PortMapping." )

3. PathName ("paramName")
( eg: "Device.NAT.PortMapping.1.Alias" )
Type: string, Value: new service

4. PathName ("paramName")
( eg: "Device.NAT.PortMapping.1.Protocol" )
Type: string Value: UDP

5. PathName ("paramName")
( eg: "Device.NAT.PortMapping.1.ExternalPort" )
Type: unsignedint Value : 21

6. PathName ("paramName")
( eg: "Device.NAT.PortMapping.1.ExternalPortEndRange" )
Type: unsignedint Value : 21

7. PathName ("paramName")
( eg: "Device.NAT.PortMapping.1.InternalClient" )
Type: string Value : 192.168.22.22</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested  
(AdvancedConfig_Set,AdvancedConfig_AddObject, AdvancedConfig_GetNames - func name - "If not exists already"
 advancedconfig - module name
 Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automically by Test Manager with provided arguments in configure page (TS_ADVANCEDCONFIG_PFDuplicateServiceName.py)
3.Execute the generated Script(TS_ADVANCEDCONFIG_PFDuplicateServiceName.py) using execution page of  Test Manager GUI
4.advancedconfigstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named AdvancedConfig_Set, AdvancedConfig_AddObject through registered TDK advancedconfigstub function along with necessary Entry Values as arguments
5.AdvancedConfig_Set function will call ssp_setParameterValue,that inturn will call CCSP Base Interface Function named CcspBaseIf_setParameterValues.
6. AdvancedConfig_AddObject function will call ssp_addTableRow, that inturn will call CCSP Base Interface Function named CcspBaseIf_AddTblRow and AdvancedConfig_GetNames Will find the instance number of the row added and will process the function for the instance number generated.
7.Responses(printf) from TDK Component,Ccsp Library function and advancedcongifstub would be logged in Agent Console log based on the debug info redirected to agent console   
8.advancedconfigstub will validate the available result (from ssp_setParameterValue as zero) with expected result (zero) and the result is updated in agent console log and json output variable
9.TestManager will publish the result in GUI as SUCCESS/FAILURE based on the response from AdvancedConfig_Set and AdvancedConfig_AddObject function.</automation_approch>
    <except_output>Checkpoint 1:
Check if the service name option for port forwarding rule is success. 
CheckPoint 2:
Success log should be available in Agent Console Log
CheckPoint 3:
TDK agent Test Function will log the test case result as SUCCESS based on API response 
CheckPoint 4:
TestManager GUI will publish the result as SUCCESS in Execution page</except_output>
    <priority>High</priority>
    <test_stub_interface>none</test_stub_interface>
    <test_script>TS_ADVANCEDCONFIG_PFDuplicateServiceName</test_script>
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
obj.configureTestCase(ip,port,'TS_ADVANCEDCONFIG_PFDuplicateServiceName');

#Get the result of connection with test component and STB
loadModuleresult =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadModuleresult;

if "SUCCESS" in loadModuleresult.upper():
        obj.setLoadModuleStatus("SUCCESS");
	instance1 ="";
	instance2 ="";
	tdkTestObj = obj.createTestStep("AdvancedConfig_Get");
        tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult= tdkTestObj.getResult();
        #tdkTestObj.setResultStatus("SUCCESS");
        details_lan = tdkTestObj.getResultDetails();
        lanip = details_lan.split(':');
        iplist = lanip[1].split('.');
        iplist[3]= "7";
        clientIP1 = ".".join(iplist);
        clientIP=clientIP1.strip();	
	#Enabling port forwarding - setting the port mapping as true
        tdkTestObj = obj.createTestStep("AdvancedConfig_Set");
        tdkTestObj.addParameter("paramName","Device.NAT.X_Comcast_com_EnablePortMapping");
        tdkTestObj.addParameter("paramValue","true");
        tdkTestObj.addParameter("paramType","boolean");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
        if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                details = tdkTestObj.getResultDetails();
                print "[TEST STEP 1]: Enabling Port Mapping";
                print "[EXPECTED RESULT 1]: Should enable Port Mapping";
                print "[ACTUAL RESULT 1]: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Port Mapping is enabled\n"

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
                        print "[TEST STEP 2]: Adding new rule to Port Mapping";
                        print "[EXPECTED RESULT 2]: Should add new rule to Port Mapping";
                        print "[ACTUAL RESULT 2]: %s" %details;
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                        print "Add service option is selected and a new table is created\n"
                        temp = details.split(':');
                        instance1 = temp[1];
                        if (instance1>0):
                            print "INSTANCE VALUE: %s" %instance1
                            # Setting the service name
                            tdkTestObj = obj.createTestStep("AdvancedConfig_SetMultiple");
                            tdkTestObj.addParameter("paramList","Device.NAT.PortMapping.%s.ExternalPort|21|unsignedint|Device.NAT.PortMapping.%s.InternalPort|1|unsignedint|Device.NAT.PortMapping.%s.Protocol|UDP|string|Device.NAT.PortMapping.%s.InternalClient|%s|string|Device.NAT.PortMapping.%s.Description|NEW_RULE|string|Device.NAT.PortMapping.%s.ExternalPortEndRange|21|unsignedint|Device.NAT.PortMapping.%s.Enable|true|bool" %(instance1, instance1, instance1, instance1, clientIP, instance1, instance1, instance1));
                            expectedresult="SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                details = tdkTestObj.getResultDetails();
                                print "[TEST STEP 3]: Setting external port";
                                print "[EXPECTED RESULT 3]: Should set external port successfully";
                                print "[ACTUAL RESULT 3]: %s" %details;
                                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                print "Added port mapping rule successfully\n"
                                # Adding new row
                                tdkTestObj = obj.createTestStep("AdvancedConfig_AddObject");
                                tdkTestObj.addParameter("paramName","Device.NAT.PortMapping.");
                                expectedresult="SUCCESS";
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                if expectedresult in actualresult:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    details = tdkTestObj.getResultDetails();
                                    print "[TEST STEP 4]: Adding new rule to Port Mapping";
                                    print "[EXPECTED RESULT 4]: Should add new rule to Port Mapping";
                                    print "[ACTUAL RESULT 4]: %s" %details;
                                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                    print "Add service option is selected and a new table is created\n"
                                    temp = details.split(':');
                                    instance2 = temp[1];
                                    #setting the start port
                                    tdkTestObj = obj.createTestStep("AdvancedConfig_SetMultiple");
                                    tdkTestObj.addParameter("paramList","Device.NAT.PortMapping.%s.ExternalPort|22|unsignedint|Device.NAT.PortMapping.%s.InternalPort|5|unsignedint|Device.NAT.PortMapping.%s.Protocol|UDP|string|Device.NAT.PortMapping.%s.InternalClient|%s|string|Device.NAT.PortMapping.%s.Description|NEW_RULE|string|Device.NAT.PortMapping.%s.ExternalPortEndRange|31|unsignedint|Device.NAT.PortMapping.%s.Enable|true|bool" %(instance2, instance2, instance2, instance2, clientIP, instance2, instance2, instance2));
                                    expectedresult="FAILURE";
                                    tdkTestObj.executeTestCase(expectedresult);
                                    actualresult = tdkTestObj.getResult();
                                    if expectedresult in actualresult:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        details = tdkTestObj.getResultDetails();
                                        print "[TEST STEP 5]: Setting external port with duplicate value";
                                        print "[EXPECTED RESULT 5]: Should not set external port with duplicate value";
                                        print "[ACTUAL RESULT 5]: %s" %details;
                                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                        print "Duplicate port forwarding rules are not allowed, since same service name is given\n"
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        details = tdkTestObj.getResultDetails();
                                        print "[TEST STEP 5]: Setting external port with duplicate value";
                                        print "[EXPECTED RESULT 5]: Should not set external port with duplicate value";
                                        print "[ACTUAL RESULT 5]: %s" %details;
                                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                        print "Failure in validating duplicate service name for the port forwarding rules\n"
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    details = tdkTestObj.getResultDetails();
                                    print "[TEST STEP 4]: Adding new rule to Port Mapping";
                                    print "[EXPECTED RESULT 4]: Should add new rule to Port Mapping";
                                    print "[ACTUAL RESULT 4]: %s" %details;
                                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                    print "Failure in adding the new port forwarding row\n"
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                details = tdkTestObj.getResultDetails();
                                print "[TEST STEP 3]: Setting external port";
                                print "[EXPECTED RESULT 3]: Should set external port successfully";
                                print "[ACTUAL RESULT 3]: %s" %details;
                                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                                print "Failure in setting the start port\n"


                        else:
                            print "Instance value should be greater than 0\n"
                            print "Wrong instance value\n"
                else:
                        tdkTestObj.setResultStatus("FAILURE");
                        details = tdkTestObj.getResultDetails();
                        print "[TEST STEP 2]: Adding new rule to Port Mapping";
                        print "[EXPECTED RESULT 2]: Should add new rule to Port Mapping";
                        print "[ACTUAL RESULT 2]: %s" %details;
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                        print "Failure in adding the new port forwarding row\n"
        else:
                tdkTestObj.setResultStatus("FAILURE");
                details = tdkTestObj.getResultDetails();
                print "[TEST STEP 1]: Enabling Port Mapping";
                print "[EXPECTED RESULT 1]: Should enable Port Mapping";
                print "[ACTUAL RESULT 1]: %s" %details;
                print "[TEST EXECUTION RESULT] : %s" %actualresult;
                print "Failure in setting the port forwarding as true\n "

        #To delete the added table
        if instance1:
            tdkTestObj = obj.createTestStep("AdvancedConfig_DelObject");
            tdkTestObj.addParameter("paramName","Device.NAT.PortMapping.%s." %instance1);
            expectedresult = "SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            if expectedresult in actualresult:
                if instance2:
                    tdkTestObj = obj.createTestStep("AdvancedConfig_DelObject");
                    tdkTestObj.addParameter("paramName","Device.NAT.PortMapping.%s." %instance2);
                    expectedresult = "SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
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

					

					

					

					

					

					
