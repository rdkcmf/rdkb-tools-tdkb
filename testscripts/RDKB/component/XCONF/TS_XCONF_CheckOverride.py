##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
  <version>2</version>
  <name>TS_XCONF_CheckOverride</name>
  <primitive_test_id/>
  <primitive_test_name>XCONF_DoNothing</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Test if the xconf server url from override file is used instead of default url by xconf client</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_XCONF_1</test_case_id>
    <test_objective>Test if the xconf server url from override file is used instead of default url by xconf client</test_objective>
    <test_type>Positive</test_type>
    <test_setup>XB3</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>GetPlatformProperties
ExecuteCmd</api_or_interface_used>
    <input_parameters>XCONF_OVERRIDE_FILE
CDN_LOG
CDN_FILE
mv " + xconfFile + " " + xconfFile + "_bck ; echo " + XCONF_OVERRIDE_URL + " &gt; " + xconfFile
"rm " + cdnLog
"sh " + cdnFile + " 0 1 &amp;"
grep -inr \"CURL_CMD\" " + cdnLog + " | grep " + XCONF_OVERRIDE_URL + " ;echo $?
mv " + xconfFile + "_bck " + xconfFile</input_parameters>
    <automation_approch>1. Load sysutil module
2. Get override file name from device
3. Add the override url to this file
4. Get CDN_LOG and CDN_FILE values from the device
5. Remove previous logs, CDN_LOG
6. Execute CDN_FILE
7. In the new log, check for the override url in the client request
8. Restore override file
9. Unload sysutil module</automation_approch>
    <except_output>Xconf client should use override url instead of default url</except_output>
    <priority>High</priority>
    <test_stub_interface>sysutil</test_stub_interface>
    <test_script>TS_XCONF_CheckOverride</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
import xconfUtilityLib;
from xconfUtilityLib import *
from xconfVariables import *
import time

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_XCONF_CheckOverride');

result =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %result;

if "SUCCESS" in result.upper() :
    #Set the module loading status
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS"

    ####Override server url to be used as the mock server url
    actualresult, xconfFile = xconfUtilityLib.overrideServerUrl(obj, XCONF_OVERRIDE_URL)

    if expectedresult in actualresult:
        ################get log file name from tdk_platform.properties
        actualresult, propVal = xconfUtilityLib.GetPlatformProperties(obj, "CDN_LOG");
        if expectedresult in actualresult:
            cdnLog = propVal
            print "SUCCESS:get log file name"
        else:
            print "FAILURE:failed to get log file name"

        ################get CDN file name from tdk_platform.properties
        actualresult, propVal = xconfUtilityLib.GetPlatformProperties(obj, "CDN_FILE");
        if expectedresult in actualresult:
            print "SUCCESS:get cdn file name"
            cdnFile = propVal
        else:
            print "FAILURE:failed to get log file name"

        #Remove the exsisting logs
        result = xconfUtilityLib.removeLog(obj, cdnLog);
        if "SUCCESS" in result:
            ###########excute the shell script to download firmware
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            tdkTestObj.addParameter("command", "sh " + cdnFile + " 0 1  > /dev/null 2>&1 &");
            tdkTestObj.executeTestCase("SUCCESS");

            result = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            #wait till log updation
            time.sleep(20)
            if "SUCCESS" in result:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 5: Initiate firmware download"
                print "EXPECTED RESULT 5: firmware download should be initiated"
                print "ACTUAL RESULT 5: is %s " %details
                print "[TEST EXECUTION RESULT] : SUCCESS"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 5: Initiate firmware download"
                print "EXPECTED RESULT 5: firmware download should be initiated"
                print "ACTUAL RESULT 5: is %s " %details
                print "[TEST EXECUTION RESULT] : FAILURE"

	    ######search in Log whether override url is used insted of default url
	    tdkTestObj = obj.createTestStep('ExecuteCmd');
	    tdkTestObj.addParameter("command","grep -inr \"CURL_CMD\" " + cdnLog + " | grep " + XCONF_OVERRIDE_URL + " ;echo $?")
	    tdkTestObj.executeTestCase("SUCCESS");
	    result = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();
    	    if "0" in details.lower():
	        print "TEST STEP 6: Search for pattern in logs"
        	print "EXPECTED RESULT 6: Should find the pattern in the logs"
	        print "ACTUAL RESULT 6: is %s " %details
        	print "[TEST EXECUTION RESULT] : SUCCESS"
	        tdkTestObj.setResultStatus("SUCCESS");
	    else:
        	tdkTestObj.setResultStatus("FAILURE");
	        print "TEST STEP 6: Search for pattern in logs"
        	print "EXPECTED RESULT 6: Should find the pattern in the logs"
	        print "ACTUAL RESULT 6: is %s " %details
        	print "[TEST EXECUTION RESULT] : FAILURE"
		tdkTestObj.setResultStatus("FAILURE");

    #######restore the override file
    xconfUtilityLib.restoreOverrideFile(obj, xconfFile);

    obj.unloadModule("sysutil");
else:
    print"Load module failed";
    #Set the module loading status
    obj.setLoadModuleStatus("FAILURE");
