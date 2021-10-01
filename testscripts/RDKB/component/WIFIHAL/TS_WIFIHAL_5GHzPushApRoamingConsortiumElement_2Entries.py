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
  <name>TS_WIFIHAL_5GHzPushApRoamingConsortiumElement_2Entries</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApRoamingConsortiumElement</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Set an OUI list with 2 OUI entries using wifi_pushApRoamingConsortiumElement() and verify it using wifi_getApRoamingConsortiumElement()</synopsis>
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
    <test_case_id>TC_WIFIHAL_448</test_case_id>
    <test_objective>Set an OUI list with 2 OUI entries using wifi_pushApRoamingConsortiumElement() and verify it using wifi_getApRoamingConsortiumElement()</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_pushApRoamingConsortiumElement
wifi_getApRoamingConsortiumElement</api_or_interface_used>
    <input_parameters>index:9</input_parameters>
    <automation_approch>1. Load wifihal module
2. Invoke wifi_getApRoamingConsortiumElement() to get the current OUI details and save them
3. Set a new RoamingConsortiumElement with 2 OUI entries using wifi_pushApRoamingConsortiumElement
4. Verify the push operation using wifi_getApRoamingConsortiumElement()
5. Revert to initial RoamingConsortiumElement
6. Unload wifihal module</automation_approch>
    <expected_output>Should successfully set an OUI list with 2 entries using wifi_pushApRoamingConsortiumElement()</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPushApRoamingConsortiumElement_2Entries</test_script>
    <skipped>No</skipped>
    <release_version>M84</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import binascii;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPushApRoamingConsortiumElement_2Entries');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Script to load the configuration file of the component
    passPoint_5G_Index = 9;
    oui_array_length = 3;

    tdkTestObj = obj.createTestStep("WIFIHAL_GetApRoamingConsortiumElement");
    tdkTestObj.addParameter("apIndex", passPoint_5G_Index);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "TEST STEP 1: Get and save the RoamingConsortiumElement  for 5GHz";
    print "EXPECTED RESULT 1: Should get the RoamingConsortiumElement  for 5GHz";

    if expectedresult in actualresult :
	print "ACTUAL RESULT 1: %s" %details;
	#Get the result of execution
	print "[TEST EXECUTION RESULT] : SUCCESS";
        tdkTestObj.setResultStatus("SUCCESS");

        #extract the entryCount, ouis and its length values to be used for revert operation
        entryCount = int(details.split(':')[1].strip().split(',')[0].split(' ')[1])
        ouis=details.split(':')[1].strip().split(',')
        #removing entry count from list
        ouis.pop(0)
        init_ouis=""
        init_lens=""

        for i in range (0, oui_array_length):
            init_ouis+=ouis[2*i].split(' ')[2]
            init_ouis+=","
            init_lens+=ouis[2*i+1].split(' ')[2]
            init_lens+=","

        #remove extra , at the end
        init_ouis=init_ouis[:-1]
        init_lens = init_lens[:-1]

        print "TEST STEP 2: Set RoamingConsortiumElement  2 OUIs for 5GHz";
        print "EXPECTED RESULT 2: Should successfully set RoamingConsortiumElement  2 OUIs for 5GHz";

        #Invoking the Push API
        ouiCount = 2
        ouiList = "001bc504bd,506f9b"
        ouiLen = str(len(binascii.a2b_hex("001bc504bd"))) + "," + str(len(binascii.a2b_hex("506f9b")))
        print ("Set the values EntryCount: " + str(ouiCount) + "  OUI: " + ouiList  + "  LenOfOUI: " + ouiLen );
        tdkTestObj = obj.createTestStep('WIFIHAL_PushApRoamingConsortiumElement');
        tdkTestObj.addParameter("apIndex", passPoint_5G_Index);
        tdkTestObj.addParameter("ouiCount", ouiCount);
        tdkTestObj.addParameter("ouiList", ouiList);
        tdkTestObj.addParameter("ouiLen", ouiLen);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        if expectedresult in actualresult :
	    print "ACTUAL RESULT 2: %s" %details;
	    print "[TEST EXECUTION RESULT] : SUCCESS";
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 3: Get the RoamingConsortiumElement  for 5GHz and verify push operation";
            print "EXPECTED RESULT 3: Get RoamingConsortiumElement for 5GHz should reflect the last push operation";

            #Invoking the Get API to validate the Push API
            tdkTestObj = obj.createTestStep("WIFIHAL_GetApRoamingConsortiumElement");
            tdkTestObj.addParameter("apIndex", passPoint_5G_Index);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult :
                print "ACTUAL RESULT 3: %s" %details;

                #extract the entryCount, ouis and its length values to compare with pushed values
                newEntryCount = int(details.split(':')[1].strip().split(',')[0].split(' ')[1])
                ouisList=details.split(':')[1].strip().split(',')
                #removing entry count from list
                ouisList.pop(0)
                new_ouis=""
                new_lens=""

                for i in range (0, ouiCount):
                    new_ouis+=ouisList[2*i].split(' ')[2]
                    new_ouis+=","
                    new_lens+=ouisList[2*i+1].split(' ')[2]
                    new_lens+=","

                #remove extra , at the end
                new_ouis=new_ouis[:-1]
                new_lens = new_lens[:-1]
                print ("Got the values EntryCount: " + str(newEntryCount) + "  OUI: " + new_ouis + "  LenOfOUI: " + new_lens);

                if new_ouis == ouiList  and new_lens == ouiLen:
                    print "Push operation successfully verified with get RoamingConsortiumElement"
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    print "Failed: Values set using push operation is not matching with get RoamingConsortiumElement output"
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "ACTUAL RESULT 3: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
                tdkTestObj.setResultStatus("FAILURE");

            #Revert RoamingConsortiumElement values to the initial ones
            print "TEST STEP 4: Revert RoamingConsortiumElement to initial values";
            print "EXPECTED RESULT 4: Should successfully revert RoamingConsortiumElement values";
            tdkTestObj = obj.createTestStep('WIFIHAL_PushApRoamingConsortiumElement');
            tdkTestObj.addParameter("apIndex", passPoint_5G_Index);
            tdkTestObj.addParameter("ouiCount", entryCount);
            tdkTestObj.addParameter("ouiList", init_ouis );
            tdkTestObj.addParameter("ouiLen", init_lens );
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            if expectedresult in actualresult :
	        print "ACTUAL RESULT 4: %s" %details;
	        print "[TEST EXECUTION RESULT] : SUCCESS";
                tdkTestObj.setResultStatus("SUCCESS");
            else:
                print "ACTUAL RESULT 4: %s" %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
                tdkTestObj.setResultStatus("FAILURE");
        else:
	    print "ACTUAL RESULT 2: %s" %details;
	    print "[TEST EXECUTION RESULT] : FAILURE";
            tdkTestObj.setResultStatus("FAILURE");
    else:
	print "ACTUAL RESULT 1: %s" %details;
	#Get the result of execution
	print "[TEST EXECUTION RESULT] : FAILURE";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
