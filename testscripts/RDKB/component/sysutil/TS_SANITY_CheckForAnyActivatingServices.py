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
  <name>TS_SANITY_CheckForAnyActivatingServices</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if any service is found to be in activating state in the device after boot-up.</synopsis>
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
    <test_case_id>TC_SANITY_63</test_case_id>
    <test_objective>To check if any service is found to be in activating state in the device after boot-up.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the sysutil module
2. Get the device uptime using Device.DeviceInfo.UpTime
3. Check if any services are in activating state in the device in the current uptime
4. If the uptime is greater than 10mins and no activating services are found then initiate a device reboot
5. Once the device comes up after reboot, check if any services are found in activating state.
6. Unload the module</automation_approch>
    <expected_output>No service should be in activating state once the device comes up after reboot.</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_CheckForAnyActivatingServices</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''

def checkActivatingServices(obj, step):
    status = 0;
    query="systemctl -a --state=activating | grep -rin \"activating\"";
    print "query:%s" %query
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", query)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n","");
    print "Search Result :%s "%details;

    if expectedresult in actualresult and "activating" in details:
        status = 1;
        tdkTestObj.setResultStatus("FAILURE");
        print "\nTEST STEP %d: Checking if any Activating Services are seen" %step;
        print "EXPECTED RESULT %d: No Activating Services should be present" %step;
        print "ACTUAL RESULT %d : %s" %(step, details);
        print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("SUCCESS");
        print "\nTEST STEP %d: Checking if any Activating Services are seen" %step;
        print "EXPECTED RESULT %d: No Activating Services should be present" %step;
        print "ACTUAL RESULT %d: %s" %(step, details);
        print "[TEST EXECUTION RESULT] : SUCCESS";
    return status, tdkTestObj;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");
pamobj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SANITY_CheckForAnyActivatingServices');
pamobj.configureTestCase(ip,port,'TS_SANITY_CheckForAnyActivatingServices');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=pamobj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    pamobj.setLoadModuleStatus("SUCCESS");

    #Get the uptime and check if it is greater than 600s(10 mins)
    tdkTestObj = pamobj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.DeviceInfo.UpTime");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP 1: Get the UpTime";
    print "EXPECTED RESULT 1: Should get the UpTime";

    if expectedresult in actualresult and details.isdigit():
        uptime = int(details);
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: UpTime is %d" %uptime;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #check if any services are found in activating state in the device
        step = 2;
        status, tdkTestObj = checkActivatingServices(obj, step);
        if status == 1:
            tdkTestObj.setResultStatus("FAILURE");
            print "Services are found in activating state after an uptime of %ds" %uptime;
        else:
            tdkTestObj.setResultStatus("SUCCESS");
            print "Services are not found in activating state after an uptime of %ds" %uptime;

        #check if any service is in activating state after reboot if the uptime is greater than 10mins
        if uptime >= 600 and status == 0:
            #Initiate a device reboot and check if any services are in activating state after devices comes up
            print "\n****DUT is going for a reboot and will be up after 360 seconds*****";
            obj.initiateReboot();
            sleep(360);
            step = 3;
            status, tdkTestObj = checkActivatingServices(obj, step);

            if status == 1:
                tdkTestObj.setResultStatus("FAILURE");
                print "Services are found in activating state after device boot-up";
            else:
                tdkTestObj.setResultStatus("SUCCESS");
                print "Services are not found in activating state after device boot-up";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Failure in getting the UpTime. Details: %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("sysutil");
    pamobj.unloadModule("pam");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    pamobj.setLoadModuleStatus("FAILURE");

