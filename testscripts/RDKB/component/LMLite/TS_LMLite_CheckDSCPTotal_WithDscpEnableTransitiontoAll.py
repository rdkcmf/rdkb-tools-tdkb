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
  <version>1</version>
  <name>TS_LMLite_CheckDSCPTotal_WithDscpEnableTransitiontoAll</name>
  <primitive_test_id/>
  <primitive_test_name>LMLiteStub_Set_Get</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the DSCP Total traffic counts is non-empty when the DSCP Enable is set to "-1" from "0,8,20,28" and DSCP Interval is set to "10s" from "100s".</synopsis>
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
    <test_case_id>TC_LMLite_30</test_case_id>
    <test_objective>To check if the DSCP Total traffic counts is non-empty when the DSCP Enable is set to "-1" from "0,8,20,28" and DSCP Interval is set to "10s" from "100s".</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable
paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
paramName/ParamName  : Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable
ParamValue : "0,8,20,28"/-1
ParamType : string
parmName/ParamName : Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval
ParamValue : 100/110/10
ParamType : unsignedint
parmName : Device.X_RDK_WAN.Interface.1.Stats.DscpCountTotal</input_parameters>
    <automation_approch>1. Load the module
2. As pre-requisite, check if the DUT is in RBUS enabled mode. Also check if the Lan Mode is router, if not set to router and validate the set operation.
3. Get the initial DSCP enabled values for WAN traffic counts using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable and store it.
4. Get the initial DSCP count interval Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval and store it.
5. Set Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable to "0,8,20,28" and validate with get operation.
6. Set Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval to 100s or 110s and validate with get operation.
7. Sleep for the duration of Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval set.
8. After that query Device.X_RDK_WAN.Interface.1.Stats.DscpCountPerInterval and check if the traffic counts does not give an empty value.
9. Set Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable to "-1" to enable all DSCP traffic counts and validate with get.
10. Set Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval to a smaller interval such as 10s and validate with get.
11. Query Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval soon after that without additional sleep time and ensure that it is non-empty.
12. Revert the Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable to initial value.
13. Revert Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval to initial value.
14. Revert the pre-requisites set if required.
15. Unload the module</automation_approch>
    <expected_output>Device.X_RDK_WAN.Interface.1.Stats.DscpCountTotal should remain non-empty when the DSCP enabled is transitioned to "-1" from a discrete set of values and the DSCP count interval is set to a smaller interval such as 10s from 100s.</expected_output>
    <priority>High</priority>
    <test_stub_interface>lmlite</test_stub_interface>
    <test_script>TS_LMLite_CheckDSCPTotal_WithDscpEnableTransitiontoAll</test_script>
    <skipped>No</skipped>
    <release_version>M104</release_version>
    <remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_LMLite_CheckDSCPTotal_WithDscpEnableTransitiontoAll');

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

                    #Sleep for the DSCP Count Interval set + 5s for DSCP Total to be populated
                    sleep_time = int(dscpCountInterval) + 5;
                    print "Sleeping the DSCP Count Interval set : %ss for WAN Traffic Counts to be updated" %sleep_time;
                    sleep(sleep_time);

                    #Check if the DSCP Count Total is non-empty
                    step = step + 1;
                    print "\nTEST STEP %d : Get the DSCP Count Total using Device.X_RDK_WAN.Interface.1.Stats.DscpCountTotal" %(step);
                    print "EXPECTED RESULT %d : DSCP count total should be retrieved successfully as non-empty" %step;

                    tdkTestObj = obj.createTestStep("LMLiteStub_Get");
                    tdkTestObj.addParameter("paramName","Device.X_RDK_WAN.Interface.1.Stats.DscpCountTotal");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : DSCP count total is retrieved as : %s" %(step, details);
                        print "TEST EXECUTION RESULT : SUCCESS";

                        #Now set the DSCP Enable to "-1" indicating all DSCP WAN values
                        step = step + 1;
                        dscpCountEnable_str = "-1";
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

                            #Set DSCP Interval to a smaller interval such as 10
                            step = step + 1;
                            dscpCountInterval = "10";

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
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d : DSCP count interval set operation success; Details : %s" %(step, details);
                                print "TEST EXECUTION RESULT : SUCCESS";

                                #Check the DSCP Total traffic counts and check if they are non-empty
                                step = step + 1;
                                print "\nTEST STEP %d : Get the DSCP Count Total using Device.X_RDK_WAN.Interface.1.Stats.DscpCountTotal" %(step);
                                print "EXPECTED RESULT %d : DSCP count total should be retrieved successfully as non-empty" %step;

                                tdkTestObj = obj.createTestStep("LMLiteStub_Get");
                                tdkTestObj.addParameter("paramName","Device.X_RDK_WAN.Interface.1.Stats.DscpCountTotal");
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();

                                if expectedresult in actualresult and details != "":
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d : DSCP count total is retrieved as : %s" %(step, details);
                                    print "TEST EXECUTION RESULT : SUCCESS";
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d : DSCP count total is retrieved as : %s" %(step, details);
                                    print "TEST EXECUTION RESULT : FAILURE";
                            else :
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d : DSCP count interval set operation failed; Details : %s" %(step, details);
                                print "TEST EXECUTION RESULT : FAILURE";
                        else :
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d : DSCP count enable set operation failed; Details : %s" %(step, details);
                            print "TEST EXECUTION RESULT : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : DSCP count total is retrieved as : %s" %(step, details);
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
