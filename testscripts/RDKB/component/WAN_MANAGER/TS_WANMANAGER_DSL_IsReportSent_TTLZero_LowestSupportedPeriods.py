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
  <version>2</version>
  <name>TS_WANMANAGER_DSL_IsReportSent_TTLZero_LowestSupportedPeriods</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Verify whether the report is send when the  Default Reporting Period and Reporting Period  is changed to lowest supported values with Override TTL as zero</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_WANMANAGER_31</test_case_id>
    <test_objective>Verify whether the report is send when the  Default Reporting Period and Reporting Period  is changed to lowest supported values with Override TTL as zero</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled
4.DSL connection must be enabled.</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DSL.X_RDK_Report.DSL.Enabled : True
Device.DSL.X_RDK_Report.DSL.ReportingPeriod : 1
Device.DSL.X_RDK_Report.DSL.Default.ReportingPeriod : 1
Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL : 0</input_parameters>
    <automation_approch>1. Get the DSL Diagnostic Reporting parameters.
2. If override TTL is not 0, reboot the device to reset it to 0.
3. Invoke the DSL reports pre-requisite function and set the reporting parameters to 0.
4.Set DSL Enable to true, Reporting period to 1, Default Reporting period to 1.
5. Sleep for 10s and check if the expected log line "Sent message successfully to parodus" in XDSLWANMANAGER.txt.0 is present. The number of DSL reports sent should be 10 in 10s.
6. Revert the Reporting parameters to initial values.</automation_approch>
    <expected_output>DSL Report should be sent when the  Default Reporting Period and Reporting Period  is changed to lowest supported values with Override TTL as zero.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_DSL_IsReportSent_TTLZero_LowestSupportedPeriods</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
