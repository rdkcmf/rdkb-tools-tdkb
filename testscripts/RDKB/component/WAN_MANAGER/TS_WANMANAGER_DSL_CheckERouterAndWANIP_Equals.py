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
  <name>TS_WANMANAGER_DSL_CheckERouterAndWANIP_Equals</name>
  <primitive_test_id/>
  <primitive_test_name>wanmanager_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To Check eRouter IP address equals to WAN IP when WAN Manager is Enabled with a active DSL Line</synopsis>
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
    <test_case_id>TC_WANMANAGER_42</test_case_id>
    <test_objective>This test case is to Check eRouter IP address equals to WAN IP when WAN Manager is Enabled with a active DSL Line</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.WAN Manager should be enabled
4. DSL Line Should be Enabled.</pre_requisite>
    <api_or_interface_used>none</api_or_interface_used>
    <input_parameters>none</input_parameters>
    <automation_approch>1.Load the module
2.Check if  DSL interface is present and enabled
3.Get the ipv4 wan address and ipv4 erouter0 address
4.The ip addresses are expected to be present and equal
5.Unload the module</automation_approch>
    <expected_output>Ipv4 wan address and ipv4 erouter0 address are expected to be present and equal</expected_output>
    <priority>High</priority>
    <test_stub_interface>WAN MANAGER</test_stub_interface>
    <test_script>TS_WANMANAGER_DSL_CheckERouterAndWANIP_Equals</test_script>
    <skipped>No</skipped>
    <release_version>M89</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
from WanManager_Utility import *;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
obj1= tdklib.TDKScriptingLibrary("tdkbtr181","RDKB");
tadobj= tdklib.TDKScriptingLibrary("tad","RDKB");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckERouterAndWANIP_Equals');
obj1.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckERouterAndWANIP_Equals');
tadobj.configureTestCase(ip,port,'TS_WANMANAGER_DSL_CheckERouterAndWANIP_Equals');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
loadmodulestatus2 = tadobj.getLoadModuleResult();

if "SUCCESS" in loadmodulestatus.upper() and  "SUCCESS" in loadmodulestatus1.upper() and  "SUCCESS" in loadmodulestatus2.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tadobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    revertWANOE =0;
    objReturned,dsl_wan,active = getDSLWANStatus(tadobj,1);

    if active == 0:
        i =1;
        tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Get');
        tdkTestObj.addParameter("ParamName","Device.X_RDK_WanManager.CPEInterface.%s.Wan.Enable" %i);
        #Execute the test case in DUT
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
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

            query="sysevent get ipv4_wan_ipaddr";
            print "query:%s" %query
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", query)
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult1 = tdkTestObj.getResult();
            wan_ip = tdkTestObj.getResultDetails().strip().replace("\\n","");

            query="sysevent get ipv4_erouter0_ipaddr";
            print "query:%s" %query
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", query)
            expectedresult2="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult2 = tdkTestObj.getResult();
            erouter_ip = tdkTestObj.getResultDetails().strip().replace("\\n","");

            query="ifconfig erouter0 | grep -i \"inet addr:\"";
            print "query:%s" %query
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", query)
            expectedresult2="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult3 = tdkTestObj.getResult();
            ifconfig_ip = tdkTestObj.getResultDetails().split(":")[1].split(" ")[0];

            if expectedresult in (actualresult1 and actualresult2 and actualresult3):
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3 :Get th ipv4 address for wan and erouter0 ip from syscfg and ifconfig";
                print "EXPECTED RESULT 3: Should get ipv4 address for wan and erouter0 ip from syscfg and ifconfig";
                print "ACTUAL RESULT 3: wan_ip : %s,erouter_ip :%s,ifconfig erouter ip :%s"%(wan_ip,erouter_ip,ifconfig_ip);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                if details == "true":
                    print "The DSL is enabled , wan ip and erouter0 ip are expected to be non-empty";
                    if wan_ip != "" and erouter_ip != "" and ifconfig_ip != "" and (wan_ip == erouter_ip == ifconfig_ip):
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4 :check if ipv4 address for wan and erouter0 are non empty and equal";
                        print "EXPECTED RESULT 4: Should get ipv4 address for wan and erouter0 non empty and equal";
                        print "ACTUAL RESULT 4: wan_ip : %s,erouter_ip :%s,ifconfig erouter ip :%s"%(wan_ip,erouter_ip,ifconfig_ip);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4:check if ipv4 address for wan and erouter0 are non-empty and equal";
                        print "EXPECTED RESULT 4: Should get ipv4 address for wan and erouter0 are non-empty and equal";
                        print "ACTUAL RESULT 4: wan_ip : %s,erouter_ip :%s,ifconfig erouter ip :%s"%(wan_ip,erouter_ip,ifconfig_ip);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "TEST STEP 4:check if ipv4 address for wan and erouter0 are empty";
                    print "EXPECTED RESULT 4: Should get ipv4 address for wan and erouter0 empty";
                    print "ACTUAL RESULT 4: wan_ip : %s,erouter_ip :%s,ifconfig erouter ip :%s"%(wan_ip,erouter_ip,ifconfig_ip);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3 :Get th ipv4 address for wan and erouter0";
                print "EXPECTED RESULT 3: Should get ipv4 address for wan and erouter0";
                print "ACTUAL RESULT 3: wan_ip : %s,erouter_ip :%s,ifconfig erouter ip :%s"%(wan_ip,erouter_ip,ifconfig_ip);
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
    #Revert operations
    if  revertWANOE == 1:
         tdkTestObj = obj1.createTestStep('TDKB_TR181Stub_Set');
         result,tdkTestObj = EnableDisableInterafce(2,"true",tdkTestObj);
         if expectedresult in result:
             tdkTestObj.setResultStatus("SUCCESS");
         else:
             tdkTestObj.setResultStatus("FAILURE");
             print "Enabling the WNOE interafce failed";
    obj.unloadModule("sysutil");
    obj1.unloadModule("tdkbtr181");
    tadobj.unloadModule("tad");
else:
    print "Failed to load sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    tadobj.setLoadModuleStatus("FAILURE");
