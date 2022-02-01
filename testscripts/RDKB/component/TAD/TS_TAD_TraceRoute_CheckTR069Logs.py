##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <name>TS_TAD_TraceRoute_CheckTR069Logs</name>
  <primitive_test_id/>
  <primitive_test_name>TADstub_Set</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To ensure no DIAGNOSTICS COMPLETE logs are coming in TR069.log when the Traceroute is triggered using namespaces</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_TAD_78</test_case_id>
    <test_objective>To ensure no DIAGNOSTICS COMPLETE logs are coming in TR069.log when the Traceroute is triggered using namespaces</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Set,TADstub_Get</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable
Device.IP.Diagnostics.TraceRoute.Interface
Device.IP.Diagnostics.TraceRoute.Host
Device.IP.Diagnostics.TraceRoute.DiagnosticsState
Device.IP.Diagnostics.TraceRoute.RouteHopsNumberOfEntries</input_parameters>
    <automation_approch>1. Load TAD modules
2. Enable TR069 RFC if not enabled and check if TR069 log file is present under /rdklogs/logs
3. From script invoke TADstub_Set to set all the trace route parameters
4. Check if the logs are updating in TR069 log file
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <expected_output>The /rdklogs/logs/TR69log.txt.0 file should not contains the following strings on the log
    CwmpEvent-&gt;EventCode = 8 DIAGNOSTICS COMPLETE</expected_output>
    <priority>High</priority>
    <test_stub_interface>TAD</test_stub_interface>
    <test_script>TS_TAD_TraceRoute_CheckTR069Logs</test_script>
    <skipped>No</skipped>
    <release_version>M73</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import time;
import tdkutility;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_TraceRoute_CheckTR069Logs');
sysobj.configureTestCase(ip,port,'TS_TAD_TraceRoute_CheckTR069Logs');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    host = tdkutility.readtdkbConfigFile(obj);
    if host == "NULL":
        tdkTestObj.setResultStatus("FAILURE");
        print "Host name not available in tdkb config file"
    else:
        #Check if TR69 RFC is enabled
        step = 1;
        tr69_flag = 0;
        tdkTestObj = obj.createTestStep('TADstub_Get');
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable");
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP %d : Get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable" %step;
        print "EXPECTED RESULT %d : Should get the value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable" %step;

        if expectedresult in actualresult:
            init_enable = details.strip().replace("\\n", "");
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d : Enable Status of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is : %s" %(step, init_enable);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #If disabled initially, then enable
            if init_enable == "false":
                step = step + 1;
                value = "true";
                tdkTestObj = obj.createTestStep('TADstub_Set');
                tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable");
                tdkTestObj.addParameter("ParamValue",value);
                tdkTestObj.addParameter("Type","bool");
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP %d: Set Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable to %s" %(step, value);
                print "EXPECTED RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable should be set to %s successfully" %(step,value);

                if expectedresult in actualresult:
                    tr69_flag = 1;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is set to %s successfully; Details : %s" %(step, value, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable is not set to %s successfully; Details : %s" %(step, value, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tr69_flag = 1;
                tdkTestObj.setResultStatus("SUCCESS");
                print "TR69 RFC is enabled initially";

            if tr69_flag == 1:
                #Check if the TR69 log file is created under /rdklogs/logs/TR69log.txt.0
                step = step + 1;
                time.sleep(10);
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                file = "/rdklogs/logs/TR69log.txt.0"
                cmd = "[ -f " + file + " ] && echo \"File exist\" || echo \"File does not exist\"";
                print "Command : ", cmd;
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                print "\nTEST STEP %d: Check for %s file presence" %(step, file);
                print "EXPECTED RESULT %d: %s file should be present" %(step, file);

                if details == "File exist":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: %s file is present" %(step, file);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Set Device.IP.Diagnostics.TraceRoute.Interface
                    step = step + 1;
                    tdkTestObj = obj.createTestStep('TADstub_Set');
                    tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.TraceRoute.Interface");
                    tdkTestObj.addParameter("ParamValue","Interface_erouter0");
                    tdkTestObj.addParameter("Type","string");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    print "\nTEST STEP %d: Set the interface of TraceRoute" %step;
                    print "EXPECTED RESULT %d: Should set the interface of TraceRoute" %step;

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Set Device.IP.Diagnostics.TraceRoute.Host
                        step = step + 1;
                        tdkTestObj = obj.createTestStep('TADstub_Set');
                        tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.TraceRoute.Host");
                        tdkTestObj.addParameter("ParamValue",host);
                        tdkTestObj.addParameter("Type","string");
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        print "\nTEST STEP %d: Set the host of TraceRoute" %step;
                        print "EXPECTED RESULT %d: Should set the host of TraceRoute" %step;

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Set Device.IP.Diagnostics.TraceRoute.DiagnosticsState
                            step = step + 1;
                            tdkTestObj = obj.createTestStep('TADstub_Set');
                            tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.TraceRoute.DiagnosticsState");
                            tdkTestObj.addParameter("ParamValue","Requested");
                            tdkTestObj.addParameter("Type","string");
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();

                            print "\nTEST STEP %d: Set DiagnosticsState of TraceRoute as Requested" %step;
                            print "EXPECTED RESULT %d: Should set DiagnosticsState of TraceRoute as Requested" %step;

                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: %s" %(step, details);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                #Check if 'CwmpEvent->EventCode = 8 DIAGNOSTICS COMPLETE' is present in TR69 log file
                                step = step + 1;
                                time.sleep(180);
                                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                                cmd = "cat /rdklogs/logs/TR69log.txt.0 | grep 'CwmpEvent->EventCode = 8 DIAGNOSTICS COMPLETE'"
                                tdkTestObj.addParameter("command", cmd);
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                logstatus = tdkTestObj.getResultDetails().strip();

                                print "\nTEST STEP %d : Check if the logs for traceroute are updated in TR069 log file" %step;
                                print "EXPECTED RESULT %d : Logs for tracerouter should not be updated in TR69 log file" %step;

                                if "COMPLETE" in logstatus:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d : The logs for traceroute are updated in the TR069 log file; Details : %s"%(step, logstatus);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                                else:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d : The logs for traceroute are not updated in the TR069 log file" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: %s" %(step, details);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: %s file is not present" %(step, file);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert operation
                if init_enable != "true":
                    tdkTestObj = obj.createTestStep('TADstub_Set');
                    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.TR069support.Enable");
                    tdkTestObj.addParameter("ParamValue","false");
                    tdkTestObj.addParameter("Type","bool");
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Revert operation of TR69 RFC was success";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Revert operation of TR69 RFC was failed";
                else:
                    print "TR69 RFC revert not required";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "TR69 RFC could not be enabled";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d : GET operation failed; Details : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

    obj.unloadModule("tad");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load tad module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

