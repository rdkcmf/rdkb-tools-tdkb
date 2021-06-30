##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2021 RDK Management
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
  <name>TS_WIFIHAL_5GHzPublicWiFi_PushApInterworkingElement</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_PushApInterworkingElement</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke wifi_pushApInterworkingElement() HAL API and push the Interworking Element values and cross check by invoking wifi_getApInterworkingElement() API for 5GHz Public WiFi.</synopsis>
  <groups_id/>
  <execution_time>1</execution_time>
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
    <test_case_id>TC_WIFIHAL_568</test_case_id>
    <test_objective>Invoke wifi_pushApInterworkingElement() HAL API and push the Interworking Element values and cross check by invoking wifi_getApInterworkingElement() API for 5GHz Public WiFi.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>WIFIHALPushApInterworkingElement</api_or_interface_used>
    <input_parameters>apIndex : 9
interworkingEnabled : value set dynamically
accessNetworkType :  value set dynamically
internetAvailable :  value set dynamically
asra :  value set dynamically
esra :  value set dynamically
uesa :  value set dynamically
venueOptionPresent : 1
venueType :  value set dynamically
venueGroup :  value set dynamically
hessOptionPresent : 1
hessid :  value set dynamically</input_parameters>
    <automation_approch>1. Load the wifihal module.
2. Invoke wifi_getApInterworkingElement() HAL API for 5GHz Public WiFi and save the initial values. The GET operation should return success.
3. Invoke  wifi_pushApInterworkingElement() HAL API for 5GHz Public WiFi and set the values for the Interworking element. The SET operation should return success.
4. Cross check the values set with wifi_getApInterworkingElement() API.
5. Revert to initial values
6. Unload the module</automation_approch>
    <expected_output>wifi_pushApInterworkingElement() HAL API should push the Interworking Element values and wifi_getApInterworkingElement() API when invoked should return the set values properly for 5GHz Public WiFi.</expected_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_5GHzPublicWiFi_PushApInterworkingElement</test_script>
    <skipped>No</skipped>
    <release_version>M90</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
def push_element(tdkTestObj, apIndex, step, element):
    expectedresult = "SUCCESS"
    return_val = 1;
    tdkTestObj.addParameter("radioIndex",apIndex);
    #For the API wifi_pushApInterworkingElement, pass the following arguments
    tdkTestObj.addParameter("interworkingEnabled", element[0])
    tdkTestObj.addParameter("accessNetworkType", element[1])
    tdkTestObj.addParameter("internetAvailable", element[2])
    tdkTestObj.addParameter("asra", element[3])
    tdkTestObj.addParameter("esra", element[4])
    tdkTestObj.addParameter("uesa", element[5])
    tdkTestObj.addParameter("venueOptionPresent", element[6])
    tdkTestObj.addParameter("venueType", element[7])
    tdkTestObj.addParameter("venueGroup", element[8])
    tdkTestObj.addParameter("hessOptionPresent", element[9])
    tdkTestObj.addParameter("hessid", element[10] )
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        return_val = 0;
        print "TEST STEP %d: Invoke the wifi api wifi_pushApInterworkingElement() for 5GHz Public WiFi" %step;
        print "EXPECTED RESULT %d: Should successfully invoke wifi_pushApInterworkingElement()" %step;
        print "ACTUAL RESULT %d: %s"%(step, details);
        print "TEST EXECUTION RESULT %d: SUCCESS" %step;
        tdkTestObj.setResultStatus("SUCCESS");
    else:
        print "TEST STEP %d: Invoke the wifi api wifi_pushApInterworkingElement()" %step;
        print "EXPECTED RESULT %d: Should successfully invoke wifi_pushApInterworkingElement()" %step;
        print "ACTUAL RESULT %d: %s"%(step, details);
        print "TEST EXECUTION RESULT %d: FAILURE" %step;
        tdkTestObj.setResultStatus("FAILURE");
    return return_val;

