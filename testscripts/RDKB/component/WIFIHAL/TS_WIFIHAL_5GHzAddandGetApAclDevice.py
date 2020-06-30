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
  <version>3</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzAddandGetApAclDevice</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetApAclDevices</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Add a new MAC in ACL list of 5GHZ using wifi_addApAclDevice() and check using wifi_getApAclDevices() whether new MAC is available in ACL list</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_373</test_case_id>
    <test_objective>Add a new MAC in 5GHZ ACL list using wifi_addApAclDevice() and check using wifi_getApAclDevices() whether new MAC is available in ACL list</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
</pre_requisite>
    <api_or_interface_used>wifi_getApAclDevice()
wifi_addApAclDevice()
wifi_delApAclDevice()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the module
2. Get the current list of Acl devices using wifi_getApAclDevice() and save it
3. Add a new MAC to Acl list using wifi_addApAclDevice()
4. Get the list of Acl devices using wifi_getApAclDevice() and check if it has the new MAC added
5. Delete the newly added MAC from Acl list using wifi_delApAclDevice()
6. Unload Wifihal module</automation_approch>
    <expected_output>A new MAC added to 5GHZ ACL list using wifi_addApAclDevice() should be reflected in next wifi_getApAclDevices() </expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzAddandGetApAclDevice</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import random;

radio = "5G"

def GetApAclDevices(tdkTestObj, radioIndex):
    tdkTestObj.addParameter("apIndex", radioIndex);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "Mac Details",details
    macAddress= []
    mac_count = 0
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");

        mac_count = int(details.split(';')[3].split('=')[1]);
        if mac_count > 0:
            macAddress = details.split(";")[1].strip().split("n")
            for i in range(len(macAddress)):
                macAddress[i] =  macAddress[i].replace("\\", '')
            if '' in macAddress:
                macAddress.remove('')
        print "TEST STEP: Get the Acl Devices"
        print "EXPECTED RESULT: Should get the list of acl devices"
        print "List of Acl Devices MAC Address:",macAddress
        print "TEST EXECUTION RESULT :SUCCESS"
    else:
        print "TEST STEP: Get the Acl Devices List"
        print "EXPECTED RESULT: Should get the total list of associated devices"
        print "ACTUAL RESULT : wifi_getApAclDevices call failed"
        print "TEST EXECUTION RESULT :FAILURE"
        tdkTestObj.setResultStatus("FAILURE");

    return actualresult, mac_count, macAddress

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzAddandGetApAclDevice');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
	expectedresult = "SUCCESS"
	radioIndex = idx
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAclDevices');
        actualresult, mac_count, macAddress = GetApAclDevices(tdkTestObj, radioIndex)

        if expectedresult in actualresult:
            addMAC = "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))

            if mac_count > 0:
                while 1:
                    if addMAC not in macAddress:
                        break;
                    addMAC = "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))

            print "MAC to be added is ", addMAC;
            #Add the new MAC to ACL list
            tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
            tdkTestObj.addParameter("methodName","addApAclDevice");
            tdkTestObj.addParameter("apIndex",radioIndex);
            tdkTestObj.addParameter("DeviceMacAddress",addMAC);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print"Successfully added ApAclDevice", addMAC

                #Invoke wifi_getApAclDevices() to verify addApAcl
                tdkTestObj = obj.createTestStep('WIFIHAL_GetApAclDevices');
                actualresult, mac_count, macAddress = GetApAclDevices(tdkTestObj, radioIndex)
                if expectedresult in actualresult and mac_count>0:
                    if addMAC in macAddress:
                        print "wifi_addApAclDevice() successfully verified using wifi_getApAclDevices()";
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST EXECUTION RESULT :SUCCESS"
                        #Delete the ACL MAC added for testing
                        tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
                        tdkTestObj.addParameter("methodName","delApAclDevice");
                        tdkTestObj.addParameter("apIndex",radioIndex);
                        tdkTestObj.addParameter("DeviceMacAddress",addMAC);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();
                        if expectedresult in actualresult:
                            print "TEST STEP: Delete the added Acl Device"
                            print "EXPECTED RESULT: Should Delete the added Acl Device"
                            print "TEST EXECUTION RESULT :SUCCESS"
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "Deleted device :", addMAC
                        else:
                            print "TEST STEP: Delete the added Acl Device"
                            print "EXPECTED RESULT: Should Delete the added Acl Device"
                            print "TEST EXECUTION RESULT :FAILURE"
                            tdkTestObj.setResultStatus("FAILURE");
                            print "addApAclDevice failed not reverted back"
                    else:
                        print "wifi_addApAclDevice() verification using wifi_getApAclDevices() failed. New MAC not found in AclDevice list";
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST EXECUTION RESULT :FAILURE"
                else:
                    print "wifi_getApAclDevices() failed after wifi_addApAclDevice()"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"wifi_addApAclDevice() operation failed after add operation";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print"wifi_getApAclDevices() operation failed";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
