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
  <version>8</version>
  <name>TS_WIFIAGENT_CheckCSIEntries_PersistenceOnReboot</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_AddObject</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if Device.WiFi.X_RDK_CSINumberOfEntries value is non-zero when CSI instances are added and if the value resets to 0 on reboot.</synopsis>
  <groups_id/>
  <execution_time>20</execution_time>
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
    <test_case_id>TC_WIFIAGENT_173</test_case_id>
    <test_objective>To check if Device.WiFi.X_RDK_CSINumberOfEntries value is non-zero when CSI instances are added and if the value resets to 0 on reboot.</test_objective>
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
4. If initial number of entries is greater than 0, copy the enable values and clientMAClist of each of the instances. Else if its is equal to 0, add a new CSI table instance.
5. If a new table instance is added, check if Device.WiFi.X_RDK_CSINumberOfEntries is incremented by 1.
6. Reboot the DUT.
7. Once the device comes up, check if Device.WiFi.X_RDK_CSINumberOfEntries is reset to 0.
8. Revert to initial state and restore the CSI table instances if required.
9. Unload the modules.
</automation_approch>
    <expected_output>Device.WiFi.X_RDK_CSINumberOfEntries should reset to 0 on device reboot.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckCSIEntries_PersistenceOnReboot</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckCSIEntries_PersistenceOnReboot');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_CheckCSIEntries_PersistenceOnReboot');

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

            #Store the initial CSI values if number of Entries > 0
            copy_csi = 0;
            reboot_ready = 0;
            if initial_entries > 0:
                copy_csi = 1;
                csi_values_enable = [];
                csi_values_maclist = [];
                step = step + 1;
                count = 0;
                print "\nTEST STEP %d: Get the initial CSI values and store them" %step;
                print "EXPECTED RESULT %d: Should get the initial CSI values and store them" %step;

                for entry in range(1, initial_entries + 1):
                    print "Storing initial CSI values of instance %d" %entry;
                    enable_param = "Device.WiFi.X_RDK_CSI." + str(entry) + ".Enable";
                    ClientMaclist_param = "Device.WiFi.X_RDK_CSI." + str(entry) + ".ClientMaclist";
                    tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Get");
                    actualresult1, details1 = getTR181Value(tdkTestObj, enable_param);
                    actualresult2, details2 = getTR181Value(tdkTestObj, ClientMaclist_param);

                    if expectedresult in actualresult1 and expectedresult in actualresult2:
                        tdkTestObj.setResultStatus("SUCCESS");
                        count = count + 1;
                        print "Entry %d : %s : %s and %s : %s" %(entry, enable_param, details1, ClientMaclist_param, details2);
                        csi_values_enable.append(details1);
                        csi_values_maclist.append(details2);
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Entry %d : %s : %s and %s : %s" %(entry, enable_param, details1, ClientMaclist_param, details2);

                if count == initial_entries:
                    reboot_ready = 1;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: All CSI initial values of instances retrieved" %step;
                    print "TEST EXECUTION RESULT : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: All CSI initial values of instances NOT retrieved" %step;
                    print "TEST EXECUTION RESULT : FAILURE";
            else:
                #Add a new CSI table instance
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
                                reboot_ready = 1;
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
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "INSTANCE VALUE : %s is not a valid value" %instance;
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Unable to add a new CSI Table instance successfully; Details : %s" %(step, details);
                    print "TEST EXECUTION RESULT : %s" %actualresult;

            #Reboot the DUT
            if reboot_ready == 1:
                print "****DUT is going for a reboot and will be up after 300 seconds*****";
                obj.initiateReboot();
                sleep(300);

                #Once DUT is up, check if the CSINumberOfEntries is 0
                step = step + 1;
                tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Get");
                actualresult, final_entries = getTR181Value(tdkTestObj, csi_entries_param);

                print "\nTEST STEP %d: Get the value of Device.WiFi.X_RDK_CSINumberOfEntries after reboot" %step;
                print "EXPECTED RESULT %d: Should get the value of Device.WiFi.X_RDK_CSINumberOfEntries successfully" %step;

                if expectedresult in actualresult and final_entries.isdigit():
                    final_entries = int(final_entries);
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: CSI Number of Entries retrieved; Details : %d" %(step, final_entries);
                    print "TEST EXECUTION RESULT : %s" %actualresult;

                    step = step + 1;
                    print "\nTEST STEP %d: Check if the current Device.WiFi.X_RDK_CSINumberOfEntries is 0" %step;
                    print "EXPECTED RESULT %d: Should get the value of Device.WiFi.X_RDK_CSINumberOfEntries as 0" %step;

                    if final_entries == 0:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: CSI Number of Entries retrieved is 0 after reboot" %step;
                        print "TEST EXECUTION RESULT : SUCCESS";

                        #Revert to initial state if required
                        if copy_csi == 1:
                            count = 0;
                            step = step + 1;
                            print "\nTEST STEP %d : Restore the CSI Table with initial values" %step;
                            print "EXPECTED RESULT %d : Should successfully restore the CSI Table with initial values" %step;

                            for entry in range(1, initial_entries + 1):
                                #Add a new CSI table instance
                                tdkTestObj = obj.createTestStep("TDKB_TR181Stub_AddObject");
                                paramName = "Device.WiFi.X_RDK_CSI.";
                                tdkTestObj.addParameter("paramName",paramName);
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();

                                if expectedresult in actualresult:
                                    tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Set");
                                    enable_param = "Device.WiFi.X_RDK_CSI." + str(entry) + ".Enable";
                                    ClientMaclist_param = "Device.WiFi.X_RDK_CSI." + str(entry) + ".ClientMaclist";
                                    actualresult1 ,details1 = setTR181Value(tdkTestObj,enable_param,csi_values_enable[entry-1],"boolean");
                                    actualresult2 ,details2 = setTR181Value(tdkTestObj,ClientMaclist_param,csi_values_maclist[entry-1],"string");

                                    if expectedresult in actualresult1 and expectedresult in actualresult2:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "Instance %d added successfully" %entry;
                                        count = count + 1;
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "Instance %d NOT added successfully" %entry;
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "Unable to add CSI row";
                        else:
                            print "Restoring CSI Table not required";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: CSI Number of Entries retrieved is NOT 0 after reboot" %step;
                        print "TEST EXECUTION RESULT : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: CSI Number of Entries retrieved; Details : %s" %(step, final_entries);
                    print "TEST EXECUTION RESULT : %s" %actualresult;
            else:
                print "Cannot Reboot the DUT as the previous steps failed";
                tdkTestObj.setResultStatus("FAILURE");
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