#use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from tdkutility import *
from WanManager_Utility import *
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");
obj2 = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_DSL_IsReportSent_TTLZero_LowestSupportedPeriods');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_DSL_IsReportSent_TTLZero_LowestSupportedPeriods');
obj2.configureTestCase(ip,port,'TS_WANMANAGER_DSL_IsReportSent_TTLZero_LowestSupportedPeriods');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=obj1.getLoadModuleResult();
loadmodulestatus2=obj2.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() :
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS")
    obj1.setLoadModuleStatus("SUCCESS")
    obj2.setLoadModuleStatus("SUCCESS")
    expectedresult="SUCCESS";
    #Verify is DSL is enabled
    step = 1;
    tdkTestObj,dsl_wan, enable = getDSLWANStatus(obj, step);
    step = step + 1;
    print "TEST STEP %d : Check if the DSL WAN Status is Up and Active Link is Enabled" %step;
    print "EXPECTED RESULT %d : The DSL WAN Status is Up and Active Link is true" %step;

    #If DSL is enabled
    if enable == 0:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: DSL WAN Status is Up and Active Link is true" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        step = step + 1;
        #Get the initial values of "Device.DSL.X_RDK_Report.DSL.Enabled", "Device.DSL.X_RDK_Report.DSL.ReportingPeriod", "Device.DSL.X_RDK_Report.DSL.Default.ReportingPeriod", "Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL"
        tdkTestObj,initial_value,status = getReportingParams(obj, step);

        #If the initial values are retrieved successfully
        if status == 0:
            step = step + 1;
            print "TEST STEP %d : Check if Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL is 0, if not reboot the device and check if it is reset to 0" %step;
            print "EXPECTED RESULT %d : Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL should be 0" %step;

            #Check if Override TTL is 0, if not 0 reboot the device
            TTL_flag = 0;
            if int(initial_value[3]) != 0:
                TTL_flag = 1;
                print "Reboot the device for Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL to be reset to 0";
                obj.initiateReboot();
                sleep(300);
                #After reboot check if Override TTL is 0
                tdkTestObj = obj.createTestStep('TADstub_Get');
                tdkTestObj.addParameter("paramName","Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult :
                    value = int(details);
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL is :%d" %(step, value);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if value == 0:
                        TTL_flag = 0;
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Override TTL is 0 after reboot"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Override TTL is not 0 after reboot"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL is not fetched successfully" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL is 0" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            print "Reporting pararmeters are not retrieved successfully";

        if TTL_flag == 0:

            flag = 0;
            #Check if Pre-requisite function needs to be invoked
            if initial_value[0] == "true":
                #Invoke the DSL Diagnostic reports pre-requisite function
                print "Invoking Pre-requisite function for DSL Diagnostic Reports validation....."
                step = step + 1;
                tdkTestObj2 = obj2.createTestStep("TDKB_TR181Stub_SetMultiple");
                status = dslreports_prereq(tdkTestObj2, initial_value, step);

                if status == 0:
                   print "Pre-requisites set successfully";
                else:
                   flag = 1;
                   print "Pre-requisites are not set completely";
            else :
                print "Pre-requisite function need not be invoked";

            if flag == 0:

                #Get the number of log lines "Sent message successfully to parodus" in /rdklogs/logs/XDSLMANAGERLog.txt.0
                step = step + 1;
                tdkTestObj1 = obj1.createTestStep('ExecuteCmd');
                log = "Sent message successfully to parodus";
                no_of_lines,step = getLogFileTotalLinesCount(tdkTestObj1, log, step);
                print "The initial number of log lines \"Sent message successfully to parodus\" in XDSLMANAGERLog.txt.0 is : %d" %no_of_lines;

                #Set Default Reporting Period & Reporting Period to supported values
                print "Set Reporting periods to lowest supported values and override TTL as 0";
                step = step + 1;
                value_list = [];
                expectedresult = "SUCCESS";
                reporting_enable = "true";
                def_reporting_period = "1";
                reporting_period = "1";
                override_TTL = "0";
                value_list = [reporting_enable, reporting_period, def_reporting_period, override_TTL];
                tdkTestObj2 = obj2.createTestStep("TDKB_TR181Stub_SetMultiple");
                set_status = setReportingParams(tdkTestObj2, expectedresult, value_list, step);

                if set_status == 0:
                    #Check if the values are set properly
                    step = step + 1;
                    tdkTestObj, set_value, status = getReportingParams(obj, step);
                    step = step + 1;
                    print "TEST STEP %d : Check if the values set are retrived with get" %step;
                    print "EXPECTED RESULT %d : The get values should match the set values" %step;

                    if (set_value[0] == str(value_list[0])) and (set_value[1] == str(value_list[1])) and (set_value[2] == str(value_list[2])) and (set_value[3] == str(value_list[3])):
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: The get and the set values match" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        #As the Device.DSL.X_RDK_Report.DSL.Default.ReportingPeriod is set to 1s and override TTL =0,  sleeping for 10s
                        print "Sleeping for 10s";
                        sleep(10);

                        #Get the number of log lines "Sent message successfully to parodus" in /rdklogs/logs/XDSLMANAGERLog.txt.0
                        step = step + 1;
                        tdkTestObj1 = obj1.createTestStep('ExecuteCmd');
                        no_of_lines_after_rp,step = getLogFileTotalLinesCount(tdkTestObj1, log, step);
                        print "The final number of log lines \"Sent message successfully to parodus\" in XDSLMANAGERLog.txt.0 is : %d" %no_of_lines_after_rp;

                        #10 more reports should be sent in the last 10 seconds
                        step = step + 1;
                        print "TEST STEP %d : Check if the number of DSL reports sent after Default Reporting Period & Reporting Period are set to lowest supported values is 10" %step;
                        print "EXPECTED RESULT %d : The number of DSL reports sent after the set operation should be 10" %step;
                        difference = no_of_lines_after_rp - no_of_lines;

                        if difference == 10:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: The number of DSL reports sent after the set operation is : %d" %(step, difference);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: The number of DSL reports sent after the set operation is : %d" %(step, difference);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";

                        #Revert Operation
                        if (initial_value[0] != set_value[0]) or (initial_value[1] != set_value[1]) or (initial_value[2] != set_value[2]) or (initial_value[3] != set_value[3]):
                            print "\n************Revert operation required***************";
                            expectedresult = "SUCCESS";
                            step = step + 1;
                            value_list = [];
                            value_list = [initial_value[0], initial_value[1], initial_value[2], initial_value[3]]
                            tdkTestObj2 = obj2.createTestStep("TDKB_TR181Stub_SetMultiple");
                            set_status = setReportingParams(tdkTestObj2, expectedresult, value_list, step);

                            if set_status == 0:
                                tdkTestObj2.setResultStatus("SUCCESS");
                                print "Revert operation was successful";
                            else :
                                tdkTestObj2.setResultStatus("FAILURE");
                                print "Revert operation was not successful";
                        else:
                            print "Revert operation not required";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: The get and the set values do not match" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "Reporting parameters are not set successfully";
            else:
                print "Pre-requisites are not set successfully";
        else:
            print "Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL is not changed to 0";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: DSL WAN Status is %s and Active Link is %s" %(step, dsl_wan[1], dsl_wan[2]);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tad");
    obj1.unloadModule("sysutil");
    obj2.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    obj2.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

