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
  <name>TS_WIFIHAL_5GHzSetBSSTransitionActivation</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To toggle the BSS transition status using wifi_setBSSTransitionActivation()</synopsis>
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
    <test_case_id>TC_WIFIHAL_361</test_case_id>
    <test_objective>To check the set and get functionality for BSSTransitionActivation</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getBSSTransitionImplemented
wifi_setBSSTransitionImplemented</api_or_interface_used>
    <input_parameters>methodName :'WIFIHAL_GetOrSetParamBoolValue
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the module.
2.Get the getBSSTransitionActivation  using   wifi_getBSSTransitionActivation API and store the value .
3.Toggle its value using wifi_setBSSTransitionActivation
4.Check for succesful set using wifi_getBSSTransitionActivation
5. Revert the value to initial
6.Unload module.</automation_approch>
    <expected_output>The toggled value should be set successfully</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetBSSTransitionActivation</test_script>
    <skipped>No</skipped>
    <release_version>M73</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
revertValue = 0
setValue = 0
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
radio = "5G"
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetBSSTransitionActivation');

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

        expectedresult="SUCCESS";
        radioIndex = idx
        getMethod = "getBSSTransitionActivation"
        primitive = 'WIFIHAL_GetOrSetParamBoolValue'
        #Getting the default enable mode
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)

        if expectedresult in actualresult :
           tdkTestObj.setResultStatus("SUCCESS");
           initialValue = details.split(":")[1].strip()
           if initialValue == "TRUE" :
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
           tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setValue, setMethod)

           if expectedresult in actualresult :
              tdkTestObj.setResultStatus("SUCCESS");
              print "Enable state toggled using set"
              #Get the New enable status
              getMethod = "getBSSTransitionActivation"
              primitive = 'WIFIHAL_GetOrSetParamBoolValue'
              tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
              getValue = details.split(":")[1].strip()
              print "value Set is : ",getValue

              if expectedresult in actualresult and checkValue == getValue :
                 print "getBSSTransitionActivation Success, verified along with setRadioDCSEnable() api"
                 #Revert back to original Enable status
		 setMethod = "setBSSTransitionActivation"
		 primitive = 'WIFIHAL_GetOrSetParamIntValue'
                 tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, revertValue, setMethod)

                 if expectedresult in actualresult :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Enable status reverted back";
                 else:
                     print "Couldn't revert enable status"
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

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");




