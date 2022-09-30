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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>8</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckBrlan0SelfHeal</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if SelfHeal brings up brlan0 interface within 15mins of bringing down the interface given that the DUT is in router mode and Self Heal is enabled.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>25</execution_time>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SANITY_77</test_case_id>
    <test_objective>To check if SelfHeal brings up brlan0 interface within 15mins of bringing down the interface given that the DUT is in router mode and Self Heal is enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
ParamValue : router/bridge-static
Type : string
ParamName : Device.SelfHeal.X_RDKCENTRAL-COM_Enable
ParamValue : true/false
Type : boolean</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial lan mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode.
3. If the initial lan mode is not router, set it to router and validate with get.
4. Get the initial Self Heal enable state using Device.SelfHeal.X_RDKCENTRAL-COM_Enable
5. If Self Heal is not already enabled, set to true and validate with get.
6. Get the initial brlan0 interface IP and check if it is valid.
7. Get the brlan0 interface status - UP or DOWN.
8. If the interface is UP, bring it to DOWN and validate the status.
9. Check if brlan0 status changes to UP within a duration of 15mins in 60s iterations.
10. Revert the Self Heal enable value if required.
11. Revert the lan mode if required.
12. Unload the modules.</automation_approch>
    <expected_output>SelfHeal should bring up brlan0 interface within 15mins of bringing down the interface given that the DUT is in router mode and Self Heal is enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckBrlan0SelfHeal</test_script>
    <skipped>No</skipped>
    <release_version>M105</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckBrlan0SelfHeal');
sysobj.configureTestCase(ip,port,'TS_SANITY_CheckBrlan0SelfHeal');

