##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <version>10</version>
  <name>TS_WIFIHAL_2.4GHzGetApDeviceTxrate</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApDeviceTxRxRate</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the Tx rate of Ap associated devices for 2.4GHz.</synopsis>
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
    <test_case_id>TC_WIFIHAL_345</test_case_id>
    <test_objective>To get the Tx rate of Ap associated devices for 2.4GHz.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApDeviceTxrate()</api_or_interface_used>
    <input_parameters>apIndex =  0
methodName = getApDeviceTxrate
MAC Address : Should be connected atleast one device before execution</input_parameters>
    <automation_approch>1.Load the module.
2.Get the Tx rate of Ap associated devices using wifi_getApDeviceTxrate() API.
3.Unload the module.</automation_approch>
    <except_output>Get the Tx rate of Ap associated devices for 2.4GHz.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetApDeviceTxrate</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import re;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
from wifiUtility import *;
radio2 = "2.4G"

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetApDeviceTxrate');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Validate wifi_getApAssociatedDeviceDiagnosticResult2() for 2.4GHZ
    tdkTestObjTemp, idx = getIndex(obj, radio2);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio2;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDevice');
        tdkTestObj.addParameter("apIndex",idx);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print "Entire Details:",details;
        if expectedresult in actualresult:
           outputList = details.split("=")[1].strip()
           if "," in outputList:
              outputValue = outputList.split(",")[0].strip()
           else:
            outputValue = outputList.split(":Value")[0].strip()

           print "TEST STEP: get the associateddevice"
           print "expected result: should get the number of associated devices"
           print "Associated Device's MAC address:",outputValue

           #check if outputvalue is a mac address
           if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", outputValue.lower()):
              #Prmitive test case which associated to this Script
              tdkTestObj = obj.createTestStep('WIFIHAL_GetApDeviceTxRxRate');
              tdkTestObj.addParameter("methodName","getApDeviceTxrate");
              tdkTestObj.addParameter("apIndex", idx);
              #Connect a device and add MAC Address
              tdkTestObj.addParameter("MAC",outputValue);
              expectedresult="SUCCESS";
              tdkTestObj.executeTestCase(expectedresult);
              actualresult = tdkTestObj.getResult();
              details = tdkTestObj.getResultDetails();
              print"details",details;
              if expectedresult in actualresult :
                 tdkTestObj.setResultStatus("SUCCESS");
                 details = int(details.split(":")[1].strip());
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP : Get the ApDeviceTxrate"
                 print "EXPECTED RESULT : Should successfully get the ApDeviceTxrate"
                 print "ACTUAL RESULT : Successfully gets the ApDeviceTxrate"
                 print "TxRate in Mbps", details
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";
              else:
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP : Get the ApDeviceTxrate"
                  print "EXPECTED RESULT : Should successfully get the ApDeviceTxrate"
                  print "ACTUAL RESULT : Failed to get the ApDeviceTxrate"
                  print "Details: %s"%details
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "Not able to  Get the ApDeviceTxrate as no device is connected or Invalid Format"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP: get the associateddevice"
            print "EXPECTED RESULT: should get the number of associated devices"
            print "ACTUAL RESULT : Failed to get the number of associated devices"
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
