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
  <version>7</version>
  <name>TS_WIFIAGENT_5GHzClientStartStopCSIDataCollection</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_AddObject</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Enable a CSI session with a 5GHz connected client using wifi_events_consumer process after enabling the CSI enable and setting ClientMAC value for new CSI table instance created. Kill the wifi_events_consumer process after 10s and check if the logs "WiFi_CSI_SubscriptionStarted" and "WiFi_CSI_SubscriptionCancelled" is found under /rdklogs/logs/WiFilog.txt.0 on starting and cancelling the CSI data collection respectively.</synopsis>
  <groups_id/>
  <execution_time>3</execution_time>
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
    <test_case_id>TC_WIFIAGENT_175</test_case_id>
    <test_objective>Enable a CSI session with a 5GHz connected client using wifi_events_consumer process after enabling the CSI enable and setting ClientMAC value for new CSI table instance created. Kill the wifi_events_consumer process after 10s and check if the logs "WiFi_CSI_SubscriptionStarted" and "WiFi_CSI_SubscriptionCancelled" is found under /rdklogs/logs/WiFilog.txt.0 on starting and cancelling the CSI data collection respectively.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Device should be in RBUS mode
4. A client should be connected to 5G</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.X_RDK_CSI.
paramName : Device.WiFi.X_RDK_CSI.[i].
paramName : Device.WiFi.X_RDK_CSI.[i].Enable
paramName : Device.WiFi.X_RDK_CSI.[i].ClientMacList
paramName : Device.Hosts.HostNumberOfEntries
paramName : Device.Hosts.Host.[j].Active
paramName : Device.Hosts.Host.[i].PhysAddress</input_parameters>
    <automation_approch>1. Load the modules
