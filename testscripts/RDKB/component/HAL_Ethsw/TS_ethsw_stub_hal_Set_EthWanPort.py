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
  <version>9</version>
  <name>TS_ethsw_stub_hal_Set_EthWanPort</name>
  <primitive_test_id/>
  <primitive_test_name>ethsw_stub_hal_Set_EthWanPort</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set the ethwan port using CcspHalExtSw_setEthWanPort() and validate it using CcspHalExtSw_getEthWanPort()</synopsis>
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
    <test_case_id>TC_HAL_Ethsw_27</test_case_id>
    <test_objective>Set the ethwan port using CcspHalExtSw_setEthWanPort() and validate it using CcspHalExtSw_getEthWanPort()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Device should be in ethwan mode
2. Ccsp Components  should be in a running state of DUT
3.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>CcspHalExtSw_setEthWanPort() 
CcspHalExtSw_getEthWanPort()</api_or_interface_used>
    <input_parameters>CcspHalExtSw_setEthWanPort()  : port</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. Get and save the valid ethwan port options from tdk_platform.properties 
3. Get the current EthWan port using CcspHalExtSw_getEthWanPort()() and save it
4. From the list of port values saved from step2, set port values one by one using CcspHalExtSw_setEthWanPort(). 
5. Get the ethwan port and check if it is same as the set port
6. Revert the ethwan port to its original value
5. Unload halethsw module</automation_approch>
    <expected_output>Should successfully set ethwan ports using CcspHalExtSw_setEthWanPort()</expected_output>
    <priority>High</priority>
    <test_stub_interface>HAL_Ethsw</test_stub_interface>
    <test_script>TS_ethsw_stub_hal_Set_EthWanPort</test_script>
    <skipped>No</skipped>
    <release_version>M77</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib;
