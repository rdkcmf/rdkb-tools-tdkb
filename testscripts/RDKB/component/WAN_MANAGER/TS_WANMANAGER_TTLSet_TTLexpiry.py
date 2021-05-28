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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>5</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WANMANAGER_TTLSet_TTLexpiry</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Verify whether Override TTL value is changed to zero after the last set Override TTL time period expires</synopsis>
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
    <test_case_id>TC_WANMANAGER_37</test_case_id>
    <test_objective>Verify whether Override TTL value is changed to zero after the last set Override TTL time period expires    </test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled
</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL : 300</input_parameters>
    <automation_approch>1. Get the DSL Diagnostic Reporting parameters.
2. Set override TTL to 300..
3. Sleep for 300s and and check if at the end of 300s, override TTL expires to 0.
4. Revert the Reporting parameters to initial values if required.</automation_approch>
    <expected_output>The override TTL must decrement from the value set and should expire to 0 once the time set in seconds is exhausted.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_DSL_TTLSet_TTLexpiry</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;
from WanManager_Utility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_TTLSet_TTLexpiry');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")

    expectedresult="SUCCESS";
    #DSL connection can be enabled or disabled
    step = 1;

    #Get the initial values of "Device.DSL.X_RDK_Report.DSL.Enabled", "Device.DSL.X_RDK_Report.DSL.ReportingPeriod", "Device.DSL.X_RDK_Report.DSL.Default.ReportingPeriod", "Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL"
    tdkTestObj,initial_value,status = getReportingParams(obj, step);

    #If the initial values are retrieved successfully
    if status == 0:
        #Set override TTL to supported value
        step = step + 1;
        override_TTL = "300";
        tdkTestObj = obj.createTestStep('TADstub_Set');
        tdkTestObj.addParameter("ParamName","Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL")
        tdkTestObj.addParameter("ParamValue",override_TTL);
        tdkTestObj.addParameter("Type","unsignedint");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "TEST STEP %d : Set Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL to supported value : %s" %(step, override_TTL);
        print "EXPECTED RESULT %d : Set operation should be success" %step;

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: %s" %(step, details);
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #sleep for the duration of override TTL
            print "Sleeping for the duation of 300s";
            sleep(300);

            #check if override TTL is zero after the expiry time
            step = step + 1;
            tdkTestObj = obj.createTestStep('TADstub_Get');
            tdkTestObj.addParameter("paramName","Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            print "TEST STEP %d : Check if Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL is 0 after the expiry time" %step;
            print "EXPECTED RESULT %d : Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL should be 0" %step;

            if expectedresult in actualresult :
                value = int(details);
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL is :%d" %(step, value);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                if value == 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Override TTL is 0 after expiry time";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Override TTL is not 0 after expiry time";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL is not fetched successfully" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert back to the initial override TTL only when it has non-zero value initially
            if int(initial_value[3]) != 0:
                step = step + 1;
                tdkTestObj = obj.createTestStep('TADstub_Set');
                tdkTestObj.addParameter("ParamName","Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL")
                tdkTestObj.addParameter("ParamValue", initial_value[3]);
                tdkTestObj.addParameter("Type","unsignedint");
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                print "TEST STEP %d : Revert Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL to : %s" %(step, initial_value[3]);
                print "EXPECTED RESULT %d : Revert operation should be success" %step;

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: %s" %(step, details);
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: %s" %(step, details);
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                print "Revert operation is not required";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: %s" %(step, details);
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        print "Reporting parameters are not retrieved successfully";
    obj.unloadModule("tad");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

