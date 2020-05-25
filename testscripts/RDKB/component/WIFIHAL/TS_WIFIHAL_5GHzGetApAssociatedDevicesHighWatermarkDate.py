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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_5GHzGetApAssociatedDevicesHighWatermarkDate</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamULongValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get the Date and Time at which the maximum number of associated devices that has ever associated with the access point concurrently since the last reset of the device or WiFi module for 5GHz</synopsis>
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
    <test_case_id>TC_WIFIHAL_229</test_case_id>
    <test_objective>To get the Date and Time at which the maximum number of associated devices that has ever associated with the access point concurrently since the last reset of the device or WiFi module for 5GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, Rpi</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDevicesHighWatermarkDate()</api_or_interface_used>
    <input_parameters>methodName   :   getApAssociatedDevicesHighWatermarkDate
apIndex      :   1</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke "WIFIHAL_GetOrSetParamULongValue" to call wifi_getApAssociatedDevicesHighWatermarkDate for 5GHz
3.Return failure or success depending upon the return value of the api
4.Unload wifihal module</automation_approch>
    <except_output>Should return AssociatedDevicesHighWatermarkDate as a non zero value</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzGetApAssociatedDevicesHighWatermarkDate</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
import re;
from datetime import datetime
import time;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzGetApAssociatedDevicesHighWatermarkDate');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():

    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else: 

	    apIndex = idx
	    obj.setLoadModuleStatus("SUCCESS");
	    #Prmitive test case which is associated to this Script
	    tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDeviceDiagnosticResult');
	    tdkTestObj.addParameter("radioIndex", idx);
	    expectedresult="SUCCESS";
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();


	    if expectedresult in actualresult :
		tdkTestObj.setResultStatus("SUCCESS");
		print "wifi_getApAssociatedDeviceDiagnosticResult() call to get STA details is SUCCESS";
		details = details.split(":")[1].strip();
		output_array_size = details.split("=")[1].strip();
		noOfClients = int(output_array_size);
		if noOfClients  > 0 :
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "**********STA Associated with DUT**********";
		    print "TEST EXECUTION RESULT :SUCCESS"
		    print "no of Clients:",noOfClients

		    #getting maxAssociatedDevice
		    getMethodToCheck = "getApMaxAssociatedDevices"
		    primitive = 'WIFIHAL_GetOrSetParamUIntValue'
		    #Calling the method from wifiUtility to execute test case and set result status for the test.
		    tdkTestObj, actualresult, maxDevice = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethodToCheck)
		    maxDevice =  int(maxDevice.split(":")[1])
		    print "maxDevice: ",maxDevice
		    if expectedresult in actualresult :
		       if noOfClients < maxDevice:

			  # getting the initial value of getApAssociatedDevicesHighWatermarkThreshold
			  expectedresult="SUCCESS";
			  getMethod = "getApAssociatedDevicesHighWatermarkThreshold"
			  primitive = 'WIFIHAL_GetOrSetParamUIntValue'

			  #Calling the method from wifiUtility to execute test case and set result status for the test.
			  tdkTestObj, actualresult, initial  = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)

			  if expectedresult in actualresult:
			     setThreshold = noOfClients+1
			     expectedresult="SUCCESS"
			     setMethod = "setApAssociatedDevicesHighWatermarkThreshold"
			     primitive = 'WIFIHAL_GetOrSetParamUIntValue'
			     #Calling the method from wifiUtility to execute test case and set result status for the test.
			     tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setThreshold, setMethod)
			     if expectedresult in actualresult:
				#now get the HighWatermarkDate
				expectedresult="SUCCESS";
				getMethod = "getApAssociatedDevicesHighWatermarkDate"
				primitive = 'WIFIHAL_GetOrSetParamULongValue'
				#Calling the method to execute wifi_getApAssociatedDevicesHighWatermarkDate()
				tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, 0, getMethod)
				date_in_seconds  = float(details.split(":")[1])

				if expectedresult in actualresult and date_in_seconds != 0:
				   #converting seconds to utc format
				   date_in_utc  =  datetime.fromtimestamp(date_in_seconds).strftime("%A, %B %d, %Y %I:%M:%S")
				   print "The seconds converted to utc format :",date_in_utc

				   print "TEST STEP: Get the AssociatedDevicesHighWatermarkDate"
				   print "EXPECTED RESULT: Should get the date in seconds"
				   print "ACTUAL RESULT : Received the date in seconds"
				   print "AssociatedDevicesHighWatermarkDate :",date_in_seconds
				   print "TEST EXECUTION RESULT :SUCCESS"
				   tdkTestObj.setResultStatus("SUCCESS");
				else:
				    print "TEST STEP: Get the AssociatedDevicesHighWatermarkDate"
				    print "EXPECTED RESULT: Should get the date in seconds"
				    print "AssociatedDevicesHighWatermarkDate :",date_in_seconds
				    print "TEST EXECUTION RESULT :FAILURE"
				    tdkTestObj.setResultStatus("FAILURE");

				#Revert back to the initial
				expectedresult="SUCCESS"
				setMethod = "setApAssociatedDevicesHighWatermarkThreshold"
				primitive = 'WIFIHAL_GetOrSetParamUIntValue'
				initial = int(initial.split(":")[1])
				#Calling the method from wifiUtility to execute test case and set result status for the test.
				tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, setThreshold, setMethod)

				if expectedresult in actualresult :
				   tdkTestObj.setResultStatus("SUCCESS");
				   print "TEST STEP: Revert  back the HighWatermarkThreshold to initial"
				   print "EXPECTED RESULT:Should revert the value successfully"
				   print "ACTUAL RESULT : Reverted the value successfully"
				   print "TEST EXECUTION RESULT :SUCCESS"
				else:
				    tdkTestObj.setResultStatus("FAILURE");
				    print "TEST STEP: Revert  back the HighWatermarkThreshold to initial"
				    print "EXPECTED RESULT:Should revert the value successfully"
				    print "ACTUAL RESULT : Could not revert the value"
				    print "TEST EXECUTION RESULT :FAILURE"
			     else:
				 tdkTestObj.setResultStatus("FAILURE");
				 print"wifi_setApAssociatedDevicesHighWatermarkThreshold() failed"
			  else:
			      tdkTestObj.setResultStatus("FAILURE");
			      print "wifi_getApAssociatedDevicesHighWatermarkThreshold() call failed"

		       else:
			   tdkTestObj.setResultStatus("FAILURE");
			   print "wifi_getApAssociatedDevicesHighWatermarkDate() call failed"
		    else:
			tdkTestObj.setResultStatus("FAILURE");
			print "wifi_getApMaxAssociatedDevices() call failed"


		else:
		    tdkTestObj.setResultStatus("FAILURE");
		    print "**********STA NOT Associated with DUT**********";
		    print "TEST EXECUTION RESULT :FAILURE"
    obj.unloadModule("wifihal");

else:
     print "Failed to load wifi module";
     obj.setLoadModuleStatus("FAILURE");


