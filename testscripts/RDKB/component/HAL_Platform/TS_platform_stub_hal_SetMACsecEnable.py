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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>1</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_platform_stub_hal_SetMACsecEnable</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>platform_stub_hal_SetMACsecEnable</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To Validate the Successful get and Set operation of Platfrom HAL API's platfrom_hal_GetMAsecEnable and platform_hal_SetMACsecEnble.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>15</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_HAL_Platform_38</test_case_id>
    <test_objective>To get and set  the MACsec  Enable Status using platform_hal_GetMACsecEnable() and platform_hal_SetMACsecEnable() api respectively  and validate</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Device under test should have ethwan setup.</pre_requisite>
    <api_or_interface_used>platform_hal_GetMACsecEnable
platform_hal_SetMACsecEnable</api_or_interface_used>
    <input_parameters>ethport- Give the Ethernet port number
flag - indicates negative or positive scenario.
index - the value to be set</input_parameters>
    <automation_approch>1. Load  platform module.
2. From script invoke platform_hal_GetMACsecEnable().and store the value
3. Toggle the value to opposite value of get.
4. Invoke  platform_stub_hal_SetMACsecEnable() and set the value to toggle.
5. check if the value is set successfully.
6. Revert back the value to previous value which was stored on intial get function.
7. Validation of  the result is done within the python script and send the result status to Test Manager.
8. Test Manager will publish the result in GUI as PASS/FAILURE based on the response from HAL_Platform stub.</automation_approch>
    <expected_output>The get and set functionality of the api should be successful.</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_PLATFORM</test_stub_interface>
    <test_script>TS_platform_stub_hal_SetMACsecEnable</test_script>
    <skipped>No</skipped>
    <release_version>M76</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
 # use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","RDKB");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

obj.configureTestCase(ip,port,'TS_platform_stub_hal_SetMACsecEnable');
obj1.configureTestCase(ip,port,'TS_platform_stub_hal_SetMACsecEnable');

