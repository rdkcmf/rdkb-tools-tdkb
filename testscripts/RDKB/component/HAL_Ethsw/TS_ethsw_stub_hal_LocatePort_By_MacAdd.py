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
  <version>4</version>
  <name>TS_ethsw_stub_hal_LocatePort_By_MacAdd</name>
  <primitive_test_id/>
  <primitive_test_name>ethsw_stub_hal_LocatePort_By_MacAddress</primitive_test_name>
  <primitive_test_version>4</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke CcspHalEthSwLocatePortByMacAddress() with a valid client MAC and check the port value returned</synopsis>
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
    <test_case_id>TC_HAL_Ethsw_43</test_case_id>
    <test_objective>Invoke CcspHalEthSwLocatePortByMacAddress() with a valid client MAC and check the port value returned</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. A Lan client should be connected with the DUT</pre_requisite>
    <api_or_interface_used>CcspHalEthSwLocatePortByMacAddress()</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1. Load  halethsw module.
2. Invoke CcspHalExtSw_getAssociatedDevice() to get the associated device details
3. Get the associated device's MAC and port from step 2 output
4. Invoke ethsw_stub_hal_LocatePort_By_MacAddress() with an the associated device MAC from step 3
5. Check if the port value returned by ethsw_stub_hal_LocatePort_By_MacAddress() is matching with the port value from step3
6. Unload  halethsw module.</automation_approch>
    <expected_output> CcspHalEthSwLocatePortByMacAddress() should return the port value associated with the client's MAC used for api invocation</expected_output>
    <priority>High</priority>
    <test_stub_interface>halethsw </test_stub_interface>
    <test_script>TS_ethsw_stub_hal_LocatePort_By_MacAdd</test_script>
    <skipped>No</skipped>
    <release_version>M83</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halethsw","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_ethsw_stub_hal_LocatePort_By_MacAdd');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus;

if "SUCCESS" in loadmodulestatus.upper():
        obj.setLoadModuleStatus("SUCCESS");

        #Script to load the configuration file of the component
        tdkTestObj = obj.createTestStep("ethsw_stub_hal_Get_AssociatedDevice");
        expectedresult = "SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();

        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Retrieve the details of associated device";
            print "EXPECTED RESULT 1: Should retrieve the details of associated device successfully";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : %s" %actualresult ;
            print "%s" %details;

            if "No Associated device" not in details:
                port=details.split(',')[1].strip().split(' ')[1]
                clientMac=details.split(',')[2].strip().split(' ')[2]
                print "Associated device MAC is %s and port is %s" %(clientMac, port)

                tdkTestObj = obj.createTestStep("ethsw_stub_hal_LocatePort_By_MacAddress");
                tdkTestObj.addParameter("macID", clientMac);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult and details and int(details)== int(port):
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Invoke CcspHalEthSwLocatePortByMacAddress() with a valid client MAC and check the port value returned";
                    print "EXPECTED RESULT 2: CcspHalEthSwLocatePortByMacAddress() should return the port value: ", port;
                    #Get the result of execution
                    print "Actual result: port value retuned is %s" %details;
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 2: Invoke CcspHalEthSwLocatePortByMacAddress() with a valid client MAC and check the port value returned";
                    print "EXPECTED RESULT 2: CcspHalEthSwLocatePortByMacAddress() should return the port value: ", port;
                    #Get the result of execution
                    print "Actual result: port value retuned is %s" %details;
                    print "[TEST EXECUTION RESULT] : %s" %actualresult;
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "ERROR: No Associated device found. Test requires a lan client"
                tdkTestObj.setResultStatus("FAILURE");
                print "[TEST EXECUTION RESULT] : FAILURE";

        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Retrieve the details of associated device";
            print "EXPECTED RESULT 1: Should retrieve the details of associated device successfully";
            print "[TEST EXECUTION RESULT] : FAILURE" ;
        obj.unloadModule("halethsw");
else:
        print "Failed to load the module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
