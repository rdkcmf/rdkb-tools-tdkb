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
  <name>TS_WIFIHAL_SetBandSteeringEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To enable/disable the band steering</synopsis>
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
    <test_case_id>TC_WIFIHAL_143</test_case_id>
    <test_objective>To enable/disable the BandSteering</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getBandSteeringCapability()
wifi_getBandSteeringEnable()
wifi_setBandSteeringEnable()
</api_or_interface_used>
    <input_parameters>methodName : getBandSteeringCapability
methodName : getBandSteeringEnable
methodName : setBandSteeringEnable

</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using WIFIHAL_GetOrSetParamBoolValue invoke wifi_getBandSteeringCapability() to see if the BandSteering Capability is available or not. If available proceed to next step, else return SUCCESS and exit. 
3. Using  WIFIHAL_GetOrSetParamBoolValue invoke wifi_getBandSteeringEnable()
4. Depending upon the value retrieved from previous step, toggle the enable status using wifi_setBandSteeringEnable.
5. Invoke wifi_getBandSteeringEnable() to get the previously set value. 
6. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
7. Revert the BandSteeringEnable status back to initial value
8. Unload wifihal module</automation_approch>
    <except_output>Set and get values of BandSteeringEnable  should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_SetBandSteeringEnable</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_SetBandSteeringEnable');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    expectedresult="SUCCESS";
    getMethod = "getBandSteeringCapability"
    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, 0, 0, getMethod)

    if expectedresult in actualresult:
        enable = details.split(":")[1].strip()
        tdkTestObj.setResultStatus("SUCCESS");
        if "Enabled" in enable:

            getMethod = "getBandSteeringEnable"
            primitive = 'WIFIHAL_GetOrSetParamBoolValue'
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, 0, 0, getMethod)
            enable = details.split(":")[1].strip()

            if expectedresult in actualresult:
        	if "Enabled" in enable:
            	    oldEnable = 1
            	    newEnable = 0
        	else:
                    oldEnable = 0
            	    newEnable = 1

                setMethod = "setBandSteeringEnable"
                primitive = 'WIFIHAL_GetOrSetParamBoolValue'
                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, 0, newEnable, setMethod)

                if expectedresult in actualresult:
                    getMethod = "getBandSteeringEnable"
                    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, 0, 0, getMethod)

                    if expectedresult in actualresult and enable not in details.split(":")[1].strip():
                        tdkTestObj.setResultStatus("SUCCESS");
			print "setBandSteeringEnable() success and verified using getBandSteeringEnable()"
                        finalGetValue = details.split(":")[1].strip()

                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "getBandSteeringEnable() call failed after set operation"

                    #Revert back to initial value
                    setMethod = "setBandSteeringEnable"
                    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
                    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, 0, oldEnable, setMethod)

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "Successfully reverted back to inital value"
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Unable to revert to initial value"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "setBandSteeringEnable() call failed"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "getBandSteeringEnable() call failed"
        else:
            tdkTestObj.setResultStatus("SUCCESS");
            print "BandSteeringCapability is disabled"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "getBandSteeringCapability() call failed"
    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");

