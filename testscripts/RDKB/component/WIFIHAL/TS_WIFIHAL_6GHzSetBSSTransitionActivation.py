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
  <version>1</version>
  <name>TS_WIFIHAL_6GHzSetBSSTransitionActivation</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check the set and get BSSTransitionActivation    for 6GHz radio using the HAL APIs wifi_setBSSTransitionActivation() and wifi_getBSSTransitionActivation().</synopsis>
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
    <test_case_id>TC_WIFIHAL_651</test_case_id>
    <test_objective>To check the set and get BSSTransitionActivation    for 6GHz radio using the HAL APIs wifi_setBSSTransitionActivation() and wifi_getBSSTransitionActivation().</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getBSSTransitionActivation()
wifi_setBSSTransitionActivation()</api_or_interface_used>
    <input_parameters>methodname : getBSSTransitionActivation
methodname : setBSSTransitionActivation
apIndex : fetched from the platform property file</input_parameters>
    <automation_approch>1.Load the module.
2. Get the 6GHz access point index from the platform property file.
3.Get the BSSTransitionActivation using   wifi_getBSSTransitionActivation() API and store the value .
4.Toggle its value using wifi_setBSSTransitionActivation()
5.Check for successful set using wifi_getBSSTransitionActivation()
6. Revert the value to initial
7.Unload module.</automation_approch>
    <expected_output>The BSS Transition Activation should be toggled successfully using the HAL API wifi_setBSSTransitionActivation() and it should get reflected in wifi_getBSSTransitionActivation() for 6GHz.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetBSSTransitionActivation</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetBSSTransitionActivation');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetBSSTransitionActivation');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    expectedresult = "SUCCESS";
    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

    if apIndex == -1:
        print "Failed to get the Access Point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        getMethod = "getBSSTransitionActivation"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            initialValue = details.split(":")[1].strip()

            if initialValue == "Enabled" :
                #value to revert
                revertValue = 1
                setValue = 0
                checkValue = "Disabled"
            else:
                revertValue = 0
                setValue = 1
                checkValue = "Enabled"

            setMethod = "setBSSTransitionActivation"
            primitive = 'WIFIHAL_GetOrSetParamIntValue'
            #Toggle the enable status using set
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setValue, setMethod)

            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "Enable state toggled using set"
                #Get the New enable status

                getMethod = "getBSSTransitionActivation"
                primitive = 'WIFIHAL_GetOrSetParamBoolValue'
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)
                getValue = details.split(":")[1].strip()
                print "getValue:",getValue

                if expectedresult in actualresult and checkValue == getValue  :
                    print "getBSSTransitionActivation Success, verified along with setBSSTransitionActivation() api"
                    #Revert back to original Enable status

                    setMethod = "setBSSTransitionActivation"
                    primitive = 'WIFIHAL_GetOrSetParamIntValue'
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, revertValue, setMethod)

                    if expectedresult in actualresult :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Reverted Successfully";
                    else:
                        print "Revert operation failed"
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    print "getBSSTransitionActivation() failed after set function"
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "setBSSTransitionActivation() failed"
                tdkTestObj.setResultStatus("FAILURE");
        else:
            print "getBSSTransitionActivation() failed"
            tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