2. Check the pre-requisites : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable - true, Device.WiFi.X_RDKCENTRAL-COM_BandSteering.Enable - false and Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable - true. If the Mesh enable or Band Steering enable have different values, set them to true and false respectively provided the DUT is initially in RBUS mode. Else return failure.
3. Retrieve the MAC address of the connected client using Device.Hosts.Host.[i].PhysAddress if the host is active.
4. Add a new CSI table instance using Device.WiFi.X_RDK_CSI.
5. Set the Device.WiFi.X_RDK_CSI.[i].Enable to true and Device.WiFi.X_RDK_CSI.[i].ClientMacList to the connected client MAC for the newly added instance.
6. Get the enable status and the ClientMacList of the instance to cross check if SET is reflected in GET.
7. Capture the number of initial log lines of "WiFi_CSI_SubscriptionStarted" and "WiFi_CSI_SubscriptionCancelled" from /rdklogs/logs/WiFilog.txt.0
8. Start the CSI data collection for the connected client using the command "wifi_events_consumer -e 7" and wait for 10 seconds.
9. Kill the wifi_events_consumer process.
10. Check the final log line count of "WiFi_CSI_SubscriptionStarted" and "WiFi_CSI_SubscriptionCancelled" from /rdklogs/logs/WiFilog.txt.0
11. Check if the final log line count for both Subscription and Cancellation is incremented by 1.
12. Delete the newly added instance.
13. Revert to initial state if required.
14. Unload the modules.</automation_approch>
    <expected_output>CSI data collection should be subscribed and cancelled for the connected client successfully by starting and killing the wifi_events_consumer process and the required logs "WiFi_CSI_SubscriptionStarted" and "WiFi_CSI_SubscriptionCancelled" respectively should be found under /rdklogs/logs/WiFilog.txt.0.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_5GHzClientStartStopCSIDataCollection</test_script>
    <skipped>No</skipped>
    <release_version>M99</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def StartStopCSI(sysobj, step):
    #Get the WiFi_CSI_SubscriptionStarted log line count
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    print "\nGet the initial number of log lines of \"WiFi_CSI_SubscriptionStarted\"";
    file = "/rdklogs/logs/WiFilog.txt.0";
    search_string_csistart = "WiFi_CSI_SubscriptionStarted"
    count_csistart_initial = getLogFileTotalLinesCount(tdkTestObj, file, search_string_csistart, step);

    #Get the WiFi_CSI_SubscriptionCancelled log line count
    print "\nGet the initial number of log lines of \"WiFi_CSI_SubscriptionCancelled\"";
    step = step + 1;
    search_string_csiend = "WiFi_CSI_SubscriptionCancelled"
    count_csiend_initial = getLogFileTotalLinesCount(tdkTestObj, file, search_string_csiend, step);

    #Start and cancel the CSI data collection within 10s
    step = step + 1;
    query="wifi_events_consumer -e 7 & sleep 10 & pkill wifi_events_consumer";
    print "query:%s" %query
    tdkTestObj.addParameter("command", query)
    tdkTestObj.executeTestCase("SUCCESS");
    actualresult = tdkTestObj.getResult();
    result = tdkTestObj.getResultDetails().strip("\\n");

    print "\nTEST STEP %d : Start the CSI data collection for the CSI sessions that are enabled with a valid client MAC and cancel the CSI data collection in 10s" %step;
    print "EXPECTED RESULT %d : Should start the CSI data collection for the CSI sessions that are enabled with a valid client MAC and cancel the CSI data collection in 10s " %step;

    if expectedresult in actualresult :
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: CSI data collection for the CSI sessions that are enabled with a valid client MAC is started successfully and cancelled the CSI data collection in 10s " %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Get the WiFi_CSI_SubscriptionStarted log line count
        print "\nGet the final number of log lines of \"WiFi_CSI_SubscriptionStarted\"";
        step = step + 1;
        count_csistart_final = getLogFileTotalLinesCount(tdkTestObj, file, search_string_csistart, step);

        #Get the WiFi_CSI_SubscriptionCancelled log line count
        print "\nGet the final number of log lines of \"WiFi_CSI_SubscriptionCancelled\"";
        step = step + 1;
        count_csiend_final = getLogFileTotalLinesCount(tdkTestObj, file, search_string_csiend, step);
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: CSI data collection for the CSI sessions that are enabled with a valid client MAC is not started" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return count_csistart_initial, count_csistart_final, count_csiend_initial, count_csiend_final, step;

