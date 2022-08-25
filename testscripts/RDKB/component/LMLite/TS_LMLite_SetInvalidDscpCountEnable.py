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
  <version>7</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_LMLite_SetInvalidDscpCountEnable</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>LMLiteStub_Set_Get</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if setting DSCP Enabled to invalid values using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable returns failure.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_LMLite_31</test_case_id>
    <test_objective>To check if setting DSCP Enabled to invalid values using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable returns failure.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RBUS.Enable
paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
paramName  : Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable
paramValue : invalid values
Type : string
</input_parameters>
    <automation_approch>1. Load the module
2. As pre-requisite, check if the DUT is in RBUS enabled mode. Also check if the Lan Mode is router, if not set to router and validate the set operation.
3. Get the initial DSCP enabled values for WAN traffic counts using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable and store it.
4. Set Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable to invalid values such as : ["70", "0,64", "8,-10", "0,8,28,100", "150,200,250,300,350,400"] which are out of the acceptable range of 0-63 and check if the set is failure.
5. Revert Device.X_RDK_WAN.Interface.1.Stats.DscpCountInterval to initial value if required.
6. Revert the pre-requisites set if required.
7. Unload the module</automation_approch>
    <expected_output>DSCP Enabled to invalid values using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable should return failure.</expected_output>
    <priority>High</priority>
    <test_stub_interface>lmlite</test_stub_interface>
    <test_script>TS_LMLite_SetInvalidDscpCountEnable</test_script>
    <skipped>No</skipped>
    <release_version>M104</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
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
obj.configureTestCase(ip,port,'TS_LMLite_SetInvalidDscpCountEnable');

#Get the result of connection with test component and DUT
loadmodulestatus1=obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    #Check the Pre-requisites for WAN Traffic Counts
    step = 1;
    pre_req_set, tdkTestObj, step, revert_flag, initial_lanmode = CheckWANTrafficCountsPre_requisite(obj, step);

    if pre_req_set == 1:
        print "\n*************RFC Pre-requisite set for the DUT*****************";

        #Get the initial DscpCountEnable value
        step = step + 1;
        print "\nTEST STEP %d : Get the initial DSCP Count Enable using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable" %(step);
        print "EXPECTED RESULT %d : DSCP count enable should be retrieved successfully" %step;

        tdkTestObj = obj.createTestStep("LMLiteStub_Get");
        tdkTestObj.addParameter("paramName","Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        initial_dscp = tdkTestObj.getResultDetails();

        if expectedresult in actualresult :
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d : DSCP count enable retrieved successfully" %step;
            print "Initial DSCP Count Enable : %s" %initial_dscp;
            print "TEST EXECUTION RESULT : SUCCESS";

            #Set DscpCountEnable to invalid DSCP values
            flag = 0;
            invalid_vals = ["70", "0,64", "8,-10", "0,8,28,100", "150,200,250,300,350,400"];
            step = step + 1;
            print "\nTEST STEP %d : Set the DSCP Count Enable using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable to invalid DSCP values" %(step);
            print "EXPECTED RESULT %d : DSCP count enable set operation should fail for all invalid DSCP values" %step;

            for dscpCountEnable_str in invalid_vals:
                print "\nFor the invalid DSCP Enable string : %s" %dscpCountEnable_str;
                tdkTestObj = obj.createTestStep("LMLiteStub_Set");
                tdkTestObj.addParameter("ParamName","Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable");
                tdkTestObj.addParameter("ParamValue",dscpCountEnable_str);
                tdkTestObj.addParameter("Type","string");
                expectedresult="FAILURE";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "DSCP Enable set operation failed";
                else:
                    flag = 1;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "DSCP Enable set operation success";

            if flag == 0:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : DSCP count enable set operation failed for all invalid values" %step;
                print "TEST EXECUTION RESULT : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : DSCP count enable set operation did NOT fail for all invalid values" %step;
                print "TEST EXECUTION RESULT : FAILURE";

                #Revert DscpCountEnable to initial value
                step = step + 1;
                print "\nTEST STEP %d : Revert the DSCP Count Enable using Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable" %step;
                print "EXPECTED RESULT %d : DSCP count enable revert operation should be success" %step;

                tdkTestObj = obj.createTestStep("LMLiteStub_Set_Get");
                tdkTestObj.addParameter("ParamName","Device.X_RDK_WAN.Interface.1.Stats.DscpCountEnable");
                tdkTestObj.addParameter("ParamValue",initial_dscp);
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
        else :
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d : DSCP count enable NOT retrieved successfully" %step;
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
