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
  <name>TS_WANMANAGER_SetReportEnable_NonBool</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if setting non Boolean value for DSL report fails as expected.</synopsis>
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
    <test_case_id>TC_WANMANAGER_38</test_case_id>
    <test_objective>To check if setting non Boolean value for DSL report fails as expected.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled
</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DSL.X_RDK_Report.DSL.Enabled : invalid</input_parameters>
    <automation_approch>1. Get the DSL Diagnostic Reporting parameters.
2. Set Device.DSL.X_RDK_Report.DSL.Enabled to invalid. The set operation should fail.
3. Get the DSL Diagnostic Reporting parameters and verify that there are no change in values for any parameters.
4. Revert to initial values if required.</automation_approch>
    <expected_output>Setting non Boolean value for DSL report should fail as expected.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_SetReportEnable_NonBool</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from tdkutility import *
from WanManager_Utility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_SetReportEnable_NonBool');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_SetReportEnable_NonBool');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")

    #DSL can be enbled or disabled to test the scenario
    step = 1;
    #Get the initial values of "Device.DSL.X_RDK_Report.DSL.Enabled", "Device.DSL.X_RDK_Report.DSL.ReportingPeriod", "Device.DSL.X_RDK_Report.DSL.Default.ReportingPeriod", "Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL"
    tdkTestObj,initial_value,status = getReportingParams(obj, step);

    #If the initial values are retrieved successfully
    if status == 0:
        #Set Device.DSL.X_RDK_Report.DSL.Enabled to an non-bool value
        step = step + 1;
        tdkTestObj = obj.createTestStep('TADstub_Set');
        reporting_enable = "invalid";
        tdkTestObj.addParameter("ParamName","Device.DSL.X_RDK_Report.DSL.Enabled")
        tdkTestObj.addParameter("ParamValue",reporting_enable);
        tdkTestObj.addParameter("Type","boolean");
        expectedresult="FAILURE";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "TEST STEP %d : Set Device.DSL.X_RDK_Report.DSL.Enabled to a non-bool value %s" %(step, reporting_enable);
        print "EXPECTED RESULT %d : Should not set Device.DSL.X_RDK_Report.DSL.Enabled to a non-bool value" %step;

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: %s" %(step, details);
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        #Check if the values are set
        step = step + 1;
        tdkTestObj, set_value, status = getReportingParams(obj, step);
        step = step + 1;
        print "TEST STEP %d : Check if all reporting parameters retained their values after the invalid set" %step;
        print "EXPECTED RESULT %d : All reporting parameters should retain their values after the invalid set" %step;

        if (set_value[0] != str(initial_value[0])) or (set_value[1] != str(initial_value[1])) or (set_value[2] != str(initial_value[2])) or (set_value[3] != str(initial_value[3])):
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: All reporting parameters did not retain their values after invalid set" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

            print "\n************Revert operation required***************";
            expectedresult = "SUCCESS";
            step = step + 1;
            value_list = [];
            value_list = [initial_value[0], initial_value[1], initial_value[2], initial_value[3]]
            tdkTestObj1 = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
            set_status = setReportingParams(tdkTestObj2, expectedresult, value_list, step);

            if set_status == 0:
                print "Revert operation was successful";
            else :
                print "Revert operation was not successful";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: All reporting parameters retained their values after the invalid set" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        print "Reporting parameters are not retrieved successfully";
    obj.unloadModule("tad");
    obj1.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

