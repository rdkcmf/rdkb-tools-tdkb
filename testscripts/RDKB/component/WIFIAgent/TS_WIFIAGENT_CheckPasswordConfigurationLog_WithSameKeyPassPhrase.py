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
  <version>10</version>
  <name>TS_WIFIAGENT_CheckPasswordConfigurationLog_WithSameKeyPassPhrase</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_SetMultiple</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set the same KeyPassphrase to Device.WiFi.AccessPoint.1.Security.KeyPassphrase and Device.WiFi.AccessPoint.2.Security.KeyPassphrase and check if the log "Same password was configured on User Private SSID for 2.4 and 5 GHz radios" is found in /rdklogs/logs/WiFilog.txt.0.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_WIFIAGENT_168</test_case_id>
    <test_objective>Set the same KeyPassphrase to Device.WiFi.AccessPoint.1.Security.KeyPassphrase and Device.WiFi.AccessPoint.2.Security.KeyPassphrase and check if the log "Same password was configured on User Private SSID for 2.4 and 5 GHz radios" is found in /rdklogs/logs/WiFilog.txt.0.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.AccessPoint.1.Security.KeyPassphrase
paramName : Device.WiFi.AccessPoint.2.Security.KeyPassphrase
PASSWORD_2G : "test_password"
PASSWORD_5G : "test_password"
</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial values of Device.WiFi.AccessPoint.1.Security.KeyPassphrase and Device.WiFi.AccessPoint.2.Security.KeyPassphrase and store them.
3. Get the initial number of log lines "Same password was configured on User Private SSID for 2.4 and 5 GHz radios"
 in WiFilog.txt.0 under /rdklogs/logs
