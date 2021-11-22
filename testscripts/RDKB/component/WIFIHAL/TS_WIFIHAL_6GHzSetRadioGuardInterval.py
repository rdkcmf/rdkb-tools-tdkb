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
  <name>TS_WIFIHAL_6GHzSetRadioGuardInterval</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>8</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_setRadioGuradInterval() and set the intervals ["Auto", "400nsec", "800nsec"] for 6GHz radio and validate the set using the get API wifi_getRadioGuardInterval().</synopsis>
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
    <test_case_id>TC_WIFIHAL_672</test_case_id>
    <test_objective>Invoke the HAL API wifi_setRadioGuradInterval() and set the intervals ["Auto", "400nsec", "800nsec"] for 6GHz radio and validate the set using the get API wifi_getRadioGuardInterval().</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioGuradInterval()
wifi_getRadioGuradInterval()</api_or_interface_used>
    <input_parameters>methodname : setRadioGuradInterval
methodname : getRadioGuardInterval
radioIndex : 6G radio index
setGuardInt : Auto, 400nsec, 800nsec</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getRadioGuradInterval() and retrieve the initial guard interval for 6G radio and store it.
3. Invoke the HAL API wifi_setRadioGuradInterval() to set the Guard interval to Auto, 400nsec, 800nsec sequentially.
4. After each set invoke wifi_getRadioGuradInterval() to check if the SET is reflected in the GET.
5. Revert to initial guard interval value.
6. Unload the module</automation_approch>
    <expected_output>The HAL API wifi_setRadioGuradInterval should set the Guard Interval to Auto, 400nsec and 800nsec successfully for 6G radio and the set guard interval should reflect in the get API, wifi_getRadioGuradInterval().</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetRadioGuardInterval</test_script>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetRadioGuardInterval');

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
        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
        tdkTestObj.addParameter("methodName","getRadioGuardInterval");
        tdkTestObj.addParameter("radioIndex",idx);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 1: Invoke the HAL API wifi_getRadioGuardInterval() for 6GHz radio";
        print "EXPECTED RESULT 1 : The API should be invoked successfully";

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            initialGuardInt = details.split(":")[1].strip("nsec");
            print "ACTUAL RESULT 1 : The API was invoked successfully; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            if (initialGuardInt == "Auto" or (initialGuardInt.isdigit() and (100 <= int(initialGuardInt) <= 800))):
                tdkTestObj.setResultStatus("SUCCESS");
                print "Initial Guard Interval : %s" %initialGuardInt;
                #Possible guard interval values to set
                possibleGuardInt = ["400nsec", "800nsec", "Auto"];
                step = 1;

                for setGuardInt in possibleGuardInt:
                    step = step + 1;
                    print "\nSetting Guard Interval to : %s" %setGuardInt;
                    #Script to load the configuration file of the component
                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                    tdkTestObj.addParameter("methodName","setRadioGuardInterval");
                    tdkTestObj.addParameter("radioIndex",idx);
                    tdkTestObj.addParameter("param",setGuardInt);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    print "\nTEST STEP %d : Set the guard interval to %s using the HAL API wifi_setRadioGuradInterval()" %(step,setGuardInt);
                    print "EXPECTED RESULT %d : The guard interval should be set successfully" %step;

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : Set operation success; Details : %s" %(step,details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #cross check the set with get
                        step = step + 1;
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                        tdkTestObj.addParameter("methodName","getRadioGuardInterval");
                        tdkTestObj.addParameter("radioIndex",idx);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        print "\nTEST STEP %d: Check if the guard interval set is reflected in the get" %step;
                        print "EXPECTED RESULT %d : The guard interval set should be reflected in the get" %step;

                        if expectedresult in actualresult:
                            finalGuardInt = details.split(":")[1];
                            print "Set Value : %s" %setGuardInt;
                            print "Get Value : %s" %finalGuardInt

                            if finalGuardInt == setGuardInt:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d : Set reflected in Get" %step;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d : Set not reflected in Get" %step;
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d : wifi_getRadioGuardInterval failed after set" %step;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : Set operation failed; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Initial Guard Interval : %s is not a valid value" %initialGuardInt;

            #Revert operation
            if finalGuardInt != initialGuardInt:
                print "\nReverting Guard Interval to : %s" %initialGuardInt;
                #Script to load the configuration file of the component
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
                tdkTestObj.addParameter("methodName","setRadioGuardInterval");
                tdkTestObj.addParameter("radioIndex",idx);
                tdkTestObj.addParameter("param",initialGuardInt);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Guard interval reveted to initial value successfully";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Guard interval is not reverted back to initial value";
            else:
                print "Revert operation is not required";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1 : The API was not invoked successfully; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
