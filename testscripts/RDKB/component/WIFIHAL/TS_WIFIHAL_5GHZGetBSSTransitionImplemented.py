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
  <name>TS_WIFIHAL_5GHZGetBSSTransitionImplemented</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To verify wether the BSSTransitionImplemented using using wifi_getBSSTransitionImplemented()</synopsis>
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
    <test_case_id>TC_WIFIHAL_359</test_case_id>
    <test_objective>To check for the whether GetBSSTransition is Implemented in the device</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wif_getBSSTransitionImplemented</api_or_interface_used>
    <input_parameters>methodName :'WIFIHAL_GetBSSTransitionImplemented
radioIndex : 1</input_parameters>
    <automation_approch>1.Load the module.
2.Get the getBSSTransitionImplemented using   wifi_getBSSTransitionImplemented API.
3. Get the  IS_BTM_CAPABLE value from platform properties file.
4.Compare the value from api and from the value received from properties file.
4.Return SUCCESS for non empty value,else FAILURE.
5.Unload module.</automation_approch>
    <expected_output>The value form api  and the one got from platfrom properties value should be same.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHZGetBSSTransitionImplemented</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
import tdkutility
from tdkutility import *
radio = "5G"
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with corresponding Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHZGetBSSTransitionImplemented');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHZGetBSSTransitionImplemented');
#Get the result of connection with test component and STB

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:

        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
        expectedresult="SUCCESS";
        #Getting  IS_BTM_CAPABLE value from tdk_platform_properties"
        cmd= "sh %s/tdk_utility.sh parseConfigFile BTM_CAPABILITY" %TDK_PATH;
        print cmd;
        expectedresult="SUCCESS";
        tdkTestObj.addParameter("command",cmd);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        platformValue = tdkTestObj.getResultDetails().strip().replace("\\n", "");
        print "IS_BTM_CAPABLE :",platformValue
        if expectedresult in actualresult and platformValue!= "":
           #Prmitive test case which is associated to this Script
           tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetParamBoolValue');
           tdkTestObj.addParameter("methodName","getBSSTransitionImplemented");
           tdkTestObj.addParameter("radioIndex", 1);
           expectedresult="SUCCESS";
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
           details = details.split(':')[1].strip();
           print "Details : ",details
           if expectedresult in actualresult and platformValue == details:
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP :check whether wifi_getBSSTransitionImplemented() returns the BSS capability of device"
              print "EXPECTED RESULT : Should check wether the BSSTransition Implemented "
              print "ACTUAL RESULT : BSSTransition Implemented in the device"
              print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP : check whether wifi_getBSSTransitionImplemented() returns the BSS capability of device"
               print "EXPECTED RESULT : Should check wether the BSSTransition Implemented "
               print "ACTUAL RESULT : difference in api return and property file entry"
               print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : get BSS capability from property file"
            print "ACTUAL RESULT : BSS capability from property file :",platformValue
            #Get the result of execution
            print "[TEST EXECUTION RESULT] :FAILURE";
    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";




