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
  <name>TS_WANMANAGER_DSL_CheckLTimeDateAndTimeOffset</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if LTime ,date and Time offset are populated properly with active DSL Line</synopsis>
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
    <test_case_id>TC_WANMANAGER_41</test_case_id>
    <test_objective>This test case is to check if LTime ,date and Time offset are populated properly with active DSL Line</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.WAN Manager should be enabled
4.DSL Line Should be Enabled </pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>none</input_parameters>
    <automation_approch>1.Load the module
2.Check if DSL is present and enabled
3.Get the LTime and date of the DUT and are expected to be nonempty and unequal
4.Check the TImeoffset and should not be empty
5.Unload the module</automation_approch>
    <expected_output>Ltime and date are expected to be nonempty and unequal .</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_DSL_CheckLTimeDateAndTimeOffset</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>none</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
import tdklib;
import time;
from WanManager_Utility import *;
#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
tadobj =  tdklib.TDKScriptingLibrary("tad","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>

sysObj.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckLTimeDateAndTimeOffset');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckLTimeDateAndTimeOffset');
tadobj.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckLTimeDateAndTimeOffset');
#Get the result of connection with test component and DUT
loadmodulestatus1 =sysObj.getLoadModuleResult();
loadmodulestatus2 =obj1.getLoadModuleResult();
loadmodulestatus3 =tadobj.getLoadModuleResult();

if "SUCCESS" in (loadmodulestatus1.upper() and loadmodulestatus2.upper() and loadmodulestatus3.upper()) :
    #Set the result status of execution
    sysObj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    revertWANOE =0;
    expectedresult="SUCCESS";
    tadobj.setLoadModuleStatus("SUCCESS");

    objReturned,dsl_wan,active = getDSLWANStatus(tadobj,1);

    if active == 0:
        i=1;
        tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
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

            print "******performing a pre-requisite where in WANOE inteface is expected to be disabled ***";
            tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
            tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.2.Wan.Enable");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult and details == "true":
                print "WANOE is enabled and disabling it ";
                tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
                result,tdkTestObj = EnableDisableInterafce(2,"false",tdkTestObj);
                revertWANOE = 1;

            tdkTestObj = sysObj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", "LTime");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult1 = tdkTestObj.getResult();
            LTime= tdkTestObj.getResultDetails().strip().replace("\\n","");

            tdkTestObj = sysObj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", "date");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult2 = tdkTestObj.getResult();
            date= tdkTestObj.getResultDetails().strip().replace(" ",",");
            if expectedresult in (actualresult2 and actualresult1):
                date= date.split(",")[3];
                if "" != (LTime and date)  and LTime !=  date:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3 :Get the LTime and date ";
                    print "EXPECTED RESULT 3: Should get the LTime and date unequal";
                    print "ACTUAL RESULT 3 :Ltime :%s and date : %s" %(LTime,date);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
                    tdkTestObj.addParameter("ParamName","Device.Time.TimeOffset");
                    #Execute the test case in DUT
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().replace("\\n","");
                    if expectedresult in actualresult and details!= "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4:Get the Time offset";
                        print "EXPECTED RESULT 4: Should get the Time offset non empty";
                        print "ACTUAL RESULT 4: Timeoffset is :%s"%details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4:Get the Time offset";
                        print "EXPECTED RESULT 4: Should get the Time offset non empty";
                        print "ACTUAL RESULT 4: Timeoffset is :%s"%details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3 :Get the LTime and date ";
                    print "EXPECTED RESULT 3: Should get the LTime and date unequal";
                    print "ACTUAL RESULT 3 :Ltime :%s and date : %s" %(LTime,date);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] :FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3 :Get the LTime and date ";
                print "EXPECTED RESULT 3: Should get the LTime and date";
                print "ACTUAL RESULT 3 : Get operation failed";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] :FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2 :Check if DSL is enabled";
            print "EXPECTED RESULT 2: Should get the status of DSL";
            print "ACTUAL RESULT 2: The value received is :",details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        print "TEST STEP 1 :Check if DSL interface is active";
        print "EXPECTED RESULT 1: DSL interface is expected to be active";
        print "ACTUAL RESULT 1: DSL interface is inactive";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    #Revert operations
    if  revertWANOE == 1:
         tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
         result,tdkTestObj = EnableDisableInterafce(2,"true",tdkTestObj);
         if expectedresult in result:
             tdkTestObj.setResultStatus("SUCCESS");
             print "WANOE revert operation successfull";
         else:
             tdkTestObj.setResultStatus("FAILURE");
             print "Enabling the WNOE interafce failed at revert step";

    sysObj.unloadModule("sysutil");
    obj1.unloadModule("tdkbtr181");
    tadobj.unloadModule("tad");
else:
    print "Failed to load sysutil module";
    sysObj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    tadobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
