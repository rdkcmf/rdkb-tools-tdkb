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
  <version>9</version>
  <name>TS_WIFIHAL_2.4GHzSetApSecurityMFPConfig</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>9</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check get/setApSecurityMFPConfig() functionality and get value as expected.</synopsis>
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
    <test_case_id>TC_WIFIHAL_348</test_case_id>
    <test_objective>To check get/setApSecurityMFPConfig() functionality for 2.4GHz.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApSecurityMFPConfig()
wifi_setApSecurityMFPConfig</api_or_interface_used>
    <input_parameters>methodName: getApSecurityMFPConfig
methodName: setApSecurityMFPConfig
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke "WIFIHAL_GetOrSetParamStringValue" to get the MFP config value  for 2.4GHz and store in the variable initialConfigValue
3. Invoke "WIFIHAL_GetOrSetParamStringValue" to set the MFP config values  other than initialConfigValue .
4.  Invoke "WIFIHAL_GetOrSetParamStringValue" to get the current MFP config value  for 2.4GHz and store in the variable finalConfigValue to verify with setConfigValue
5. Reverted the MFP config value to initialConfigValue
6.Unload wifihal module</automation_approch>
    <except_output>Return Success when the setConfigValue and finalConfigValue are same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetApSecurityMFPConfig</test_script>
    <skipped>No</skipped>
    <release_version>Nil</release_version>
    <remarks>Nil</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
import tdklib;
from wifiUtility import *;
radio2 = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetApSecurityMFPConfig');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Validate wifi_getApAssociatedDeviceDiagnosticResult2() for 2.4GHZ
    tdkTestObjTemp, idx = getIndex(obj, radio2);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio2;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";

        #Checking for AP Index 1, Similar way we can check for other APs
        apIndex = idx
        getMethod = "getApSecurityMFPConfig"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
        mfpConfigValues = ["Disabled", "Optional", "Required"]

        if expectedresult in actualresult:
           initialConfigValue = details.split(":")[1].strip()
           print "initialConfigValue : ", initialConfigValue
           if initialConfigValue in mfpConfigValues:
              mfpConfigValues.remove(str(initialConfigValue))
              print "mfpConfigValues : ", mfpConfigValues
              for i,word in enumerate(mfpConfigValues):
                  expectedresult="SUCCESS";
                  apIndex = idx
                  setMethod = "setApSecurityMFPConfig"
                  setConfigValue = mfpConfigValues[i]
                  primitive = 'WIFIHAL_GetOrSetParamStringValue'
                  print "setConfigValue : ", setConfigValue

                  #Calling the method from wifiUtility to execute test case and set result status for the test.
                  tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setConfigValue, setMethod)

                  if expectedresult in actualresult:
                      apIndex = idx
                      getMethod = "getApSecurityMFPConfig"
                      primitive = 'WIFIHAL_GetOrSetParamStringValue'

                      #Calling the method from wifiUtility to execute test case and set result status for the test.
                      tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, "0", getMethod)
                      finalConfigValue = details.split(":")[1].strip()
                      print "finalConfigValue : ", finalConfigValue

                      if expectedresult in actualresult:
                         if finalConfigValue == setConfigValue:
                             tdkTestObj.setResultStatus("SUCCESS");
                             print "TEST STEP : Compare set and get values of ApSecurityMFPConfig"
                             print "EXPECTED RESULT : Set and get values of ApSecurityMFPConfig should be the same"
                             print "ACTUAl RESULT : Set and get values of ApSecurityMFPConfig are the same"
                             print "setApSecurityMFPConfig = ",setConfigValue
                             print "getApSecurityMFPConfig = ",finalConfigValue
                             print "TEST EXECUTION RESULT :SUCCESS"
                         else:
                             tdkTestObj.setResultStatus("FAILURE");
                             print "TEST STEP : Compare set and get values of ApSecurityMFPConfig"
                             print "EXPECTED RESULT : Set and get values of ApSecurityMFPConfig should be the same"
                             print "ACTUAl RESULT : Set and get values of ApSecurityMFPConfig are NOT the same"
                             print "setApSecurityMFPConfig = ",setConfigValue
                             print "getApSecurityMFPConfig = ",finalConfigValue
                             print "TEST EXECUTION RESULT :FAILURE"
                      else:
                          tdkTestObj.setResultStatus("FAILURE")
                          print "wifi_getApSecurityMFPConfig() function failed"

                  else:
                      tdkTestObj.setResultStatus("FAILURE")
                      print "wifi_setApSecurityMFPConfig() function failed";
                  #Revert the ApSecurityMFPConfig value back o initial value
                  print "Reverting Back to initial value"
                  apIndex = idx
                  setMethod = "setApSecurityMFPConfig"
                  primitive = 'WIFIHAL_GetOrSetParamStringValue'
                  #Calling the method from wifiUtility to execute test case and set result status for the test.
                  tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, initialConfigValue, setMethod)
                  if expectedresult in actualresult:
                     tdkTestObj.setResultStatus("SUCCESS")
                     print "Successfully reverted back to initial value"
                  else:
                      tdkTestObj.setResultStatus("FAILURE")
                      print "Unable to revert to initial value"
           else:
               print "initialConfigValue not in mfpConfigValues list"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "wifi_getApSecurityMFPConfig function failed";

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
