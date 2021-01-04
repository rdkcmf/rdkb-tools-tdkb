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
  <version>3</version>
  <name>TS_WIFIHAL_5GHzGetApRoamingConsortiumElement</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApRoamingConsortiumElement</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Get the current RoamingConsortiumElement using wifi_getApRoamingConsortiumElement() and verify them</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIHAL_444</test_case_id>
    <test_objective>Get the current RoamingConsortiumElement using wifi_getApRoamingConsortiumElement() and verify them</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApRoamingConsortiumElement()</api_or_interface_used>
    <input_parameters>index:9</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getApRoamingConsortiumElement() and get the current OUI details
3. If OUI entry count is greater than zero, check if each OUI value retrieved has length within the acceptable range of 3 to 15
4.Unload wifihal module</automation_approch>
    <expected_output>wifi_getApRoamingConsortiumElement() should successfully return the RoamingConsortiumElement values</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetApRoamingConsortiumElement</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetApRoamingConsortiumElement');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    passPoint_5G_Index = 9;
    tdkTestObj = obj.createTestStep("WIFIHAL_GetApRoamingConsortiumElement");
    tdkTestObj.addParameter("apIndex", passPoint_5G_Index);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "TEST STEP 1: Get the RoamingConsortiumElement  for 5GHz using wifi_getApRoamingConsortiumElement()";
    print "EXPECTED RESULT 1: Should get the RoamingConsortiumElement  for 5GHz";
    if expectedresult in actualresult :
	print "ACTUAL RESULT 1: %s" %details;
	#Get the result of execution
	print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        entryCount = int(details.split(':')[1].strip().split(',')[0].split(' ')[1])
        print "RoamingConsortiumElement  entryCount received is: ", entryCount
        print "TEST STEP 2: Verify the RoamingConsortiumElements returned are within the specified range";
        print "EXPECTED RESULT 2: RoamingConsortiumElement OUI length should be between 3 to 15";
        if entryCount == 0:
            print "ACTUAL RESULT 1: No RoamingConsortiumElement available"
	    print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj.setResultStatus("SUCCESS");
        else:
            flag =1
            for i in range(1, entryCount +1):
                ouiLen = int(details.split(':')[1].strip().split(',')[i*2].strip().split(' ')[1])
                if ouiLen >2 and ouiLen <16:
                    print "Length of OUI %d : %d is within range" %(i, ouiLen)
                else:
                    print "Error: Length of OUI %d : %d is within range" %(i, ouiLen)
                    flag = 0;
            if flag == 1:
                print "ACTUAL RESULT 2: RoamingConsortiumElements returned are within the specified range"
                print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "ACTUAL RESULT 2: RoamingConsortiumElements returned are not within the specified range"
                print "[TEST EXECUTION RESULT] :FAILURE";
                tdkTestObj.setResultStatus("FAILURE");
    else:
	print "ACTUAL RESULT 1: %s" %details;
	#Get the result of execution
	print "[TEST EXECUTION RESULT] : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