4. Set Device.WiFi.AccessPoint.1.Security.KeyPassphrase and Device.WiFi.AccessPoint.2.Security.KeyPassphrase to the same new KeyPassphrase value. Check if the SET operation is success.
5. Validate the SET with GET
6. Get the final count of log lines. It should be incremented by 2 from the initial value as the same KeyPassphrase is set to both radios.
7. Revert to initial values
8. Unload the modules
</automation_approch>
    <expected_output>The same KeyPassphrase should be set successfully to Device.WiFi.AccessPoint.1.Security.KeyPassphrase and Device.WiFi.AccessPoint.2.Security.KeyPassphrase and the required log lines should be present under /rdklogs/logs/WiFilog.txt.0 after the SET operation.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckPasswordConfigurationLog_WithSameKeyPassPhrase</test_script>
    <skipped>No</skipped>
    <release_version>M98</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("wifiagent","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckPasswordConfigurationLog_WithSameKeyPassPhrase');
obj1.configureTestCase(ip,port,'TS_WIFIAGENT_CheckPasswordConfigurationLog_WithSameKeyPassPhrase');
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckPasswordConfigurationLog_WithSameKeyPassPhrase');

#Get the result of connection with test component and STB
loadmodulestatus1 =obj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();
loadmodulestatus3 =sysobj.getLoadModuleResult();
PASSWORD_2G = "test_password"
PASSWORD_5G = "test_password"

if "SUCCESS" in loadmodulestatus1.upper() and "SUCCESS" in loadmodulestatus2.upper() and "SUCCESS" in loadmodulestatus3.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    #Get the initial KeyPassphrase and store them
    paramList=["Device.WiFi.AccessPoint.1.Security.KeyPassphrase", "Device.WiFi.AccessPoint.2.Security.KeyPassphrase"]
    tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)
    print "\nTEST STEP 1: Get the values of Device.WiFi.AccessPoint.1.Security.KeyPassphrase and Device.WiFi.AccessPoint.2.Security.KeyPassphrase";
    print "EXPECTED RESULT 1 : The values should be retrieved successfully";

    if expectedresult in status and orgValue[0] != "" and orgValue[1] != "" :
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: KeyPassphrase are respectively : %s, %s" %(orgValue[0],orgValue[1]) ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check the number of log lines "Same password was configured on User Private SSID for 2.4 and 5 GHz radios" in WiFilog.txt.0
        print "\nGet the number of log lines \"Same password was configured on User Private SSID for 2.4 and 5 GHz radios\" in /rdklogs/logs/WiFilog.txt.0";
        tdkTestObj1 = sysobj.createTestStep('ExecuteCmd');
        file = "/rdklogs/logs/WiFilog.txt.0";
        step = 2;
        log = "Same password was configured on User Private SSID for 2.4 and 5 GHz radios";
        count_initial = getLogFileTotalLinesCount(tdkTestObj1, file, log, step);
        print "The initial number of required log lines in WiFilog.txt.0 is : %d" %count_initial;

        #Set the KeyPassphrase of 2.4G and 5G to the same values
        tdkTestObj = obj1.createTestStep("WIFIAgent_SetMultiple");
        tdkTestObj.addParameter("paramList","Device.WiFi.AccessPoint.1.Security.KeyPassphrase|%s|string|Device.WiFi.AccessPoint.2.Security.KeyPassphrase|%s|string|Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting|true|bool|Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting|true|bool" %(PASSWORD_2G, PASSWORD_5G));
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP 3 : Set Device.WiFi.AccessPoint.1.Security.KeyPassphrase and Device.WiFi.AccessPoint.2.Security.KeyPassphrase to same values";
        print "EXPECTED RESULT 3 : Should successfully set Device.WiFi.AccessPoint.1.Security.KeyPassphrase to %s and Device.WiFi.AccessPoint.1.Security.KeyPassphraseto %s" %(PASSWORD_2G, PASSWORD_5G);

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 3: Set operation success; Details : %s" %details;
            print "TEST EXECUTION RESULT :SUCCESS";

            #Validate the SET with GET
            tdkTestObj,status,setValue = getMultipleParameterValues(obj,paramList)
            print "\nTEST STEP 4: Get the values of Device.WiFi.AccessPoint.1.Security.KeyPassphrase and Device.WiFi.AccessPoint.2.Security.KeyPassphrase";
            print "EXPECTED RESULT 4: The values should be retrieved successfully and should be the same as set values";

            if expectedresult in status and setValue[0] == PASSWORD_2G and setValue[1] == PASSWORD_5G :
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 4: KeyPasshrase values after the GET are same as the SET values : %s, %s" %(setValue[0],setValue[1]) ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check the number of log lines "Same password was configured on User Private SSID for 2.4 and 5 GHz radios" in WiFilog.txt.0
                print "\nGet the number of log lines \"Same password was configured on User Private SSID for 2.4 and 5 GHz radios\" in /rdklogs/logs/WiFilog.txt.0";
                tdkTestObj1 = sysobj.createTestStep('ExecuteCmd');
                step = 5;
                count_final = getLogFileTotalLinesCount(tdkTestObj1, file, log, step);
                print "The final number of required log lines in WiFilog.txt.0 is : %d" %count_final;

                #Check if the final log line number is incremented by 2 as KeyPassphrase set is done for both 2.4 and 5 radios
                print "\nTEST STEP 6 : Check if the final number of log lines is incremented by 2";
                print "EXPECTED RESULT 6 : The final number of log lines should be incremented by 2";
                print "Initial Count : %d" %count_initial;
                print "Final Count : %d" %count_final;

                if count_final == (count_initial + 2):
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 6:The final number of log lines is incremented by 2";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 6:The final number of log lines is not incremented by 2";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";

                #Revert the KeyPassphrase to initial values
                tdkTestObj = obj1.createTestStep("WIFIAgent_SetMultiple");
                tdkTestObj.addParameter("paramList","Device.WiFi.AccessPoint.1.Security.KeyPassphrase|%s|string|Device.WiFi.AccessPoint.2.Security.KeyPassphrase|%s|string|Device.WiFi.Radio.1.X_CISCO_COM_ApplySetting|true|bool|Device.WiFi.Radio.2.X_CISCO_COM_ApplySetting|true|bool" %(orgValue[0], orgValue[1]));
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP 7 : Revert Device.WiFi.AccessPoint.1.Security.KeyPassphrase and Device.WiFi.AccessPoint.2.Security.KeyPassphrase to initial values";
                print "EXPECTED RESULT 7 : Should successfully set Device.WiFi.AccessPoint.1.Security.KeyPassphrase to %s and Device.WiFi.AccessPoint.1.Security.KeyPassphraseto %s" %(orgValue[0], orgValue[1]);

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 7: Set operation success; Details : %s" %details;
                    print "TEST EXECUTION RESULT :SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 7: Set operation failed; Details : %s" %details;
                    print "TEST EXECUTION RESULT :FAILURE";
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 4: KeyPasshrase values after the GET are not same as the SET values : %s, %s" %(setValue[0],setValue[1]) ;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 3: Set operation failed; Details : %s" %details;
            print "TEST EXECUTION RESULT :FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Failed to get KeyPassphrase values; Details : %s" %details;
        print "TEST EXECUTION RESULT :FAILURE";

    obj.unloadModule("tad");
    obj1.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
