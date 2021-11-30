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
  <name>TS_PAM_CheckApparmorBlocklist_OnFR</name>
  <primitive_test_id/>
  <primitive_test_name>pam_GetParameterValues</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the Apparmor Blocklist from Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.ApparmorBlocklist matches with the Blocklist in the DUT.</synopsis>
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
    <test_case_id>TC_PAM_219</test_case_id>
    <test_objective>To check if the Apparmor Blocklist from Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.ApparmorBlocklist matches with the Blocklist in the DUT.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>ParamName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.ApparmorBlocklist
ParamName : Device.X_CISCO_COM_DeviceControl.FactoryReset
ParamValue : Router,Wifi,VoIP,Dect,MoCA
Type : string
</input_parameters>
    <automation_approch>1. Load the modules
2. Initiate a device Factory reset.
3. After the device comes up, get the default value of Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.ApparmorBlocklist.
4. Retrieve the location of Blocklist file in the DUT from platform properties file.
5. Check if the mode of all the Apps in the blocklist from the TR181 parameter matches with the blocklist modes of the Apps from the file in DUT.
6. Unload the modules.</automation_approch>
    <expected_output>The Apparmor Blocklist from Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.ApparmorBlocklist should match with the Blocklist in the DUT for all the Apps.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_CheckApparmorBlocklist_OnFR</test_script>
    <skipped>No</skipped>
    <release_version>M95</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_CheckApparmorBlocklist_OnFR');
sysobj.configureTestCase(ip,port,'TS_PAM_CheckApparmorBlocklist_OnFR');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysutilloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus ;

if "SUCCESS" in (loadmodulestatus.upper() and sysutilloadmodulestatus.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    obj.saveCurrentState();
    #Initiate Factory reset before checking the default value
    tdkTestObj = obj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("Type","string");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "\nTEST STEP 1: Initiate factory reset ";
        print "EXPECTED RESULT 1 : Should initiate FR successfully";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Restore the device state saved before reboot
        obj.restorePreviousStateAfterReboot();

        tdkTestObj = obj.createTestStep('pam_GetParameterValues');
        tdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.ApparmorBlocklist");
        expectedresult="SUCCESS";
        #Execute the test case in DUT
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        blockList = tdkTestObj.getResultDetails().strip();

        print "\nTEST STEP 2: Retrieve the Default Apparmor Blocklist using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.NonRootSupport.ApparmorBlocklist"
        print "EXPECTED RESULT 2: Should get the Apparmor Blocklist successfully"

        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: The Default value is :  %s" %blockList;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            #Get the Apparmor file location
            tdkTestObj = sysobj.createTestStep('ExecuteCmd');
            cmd = "sh %s/tdk_utility.sh parseConfigFile APPARMOR_BLOCKLIST" %TDK_PATH;
            print "\nCommand : ", cmd;
            tdkTestObj.addParameter("command", cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            file = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            print "\nTEST STEP 3: Get the Apparmour Blocklist file location from platform property file";
            print "EXPECTED RESULT 3: Should successfully get the Apparmour Blocklist file location from platform property file";

            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: File location: %s" %file;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Verify if the file is present in the location
                cmd = "[ -f " + file + " ] && echo \"File exist\" || echo \"File does not exist\"";
                print "\nCommand : ", cmd;
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                print "\nTEST STEP 4: Check for %s file presence" %(file);
                print "EXPECTED RESULT 4: %s file should be present" %(file);

                if expectedresult in actualresult and details == "File exist":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: %s file is present" %(file);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Verify the Apparmour blocklist
                    blockList = blockList.split(",");
                    no_of_apps = len(blockList);
                    total_verified = 0;

                    print "\nTEST STEP 5 : Check if the Apparmor blocklist from TR181 parameter match with the blocklist in the file %s"%file;
                    print "EXPECTED RESULT 5 : The Apparmor blocklist from TR181 parameter should match with the blocklist in the file %s"%file;

                    for index in range(0,no_of_apps):
                        appName = blockList[index].split(":")[0];
                        mode = blockList[index].split(":")[1];
                        cmd = "cat " + file + " | grep " + appName;
                        print "\nCommand : ", cmd;
                        tdkTestObj.addParameter("command",cmd);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                        print "For the App %s" %appName;

                        if expectedresult in actualresult and details != "":
                            tdkTestObj.setResultStatus("SUCCESS");
                            details = details.split(":")[1];
                            print "Mode from TR181 : %s" %mode;
                            print "Mode from %s : %s" %(file, mode);

                            if details == mode:
                               total_verified = total_verified + 1;
                               tdkTestObj.setResultStatus("SUCCESS");
                               print "The Mode is matched for the App";
                            else:
                               tdkTestObj.setResultStatus("FAILURE");
                               print "The Mode is not matched for the App";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "App details not found in the file %s" %file;

                    if total_verified == no_of_apps:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 5: The Apparmor blaocklist is verified";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 5: The Apparmor blaocklist is not verified";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: %s file is not present" %(file);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: File location: %s" %file;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: The parameter value not retrieved successfully; Details : %s"%blockList;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "\nTEST STEP 1: Initiate factory reset ";
        print "EXPECTED RESULT 1 : Should initiate FR successfully"
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("pam");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load pam/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
