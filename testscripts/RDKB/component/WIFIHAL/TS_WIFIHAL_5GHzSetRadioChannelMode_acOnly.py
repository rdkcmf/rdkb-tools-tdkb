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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>1</version>
  <name>TS_WIFIHAL_5GHzSetRadioChannelMode_acOnly</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetRadioStandard</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set the applicable radio modes which supports acOnly for 5GHZ using wifi_setRadioChannelMode() and validate using wifi_getRadioStandard</synopsis>
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
    <test_case_id>TC_WIFIHAL_403</test_case_id>
    <test_objective>Set the applicable radio modes which supports acOnly for 5GHZ using wifi_setRadioChannelMode() and validate using wifi_getRadioStandard</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioChannelMode() wifi_getRadioStandard</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the wifihal  and sysutil module
2.Get the list of 5G Radio modes which supports acOnly puremode from tdk_platfrom properties file
3. Loop through the supported Radio modes list and set the radio modes using wifi_setRadioChannelMode()
4. For each mode set using wifi_setRadioMode(), do a get using wifi_getRadioStandard and check the radio standard and pure mode flags
5.Unload the wifihal and sysutil modules.</automation_approch>
    <expected_output>Set operation using wifi_setRadioChannelMode()  should be success</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzSetRadioChannelMode_acOnly</test_script>
    <skipped>No</skipped>
    <release_version>M81</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from tdkbVariables import *;

radio = "5G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1")

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetRadioChannelMode_acOnly');
obj1.configureTestCase(ip,port,'TS_WIFIHAL_5GHzSetRadioChannelMode_acOnly');

def getRadioChannelMode(tdkTestObj, index, methodName):
    tdkTestObj.addParameter("radioIndex", index);
    tdkTestObj.addParameter("methodName", methodName)
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult,details

def setRadioChannelMode(tdkTestObj, index, methodName, chnmode, gOnly, nOnly, acOnly):
    tdkTestObj.addParameter("radioIndex", index);
    tdkTestObj.addParameter("methodName", methodName)
    tdkTestObj.addParameter("param", chnmode);
    tdkTestObj.addParameter("gOnly", gOnly);
    tdkTestObj.addParameter("nOnly", nOnly);
    tdkTestObj.addParameter("acOnly", acOnly);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult,details

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysutilmodulestatus =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[SYSUTIL  LOAD STATUS]  :  %s" %sysutilmodulestatus

if "SUCCESS" in (loadmodulestatus.upper() and  sysutilmodulestatus.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        expectedresult="SUCCESS";
	radioIndex = idx

        #Get the initial Mode
        expectedresult="SUCCESS";
        #Get the default value from properties file
        tdkTestObj1 = obj1.createTestStep('ExecuteCmd');
        cmd = "sh %s/tdk_utility.sh parseConfigFile CHANNEL_MODES_5_AC_ONLY" %TDK_PATH;
        print cmd;
        expectedresult="SUCCESS";
        tdkTestObj1.addParameter("command", cmd);
        tdkTestObj1.executeTestCase(expectedresult);
        actualresult = tdkTestObj1.getResult();
        details = ""
        details = tdkTestObj1.getResultDetails().strip();
        if details != "" and ( expectedresult in  actualresult):
            modeList = details.replace("\\n", "").split(',');
            print "Radio modes:",modeList
            tdkTestObj1.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the value of CHANNEL_MODES_5_AC_ONLY from tdk_platform properties file";
            print "EXPECTED RESULT 1: Should Get the value of CHANNEL_MODES_5_AC_ONLY from platform properties file";
            print "ACTUAL RESULT 1: CHANNEL_MODES_5_AC_ONLY values from tdk_platform properties file is : ", modeList;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            set_gOnly = 0
            set_nOnly = 0
            set_acOnly = 1
            for mode in modeList:
                std = mode.split(':')[0]
                stdStr = mode.split(':')[1]

                tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetRadioStandard');
                actualresult,details = setRadioChannelMode(tdkTestObj, radioIndex, "setRadioChannelMode", stdStr, set_gOnly, set_nOnly, set_acOnly);
                if expectedresult in actualresult :
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Set the Radio Channel Mode"
                    print "EXPECTED RESULT 2: Should successfully Set the Radio Channel Mode as : %s,  gOnly = %d, nOnly = %d, acOnly = %d" %(stdStr, set_gOnly , set_nOnly, set_acOnly)
                    print "ACTUAL RESULT 2: Successfully Sets the Radio Mode"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Prmitive test case which is associated to this Script
                    tdkTestObj = obj.createTestStep('WIFIHAL_GetOrSetRadioStandard');
                    actualresult,details = getRadioChannelMode(tdkTestObj, radioIndex,"getRadioStandard");
                    print "Details: %s"%details
                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3: Get the Radio Mode using wifi_getRadioStandard"
                        print "EXPECTED RESULT 3: Should successfully get the Radio Mode using wifi_getRadioStandard"
                        print "ACTUAL RESULT : Successfully gets the Radio Mode. %s"%details
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

	                getStd = details.split(":")[1].split(" ")[0];
	                gOnly = int(details.split(":")[1].split(" ")[1].strip())
	                nOnly = int(details.split(":")[1].split(" ")[2].strip());
	                acOnly = int(details.split(":")[1].split(" ")[3].strip());
                        if getStd == std and gOnly == set_gOnly and nOnly == set_nOnly and acOnly == set_acOnly:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 4: Get the Radio Mode and check if set was success"
                            print "EXPECTED RESULT 4: Should successfully get the Std as:  %s,  gOnly = %d, nOnly = %d, acOnly = %d" %(std, set_gOnly , set_nOnly, set_acOnly)
                            print "ACTUAL RESULT : Successfully verified set using get operation";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 4: Get the Radio Mode and check if set was success"
                            print "EXPECTED RESULT 4: Should successfully get the Std as:  %s,  gOnly = %d, nOnly = %d, acOnly = %d" %(std, set_gOnly , set_nOnly, set_acOnly)
                            print "ACTUAL RESULT : Failed to verify  set using get operation";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Get the Radio Mode using wifi_getRadioStandard"
                        print "EXPECTED RESULT 3: Should successfully get the Radio Mode using wifi_getRadioStandard"
                        print "ACTUAL RESULT : Failed to get the Radio Mode. %s"%details
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 3: Set the Radio Channel Mode"
                    print "EXPECTED RESULT 3: Should successfully Set the Radio Channel Mode as : %s,  gOnly = %d, nOnly = %d, acOnly = %d" %(stdStr, set_gOnly , set_nOnly, set_acOnly)
                    print "ACTUAL RESULT 3: Failed to set the Radio Mode %s"
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj1.setResultStatus("SUCCESS");
            print "TEST STEP 2: Get the value of CHANNEL_MODES_5_AC_ONLY from tdk_platform properties file";
            print "EXPECTED RESULT 2: Should Get the value of CHANNEL_MODES_5_AC_ONLY from platform properties file";
            print "ACTUAL RESULT 2:Failed to get CHANNEL_MODES_5_AC_ONLY values from tdk_platform properties file";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE"
    obj.unloadModule("wifihal");
    obj.unloadModule("sysutil");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
