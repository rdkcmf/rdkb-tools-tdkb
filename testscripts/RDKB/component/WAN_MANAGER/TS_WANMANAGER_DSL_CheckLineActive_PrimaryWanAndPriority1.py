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
  <version>3</version>
  <name>TS_WANMANAGER_DSL_CheckLineActive_PrimaryWanAndPriority1</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if DSL Line is active with Primary WAN type and its priority as 1 after reboot with a active DSL Line</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_WANMANAGER_47</test_case_id>
    <test_objective>To check if DSL Line is active with Primary WAN type and its priority as 1 after reboot with a active DSL Line</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.WAN  Manager should be enabled
4.DSL Line Should be Enabled.</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>Device.X_RDK_WanManager.CPEInterface.1.Wan.Type
Device.X_RDK_WanManager.CPEInterface.2.Wan.Type
Device.X_RDK_WanManager.CPEInterface.1.Wan.Priority
Device.X_RDK_WanManager.CPEInterface.2.Wan.Priority</input_parameters>
    <automation_approch>1.Load the module
2.Check if DSL connection is active , check WANoE is disabled if not disable it
3.Get the WAN Type and  priorities for DSL and WANOE.
4.Set the (WAN type ,WAN Priority) as (Primary ,1) for DSL and (Secondary, 0)for WANOE respectively
5.reboot the device
6.DSL line is expected to be active and WANOE line should be inactive
7.Revert the set Values
8.Unload the module</automation_approch>
    <expected_output>With (WAN type ,WAN Priority) as (Primary ,1) for DSL and (Secondary, 0) for WANOE respectively DSL line is expected to be active and WANOE line should be inactive</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN_MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_DSL_CheckLineActive_PrimaryWanAndPriority1</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from time import sleep;
