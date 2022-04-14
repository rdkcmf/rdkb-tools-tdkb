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
  <name>TS_WIFIHAL_5GHzPushApFastTransitionConfig</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_PushApFastTransitionConfig</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_pushApFastTransitionConfig() for 5G private AP and set the BSS Transition Support, Mobility Domain ID and FT Over DS Activated enable state to new values and cross check if the values set using the Push API is reflected in wifi_getBSSTransitionActivated(), wifi_getFTMobilityDomainID() and wifi_getFTOverDSActivated() HAL APIs.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIHAL_786</test_case_id>
    <test_objective>Invoke the HAL API wifi_pushApFastTransitionConfig() for 5G private AP and set the BSS Transition Support, Mobility Domain ID and FT Over DS Activated enable state to new values and cross check if the values set using the Push API is reflected in wifi_getBSSTransitionActivated(), wifi_getFTMobilityDomainID() and wifi_getFTOverDSActivated() HAL APIs.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_pushApFastTransitionConfig()
wifi_getBSSTransitionActivated()
wifi_getFTMobilityDomainID()
wifi_getFTOverDSActivated()</api_or_interface_used>
    <input_parameters>apIndex : 5G private AP index
radioIndex : 5G radio index
methodName : getBSSTransitionActivated
methodName : getFTMobilityDomainID
methodName : getFTOverDSActivated
support : BSS Transition activated enabled/disabled(1/0)
mobilityDomain : Mobility Domain ID dynamically generated
overDS : FT Over DS Activated Enabled/Disabled(1/0)</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL APIs wifi_getBSSTransitionActivated(), wifi_getFTMobilityDomainID() and wifi_getFTOverDSActivated() to retrieve the initial values of BSS Transition activated, Mobility Domain ID and FT Over DS Activated.
3. Invoke the HAL API wifi_pushApFastTransitionConfig() to set BSS Transition activated, Mobility Domain ID and FT Over DS Activated to new values.
4. Check if the API returns success.
5. If the Push API returns success, invoke the APIs wifi_getBSSTransitionActivated(), wifi_getFTMobilityDomainID() and wifi_getFTOverDSActivated() to retrieve the current values.
6. Check if the GET values match with values SET using the Push API.
7. Revert to initial state.
8. Unload the module.</automation_approch>
    <expected_output>The HAL API wifi_pushApFastTransitionConfig() for 5G private AP to set the BSS Transition Support, Mobility Domain ID and FT Over DS Activated enable state to new values should be invoked successfully and the values set using the Push API should be reflected in wifi_getBSSTransitionActivated(), wifi_getFTMobilityDomainID() and wifi_getFTOverDSActivated() HAL APIs.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPushApFastTransitionConfig</test_script>
    <skipped>No</skipped>
    <release_version>M100</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def getApFTValues(obj, primitive, idx, api, step):
    expectedresult = "SUCCESS";
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("methodName", api);

    if api == "getFTMobilityDomainID":
        tdkTestObj.addParameter("apIndex", idx);
    else:
        tdkTestObj.addParameter("radioIndex", idx);

    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d : Invoke the HAL API wifi_%s and get the FT parameter value for 5G private AP" %(step, api);
    print "EXPECTED RESULT %d : Invocation of wifi_%s should be success" %(step, api);

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: API was invoked successfully; Details : %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else :
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: API was NOT invoked successfully; Details : %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return actualresult, details, tdkTestObj;

def HextoIntConversion(hex_value0, hex_value1):
    #Covert the Hex value to corresponding integer value
    hex0 = hex_value0.split("0x")[1];
    hex1 = hex_value1.split("0x")[1];

    #Ensure that 0xf is considered as 0x0f
    if len(hex0) == 1:
        hex0 = "0" + hex0;
    if len(hex1) == 1:
        hex1 = "0" + hex1;

    #Concatenate the two Hex parts to get the full hex value
    hex_value = hex1 + hex0;
    mobility_id = int(hex_value, 16);
    print "\nThe Hex value after combining the Mobility Domain IDs is : 0x%s" %hex_value;
    return mobility_id;

