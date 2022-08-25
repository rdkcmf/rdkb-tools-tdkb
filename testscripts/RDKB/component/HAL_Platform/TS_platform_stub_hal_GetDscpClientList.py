##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2022 RDK Management
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
  <version>11</version>
  <name>TS_platform_stub_hal_GetDscpClientList</name>
  <primitive_test_id/>
  <primitive_test_name>platform_stub_hal_GetDscpClientList</primitive_test_name>
  <primitive_test_version>5</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API platform_hal_getDscpClientList() and check if the DSCP client List data retrieved is valid.</synopsis>
  <groups_id/>
  <execution_time>2</execution_time>
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
    <test_case_id>TC_HAL_PLATFORM_93</test_case_id>
    <test_objective>Invoke the HAL API platform_hal_getDscpClientList() and check if the DSCP client List data retrieved is valid.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>platform_hal_getDscpClientList()</api_or_interface_used>
    <input_parameters>interfaceType : 1(DOCSIS)</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API platform_hal_getDscpClientList() to retrieve the DSCP client list comprising of interface mac addresses, its corresponding DSCP values and the  txBytes and rxBytes details.
3. Check if the invocation is success and if all the values retrieved are valid.
4. Unload the module</automation_approch>
    <expected_output>The HAL API platform_hal_getDscpClientList() should be invoked successfully and the DSCP details received should be valid.</expected_output>
    <priority>High</priority>
    <test_stub_interface>platformhal</test_stub_interface>
    <test_script>TS_platform_stub_hal_GetDscpClientList</test_script>
    <skipped>No</skipped>
    <release_version>M104</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("halplatform","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_platform_stub_hal_GetDscpClientList');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Get the DSCP Client List
    tdkTestObj = obj.createTestStep("platform_stub_hal_GetDscpClientList");
    #For DOCSIS interface
    tdkTestObj.addParameter("interfaceType",1);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n","");

    print "\nTEST STEP 1: Invoke the HAL API platform_hal_getDscpClientList() to retrieve the DSCP Client List values";
    print "EXPECTED RESULT 1: platform_hal_getDscpClientList() should be invoked successfully";

    if expectedresult in actualresult and "platform_hal_getDscpClientList() function invocation was successful" in details:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: platform_hal_getDscpClientList() API is invoked successfully";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check if the DSCP details are valid
        flag = 0;
        print "\nTEST STEP 2 : Check if the DSCP details retrieved are valid";
        print "EXPECTED RESULT 2 : The DSCP details retrieved should be valid";

        #Get the total DSCP number of elements
        noOfElements = details.split("Total DSCP number of elements = ")[1].split(";")[0];

        if noOfElements.isdigit():
            noOfElements = int(noOfElements);
            print "Total Number of DSCP Elements : ", noOfElements;
            tdkTestObj.setResultStatus("SUCCESS");

            for element in range(1, noOfElements+1):
                print "\n**********For DSCP Element %d**********" %element;
                elementDetails = details.split(";")[element + 1];
                dscpValue = elementDetails.split("DSCP value[")[1].split("]")[0];

                if dscpValue.isdigit() and int(dscpValue) >= 0 and int(dscpValue) <= 63:
                    print "DSCP value of the element is %s and it is valid" %dscpValue;
                    tdkTestObj.setResultStatus("SUCCESS");
                    noOfClients = elementDetails.split("DSCP numClients[")[1].split("]")[0];

                    if noOfClients.isdigit() and int(noOfClients) > 0:
                        noOfClients = int(noOfClients);
                        print "Total Number of Clients : ", noOfClients;
                        tdkTestObj.setResultStatus("SUCCESS");

                        for client in range(1, noOfClients+1):
                            clientDetails = elementDetails.split("DSCP client num")[client];
                            mac = clientDetails.split("mac - ")[1].split(",")[0];
                            rxBytes = clientDetails.split("rxBytes - ")[1].split(",")[0];
                            txBytes = clientDetails.split("txBytes - ")[1].split(" ")[0];
                            print "-----For Client %d-----" %client;
                            print "MAC : %s" %mac;
                            print "rxBytes : %s" %rxBytes;
                            print "txBytes : %s" %txBytes;

                            if mac != "" and rxBytes.isdigit() and txBytes.isdigit():
                                print "The DSCP counter details for client %d are valid" %client;
                                tdkTestObj.setResultStatus("SUCCESS");
                            else:
                                flag = 1;
                                print "The DSCP counter details for client %d are NOT valid" %client;
                                tdkTestObj.setResultStatus("FAILURE");
                                break;
                    else:
                        flag = 1;
                        print "Total Number of Clients is not a valid value";
                        tdkTestObj.setResultStatus("FAILURE");
                else:
                    flag = 1;
                    print "DSCP value of the element is %s and it is NOT valid" %dscpValue;
                    tdkTestObj.setResultStatus("FAILURE");
        else:
            flag = 1;
            print "Total Number of DSCP Elements is not a valid value";
            tdkTestObj.setResultStatus("FAILURE");

        if flag == 0:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: The DSCP values retrieved are valid";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: The DSCP values retrieved are NOT valid";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: %s"%details;
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("halplatform");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
