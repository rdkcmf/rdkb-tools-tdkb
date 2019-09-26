##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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
  <version>1</version>
  <name>TS_WIFIHAL_2.4GHzGetRadioStandard</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the current radio standard for 2.4 GHz and to check whether it one of the 	supported standards for 2.4 GHz</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIHAL_21</test_case_id>
    <test_objective>To get the current radio standard for 2.4 GHz and to check whether it one of the supported standards for 2.4 GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_getRadioStandard()</api_or_interface_used>
    <input_parameters>methodName: "getRadioStandard"
radioIndex : 0</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke "WIFIHAL_GetOrSetParamStringValue" to get the current Radio Standard for 2.4GHz
3.Check if the value returned is valid or not
4. If not, return failure
5.Unload wifihal module</automation_approch>
    <except_output>The current radio standard for 2.4GHz should be a sublist of radio supported standards for 2.4GHz.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetRadioStandard</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetRadioStandard');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Script to load the configuration file of the component

    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamStringValue");
    #Giving the method name to invoke the api for getting Supported standards. ie,wifi_getRadioSupportedStandards()
    tdkTestObj.addParameter("methodName","getRadioSupportedStandards");
    #Radio index is 0 for 2.4GHz and 1 for 5GHz
    tdkTestObj.addParameter("radioIndex",0);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    SupportedStandards = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
        SplitList = SupportedStandards.split(":")[1].split(",");
        ActualList = [s.strip() for s in SplitList];
	tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Radio Supported Standards for 2.4GHz";
        print "EXPECTED RESULT 1: Should get the Radio Supported Standards for 2.4GHz";
        print "ACTUAL RESULT 1: %s" %SupportedStandards;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetRadioStandard");
        #Giving the method name to invoke the api wifi_getRadioStandard()
        tdkTestObj.addParameter("methodName","getRadioStandard")
        #Radio index is 0 for 2.4GHz and 1 for 5GHz
        tdkTestObj.addParameter("radioIndex",0);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult :
            CurrStandard = details.split(":")[1].split(" ")[0];
	    gOnly = details.split(":")[1].split(" ")[1].strip();
	    nOnly = details.split(":")[1].split(" ")[2].strip();
	    acOnly = details.split(":")[1].split(" ")[3].strip();
            if CurrStandard in ActualList:
                if int(gOnly) == 0 and int(nOnly) == 1 and int(acOnly) == 0:
                    radioStd = "n"
                elif int(gOnly) == 1 and int(nOnly) == 0 and int(acOnly) == 0:
                    radioStd = "g,n"
                else:
                    radioStd = "b,g,n"
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 2: Get the current Radio standard";
                print "EXPECTED RESULT 2: Should get the Radio standard for 2.4GHz";
                print "ACTUAL RESULT 2: %s" %radioStd;
                print "[TEST EXECUTION RESULT] : SUCCESS";

	    else:
		tdkTestObj.setResultStatus("FAILURE");
		print "FAILURE: Current radio std: not in Supported std list"
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Get the Radio standard";
            print "EXPECTED RESULT 2: Should get the Radio standard for 2.4GHz";
            print "ACTUAL RESULT 2: %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Radio Supported Standards for 2.4GHz";
        print "EXPECTED RESULT 1: Should get the Radio Supported Standards 2.4GHz";
        print "ACTUAL RESULT 1: %s" %SupportedStandards;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
