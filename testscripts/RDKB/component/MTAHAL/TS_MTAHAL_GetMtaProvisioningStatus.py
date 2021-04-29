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
  <version>5</version>
  <name>TS_MTAHAL_GetMtaProvisioningStatus</name>
  <primitive_test_id/>
  <primitive_test_name>MTAHAL_GetMtaProvisioningStatus</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the MTAHAL API mta_hal_getMtaProvisioningStatus() and get the current Provisioning Status.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_MTAHAL_68</test_case_id>
    <test_objective>Invoke the MTAHAL API mta_hal_getMtaProvisioningStatus() and get the current Provisioning Status. Check if the value of Device.DeviceInfo.X_COMCAST-COM_MTA_IP is obtained as expected for the Provisioning Status.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>MTAHAL_GetMtaProvisioningStatus</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load the mtahal module
2. Invoke the HAL API mta_hal_getMtaProvisioningStatus() and get the Provisioning Status.
3. Get the MTA IP from Device.DeviceInfo.X_COMCAST-COM_MTA_IP
4. If status is MTA_NON_PROVISIONED, then MTA IP should be 0.0.0.0. If status is MTA_PROVISIONED then a valid MTA IP should be obtained when Device.DeviceInfo.X_COMCAST-COM_MTA_IP is queried.
5. Unload the module</automation_approch>
    <expected_output>mta_hal_getMtaProvisioningStatus() should be invoked and the current Provisioning Status retrieved successfully. The value of Device.DeviceInfo.X_COMCAST-COM_MTA_IP should be obtained as expected for the Provisioning Status retrieved.</expected_output>
    <priority>High</priority>
    <test_stub_interface>MTAHAL</test_stub_interface>
    <test_script>TS_MTAHAL_GetMtaProvisioningStatus</test_script>
    <skipped>No</skipped>
    <release_version>M88</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("mtahal","1")
pamobj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MTAHAL_GetMtaProvisioningStatus')
pamobj.configureTestCase(ip,port,'TS_MTAHAL_GetMtaProvisioningStatus')

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult()
loadmodulestatus1 =pamobj.getLoadModuleResult()
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in (loadmodulestatus.upper() and loadmodulestatus1.upper()):
    obj.setLoadModuleStatus("SUCCESS")
    pamobj.setLoadModuleStatus("SUCCESS")
    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("MTAHAL_GetMtaProvisioningStatus")
    pamtdkTestObj = pamobj.createTestStep("pam_GetParameterValues")
    expectedresult="SUCCESS"
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    resultDetails = tdkTestObj.getResultDetails()

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS")
        print "TEST STEP 1: Invoke the MTAHAL API mta_hal_getMtaProvisioningStatus()"
        print "EXPECTED RESULT 1: Should invoke mta_hal_getMtaProvisioningStatus() successfully"
        print "ACTUAL RESULT 1:  mta_hal_getMtaProvisioningStatus() API invoked successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"

        if resultDetails != "":
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS")
            print "TEST STEP 2: Get MTA Provisioning Status"
            print "EXPECTED RESULT 2: Should get MTA Provisioning status successfully"
            print "ACTUAL RESULT 2:  %s" %resultDetails;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"
            status = resultDetails.split(":")[1].split(' ')[0];

            pamtdkTestObj.addParameter("ParamName","Device.DeviceInfo.X_COMCAST-COM_MTA_IP");
            expectedresult="SUCCESS";
            pamtdkTestObj.executeTestCase(expectedresult);
            actualresult = pamtdkTestObj.getResult();

            if expectedresult in actualresult :
                mta_ip = pamtdkTestObj.getResultDetails();
                #Set the result status of execution
                pamtdkTestObj.setResultStatus("SUCCESS")
                print "TEST STEP 3: Get MTA IP from Device.DeviceInfo.X_COMCAST-COM_MTA_IP"
                print "EXPECTED RESULT 3: Should get MTA IP from Device.DeviceInfo.X_COMCAST-COM_MTA_IP"
                print "ACTUAL RESULT 3:  Device.DeviceInfo.X_COMCAST-COM_MTA_IP is : %s" %mta_ip;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS"
                non_prov_ip = "0.0.0.0"

                if status == "MTA_NON_PROVISIONED":
                    if mta_ip in non_prov_ip :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS")
                        print "TEST STEP 4: Check if the MTA IP is %s as the Provisioning status is MTA_NON_PROVISIONED" %non_prov_ip;
                        print "EXPECTED RESULT 4: The MTA IP should be %s as the Provisioning status is MTA_NON_PROVISIONED" %non_prov_ip;
                        print "ACTUAL RESULT 4:  The MTA IP is %s as the the Provisioning status is MTA_NON_PROVISIONED" %mta_ip;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS"
                    else :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE")
                        print "TEST STEP 4: Check if the MTA IP is %s as the Provisioning status is MTA_NON_PROVISIONED" %non_prov_ip;
                        print "EXPECTED RESULT 4: The MTA IP should be %s as the Provisioning status is MTA_NON_PROVISIONED" %non_prov_ip;
                        print "ACTUAL RESULT 4:  The MTA IP is %s as the the Provisioning status is MTA_NON_PROVISIONED" %mta_ip;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE"

                else:
                    if mta_ip not in non_prov_ip :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS")
                        print "TEST STEP 4: Check if the MTA IP is not %s as the Provisioning status is MTA_PROVISIONED" %non_prov_ip;
                        print "EXPECTED RESULT 4: The MTA IP should not be %s as the Provisioning status is MTA_PROVISIONED" %non_prov_ip;
                        print "ACTUAL RESULT 4:  The MTA IP is %s as the the Provisioning status is MTA_PROVISIONED" %mta_ip;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS"
                    else :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE")
                        print "TEST STEP 4: Check if the MTA IP is not %s as the Provisioning status is MTA_PROVISIONED" %non_prov_ip;
                        print "EXPECTED RESULT 4: The MTA IP should not be %s as the Provisioning status is MTA_PROVISIONED" %non_prov_ip;
                        print "ACTUAL RESULT 4:  The MTA IP is %s as the the Provisioning status is MTA_PROVISIONED" %mta_ip;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE"
            else :
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE")
                print "TEST STEP 3: Get MTA IP from Device.DeviceInfo.X_COMCAST-COM_MTA_IP"
                print "EXPECTED RESULT 3: Should get MTA IP from Device.DeviceInfo.X_COMCAST-COM_MTA_IP"
                print "ACTUAL RESULT 3:  Device.DeviceInfo.X_COMCAST-COM_MTA_IP is not retrieved"
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print "TEST STEP 2: Get MTA Provisioning Status"
            print "EXPECTED RESULT 2: Should get MTA Provisioning status successfully"
            print "ACTUAL RESULT 2: Failed to get MTA Provisioning status, Details: %s" %resultDetails;
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print "TEST STEP 1: Invoke the MTAHAL API mta_hal_getMtaProvisioningStatus()"
        print "EXPECTED RESULT 1: Should invoke mta_hal_getMtaProvisioningStatus() successfully"
        print "ACTUAL RESULT 1:  mta_hal_getMtaProvisioningStatus() API not invoked successfully";
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("mtahal")
    pamobj.unloadModule("pam")
else:
    print "Failed to load the module"
    obj.setLoadModuleStatus("FAILURE")
    pamobj.setLoadModuleStatus("FAILURE")
    print "Module loading failed"