#Get the result of connection with test component and DUT
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =sysobj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Get the Lan Mode
    step = 1;
    lan_param = "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode";
    print "\nTEST STEP %d: Get the initial Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
    print "EXPECTED RESULT %d: Should get the initial Lan Mode successfully" %step;

    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
    actualresult, lanmodeInitial = getTR181Value(tdkTestObj, lan_param);

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: GET operation success; Lanmode is : %s" %(step, lanmodeInitial);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #If the Lan Mode is not router, set to router
        proceed_flag = 0;
        revert_lan = 0;
        if lanmodeInitial != "router" :
            step = step + 1;
            setValue = "router";
            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
            actualresult, details = setTR181Value(tdkTestObj, lan_param, setValue, "string");

            print "\nTEST STEP %d: Transition the lanmode to %s using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %(step, setValue);
            print "EXPECTED RESULT %d: Should set the Lan Mode to %s successfully" %(step, setValue);

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Lan Mode set successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the Lan Mode is set properly
                sleep(120);
                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                actualresult, currLanMode = getTR181Value(tdkTestObj, lan_param);

                print "\nTEST STEP %d: Get the current Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
                print "EXPECTED RESULT %d: Should get the current Lan Mode as %s" %(step, setValue);

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: GET operation success; Lanmode is : %s" %(step, currLanMode);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if currLanMode == setValue :
                        revert_lan = 1;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "SET reflects in GET";
                    else :
                        proceed_flag = 1;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "SET does not reflect in GET";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: GET operation failed; Details  : %s" %(step, currLanMode);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Lan Mode not set successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "Lan Mode is initially router, SET operation not required";

        #Check if Device.SelfHeal.X_RDKCENTRAL-COM_Enable is enabled
        if proceed_flag == 0 :
            step = step + 1;
            selfheal_param = "Device.SelfHeal.X_RDKCENTRAL-COM_Enable";
            print "\nTEST STEP %d: Get the initial value of  Device.SelfHeal.X_RDKCENTRAL-COM_Enable" %step;
            print "EXPECTED RESULT %d: Device.SelfHeal.X_RDKCENTRAL-COM_Enable should be retrieved successfully" %step;

            tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
            actualresult, selfhealInitial = getTR181Value(tdkTestObj, selfheal_param);

            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : Self Heal enable retrieved as : %s" %(step, selfhealInitial);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Enable SelfHeal if it is disabled initially
                revert_selfheal = 0;
                if selfhealInitial == "false":
                    step = step + 1;
                    print "\nTEST STEP %d: Enable Device.SelfHeal.X_RDKCENTRAL-COM_Enable" %step;
                    print "EXPECTED RESULT %d: Should enable Device.SelfHeal.X_RDKCENTRAL-COM_Enable successfully" %step;

                    tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                    actualresult, details = setTR181Value(tdkTestObj, selfheal_param, "true", "boolean");

                    if expectedresult in actualresult :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : Self Heal enabled successfully; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Validate with GET
                        step = step + 1;
                        print "\nTEST STEP %d: Get the current value of  Device.SelfHeal.X_RDKCENTRAL-COM_Enable" %step;
                        print "EXPECTED RESULT %d: Current Device.SelfHeal.X_RDKCENTRAL-COM_Enable should be retrieved successfully" %step;

                        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                        actualresult, selfhealFinal = getTR181Value(tdkTestObj, selfheal_param);

                        if expectedresult in actualresult :
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d : Current Self Heal enable retrieved as : %s" %(step, selfhealFinal);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            if selfhealFinal == "true":
                                revert_selfheal = 1;
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "SET reflects in GET";
                            else :
                                proceed_flag = 1;
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "SET does not reflect in GET";
                        else :
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d : Current Self Heal enable NOT retrieved; Details : %s" %(step, selfhealFinal);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : Self Heal NOT enabled successfully; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "Self Heal already enabled, SET operation not required";

                #Check if brlan0 is getting IP
                if proceed_flag == 0:
                    step = step + 1;
                    print "\nTEST STEP %d : Verify whether brlan0 is assigned properly with valid DHCPv4 address" %step;
                    print "EXPECTED RESULT %d : brlan0 IP should be valid" %step;

                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                    tdkTestObj.addParameter("command", "ifconfig brlan0 | grep \"inet addr\" | cut -f2 -d ':' | cut -f1 -d ' '");
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    ip = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    if expectedresult in actualresult and ip != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: brlan0 is up with IP %s" %(step, ip);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Check if brlan0 Interface is UP or DOWN
                        step = step + 1;
                        print "\nTEST STEP %d : Check whether brlan0 interface is UP or DOWN" %step;
                        print "EXPECTED RESULT %d : brlan0 interface should be UP or DOWN" %step;

                        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                        tdkTestObj.addParameter("command", "/sbin/ip a show brlan0 | grep -m1 \"brlan0\" | cut -f9 -d ' '");
                        #Execute the test case in DUT
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        status = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                        if expectedresult in actualresult and status != "":
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: brlan0 interface status is : %s" %(step, status);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #If status is UP, bring it DOWN
                            if status == "UP":
                                step = step + 1;
                                print "\nTEST STEP %d : Bring down the brlan0 interface using \"ifconfig brlan0 down\"" %step;
                                print "EXPECTED RESULT %d : brlan0 interface should be brought down" %step;

                                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                                tdkTestObj.addParameter("command", "ifconfig brlan0 down");
                                #Execute the test case in DUT
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                                if expectedresult in actualresult and details == "":
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: Command to bring down brlan0 interface was executed successfully" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

                                    #Verify if the Interface is down
                                    step = step + 1;
                                    print "\nTEST STEP %d : Verify whether brlan0 interface is DOWN" %step;
                                    print "EXPECTED RESULT %d : brlan0 interface should be DOWN" %step;

                                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                                    tdkTestObj.addParameter("command", "/sbin/ip a show brlan0 | grep -m1 \"brlan0\" | cut -f9 -d ' '");
                                    #Execute the test case in DUT
                                    tdkTestObj.executeTestCase(expectedresult);
                                    actualresult = tdkTestObj.getResult();
                                    status = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                                    if expectedresult in actualresult and status == "DOWN":
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT %d: brlan0 interface status is DOWN" %step;
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS";
                                    else:
                                        proceed_flag = 1;
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT %d: brlan0 interface status is NOT DOWN" %step;
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE";
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: Command to bring down brlan0 interface was NOT executed successfully" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                print "Status is already DOWN, need not bring down again";

                            #Wait for a duration of 15mins for 60s iterations for brlan0 interface to come UP again
                            if proceed_flag == 0:
                                step = step + 1;
                                statusUp = 0;
                                print "\nTEST STEP %d : Check if SelfHeal brings up brlan0 interface within 15mins" %step;
                                print "EXPECTED RESULT %d : SelfHeal should bring up brlan0 interface within 15mins" %step;

                                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                                tdkTestObj.addParameter("command", "/sbin/ip a show brlan0 | grep -m1 \"brlan0\" | cut -f9 -d ' '");

                                #Checking every 60s for 15 mins
                                for sub_iteration in range(1,17):
                                    print "Waiting for brlan0 to be brought up by SelfHeal....\nIteration : %d" %sub_iteration;
                                    tdkTestObj.executeTestCase(expectedresult);
                                    actualresult = tdkTestObj.getResult();
                                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                                    if expectedresult in actualresult and "UP" in details:
                                        statusUp = 1;
                                        break;
                                    else:
                                        sleep(60);
                                        continue;

                                if statusUp == 1:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: brlan0 interface is successfully brought up by SelfHeal" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: brlan0 interface is NOT successfully brought up by SelfHeal" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "Unable to bring down brlan0, cannot proceed....";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: brlan0 interface status is : %s" %(step, status);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: brlan0 does not have IP" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";

                    #Revert Self Heal enable
                    if revert_selfheal == 1:
                        step = step + 1;
                        print "\nTEST STEP %d: Revert Device.SelfHeal.X_RDKCENTRAL-COM_Enable" %step;
                        print "EXPECTED RESULT %d: Should revert Device.SelfHeal.X_RDKCENTRAL-COM_Enable successfully" %step;

                        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                        actualresult, details = setTR181Value(tdkTestObj, selfheal_param, "false", "boolean");

                        if expectedresult in actualresult :
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d : Self Heal reverted successfully; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else :
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d : Self Heal NOT reverted successfully; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        print "Self Heal enable revert operation not required";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Unable to enable SelfHeal, cannot proceed...";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : Self Heal enable retrieved as : %s" %(step, selfhealInitial);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert Lan Mode
            if revert_lan == 1:
                step = step + 1;
                setValue = "bridge-static";
                print "\nTEST STEP %d: Revert the lanmode to %s using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %(step, setValue);
                print "EXPECTED RESULT %d: Should revert the Lan Mode to %s successfully" %(step, setValue);

                tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                actualresult, details = setTR181Value(tdkTestObj, lan_param, setValue, "string");

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Lan Mode reverted successfully; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Lan Mode NOT reverted successfully; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else :
                print "Lan Mode revert operation not required";
        else :
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "Unable to set the Lan Mode to router, cannot proceed...";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: GET operation failed; Lanmode is : %s" %(step, lanmodeInitial);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
