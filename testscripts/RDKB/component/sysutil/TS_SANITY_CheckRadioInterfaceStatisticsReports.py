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
  <version>6</version>
  <name>TS_SANITY_CheckRadioInterfaceStatisticsReports</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check for the presence of RadoInterfaceStatistics report logs,  "event:raw.kestrel.reports.RadioInterfacesStatistics" in 	PARODUSlog.txt.0 when Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled is in enabled state and "Sent message successfully to parodus" is populated under Harvesterlog.txt.0.</synopsis>
  <groups_id/>
  <execution_time>20</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SANITY_67</test_case_id>
    <test_objective>Check for the presence of RadoInterfaceStatistics report logs,  "event:raw.kestrel.reports.RadioInterfacesStatistic"  in PARODUSlog.txt.0 when Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled is in enabled state and "Sent message successfully to parodus" is populated under Harvesterlog.txt.0.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled
Type : bool
ParamValue : true</input_parameters>
    <automation_approch>1. Load the modules
2. Check if the log files PARODUSlog.txt.0 and Harvesterlog.txt.0 is present under /rdklogs/logs.
3. Get the initial value of Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled and store it.
4. Set Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled to true if not already true.
5. Check for the logs "Sent message successfully to parodus" in Harvesterlog.txt.0 in a loop.
6. Once the required logs are populated, check for the logs "event:raw.kestrel.reports.RadioInterfacesStatistics" in PARODUSlog.txt.0.
7. Revert to initial state if required
8. Unload the modules</automation_approch>
    <expected_output>The RadoInterfaceStatistics report logs,  "event:raw.kestrel.reports.RadioInterfacesStatistic"
 should be present in PARODUSlog.txt.0 when Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled is in enabled state and "Sent message successfully to parodus" is populated under Harvesterlog.txt.0.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckRadioInterfaceStatisticsReports</test_script>
    <skipped>No</skipped>
    <release_version>M98</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def set_Enable(pamobj, value, step):
    status = 1;
    expectedresult = "SUCCESS";
    tdkTestObj = pamobj.createTestStep('pam_SetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled");
    tdkTestObj.addParameter("ParamValue",value);
    tdkTestObj.addParameter("Type","bool");
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Set Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled to %s" %(step, value);
    print "EXPECTED RESULT %d : Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled should be set to %s successfully" %(step, value);

    if expectedresult in actualresult and details != "":
        status = 0;
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d : Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled is set to %s successfully; Details : %s" %(step, value, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d : Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled is not set to %s successfully; Details : %s" %(step, value, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
pamobj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_CheckRadioInterfaceStatisticsReports');
pamobj.configureTestCase(ip,port,'TS_SANITY_CheckRadioInterfaceStatisticsReports');

#Get the result of connection with test component and DUT
sysutilloadmodulestatus=sysObj.getLoadModuleResult();
pamloadmodulestatus=pamobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %pamloadmodulestatus

if "SUCCESS" in sysutilloadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    pamobj.setLoadModuleStatus("SUCCESS");

    #Check if file is present
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/Harvesterlog.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    #Check if file is present
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/PARODUSlog.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details1 = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    step = 1;
    print "\nTEST STEP %d: Check for Harvesterlog.txt.0 and PARODUSlog.txt.0 file presence" %step;
    print "EXPECTED RESULT %d: Files should be present" %step;

    if details == "File exist" and details1 == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d :  Harvesterlog.txt.0 and PARODUSlog.txt.0 file are present" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Get the enable status of Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled
        step = step + 1;
        tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP %d : Get the value of Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled" %step;
        print "EXPECTED RESULT %d: Should get the value of Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled" %step;

        if expectedresult in actualresult and details != "":
            enable = details.strip().replace("\\n", "");
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d : Enable Status of Device.X_RDKCENTRAL-COM_Report.RadioInterfaceStatistics.Enabled is : %s" %(step, enable);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #If initially disabled, then enable it
            revert_flag = 0;
            if "false" in enable:
                value = "true";
                step = step + 1;
                status = set_Enable(pamobj, value, step);

                if status == 0 :
                    revert_flag = 1;
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "RadioInterfaceStatistics is now enabled";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "RadioInterfaceStatistics is not enabled";
            else:
                status = 0;
                tdkTestObj.setResultStatus("SUCCESS");
                print "RadioInterfaceStatistics is enabled";

            if status == 0:
                #Check for the required log "Sent message successfully to parodus"
                step = step + 1;
                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                cmd = "grep -ire \"Sent message successfully to parodus\" /rdklogs/logs/Harvesterlog.txt.0";
                tdkTestObj.addParameter("command",cmd);
                str_1 = "Sent message successfully to parodus";

                print "\nTEST STEP %d: Check for the presence of the string %s" %(step, str_1);
                print "EXPECTED RESULT %d: %s string should be present" %(step, str_1);
                stringfound = 0;

                #Giving 16 iterations of 60s as the logging 15 minutes
                for iteration in range(1,17):
                    print "Checking for the log in Harvesterlog.txt.0....\nIteration : %d" %iteration;
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    if expectedresult in actualresult and str_1 in details:
                        stringfound = 1;
                        break;
                    else:
                        sleep(60);
                        continue;

                if stringfound == 1:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: %s string is found; Details : %s" %(step,str_1,details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Check if the required log "event:raw.kestrel.reports.RadioInterfacesStatistics" is also logged in the same interval in PARODUSlog.txt.0
                    step = step + 1;
                    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                    str_2 = "event:raw.kestrel.reports.RadioInterfacesStatistics";
                    cmd = "grep -ire \"event:raw.kestrel.reports.RadioInterfacesStatistics\" /rdklogs/logs/PARODUSlog.txt.0";
                    tdkTestObj.addParameter("command",cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    print "\nTEST STEP %d: Check for the presence of the string %s" %(step, str_2);
                    print "EXPECTED RESULT %d: %s string should be present" %(step, str_2);

                    if expectedresult in actualresult and str_2 in details:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: %s string is found; Details : %s" %(step,str_2,details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: %s string is not found; Details : %s" %(step,str_2,details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: %s string is not found; Details : %s" %(step,str_1,details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert operation
                if revert_flag == 1:
                    value = "false";
                    step = step + 1;
                    status = set_Enable(pamobj, value, step);

                    if status == 0 :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "RadioInterfaceStatistics parameter reverted";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "RadioInterfaceStatistics parameter not reverted";
                else:
                    print "Revert operation not required";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Need not check for RadioInterfacesStatistics logs as the parameter itself could not be enabled";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d : Parameter value not retrieved; Details : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Harvesterlog.txt.0 : %s, PARODUSlog.txt.0 : %s" %(step, details, details1);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
    pamobj.unloadModule("pam");
else:
    print "Failed to load module";
    sysObj.setLoadModuleStatus("FAILURE");
    pamobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