def GetClientMAC(tr181_obj, step):
    #Get the Number of Hosts
    tdkTestObj = tr181_obj.createTestStep('TDKB_TR181Stub_Get');
    actualresult, NoOfHosts = getTR181Value(tdkTestObj, "Device.Hosts.HostNumberOfEntries");
    macaddressFound = 0;
    hostMacAddress = "";

    print "\nTEST STEP %d: Get the number of hosts" %step;
    print "EXPECTED RESULT %d: Should get the number of hosts" %step;

    if expectedresult in actualresult and int(NoOfHosts)>0:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Number of hosts :%s" %(step, NoOfHosts);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Find the active hosts amoung the listed Hosts. List will contains the ids of active hosts
        List=[];
        macaddressFound = 0;

        for i in range(1,int(NoOfHosts)+1):
            if int(macaddressFound) == 1:
                break;

            #Get the Active Clients from the Host table
            paramName = "Device.Hosts.Host." + str(i) + ".Active";
            actualresult, status = getTR181Value(tdkTestObj, paramName);

            if "true" in status:
                 List.extend(str(i));

                 step = step + 1;
                 print "\nTEST STEP %d: Get the active clients" %step;
                 print "EXPECTED RESULT %d: Should get the active clients" %step;

                 if expectedresult in actualresult:
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("SUCCESS");
                     print "ACTUAL RESULT %d: Active clients are obtained" %step;
                     print "Active client list : ", List;
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : SUCCESS";

                     for i in range(1,len(List)):
                         if int(macaddressFound) == 1:
                             break;

                         step = step + 1;
                         paramName = "Device.Hosts.Host." + str(i) + ".PhysAddress";
                         actualresult, hostMacAddress = getTR181Value(tdkTestObj, paramName);
                         print "\nTEST STEP %d: Get the MAC address of the Client" %step;
                         print "EXPECTED RESULT %d: Get the MAC address of the device" %step;

                         if expectedresult in actualresult:
                             macaddressFound = 1;
                             #Set the result status of execution
                             tdkTestObj.setResultStatus("SUCCESS");
                             print "ACTUAL RESULT %d: MAC address Found in host table: %s" %(step, hostMacAddress);
                             #Get the result of execution
                             print "[TEST EXECUTION RESULT] : SUCCESS";
                         else:
                             #Set the result status of execution
                             tdkTestObj.setResultStatus("FAILURE");
                             print "ACTUAL RESULT %d: MAC address NOT Found in host table: %s" %(step, hostMacAddress);
                             #Get the result of execution
                             print "[TEST EXECUTION RESULT] : FAILURE";
                 else:
                     #Set the result status of execution
                     tdkTestObj.setResultStatus("FAILURE");
                     print "ACTUAL RESULT %d: Active clients are NOT obtained" %step;
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                 continue;
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Number of hosts :%s" %(step, NoOfHosts);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return hostMacAddress, step;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *
from tdkutility import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
obj1 = tdklib.TDKScriptingLibrary("tad","RDKB");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHzClientStartStopCSIDataCollection');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_5GHzClientStartStopCSIDataCollection');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHzClientStartStopCSIDataCollection');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();
loadmodulestatus2=sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus2

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Check the pre-requisites; Band Steering should be Disabled, RBUS and Mesh should be enabled
    pre_req_set, tdkTestObj, step, revert_flag, initial_val = CheckPreReqForCSI(obj1, obj);

    if pre_req_set == 1:
        print "\n*************All pre-requisites set for the DUT*****************";
        #Get the connected client MAC Address
        step = step + 1;
        hostMacAddress, step = GetClientMAC(obj, step);

        if hostMacAddress != "" :
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

                    #Set values for the CSI Enable and ClientMaclist after instance is created
                    step = step + 1;
                    sleep(5);
                    enable_param = "Device.WiFi.X_RDK_CSI." + instance + ".Enable";
                    ClientMaclist_param = "Device.WiFi.X_RDK_CSI." + instance + ".ClientMaclist";
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

                                #Start CSI data collection, kill the process later and then check for the required subscription log lines
                                step = step + 1;
                                count_csistart_initial, count_csistart_final, count_csiend_initial, count_csiend_final, step = StartStopCSI(sysobj, step);
                                step = step + 1;

                                print "\nTEST STEP %d : Check if the CSI start data collection log - \"WiFi_CSI_SubscriptionStarted\" and stop CSI data collection log - \"WiFi_CSI_SubscriptionCancelled\" are populated under WiFilog.txt.0" %step;
                                print "EXPECTED RESULT %d : The CSI start - stop data collection logs should be present under the WiFilog.txt.0" %step;
                                print "Number of initial log lines of \"WiFi_CSI_SubscriptionStarted\" : ", count_csistart_initial;
                                print "Number of final log lines of \"WiFi_CSI_SubscriptionStarted\" : ", count_csistart_final;
                                print "Number of initial log lines of \"WiFi_CSI_SubscriptionCancelled\" : ", count_csiend_initial;
                                print "Number of final log lines of \"WiFi_CSI_SubscriptionCancelled\" : ", count_csiend_final;

                                if (count_csistart_final == (count_csistart_initial + 1)) and (count_csiend_final == (count_csiend_initial + 1)):
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d : The required subsription log lines are found in WiFilog.txt.0 on starting and cancelling CSI data collection" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d : The required subsription log lines are NOT found in WiFilog.txt.0 on starting and cancelling CSI data collection" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
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
        else :
            print "No active clients connected...";
            tdkTestObj.setResultStatus("FAILURE");

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
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
