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
  <version>1</version>
  <name>TS_platform_stub_hal_GetFanStatus</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_getFanStatus</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check  the get functionality for Fan status .</synopsis>
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
    <test_case_id>TC_HAL_Platform_41</test_case_id>
    <test_objective>To validate Platform HAL API platform_hal_GetFanStatus()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_GetFanStatus()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  platform module.
2. Get the value form equivalent tr181 parameter Device.Thermal.Fan.Status
3. From script invoke platform_stub_hal_GetFanStatus().
4.  Check whether  the tr81 and  hal received value are equivalent
5. Validation of  the result is done within the python script and send the result status to Test Manager.
6. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Platform stub.</automation_approch>
    <expected_output>The tr181 and hal api  should result with the same value.</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_PLATFORM</test_stub_interface>
    <test_script>TS_platform_stub_hal_GetFanStatus</test_script>
    <skipped>No</skipped>
    <release_version>M76</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");
tr181obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_GetFanStatus');
tr181obj.configureTestCase(ip,port,'TS_platform_stub_hal_GetFanStatus');

loadmodulestatus =obj.getLoadModuleResult();
tr181loadmodulestatus =tr181obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %tr181loadmodulestatus ;

if "SUCCESS" in (loadmodulestatus.upper() and  tr181loadmodulestatus.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    tr181obj.setLoadModuleStatus("SUCCESS")

    tdkTestObj = tr181obj.createTestStep("TDKB_TR181Stub_Get");
    tdkTestObj.addParameter("ParamName","Device.Thermal.Fan.Status");
    expectedresult ="SUCCESS"
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    Tr181FanStatus = " ";
    Tr181FanStatus = tdkTestObj.getResultDetails();

    if expectedresult in actualresult and Tr181FanStatus != "":
       print "TEST STEP 1: Get the Fan status using tr181 parameter";
       print "EXPECTED RESULT 1: Should get the Fan status ";
       print "ACTUAL RESULT 1: Fan status is :",Tr181FanStatus;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
       tdkTestObj.setResultStatus("SUCCESS");

       #Script to load the configuration file of the component
       tdkTestObj = obj.createTestStep("platform_stub_hal_getFanStatus");
       expectedresult="SUCCESS";
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails();

       if expectedresult in actualresult :
          print"TEST STEP 2:  Call  the platform_stub_hal_getFanStatus"
          print"EXPECTED RESULT 2: The  platform_stub_hal_getFanStatus should be successfull"
          print"ACTUAL RESULT 2: platform_stub_hal_getFanStatus call successfull"
          tdkTestObj.setResultStatus("SUCCESS");
          print "[TEST EXECUTION RESULT] : SUCCESS";

          HalFanStatus = details.split(":")[1].strip();

          if int(HalFanStatus) == 0:
             Checkvalue  = "false";

          else:
              Checkvalue = "true";

          print "FanStatus from Tr181 query:",Tr181FanStatus;
          print "FanStatus from hal call api:",Checkvalue;

          if Checkvalue == Tr181FanStatus:
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Get the Fan Status using HAL call api";
             print "EXPECTED RESULT 3: Should get the fan status  from HAL api call and  tr181 equal";
             print "ACTUAL RESULT 3: %s"%details;
             print "[TEST EXECUTION RESULT] : SUCCESS";

          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Get the Fan status using HAL call api";
              print "EXPECTED RESULT 3: Should get the Fan status from HAL api call and from tr181 equal";
              print "ACTUAL RESULT 3: %s" %details;
              print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           print"TEST STEP 2:  Call  the platform_stub_hal_getFanStatus"
           print"EXPECTED RESULT 2: The  platform_stub_hal_getFanStatus should be successfull"
           print"ACTUAL RESULT 2: platform_stub_hal_getFanStatus call failed"
           tdkTestObj.setResultStatus("FAILURE");
           print "[TEST EXECUTION RESULT] : FAILURE";

    else:
        print "TEST STEP 1: Get the Fan status using tr181 parameter";
        print "EXPECTED RESULT 1: Should get the Fan status ";
        print "ACTUAL RESULT 1: Failed to get the Fan Status :",Tr181FanStatus;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("halplatform");
    tr181obj.unloadModule("tdkbtr181");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

