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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>11</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzGetApAssociatedDeviceStats</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetApAssociatedDeviceStats</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To validate the api which returns the associated device status for 5GHz .</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_560</test_case_id>
    <test_objective>To validate the api which returns the associated device status for 5Ghz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it Through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDeviceStats()</api_or_interface_used>
    <input_parameters>apIndex = 0
MAC : MAC of device.
At least one device should be connected to get details.</input_parameters>
    <automation_approch>1. Load wifihal module
2. Get the Ap Associated Device status of the device for 5GHz by using the primitive WIFIHAL_GetApAssociatedDeviceStats.
3. Unload wifihal module</automation_approch>
    <except_output>Should successfully list the associated device status for 5GHz radio by calling the primitive WIFIHAL_GetApAssociatedDeviceStats.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetApAssociatedDeviceStats</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import re;
from wifiUtility import *;
radio5 = "5G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetApAssociatedDeviceStats');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Validate wifi_getApAssociatedDeviceDiagnosticResult2() for 5GHZ
    tdkTestObjTemp, idx = getIndex(obj, radio5);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio5;
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
              tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDeviceStats');
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
                 print "TEST STEP : Get the ApAssociatedDeviceStats info"
                 print "EXPECTED RESULT : Should successfully get the ApAssociatedDeviceStats info"
                 print "ACTUAL RESULT : Successfully gets the ApAssociatedDeviceStats info"
                 print "Details: "
                 detailList = details.split(",")
                 for i in detailList:
                     print i;
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";
              else:
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP : Get the ApAssociatedDeviceStats info"
                  print "EXPECTED RESULT : Should successfully get the ApAssociatedDeviceStats info"
                  print "ACTUAL RESULT : Successfully gets the ApAssociatedDeviceStats info"
                  print "Details: %s"%details
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "Not able to  Get the ApAssociatedDeviceStats info as no device is connected or Invalid Format"
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
