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
  <name>TS_WEBPA_EPON_DPoE_ClearOnuLinkStatistics</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WEBPA_Donothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Using webpa check if Device.DPoE.ClearOnuLinkStatistics clears the existing Device.DPoE.DPoE_OnuLinkStatistics. entries</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>25</execution_time>
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
    <test_case_id>TC_WEBPA_18</test_case_id>
    <test_objective>Using webpa check if Device.DPoE.ClearOnuLinkStatistics clears the existing Device.DPoE.DPoE_OnuLinkStatistics. entries</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>If SAT token is to be used, token should be created and made available in test manager. Also the config variables SAT_REQUIRED, SAT_TOKEN_FILE, SERVER_URI should be updated in webpaVariables.py</pre_requisite>
    <api_or_interface_used>webpaQuery
parseWebpaResponse</api_or_interface_used>
    <input_parameters>Device.DPoE.ClearOnuLinkStatistics
Device.DPoE.DPoE_OnuLinkStatistics.%s.rxUnicastFrames</input_parameters>
    <automation_approch>1. Load sysutil module
2. Configure WEBPA server to send get request for Device.DPoE.DPoE_OnuLinkStatisticsNumberOfEntries
3. Parse the WEBPA response
4. If webpa response status is SUCCESS, get operation was success otherwise failure
5. Using webpa query get all the current Device.DPoE.DPoE_OnuLinkStatistics.%s.rxUnicastFrames
6. Configure WEBPA server to send set request for Device.DPoE.ClearOnuLinkStatistics
7. If set is success, get all the current Device.DPoE.DPoE_OnuLinkStatistics.%s.rxUnicastFrames
8. Values of Device.DPoE.DPoE_OnuLinkStatistics.%s.rxUnicastFrames after reset should be less than the values before reset
9. Unload sysutil module</automation_approch>
    <except_output>Device.DPoE.ClearOnuLinkStatistics should clear the existing Device.DPoE.DPoE_OnuLinkStatistics.%s.rxUnicastFrames entries</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_WEBPA_EPON_DPoE_ClearOnuLinkStatistics</test_script>
    <skipped>No</skipped>
    <release_version>M59</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from webpaUtility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WEBPA_EPON_DPoE_ClearOnuLinkStatistics');

#Get the result of connection with test component and STB
result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");

    tdkTestObj,preRequisiteStatus = webpaPreRequisite(obj);
    if "SUCCESS" in preRequisiteStatus:

        queryParam = {"name":"Device.DPoE.DPoE_OnuLinkStatisticsNumberOfEntries"}
        queryResponse = webpaQuery(obj, queryParam)

        parsedResponse = parseWebpaResponse(queryResponse, 1)
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.executeTestCase("SUCCESS");
        if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
            tdkTestObj.setResultStatus("SUCCESS");
            print "[TEST EXECUTION RESULT] : SUCCESS"

	    entryCount = parsedResponse[1]
	    entryCount = int(entryCount)

	    print "OnuLinkStatisticsNumberOfEntries: ",entryCount

	    if entryCount > 6:
                flag = "true"
                rxUnicastFrameOrg = " "
                for i in range(1, 6):
                    queryParam = {"name":"Device.DPoE.DPoE_OnuLinkStatistics.%s.rxUnicastFrames" %i}
                    queryResponse = webpaQuery(obj, queryParam)
                    parsedResponse = parseWebpaResponse(queryResponse, 1)
                    if "SUCCESS" not in parsedResponse[0]:
                        flag = "false"
                        break;
                    else:
                        rxUnicastFrameOrg = rxUnicastFrameOrg + parsedResponse[1] + " "

                if flag == "true" :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                    print "Got all the rxUnicastFrames entries"
		    rxUnicastFrameOrg = rxUnicastFrameOrg.lstrip(" ").rstrip(" ").split(" ");
                    print "rxUnicastFrames: ",rxUnicastFrameOrg

      	            #clear the OnuLinkStatistics
	            print "TEST STEP 2: Clear the OnuLinkStatistics"
	            queryParam = {"name":"Device.DPoE.ClearOnuLinkStatistics","value":"true","dataType":3}
	            queryResponse = webpaQuery(obj, queryParam, "set")
	            parsedResponse = parseWebpaResponse(queryResponse, 1, "set")
	            tdkTestObj.executeTestCase("SUCCESS");
                    if "SUCCESS" in parsedResponse[0] and parsedResponse[1] != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 2[TEST EXECUTION RESULT] : SUCCESS"
	                print "Reset success"

	                flag = "true"
                        rxUnicastFrame = " "
	                for i in range(1, 6):
	                    queryParam = {"name":"Device.DPoE.DPoE_OnuLinkStatistics.%s.rxUnicastFrames" %i}
	                    queryResponse = webpaQuery(obj, queryParam)
	                    parsedResponse = parseWebpaResponse(queryResponse, 1)
	                    if "SUCCESS" not in parsedResponse[0]:
	            	        flag = "false"
    	            	        break;
	                    else:
	            	        rxUnicastFrame = rxUnicastFrame + parsedResponse[1] + " "
	                if flag == "true" :
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "[TEST EXECUTION RESULT] : SUCCESS"
                            print "Got all the rxUnicastFrames entries after reset"
			    rxUnicastFrame = rxUnicastFrame.lstrip(" ").rstrip(" ").split(" ");
                            print "rxUnicastFrames after reset: ",rxUnicastFrame

			    resetOk = "true"
			    for i in range(5):
			        if int(rxUnicastFrame[i]) > int(rxUnicastFrameOrg[i]) :
				    resetOk = "false"
				    break;
			    if flag == "true" :
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "[TEST EXECUTION RESULT] : SUCCESS"
                                print "OnuLinkStatistics successfully cleared"
                            if flag == "false" :
                                tdkTestObj.setResultStatus("FAILURE");
                                print "[TEST EXECUTION RESULT] : FAILURE"
                                print "Failed to clear OnuLinkStatistics"

	                else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "[TEST EXECUTION RESULT] : FAILURE"
                            print "Failed to get all the rxUnicastFrames entries after reset"
	            else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 2[TEST EXECUTION RESULT] : FAILURE"
                        print "Reset failed"
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "[TEST EXECUTION RESULT] : FAILURE"
                    print "Failed to get all the rxUnicastFrames entries"
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "Webpa Pre-requisite failed. Please check parodus and webpa processes are running in device"

    obj.unloadModule("sysutil");

else:
    print "FAILURE to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";
