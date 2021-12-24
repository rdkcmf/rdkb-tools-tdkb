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
  <name>TS_PAM_SetMaxAddrLesserThanMinAddr_SubnetMask255.255.255.0_LanIP10.0.0.1</name>
  <primitive_test_id/>
  <primitive_test_name>pam_Setparams</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if setting a Max Address lesser than Min Address fails when the Subnet Mask is 255.255.255.0 and Lan IP is 10.0.0.1.</synopsis>
  <groups_id/>
  <execution_time>3</execution_time>
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
    <test_case_id>TC_PAM_235</test_case_id>
    <test_objective>To check if setting a Max Address lesser than Min Address fails when the Subnet Mask is 255.255.255.0 and Lan IP is 10.0.0.1.</test_objective>
    <test_type>Negative</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>subnet_mask = 255.255.255.0
lanip_addr = 10.0.0.1
min_addr = 10.0.0.10
max_addr = 10.0.0.253
max_lesser_addr = 10.0.0.8</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial values of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress and store them.
3. Check if the initial values of Subnet Mask is 255.255.255.0, Lan IP is 10.0.0.1, Min Address is 10.0.0.10 and Max Address is 10.0.0.253. If not set them to the required values. Cross check the GET with SET if required.
4. Set the Max Address to a value lesser than Min Address such as 10.0.0.8 with respect to the Subnet Mask and Lan IP and check if the SET operation returns failure.
5. Revert to initial values if required
6. Unload the modules</automation_approch>
    <expected_output>Setting a Max Address lesser than Min Address should fail when the Subnet Mask is 255.255.255.0 and Lan IP is 10.0.0.1.</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_SetMaxAddrLesserThanMinAddr_SubnetMask255.255.255.0_LanIP10.0.0.1</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def setMaxAddr(obj1, step, addr):
    expectedresult = "FAILURE";
    tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_Set");
    tdkTestObj.addParameter("ParamName", "Device.DHCPv4.Server.Pool.1.MaxAddress");
    tdkTestObj.addParameter("ParamValue", addr);
    tdkTestObj.addParameter("Type", "string");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print"\nSetting the Max Address lesser than Min Address : %s"%addr;
    print "TEST STEP %d : Set Device.DHCPv4.Server.Pool.1.MaxAddress to an address %s which is lower than Min Address" %(step, addr);
    print "EXPECTED RESULT %d : SET operations should Fail as the Max Address is lesser than Min Address" %step;

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Set operation failed as expected as the Max Addr is less than Min Addr; Details : %s" %(step, details);
        print "TEST EXECUTION RESULT :SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Set operation is success even through the Max Addr is less than Min Addr; Details : %s" %(step, details);
        print "TEST EXECUTION RESULT : FAILURE";
    return;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkutility import *
