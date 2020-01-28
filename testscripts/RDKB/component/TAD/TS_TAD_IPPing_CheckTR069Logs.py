##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_TAD_IPPing_CheckTR069Logs</name>
  <primitive_test_id/>
  <primitive_test_name>TADstub_Set</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To ensure no DIAGNOSTICS COMPLETE logs are coming in TR069.log when the IP Ping is triggered using namespaces.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_TAD_77</test_case_id>
    <test_objective>To ensure no DIAGNOSTICS COMPLETE logs are coming in TR069.log when the IP Ping is triggered using namespaces.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Set,TADstub_Get</api_or_interface_used>
    <input_parameters>Device.LogAgent.X_RDKCENTRAL-COM_TR69_LogLevel
Device.LogAgent.X_RDKCENTRAL-COM_TR69_LoggerEnable
Device.IP.Diagnostics.IPPing.Interface
Device.IP.Diagnostics.IPPing.Host
Device.IP.Diagnostics.IPPing.DiagnosticsState
Device.IP.Diagnostics.IPPing.AverageResponseTime</input_parameters>
    <automation_approch>1. Load  TAD modules
2.Enable the TR069 logging and set the log level as DEBUG
3. From script invoke TADstub_Set to set all the IPPing parameters
4. If set returns success, check if logs are updated in the TR069 logs
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6.Test Manager will publish the result in GUI as PASS/FAILURE based on the response from TAD stub.</automation_approch>
    <expected_output>The file /rdklogs/logs/TR69log.txt.0  should not contains the following strings on the log
    CwmpEvent-&gt;EventCode = 8 DIAGNOSTICS COMPLETE</expected_output>
    <priority>High</priority>
    <test_stub_interface>TAD</test_stub_interface>
    <test_script>TS_TAD_IPPing_CheckTR069Logs</test_script>
    <skipped>No</skipped>
    <release_version>M73</release_version>
    <remarks>None</remarks>
  </test_cases>
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
obj.configureTestCase(ip,port,'TS_TAD_IPPing_CheckSuccessCount');
sysobj.configureTestCase(ip,port,'TS_TAD_IPPing_CheckSuccessCount');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    host = tdkutility.readtdkbConfigFile(obj);
    #tdkTestObj = obj.createTestStep('TADstub_Get');
    #tdkTestObj.addParameter("paramName","Device.IP.Diagnostics.TraceRoute.Host");
    #expectedresult="SUCCESS";
    #tdkTestObj.executeTestCase(expectedresult);
    if host == "NULL":
        tdkTestObj.setResultStatus("FAILURE");
        print "Host name not available in tdkb config file"
    else:

	#Set the loglevel of TR69.log to DEBUG level
	tdkTestObj = obj.createTestStep('TADstub_Get');
        tdkTestObj.addParameter("paramName","Device.LogAgent.X_RDKCENTRAL-COM_TR69_LoggerEnable");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        logEnable = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
	    tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the enable status of TR069 logs";
            print "EXPECTED RESULT 1: Should get the enable status of TR069 logs";
            print "ACTUAL RESULT 1: %s" %logEnable
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    tdkTestObj.addParameter("paramName","Device.LogAgent.X_RDKCENTRAL-COM_TR69_LogLevel");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            logLevel = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Get the log level of TR069 logs";
                print "EXPECTED RESULT 2: Should get the log level of TR069 logs";
                print "ACTUAL RESULT 2: %s" %logLevel
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

		tdkTestObj = obj.createTestStep('TADstub_Set');
                tdkTestObj.addParameter("ParamName","Device.LogAgent.X_RDKCENTRAL-COM_TR69_LogLevel");
                tdkTestObj.addParameter("ParamValue","4");
                tdkTestObj.addParameter("Type","unsignedint");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult1 = tdkTestObj.getResult();
                details1 = tdkTestObj.getResultDetails();

		tdkTestObj.addParameter("ParamName","Device.LogAgent.X_RDKCENTRAL-COM_TR69_LoggerEnable");
                tdkTestObj.addParameter("ParamValue","true");
                tdkTestObj.addParameter("Type","bool");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult2 = tdkTestObj.getResult();
                details2 = tdkTestObj.getResultDetails();

		if expectedresult in actualresult1 and  expectedresult in actualresult2:
		    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Enable TR069 logging and set level as DEBUG";
                    print "EXPECTED RESULT 3: Should enable the TR069 logging and set level as DEBUG";
                    print "ACTUAL RESULT 3: %s,%s" %(details1,details2);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

		    #set the IP Ping params
        	    tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.IPPing.Interface");
        	    tdkTestObj.addParameter("ParamValue","Interface_erouter0");
        	    tdkTestObj.addParameter("Type","string");
        	    tdkTestObj.executeTestCase(expectedresult);
        	    actualresult = tdkTestObj.getResult();
        	    details = tdkTestObj.getResultDetails();
        	    if expectedresult in actualresult:
        	        #Set the result status of execution
        	        tdkTestObj.setResultStatus("SUCCESS");
        	        print "TEST STEP 4: Set the interface of IPPing";
        	        print "EXPECTED RESULT 4: Should set the interface of IPPing";
        	        print "ACTUAL RESULT 4: %s" %details;
        	        #Get the result of execution
        	        print "[TEST EXECUTION RESULT] : SUCCESS";

        	        tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.IPPing.Host");
        	        tdkTestObj.addParameter("ParamValue",host);
        	        tdkTestObj.addParameter("Type","string");
        	        tdkTestObj.executeTestCase(expectedresult);
        	        actualresult = tdkTestObj.getResult();
        	        details = tdkTestObj.getResultDetails();
        	        if expectedresult in actualresult:
        	            #Set the result status of execution
        	            tdkTestObj.setResultStatus("SUCCESS");
        	            print "TEST STEP 5: Set the host of IPPing";
        	            print "EXPECTED RESULT 5: Should set the host of IPPing";
        	            print "ACTUAL RESULT 5: %s" %details;
        	            #Get the result of execution
        	            print "[TEST EXECUTION RESULT] : SUCCESS";

                	    tdkTestObj.addParameter("ParamName","Device.IP.Diagnostics.IPPing.DiagnosticsState");
                	    tdkTestObj.addParameter("ParamValue","Requested");
                	    tdkTestObj.addParameter("Type","string");
                	    expectedresult="SUCCESS";
                	    tdkTestObj.executeTestCase(expectedresult);
                	    actualresult = tdkTestObj.getResult();
                	    details = tdkTestObj.getResultDetails();
                	    if expectedresult in actualresult:
                	        #Set the result status of execution
                	        tdkTestObj.setResultStatus("SUCCESS");
                	        print "TEST STEP 6: Set DiagnosticsState of IPPing as Requested";
                	        print "EXPECTED RESULT 6: Should set DiagnosticsState of IPPing as Requested";
                	        print "ACTUAL RESULT 6: %s" %details;
                	        #Get the result of execution
                	        print "[TEST EXECUTION RESULT] : SUCCESS";
                    		time.sleep(40);

				tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                		cmd = "cat /rdklogs/logs/TR69log.txt.0 | grep 'CwmpEvent->EventCode = 8 DIAGNOSTICS COMPLETE'"
                		tdkTestObj.addParameter("command", cmd);
                		tdkTestObj.executeTestCase(expectedresult);
                		actualresult = tdkTestObj.getResult();
                		logstatus = tdkTestObj.getResultDetails().strip();
				if logstatus:
				    tdkTestObj.setResultStatus("FAILURE");
				    print "The logs for ip ping are updated in the TR069 log file"
				else:
				    tdkTestObj.setResultStatus("SUCCESS");
				    print "The logs for ip ping are not updated in the TR069 log file"
                	    else:
                	        #Set the result status of execution
                	        tdkTestObj.setResultStatus("FAILURE");
                	        print "TEST STEP 6: Set DiagnosticsState of IPPing as Requested";
                	        print "EXPECTED RESULT 6: Should set DiagnosticsState of IPPing as Requested";
                	        print "ACTUAL RESULT 6: %s" %details;
                	        #Get the result of execution
                	        print "[TEST EXECUTION RESULT] : FAILURE";
        	        else:
        	            #Set the result status of execution
        	            tdkTestObj.setResultStatus("FAILURE");
        	            print "TEST STEP 5: Set the host of IPPing";
        	            print "EXPECTED RESULT 5: Should set the host of IPPing";
        	            print "ACTUAL RESULT 5: %s" %details;
        	            #Get the result of execution
        	            print "[TEST EXECUTION RESULT] : FAILURE";
        	    else:
        	        #Set the result status of execution
        	        tdkTestObj.setResultStatus("FAILURE");
        	        print "TEST STEP 4: Set the interface of IPPing";
        	        print "EXPECTED RESULT 4: Should set the interface of IPPing";
        	        print "ACTUAL RESULT 4: %s" %details;
        	        #Get the result of execution
        	        print "[TEST EXECUTION RESULT] : FAILURE";
		    #Revert the log param values
		    tdkTestObj = obj.createTestStep('TADstub_Set');
                    tdkTestObj.addParameter("ParamName","Device.LogAgent.X_RDKCENTRAL-COM_TR69_LogLevel");
                    tdkTestObj.addParameter("ParamValue",logLevel);
                    tdkTestObj.addParameter("Type","unsignedint");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult1 = tdkTestObj.getResult();
                    details1 = tdkTestObj.getResultDetails();

                    tdkTestObj.addParameter("ParamName","Device.LogAgent.X_RDKCENTRAL-COM_TR69_LoggerEnable");
                    tdkTestObj.addParameter("ParamValue",logEnable);
                    tdkTestObj.addParameter("Type","bool");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult2 = tdkTestObj.getResult();
                    details2 = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult1 and  expectedresult in actualresult2:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3: Revert the loglevel and enable status";
                        print "EXPECTED RESULT 3: Should revert the loglevel and enable status";
                        print "ACTUAL RESULT 3: %s,%s" %(details1,details2);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
		    else:
			tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Revert the loglevel and enable status";
                        print "EXPECTED RESULT 3: Should revert the loglevel and enable status";
                        print "ACTUAL RESULT 3: %s,%s" %(details1,details2);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
		  
		else:
		    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Enable TR069 logging and set level as DEBUG";
                    print "EXPECTED RESULT 3: Should enable the TR069 logging and set level as DEBUG";
                    print "ACTUAL RESULT 3: %s,%s" %(details1,details2);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
		tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Get the log level of TR069 logs";
                print "EXPECTED RESULT 2: Should get the log level of TR069 logs";
                print "ACTUAL RESULT 2: %s" %logLevel
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
	else:
	    tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the enable status of TR069 logs";
            print "EXPECTED RESULT 1: Should get the enable status of TR069 logs";
            print "ACTUAL RESULT 1: %s" %logEnable
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tad");

else:
        print "Failed to load tad module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
