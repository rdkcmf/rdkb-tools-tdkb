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
  <name>TS_WIFIHAL_5GHZGetApAssociatedDeviceDiagnosticResult2</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApAssociatedDeviceDiagnosticResult2</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check for the successful invocation of sum_time_ms,tid,sum_time_m using wifi_getApAssociatedDeviceTidStatsResult</synopsis>
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
    <test_case_id>TC_WIFIHAL_356</test_case_id>
    <test_objective>To check for the successful invocation of sum_time_ms,tid,sum_time_m using wifi_getApAssociatedDeviceTidStatsResult</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Connect a wifi client</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDeviceDiagnosticResult2</api_or_interface_used>
    <input_parameters>methodName :'WIFIHAL_GetApAssociatedDeviceDiagnosticResult2
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the module.
2.Get the getApAssociatedDeviceDiagnosticResult2  using   wifi_getApAssociatedDeviceDiagnosticResult2API.
3.Return SUCCESS for non empty value,else FAILURE.
4.Unload module.</automation_approch>
    <expected_output>Api should be invoked successfully and the values received from the api should be non empty</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHZGetApAssociatedDeviceDiagnosticResult2</test_script>
    <skipped>No</skipped>
    <release_version>M73</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
radio = "5G"
#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetApAssociatedDeviceDiagnosticResult2');
#Get the result of connection with test component and STB

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Prmitive test case which is associated to this Script
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDeviceDiagnosticResult2');
        tdkTestObj.addParameter("apIndex", idx);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        resultDetails = tdkTestObj.getResultDetails();

        if expectedresult in actualresult :
           output_array_size = resultDetails.split(':')[2].split(',')[0].strip()
           print "output_array_size: ",output_array_size
           cli_IPAddress = resultDetails.split(':')[3].split(',')[0].strip()
           print "cli_IPAddress: ",cli_IPAddress
           if int(output_array_size) > 0 and  cli_IPAddress:
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP : Get the output_array_size,cli_IPAddress"
              print "EXPECTED RESULT : Should get the output_array_size,cli_IPAddress"
              print "ACTUAL RESULT : %s"%resultDetails;
              print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "EXPECTED RESULT :  Get the output_array_size,cli_IPAddress"
               print "ACTUAL RESULT : Should get the output_array_size,cli_IPAddress";
               print "ACTUAL RESULT : %s"%resultDetails;
               print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP :Invoke GetApAssociatedDeviceDiagnosticResult2"
            print "EXPECTED RESULT : Should successfully invoke GetApAssociatedDeviceDiagnosticResult2"
            print "ACTUAL RESULT : Failed to invoke the GetApAssociatedDeviceDiagnosticResult2"
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"


    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";



