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
  <version>38</version>
  <name>TS_WIFIAGENT_AddAndDeleteCSITableInstance_CheckDefaultValues</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_AddObject</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if a new CSI Table instance is created successfully by add table operation with the parameter Device.WiFi.X_RDK_CSI. and the added instance should have the Enable parameter and ClientMacList parameter with default values false and empty respectively. Also set new values to CSI instance parameters and delete the added instance by delete table operation.</synopsis>
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
    <test_case_id>TC_WIFIAGENT_171</test_case_id>
    <test_objective>To check if a new CSI Table instance is created successfully by add table operation with the parameter Device.WiFi.X_RDK_CSI. and the added instance should have the Enable parameter and ClientMacList parameter with default values false and empty respectively. Also set new values to CSI instance parameters and delete the added instance by delete table operation.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Device should be in RBUS mode</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.X_RDK_CSI.
enable_param : Device.WiFi.X_RDK_CSI.[i].Enable
ClientMaclist_param : Device.WiFi.X_RDK_CSI.[i].ClientMaclist
paramName : Device.WiFi.X_RDK_CSI.[i].</input_parameters>
    <automation_approch>1. Load the modules
2. Check the pre-requisites : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable - true, Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable - false and Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable - true. If the Mesh enable or Band Steering enable have different values, set them to true and false respectively provided the DUT is initially in RBUS mode. Else return failure.
3. Add a new instance to the CSI data table using Device.WiFi.X_RDK_CSI.
4. Check if a valid instance number is returned greater than 0 is returned.
5. Query Device.WiFi.X_RDK_CSI.[i].Enable and Device.WiFi.X_RDK_CSI.[i].ClientMaclist and ensure that they have default values false and empty respectively.
6. Set Device.WiFi.X_RDK_CSI.[i].Enable to true and Device.WiFi.X_RDK_CSI.[i].ClientMaclist to AA:BB:CC:DD:EE:FF and cross check with GET.
7. Delete the newly added CSI table instance using Device.WiFi.X_RDK_CSI.[i].
8. Revert to initial state if required.
9. Unload the modules</automation_approch>
    <expected_output>New CSI Table instance should be created successfully and the default values of the enable and ClientMACList parameter should be false and empty respectively and setting the CSI instance parameters to new values should be success and deletion of the newly added instance should return success.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_AddAndDeleteCSITableInstance_CheckDefaultValues</test_script>
    <skipped>No</skipped>
    <release_version>M99</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *
