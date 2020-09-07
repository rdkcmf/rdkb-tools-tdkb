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
  <version>17</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzGetAssociatedDeviceDetail</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetAssociatedDeviceDetail</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check the functionality of wifi_getAssociatedDeviceDetail  WIFIHAL api.</synopsis>
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
    <test_case_id>TC_WIFIHAL_290</test_case_id>
    <test_objective>To give the details of single associated device of specific device Index for 5GHz wifi.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script.
3.Connect a wifi client.</pre_requisite>
    <api_or_interface_used>wifi_getAssociatedDeviceDetail</api_or_interface_used>
    <input_parameters>methodName = getAssociatedDeviceDetail</input_parameters>
    <automation_approch>1.Load the module.
2. Get the number of devices connected to 5Ghz
3.Get the details of associated devices of  each device Index using wifi_getAssociatedDeviceDetail api
4.Crosscheck the mac address from TR181 para with mac addresss from api result
5.Unload the module</automation_approch>
    <expected_output>Should get the details of single associated device of specific device Index for 5GHz</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetAssociatedDeviceDetail</test_script>
    <skipped>No</skipped>
    <release_version>M80</release_version>
    <remarks>Nil</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");

radio = "5G"

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetAssociatedDeviceDetail');
wifiobj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetAssociatedDeviceDetail');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
sysloadmodulestatus = wifiobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus
if "SUCCESS" in loadmodulestatus.upper() and sysloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    wifiobj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #check the number of associated devices to 5G
        tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
        tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.AssociatedDeviceNumberOfEntries");
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            devCount = int(details.split("VALUE:")[1].split(' ')[0]);
            print "TEST STEP 1 : Get the number of the connected client ";
            print "ACTUAL RESULT 1: Should get the number of connected client ";
            print "EXPECTED RESULT 1 :",devCount;
            print "[TEST EXECUTION RESULT] : SUCCESS";
	    if  devCount :
	        for devIndex in range(1,devCount+1):
	     	    #Prmitive test case which associated to this Script
                    tdkTestObj = obj.createTestStep('WIFIHAL_GetAssociatedDeviceDetail');
               	    tdkTestObj.addParameter("apIndex", idx);
               	    tdkTestObj.addParameter("devIndex", devIndex);
               	    expectedresult="SUCCESS";
               	    tdkTestObj.executeTestCase(expectedresult);
               	    actualresult = tdkTestObj.getResult();
               	    details = tdkTestObj.getResultDetails().strip().replace("\\n","");
		    mac = details.split(": ")[1].split(" ")[0].strip()
               	    if expectedresult in actualresult :
		        tdkTestObj.setResultStatus("SUCCESS");
                	print "TEST STEP 2 : Get the AssociatedDevice Detail using getAssociatedDeviceDetail() api"
               		print "EXPECTED RESULT 2 : Should successfully get the  AssociatedDevice Details"
               		print "ACTUAL RESULT 2: Successfully gets the AssociatedDevice Details of Device Index ",devIndex;
               		print "Details: ",details;
			#Get the result of execution
               		print "[TEST EXECUTION RESULT] : SUCCESS";
			#check the MAC address of associated devices to 5G
        		tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
        		tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.AssociatedDevice.%d.MACAddress" %devIndex);
        		expectedresult="SUCCESS";
       			tdkTestObj.executeTestCase(expectedresult);
       			actualresult = tdkTestObj.getResult();
       			details = tdkTestObj.getResultDetails();
       			if expectedresult in actualresult :
        		    tdkTestObj.setResultStatus("SUCCESS");
            		    macAddress = details.split("VALUE:")[1].split(' ')[0];
	  		    print "Device.WiFi.AccessPoint.2.AssociatedDevice.%d.MACAddress :" %devIndex,macAddress;
			    print "Mac address from api : ",mac;
			    if mac == macAddress.lower() :
			        tdkTestObj.setResultStatus("SUCCESS");
				print "TEST STEP 3 :  check the MAC from wifi_getAssociatedDeviceDetail api result with Device.WiFi.AccessPoint.2.AssociatedDevice.%d.MACAddress"%devIndex
				print "EXPECTED RESULT 3 : Should successfully matches the MAC from wifi_getAssociatedDeviceDetail api result with Device.WiFi.AccessPoint.2.AssociatedDevice.%d.MACAddress " %devIndex
			        print "ACTUAL RESULT 3 : Successfully matches MAC from wifi_getAssociatedDeviceDetail api result with Device.WiFi.AccessPoint.2.AssociatedDevice.%d.MACAddress" %devIndex;
		                #Get the result of execution
                		print "[TEST EXECUTION RESULT] : SUCCESS";
			    else :
			        tdkTestObj.setResultStatus("FAILURE");
				print "TEST STEP 3 :  check the MAC from wifi_getAssociatedDeviceDetail api result with Device.WiFi.AccessPoint.2.AssociatedDevice.%d.MACAddress" %devIndex
			        print "EXPECTED RESULT 3 : Should successfully matches the MAC from wifi_getAssociatedDeviceDetail api result with Device.WiFi.AccessPoint.2.AssociatedDevice.%d.MACAddress " %devIndex
			        print "ACTUAL RESULT 3 : Failed to match MAC from wifi_getAssociatedDeviceDetail api result with Device.WiFi.AccessPoint.2.AssociatedDevice.%d.MACAddress" %devIndex;
				#Get the result of execution
                		print "[TEST EXECUTION RESULT] : FAILURE";
		    	else:
		            tdkTestObj.setResultStatus("FAILURE");
             		    print "Not able to  retrieve Device.WiFi.AccessPoint.2.AssociatedDevice.%d.MACAddress" %devIndex
                            #Get the result of execution
                	    print "[TEST EXECUTION RESULT] : FAILURE";
		    else:
                        tdkTestObj.setResultStatus("FAILURE");
                	print "TEST STEP 2: Get the AssociatedDevice Detail using getAssociatedDeviceDetail() api"
               		print "EXPECTED RESULT 2 : Should successfully get the  AssociatedDevice Details"
               		print "ACTUAL RESULT 2: Failed to get the  AssociatedDevice Details of Device Index ",devIndex;
               		print "Details: %s"%details
               		#Get the result of execution
               		print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
	        tdkTestObj.setResultStatus("FAILURE");
                print "Not able to  get the number of connected client  as no device is connected or AssociatedDeviceNumberOfEntries received from TR181 param is zero "
	        #Get the result of execution
               	print "[TEST EXECUTION RESULT] : FAILURE";
	else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1 : Get number of associated devices using TR181 param"
            print "EXPECTED RESULT 1: should get number of associated devices"
            print "ACTUAL RESULT 1: Failed to get the number of associated devices"
	    #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
    wifiobj.unloadModule("wifiagent");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";