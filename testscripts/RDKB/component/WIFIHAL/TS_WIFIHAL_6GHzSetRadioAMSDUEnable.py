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
  <name>TS_WIFIHAL_6GHzSetRadioAMSDUEnable</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_getRadioAMSDUEnable() to get the AMSDU enable status for 6G radio and toggle using wifi_setRadioAMSDUEnable() and verify if the set is getting reflected in the get.</synopsis>
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
    <test_case_id>TC_WIFIHAL_674</test_case_id>
    <test_objective>Invoke the HAL API wifi_getRadioAMSDUEnable() to get the AMSDU enable status for 6G radio and toggle using wifi_setRadioAMSDUEnable() and verify if the set is getting reflected in the get.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioAMSDUEnable()
wifi_setRadioAMSDUEnable()</api_or_interface_used>
    <input_parameters>methodname : getRadioAMSDUEnable
methodname : setRadioAMSDUEnable
radioIndex : 6G radio index
newEnable : 0 or 1</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getRadioAMSDUEnable() and store the initial AMSDU Enable value.
3. Toggle the AMSDU Enable using wifi_setRadioAMSDUEnable(). The SET operation should be success.
4. Invoke the get API wifi_getRadioAMSDUEnable() and check if the SET is reflected in the GET.
5. Revert to initial AMSDU Enable
6. Unload module</automation_approch>
    <expected_output>The HAL API wifi_setRadioAMSDUEnable() should successfully toggle the AMSDU Enable value and the SET should reflect in the GET using the API wifi_getRadioAMSDUEnable().</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetRadioAMSDUEnable</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "6G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetRadioAMSDUEnable');

def RadioAMSDUEnable(methodName,param,idx):
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
    #Giving the method name to invoke the api for getting RadioAMSDU Enable status
    tdkTestObj.addParameter("methodName",methodName);
    tdkTestObj.addParameter("radioIndex",idx);
    tdkTestObj.addParameter("param",param);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return (tdkTestObj, actualresult, details);

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
        methodName = "getRadioAMSDUEnable";
        #Dummy param for get method
        param = 0;
        tdkTestObj, actualresult, details = RadioAMSDUEnable(methodName,param,idx);

        print "\nTEST STEP 1: Get the initial Radio AMSDU Enable status using the HAL API wifi_getRadioAMSDUEnable()";
        print "EXPECTED RESULT 1: The HAL API wifi_getRadioAMSDUEnable() should be invoked successfully";

        if expectedresult in actualresult :
            print "ACTUAL RESULT 1: API invoked successfully; Details : %s" %details;
            print "TEST EXECUTION RESULT :SUCCESS"
            tdkTestObj.setResultStatus("SUCCESS");
            enable = details.split(":")[1].strip();
            print "Initial AMSDU Enable :" ,enable;

            if "Enabled" in enable:
                oldEnable = 1
                newEnable = 0
                newStatus = "Disabled"
            else:
                oldEnable = 0
                newEnable = 1
                newStatus = "Enabled"

            #Toggle the enable status using set
            methodName = "setRadioAMSDUEnable"
            tdkTestObj, actualresult, details = RadioAMSDUEnable(methodName,newEnable,idx);

            print "\nTEST STEP 2: Toggle the radio AMSDU enable status to %s using the HAL API wifi_setRadioAMSDUEnable()" %newStatus;
            print "EXPECTED RESULT 2: The set operation should be success";


            if expectedresult in actualresult :
                print "ACTUAL RESULT 2: Set API returns success; Details : %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS"
                tdkTestObj.setResultStatus("SUCCESS");

                # Get the New AP enable status
                methodName = "getRadioAMSDUEnable";
                #Dummy param for get method
                param = 0;
                tdkTestObj, actualresult, details = RadioAMSDUEnable(methodName,param,idx);

                print "\nTEST STEP 3: Get the current AMSDU Enable status using wifi_setRadioAMSDUEnable()";
                print "EXPECTED RESULT 3: The current AMSDU status should be retrieved successfully";

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: GET API returns success; Details : %s" %details;
                    print "TEST EXECUTION RESULT :SUCCESS"

                    #Check if the SET is reflected in GET
                    getValue = details.split(":")[1].strip();
                    print "\nTEST STEP 4 : Check if the AMDSU enable SET is reflected in the GET";
                    print "EXPECTED RESULT 4 : The AMSDU value SET is reflected in the GET";
                    print "AMSDU value Set : ", newStatus;
                    print "AMSDU value Get : ", getValue;

                    if getValue == newStatus:
                        print "ACTUAL RESULT 4 :The SET value is reflected in GET";
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST EXECUTION RESULT :SUCCESS"

                        #Revert back to original Enable status
                        methodName = "setRadioAMSDUEnable"
                        tdkTestObj, actualresult, details = RadioAMSDUEnable(methodName,oldEnable,idx);
                        print "\nTEST STEP 5 : Revert the enable status to initial value";
                        print "EXPECTED RESULT 5: Revert operation should be success";

                        if expectedresult in actualresult :
                            print "ACTUAL RESULT 5:Enable status reverted back; Details : %s" %details;
                            print "TEST EXECUTION RESULT :SUCCESS"
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "ACTUAL RESULT 5:Enable status not reverted back; Details : %s" %details;
                            print "TEST EXECUTION RESULT :FAILURE"
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "ACTUAL RESULT 4 :The SET value is not reflected in GET";
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST EXECUTION RESULT :FAILURE"
                else:
                    print "ACTUAL RESULT 3: GET API invocation fails after SET API invocation; Details : %s" %details;
                    print "TEST EXECUTION RESULT :FAILURE"
                    tdkTestObj.setResultStatus("FAILURE");
            else :
                print "ACTUAL RESULT 2: Set API returns failure; Details : %s" %details;
                print "TEST EXECUTION RESULT :FAILURE"
                tdkTestObj.setResultStatus("FAILURE");
        else :
            print "ACTUAL RESULT 1: API not invoked successfully; Details : %s" %details;
            print "TEST EXECUTION RESULT :FAILURE"
            tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
