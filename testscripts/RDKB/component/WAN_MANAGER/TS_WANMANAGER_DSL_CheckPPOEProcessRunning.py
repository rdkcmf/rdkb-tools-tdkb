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
  <name>TS_WANMANAGER_DSL_CheckPPOEProcessRunning</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To Check if pppoe process is running When WAN Manager is Enabled with DSL Line Active</synopsis>
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
    <test_case_id>TC_WANAMANAGER_40</test_case_id>
    <test_objective>To Check if pppoe process is running When WAN Manager is Enabled with DSL Line Active.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.WAN Manager should be enabled
4.DSL Line Should be Enabled.</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>none</input_parameters>
    <automation_approch>1.Load the module
2.Check if DSL interface is present and enabled
3.Get the current value of PPP Link type , Enables status of ppp along with its ipv4 and ipv6 CP enable status
4.Enable the PPP Link type ,  status of ppp along with it enable ipv4 and ipv6 CP .
5.Check if  pppmanager process manager is running
6.Revert the enabled values
7.Unload the module
</automation_approch>
    <expected_output>On enabling PPP link parameters pppmanager is expected to run</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_DSL_CheckPPOEProcessRunning</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
import tdkutility
from tdkutility import *
from WanManager_Utility import *;
obj = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");
obj2 = tdklib.TDKScriptingLibrary("tad","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckPPOEProcessRunning');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckPPOEProcessRunning');
obj2.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckPPOEProcessRunning');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
loadmodulestatus2 =obj2.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus2 ;

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper() and loadmodulestatus2.upper()):
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    obj2.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    objReturned,dsl_wan,active = getDSLWANStatus(obj2,1);

    if active == 0:
        i=1;
        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.%s.Wan.Enable" %i);
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult and details == "true":
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2 :Check if DSL is enabled";
            print "EXPECTED RESULT 2: Should get the status of DSL";
            print "ACTUAL RESULT 2: The value received is :",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            expectedresult = "SUCCESS";
            tdkTestObj = obj2.createTestStep('TADstub_Get');
            paramList=["Device.X_RDK_WanManager.CPEInterface.2.PPP.LinkType","Device.X_RDK_WanManager.CPEInterface.2.PPP.Enable","Device.X_RDK_WanManager.CPEInterface.2.PPP.IPCPEnable","Device.X_RDK_WanManager.CPEInterface.2.PPP.IPv6CPEnable"];
            tdkTestObj,status,Value = getMultipleParameterValues(obj2,paramList);

            if expectedresult in status:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the current status of PPP Link parameters";
                print "EXPECTED RESULT 3: Should get the status of PPP Link parameters:",paramList;
                print "ACTUAL RESULT 3: The status is  ",Value;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                dataType =["string","bool","bool","bool"];
                setValue = ["PPPoE","true","true","true"];
                setflag =0;
                index = 0;
                for item in paramList:
                     tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                     tdkTestObj.addParameter("ParamName",item)
                     tdkTestObj.addParameter("ParamValue",setValue[index]);
                     tdkTestObj.addParameter("Type",dataType[index]);
                     expectedresult= "SUCCESS";
                     #Execute testcase on DUT
                     tdkTestObj.executeTestCase(expectedresult);
                     actualresult = tdkTestObj.getResult();
                     Setresult = tdkTestObj.getResultDetails();
                     index = index+1;
                     if expectedresult in actualresult:
                         print "Set operation on %s"%item;
                     else:
                         setflag =1;

                if setflag == 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Enable the  PPP Link parameters";
                    print "EXPECTED RESULT 4: Should enable PPP Link parameters:",paramList;
                    print "ACTUAL RESULT 4:  ",Setresult;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    tdkTestObj = obj1.createTestStep('ExecuteCmd');
                    cmd = "pidof pppmanager";
                    tdkTestObj.addParameter("command",cmd);
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                    if expectedresult in actualresult  and details != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Check if pppoe process is running";
                        print "EXPECTED RESULT 5:pppoe process should be running";
                        print "ACTUAL RESULT 5: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Check if pppoe process is running";
                        print "EXPECTED RESULT 5 :pppoe process should be running";
                        print "ACTUAL RESULT 5: %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                    #Revert the value to previous
                    index = 0;
                    flag =0;
                    print "TEST STEP 6 :  Performing revert operation for :",paramList;
                    for item in paramList:
                        tdkTestObj = obj.createTestStep('TDKB_TR181Stub_Set');
                        tdkTestObj.addParameter("ParamName",item)
                        tdkTestObj.addParameter("ParamValue",Value[index]);
                        tdkTestObj.addParameter("Type",dataType[index]);
                        expectedresult= "SUCCESS";
                        #Execute testcase on DUT
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        Setresult = tdkTestObj.getResultDetails();
                        index = index+1;
                        if expectedresult in actualresult:
                           print "revert operation on %s"%item;
                        else:
                            flag =1;
                    if flag == 0:
                       #Set the result status of execution
                       tdkTestObj.setResultStatus("SUCCESS");
                       print "ACTUAL RESULT 6: Revert operation is successful";
                       #Get the result of execution
                       print "[TEST EXECUTION RESULT] : SUCCESSS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 6: Revert operation failed";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Enable the PPP Link parameters";
                    print "EXPECTED RESULT 4: Should enable PPP Link parameters:",paramList;
                    print "ACTUAL RESULT 4:  ",Setresult;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the current status of PPP Link parameters";
                print "EXPECTED RESULT 3: Should get the status of PPP Link parameters:",paramList;
                print "ACTUAL RESULT 3: The status is  ",Value;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2 :Check if DSL is enabled";
            print "EXPECTED RESULT 2: Should get the status of DSL";
            print "ACTUAL RESULT 2: The value received is :",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        objReturned.setResultStatus("FAILURE");
        print "TEST STEP 1 :Check if DSL interface is active";
        print "EXPECTED RESULT 1: DSL interface is expected to be active";
        print "ACTUAL RESULT 1: DSL interface is inactive";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("tdkbtr181");
    obj1.unloadModule("sysutil");
    obj2.unloadModule("tad");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    obj2.setLoadModuleStatus("FAILURE");