def PushApFTConfig(tdkTestObj, apIndex, setvalues, radioIndex):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("apIndex", apIndex);
    tdkTestObj.addParameter("support", setvalues[0]);
    tdkTestObj.addParameter("mobilityDomain", setvalues[1]);
    tdkTestObj.addParameter("overDS", setvalues[2]);
    tdkTestObj.addParameter("radioIndex", radioIndex);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult, details;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from random import randint;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPushApFastTransitionConfig');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the initial value of BSSTransitionActivated
        step = 1;
        primitive = "WIFIHAL_GetOrSetParamBoolValue";
        api = "getBSSTransitionActivated";
        actualresult, details, tdkTestObj = getApFTValues(obj, primitive, idx, api, step);

        if expectedresult in actualresult and details != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            initial_bss_transition_activated = details.split(":")[1].strip();
            print "Initial BSS Transition Activated : %s" %initial_bss_transition_activated;

            #Get the initial value of FTMobilityDomainID
            step = step + 1;
            primitive = "WIFIHAL_GetOrSetFTMobilityDomainID";
            api = "getFTMobilityDomainID";
            actualresult, details, tdkTestObj = getApFTValues(obj, primitive, idx, api, step);

            if expectedresult in actualresult and details != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");

                #Check if proper Hex values are retrieved and convert them to integer value
                hex_value0 = details.split("ID[0] : ")[1].split(",")[0];
                hex_value1 = details.split("ID[1] : ")[1];
                print "Mobility Domain ID[0] : %s" %hex_value0;
                print "Mobility Domain ID[1] : %s" %hex_value1;

                if "0x" in hex_value0 and "0x" in hex_value1:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    #Covert to corresponding Integer values
                    initial_FTMDID = HextoIntConversion(hex_value0, hex_value1);
                    print "Initial FT Mobility Domain ID : %d" %initial_FTMDID;

                    #Get the initial value of FTOverDSActivated
                    step = step + 1;
                    primitive = "WIFIHAL_GetOrSetParamBoolValue";
                    api = "getFTOverDSActivated";
                    actualresult, details, tdkTestObj = getApFTValues(obj, primitive, idx, api, step);

                    if expectedresult in actualresult and details != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        initial_ft_over_ds = details.split(":")[1].strip();
                        print "Initial FT Over DS Activated : %s" %initial_ft_over_ds;

                        #Invoke the PushApFastTransitionConfig API
                        step = step + 1;

                        #Toggle the BSS transition activated(BSS Support)
                        if initial_bss_transition_activated == "Enabled":
                            bss_old_enable = 1;
                            bss_new_enable = 0;
                            bss_new_status = "Disabled";
                        else:
                            bss_old_enable = 0;
                            bss_new_enable = 1;
                            bss_new_status = "Enabled";

                        #New FT MobilityDomain ID
                        new_ft_mobility = randint(0, 10000);

                        #Toggle the FT over DS Activated
                        if initial_ft_over_ds == "Enabled":
                            overDS_old_enable = 1;
                            overDS_new_enable = 0;
                            overDS_new_status = "Disabled";
                        else:
                            overDS_old_enable = 0;
                            overDS_new_enable = 1;
                            overDS_new_status = "Enabled";

                        apIndex = idx;
                        radioIndex = idx;
                        setvalues = [bss_new_enable, new_ft_mobility, overDS_new_enable];
                        print "New FT Values to be set for BSS TransitionActivated : %s, FT Mobility Domain ID : %d, FT Over DS Activated : %s"	%(bss_new_status, new_ft_mobility, overDS_new_status);
                        tdkTestObj = obj.createTestStep("WIFIHAL_PushApFastTransitionConfig");
                        actualresult, details = PushApFTConfig(tdkTestObj, apIndex, setvalues, radioIndex);

                        print "\nTEST STEP %d: Invoke the HAL API wifi_PushApFastTransitionConfig() for 5G private AP" %step;
                        print "EXPECTED RESULT %d: The HAL API should be invoked successfully" %step;

                        if expectedresult in actualresult and details != "":
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: API was invoked successfully; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Cross check the PUSH operation using the GET APIs
                            #Get the final value of BSSTransitionActivated
                            step = step + 1;
                            primitive = "WIFIHAL_GetOrSetParamBoolValue";
                            api = "getBSSTransitionActivated";
                            actualresult, details, tdkTestObj = getApFTValues(obj, primitive, idx, api, step);

                            if expectedresult in actualresult and details != "":
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                final_bss_transition_activated = details.split(":")[1].strip();
                                print "Final BSS Transition Activated : %s" %final_bss_transition_activated;

                                #Get the final value of FTMobilityDomainID
                                step = step + 1;
                                primitive = "WIFIHAL_GetOrSetFTMobilityDomainID";
                                api = "getFTMobilityDomainID";
                                actualresult, details, tdkTestObj = getApFTValues(obj, primitive, idx, api, step);

                                if expectedresult in actualresult and details != "":
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");

                                    #Check if proper Hex values are retrieved and convert them to integer value
                                    hex_value0 = details.split("ID[0] : ")[1].split(",")[0];
                                    hex_value1 = details.split("ID[1] : ")[1];
                                    print "Mobility Domain ID[0] : %s" %hex_value0;
                                    print "Mobility Domain ID[1] : %s" %hex_value1;

                                    if "0x" in hex_value0 and "0x" in hex_value1:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        #Covert to corresponding Integer values
                                        final_FTMDID = HextoIntConversion(hex_value0, hex_value1);
                                        print "Final FT Mobility Domain ID : %d" %final_FTMDID;

                                        #Get the final value of FTOverDSActivated
                                        step = step + 1;
                                        primitive = "WIFIHAL_GetOrSetParamBoolValue";
                                        api = "getFTOverDSActivated";
                                        actualresult, details, tdkTestObj = getApFTValues(obj, primitive, idx, api, step);

                                        if expectedresult in actualresult and details != "":
                                            #Set the result status of execution
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            final_ft_over_ds = details.split(":")[1].strip();
                                            print "Final FT Over DS Activated : %s" %final_ft_over_ds;

                                            #Check if GET values match with SET values
                                            step = step + 1;
                                            print "\nTEST STEP %d: Check if GET values of FT parameters match with the SET values" %step;
                                            print "EXPECTED RESULT %d : The GET values should match with the SET values" %step;
                                            print "BSS Transition Activated SET : ", bss_new_status;
                                            print "BSS Transition Activated GET : ", final_bss_transition_activated;
                                            print "FT Mobility Domain ID SET : ", new_ft_mobility;
                                            print "FT Mobility Domain ID GET : ", final_FTMDID;
                                            print "FT Over DS Activated SET : ", overDS_new_status;
                                            print "FT Over DS Activated GET : ", final_ft_over_ds;

                                            if (bss_new_status == final_bss_transition_activated) and (new_ft_mobility == final_FTMDID) and (overDS_new_status == final_ft_over_ds) :
                                                tdkTestObj.setResultStatus("SUCCESS");
                                                print "ACTUAL RESULT %d: GET values match with SET values" %step;
                                                print "[TEST EXECUTION RESULT] : SUCCESS";
                                            else:
                                                tdkTestObj.setResultStatus("FAILURE");
                                                print "ACTUAL RESULT %d: GET values does NOT match with SET values" %step;
                                                print "[TEST EXECUTION RESULT] : FAILURE";
                                        else:
                                            #Set the result status of execution
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "Final FT Over DS Activated value not retrieved";
                                    else:
                                        #Set the result status of execution
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "FT Mobility Domain ID is not retrieved as two Hex values";
                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "Final FT Mobility Domain ID value not retrieved";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "Final BSS Transition Activated value not retrieved";

                            #Revert operation
                            step = step + 1;
                            setvalues = [bss_old_enable, initial_FTMDID, overDS_old_enable];
                            print "Revert FT values:- BSS TransitionActivated : %s, FT Mobility Domain ID : %d, FT Over DS Activated : %s"	%(initial_bss_transition_activated, initial_FTMDID, initial_ft_over_ds);
                            tdkTestObj = obj.createTestStep("WIFIHAL_PushApFastTransitionConfig");
                            actualresult, details = PushApFTConfig(tdkTestObj, apIndex, setvalues, radioIndex);

                            print "\nTEST STEP %d: Invoke the HAL API wifi_PushApFastTransitionConfig() for 5G private AP and revert to initial state" %step;
                            print "EXPECTED RESULT %d: The HAL API should be invoked successfully" %step;

                            if expectedresult in actualresult and details != "":
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: Revert operation success; Details : %s" %(step, details);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";
                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: Revert operation failed; Details : %s" %(step, details);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: API was not invoked successfully; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Initial FT Over DS Activated value not retrieved";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "FT Mobility Domain ID is not retrieved as two Hex values";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "Initial FT Mobility Domain ID value not retrieved";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "Initial BSS Transition Activated value not retrieved";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
