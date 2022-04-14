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
  <version>11</version>
  <name>TS_WIFIAGENT_2.4GHzSetKeyPassphrase_WithPersonalSecurityModes</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the KeyPassphrase is successfully set using Device.WiFi.AccessPoint.1.Security.KeyPassphrase when different personal security modes is set using Device.WiFi.AccessPoint.1.Security.ModeEnabled from the supported list of modes retrieved using Device.WiFi.AccessPoint.1.Security.ModesSupported.</synopsis>
  <groups_id/>
  <execution_time>3</execution_time>
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
    <test_case_id>TC_WIFIAGENT_162</test_case_id>
    <test_objective>Check if the KeyPassphrase is successfully set using Device.WiFi.AccessPoint.1.Security.KeyPassphrase when different personal security modes is set using Device.WiFi.AccessPoint.1.Security.ModeEnabled from the supported list of modes retrieved using Device.WiFi.AccessPoint.1.Security.ModesSupported.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.AccessPoint.1.Security.KeyPassphrase
paramValue : keyPassphrase
paramType : string
paramName : Device.WiFi.AccessPoint.1.Security.ModeEnabled
paramValue : mode
paramType : bool
paramName : Device.WiFi.AccessPoint.1.Security.ModesSupported</input_parameters>
    <automation_approch>1. Load the modules
2. Get the supported security modes using Device.WiFi.AccessPoint.1.Security.ModesSupported.
4. Get the initial security mode using Device.WiFi.AccessPoint.1.Security.ModeEnabled
3. Get the initial security KeyPassphrase using Device.WiFi.AccessPoint.1.Security.KeyPassphrase
4. Set the security mode to supported Personal modes and for each Personal mode set, set the Security KeyPassphrase and check if the SET operation is success.
5. Revert to initial values.
6. Unload the modules.</automation_approch>
    <expected_output>The KeyPassphrase should be successfully set using Device.WiFi.AccessPoint.1.Security.KeyPassphrase when different personal security modes is set using Device.WiFi.AccessPoint.1.Security.ModeEnabled from the supported list of modes retrieved using Device.WiFi.AccessPoint.1.Security.ModesSupported.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_2.4GHzSetKeyPassphrase_WithPersonalSecurityModes</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def setKeyPassphrase(obj1, keyPassphrase, step):
    expectedresult = "SUCCESS";
    tdkTestObj = obj1.createTestStep("WIFIAgent_Set");
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.KeyPassphrase");
    tdkTestObj.addParameter("paramValue",keyPassphrase);
    tdkTestObj.addParameter("paramType","string");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d : Set Device.WiFi.AccessPoint.1.Security.KeyPassphrase to %s" %(step, keyPassphrase);
    print "EXPECTED RESULT %d : Should successfully set Device.WiFi.AccessPoint.1.Security.KeyPassphrase to %s" %(step,keyPassphrase);

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details);
        print "TEST EXECUTION RESULT :SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details);
        print "TEST EXECUTION RESULT :FAILURE";
    return actualresult;

def setSecurityMode(obj1, mode, step):
    expectedresult = "SUCCESS";
    tdkTestObj = obj1.createTestStep("WIFIAgent_Set");
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.ModeEnabled");
    tdkTestObj.addParameter("paramValue",mode);
    tdkTestObj.addParameter("paramType","string");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d : Set Device.WiFi.AccessPoint.1.Security.ModeEnabled to %s" %(step, mode);
    print "EXPECTED RESULT %d : Should successfully set Device.WiFi.AccessPoint.1.Security.ModeEnabled to %s" %(step,mode);

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Set operation success; Details : %s" %(step,details);
        print "TEST EXECUTION RESULT :SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Set operation failed; Details : %s" %(step,details);
        print "TEST EXECUTION RESULT :FAILURE";
    return actualresult;

def getSecurityMode(obj1, step):
    #Get the supported Security Modes
    tdkTestObj = obj1.createTestStep("WIFIAgent_Get");
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.ModeEnabled");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d : Get the Security Mode using Device.WiFi.AccessPoint.1.Security.ModeEnabled" %step;
    print "EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.1.Security.ModeEnabled" %step;

    if expectedresult in actualresult:
        details = details.split("VALUE:")[1].split(' ')[0].split(',');
        details = details[0];
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step,details);
        print "TEST EXECUTION RESULT :SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,details);
        print "TEST EXECUTION RESULT :FAILURE";
    return actualresult, details;

