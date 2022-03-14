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
  <version>3</version>
  <name>TS_WIFIAGENT_CheckCSINumberOfEntries_OnAddAndDeleteTable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_AddObject</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if adding a new CSI Table instance increments the CSINumberOfEntries parameter Device.WiFi.X_RDK_CSINumberOfEntries and deleting the added CSI Table instance decrements the Device.WiFi.X_RDK_CSINumberOfEntries to initial value.</synopsis>
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
    <test_case_id>TC_WIFIAGENT_172</test_case_id>
    <test_objective>To check if adding a new CSI Table instance increments the CSINumberOfEntries parameter Device.WiFi.X_RDK_CSINumberOfEntries and deleting the added CSI Table instance decrements the Device.WiFi.X_RDK_CSINumberOfEntries to initial value.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Device should be in RBUS mode</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.X_RDK_CSI.
paramName : Device.WiFi.X_RDK_CSI.[i].
paramName : Device.WiFi.X_RDK_CSINumberOfEntries</input_parameters>
    <automation_approch>1. Load the modules
2. Check the pre-requisites : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable - true, Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable - false and Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable - true. If the Mesh enable or Band Steering enable have different values, set them to true and false respectively provided the DUT is initially in RBUS mode. Else return failure.
3. Get the initial number of CSI entries using Device.WiFi.X_RDK_CSINumberOfEntries
4. Add a new instance to the CSI data table using Device.WiFi.X_RDK_CSI.
5. Check if a valid instance number is returned.
6. Get the current value of Device.WiFi.X_RDK_CSINumberOfEntries. Check whether it gets incremented by 1.
7. Delete the newly added CSI table instance Device.WiFi.X_RDK_CSI.[i].
8. Check if Device.WiFi.X_RDK_CSINumberOfEntries it gets decremented by 1 and has the initial value.
9. Revert to initial state if required
10. Unload the modules.</automation_approch>
    <expected_output>Device.WiFi.X_RDK_CSINumberOfEntries should get incremented  by 1 when a new CSI table instance is added and should be decremented by 1 when an instance is deleted.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckCSINumberOfEntries_OnAddAndDeleteTable</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckCSINumberOfEntries_OnAddAndDeleteTable');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_CheckCSINumberOfEntries_OnAddAndDeleteTable');

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

        #Get the initial CSINumberOfEntries
        step = step + 1;
        tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Get");
        csi_entries_param = "Device.WiFi.X_RDK_CSINumberOfEntries";
        actualresult, initial_entries = getTR181Value(tdkTestObj, csi_entries_param);

        print "\nTEST STEP %d: Get the initial value of Device.WiFi.X_RDK_CSINumberOfEntries" %step;
        print "EXPECTED RESULT %d: Should get the value of Device.WiFi.X_RDK_CSINumberOfEntries successfully" %step;

        if expectedresult in actualresult and initial_entries.isdigit():
            initial_entries = int(initial_entries);
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Initial CSI Number of Entries retrieved; Details : %d" %(step, initial_entries);
            print "TEST EXECUTION RESULT : %s" %actualresult;

            #Add a new CSI Object
            step = step + 1;
            tdkTestObj = obj.createTestStep("TDKB_TR181Stub_AddObject");
            paramName = "Device.WiFi.X_RDK_CSI.";
            tdkTestObj.addParameter("paramName",paramName);
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

                    #Check CSINumberOfEntries after adding a new CSI instance
                    step = step + 1;
                    tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Get");
                    actualresult, current_entries = getTR181Value(tdkTestObj, csi_entries_param);

                    print "\nTEST STEP %d: Get the current value of Device.WiFi.X_RDK_CSINumberOfEntries" %step;
                    print "EXPECTED RESULT %d: Should get the value of Device.WiFi.X_RDK_CSINumberOfEntries successfully" %step;

                    if expectedresult in actualresult and current_entries.isdigit():
                        current_entries = int(current_entries);
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Current CSI Number of Entries retrieved; Details : %d" %(step, current_entries);
                        print "TEST EXECUTION RESULT : SUCCESS";

                        #Check if CSINumberOfEntries is incremented by 1
                        step = step + 1;
                        print "\nTEST STEP %d: Check if the current Device.WiFi.X_RDK_CSINumberOfEntries is incremented by 1" %step;
                        print "EXPECTED RESULT %d: Should get the value of Device.WiFi.X_RDK_CSINumberOfEntries incremented by 1" %step;
                        print "Initial CSI Number of Entries : %d" %initial_entries;
                        print "Current CSI Number of Entries : %d" %current_entries;

                        if current_entries == (initial_entries + 1):
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Current CSI Number of Entries retrieved is incremented by 1" %step;
                            print "TEST EXECUTION RESULT : SUCCESS";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Current CSI Number of Entries retrieved is NOT incremented by 1" %step;
                            print "TEST EXECUTION RESULT : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Current CSI Number of Entries not retrieved successfully; Details : %s" %(step, current_entries);
                        print "TEST EXECUTION RESULT : FAILURE";

                    #Delete the added instance from the CSI Table
                    step = step + 1;
                    tdkTestObj = obj.createTestStep("TDKB_TR181Stub_DelObject");
                    paramName = "Device.WiFi.X_RDK_CSI." + instance + ".";
                    tdkTestObj.addParameter("paramName",paramName);
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

                        #Get the final CSINumberOfEntries
                        step = step + 1;
                        tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Get");
                        actualresult, final_entries = getTR181Value(tdkTestObj, csi_entries_param);

                        print "\nTEST STEP %d: Get the final value of Device.WiFi.X_RDK_CSINumberOfEntries" %step;
                        print "EXPECTED RESULT %d: Should get the value of Device.WiFi.X_RDK_CSINumberOfEntries successfully" %step;

                        if expectedresult in actualresult and final_entries.isdigit():
                            final_entries = int(final_entries);
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Current CSI Number of Entries retrieved; Details : %d" %(step, final_entries);
                            print "TEST EXECUTION RESULT : SUCCESS";

                            #Check if CSINumberOfEntries is decremented by 1
                            step = step + 1;
                            print "\nTEST STEP %d: Check if the final Device.WiFi.X_RDK_CSINumberOfEntries is decremented by 1 and same as initial CSINumberOfEntries" %step;
                            print "EXPECTED RESULT %d: Should get the value of Device.WiFi.X_RDK_CSINumberOfEntries decremented by 1 and same as initial CSINumberOfEntries" %step;
                            print "Initial CSI Number of Entries : %d" %initial_entries;
                            print "Final CSI Number of Entries : %d" %final_entries;

                            if final_entries == (current_entries - 1) and final_entries == initial_entries:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: Final CSI Number of Entries retrieved is decremented by 1 and same as initial CSINumberOfEntries" %step;
                                print "TEST EXECUTION RESULT : SUCCESS";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: Final CSI Number of Entries retrieved is NOT decremented by 1 or same as initial CSINumberOfEntries" %step;
                                print "TEST EXECUTION RESULT : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Current CSI Number of Entries not retrieved successfully; Details : %s" %(step, final_entries);
                            print "TEST EXECUTION RESULT : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : New instance NOT deleted successfully; Details : %s" %(step, details);
                        print "[TEST EXECUTION RESULT] : %s" %actualresult;
                        print "Added instance could not be deleted";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "INSTANCE VALUE : %s is not a valid value" %instance;
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Unable to add a new instance to CSI Table; Details : %s" %(step, details);
                print "TEST EXECUTION RESULT : %s" %actualresult;
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Initial CSI Number of Entries NOT retrieved; Details : %s" %(step, initial_entries);
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
