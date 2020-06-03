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
  <version>11</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_MoCAHAL_SetIfAcaConfig</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id> </primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>MoCAHAL_SetIfAcaConfig</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>Set the MoCA Interface ACA configuration details using the hal api  moca_setIfAcaConfig()</synopsis>
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
    <test_case_id>TC_MoCAHAL_20</test_case_id>
    <test_objective>Set the MoCA Interface ACA configuration details using the hal api  moca_setIfAcaConfig()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>moca_setIfAcaConfig()
moca_getIfAcaConfig()</api_or_interface_used>
    <input_parameters>ifIndex
nodeId
channel
reportNodes
probeType
ACAStart</input_parameters>
    <automation_approch>1. Load mocahal module
2. Invoke the HAL api moca_GetIfAcaConfig() and save the current ACA config
3. Using  moca_SetIfAcaConfig(), set new ACA config
4. The wrapper for moca_SetIfAcaConfig() will do a get after executing moca_SetIfAcaConfig() and will return the config value after set
5. Compare the values after set with the values used to set. Both should be same
6. Revert ACA config to its original values
7. Unload mocahal module</automation_approch>
    <expected_output>Should successfully set ACA config using moca_SetIfAcaConfig()</expected_output>
    <priority>High</priority>
    <test_stub_interface>mocahal</test_stub_interface>
    <test_script>TS_MoCAHAL_SetIfAcaConfig</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("mocahal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_MoCAHAL_SetIfAcaConfig');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    tdkTestObj = obj.createTestStep("MoCAHAL_GetIfAcaConfig");

    tdkTestObj.addParameter("ifIndex",1);
    tdkTestObj.addParameter("paramType","struct");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    conf = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and conf:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get MoCA interface ACA config using moca_getIfAcaConfig()"
        print "EXPECTED RESULT 1: Should Get MoCA interface ACA config"
        print "ACTUAL RESULT 1:  %s" %conf;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

	#store the current ACA config values
	nodeId= conf.split("NodeID=")[1].split(",")[0]
        probeType = conf.split("ProbeType=")[1].split(",")[0]
        channel = conf.split("Channel=")[1].split(",")[0]
        reportNodes = conf.split("ReportNodes=")[1].split(",")[0]
        ACAStart = conf.split("ACAStart=")[1].split(",")[0]

        #Set ACA config
	tdkTestObj = obj.createTestStep("MoCAHAL_SetIfAcaConfig");
	tdkTestObj.addParameter("nodeId",1);
	tdkTestObj.addParameter("channel",1);
	tdkTestObj.addParameter("probeType",0);
	tdkTestObj.addParameter("reportNodes",5);
        tdkTestObj.addParameter("ACAStart",1);
	tdkTestObj.addParameter("ifIndex",1);
	expectedresult="SUCCESS";
	tdkTestObj.executeTestCase(expectedresult);
	actualresult = tdkTestObj.getResult();
	details = tdkTestObj.getResultDetails();

	if expectedresult in actualresult:
            #Set the result status of execution
	    tdkTestObj.setResultStatus("SUCCESS");
	    print "TEST STEP 2: Set the MoCA interface ACA config using moca_setIfAcaConfig()"
	    print "EXPECTED RESULT 2: Should set the MoCA interface ACA config values as NodeID=1, ProbeType=0, Channel=1, ReportNodes=5, ACAStart=1";
            print "ACTUAL RESULT 2: The MoCA set configuration was success "
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] : SUCCESS";
            #MoCAHAL_SetIfAcaConfig() will do a get internally after doing set and return the get values
	    conf_afterset = details;

	    #store the ACA config values after set
	    nodeId_new= conf_afterset.split("NodeID=")[1].split(",")[0]
            probeType_new = conf_afterset.split("ProbeType=")[1].split(",")[0]
            channel_new = conf_afterset.split("Channel=")[1].split(",")[0]
            reportNodes_new = conf_afterset.split("ReportNodes=")[1].split(",")[0]
            ACAStart_new = conf_afterset.split("ACAStart=")[1].split(",")[0]

            if expectedresult in actualresult and int(nodeId_new) == 1 and int(probeType_new) == 0 and int(channel_new) == 1 and int(reportNodes_new) == 5 and int(ACAStart_new) == 1:
		#Set the result status of execution
		tdkTestObj.setResultStatus("SUCCESS");
		print "TEST STEP 3: Compare the configuration parameters with set values"
		print "EXPECTED RESULT 3: Configuration parameters should match with set values";
		print "ACTUAL RESULT 3: Configurations are matching. %s" %conf_afterset;
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : SUCCESS";
	    else:
		#Set the result status of execution
		tdkTestObj.setResultStatus("FAILURE");
		print "TEST STEP 3: Compare the configuration parameters with set values"
		print "EXPECTED RESULT 3: Configuration parameters should match with set values";
		print "ACTUAL RESULT 3: Configurations are NOT matching %s" %conf_afterset;
		#Get the result of execution
		print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert the ACA config
	    tdkTestObj = obj.createTestStep("MoCAHAL_SetIfAcaConfig");
	    tdkTestObj.addParameter("nodeId",int(nodeId));
	    tdkTestObj.addParameter("channel",int(channel));
	    tdkTestObj.addParameter("probeType",int(probeType));
	    tdkTestObj.addParameter("reportNodes",int(reportNodes));
            tdkTestObj.addParameter("ACAStart",int(ACAStart));
	    tdkTestObj.addParameter("ifIndex",1);
	    expectedresult="SUCCESS";
	    tdkTestObj.executeTestCase(expectedresult);
	    actualresult = tdkTestObj.getResult();
	    details = tdkTestObj.getResultDetails();

	    if expectedresult in actualresult:
                #Set the result status of execution
	        tdkTestObj.setResultStatus("SUCCESS");
	        print "TEST STEP 4: Revert the MoCA interface ACA config using moca_setIfAcaConfig()"
	        print "EXPECTED RESULT 4: Should revert the MoCA interface ACA config";
                print "ACTUAL RESULT 4: The MoCA ACA revert configuration was success %s" %details;
	        #Get the result of execution
	        print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
	        tdkTestObj.setResultStatus("FAILURE");
	        print "TEST STEP 4: Revert the MoCA interface ACA config using moca_setIfAcaConfig()"
	        print "EXPECTED RESULT 4: Should revert the MoCA interface ACA config";
                print "ACTUAL RESULT 4: The MoCA ACA revert configuration failed";
	        #Get the result of execution
	        print "[TEST EXECUTION RESULT] : FAILURE"
        else:
            #Set the result status of execution
	    tdkTestObj.setResultStatus("FAILURE");
	    print "TEST STEP 2: Set the MoCA interface ACA config using moca_setIfAcaConfig()"
	    print "EXPECTED RESULT 2: Should set the MoCA interface ACA config";
            print "ACTUAL RESULT 2: The MoCA set configuration failed, details: %s" %details;
	    #Get the result of execution
	    print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get MoCA interface ACA config using moca_getIfAcaConfig()"
        print "EXPECTED RESULT 1: Should Get MoCA interface ACA config"
        print "ACTUAL RESULT 1: %s" %conf;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("mocahal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