def get_element(tdkTestObj, apIndex, step):
    expectedresult = "SUCCESS"
    element_details = [];
    tdkTestObj.addParameter("radioIndex",apIndex);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();

    if expectedresult in actualresult:
        print "TEST STEP %d: Invoke the wifi api wifi_getApInterworkingElement() for 5GHz Public WiFi" %step;
        print "EXPECTED RESULT %d: Should succeesully invoke wifi_getApInterworkingElement()" %step;
        print "ACTUAL RESULT %d: wifi_getApInterworkingElement() invoked successfully" %step;
        print "TEST EXECUTION RESULT %d: SUCCESS" %step;
        tdkTestObj.setResultStatus("SUCCESS");
        details = tdkTestObj.getResultDetails();

        if details != " ":
            status = 0;
            step = step + 1;
            print "TEST STEP %d: Get the Access Point InterworkingElement details" %step;
            print "EXPECTED RESULT %d: Should get the Access Point InterworkingElement details successfully" %step;
            print "ACTUAL RESULT %d: The Access Point InterworkingElement details are :%s"%(step, details);
            print "TEST EXECUTION RESULT %d: SUCCESS" %step;
            tdkTestObj.setResultStatus("SUCCESS");
            interworkingEnabled = int(details.split("interworkingEnabled")[1].split("=")[1].split(",")[0].strip());
            accessNetworkType = int(details.split("accessNetworkType")[1].split("=")[1].split(",")[0].strip());
            internetAvailable = int(details.split("internetAvailable")[1].split("=")[1].split(",")[0].strip());
            asra = int(details.split("asra")[1].split("=")[1].split(",")[0].strip());
            esra = int(details.split("esra")[1].split("=")[1].split(",")[0].strip());
            uesa = int(details.split("uesa")[1].split("=")[1].split(",")[0].strip());
            venueOptionPresent = int(details.split("venueOptionPresent")[1].split("=")[1].split(",")[0].strip());
            venueType = int(details.split("venueType")[1].split("=")[1].split(",")[0].strip());
            venueGroup = int(details.split("venueGroup")[1].split("=")[1].split(",")[0].strip());
            hessOptionPresent = int(details.split("hessOptionPresent")[1].split("=")[1].split(",")[0].strip());
            hessid = str(details.split("hessid")[1].split("=")[1].strip());
            element_details = [interworkingEnabled, accessNetworkType, internetAvailable, asra, esra, uesa, venueOptionPresent, venueType, venueGroup, hessOptionPresent, hessid]
        else:
            print "TEST STEP %d: Get the Access Point InterworkingElement details" %step;
            print "EXPECTED RESULT %d: Should get the Access Point InterworkingElement details successfully" %step;
            print "ACTUAL RESULT %d: The Access Point InterworkingElement details are not obtained :%s"%(step, details);
            print "TEST EXECUTION RESULT %d: FAILURE" %step;
            tdkTestObj.setResultStatus("FAILURE");
    else:
        print "TEST STEP %d: Invoke the wifi api wifi_getApInterworkingElement()" %step;
        print "EXPECTED RESULT %d: Should succeesully invoke wifi_getApInterworkingElement()" %step;
        print "ACTUAL RESULT %d: wifi_getApInterworkingElement() is not invoked successfully" %step;
        print "TEST EXECUTION RESULT %d: FAILURE" %step;
        tdkTestObj.setResultStatus("FAILURE");
    return element_details;

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;
from random import randint
import functools;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_5GHzPublicWiFi_PushApInterworkingElement');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    print "5GHz Public WiFi index : %s" %apIndex_5G_Public_Wifi;
    apIndex = apIndex_5G_Public_Wifi;

    tdkTestObj = obj.createTestStep('WIFIHAL_GetApInterworkingElement');
    tdkTestObj1 = obj.createTestStep('WIFIHAL_PushApInterworkingElement');
    step = 1;
    #Get the initial values and store them in initial_state
    initial_state = get_element(tdkTestObj, apIndex, step);
    print "Initial Interworking Element values : interworkingEnabled :%d, accessNetworkType :%d, internetAvailable :%d, asra :%d, esra :%d, uesa :%d, venueOptionPresent :%d, venueType :%d, venurGroup :%d, hessOptionPresent :%d, hessid : %s" %(initial_state[0], initial_state[1], initial_state[2], initial_state[3], initial_state[4], initial_state[5], initial_state[6], initial_state[7], initial_state[8], initial_state[9], initial_state[10]);

    if initial_state != []:
        #Set the element values [interworkingEnabled, accessNetworkType, internetAvailable, asra, esra, uesa, venueOptionPresent, venueType, venueGroup, hessOptionPresent, hessid]
        #The following values are randomly generated such that the values are with the range. venueOptionPresent and hessOptionPresent are to be set to 1.
        interworkingEnabled = randint(0, 1);
        accessNetworkType = randint(0, 15);
        internetAvailable = randint(0, 1);
        asra = randint(0, 1);
        esra = randint(0, 1);
        uesa = randint(0, 1);
        venueOptionPresent = 1;
        venueType = randint(0, 10);
        venueGroup = randint(0, 10);
        hessOptionPresent = 1;
        # Generate MAC address
        hessid_partial = "7a:36:76:41:9a:";
        x = str(randint(10,99));
        hessid = hessid_partial+x;
        element = [interworkingEnabled, accessNetworkType, internetAvailable, asra, esra, uesa, venueOptionPresent, venueType, venueGroup, hessOptionPresent, hessid];
        print "The Values to be pushed are : %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %s"%(interworkingEnabled, accessNetworkType, internetAvailable, asra, esra, uesa, venueOptionPresent, venueType, venueGroup, hessOptionPresent, hessid);
        #Push the element values
        step = step + 2;
        return_val = push_element(tdkTestObj1, apIndex, step, element);

        if return_val == 0:
            print "\nCross check with wifi_getApInterworkingElement API";
            step = step + 1;
            setvalues = get_element(tdkTestObj, apIndex, step);

            if reduce(lambda x, y: x and y, map(lambda a, b: a == b, setvalues, element), True):
                tdkTestObj.setResultStatus("SUCCESS");
                print "The values pushed by invoking wifi_pushApInterworkingElement() is same as values retrieved by wifi_GetApInterworkingElement()";
                #Revert Operation
                print "\n--------REVERT OPERATION---------";
                #Restore Initial values
                step = step + 2;
                return_val = push_element(tdkTestObj1, apIndex, step, initial_state);

                if return_val == 0:
                    tdkTestObj1.setResultStatus("SUCCESS");
                    print "Revert Operation successful";
                else:
                    tdkTestObj1.setResultStatus("FAILURE");
                    print "Revert Operation failed";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "The values pushed by invoking wifi_pushApInterworkingElement() is not the same as values retrieved by wifi_GetApInterworkingElement()";
        else:
            print "wifi_pushApInterworkingElement API failed";
            tdkTestObj1.setResultStatus("FAILURE");
    else:
        print "wifi_getApInterworkingElement API failed";
        tdkTestObj.setResultStatus("FAILURE");

    obj.unloadModule("wifihal");
else:
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading FAILURE";

