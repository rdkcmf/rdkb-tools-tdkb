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
  <name>TS_WIFIHAL_6GHzAddandGetApAclDevice</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_AddorDelApAclDevice</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To add a new MAC address using the HAL API wifi_addApAclDevice() and verify if the MAC is added properly using wifi_getApAclDevices() API for 6GHz access point.</synopsis>
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
    <test_case_id>TC_WIFIHAL_633</test_case_id>
    <test_objective>To add a new MAC address using the HAL API wifi_addApAclDevice() and verify if the MAC is added properly using wifi_getApAclDevices() API for 6GHz access point.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_addApAclDevice()
wifi_getApAclDevices()
wifi_delApAclDevice()
</api_or_interface_used>
    <input_parameters>methodname : addApAclDevice
methodname : getApAclDevices
methodname : delApAclDevice
apIndex : fetched from platform property file
DeviceMacAddress : dynamically generated
</input_parameters>
    <automation_approch>1.Load the module
2. Get the 6GHz access point index from platform property file
3. Get the current list of Acl devices using wifi_getApAclDevice() and save it
4. Add a new MAC to Acl list using wifi_addApAclDevice()
5. Get the list of Acl devices using wifi_getApAclDevice() and check if it has the new MAC added
6. Delete the newly added MAC from Acl list using wifi_delApAclDevice()
7. Unload Wifihal module</automation_approch>
    <expected_output>A new MAC added to 6GHz ACL list using wifi_addApAclDevice() should be reflected in next wifi_getApAclDevices()</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_6GHzAddandGetApAclDevice</test_script>
    <skipped>No</skipped>
    <release_version>M94</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from random import randint;

def GetApAclDevices(tdkTestObj, apIndex, step):
    tdkTestObj.addParameter("apIndex", apIndex);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    print "Mac Details : ",details
    macAddress= []
    mac_count = 0

    print "\nTEST STEP %d: Get the Acl Devices List" %step;
    print "EXPECTED RESULT %d: Should get the total list of associated devices" %step;

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        mac_count = int(details.split(';')[3].split('=')[1]);

        if mac_count > 0:
            macAddress = details.split(";")[1].strip().split("n")

            for i in range(len(macAddress)):
                macAddress[i] =  macAddress[i].replace("\\", '')

            if '' in macAddress:
                macAddress.remove('')
        print "ACTUAL RESULT %d: wifi_getApAclDevices call is success" %step;
        print "List of Acl Devices MAC Address:",macAddress
        print "TEST EXECUTION RESULT :SUCCESS"
    else:
        print "ACTUAL RESULT %d: wifi_getApAclDevices call failed" %step;
        print "TEST EXECUTION RESULT :FAILURE"
        tdkTestObj.setResultStatus("FAILURE");
    return actualresult, mac_count, macAddress

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;
import random;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzAddandGetApAclDevice');
sysobj.configureTestCase(ip,port,'TS_WIFIHAL_6GHzAddandGetApAclDevice');

loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");

    expectedresult = "SUCCESS";
    #Getting PRIVATE_6G_AP_INDEX value from tdk_platform_properties"
    tdkTestObjTemp, apIndex = getApIndexfor6G(sysobj, TDK_PATH);

    if apIndex == -1:
        print "Failed to get the Access Point index";
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAclDevices');
        step = 2;
        actualresult, mac_count, macAddress = GetApAclDevices(tdkTestObj, apIndex, step)

        if expectedresult in actualresult:
            # Generate MAC address
            mac_partial_1 = "8b:9c:4a:5c:92:"
            x = str(randint(10,99))
            addMAC = mac_partial_1+x;
            print "MAC to be added is ", addMAC;

            #Add the new MAC to ACL list
            tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
            tdkTestObj.addParameter("methodName","addApAclDevice");
            tdkTestObj.addParameter("apIndex",apIndex);
            tdkTestObj.addParameter("DeviceMacAddress",addMAC);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            step = step + 1;
            print "\nTEST STEP %d: Invoke the HAL API wifi_addApAclDevice() to add the MAC address" %step;
            print "EXPECTED RESULT %d: The API should be invoked successfully" %step;

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : The API was invoked successfully" %step;
                print"Successfully added ApAclDevice", addMAC
                print "TEST EXECUTION RESULT :SUCCESS";

                #Invoke wifi_getApAclDevices() to verify addApAcl
                tdkTestObj = obj.createTestStep('WIFIHAL_GetApAclDevices');
                step = step + 1;
                actualresult, mac_count, macAddress = GetApAclDevices(tdkTestObj, apIndex, step)

                if expectedresult in actualresult and mac_count>0:
                    step = step + 1;
                    print "\nTEST STEP %d: Verify if the MAC address is added properly" %step;
                    print "EXPECTED RESULT %d: wifi_addApAclDevice() should be successfully verified using wifi_getApAclDevices()" %step;

                    if addMAC in macAddress:
                        print "ACTUAL RESULT %d : wifi_addApAclDevice() successfully verified using wifi_getApAclDevices()" %step;
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST EXECUTION RESULT :SUCCESS"

                        #Delete the ACL MAC added for testing
                        tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
                        tdkTestObj.addParameter("methodName","delApAclDevice");
                        tdkTestObj.addParameter("apIndex",apIndex);
                        tdkTestObj.addParameter("DeviceMacAddress",addMAC);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails();

                        step = step + 1;
                        print "\nTEST STEP %d : Delete the added Acl Device using the HAL API wifi_delApAclDevice" %step;
                        print "EXPECTED RESULT %d: Should Delete the added Acl Device using the HAL API wifi_delApAclDevice" %step;

                        if expectedresult in actualresult:
                            print "ACTUAL RESULT %d : wifi_delApAclDevice was invoked successfully" %step;
                            print "Deleted device :", addMAC
                            print "TEST EXECUTION RESULT :SUCCESS"
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            print "ACTUAL RESULT %d : wifi_delApAclDevice was not invoked successfully" %step;
                            print "TEST EXECUTION RESULT :FAILURE"
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "ACTUAL RESULT %d : wifi_addApAclDevice() verification using wifi_getApAclDevices() failed. New MAC not found in AclDevice list" %step;
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST EXECUTION RESULT :FAILURE"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "wifi_getApAclDevices() failed after wifi_addApAclDevice()"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"ACTUAL RESULT %d : wifi_addApAclDevice() operation failed" %step;
                print "TEST EXECUTION RESULT : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print"wifi_getApAclDevices() operation failed";

    obj.unloadModule("wifihal");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

