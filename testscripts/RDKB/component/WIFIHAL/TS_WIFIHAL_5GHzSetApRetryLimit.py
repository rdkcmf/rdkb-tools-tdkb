##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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
  <name>TS_WIFIHAL_5GHzSetApRetryLimit</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamUIntValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set and get the ApRetryLimit for 5Ghz</synopsis>
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
    <test_case_id>TC_WIFIHAL_150</test_case_id>
    <test_objective>To set and get the ApRetryLimit for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApRetryLimit()
wifi_setApRetryLimit()</api_or_interface_used>
    <input_parameters>methodName : getApRetryLimit
methodName : setApRetryLimit
radioIndex : 1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamUIntValue invoke wifi_getApRetryLimit()  and get the initial value of retry limit
3. Using  WIFIHAL_GetOrSetParamUIntValue invoke wifi_setApRetryLimit() and set a valid value
4. Using WIFIHAL_GetOrSetParamUIntValue 
 invoke wifi_getApRetryLimit and get the previously set value. 
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
6. Revert the RetryLimit back to initial value
7. Unload wifihal module</automation_approch>
    <except_output>Set and get values of RetryLimit should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetApRetryLimit</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from wifiUtility import *;
import random

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetApRetryLimit');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    apIndex = 1
    getMethod = "getApRetryLimit"
    primitive = 'WIFIHAL_GetOrSetParamUIntValue'

    #Calling the method from wifiUtility to execute test case and set result status for the test.
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

    if expectedresult in actualresult:
        initialRetryLimit = details.split(":")[1].strip()
        r= range(1,int(initialRetryLimit))+range(int(initialRetryLimit)+1,20)
        setRetryLimit = random.choice(r)
        expectedresult="SUCCESS";
        apIndex = 1
        setMethod = "setApRetryLimit"
        primitive = 'WIFIHAL_GetOrSetParamUIntValue'

        #Calling the method from wifiUtility to execute test case and set result status for the test.
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setRetryLimit, setMethod)

        if expectedresult in actualresult:
            expectedresult="SUCCESS";
            apIndex = 1
            getMethod = "getApRetryLimit"
            primitive = 'WIFIHAL_GetOrSetParamUIntValue'

            #Calling the method from wifiUtility to execute test case and set result status for the test.
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)
            finalRetryLimit = details.split(":")[1].strip()

            if expectedresult in actualresult:
                if int(finalRetryLimit) == setRetryLimit:
                    print "TEST STEP : Comparing the set and get values of ApRetryLimit"
                    print "EXPECTED RESULT : Set and get ApRetryLimit should be the same"
                    print "ACTUAL RESULT : Set and get ApRetryLimit are the same"
		    print "Set ApRetryLimit = ",setRetryLimit
		    print "Get ApRetryLimit = ",finalRetryLimit
                    print "TEST EXECUTION RESULT : SUCCESS"
                    tdkTestObj.setResultStatus("SUCCESS");

                else:
                    print "TEST STEP : Comparing the set and get values of ApRetryLimit"
                    print "EXPECTED RESULT : Set and get ApRetryLimit should be the same"
                    print "ACTUAL RESULT : Set and get ApRetryLimit are NOT the same"
		    print "Set ApRetryLimit = ",setRetryLimit
		    print "Get ApRetryLimit = ",finalRetryLimit
                    print "TEST EXECUTION RESULT : FAILURE"
                    tdkTestObj.setResultStatus("FAILURE");

                #Revert back the ApRetryLimit to initial value
                expectedresult="SUCCESS";
                apIndex = 1
                setMethod = "setApRetryLimit"
                setRetryLimit = int(initialRetryLimit)
                primitive = 'WIFIHAL_GetOrSetParamUIntValue'

                #Calling the method from wifiUtility to execute test case and set result status for the test.
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, setMethod)

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Successfully reverted back to default value"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print" Unable to revert to default value"

            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "getApRetryLimit function failed";

        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "setApRetryLimit function failed";

    else:
        print "getApRetryLimit function failed";
        tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

