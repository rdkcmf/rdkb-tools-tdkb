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
  <version>1</version>
  <name>TS_WANMANAGER_DSL_IsReportSent_TTLSet_ReportDisabled</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Verify whether the DSL report send to cloud gets stopped, when DSL report is disabled during the Override TTL time period is running</synopsis>
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
    <test_case_id>TC_WANMANAGER_50</test_case_id>
    <test_objective>Verify whether the DSL report send to cloud gets stopped, when DSL report is disabled during the Override TTL time period is running</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Wan Manager should be enabled
4.DSL connection must be enabled</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.DSL.X_RDK_Report.DSL.Enabled : True
Device.DSL.X_RDK_Report.DSL.ReportingPeriod : 300
Device.DSL.X_RDK_Report.DSL.Default.ReportingPeriod : 60
Device.DSL.X_RDK_Report.DSL.Default.OverrideTTL : 300</input_parameters>
    <automation_approch>1. Ensure that the DSL link is active
2. Get the initial DSL Reporting parameters
3. Invoke the pre-requisite function for DSL reports.
4. Set DSL Enable to true, Reporting period to 300, Default Reporting period to 60 and override TTL to 300.
5. Sleep for 150s
6. Set DSL Enable to false
7. Sleep for the remaining 150s
8. Check if the log line "Sent message successfully to parodus" in XDSLWANMANAGER.txt.0 is present. The number of DSL reports sent should be 0 in 300s as the DSL report is disabled when override TTL is running
9. Revert back to initial values</automation_approch>
    <expected_output>DSL report send to cloud should get stopped when DSL report is disabled during the Override TTL time period is running</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_DSL_IsReportSent_TTLSet_ReportDisabled</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks/>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_WANMANAGER_DSL_IsReportSent_TTLSet_ReportDisabled');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_DSL_IsReportSent_TTLSet_ReportDisabled');
obj2.configureTestCase(ip,port,'TS_WANMANAGER_DSL_IsReportSent_TTLSet_ReportDisabled');

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
    #Verify is DSL is enabled.
    step = 1;
    tdkTestObj, dsl_wan, enable = getDSLWANStatus(obj, step);

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
                   print "Pre-requisites are not completed successfully";
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
                print "Set Reporting periods and override TTL to supported values";
                step = step + 1;
                value_list = [];
                expectedresult = "SUCCESS";
                reporting_enable = "true";
                def_reporting_period = "60";
                reporting_period = "300";
                override_TTL = "300";
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
                        #As the Device.DSL.X_RDK_Report.DSL.ReportingPeriod is set to 300s and override TTL = 300, sleeping for 300s
                        print "Sleeping for 150s";
                        sleep(150);

                        #Disable DSL reporting halfway
                        step = step + 1;
                        tdkTestObj = obj.createTestStep('TADstub_Set');
                        tdkTestObj.addParameter("ParamName","Device.DSL.X_RDK_Report.DSL.Enabled")
                        tdkTestObj.addParameter("ParamValue","false");
                        tdkTestObj.addParameter("Type","boolean");
                        expectedresult="SUCCESS";
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        print "TEST STEP %d : Set Device.DSL.X_RDK_Report.DSL.Enabled to false" %step;
                        print "EXPECTED RESULT %d : Should set Device.DSL.X_RDK_Report.DSL.Enabled to false" %step;

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: %s" %(step, details);
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                            #Wait for next half time
                            print "Sleeping for 150s";
                            sleep(150);

                            #Get the number of log lines "Sent message successfully to parodus" in /rdklogs/logs/XDSLMANAGERLog.txt.0
                            step = step + 1;
                            tdkTestObj1 = obj1.createTestStep('ExecuteCmd');
                            no_of_lines_after_rp,step = getLogFileTotalLinesCount(tdkTestObj1, log, step);
                            print "The final number of log lines \"Sent message successfully to parodus\" in XDSLMANAGERLog.txt.0 is : %d" %no_of_lines_after_rp;

                            #As the DSL Reporting is disabled midway, the number of reports sent during the 300s intreval should be 0
                            step = step + 1;
                            print "TEST STEP %d : Check if the number of DSL reports sent after setting reporting parameters is 0" %step;
                            print "EXPECTED RESULT %d : The number of DSL reports sent after the set operation should be 0" %step;
                            difference = no_of_lines_after_rp - no_of_lines;

                            if difference == 0:
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
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
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
            print "Reporting parameters are not retrieved successfully";
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

