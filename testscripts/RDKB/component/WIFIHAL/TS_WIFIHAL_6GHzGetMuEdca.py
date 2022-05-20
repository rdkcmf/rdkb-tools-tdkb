##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <name>TS_WIFIHAL_6GHzGetMuEdca</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetMuEdca</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getMuEdca() for 6G radio and check if the Arbitration Inter-Frame Space Number, Lower bound Contention Window, Upper bound Contention Window and Timer values retrieved are valid integers for each of the access categories - Background, Best effort, Video and Voice.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_789</test_case_id>
    <test_objective>Invoke the HAL API wifi_getMuEdca() for 6G radio and check if the Arbitration Inter-Frame Space Number, Lower bound Contention Window, Upper bound Contention Window and Timer values retrieved are valid integers for each of the access categories - Background, Best effort, Video and Voice.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getMuEdca()</api_or_interface_used>
    <input_parameters>radioIndex : 6G radio index
accessCategory : 0 - Background, 1 - Best effort, 2 - Video, 3 - Voice</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getMuEdca() for 6G radio for each of the access categories : Background, Best effort, Video and Voice.
3. Check if the values retrieved for Arbitration Inter-Frame Space Number, Lower bound Contention Window, Upper bound Contention Window and Timer are valid integers.
4. Unload module</automation_approch>
    <expected_output>The HAL API wifi_getMuEdca() should be invoked successfully for 6G radio and the Arbitration Inter-Frame Space Number, Lower bound Contention Window, Upper bound Contention Window and Timer values retrieved should be valid integers for each of the access categories - Background, Best effort, Video and Voice.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzGetMuEdca</test_script>
    <skipped>No</skipped>
    <release_version>M101</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzGetMuEdca');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #MU (Multi-User) EDCA (Enhanced Distributed Channel Access) includes background : 0, best effort : 1, video : 2 and voice : 3
        accessCategory = ["Background", "Best Effort", "Video", "Voice"];
        step = 1;

        for category in range(0, 4):
            print "\n**********Category : %s**********" %accessCategory[category];
            tdkTestObj = obj.createTestStep("WIFIHAL_GetMuEdca");
            tdkTestObj.addParameter("radioIndex", idx);
            tdkTestObj.addParameter("accessCategory", category);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP %d: Invoke the HAL API wifi_getMuEdca() to retrieve the 6G MU-EDCA details for %s category" %(step, accessCategory[category]);
            print "EXPECTED RESULT %d: Should invoke the HAL API wifi_getMuEdca() successfully" %step;

            if expectedresult in actualresult and "MuEdca" in details:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Retrieve the MU EDCA structure values
                aifsn = details.split("aifsn=")[1].split(",")[0];
                cw_min = details.split("cw_min=")[1].split(",")[0];
                cw_max = details.split("cw_max=")[1].split(",")[0];
                timer = details.split("timer=")[1].split(",")[0];

                #Print all MU EDCA values
                print "Arbitration Inter-Frame Space Number = %s" %aifsn;
                print "Lower bound Contention Window = %s" %cw_min;
                print "Upper bound Contention Window = %s" %cw_max;
                print "Timer = %s" %timer;

                #Check if the values retrieved are valid
                step = step + 1;
                print "\nTEST STEP %d : Check if the MU EDCA structure values are valid integer values" %step;
                print "EXPECTED RESULT %d : MU EDCA structure values should be valid integer values" %step;

                if aifsn.isdigit() and cw_min.isdigit() and cw_max.isdigit() and timer.isdigit():
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: MU EDCA structure values are all valid" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Not all MU EDCA structure values are valid" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
            step = step + 1;

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
