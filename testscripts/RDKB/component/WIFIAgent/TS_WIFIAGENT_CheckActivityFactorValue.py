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
  <version>4</version>
  <name>TS_WIFIAGENT_CheckActivityFactorValue</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the Activity Factor parameter, Device.WiFi.Radio.{i}.Stats.X_RDKCENTRAL-COM_AF is equal to the sum of the Tx channel utilization parameter Device.WiFi.Radio.{i}.Stats.X_RDKCENTRAL-COM_AFTX and Rx channel utilization parameter Device.WiFi.Radio.{i}.Stats.X_RDKCENTRAL-COM_AFRX</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_144</test_case_id>
    <test_objective>To check if the Activity Factor parameter, Device.WiFi.Radio.{i}.Stats.X_RDKCENTRAL-COM_AF is equal to the sum of the Tx channel utilization parameter Device.WiFi.Radio.{i}.Stats.X_RDKCENTRAL-COM_AFTX and Rx channel utilization parameter Device.WiFi.Radio.{i}.Stats.X_RDKCENTRAL-COM_AFRX</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.WiFi.Radio.1.Stats.X_RDKCENTRAL-COM_AF
ParamName : Device.WiFi.Radio.2.Stats.X_RDKCENTRAL-COM_AF
ParamName : Device.WiFi.Radio.1.Stats.X_RDKCENTRAL-COM_AFRX
ParamName : Device.WiFi.Radio.2.Stats.X_RDKCENTRAL-COM_AFRX
ParamName : Device.WiFi.Radio.1.Stats.X_RDKCENTRAL-COM_AFTX
ParamName : Device.WiFi.Radio.2.Stats.X_RDKCENTRAL-COM_AFTX</input_parameters>
    <automation_approch>1. Load the modules.
2. Get the value of Activity Factor(TX) from Device.WiFi.Radio.1.Stats.X_RDKCENTRAL-COM_AFTX and Activity Factor(RX) from Device.WiFi.Radio.1.Stats.X_RDKCENTRAL-COM_AFRX and compute their sum.
4. The sum calculated should be equal to the total  Activity Factor Device.WiFi.Radio.1.Stats.X_RDKCENTRAL-COM_AF.
5. Compute the sum and check the same condition for Device.WiFi.Radio.2.Stats.X_RDKCENTRAL-COM_AFTX and Device.WiFi.Radio.2.Stats.X_RDKCENTRAL-COM_AFRX with Device.WiFi.Radio.2.Stats.X_RDKCENTRAL-COM_AF
6. Unload the modules</automation_approch>
    <expected_output>The Activity Factor parameter, Device.WiFi.Radio.{i}.Stats.X_RDKCENTRAL-COM_AF should be  equal to the sum of the Tx channel utilization parameter Device.WiFi.Radio.{i}.Stats.X_RDKCENTRAL-COM_AFTX and Rx channel utilization parameter Device.WiFi.Radio.{i}.Stats.X_RDKCENTRAL-COM_AFRX</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckActivityFactorValue</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckActivityFactorValue');

#Get Module loading status
loadmodulestatus = obj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");

    step = 1;
    for index in range(1,3):
        print "\n***************For radio index : %d*********************" %index;
        print "\nGet the value of Device.WiFi.Radio.%d.Stats.X_RDKCENTRAL-COM_AFTX - Tx Channel Utilization of Self BSS use in units of percentage" %index;
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        param = "Device.WiFi.Radio." + str(index) + ".Stats.X_RDKCENTRAL-COM_AFTX";
        tdkTestObj.addParameter("ParamName",param);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP %d: Get the Tx Channel Utilitization of Self BSS from %s" %(step,param);
        print "EXPECTED RESULT %d: Should get the value of %s" %(step,param);
        print "Details : %s" %details;

        if expectedresult in actualresult and details != "":
            ActivityFactor_TX = int(details);
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: The value is : %d" %(step,ActivityFactor_TX);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            step = step + 1;
            print "\nGet the value of Device.WiFi.Radio.%d.Stats.X_RDKCENTRAL-COM_AFRX - Rx Channel Utilization of Self BSS use in units of percentage" %index;
            param = "Device.WiFi.Radio." + str(index) + ".Stats.X_RDKCENTRAL-COM_AFRX";
            tdkTestObj.addParameter("ParamName",param);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP %d: Get the Rx Channel Utilitization of Self BSS from %s" %(step,param);
            print "EXPECTED RESULT %d: Should get the value of %s" %(step,param);
            print "Details : %s" %details;

            if expectedresult in actualresult and details != "":
                ActivityFactor_RX = int(details);
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: The value is : %d" %(step,ActivityFactor_RX);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                step = step + 1;
                print "\nGet the value of Device.WiFi.Radio.%d.Stats.X_RDKCENTRAL-COM_AF - Percentage of time that the radio was transmitting or receiving Wi-Fi packets" %index;
                param = "Device.WiFi.Radio." + str(index) + ".Stats.X_RDKCENTRAL-COM_AF";
                tdkTestObj.addParameter("ParamName",param);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP %d: Get the Activity Factor from %s" %(step,param);
                print "EXPECTED RESULT %d: Should get the value of %s" %(step,param);
                print "Details : %s" %details;

                if expectedresult in actualresult and details != "":
                    ActivityFactor = int(details);
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: The value is : %d" %(step,ActivityFactor);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    step = step + 1;
                    #Check if the Activity Factor is equal to the sum of Tx + Rx Channel utilizations
                    calculated_AF = ActivityFactor_TX + ActivityFactor_RX;
                    print "\nTEST STEP %d: Check if the Activity Factor retrieved is equal to the sum of Tx and Rx Channel utilizations" %(step);
                    print "EXPECTED RESULT %d: The Activity Factor retrieved should be equal to the sum of Tx and Rx Channel utilizations" %(step);
                    print "Activity Factor retrieved from TR181 parameter : %d" %ActivityFactor;
                    print "Activity Factor from adding Tx and Rx Channel Utilizations : %d" %calculated_AF;

                    if ActivityFactor == calculated_AF:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: The values are equal" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: The values are not equal" %step;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Failed to get the value" %step;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Failed to get the value" %step;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Failed to get the value" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

        step = step + 1;
    obj.unloadModule("tdkbtr181");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

