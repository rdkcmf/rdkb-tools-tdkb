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
  <name>TS_TAD_ValidateFanMaxOverrideWithFanSpeedFile</name>
  <primitive_test_id/>
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To validate the Fan Max Override set operation with /tmp/.fan_speed_override</synopsis>
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
    <test_case_id>TC_TAD_81</test_case_id>
    <test_objective>This test case is to validate the Fan Max Override set operation with /tmp/.fan_speed_override</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.Thermal.Fan.MaxOverride</input_parameters>
    <automation_approch>1.Load the Module
2.Check if .fan_speed_override is present if present Fan Max Override is enabled
3.Disable the Fan Max Override and .fan_speed_override file should not be present.
4.else Check if .fan_speed_override is present if  not present Fan Max Override is disabled
5.Enable the Fan Max Override and .fan_speed_override file should be present.
6.Revert the Fan status to previous
7.Unload the Module</automation_approch>
    <expected_output>.fan_speed_override should be present on enabling and not present on disabling</expected_output>
    <priority>High</priority>
    <test_stub_interface>TAD</test_stub_interface>
    <test_script>TS_TAD_ValidateFanMaxOverrideWithFanSpeedFile</test_script>
    <skipped>No</skipped>
    <release_version>M79</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_ValidateFanMaxOverrideWithFanSpeedFile');
obj1.configureTestCase(ip,port,'TS_TAD_ValidateFanMaxOverrideWithFanSpeedFile');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1;

def FileExist (tdkTestObj):
    cmd = "[ -f /tmp/.fan_speed_override ] && echo \"File exist\" || echo \"File does not exist\"";
    tdkTestObj.addParameter("command",cmd);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    return actualresult,details;

def SetFanMaxOverride(tdkTestObj,setValue):
    tdkTestObj.addParameter("ParamName","Device.Thermal.Fan.MaxOverride");
    tdkTestObj.addParameter("ParamValue",setValue);
    tdkTestObj.addParameter("Type","bool");
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details= tdkTestObj.getResultDetails();

    return actualresult;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
     #Set the result status of execution
     obj.setLoadModuleStatus("SUCCESS");
     obj1.setLoadModuleStatus("SUCCESS");

     tdkTestObj = obj1.createTestStep('ExecuteCmd');
     actualresult,defdetails = FileExist (tdkTestObj);
     expectedresult="SUCCESS";

     if expectedresult in actualresult and defdetails == "File exist":
        print "TEST STEP 1: Check for .fan_speed_override"
        print "EXPECTED RESULT 1:should retrieve the presence of .fan_speed_override"
        print "ACTUAL RESULT 1 : .fan_speed_override file is present";
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        print "Fan Max override is Enabled as .fan_speed_override  is present";
        print "Disabling Fan Max Override ";

        tdkTestObj= obj.createTestStep('TADstub_SetOnly');
        actualresult = SetFanMaxOverride(tdkTestObj,"false");

        if expectedresult in actualresult:
           print "TEST STEP 2: Set the Fan Max Override to false"
           print "EXPECTED RESULT 2: Should set the Fan Max Override to false"
           print "ACTUAL RESULT 2 : Set was Successfull"
           print "[TEST EXECUTION RESULT] : SUCCESS";
           tdkTestObj.setResultStatus("SUCCESS");

           tdkTestObj = obj1.createTestStep('ExecuteCmd');
           actualresult,details = FileExist (tdkTestObj);
           if expectedresult in actualresult and details == "File does not exist":
              print "TEST STEP 3: Check for .fan_speed_override"
              print "EXPECTED RESULT 3:.fan_speed_override should not be present"
              print "ACTUAL RESULT 3 : .fan_speed_override file is not present";
              print "[TEST EXECUTION RESULT] : SUCCESS";
              tdkTestObj.setResultStatus("SUCCESS");
           else:
               print "TEST STEP 3: Check for .fan_speed_override"
               print "EXPECTED RESULT 3:.fan_speed_override should not be present"
               print "ACTUAL RESULT 3 : .fan_speed_override file is present";
               print "[TEST EXECUTION RESULT] : FAILURE";
               tdkTestObj.setResultStatus("FAILURE");
        else:
            print "TEST STEP 2: Set the Fan Max Override to false"
            print "EXPECTED RESULT 2: Should set the Fan Max Override to false"
            print "ACTUAL RESULT 2 : Set failed"
            print "[TEST EXECUTION RESULT] : FAILURE";
            tdkTestObj.setResultStatus("FAILURE");
     else:
         print "TEST STEP 1: Check for .fan_speed_override"
         print "EXPECTED RESULT 1:should retrieve the presence of .fan_speed_override"
         print "ACTUAL RESULT 1 : .fan_speed_override file is not present";
         print "[TEST EXECUTION RESULT] : SUCCESS";
         tdkTestObj.setResultStatus("SUCCESS");

         print "Fan Max override is disabled as .fan_speed_override  is not present";
         print "Enabling Fan Max Override ";

         tdkTestObj= obj.createTestStep('TADstub_SetOnly');
         actualresult = SetFanMaxOverride(tdkTestObj,"true");
         if expectedresult in actualresult:
            print "TEST STEP 2: Set the Fan Max Override to true"
            print "EXPECTED RESULT 2: Should set the Fan Max Override to true"
            print "ACTUAL RESULT 2 : Set was Successfull"
            print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj.setResultStatus("SUCCESS");

            tdkTestObj = obj1.createTestStep('ExecuteCmd');
            actualresult,details = FileExist (tdkTestObj);

            if expectedresult in actualresult and details == "File exist":
               print "TEST STEP 3: Check for .fan_speed_override"
               print "EXPECTED RESULT 3:.fan_speed_override should be present"
               print "ACTUAL RESULT 3 : .fan_speed_override file is present";
               print "[TEST EXECUTION RESULT] : SUCCESS";
               tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "TEST STEP 3: Check for .fan_speed_override"
                print "EXPECTED RESULT 3:.fan_speed_override should be present"
                print "ACTUAL RESULT 3 : .fan_speed_override file is present";
                print "[TEST EXECUTION RESULT] : FAILURE";
                tdkTestObj.setResultStatus("FAILURE");
         else:
             print "TEST STEP 2: Set the Fan Max Override to true"
             print "EXPECTED RESULT 2: Should set the Fan Max Override to true"
             print "ACTUAL RESULT 2 : Set failed"
             print "[TEST EXECUTION RESULT] : FAILURE";
             tdkTestObj.setResultStatus("FAILURE");

     #Reverting the Value
     if defdetails == "File exist":
        Setvalue = "true";
     else:
         Setvalue = "false";

     print "Reverting the SetFanMaxOverride  to ",Setvalue;
     tdkTestObj= obj.createTestStep('TADstub_SetOnly');
     actualresult = SetFanMaxOverride(tdkTestObj,Setvalue);
     if expectedresult in actualresult:
        print "TEST STEP 4: Revert SetFanMaxOverride to previous"
        print "EXPECTED RESULT 4:Should revert the SetFanMaxOverride to previous"
        print "ACTUAL RESULT 4 : Reversion was success";
        print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");
     else:
         print "TEST STEP 4: Revert SetFanMaxOverride to previous"
         print "EXPECTED RESULT 4:Should revert the SetFanMaxOverride to previous"
         print "ACTUAL RESULT 4 : Reversion failed";
         print "[TEST EXECUTION RESULT] : FAILURE";
         tdkTestObj.setResultStatus("FAILURE");
     obj.unloadModule("tad");
     obj1.unloadModule("sysutil");
else:
    print "Failed to load tad module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
