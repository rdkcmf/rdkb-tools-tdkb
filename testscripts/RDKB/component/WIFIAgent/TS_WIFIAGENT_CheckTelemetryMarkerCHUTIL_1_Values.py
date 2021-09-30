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
  <name>TS_WIFIAGENT_CheckTelemetryMarkerCHUTIL_1_Values</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the CHUTIL_1 marker comes up with the three values that are comma separated :   CU due to self BSS from transmitted traffic , CU due to self BSS from received traffic and CU due to overlapping BSS.</synopsis>
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
    <test_case_id>TC_WIFIAGENT_149</test_case_id>
    <test_objective>To check if the CHUTIL_1 marker comes up with the three values that are comma separated :   CU due to self BSS from transmitted traffic , CU due to self BSS from received traffic and CU due to overlapping BSS.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the modules
2. Check if the log file wifihealth.txt is present under /rdklogs/logs.
3. Check if the channel utilization marker CHUTIL_1 is present in wifihealth.txt. If not found, check every 60s for 15 minutes to see if the log is getting populated.
4. From the telemetry marker retrieve the comma separated values for CU due to self BSS from transmitted traffic , CU due to self BSS from received traffic and CU due to overlapping BSS.
5. Unload the modules.</automation_approch>
    <expected_output>The CHUTIL_1 marker should come up with the three values that are comma separated : CU due to self BSS from transmitted traffic , CU due to self BSS from received traffic and CU due to overlapping BSS.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckTelemetryMarkerCHUTIL_1_Values</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from  time import sleep;

#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckTelemetryMarkerCHUTIL_1_Values');

#Get the result of connection with test component and DUT
sysutilloadmodulestatus=sysObj.getLoadModuleResult();

if "SUCCESS" in sysutilloadmodulestatus.upper():
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");

    #Check if wifihealth.txt file is present
    step = 1;
    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    cmd = "[ -f /rdklogs/logs/wifihealth.txt ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d: Check for wifihealth log file presence" %step;
    print "EXPECTED RESULT %d:wifihealth log file should be present" %step;

    if details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d:wifihealth log file is present" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check for the maraker CHUTIL_1
        step = step + 1;
        tdkTestObj = sysObj.createTestStep('ExecuteCmd');
        cmd = "grep -ire \"CHUTIL_1\" /rdklogs/logs/wifihealth.txt";
        tdkTestObj.addParameter("command",cmd);
        expectedresult="SUCCESS";

        print "\nTEST STEP %d: Check for the presence of the marker CHUTIL_1" %step;
        print "EXPECTED RESULT %d: CHUTIL_1 marker should be present" %step;
        markerfound = 0;

        #Giving 15 iterations of 60s each as the default value of Channel Utility Log Interval is 900s
        for iteration in range(1,16):
            print "Waiting for the marker to get populated in wifihealth.txt....\nIteration : %d" %iteration;
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            if expectedresult in actualresult and "CHUTIL_1" in details:
                markerfound = 1;
                break;
            else:
                sleep(60);
                continue;

        if markerfound == 1:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: CHUTIL_1 marker is found; Details : %s" %(step,details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Get the values for <CU due to self BSS from transmitted traffic>,<CU due to self BSS from received traffic >,<CU due to overlapping BSS>
            marker_list = details.split("split:")[1].split(",");
            print "Marker_list : ", marker_list;

            step = step + 1;
            print "\nTEST STEP %d : Get the values for CU due to self BSS from transmitted traffic, CU due to self BSS from received traffic and CU due to overlapping BSS" %step;
            print "EXPECTED RESULT %d : Should get the values for CU due to self BSS from transmitted traffic, CU due to self BSS from received traffic and CU due to overlapping BSS" %step;

            if marker_list[0] != "" or marker_list[1] != "" or marker_list[2] != "" or marker_list[0] != " " or marker_list[1] != " " or marker_list[2] != " ":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: The marker values are retrieved successfully" %(step);
                print "CU due to self BSS from transmitted traffic : %s" %marker_list[0];
                print "CU due to self BSS from received traffic : %s" %marker_list[1];
                print "CU due to overlapping BSS : %s" %marker_list[2];
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: The marker values are not retrieved successfully" %(step);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: CHUTIL_1 marker is not found; Details : %s" %(step,details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d:wifihealth log file is not present" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
else:
    print "Failed to load module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

