##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_CMHAL_GetDHCPInfoTimeRemaining</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>CMHAL_GetParamCharValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get DhcpLeaseTimeRemaining,DhcpRebindTimeRemaining, DhcpRenewTimeRemaining of IPV4 or IPV6 depending upon the IPtype</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
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
    <test_case_id>TC_CMHAL_76</test_case_id>
    <test_objective>To get DhcpLeaseTimeRemaining,DhcpRebindTimeRemaining, DhcpRenewTimeRemaining of IPV4 or IPV6 depending upon the IPtype</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>cm_hal_GetDHCPInfo,cm_hal_GetIPv6DHCPInfo</api_or_interface_used>
    <input_parameters>Ipv4DhcpLeaseTimeRemaining,Ipv4DhcpRebindTimeRemaining,Ipv4DhcpRenewTimeRemaining,IPV6LeaseTimeRemaining,IPv6RebindTimeRemaining,IPv6RenewTimeRemaining</input_parameters>
    <automation_approch>1. Load  cmhal module
2. Get the ip type.If it is IPV4,Invoke cm_hal_GetDHCPInfo and get Ipv4DhcpLeaseTimeRemaining,Ipv4DhcpRebindTimeRemaining,Ipv4DhcpRenewTimeRemaining 
3. If it is IPV6,Invoke cm_hal_GetIPv6DHCPInfo and get IPV6LeaseTimeRemaining,IPv6RebindTimeRemaining,IPv6RenewTimeRemaining
4. Unload cmhal module</automation_approch>
    <except_output>Should get DhcpLeaseTimeRemaining,DhcpRebindTimeRemaining, DhcpRenewTimeRemaining of IPV4 or IPV6 depending upon the IPtype</except_output>
    <priority>High</priority>
    <test_stub_interface>CMHAL</test_stub_interface>
    <test_script>TS_CMHAL_GetDHCPInfoTimeRemaining</test_script>
    <skipped>No</skipped>
    <release_version>M67</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_GetDHCPInfoTimeRemaining');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("CMHAL_GetParamCharValue");
    tdkTestObj.addParameter("paramName","ProvIpType");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    IPType = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and IPType != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the provisioned wan0 iptype";
        print "EXPECTED RESULT 1: Should get the provisioned wan0 iptype successfully";
        print "ACTUAL RESULT 1: IPType is %s" %IPType;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if "IPV6" in IPType.upper():
            tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
            tdkTestObj.addParameter("paramName","IPv6LeaseTimeRemaining");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            IPv6LeaseTimeRemaining = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult and IPv6LeaseTimeRemaining != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Get the IPV6LeaseTimeRemaining";
                print "EXPECTED RESULT 2: Should get the IPV6LeaseTimeRemaining";
                print "ACTUAL RESULT 2: IPV6LeaseTimeRemaing: %s" %IPv6LeaseTimeRemaining;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
                tdkTestObj.addParameter("paramName","IPv6RebindTimeRemaining");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                IPv6RebindTimeRemaining = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult and IPv6RebindTimeRemaining != "":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 3: Get the IPv6RebindTimeRemaining";
                    print "EXPECTED RESULT 3: Should get the IPv6RebindTimeRemaining";
                    print "ACTUAL RESULT 3: IPv6RebindTimeRemaining: %s" %IPv6RebindTimeRemaining;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
                    tdkTestObj.addParameter("paramName","IPv6RenewTimeRemaining");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    IPv6RenewTimeRemaining = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                    if expectedresult in actualresult and IPv6RenewTimeRemaining != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 4: Get the IPv6RenewTimeRemaining";
                        print "EXPECTED RESULT 4: Should get the IPv6RenewTimeRemaining";
                        print "ACTUAL RESULT 4: IPv6RenewTimeRemaining: %s" %IPv6RenewTimeRemaining;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 4: Get the IPv6RenewTimeRemaining";
                        print "EXPECTED RESULT 4: Should get the IPv6RenewTimeRemaining";
                        print "ACTUAL RESULT 4:Failed to get IPv6RenewTimeRemaining";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Get the IPv6RebindTimeRemaining";
                    print "EXPECTED RESULT 3: Should get the IPv6RebindTimeRemaining";
                    print "ACTUAL RESULT 3: Failed to get IPv6RebindTimeRemaining";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 2: Get the IPV6LeaseTimeRemaining";
                print "EXPECTED RESULT 2: Should get the IPV6LeaseTimeRemaining";
                print "ACTUAL RESULT 2: Failed to get IPV6LeaseTimeRemaing: ";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        elif "IPV4" in IPType.upper():
            tdkTestObj = obj.createTestStep("CMHAL_GetParamUlongValue");
            tdkTestObj.addParameter("paramName","Ipv4DhcpLeaseTimeRemaining");
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            Ipv4DhcpLeaseTimeRemaining = tdkTestObj.getResultDetails().strip().replace("\\n", "");
            if expectedresult in actualresult and Ipv4DhcpLeaseTimeRemaining != "":
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 5: Get the Ipv4DhcpLeaseTimeRemaining";
                print "EXPECTED RESULT 5: Should get the Ipv4DhcpLeaseTimeRemaining";
                print "ACTUAL RESULT 5: Ipv4DhcpLeaseTimeRemaining: %s" %Ipv4DhcpLeaseTimeRemaining;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                tdkTestObj = obj.createTestStep("CMHAL_GetParamCharValue");
                tdkTestObj.addParameter("paramName","Ipv4DhcpRebindTimeRemaining");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                Ipv4DhcpRebindTimeRemaining = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if expectedresult in actualresult and Ipv4DhcpRebindTimeRemaining != "":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 6: Get the Ipv4DhcpRebindTimeRemaining";
                    print "EXPECTED RESULT 6: Should get the Ipv4DhcpRebindTimeRemaining";
                    print "ACTUAL RESULT 6:Ipv4DhcpRebindTimeRemaining: %s" %Ipv4DhcpRebindTimeRemaining;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    tdkTestObj = obj.createTestStep("CMHAL_GetParamCharValue");
                    tdkTestObj.addParameter("paramName","Ipv4DhcpRenewTimeRemaining");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    Ipv4DhcpRenewTimeRemaining = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                    if expectedresult in actualresult and Ipv4DhcpRenewTimeRemaining != "":
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 7: Get the Ipv4DhcpRenewTimeRemaining";
                        print "EXPECTED RESULT 7: Should get the Ipv4DhcpRenewTimeRemaining";
                        print "ACTUAL RESULT 7: Ipv4DhcpRenewTimeRemaining: %s" %Ipv4DhcpRenewTimeRemaining;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 7: Get the Ipv4DhcpRenewTimeRemaining";
                        print "EXPECTED RESULT 7: Should get the Ipv4DhcpRenewTimeRemaining";
                        print "ACTUAL RESULT 7:Failed to get Ipv4DhcpRenewTimeRemaining";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 6: Get the Ipv4DhcpRebindTimeRemaining";
                    print "EXPECTED RESULT 6: Should get the Ipv4DhcpRebindTimeRemaining";
                    print "ACTUAL RESULT 6: Failed to get Ipv4DhcpRebindTimeRemaining";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 5: Get the Ipv4DhcpLeaseTimeRemaining";
                print "EXPECTED RESULT 5: Should get the Ipv4DhcpLeaseTimeRemaining";
                print "ACTUAL RESULT 5: Failed to get Ipv4DhcpLeaseTimeRemaining: ";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the provisioned wan0 iptype";
        print "EXPECTED RESULT 1: Should get the provisioned wan0 iptype successfully";
        print "ACTUAL RESULT 1: Failed to get IPType";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("cmhal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

