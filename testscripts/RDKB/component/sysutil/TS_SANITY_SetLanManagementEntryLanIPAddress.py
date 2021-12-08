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
  <version>2</version>
  <name>TS_SANITY_SetLanManagementEntryLanIPAddress</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set lan Ip address using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddressand check if same  reflected in ifconfig of brlan0</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_SYSUTIL_31</test_case_id>
    <test_objective>This test case is to check if the Lan Ip addresses set via  Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress  gets reflected in ifconfig of brlan0</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,RPI,EMU</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress</input_parameters>
    <automation_approch>1.Load module
2. Do a get on  Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress and store the result
3.Try to set different private IPs and check if the set value reflects in ifconfig brlan0
4.TM will display the result s based on the validation as SUCCESS and FAILURE.
5.Revert the IP to its previous value
5.Unload the module</automation_approch>
    <expected_output>The IP set through tr-181 parameter should be equal to one present in ifconfig brlan0</expected_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_SANITY_SetLanManagementEntryLanIPAddress</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
import tdklib;
from time import sleep;
from tdkbVariables import *;
#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
pamObj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_SetLanManagementEntryLanIPAddress');
pamObj.configureTestCase(ip,port,'TS_SANITY_SetLanManagementEntryLanIPAddress');

#Get the result of connection with test component and DUT
loadmodulestatus1 =sysObj.getLoadModuleResult();
loadmodulestatus2 =pamObj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus1.upper() and loadmodulestatus2.upper:
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    pamObj.setLoadModuleStatus("SUCCESS");

    tdkTestObj = pamObj.createTestStep('pam_GetParameterValues');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress")
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult1 = tdkTestObj.getResult();
    defaultLanIp = tdkTestObj.getResultDetails().strip();

    tdkTestObj = sysObj.createTestStep('ExecuteCmd');
    tdkTestObj.addParameter("command", "ifconfig brlan0 | grep \"inet addr\" | cut -f2 -d ':' | cut -f1 -d ' ' | tr \"\n\" \" \"");
    expectedresult="SUCCESS";
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult2 = tdkTestObj.getResult();
    ip = tdkTestObj.getResultDetails().strip();

    if expectedresult in actualresult1 and  expectedresult in actualresult2 and defaultLanIp == ip :
       print "LAN IP via Tr-181 :",defaultLanIp;
       print "LAN IP via ifconfig brlan0:",ip;
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the Lan IP Address via tr181 and ifconfig brlan0"
       print "EXPECTED RESULT 1: Should get the Lan IP Address equal from ifconfig and brlan0";
       print "ACTUAL RESULT 1:Lan IP Address:",defaultLanIp ;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";

       SetIps = [];
       tdkTestObj = sysObj.createTestStep('ExecuteCmd');
       cmd = "sh %s/tdk_utility.sh parseConfigFile LAN_IPADDRESS" %TDK_PATH;
       print cmd;
       expectedresult="SUCCESS";
       tdkTestObj.addParameter("command", cmd);
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
       if expectedresult in actualresult  and details!= "":
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP 2: Execute the command";
           print "EXPECTED RESULT 2: Should execute the command successfully";
           print "ACTUAL RESULT 2: Details: %s" %details;
           print "[TEST EXECUTION RESULT] : SUCCESS";
           IpLists=details.split(",");

           #getting length of list
           length = len(IpLists);
           #finding the ips to be considered for validation excluding the default ip
           for i in range(length):
               if IpLists[i] != defaultLanIp:
                  SetIps.append(IpLists[i]);

           #getting length of list
           length = len(SetIps);
           flag = 0;
           equalflag = 0;
           print "Trying to Set the LAN IP's to the following:",SetIps;

           for i in range(length):
               print "Setting LAN IP to ",SetIps[i];

               tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
               tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress")
               tdkTestObj.addParameter("ParamValue",str(SetIps[i]));
               tdkTestObj.addParameter("Type","string");
               expectedresult="SUCCESS";

               #Execute testcase on DUT
               tdkTestObj.executeTestCase(expectedresult);
               actualresult = tdkTestObj.getResult();
               Setresult = tdkTestObj.getResultDetails();

               flag = 0;
               equalflag = 0;
               SetValue = SetIps[i];

               if expectedresult in actualresult:
                   flag =0;
                   print " Value set successfully to ",SetValue;
                   sleep(20);
                   tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                   tdkTestObj.addParameter("command", "ifconfig brlan0 | grep \"inet addr\" | cut -f2 -d ':' | cut -f1 -d ' ' | tr \"\n\" \" \"");
                   expectedresult="SUCCESS";

                   #Execute the test case in DUT
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult = tdkTestObj.getResult();
                   ip = tdkTestObj.getResultDetails().strip();

                   print "LAN IP in brlan0 is :",ip
                   print "LAN IP set using tr-181 parameter :",SetValue

                   if expectedresult in actualresult and ip == SetValue:
                       equalflag =0;
                       tdkTestObj.setResultStatus("SUCCESS");
                       print "[TEST EXECUTION RESULT] : SUCCESS, Set ip and brlan0 ip are same";
                   else:
                       equalflag =1
                       tdkTestObj.setResultStatus("FAILURE");
                       print "[TEST EXECUTION RESULT] : FAILURE, Set ip and brlan0 ip are not same";
                       break;
               else:
                   flag =1;
                   break;

           if flag == 0 and equalflag == 0:
               #Set the result status of execution
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 3: Set the Lan IP Address to:",SetIps,"and check if the same ip reflects in ifconfig | grep brlan0";
               print "EXPECTED RESULT 3: Should set the Lan IP Address to:",SetIps,"and check if the same ip reflects in ifconfig | grep brlan0";
               print "ACTUAL RESULT 3: Lan IP Addresses were set successfully and the ip got reflected in ifconfig | grep brlan0" ;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3: Set the Lan IP Address to:",SetIps,"and check if the same ip reflects in ifconfig | grep brlan0";
               print "EXPECTED RESULT 3: Should set the Lan IP Address to:",SetIps,"and check if the same ip reflects in ifconfig | grep brlan0";
               print "ACTUAL RESULT 3: Lan IP Addresses failed to set or failed to reflect the same in ifconfig" ;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";

           #Revert the value
           tdkTestObj = pamObj.createTestStep('pam_SetParameterValues');
           tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress")
           tdkTestObj.addParameter("ParamValue",defaultLanIp);
           tdkTestObj.addParameter("Type","string");
           expectedresult="SUCCESS";
           #Execute testcase on DUT
           tdkTestObj.executeTestCase(expectedresult);
           actualresult = tdkTestObj.getResult();
           result = tdkTestObj.getResultDetails();

           if expectedresult in  expectedresult:
               #Set the result status of execution
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 4: Revert LAN IP Address to its default";
               print "EXPECTED RESULT 4: Revert LAN IP Address to previous value";
               print "ACTUAL RESULT 4: Revert Operation sucesss:",result ;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 4: Revert LAN IP Address to its default";
               print "EXPECTED RESULT 4: Revert LAN IP Address to previous value";
               print "ACTUAL RESULT 4: Revert Operation sucesss:",result ;
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Execute the command";
           print "EXPECTED RESULT 2: Should execute the command successfully";
           print "ACTUAL RESULT 2: Details: %s" %details;
           print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Lan IP Address via tr181 and ifconfig brlan0"
        print "EXPECTED RESULT 1: Should get the Lan IP Address via tr181 and ifconfig brlan0 equal";
        print "ACTUAL RESULT 1:Lan IP Address",defaultLanIp ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    sysObj.unloadModule("sysutil");
    pamObj.unloadModule("pam");

else:
    print "Failed to load sysutil/pam  module";
    sysObj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