from WanManager_Utility import *;
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");
tadobj = tdklib.TDKScriptingLibrary("tad","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckLineActive_PrimaryWanAndPriority1');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckLineActive_PrimaryWanAndPriority1');
tadobj.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckLineActive_PrimaryWanAndPriority1');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
loadmodulestatus2 = tadobj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus2;

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper() and loadmodulestatus2.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tadobj.setLoadModuleStatus("SUCCESS");
    revertWANOE =0;
    objReturned,dsl_wan,active = getDSLWANStatus(tadobj,1);

    if active == 0:
       expectedresult="SUCCESS";

       print "******performing a pre-requisite where in WANOE inteface is expected to be disabled ***";
       tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
       tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.2.Wan.Enable");
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
       if expectedresult in actualresult and details == "true":
           print "WANOE is enabled and disabling it ";
           tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
           result,tdkTestObj = EnableDisableInterafce(2,"false",tdkTestObj);
           revertWANOE = 1;
       print "WANOE is in Disabled mode";

       if expectedresult in actualresult:
           paramList = ["Device.X_RDK_WanManager.CPEInterface.1.Wan.Type","Device.X_RDK_WanManager.CPEInterface.2.Wan.Type","Device.X_RDK_WanManager.CPEInterface.1.Wan.Priority","Device.X_RDK_WanManager.CPEInterface.2.Wan.Priority"];
           dataType = ["string","string","int","int"];
           defaults = [];
           flag =0;

           for item in paramList:
               tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
               tdkTestObj.addParameter("ParamName",item);
               #Execute the test case in DUT
               tdkTestObj.executeTestCase(expectedresult);
               actualresult = tdkTestObj.getResult();
               details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
               if expectedresult in actualresult:
                  defaults.append(details);
               else:
                   flag = 1;
                   break;

           if flag == 0:
               #Set the result status of execution
               tdkTestObj.setResultStatus("SUCCESS");
               print "TEST STEP 2: Get the Default WAN and priority values for DSL and WANOE";
               print "EXPECTED RESULT 2: Should get the default WAN and priority values for DSL and WANOE"
               print "ACTUAL RESULT 2 :The defaults for %s are %s:"%(paramList,defaults);
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : SUCCESS";

               setValues =["Primary","Secondary","1","0"];
               index = 0;
               for items in paramList:
                   tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                   tdkTestObj.addParameter("ParamName",items)
                   tdkTestObj.addParameter("ParamValue",setValues[index]);
                   tdkTestObj.addParameter("Type",dataType[index]);
                   expectedresult= "SUCCESS";
                   #Execute testcase on DUT
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult = tdkTestObj.getResult();
                   Setresult = tdkTestObj.getResultDetails();
                   index = index +1;
                   if expectedresult in actualresult:
                       print "set operation success for %s"%items;
                   else:
                       flag =1;
                       break;
               if flag == 1:
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP 3: Setting WAN and priortity as Primary ,1 for DSL and Secondary,2 for WANOE";
                  print "EXPECTED RESULT 3: Should set WAN and priortity as Primary ,1 for DSL and Secondary,2 for WANOE";
                  print "ACTUAL RESULT 3: set operation failed for %s"%item;
                  print "[TEST EXECUTION RESULT] : FAILURE";
               else:
                   #Set the result status of execution
                   tdkTestObj.setResultStatus("SUCCESS");
                   print "TEST STEP 3: Setting WAN and priortity as Primary ,1 for DSL and Secondary,2 for WANOE";
                   print "EXPECTED RESULT 3: Should set WAN and priortity as Primary ,1 for DSL and Secondary,2 for WANOE";
                   print "ACTUAL RESULT 3: Set operation is successful";
                   #Get the result of execution
                   print "[TEST EXECUTION RESULT] : SUCCESS";

                   print "Rebooting the device to verify the set operations done are working as expected";
                   obj1.initiateReboot();();
                   sleep(300);

                   tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                   tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.1.Wan.ActiveLink");
                   #Execute the test case in DUT
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult1 = tdkTestObj.getResult();
                   activeDSL = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                   tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
                   tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.2.Wan.ActiveLink");
                   #Execute the test case in DUT
                   tdkTestObj.executeTestCase(expectedresult);
                   actualresult2 = tdkTestObj.getResult();
                   activeWANOE = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                   if expectedresult in (actualresult1 and actualresult2):
                      if activeDSL == "true" and activeWANOE == "false":
                          #Set the result status of execution
                          tdkTestObj.setResultStatus("SUCCESS");
                          print "TEST STEP 4: Get the Active link status of DSL and WANOE";
                          print "EXPECTED RESULT 4: Active link status of DSL is expected to be true and WANOE as false";
                          print "ACTUAL RESULT 4: DSL status :%s, WANOE status : %s" %(activeDSL,activeWANOE);
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : SUCCESS";
                      else:
                          #Set the result status of execution
                          tdkTestObj.setResultStatus("FAILURE");
                          print "TEST STEP 4: Get the Active link status of DSL and WANOE";
                          print "EXPECTED RESULT 4: Active link status of DSL is expected to be true and WANOE as false";
                          print "ACTUAL RESULT 4: DSL status :%s, WANOE status : %s" %(activeDSL,activeWANOE);
                          #Get the result of execution
                          print "[TEST EXECUTION RESULT] : FAILURE";
                   else:
                       #Set the result status of execution
                       tdkTestObj.setResultStatus("FAILURE");
                       print "TEST STEP 4: Get the Active link status of DSL and WANOE";
                       print "EXPECTED RESULT 4: Active link status of DSL is expected to be true and WANOE as false";
                       print "ACTUAL RESULT 4: DSL status :%s, WANOE status : %s" %(activeDSL,activeWANOE);
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : FAILURE";
                   index =0;
                   revflg =0;
                   for item in paramList:
                       tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                       tdkTestObj.addParameter("ParamName",item)
                       tdkTestObj.addParameter("ParamValue",defaults[index]);
                       tdkTestObj.addParameter("Type",dataType[index]);
                       expectedresult= "SUCCESS";
                       #Execute testcase on DUT
                       tdkTestObj.executeTestCase(expectedresult);
                       actualresult = tdkTestObj.getResult();
                       Setresult = tdkTestObj.getResultDetails();
                       index = index +1;
                       if expectedresult in actualresult:
                          pass;
                       else:
                           revflg =1;
                   if revflg == 0:
                      tdkTestObj.setResultStatus("SUCCESS");
                      print "revert operation sucessful";
                      print "rebooting the device to apply the set operations done as apart of revert";
                      obj1.initiateReboot();();
                      sleep(300);
                   else:
                       tdkTestObj.setResultStatus("FAILURE");
                       print "revert operation failed";
           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 2: Get the Default WAN and priority values for DSL and WANOE";
               print "EXPECTED RESULT 2: Should get the default WAN and priority values for DSL and WANOE"
               print "ACTUAL RESULT 2 :The defaults for %s are %s:"%(paramList,defaults);
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
           print "#####Performing revert operation for interafce disabling and priorities if set######";
           #Revert operations
           if  revertWANOE == 1:
               tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
               result,tdkTestObj = EnableDisableInterafce(2,"true",tdkTestObj);
               if expectedresult in result:
                  tdkTestObj.setResultStatus("SUCCESS");
               else:
                   tdkTestObj.setResultStatus("FAILURE");
                   print "Enabling the WNOE interafce failed";
    else:
        objReturned.setResultStatus("FAILURE");
        print "*********DSL is not active please have a active connection********";
    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
    tadobj.unloadModule("tad");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    tadobj.setLoadModuleStatus("FAILURE");
