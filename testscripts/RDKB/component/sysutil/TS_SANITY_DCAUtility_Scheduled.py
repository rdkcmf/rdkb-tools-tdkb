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
  <name>TS_SANITY_DCAUtility_Scheduled</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To verify if DCA Utility is scheduled in Cron tab</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_SYSUTIL_58</test_case_id>
    <test_objective>To verify if DCA Utility is scheduled in Cron tab</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>Execute_Cmd</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the module .
2.Check if dca_utility.sh is scheduled in cron tab
3.Mark script as failure in case scheduling is not done
4.Unload the module</automation_approch>
    <expected_output>dca_utility.sh should be scheduled  in DUT</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_DCAUtility_Scheduled</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_DCAUtility_Scheduled');
#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    query="crontab -l | grep -i \"dca_utility\"";
    print "query:%s" %query
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", query)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n","");
    print "Search Result :%s "%details;

    if expectedresult in actualresult and details =="":
       tdkTestObj.setResultStatus("FAILURE");
       print "TEST STEP 1: Checking if dca_utility.sh is scheduled in cron tab";
       print "EXPECTED RESULT 1: dca_utility.sh is expected to be scheduled in cron tab";
       print "ACTUAL RESULT 1:",details;
       print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Checking if dca_utility.sh is scheduled in cron tab";
        print "EXPECTED RESULT 1: dca_utility.sh is expected to be scheduled in cron tab";
        print "ACTUAL RESULT 1:",details;
        print "[TEST EXECUTION RESULT] : SUCCESS";
    obj.unloadModule("sysutil");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
