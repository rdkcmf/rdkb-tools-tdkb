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
  <version>19</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WIFIHAL_2.4GHzSetRadioObssCoexistenceEnable</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>WIFIHAL_GetOrSetParamBoolValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>3</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check the functionality of wifi_setRadioObssCoexistenceEnable  WIFIHAL api.</synopsis>
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
    <test_case_id>TS_WIFIHAL_291</test_case_id>
    <test_objective>To validate the functionality of
 wifi_setRadioObssCoexistenceEnable api for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh scrip</pre_requisite>
    <api_or_interface_used>wifi_setRadioObssCoexistenceEnable</api_or_interface_used>
    <input_parameters>radioIndex
enable
</input_parameters>
    <automation_approch>1.Load the module.
2. Get the obss_coex value  from tdk_platformUtiliy.sh.
3. Toggle the obss_coex value using wifi_setRadioObssCoexistenceEnable  api.
4.Get the obss_coex value  from tdk_platformUtiliy.sh and check get and set matches .
5. Unload the module</automation_approch>
    <expected_output>should set the value of obss_coex  using wifi_setRadioObssCoexistenceEnable successfully</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetRadioObssCoexistenceEnable</test_script>
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
from tdkbVariables import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetRadioObssCoexistenceEnable');
sysObj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetRadioObssCoexistenceEnable');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
sysutilloadmodulestatus=sysObj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %sysutilloadmodulestatus

#Query for the RadioObssCoexistenceEnable value
def get_Radio0ObssCoexistenceEnable(tdkTestObj):
    query="sh %s/tdk_platform_utility.sh getRadio0ObssCoexistenceEnable" %TDK_PATH
    print "query:%s" %query
    tdkTestObj.addParameter("command", query);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n","");
    print " ObssCoexistenceEnable is ", details;
    return details,actualresult;

if "SUCCESS" in loadmodulestatus.upper() and sysutilloadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysObj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        tdkTestObj = sysObj.createTestStep('ExecuteCmd');
        expectedresult="SUCCESS";
        defObssCoexistenceEnable,actualresult = get_Radio0ObssCoexistenceEnable(tdkTestObj);
	if expectedresult in actualresult and defObssCoexistenceEnable!="Invalid Argument passed":
            ObssCoexistenceEnable = int(defObssCoexistenceEnable);
       	    tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP 1 :Get RadioObssCoexistenceEnable obss_coex value";
            print "EXPECTED RESULT 1 :RadioObssCoexistenceEnable obss_coex value should be present";
            print "ACTUAL RESULT 1 :RadioObssCoexistenceEnable obss_coex value is " ,ObssCoexistenceEnable;
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] : SUCCESS";
	    if ObssCoexistenceEnable == 1:
	        print "RadioObssCoexistence is Enabled"
		oldEnable = 1
		newEnable = 0
	    else:
	        print "RadioObssCoexistence is Disabled"
		oldEnable = 0
		newEnable = 1
	    expectedresult="SUCCESS";
	    apIndex = idx
	    setMethod = "setRadioObssCoexistenceEnable"
	    primitive = 'WIFIHAL_GetOrSetParamBoolValue'
	    #Toggle the enable status using set
            print "NewEnable :",newEnable;
	    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, newEnable, setMethod)
	    if expectedresult in actualresult :
	        print "Enable state toggled using set"
		# Get the New enable status
		tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                defObssCoexistenceEnable,actualresult = get_Radio0ObssCoexistenceEnable(tdkTestObj);
		if expectedresult in actualresult and defObssCoexistenceEnable!="" and newEnable == int(defObssCoexistenceEnable) :
		    ObssCoexistenceEnable = int(defObssCoexistenceEnable);
		    tdkTestObj.setResultStatus("SUCCESS");
		    print "TEST STEP 2 : Compare the get and set values of ObssCoexistenceEnable"
		    print" EXPECTED RESULT 2 : Get and set values of ObssCoexistenceEnable should be same"
		    print "ACTUAL RESULT 2 : Get and set values of ObssCoexistenceEnable are same"
		    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
		    #Revert back to original Enable status
		    tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, apIndex, oldEnable, setMethod)
		    if expectedresult in actualresult :
		        tdkTestObj.setResultStatus("SUCCESS");
		        print "Enable status reverted back successfully";
			#Get the result of execution
                	print "[TEST EXECUTION RESULT] : SUCCESS";
		    else:
		        tdkTestObj.setResultStatus("FAILURE");
		        print "Couldn't revert enable status"
			#Get the result of execution
                	print "[TEST EXECUTION RESULT] : FAILURE";
		else:
		    tdkTestObj.setResultStatus("FAILURE");
		    print "TEST STEP 2 : Compare the get and set values of ObssCoexistenceEnable"
		    print" EXPECTED RESULT 2 : Get and set values of ObssCoexistenceEnable should be same"
		    print "ACTUAL RESULT 2 : Get and set values of ObssCoexistenceEnable are not same"
		    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
	    else:
	        tdkTestObj.setResultStatus("FAILURE");
		print "setRadioObssCoexistenceEnable operation failed"
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : FAILURE";
        else:
	    tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1 : Get RadioObssCoexistenceEnable obss_coex value";
            print "EXPECTED RESULT 1 : RadioObssCoexistenceEnable obss_coex value should be present";
            print "ACTUAL RESULT 1 :RadioObssCoexistenceEnable obss_coex value not present"
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("wifihal");
    sysObj.unloadModule("sysutil");
else:
    print "Failed to load wifihal/sysutil module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";