def getKeyPassphrase(obj1, step):
    #Get the supported Security Modes
    tdkTestObj = obj1.createTestStep("WIFIAgent_Get");
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.KeyPassphrase");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d : Get the Security KeyPassphrase using Device.WiFi.AccessPoint.1.Security.KeyPassphrase" %step;
    print "EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.1.Security.KeyPassphrase" %step;

    if expectedresult in actualresult:
        details = details.split("VALUE:")[1].split(' ')[0].split(',');
        details = details[0];
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step,details);
        print "TEST EXECUTION RESULT :SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,details);
        print "TEST EXECUTION RESULT :FAILURE";
    return actualresult, details;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
from time import sleep;

#Test component to be tested
obj1 = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_2.4GHzSetKeyPassphrase_WithPersonalSecurityModes');

#Get the result of connection with test component and DUT
loadmodulestatus1 =obj1.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper():
    obj1.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";

    #Get the supported Security Modes
    step = 1;
    tdkTestObj = obj1.createTestStep("WIFIAgent_Get");
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.1.Security.ModesSupported");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d : Get the supported modes supported using Device.WiFi.AccessPoint.1.Security.ModesSupported" %step;
    print "EXPECTED RESULT %d : Should successfully get Device.WiFi.AccessPoint.1.Security.ModesSupported" %step;

    if expectedresult in actualresult:
        supported_modes = details.split("VALUE:")[1].split(' ')[0].split(',');
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Get operation success; Details : %s" %(step,details);
        print "Supported Modes : ", supported_modes;
        print "TEST EXECUTION RESULT :SUCCESS";

        #Get the initial security mode
        step = step + 1;
        actualresult, initial_mode = getSecurityMode(obj1, step);

        if expectedresult in actualresult :
            #Get the initial KeyPassphrase
            step = step + 1;
            actualresult, initial_passphrase = getKeyPassphrase(obj1, step);

            if expectedresult in actualresult:
                #Set the KeyPassphrase for each of the Security modes
                for mode in supported_modes:
                    #KeyPassphrase should be SET only in applicable Personal modes
                    if "Personal" in mode:
                        print "\n****************For Mode %s********************" %mode;

                        if "WPA3" in mode :
                            print "The security mode %s is a WPA3 Personal mode for which KeyPassphrase setting is not applicable..." %mode;
                        else :
                            #Set the security mode
                            step = step + 1;
                            actualresult =  setSecurityMode(obj1, mode, step);

                            if expectedresult in actualresult :
                                #Verify the SET with GET
                                step = step + 1;
                                actualresult, final_mode = getSecurityMode(obj1, step);
                                print "Set Mode : ", mode;
                                print "Get Mode : ", final_mode;

                                if final_mode == mode:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "SET is reflected in GET";

                                    #Set the KeyPassPhrase
                                    step = step + 1;
                                    keyPassphrase = "test_password_" + str(step);
                                    actualresult = setKeyPassphrase(obj1, keyPassphrase, step);

                                    if expectedresult in actualresult :
                                        #Check if the SET is reflected in GET
                                        step = step + 1;
                                        actualresult, final_passphrase = getKeyPassphrase(obj1, step);
                                        print "Set KeyPassphrase : ", keyPassphrase;
                                        print "Get KeyPassphrase : ", final_passphrase;

                                        if keyPassphrase == final_passphrase:
                                            tdkTestObj.setResultStatus("SUCCESS");
                                            print "SET is reflected in GET";
                                        else:
                                            tdkTestObj.setResultStatus("FAILURE");
                                            print "SET is not reflected in GET";
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "SET operation failed";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "SET is not reflected in GET";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "SET operation failed";
                    else:
                        continue;

                #Revert operation
                print "\nReverting to initial KeyPassPhrase..."
                step = step + 1;
                actualresult = setKeyPassphrase(obj1, initial_passphrase, step)

                if expectedresult in actualresult :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "Reverting to initial KeyPassPhrase was successful";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Reverting to initial KeyPassPhrase was not successful";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "GET operation failed";

            #Revert operation
            print "Reverting to initial Security Mode..."
            step = step + 1;
            actualresult = setSecurityMode(obj1, initial_mode, step);

            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "Reverting Mode to initial value was successful";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Reverting Mode to initial value was not successful";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "GET operation failed";
    else:
        tdkTestObj.setResultStatus("FAILED");
        print "ACTUAL RESULT %d: Get operation failed; Details : %s" %(step,details);
        print "TEST EXECUTION RESULT :FAILURE";

    obj1.unloadModule("wifiagent");
else:
    print "Failed to load the module";
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
