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
  <version>21</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzSetRadioDCSScanTime</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetRadioDCSScanTime</primitive_test_name>
  <!--  -->
  <primitive_test_version>2</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To set and get the radio DCS Scan Time for 2.4GHz.</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>5</execution_time>
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
    <test_case_id>TC_WIFIHAL_231</test_case_id>
    <test_objective>To set and get the DCS Scan Time for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioDCSScanTime()
wifi_setRadioDCSScanTime()</api_or_interface_used>
    <input_parameters>methodName : getRadioDCSScanTime
methodName : setRadioDCSScanTime
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Using  WIFIHAL_GetOrSetRadioDCSScanTime invoke wifi_getRadioDCSScanTime()
3. Using WIFIHAL_GetOrSetRadioDCSScanTime
 invoke wifi_setRadioDCSScanTime() and set a valid scan time.
4. Invoke wifi_getRadioDCSScanTime() to get the previously set value.
5. Compare the above two results. If the two values  are same return SUCCESS else return FAILURE
6. Revert the RadioDCSScanTime back to initial value
7. Unload wifihal module</automation_approch>
    <except_output>Set and get values of RadioDCSScanTime should be the same</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetRadioDCSScanTime</test_script>
    <skipped>No</skipped>
    <release_version></release_version>
    <remarks></remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import random;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetRadioDCSScanTime');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Primitive test case which associated to this Script
    tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetRadioDCSScanTime');
    #Giving the method name to invoke the api wifi_getRadioDCSScanTime()
    tdkTestObj.addParameter("methodName","getRadioDCSScanTime");
    #Radio index is 0 for 2.4GHz and 1 for 5GHz
    tdkTestObj.addParameter("radioIndex",0);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
	tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the DCS Scan Time for 2.4GHz";
        print "EXPECTED RESULT 1: Should get the DCS Scan Time for 2.4GHz";
        print "ACTUAL RESULT 1: %s" %details;
        output_interval_seconds = int(details.split(",")[0].split("=")[1]);
        output_dwell_milliseconds = int(details.split(",")[1].split("=")[1]);
        print "output_interval_seconds",output_interval_seconds;
        print "output_dwell_milliseconds",output_dwell_milliseconds;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Primitive test case which associated to this Script
        tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetRadioDCSScanTime');
        #Giving the method name to invoke the api wifi_setRadioDCSScanTime()
        tdkTestObj.addParameter("methodName","setRadioDCSScanTime");
        output_interval_seconds_set = random.randint(1,900);
        output_dwell_milliseconds_set = random.randint(0,500);
        print "output_interval_seconds_set",output_interval_seconds_set;
        print "output_dwell_milliseconds_set",output_dwell_milliseconds_set;
        #Radio index is 0 for 2.4GHz and 1 for 5GHz
        tdkTestObj.addParameter("radioIndex",0);
        tdkTestObj.addParameter("output_interval_seconds",output_interval_seconds_set);
        tdkTestObj.addParameter("output_dwell_milliseconds",output_dwell_milliseconds_set);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Set the DCS Scan Time for 2.4GHz";
            print "EXPECTED RESULT 2: Should set the DCS Scan Time for 2.4GHz";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    #Primitive test case which associated to this Script
	    tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetRadioDCSScanTime');
    	    #Giving the method name to invoke the api wifi_getRadioDCSScanTime()
	    tdkTestObj.addParameter("methodName","getRadioDCSScanTime");
	    #Radio index is 0 for 2.4GHz and 1 for 5GHz
	    tdkTestObj.addParameter("radioIndex",0);
	    expectedresult="SUCCESS";
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();
	    if expectedresult in actualresult:
                output_interval_seconds_get = int(details.split(",")[0].split("=")[1]);
                output_dwell_milliseconds_get = int(details.split(",")[1].split("=")[1]);
                print "output_interval_seconds_get",output_interval_seconds_get;
                print "output_dwell_milliseconds_get",output_dwell_milliseconds_get;
                if output_interval_seconds_set == output_interval_seconds_get and output_dwell_milliseconds_set == output_dwell_milliseconds_get:
        	    tdkTestObj.setResultStatus("SUCCESS");
	            print "TEST STEP 3: Get the previously set DCS Scan Time for 2.4GHz";
	            print "EXPECTED RESULT 3: Should get the previously set DCS Scan Time for 2.4GHz";
	            print "ACTUAL RESULT 3: Get and Set values are equal";
                    print "details",details;
	            #Get the result of execution
	            print "[TEST EXECUTION RESULT] : SUCCESS";
	        else:
        	    tdkTestObj.setResultStatus("FAILURE");
	            print "TEST STEP 3: Get the previously set DCS Scan Time for 2.4GHz";
	            print "EXPECTED RESULT 3: Should get the previously set DCS Scan Time for 2.4GHz";
	            print "ACTUAL RESULT 3: Get and Set values are not equal" ;
                    print "details",details;
	            #Get the result of execution
	            print "[TEST EXECUTION RESULT] : FAILURE";

            #Reverting back to initial value
            tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetRadioDCSScanTime');
    	    #Giving the method name to invoke the api wifi_setRadioDCSScanTime()
            tdkTestObj.addParameter("methodName","setRadioDCSScanTime");
            #Radio index is 0 for 2.4GHz and 1 for 5GHz
            tdkTestObj.addParameter("radioIndex",0);
            tdkTestObj.addParameter("output_interval_seconds",output_interval_seconds);
            tdkTestObj.addParameter("output_dwell_milliseconds",output_dwell_milliseconds);
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult:
		tdkTestObj.setResultStatus("SUCCESS");
		print "Successfully reverted to initial values"
                print "output_interval_seconds",output_interval_seconds;
                print "output_dwell_milliseconds",output_dwell_milliseconds;
	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "Unable to revert to initial value"
	else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Set the DCS Scan Time for 2.4GHz";
            print "EXPECTED RESULT 2: Should set the DCS Scan Time for 2.4GHz";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
	tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the DCS Scan Time for 2.4GHz";
        print "EXPECTED RESULT 1: Should get the DCS Scan Time for 2.4GHz";
        print "ACTUAL RESULT 1: %s" %details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
