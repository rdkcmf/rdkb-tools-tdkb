##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <version>2</version>
  <name>TS_LMLite_SetDscpCountEnableAndInterval_CheckDSCPCountPerInterval</name>
  <primitive_test_id/>
  <primitive_test_name>LMLiteStub_Set_Get</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the DSCP WAN values to "0,8,20,28" using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable and check if the DSCP traffic count per interval is getting populated with valid values in the interval set using Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_LMLite_29</test_case_id>
    <test_objective>To set the DSCP WAN values to "0,8,20,28" using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable and check if the DSCP traffic count per interval is getting populated with valid values in the interval set using Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable
paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
paramName/ParamName  : Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable
ParamValue : "0,8,20,28"
ParamType : string
parmName/ParamName : Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval
ParamValue : 100/110
ParamType : unsignedint
parmName : Device.X_RDK_WAN.Interface.1.Stats.DscpCountPerInterval</input_parameters>
    <automation_approch>1. Load the module
2. As pre-requisite, check if the DUT is in RBUS enabled mode. Also check if the Lan Mode is router, if not set to router and validate the set operation.
3. Get the initial DSCP enabled values for WAN traffic counts using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable and store it.
4. Get the initial DSCP count interval Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval and store it.
5. Set Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable to "0,8,20,28" and validate with get operation.
6. Set Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval to 100s or 110s and validate with get operation.
7. Sleep for the duration of Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval set.
8. After that query Device.X_RDK_WAN.Interface.1.Stats.DscpCountPerInterval and check if the traffic counts does not give an empty value.
9. Parse the traffic counts output and separate the DSCP records.
10.Check if the DSCP WAN value of each record is a valid value and is found in the DSCP enable string set.
11. For each of the DSCP WAN value, check if the number of client interfaces is greater than 0.
12. For each of the client interfaces check if the mac address, tx bytes and rx bytes are valid values.
13. Revert the Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable to initial value.
14. Revert Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval to initial value.
15. Revert the pre-requisites set if required.
16. Unload the module</automation_approch>
    <expected_output>Device.X_RDK_WAN.Interface.1.Stats.DscpCountPerInterval should update to non-empty when DSCP is enabled and DSCP Interval is set.</expected_output>
    <priority>High</priority>
    <test_stub_interface>lmlite</test_stub_interface>
    <test_script>TS_LMLite_SetDscpCountEnableAndInterval_CheckDSCPCountPerInterval</test_script>
    <skipped>No</skipped>
    <release_version>M104</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkutility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("lmlite","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_LMLite_SetDscpCountEnableAndInterval_CheckDSCPCountPerInterval');

#Get the result of connection with test component and DUT
loadmodulestatus1=obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Check the Pre-requisites for WAN Traffic Counts
    step = 1;
    pre_req_set, tdkTestObj, step, revert_flag, initial_lanmode = CheckWANTrafficCountsPre_requisite(obj, step);

    if pre_req_set == 1:
        print "\n*************RFC Pre-requisite set for the DUT*****************";

        #Get the initial DscpCountEnable and DscpCountInterval values
        step = step + 1;
        initial_values = [];
        get_flag = 0;
        paramList = ["Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable", "Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval"];
        print "\nTEST STEP %d : Get the initial DSCP Count Enable and DSCP Count Interval" %(step);
        print "EXPECTED RESULT %d : DSCP count enable and DSCP Count Interval should be retrieved successfully" %step;

        for param in paramList:
            tdkTestObj = obj.createTestStep("LMLiteStub_Get");
            tdkTestObj.addParameter("paramName",param);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult :
                initial_values.append(details);
                print "%s is retrieved successfully as : %s" %(param, details);
                tdkTestObj.setResultStatus("SUCCESS");
            else :
                get_flag = 1;
                print "%s is NOT retrieved successfully";
                tdkTestObj.setResultStatus("FAILURE");

        if get_flag == 0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d : The initial values are retrieved successfully" %step;
            print "TEST EXECUTION RESULT : SUCCESS";

            #Set DscpCountEnable to a comma separarted string of valid DSCP values in the range 0-63
            step = step + 1;
            dscpCountEnable_str = "0,8,20,28";
            print "\nTEST STEP %d : Set the DSCP Count Enable using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable to %s and validate the operation" %(step, dscpCountEnable_str);
            print "EXPECTED RESULT %d : DSCP count enable set validation should be success" %step;

            tdkTestObj = obj.createTestStep("LMLiteStub_Set_Get");
            tdkTestObj.addParameter("ParamName",paramList[0]);
            tdkTestObj.addParameter("ParamValue",dscpCountEnable_str);
            tdkTestObj.addParameter("ParamType","string");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : DSCP count enable set operation success; Details : %s" %(step, details);
                print "TEST EXECUTION RESULT : SUCCESS";

                #Set DscpCountInterval
                step = step + 1;
                interval_revert_flag = 0;

                if initial_values[1] == "100":
                    dscpCountInterval = "110";
                else:
                    dscpCountInterval = "100";

                print "\nTEST STEP %d : Set the DSCP Count Interval using Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval to %s and validate the operation" %(step, dscpCountInterval);
                print "EXPECTED RESULT %d : DSCP count interval set validation should be success" %step;

                tdkTestObj = obj.createTestStep("LMLiteStub_Set_Get");
                tdkTestObj.addParameter("ParamName",paramList[1]);
                tdkTestObj.addParameter("ParamValue",dscpCountInterval);
                tdkTestObj.addParameter("ParamType","unsignedint");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult :
                    interval_revert_flag = 1;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : DSCP count interval set operation success; Details : %s" %(step, details);
                    print "TEST EXECUTION RESULT : SUCCESS";

                    #Sleep for the DSCP Count Interval set + 5s for DSCP count to be populated
                    sleep_time = int(dscpCountInterval) + 5;
                    print "Sleeping the DSCP Count Interval set : %ss for WAN Traffic Counts to be updated" %sleep_time;
                    sleep(sleep_time);

                    #Check if the DSCP Count Per Interval is non-empty
                    step = step + 1;
                    print "\nTEST STEP %d : Get the DSCP Count Per Interval using Device.X_RDK_WAN.Interface.1.Stats.DscpCountPerInterval" %(step);
                    print "EXPECTED RESULT %d : DSCP count per interval should be retrieved successfully as non-empty" %step;

                    tdkTestObj = obj.createTestStep("LMLiteStub_Get");
                    tdkTestObj.addParameter("paramName","Device.X_RDK_WAN.Interface.1.Stats.DscpCountPerInterval");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : DSCP count per interval is retrieved as : %s" %(step, details);
                        print "TEST EXECUTION RESULT : SUCCESS";

                        #Separate the DSCP records
                        dscp_records = details.split(";");
                        #Number of DSCP records
                        num_dscp_records = len(dscp_records);

                        #Check if the data held in the DSCP count per intreval records are valid
                        step = step + 1;
                        record_flag = 0;
                        print "\nTEST STEP %d : Check if the value of Device.X_RDK_WAN.Interface.1.Stats.DscpCountPerInterval retrieved is valid" %step;
                        print "EXPECTED RESULT %d : Device.X_RDK_WAN.Interface.1.Stats.DscpCountPerInterval data retrieved should be valid" %step;

                        for record in range(0, num_dscp_records):
                            print "\n-----For DSCP record : %s-----" %dscp_records[record];
                            #DSCP WAN value of the record
                            dscp_wan = dscp_records[record].split("|")[0];
                            print "DSCP WAN value : %s" %dscp_wan;

                            #Check if DSCP WAN value is in the DSCP Enable list set
                            if dscp_wan.isdigit() and dscp_wan in dscpCountEnable_str:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "DSCP WAN value is valid";

                                #Get the DSCP client list
                                dscp_client_list = dscp_records[record].split("|");
                                #Remove the first element as it is the DSCP WAN value
                                dscp_client_list.remove(dscp_client_list[0]);
                                dscp_client_length = len(dscp_client_list);
                                print "Number of clients : %s" %dscp_client_length;

                                for client in range(0, dscp_client_length):
                                    print "--For Client %d--" %(client+1);
                                    #Separate the client details
                                    client_details = dscp_client_list[client].split(",");
                                    #Mac address of interface
                                    mac_addr = client_details[0];
                                    print "Mac address : %s" %mac_addr;
                                    #Tx Total
                                    tx_total = client_details[1];
                                    print "Tx Total : %s" %tx_total;
                                    #Rx Total
                                    rx_total = client_details[2];
                                    print "Rx Total : %s" %rx_total;

                                    if len(mac_addr) == 17 and 	tx_total.isdigit() and rx_total.isdigit():
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "Client details are valid";
                                    else:
                                        record_flag = 1;
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "Client details are NOT valid";
                            else:
                                record_flag = 1;
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "DSCP WAN value is NOT valid";
                        if record_flag == 0:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d : DSCP count per interval retrieved is valid" %(step);
                            print "TEST EXECUTION RESULT : SUCCESS";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d : DSCP count per interval retrieved is NOT valid" %(step);
                            print "TEST EXECUTION RESULT : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : DSCP count per interval is retrieved as : %s" %(step, details);
                        print "TEST EXECUTION RESULT : FAILURE";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : DSCP count interval set operation failed; Details : %s" %(step, details);
                    print "TEST EXECUTION RESULT : FAILURE";

                #Revert DscpCountEnable to initial value
                step = step + 1;
                print "\nTEST STEP %d : Revert the DSCP Count Enable using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable" %step;
                print "EXPECTED RESULT %d : DSCP count enable revert operation should be success" %step;

                tdkTestObj = obj.createTestStep("LMLiteStub_Set_Get");
                tdkTestObj.addParameter("ParamName","Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable");
                tdkTestObj.addParameter("ParamValue",initial_values[0]);
                tdkTestObj.addParameter("ParamType","string");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : DSCP count enable revert operation success; Details : %s" %(step, details);
                    print "TEST EXECUTION RESULT : SUCCESS";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : DSCP count enable revert operation failed; Details : %s" %(step, details);
                    print "TEST EXECUTION RESULT : FAILURE";

                #Revert DscpCountInterval to initial value
                if interval_revert_flag == 1:
                    step = step + 1;
                    print "\nTEST STEP %d : Revert the DSCP Count Interval using Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval" %step;
                    print "EXPECTED RESULT %d : DSCP count interval revert operation should be success" %step;

                    tdkTestObj = obj.createTestStep("LMLiteStub_Set_Get");
                    tdkTestObj.addParameter("ParamName","Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval");
                    tdkTestObj.addParameter("ParamValue",initial_values[1]);
                    tdkTestObj.addParameter("ParamType","unsignedint");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : DSCP count interval revert operation success; Details : %s" %(step, details);
                        print "TEST EXECUTION RESULT : SUCCESS";
                    else :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : DSCP count interval revert operation failed; Details : %s" %(step, details);
                        print "TEST EXECUTION RESULT : FAILURE";
                else:
                    "DSCP Interval revert operation not required";
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : DSCP count enable set operation failed; Details : %s" %(step, details);
                print "TEST EXECUTION RESULT : FAILURE";
        else :
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d : DSCP values NOT retrieved successfully" %step;
            print "TEST EXECUTION RESULT : FAILURE";

        #Revert the Pre-requisites for WAN Traffic Counts
        step = step + 1;
        status = RevertWANTrafficCountsPre_requisite(obj, step, revert_flag, initial_lanmode)

        if status == 1:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "Revert operations completed successfully";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "Revert operations NOT completed successfully";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "Pre-Requisite is not set successfully";

    obj.unloadModule("lmlite");
else:
    print "Failed to load lmlite module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