index  = -1;

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    #Get the default value from properties file
    tdkTestObj1 = obj1.createTestStep('ExecuteCmd');
    cmd = "sh %s/tdk_utility.sh parseConfigFile ETHWAN_ETH_PORT" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj1.addParameter("command", cmd);
    tdkTestObj1.executeTestCase(expectedresult);
    actualresult = tdkTestObj1.getResult();
    details = ""
    details = tdkTestObj1.getResultDetails().strip();
    ethPort = ""
    ethPort = details.replace("\\n", "");
    print"ETHWAN ETHERNET PORT:",ethPort
    if ethPort != "" and ( expectedresult in  actualresult):
       tdkTestObj1.setResultStatus("SUCCESS");
       print "TEST STEP 1: Get the ETHERNET PORT  from  tdk_platform properties file";
       print "EXPECTED RESULT 1: Should Get the default ETHERNET PORT form tdk_platfrom properties file";
       print "ACTUAL RESULT 1: The ETHERNET PORT from tdk_pltaform properties file : %s" % ethPort;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS"

       tdkTestObj = obj.createTestStep("platform_stub_hal_GetMACsecEnable");
       tdkTestObj.addParameter("ethPort",int(ethPort));
       flag = 0;
       tdkTestObj.addParameter("index",flag)
       expectedresult="SUCCESS";
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       InitMACsecState= tdkTestObj.getResultDetails();
       print "Initail MACsec Enable Status %s"%InitMACsecState;

       if expectedresult in  actualresult and InitMACsecState != "":
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP 2: Retrieve the GetMACsecEnable";
          print "EXPECTED RESULT 2: Should retrieve the  GetMACsecEnable successfully";
          print "ACTUAL RESULT 2: GetMACsecEnable is : %s" %InitMACsecState;
          print "[TEST EXECUTION RESULT] : %s" %actualresult ;

          #retriving the value to be toggled
          if  int(InitMACsecState) == 0:
              index  = 1;
          else:
              index =  0;
          print "The value to be set is :",index
          tdkTestObj = obj.createTestStep("platform_stub_hal_SetMACsecEnable");
          tdkTestObj.addParameter("ethPort",int(ethPort));
          tdkTestObj.addParameter("index",index);
          expectedresult="SUCCESS";
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails().replace("\\n", "");

          if expectedresult in  actualresult :
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Set the SetMACsecEnable";
             print "EXPECTED RESULT 3: Should set the SetMACsecEnable successfully";
             print "ACTUAL RESULT 3:%s" %details;
             print "[TEST EXECUTION RESULT] : %s" %actualresult ;

             tdkTestObj = obj.createTestStep("platform_stub_hal_GetMACsecEnable");
             tdkTestObj.addParameter("ethPort",int(ethPort));
             flag = 0;
             tdkTestObj.addParameter("index",flag);
             expectedresult="SUCCESS";
             tdkTestObj.executeTestCase(expectedresult);
             actualresult = tdkTestObj.getResult();
             GetMACsecState= tdkTestObj.getResultDetails();
             print "GetMACsec Enable status after set is %s"%GetMACsecState;

             if expectedresult in  actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Retrieve the GetMACsecEnable after SetMACsecEnable";
                print "EXPECTED RESULT 4: Should retrieve the  GetMACsecEnable after SetMACsecEnable successfully";
                print "ACTUAL RESULT 4: GetMACsecEnable after SetMACsecEnable is : %s" %GetMACsecState;
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;

                print "The value set by SetMACsecEnable is :",index
                print "The get value after set is :",GetMACsecState

                if int(GetMACsecState) == index:
                   print "TEST STEP 5: Check if Get MACsecEnable is equal to the the set value "
                   print "EXPECTED RESULT 5: Get MACsecEnable should be  equal to the the set value"
                   print "ACTUAL RESULT 5: Get MACsecEnable is  equal to the the set value"
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "[TEST EXECUTION RESULT] : SUCCESS"
                else:
                    print "TEST STEP 5: Check if Get MACsecEnable is equal to the the set value "
                    print "EXPECTED RESULT 5: Get MACsecEnable should be  equal to the the set value"
                    print "ACTUAL RESULT 5: Get MACsecEnable is not equal to the the set value"
                    tdkTestObj.setResultStatus("FAILURE");
                    print "[TEST EXECUTION RESULT] : FAILURE"
             else:
                 tdkTestObj.setResultStatus("FAILURE");
                 print "TEST STEP 4: Retrieve the GetMACsecEnable after SetMACsecEnable";
                 print "EXPECTED RESULT 4: Should retrieve the  GetMACsecEnable after SetMACsecEnable successfully";
                 print "ACTUAL RESULT 4: Failed to GetMACsecEnable after SetMACsecEnable : %s" %InitMACsecState;
                 print "[TEST EXECUTION RESULT] : %s" %actualresult ;
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 3: Set the SetMACsecEnable";
              print "EXPECTED RESULT 3: Should set the SetMACsecEnable successfully";
              print "ACTUAL RESULT 3: %s" %details;
              print "[TEST EXECUTION RESULT] : %s" %actualresult ;

          #Reverting the value
          tdkTestObj = obj.createTestStep("platform_stub_hal_SetMACsecEnable");
          tdkTestObj.addParameter("ethPort",int(ethPort));
          tdkTestObj.addParameter("index",int(InitMACsecState));
          expectedresult="SUCCESS";
          tdkTestObj.executeTestCase(expectedresult);
          actualresult = tdkTestObj.getResult();
          details = tdkTestObj.getResultDetails().replace("\\n", "");

          if expectedresult in  actualresult:
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 6: Should Revert  the MACsecEnable";
             print "EXPECTED RESULT 6: Should revert SetMACsecEnable successfully";
             print "ACTUAL RESULT 6 : %s" %details;
             print "[TEST EXECUTION RESULT] : %s" %actualresult ;
          else:
              tdkTestObj.setResultStatus("FAILURE");
              print "TEST STEP 6: Should Revert  the  SetMACsecEnable";
              print "EXPECTED RESULT 6: Should Revert  the SetMACsecEnable successfully";
              print "ACTUAL RESULT 6: %s" %details;
              print "[TEST EXECUTION RESULT] : %s" %actualresult ;
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP 2: Retrieve the GetMACsecEnable";
           print "EXPECTED RESULT 2: Should retrieve the  GetMACsecEnable successfully";
           print "ACTUAL RESULT 2: GetMACsecEnable failed the details is : %s" %InitMACsecState;
           print "[TEST EXECUTION RESULT] : %s" %actualresult ;
    else:
        tdkTestObj1.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the ETHERNET PORT  from  tdk_platform properties file";
        print "EXPECTED RESULT 1: Should Get the default ETHERNET PORT form tdk_platfrom properties file";
        print "ACTUAL RESULT 1: Failed to get  ETHERNET PORT from tdk_pltaform properties file : %s" % ethPort;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("halplatform");
    obj1.unloadModule("sysutil");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

