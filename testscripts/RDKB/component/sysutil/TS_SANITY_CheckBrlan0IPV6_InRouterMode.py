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
  <version>12</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckBrlan0IPV6_InRouterMode</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Check if the brlan0 interface gets IPV6 address when the DUT is in router mode.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>20</execution_time>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_69</test_case_id>
    <test_objective>Check if the brlan0 interface gets IPV6 address when the DUT is in router mode.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
ParamValue : router/bridge-static
Type : string</input_parameters>
    <automation_approch>1. Load the modules
2. Check the current lan mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
3. If the lan mode is not initially router, set to router. Verify with get operation
4. Check if the brlan0 interface has the IPV6 address when DUT is in router mode
5. Revert to initial lan mode if required
6. Unload the modules.</automation_approch>
    <expected_output>brlan0 interface should get IPV6 address when the DUT is in router mode.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckBrlan0IPV6_InRouterMode</test_script>
    <skipped>No</skipped>
    <release_version>M102</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
def getLanMode(tdkTestObj):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    lanmode = tdkTestObj.getResultDetails().strip();
    return actualresult, lanmode;

def setLanMode(tdkTestObj, setValue):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode");
    tdkTestObj.addParameter("ParamValue",setValue);
    tdkTestObj.addParameter("Type","string");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    sleep(120);
    return actualresult, details;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_CheckBrlan0IPV6_InRouterMode');
pamObj.configureTestCase(ip,port,'TS_SANITY_CheckBrlan0IPV6_InRouterMode');

#Get the result of connection with test component and STB
loadmodulestatus1 =sysObj.getLoadModuleResult();
loadmodulestatus2 =pamObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and loadmodulestatus2.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    pamObj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Get the lan mode
    step = 1;
    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    actualresult, lanmodeInitial = getLanMode(tdkTestObj);

    print "\nTEST STEP %d: Get the initial Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
    print "EXPECTED RESULT %d: Should get the initial Lan Mode successfully" %step;

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: GET operation success; Lanmode is : %s" %(step, lanmodeInitial);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Set lan mode to router if not already in router mode
        router_flag = 0;
        revert_flag = 0;
        if lanmodeInitial == "bridge-static":
            setValue = "router";

            #Change the Lan Mode
            step = step + 1;
            tdkTestObj = pamObj.createTestStep('pam_Setparams');
            actualresult, details = setLanMode(tdkTestObj, setValue);

            print "\nTEST STEP %d: Transition the lanmode to %s using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %(step, setValue);
            print "EXPECTED RESULT %d: Should set the Lan Mode to %s successfully" %(step, setValue);

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Lan Mode set successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the Lan Mode is set properly
                sleep(20);
                step = step + 1;
                tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
                actualresult, currLanMode = getLanMode(tdkTestObj)

                print "\nTEST STEP %d: Get the current Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
                print "EXPECTED RESULT %d: Should get the current Lan Mode as %s" %(step, setValue);

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: GET operation success; Lanmode is : %s" %(step, currLanMode);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if currLanMode == setValue :
                        router_flag = 1;
                        revert_flag = 1;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "SET reflects in GET";
                    else :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "SET does NOT reflect in GET";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: GET operation failed; Lanmode is : %s" %(step, currLanMode);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Lan Mode not set successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else :
            print "Lan Mode is router, SET operation not required";
            router_flag = 1;

        if router_flag == 1:
            #Check if brlan0 gets IPV6
            step = step + 1;
            tdkTestObj = sysObj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", "ifconfig brlan0 | grep \"inet6 addr\" | grep \"Scope:Global\" | cut -f1 -d '/' | tr \"\n\" \" \"");
            expectedresult="SUCCESS";
            #Execute the test case in DUT
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip();

            print "\nTEST STEP %d : Check if brlan0 interface gets IPV6 when the DUT is in router mode" %step;
            print "EXPECTED RESULT %d : brlan0 interface should get IPV6 when the DUT is in router mode" %step;

            if expectedresult in actualresult and "inet6 addr: " in details:
                wanipv6 = details.split("inet6 addr: ")[1];
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: brlan0 interface gets IPV6 : %s" %(step, wanipv6);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: brlan0 interface does NOT get IPV6; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else :
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "Cannot proceed with the next steps as DUT is not set to router mode...";

        #Revert operation
        if revert_flag == 1:
            setValue = lanmodeInitial
            tdkTestObj = pamObj.createTestStep('pam_Setparams');
            actualresult, details = setLanMode(tdkTestObj, setValue);

            print "\nTEST STEP %d: Revert the lanmode to %s using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %(step, setValue);
            print "EXPECTED RESULT %d: Should revert the Lan Mode to %s successfully" %(step, setValue);

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
        else:
            print "Reverting Lan Mode not required";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: GET operation failed; Lanmode is : %s" %(step, lanmodeInitial);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
    pamObj.unloadModule("pam");
else:
    print "Failed to load sysutil module";
    sysObj.setLoadModuleStatus("FAILURE");
    pamObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