from tdkbVariables import *; 

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","1");
obj1 = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_Set_EthWanPort');
obj1.configureTestCase(ip,port,'TS_ethsw_stub_hal_Set_EthWanPort');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =obj1.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in (loadmodulestatus.upper() and  loadmodulestatus1.upper()):
    obj.setLoadModuleStatus("SUCCESS");
    obj1.setLoadModuleStatus("SUCCESS");

    #Get the default value from properties file
    tdkTestObj1 = obj1.createTestStep('ExecuteCmd');
    cmd = "sh %s/tdk_utility.sh parseConfigFile ETHWAN_PORT_OPTIONS" %TDK_PATH;
    print cmd;
    expectedresult="SUCCESS";
    tdkTestObj1.addParameter("command", cmd);
    tdkTestObj1.executeTestCase(expectedresult);
    actualresult = tdkTestObj1.getResult();
    details = ""
    details = tdkTestObj1.getResultDetails().strip();
    ports = ""
    ports = details.replace("\\n", "");
    print" ETHWAN PORT OPTIONS:",ports
    if ports != "" and ( expectedresult in  actualresult):
        tdkTestObj1.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the ETHWAN port options from tdk_platform properties file";
        print "EXPECTED RESULT 1: Should Get the ETHWAN port options form tdk_platform properties file";
        print "ACTUAL RESULT 1: The ETHWAN port options from tdk_platform properties file : %s" %ports ;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS"
        ports = ports.split(',')
        test_step = 2

        for port_set in ports:
	    print "PORT value to be set is : ",port_set
            tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_EthWanPort");
            expectedresult="SUCCESS";
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult :
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP %d : Retrieve the value of CcspHalExtSw_getEthWanPort" %test_step;
                print "EXPECTED RESULT %d: Should retrieve CcspHalExtSw_getEthWanPort successfully" %test_step
                print "ACTUAL RESULT %d: Current ethwan port is %s" %(test_step, details);
                print "[TEST EXECUTION RESULT] : %s" %actualresult ;
                #Set the result status of execution
	        test_step = test_step+1

                port_present = details
	        if port_present == port_set :
	    	    print "Both Current port and port to be set are the same. Skipping this set"
	    	    break;

                #------------- Set Ethwan port ----------------
                tdkTestObj = obj.createTestStep("ethsw_stub_hal_Set_EthWanPort");
                tdkTestObj.addParameter("port", int(port_set));
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP %d: Set ethwan port using CcspHalExtSw_setEthWanPort" %test_step;
                    print "EXPECTED RESULT %d: Should set ethwan port as %s using CcspHalExtSw_setEthWanPort"%(test_step, port_set);
                    print "ACTUAL RESULT %d: %s" %(test_step,details);
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    test_step = test_step+1

	            #----------- Cross verify ethwan port --------------------
	            tdkTestObj = obj.createTestStep('ethsw_stub_hal_Get_EthWanPort');
	            expectedresult="SUCCESS";
	            tdkTestObj.executeTestCase(expectedresult);
	            actualresult = tdkTestObj.getResult();
	            details = tdkTestObj.getResultDetails();
	            if expectedresult in actualresult and details :
                        tdkTestObj.setResultStatus("SUCCESS");
	    	        print "TEST STEP %d: Retrieve the value of CcspHalExtSw_getEthWanPort" %test_step;
	    	        print "EXPECTED RESULT %d: Should retrieve the value of CcspHalExtSw_getEthWanPort successfully" %test_step;
	    	        print "ACTUAL RESULT %d: Port after set is %s" %(test_step,details);
	    	        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
	    	        test_step = test_step+1

                        if details == port_set:
	    	            print "TEST STEP %d: Cross verifying values of GET and SET" %test_step;
	    	            print "EXPECTED RESULT %d: GET and SET values should be same" %test_step;
	    	            print "ACTUAL RESULT %d: GET and SET value is %s" %(test_step,details);
	    	            print "[TEST EXECUTION RESULT] : %s" %actualresult;
	    		    test_step = test_step+1

                            #--------- Re-setting the value -----------
                            tdkTestObj = obj.createTestStep("ethsw_stub_hal_Set_EthWanPort");
                            tdkTestObj.addParameter("port", int(port_present));
                            expectedresult="SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails();
                            if expectedresult in actualresult and details:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP %d: Revert the ethwan port" %test_step;
                                print "EXPECTED RESULT %d: Should Revert the ethwan port successfully" %test_step;
                                print "ACTUAL RESULT %d: %s" %(test_step,details);        
                                print "[TEST EXECUTION RESULT] : %s" %actualresult ; 
   	    		        test_step = test_step+1
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP %d: Revert the ethwan port" %test_step;
                                print "EXPECTED RESULT %d: Should Revert the ethwan port successfully" %test_step;
                                print "ACTUAL RESULT %d: %s" %(test_step, details);
                                print "[TEST EXECUTION RESULT] : %s" %actualresult;
	    		        test_step = test_step+1
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
	    	            print "TEST STEP %d: Cross verifying values of GET and SET" %test_step;
	    	            print "EXPECTED RESULT %d: GET and SET values should be same" %test_step;
	    	            print "ACTUAL RESULT %d: %s" %(test_step, details);
	    	            print "[TEST EXECUTION RESULT] : %s" %actualresult;
	    	            print "GET and SET values are not same";
	    		    test_step = test_step+1
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
	    	        print "TEST STEP %d: Retrieve the value of CcspHalExtSw_getEthWanPort" %test_step;
	    	        print "EXPECTED RESULT %d: Should retrieve the value of CcspHalExtSw_getEthWanPort successfully" %test_step;
	    	        print "ACTUAL RESULT %d: %s" %(test_step,details);
	    	        print "[TEST EXECUTION RESULT] : %s" %actualresult ;
	    	        test_step = test_step+1
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP %d: Set ethwan enable using CcspHalExtSw_setEthWanPort" %test_step;
                    print "EXPECTED RESULT %d: Should Set ethwan enable using CcspHalExtSw_setEthWanPort successfully" %test_step;
                    print "ACTUAL RESULT %d: %s" %(test_step,details);
                    print "[TEST EXECUTION RESULT] : %s" %actualresult ; 
	    	    test_step = test_step+1
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP %d: Retrieve the value of CcspHalExtSw_getEthWanPort" %test_step;
                print "EXPECTED RESULT %d: Should Retrieve the value of CcspHalExtSw_getEthWanPort successfully" %test_step;
                print "ACTUAL RESULT %d: %s" %(test_step,details);
                print "[TEST EXECUTION RESULT] : FAILURE" 
		test_step = test_step+1

    else:
        tdkTestObj1.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the ETHWAN port options from tdk_platform properties file";
        print "EXPECTED RESULT 1: Should Get the ETHWAN port options form tdk_platform properties file";
        print "ACTUAL RESULT 1: Failed to get the ETHWAN port options from tdk_platform properties file"
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE"

    obj.unloadModule("halethsw");
    obj1.unloadModule("sysutil");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