import time;
from tdkbVariables import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
obj1 = tdklib.TDKScriptingLibrary("tdkbtr181","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_SetMaxAddrLesserThanMinAddr_SubnetMask255.255.255.0_LanIP10.0.0.1');
obj1.configureTestCase(ip,port,'TS_PAM_SetMinAddrGreaterThanMaxAddr_SubnetMask255.255.0.0_LanIP10.0.0.1');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

#Valid Min and Max Address
min_addr = "10.0.0.10";
max_addr = "10.0.0.253";

#Max Address lesser than Min Address
max_lesser_addr = "10.0.0.8";

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    tdkTestObj = obj.createTestStep('TADstub_Get');
    paramList=["Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask", "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress", "Device.DHCPv4.Server.Pool.1.MinAddress", "Device.DHCPv4.Server.Pool.1.MaxAddress"]
    tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)
    print "\nTEST STEP 1: Get the initial values of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress";
    print "EXPECTED RESULT 1 : The values should be retrieved successfully";

    if expectedresult in status and orgValue[0] != "" and orgValue[1] != "" and orgValue[2] != "" and orgValue[3] != "":
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: Lan Subnet Mask is : %s, Lan IP Address is : %s, Min Address is : %s, Max Address is : %s" %(orgValue[0],orgValue[1], orgValue[2], orgValue[3]) ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        if orgValue[0] == "255.255.255.0" and orgValue[1] == "10.0.0.1" and orgValue[2] == min_addr and orgValue[3] == max_addr :
            #Set the Max Address less than Min Addr
            step = 2;
            setMaxAddr(obj1, step, max_lesser_addr);
        else :
            #values to be set
            expectedresult = "SUCCESS";
            subnet_mask = "255.255.255.0"
            lanip_addr = "10.0.0.1";
            tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
            tdkTestObj.addParameter("paramList", "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask|%s|string|Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress|%s|string|Device.DHCPv4.Server.Pool.1.MinAddress|%s|string|Device.DHCPv4.Server.Pool.1.MaxAddress|%s|string"%(subnet_mask,lanip_addr,min_addr,max_addr));
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            sleep(30);

            print "\nTEST STEP 2 : Set Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to %s, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to %s, Device.DHCPv4.Server.Pool.1.MinAddress to %s and Device.DHCPv4.Server.Pool.1.MaxAddress to %s" %(subnet_mask,lanip_addr,min_addr,max_addr);
            print "EXPECTED RESULT 2 : SET operations should be success";

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: Set operation success; Details : %s" %details;
                print "TEST EXECUTION RESULT :SUCCESS";

                #Validate the SET with GET
                paramList=["Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask", "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress", "Device.DHCPv4.Server.Pool.1.MinAddress", "Device.DHCPv4.Server.Pool.1.MaxAddress"];
                tdkTestObj,status,setValue = getMultipleParameterValues(obj,paramList)

                print "\nTEST STEP 3: Get the values of Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress, Device.DHCPv4.Server.Pool.1.MinAddress and Device.DHCPv4.Server.Pool.1.MaxAddress";
                print "EXPECTED RESULT 3: The values should be retrieved successfully and should be the same as set values";

                if expectedresult in status and setValue[0] == subnet_mask and setValue[1] == lanip_addr and setValue[2] == min_addr and setValue[3] == max_addr:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 3: Values after the GET are same as the SET values : %s, %s, %s" %(setValue[0],setValue[1],setValue[2]) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Set the Max Address less than Min Addr
                    step = 4;
                    setMaxAddr(obj1, step, max_lesser_addr);

                    #Revert to initial values
                    print "\nReverting to initial state...";
                    tdkTestObj = obj1.createTestStep("TDKB_TR181Stub_SetMultiple");
                    tdkTestObj.addParameter("paramList", "Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask|%s|string|Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress|%s|string|Device.DHCPv4.Server.Pool.1.MinAddress|%s|string|Device.DHCPv4.Server.Pool.1.MaxAddress|%s|string"%(orgValue[0], orgValue[1], orgValue[2], orgValue[3]));
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    sleep(30);

                    print "\nTEST STEP 5 : Set Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanSubnetMask to %s, Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanIPAddress to %s, Device.DHCPv4.Server.Pool.1.MinAddress to %s and Device.DHCPv4.Server.Pool.1.MaxAddress to %s" %(orgValue[0],orgValue[1],orgValue[2],orgValue[3]);
                    print "EXPECTED RESULT 5 : SET operations should be success";

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 5: Set operation success; Details : %s" %details;
                        print "TEST EXECUTION RESULT :SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 5:Set operation failed; Details : %s" %details;
                        print "TEST EXECUTION RESULT :FAILURE";
                else :
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 3: Values after the GET are not same as the SET values : %s, %s, %s, %s" %(setValue[0],setValue[1],setValue[2],setValue[3]) ;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2:Set operation failed; Details : %s" %details;
                print "TEST EXECUTION RESULT :FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: GET operation failed";
        print "TEST EXECUTION RESULT :FAILURE";

    obj.unloadModule("tad");
    obj1.unloadModule("tdkbtr181");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
