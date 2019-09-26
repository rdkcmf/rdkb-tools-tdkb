##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <name>TS_COSAMTA_GetCalls</name>
  <primitive_test_id/>
  <primitive_test_name>CosaMTA_GetCalls</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Retrieve all call info using cosa api for the given instance number of LineTable</synopsis>
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
    <test_case_id>TC_COSAMTA_38</test_case_id>
    <test_objective>Retrieve all call info using cosa api for the given instance number of LineTable</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CosaDmlMTAGetCalls</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load Cosamta module
2. Invoke CosaDmlMtaLineTableGetNumberOfEntries() to get the number of lines
3. Check if get operation was success or not and the no: of lines is greater than 0
4. If no: of lines is greater than 0, using CosaDmlMTAGetCalls() get the call info of each of the line
5. Otherwise return failure
4. Unload Cosamta module</automation_approch>
    <except_output>No: of line table entries should be greater than 0 and should retrieve the call info of each of the line</except_output>
    <priority>High</priority>
    <test_stub_interface>cosamta</test_stub_interface>
    <test_script>TS_COSAMTA_GetCalls</test_script>
    <skipped>No</skipped>
    <release_version>M68</release_version>
    <remarks>none</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cosamta","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_COSAMTA_GetCalls');

#Get the result of connection with test component and DUT 
loadmodulestatus =obj.getLoadModuleResult()
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus 

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS")

    # Get number of entries for MTA
    tdkTestObj = obj.createTestStep("CosaMTA_LineTableGetNumberOfEntries")
    tdkTestObj.addParameter("handleType",0);
    expectedresult="SUCCESS"
    tdkTestObj.executeTestCase(expectedresult)
    actualresult = tdkTestObj.getResult()
    details = tdkTestObj.getResultDetails()

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS")
        print "TEST STEP 1: Get the LineTableNumberOfEntries"
        print "EXPECTED RESULT 1: Should get the LineTableNumberOfEntries as greater than 0"
        print "ACTUAL RESULT 1: The LineTableNumberOfEntries is %s" %details
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        numOfEntries = details.split(':')[1].strip()
        if int(numOfEntries) > 0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS")
            print "TEST STEP 2: Get the LineTableNumberOfEntries"
            print "EXPECTED RESULT 2: Should get the LineTableNumberOfEntries as greater than 0"
            print "ACTUAL RESULT 2: The LineTableNumberOfEntries is %s" %numOfEntries
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS"

            for y in range(int(numOfEntries)):
                #Script to load the configuration file of the component
                tdkTestObj = obj.createTestStep("CosaMTA_GetCalls")    
                tdkTestObj.addParameter("value",y)
                expectedresult="SUCCESS"
                tdkTestObj.executeTestCase(expectedresult)
                actualresult = tdkTestObj.getResult()    
                resultDetails = " "
                resultDetails = tdkTestObj.getResultDetails()

                if expectedresult in actualresult and resultDetails != " ":
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS")
                    print "TEST STEP %s: Get call info for line %s" %(y+2, y+1)
                    print "EXPECTED RESULT %s: Should get the call info for line %s" %(y+2, y+1)
                    print "ACTUAL RESULT %s: call info for line %s:" %(y+2, y+1)
                    print ""
                    for x in resultDetails.split(";"):
                        print x
                    print ""
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                else:
                    tdkTestObj.setResultStatus("FAILURE")
                    print "TEST STEP %s: Get call info for line %s" %(y+2, y+1)
                    print "EXPECTED RESULT %s: Should get the call info for line %s" %(y+2, y+1)
                    print "ACTUAL RESULT %s: Failed to get the call info for line %s:" %(y+2, y+1)
                    print "%s" %resultDetails
                    print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            tdkTestObj.setResultStatus("FAILURE")
            print "TEST STEP 2: Get the LineTableNumberOfEntries"
            print "EXPECTED RESULT 2: LineTableNumberOfEntries should be greater than 0"
            print "ACTUAL RESULT 2: LineTableNumberOfEntries is not greater than 0, details :%s" %numOfEntries
            print "[TEST EXECUTION RESULT] : FAILURE"
    else:
        tdkTestObj.setResultStatus("FAILURE")
        print "TEST STEP 1: Get the LineTableNumberOfEntries"
        print "EXPECTED RESULT 1: Should get the LineTableNumberOfEntries successfully"
        print "ACTUAL RESULT 1: Failed to get the LineTableNumberOfEntries, Details :%s" %details
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("cosamta")
else:
    print "Failed to load the module"
    obj.setLoadModuleStatus("FAILURE")
    print "Module loading failed"
