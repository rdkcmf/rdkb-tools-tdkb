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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_SANITY_CheckProcessStoppingRestarting</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if any process is stopping/restarting in systemd_processRestart.log except the expected processes</synopsis>
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
    <box_type>RPI</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_50</test_case_id>
    <test_objective>To check if any process is stopping/restarting in systemd_processRestart.log except the expected processes.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>N/A</input_parameters>
    <automation_approch>1.Load the module
2.check for any stopping/restarting processes in  systemd_processRestart.log expect the expected processes.
3.if any other processes are found stopping/restarting mark the script as FAILURE else SUCCESS.
4.Unload the module.
</automation_approch>
    <expected_output>no stopping/restarting process except the expected ones should not  be present .</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_CheckProcessStoppingRestarting</test_script>
    <skipped>No</skipped>
    <release_version>M92</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
#use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckProcessStoppingRestarting');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
   #Set the result status of execution
   obj.setLoadModuleStatus("SUCCESS");
   logFile = "/rdklogs/logs/systemd_processRestart.log";
   logMsg ="Stopping/Restarting";
   print "TEST STEP 1: Checking if Stopping/Restarting processes log message is present in systemd_processRestart.log";
   query="grep -rin \"%s\" \"%s\"| grep -v \"rdkfwupgrader\" | grep -v \"snmpd\" | grep -v \"snmp_v2_subagent\" | grep -v \"Xcal-Device Service\"" %(logMsg,logFile);
   print "query:%s" %query
   tdkTestObj = obj.createTestStep('ExecuteCmd');
   tdkTestObj.addParameter("command", query)
   expectedresult="SUCCESS";
   tdkTestObj.executeTestCase(expectedresult);
   actualresult = tdkTestObj.getResult();
   details = tdkTestObj.getResultDetails().strip().replace("\\n","");
   if (len(details) != 0)  and  logMsg in details:
      tdkTestObj.setResultStatus("FAILURE");
      print "EXPECTED RESULT 1 : no processes should restart/stop";
      print "ACTUAL RESULT 1 :Search Result :%s "%details;
      print "[TEST EXECUTION RESULT] : FAILURE";
   else:
       print "EXPECTED RESULT 1 : no processes should restart/stop";
       tdkTestObj.setResultStatus("SUCCESS");
       print "ACTUAL RESULT 1 :Search Result :%s "%details;
       print "[TEST EXECUTION RESULT] : SUCCESS";
   obj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
