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
  <name>TS_WIFIHAL_2.4GHz_SetApBeaconInterval</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamIntValue</primitive_test_name>
  <primitive_test_version>5</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set the Beacon Interval with wifi_setApBeaconInterval and validate for 2.4 Ghz WIFI.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_377</test_case_id>
    <test_objective>This test case is to set the Beacon Interval with wifi_setApBeaconInterval and validate for 2.4 Ghz WIFI.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setApBeaconInterval </api_or_interface_used>
    <input_parameters>radioIndex
BeaconInterval</input_parameters>
    <automation_approch>1.Load the module
2. get the Beacon Interval and store the default value
3. Increse the setvalue by 10 and set using wifi_setApBeaconInterval
4. verify the set operation .
5. Revert the Beacon Interval to previous value
6.Unload the module</automation_approch>
    <expected_output>The wifi_setApBeaconInterval  should set the value successfully</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHz_SetApBeaconInterval</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
import time;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

radio = "2.4G";

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHz_SetApBeaconInterval');
sysObj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHz_SetApBeaconInterval');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysutilloadmodulestatus =sysObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus

def get_Ap0BeaconInterval(tdkTestObj):
    query = "sh %s/tdk_platform_utility.sh getAp0BeaconInterval" %TDK_PATH
    tdkTestObj.addParameter("command", query);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    print "Beacon Interval is ",details;
    return details,actualresult;

if "SUCCESS" in (loadmodulestatus.upper() and  sysutilloadmodulestatus.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = sysObj.createTestStep('ExecuteCmd');
        expectedresult="SUCCESS";
        defBconInt,actualresult = get_Ap0BeaconInterval(tdkTestObj);

        if expectedresult in actualresult and defBconInt != "":
           defBconInt = int(defBconInt);
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 1: Get the Beacon Interval";
           print "EXPECTED RESULT 1: Should get the Beacon Interval ";
           print "ACTUAL RESULT 1: The Beacon Interval is :",defBconInt;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";

           setValue = int(defBconInt+10);

           #Script to load the configuration file of the component
           expectedresult="SUCCESS";
           radioIndex = idx;
           setMethod = "setApBeaconInterval"
           primitive = 'WIFIHAL_GetOrSetParamIntValue'
           print "Setting Beacon period to : ",setValue
           tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

           if expectedresult in actualresult:
              tdkTestObj.setResultStatus("SUCCESS");

              tdkTestObj = sysObj.createTestStep('ExecuteCmd');
              expectedresult="SUCCESS";
              bconInt,actualresult = get_Ap0BeaconInterval(tdkTestObj);

              if expectedresult in actualresult and bconInt != "" and int(bconInt)  == setValue :
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP 3: Get the Beacon Interval";
                 print "EXPECTED RESULT 3: Should get the Beacon Interval equal to the set";
                 print "ACTUAL RESULT 3: The Beacon Interval is :",bconInt,"  Beacon Set Interval was :",setValue;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";
              else:
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 3: Get the Beacon Interval";
                  print "EXPECTED RESULT 3: Should get the Beacon Interval equal to the set";
                  print "ACTUAL RESULT 3: The Beacon Interval is :",bconInt,"  Beacon Set Interval was :",setValue;
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";

              #Revert the value
              setValue = defBconInt;
              expectedresult="SUCCESS";
              radioIndex = idx;
              setMethod = "setApBeaconInterval"
              primitive = 'WIFIHAL_GetOrSetParamIntValue'
              print "Reverting Beacon period to : ",setValue
              tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

              if expectedresult in actualresult:
                 tdkTestObj.setResultStatus("SUCCESS");

                 tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                 expectedresult="SUCCESS";
                 time.sleep(20);
                 bcon,actualresult = get_Ap0BeaconInterval(tdkTestObj);
                 if expectedresult in actualresult and bcon!= "" and  int(defBconInt) ==  int(bcon):
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Get the Beacon Interval";
                    print "EXPECTED RESULT 5: Should get the Beacon Interval ";
                    print "ACTUAL RESULT 5: The Beacon Interval is :",bcon;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                 else:
                     tdkTestObj.setResultStatus("FAILURE");
                     print "TEST STEP 5: Get the Beacon Interval";
                     print "EXPECTED RESULT 5: Should get the Beacon Interval ";
                     print "ACTUAL RESULT 5: The Beacon Interval is :",bcon;
                     #Get the result of execution
                     print "[TEST EXECUTION RESULT] :FAILURE";
              else:
                  print "TEST STEP 4: Revert the Beacon Interval to previous";
                  print "EXPECTED RESULT 4: Should revert the beacon interval to previous";
                  print "ACTUAL RESULT 4: Revertion failed";
                  print "TEST EXECUTION RESULT : FAILURE";
                  tdkTestObj.setResultStatus("FAILURE");
           else:
               print "TEST STEP 2: Set the Beacon Interval";
               print "EXPECTED RESULT 2: Should set the Beacon Interval to ",setValue;
               print "ACTUAL RESULT 2: ",details;
               print "TEST EXECUTION RESULT : FAILURE";
               tdkTestObj.setResultStatus("FAILURE");
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the Beacon Interval";
            print "EXPECTED RESULT 1: Should get the Beacon Interval ";
            print "ACTUAL RESULT 1: The Beacon Interval is :",defBconInt;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
    sysObj.setLoadModuleStatus("FAILURE");
