##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
  <name>TS_WIFIHAL_2.4GHzAddorDelApAclDevice</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_AddorDelApAclDevice</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To add/delete ApAclDevice using the device Mac Address for 2.4GHz.</synopsis>
  <groups_id/>
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIHAL_259</test_case_id>
    <test_objective>To add/delete ApAclDevice using the device Mac Address for 2.4GHz.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
</pre_requisite>
    <api_or_interface_used>wifi_getApAclDeviceNum()
wifi_addApAclDevice()
wifi_delApAclDevice()</api_or_interface_used>
    <input_parameters>methodName : getApAclDeviceNum
methodName : addApAclDevice
methodName : delApAclDevice
apIndex : 0
DeviceMacAddress : 7A:36:76:41:9A:5F</input_parameters>
    <automation_approch>1.Load the module.
2.Get the number of ApAcl devices using the wifi_getApAclDeviceNum() API
3.Add a ApAcl device by passing its mac address to the api wifi_addApAclDevice().
4.Get the number of ApAcl devices using wifi_getApAclDeviceNum() API and check whether it is incremented by 1.
5.Delete the previously added ApAcl device by invoking wifi_delApAclDevice() api.
6.Get the number of ApAcl devices using wifi_getApAclDeviceNum() API and check whether it is decremented by 1.
7.Unload the module.
</automation_approch>
    <except_output>Should be able to add/delete ApAclDevice using the device Mac Address for 2.4GHz.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzAddorDelApAclDevice</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzAddorDelApAclDevice');

#Get the result of connection with test component and STB
loadmodulestatus =obj.getLoadModuleResult();

print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"
    radioIndex = 0
    getMethod = "getApAclDeviceNum"
    primitive = 'WIFIHAL_GetOrSetParamUIntValue'
    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        deviceNum = int(details.split(":")[1].strip());
        print"Number of ApAcl devices initially for 2.4GHz=",deviceNum;
        #Primitive test case which associated to this Script
        tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
        #Giving the method name to invoke the api wifi_addApAclDevice()
        tdkTestObj.addParameter("methodName","addApAclDevice");
        #Ap index is 0 for 2.4GHz and 1 for 5GHz
        tdkTestObj.addParameter("apIndex",0);
        tdkTestObj.addParameter("DeviceMacAddress","7A:36:76:41:9A:5F");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        print"details",details;
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            expectedresult = "SUCCESS"
            radioIndex = 0
            getMethod = "getApAclDeviceNum"
            primitive = 'WIFIHAL_GetOrSetParamUIntValue'
            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
            deviceNum_add = int(details.split(":")[1].strip());
            deviceNum_new = deviceNum_add - deviceNum;
            if expectedresult in actualresult:
                if deviceNum_new == 1:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print"Number of ApAcl devices after adding for 2.4GHz =",deviceNum_add;
                    #Primitive test case which associated to this Script
                    tdkTestObj = obj.createTestStep('WIFIHAL_AddorDelApAclDevice');
                    #Giving the method name to invoke the api wifi_delApAclDevice
                    tdkTestObj.addParameter("methodName","delApAclDevice");
                   #Ap index is 0 for 2.4GHz and 1 for 5GHz
                    tdkTestObj.addParameter("apIndex",0);
                    tdkTestObj.addParameter("DeviceMacAddress","7A:36:76:41:9A:5F");
                    expectedresult="SUCCESS";
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    print"details",details;
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print"ApAclDevice is successfully deleted";
                        expectedresult = "SUCCESS"
                        radioIndex = 0
                        getMethod = "getApAclDeviceNum"
                        primitive = 'WIFIHAL_GetOrSetParamUIntValue'
                        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 0, getMethod)
                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            deviceNum_del = int(details.split(":")[1].strip());
                            print"Number of ApAcl devices after deleting for 2.4GHz =",deviceNum_del;
                            if deviceNum ==deviceNum_del:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print"Number of ApAcl devices after deleting are equal to number of ApAcl devices initially";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print"Number of ApAcl devices after deleting are not equal to number of ApAcl devices initially";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print"wifi_getApAclDeviceNum() operation failed after delete operation";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print"ApAclDevice is not deleted";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Number of ApAclDevices not incremented after add operation";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print"wifi_getApAclDeviceNum() operation failed after add operation";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print"wifi_addApAclDevice() operation failed";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print"wifi_getApAclDeviceNum() operation failed";
    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
