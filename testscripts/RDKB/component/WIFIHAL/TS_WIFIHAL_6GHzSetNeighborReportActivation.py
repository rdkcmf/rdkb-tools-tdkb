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
  <version>2</version>
  <name>TS_WIFIHAL_6GHzSetNeighborReportActivation</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_setNeighborReportActivation() to toggle the Neighbor Report Activation enable state from initial value and cross check if the value set is getting reflected in wifi_getNeighborReportActivation() for 6GHz radio private AP.</synopsis>
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
    <test_case_id>TC_WIFIHAL_716</test_case_id>
    <test_objective>Invoke the HAL API wifi_setNeighborReportActivation() to toggle the Neighbor Report Activation enable state from initial value and cross check if the value set is getting reflected in wifi_getNeighborReportActivation() for 6GHz radio private AP.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setNeighborReportActivation()
wifi_getNeighborReportActivation()</api_or_interface_used>
    <input_parameters>methodname : getNeighborReportActivation
methodname : setNeighborReportActivation
radioIndex : 6G Private AP index
param : 0 or 1</input_parameters>
    <automation_approch>1. Load the wifihal module.
2. Invoke the HAL API wifi_getNeighborReportActivation() with 6G radio index and get the initial enable state and save it.
3. Invoke the HAL API wifi_setNeighborReportActivation() and toggle the enable set.
4. Invoke wifi_getNeighborReportActivation() to cross check if the enable state is toggled properly.
5. Revert to initial state
6. Unload the module</automation_approch>
    <expected_output>The HAL API wifi_setNeighborReportActivation() should successfully toggle the Neighbor Report Activation enable set and it should be reflected in wifi_getNeighborReportActivation() for 6G radio private AP index.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzSetNeighborReportActivation</test_script>
    <skipped>No</skipped>
    <release_version>M97</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
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
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetNeighborReportActivation');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzSetNeighborReportActivation');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);
    if apIndex == -1:
        print "Failed to get the Access Point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the initial value
        print "\nTEST STEP 1: Invoke the wifi_getNeighborReportActivation API to get the initial enable state of neighbor report activation";
        print "EXPECTED RESULT 1:Invocation of wifi_getNeighborReportActivation should be success";
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
        tdkTestObj.addParameter("methodName","getNeighborReportActivation")
        tdkTestObj.addParameter("radioIndex", apIndex)
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: Invocation of wifi_getNeighborReportActivation was success. Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            enable = details.split(":")[1].strip()
            print "\nInitial enable status is : %s" %enable;

            if "Enabled" in enable:
                oldEnable = 1
                newEnable = 0
                newStatus = "Disabled"
            else:
                oldEnable = 0
                newEnable = 1
                newStatus = "Enabled"

            #Toggle the enable state
            print "\nTEST STEP 2: Toggle the enabled state using wifi_setNeighborReportActivation() HAL API";
            print "EXPECTED RESULT 2: wifi_setNeighborReportActivation should successfully toggle Neighbor Report Activation Enable status to ",newStatus ;
            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
            tdkTestObj.addParameter("methodName","setNeighborReportActivation")
            tdkTestObj.addParameter("radioIndex", apIndex)
            tdkTestObj.addParameter("param", newEnable)
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2:  Set operation was success; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Cross check the enable SET with enable GET
                print "\nTEST STEP 3: Invoke  wifi_getNeighborReportActivation to verify toggling done by wifi_setNeighborReportActivation api";
                print "EXPECTED RESULT 3: wifi_getNeighborReportActivation should be invoked successfully after the set operation";
                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                tdkTestObj.addParameter("methodName","getNeighborReportActivation")
                tdkTestObj.addParameter("radioIndex", apIndex)
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: Invocation of wifi_getNeighborReportActivation was success. Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    new_enable = details.split(":")[1].strip();

                    print "\nTEST STEP 4 : Verify if Neighbor Report Activation set value and get value are same";
                    print "EXPECTED RESULT 4 : The set and get values should match";
                    print "Enable SET : ",newStatus;
                    print "Enable GET : ",new_enable;

                    if new_enable == newStatus :
                        print "ACTUAL RESULT 4:  The SET matches with GET";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        tdkTestObj.setResultStatus("SUCCESS");

                        #Revert Neighbor Report Activation to initial value
                        print "\nTEST STEP 5: Revert the enabled state using NeighborReportActivation API";
                        print "EXPECTED RESULT 5: wifi_setNeighborReportActivation should successfully revert Neighbor Report Activation status";
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                        tdkTestObj.addParameter("methodName","setNeighborReportActivation")
                        tdkTestObj.addParameter("radioIndex", apIndex)
                        tdkTestObj.addParameter("param", oldEnable)
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 5: Revert operation was success; Details : %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 5: Revert operation failed; Details : %s" %details;
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        print "ACTUAL RESULT 4: API invocation failed; Details : %s" %details;
                        tdkTestObj.setResultStatus("FAILURE");
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: API invocation failed; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: API invocation failed; Details : %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: API invocation failed; Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
