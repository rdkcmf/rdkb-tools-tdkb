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
  <version>3</version>
  <name>TS_WIFIHAL_EnableGreylistAccessControl</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To enable Grey List access control  using wifi api wifi_enableGreylistAccessControl and check if the necessary hostapd conf files are populated</synopsis>
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
    <test_case_id>TC_WIFIHAL_551</test_case_id>
    <test_objective>To enable Grey List access control  using wifi api wifi_enableGreylistAccessControl and check if the necessary hostapd conf files are populated</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHAL_GetOrSetParamBoolValue</api_or_interface_used>
    <input_parameters>methodname  - enableGreylistAccessControl
param - 1 for enable</input_parameters>
    <automation_approch>1.Load the module
2.Get the current radius grey list Enable status using tr181 parameter Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RadiusGreyList.Enable
3.Enable the radius grey list Enable status using api wifi_enableGreylistAccessControl
4.Check if hostapd conf files secath4,secath5,secath8,secath9  are present
5.revert the value to previous
6.Unload the module</automation_approch>
    <expected_output>The api call to enable wifi_enableGreylistAccessControl should be successfull and respective conf files should get populated</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_EnableGreylistAccessControl</test_script>
    <skipped>No</skipped>
    <release_version>M88</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from time import sleep ;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","RDKB");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
radio = "2.4G"

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_EnableGreylistAccessControl');
wifiobj.configureTestCase(ip,port,'TS_WIFIHAL_EnableGreylistAccessControl');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_EnableGreylistAccessControl');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

wifiloadmodulestatus = wifiobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %wifiloadmodulestatus;

sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus

if "SUCCESS" in (loadmodulestatus.upper() and sysloadmodulestatus.upper() and wifiloadmodulestatus.upper()):
        obj.setLoadModuleStatus("SUCCESS");
        wifiobj.setLoadModuleStatus("SUCCESS");
        sysobj.setLoadModuleStatus("SUCCESS");

        tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.RadiusGreyList.Enable");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        currValue = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1 : Get the current radius grey list Enable status";
            print "ACTUAL RESULT 1: Should get the current radius grey list Enable status";
            print "EXPECTED RESULT 1 :The current radius grey list Enable status is :",currValue;
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if "true" in currValue:
               oldEnable = 1
            else:
                oldEnable = 0

            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
            tdkTestObj.addParameter("methodName","enableGreylistAccessControl");
            tdkTestObj.addParameter("param",1);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 2 : Enable the radius grey list Enable status ";
               print "ACTUAL RESULT 2: Should enable the radius grey list Enable status successfully";
               print "EXPECTED RESULT 2 :set status is :",details;
               print "[TEST EXECUTION RESULT] : SUCCESS";

               sleep(60);

               confFiles = ["/tmp/secath4","tmp/secath5","/tmp/secath8/","/tmp/secath9"];
               print "TEST STEP :Checking if %s are present" %confFiles;
               for item in confFiles:
                   tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                   cmd = "[ -f %s ] && echo \"File exist\" || echo \"File does not exist\""%item;
                   tdkTestObj.addParameter("command",cmd);
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult = tdkTestObj.getResult();
                   details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                   if details == "File exist":
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "EXEPCTED RESULT : %s conf file should be present"%item;
                      print "ACTUAL RESULT : %s file is present"%item;
                      print "[TEST EXECUTION RESULT] : SUCCESS";
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "EXEPCTED RESULT : %s conf file should be present"%item;
                       print "ACTUAL RESULT  : %s file is not present"%item;
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : FAILURE";
                       break;

               if oldEnable!= 1:
                   #Revert the value to previous
                   tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                   tdkTestObj.addParameter("methodName","enableGreylistAccessControl");
                   tdkTestObj.addParameter("param",oldEnable);
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult = tdkTestObj.getResult();
                   details = tdkTestObj.getResultDetails();
                   if expectedresult in actualresult:
                       tdkTestObj.setResultStatus("SUCCESS");
                       print "TEST STEP 3 : Revert the radius grey list Enable status to %s"%oldEnable;
                       print "ACTUAL RESULT 3: Should revert the radius grey list Enable status successfully";
                       print "EXPECTED RESULT 3 :",details;
                       print "[TEST EXECUTION RESULT] : SUCCESS";
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 3 : Revert the radius grey list Enable status to %s"%oldEnable;
                       print "ACTUAL RESULT 3: Should revert the radius grey list Enable status successfully";
                       print "EXPECTED RESULT 3 :",details;
                       print "[TEST EXECUTION RESULT] : FAILURE";
            else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 2 : Enable the radius grey list Enable status";
               print "ACTUAL RESULT 2: Should enable the radius grey list Enable status successfully";
               print "EXPECTED RESULT 2 :set status is :",details;
               print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1 : Get the current radius grey list Enable status";
            print "ACTUAL RESULT 1: Should get the current radius grey list Enable status";
            print "EXPECTED RESULT 1 :The current radius grey list Enable status is :",currValue;
            print "[TEST EXECUTION RESULT] : FAILURE";
        obj.unloadModule("wifihal");
        wifiobj.unloadModule("wifiagent");
        sysobj.unloadModule("sysutil");
else:
    print "Failed to load  module";
    obj.setLoadModuleStatus("FAILURE");
    wifiobj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
