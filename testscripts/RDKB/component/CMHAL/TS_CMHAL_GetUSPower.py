##########################################################################
#If not stated otherwise in this file or this component's Licenses.txt
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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>1</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_CMHAL_GetUSPower</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>CMHAL_GetParamCharValue</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To get the modulation and Power Levels of upstream channels and check whether it is in valid or not.</synopsis>
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
    <test_case_id>TC_CMHAL_45</test_case_id>
    <test_objective>To get the modulation and Power Levels of upstream channels and check whether it is valid or not.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>docsis_GetUSChannel</api_or_interface_used>
    <input_parameters>paramName : ModulationAndUSPower</input_parameters>
    <automation_approch>1. Load  cmhal module
2. Invoke docsis_GetUSChannel to get the modulation and the power levels of upstream channels.
3. The power levels must be as per the modulation type.
4. The test should return FAILURE if the power levels are not in range w.r.t modulation. 
5. Unload cmhal module</automation_approch>
    <except_output>The Power Level must be in a range w.r.t modulation.

if modulation is 64QAM  and 32QAM , Power Level should be within 8 and 54dBmV.

For 8-QAM and 16-QAM: Power Level should be within 8 and 55dBmV.

QPSK: Power Level should be within  +8 to +58 dBmV .</except_output>
    <priority>High</priority>
    <test_stub_interface>CM_HAL</test_stub_interface>
    <test_script>TS_CMHAL_GetUSPower</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("cmhal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_CMHAL_GetUSPower');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

     #This method invokes the HAL API docsis_GetUSChannel and retrieves the modulation and the powerlevels in upstream channels.
    tdkTestObj = obj.createTestStep("CMHAL_GetParamCharValue");
    tdkTestObj.addParameter("paramName","ModulationAndUSPower");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    Details = tdkTestObj.getResultDetails();
    print Details;
    List = Details.split(",");
    for item in List:
        Data = item.split(":");
        if "256QAM" or "256 QAM"in Data[0]:
            minpower = 8.00;
            maxpower = 54.00;
        elif "64QAM" or "64 QAM"in Data[0]:
            minpower = 8.00;
            maxpower = 54.00;
        elif "32QAM" or "32 QAM"  in Data[0]:
            minpower = 8.00;
            maxpower = 54.00;
        elif "16QAM" or "16 QAM"  in Data[0]:
            minpower = 8.00;
            maxpower = 55.00;
        elif "8QAM" or "8 QAM" in Data[0]:
            minpower = 8.00;
            maxpower = 55.00;
        elif "QPSK" in Data[0]:
            minpower = 8.00;
            maxpower = 58.00;
        else:
            minpower = 0;
            maxpower =0;
        
        if  Data[0]!=""  and "dBmV" in Data[1]:
            if minpower !=0 and float(Data[1].split(" ")[0]) >= minpower:
                status = "Success";
            else:
                status = "Failure";
                break; 
        elif "" not in Data[0]  and "dBmV" not in Data[1]:
            if minpower !=0 and float(Data[1]) >= minpower:
                status = "Success";
            else:
                status = "Failure";
                break; 
        elif "" in Data[0] and "" in Data[1]:
            status = "Success";
        elif not Data[0]:
            status = "Success";
        else:
            status = "Failure";
            break;
    if expectedresult in actualresult and "Success" in status:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get and validate the UpStream Modulation and power range";
        print "EXPECTED RESULT 1: Upstream power range should be within the range w.r.t Modulation";
        print "ACTUAL RESULT 1: Successfully validated the powerLevel";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get and validate the UpStream Modulation and powerrange";
        print "EXPECTED RESULT 1: upstream powerLevel should be within the range w.r.t Modulation";
        print "ACTUAL RESULT 1: Validation of powerLevel is failed";
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("cmhal");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";