from tdkutility import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1 = tdklib.TDKScriptingLibrary("tad","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_AddAndDeleteCSITableInstance_CheckDefaultValues');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_AddAndDeleteCSITableInstance_CheckDefaultValues');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";

    #Check the pre-requisites; Band Steering should be Disabled, RBUS and Mesh should be enabled
    pre_req_set, tdkTestObj, step, revert_flag, initial_val = CheckPreReqForCSI(obj1, obj);

    if pre_req_set == 1:
        print "\n*************All pre-requisites set for the DUT*****************";
        #Add a new CSI Object
        step = step + 1;
        tdkTestObj = obj.createTestStep("TDKB_TR181Stub_AddObject");
        tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK_CSI.");
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP %d: Add a new CSI Table instance" %step;
        print "EXPECTED RESULT %d: Should add a new CSI Table instance successfully" %step;

        if expectedresult in actualresult and details != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Added a new CSI Table instance successfully; Details : %s" %(step, details);
            print "TEST EXECUTION RESULT : %s" %actualresult;
            instance = details.split(':')[1];

            if instance.isdigit() and int(instance) > 0:
                tdkTestObj.setResultStatus("SUCCESS");
                print "INSTANCE VALUE : %s" %instance;

                #Check default values of the Enable value and ClientMaclist after instance is created
                step = step + 1;
                sleep(5);
                enable_param = "Device.WiFi.X_RDK_CSI." + instance + ".Enable";
                ClientMaclist_param = "Device.WiFi.X_RDK_CSI." + instance + ".ClientMaclist";
                tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Get");
                actualresult1, details1 = getTR181Value(tdkTestObj, enable_param);
                actualresult2, details2 = getTR181Value(tdkTestObj, ClientMaclist_param);

                print "\nTEST STEP %d : Get the default values of %s and %s and check if it is false and empty respectively" %(step, enable_param, ClientMaclist_param);
                print "EXPECTED RESULT %d : The values should be retrieved successfully and it should be false and empty respectively" %step;

                if expectedresult in actualresult1 and expectedresult in actualresult2:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : The default values of the newly added instance retrieved successfully" %step;
                    print "%s : %s, %s : %s" %(enable_param, details1, ClientMaclist_param, details2);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if details1 == "false" and details2 == "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "The default values of the new CSI Table instance - %s is false and %s is empty as expected" %(enable_param, ClientMaclist_param);

                        #Check if are able to set new values to both parameters
                        hostMacAddress = "AA:BB:CC:DD:EE:FF";
                        step = step + 1;
                        tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Set");
                        actualresult1, details1 = setTR181Value(tdkTestObj, enable_param, "true", "boolean");
                        actualresult2, details2 = setTR181Value(tdkTestObj, ClientMaclist_param, hostMacAddress, "string");

                        print "\nTEST STEP %d : Set values for %s and %s to true and %s respectively" %(step, enable_param, ClientMaclist_param, hostMacAddress);
                        print "EXPECTED RESULT %d : The values should be set successfully" %step;

                        if expectedresult in actualresult1 and expectedresult in actualresult2:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d : The Enable and ClientMAC values of the newly added instance set successfully" %step;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Cross check the SET values with GET
                            step = step + 1;
                            tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Get");
                            actualresult1, details1 = getTR181Value(tdkTestObj, enable_param);
                            actualresult2, details2 = getTR181Value(tdkTestObj, ClientMaclist_param);

                            print "\nTEST STEP %d : Get the values of %s and %s and check if it is same as set values" %(step, enable_param, ClientMaclist_param);
                            print "EXPECTED RESULT %d : The values should be retrieved successfully and it should be the same as set values" %step;

                            if expectedresult in actualresult1 and expectedresult in actualresult2:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d : The values of the newly added instance retrieved successfully" %step;
                                print "%s : %s, %s : %s" %(enable_param, details1, ClientMaclist_param, details2);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                if details1 == "true" and details2 == hostMacAddress:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "The values of the new CSI Table instance - %s is true and %s is %s as expected" %(enable_param, ClientMaclist_param, hostMacAddress);
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "The GET values of the new CSI Table instance are not as expected";
                            else :
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d : Failed to retrieve the new CSI Table instance values" %step;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d : The Enable and ClientMAC values of the newly added instance NOT set successfully" %step;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "The default values of the new CSI Table instance are not as expected";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : Failed to retrieve the new CSI Table instance values" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Delete the added instance from the CSI Table
                step = step + 1;
                tdkTestObj = obj.createTestStep("TDKB_TR181Stub_DelObject");
                tdkTestObj.addParameter("paramName","Device.WiFi.X_RDK_CSI.%s." %instance);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP %d : Delete the newly added CSI Table instance" %step;
                print "EXPECTED RESULT %d: Should delete the newly added CSI Table instance successfully" %step;

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : New instance deleted successfully; Details : %s" %(step, details);
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    print "Added instance is deleted successfully";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : New instance NOT deleted successfully; Details : %s" %(step, details);
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    print "Added instance could not be deleted";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "INSTANCE VALUE : %s is not a valid value" %instance
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Unable to add a new instance to CSI Table; Details : %s" %(step, details);
            print "TEST EXECUTION RESULT : FAILURE";

        #Revert the pre-requisites set
        if revert_flag == 1:
            step = step + 1;
            status = RevertCSIPreReq(obj, initial_val);
            print "\nTEST STEP %d : Revert the pre-requisites set to initial values" %step;
            print "\nEXPECTED RESULT %d : Pre-requisites set should be reverted successfully" %step;

            if status == 1:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : Revert operation was success" %step;
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : Revert operation failed" %step;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "Revert operations not required";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "Pre-Requisites are not set successfully";

    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("tad");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
