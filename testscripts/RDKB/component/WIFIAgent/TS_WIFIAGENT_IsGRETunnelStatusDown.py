##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2018 RDK Management
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
<?xml version="1.0" encoding="UTF-8"?>
<xml>
  <id/>
  <version>2</version>
  <name>TS_WIFIAGENT_IsGRETunnelStatusDown</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Get</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To set Device.X_COMCAST-COM_GRE.Tunnel.1.Enable  to false and check whether the tunnel status is Down or not</synopsis>
  <groups_id/>
  <execution_time>4</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>Emulator</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_56</test_case_id>
    <test_objective>To set Device.X_COMCAST-COM_GRE.Tunnel.1.Enable  to false and check whether the tunnel status is Down or not</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>Device.X_COMCAST-COM_GRE.Tunnel.1.Enable
"Device.X_COMCAST-COM_GRE.Tunnel.1.Status"</input_parameters>
    <automation_approch>1. Load wifiagent module
2. Using WIFIAgent_Get, get and save Device.X_COMCAST-COM_GRE.Tunnel.1.Enable
3.Set Device.X_COMCAST-COM_GRE.Tunnel.1.Enable as false
3. Using WIFIAgent_Get, get Device.X_COMCAST-COM_GRE.Tunnel.1.Status
6. Restore value of Device.X_COMCAST-COM_GRE.Tunnel.1.Enable</automation_approch>
    <except_output>Device.X_COMCAST-COM_GRE.Tunnel.1.Status should be Down</except_output>
    <priority>High</priority>
    <test_stub_interface>WifiAgent</test_stub_interface>
    <test_script>TS_WIFIAGENT_IsGRETunnelStatusDown</test_script>
    <skipped>No</skipped>
    <release_version>M58</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script 
import tdklib; 
from time import sleep;
from xfinityWiFiLib import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_IsGRETunnelStatusDown');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");

    #Get current values of public wifi params
    expectedresult="SUCCESS";
    tdkTestObj,actualresult,orgValue = getPublicWiFiParamValues(obj);
    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1:Get values of PublicWiFi params"
        print "TEST STEP 1 : Should get values of PublicWiFi params"
        print "ACTUAL RESULT 1:%s" %orgValue
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Set values to enable public wifi
        setvalues = ["44","68.86.15.199","68.86.15.171","true","true","true"];
        tdkTestObj, actualresult, details = setPublicWiFiParamValues(obj,setvalues);
        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Enable public wifi"
            print "TEST STEP 2 : Should enable PublicWiFi"
            print "ACTUAL RESULT 2:%s" %details
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Get the Tunnel status
            tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.X_COMCAST-COM_GRE.Tunnel.1.Enable")
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            tunnelStatus = details.split("VALUE:")[1].split(' ')[0];

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Get the Tunnel status";
                print "EXPECTED RESULT 3: Should get the Tunnel Status";
                print "ACTUAL RESULT 3: Status is %s" %tunnelStatus;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Enable the Tunnel
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.X_COMCAST-COM_GRE.Tunnel.1.Enable")
                tdkTestObj.addParameter("paramValue","false")
                tdkTestObj.addParameter("paramType","boolean")
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Disable the Tunnel";
                    print "EXPECTED RESULT 4: Should disable the Tunnel"
                    print "ACTUAL RESULT 4: %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #check if Tunnel status is up or not
                    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                    tdkTestObj.addParameter("paramName","Device.X_COMCAST-COM_GRE.Tunnel.1.Status")
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();
                    status = details.split("VALUE:")[1].split(' ')[0];

                    if expectedresult in actualresult and "Down" in status:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Check if Tunnel staus is Down";
                        print "EXPECTED RESULT 5: Tunnel staus should be Down";
                        print "ACTUAL RESULT 5: Status is %s" %status;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Check if Tunnel staus is Down";
                        print "EXPECTED RESULT 5: Tunnel staus should be Down";
                        print "ACTUAL RESULT 5: Status is %s" %status;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                    #Revert the Tunnel Status
                    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                    tdkTestObj.addParameter("paramName","Device.X_COMCAST-COM_GRE.Tunnel.1.Enable")
                    tdkTestObj.addParameter("paramValue",tunnelStatus)
                    tdkTestObj.addParameter("paramType","boolean")
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 6: Revert the Tunnel Status";
                        print "EXPECTED RESULT 6: Should revert the Tunnel status"
                        print "ACTUAL RESULT 6: %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 6: Revert the Tunnel Status";
                        print "EXPECTED RESULT 6: Should revert the Tunnel status"
                        print "ACTUAL RESULT 6: %s " %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Disable the Tunnel";
                    print "EXPECTED RESULT 4: Should disable the Tunnel"
                    print "ACTUAL RESULT 4: %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 3: Get the Tunnel status";
                print "EXPECTED RESULT 3: Should get the Tunnel Status";
                print "ACTUAL RESULT 3: Status is  %s" %tunnelStatus;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert the values of public wifi params
            tdkTestObj, actualresult, details = setPublicWiFiParamValues(obj,orgValue);
            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 7:Revert the PublicWiFi param values"
                print "TEST STEP 7 : Should revert the PublicWiFi values"
                print "ACTUAL RESULT 7:%s" %details
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 7:Revert the PublicWiFi param values"
                print "TEST STEP 7 : Should revert the PublicWiFi param values"
                print "ACTUAL RESULT 7:%s" %details
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2:Enable PublicWiFi"
            print "TEST STEP 2 : Should enable PublicWiFi"
            print "ACTUAL RESULT 2:%s" %details
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1:Get values of PublicWiFi params"
        print "TEST STEP 1 : Should get values of PublicWiFi params"
        print "ACTUAL RESULT 1:%s" %orgValue
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");

else:
        print "Failed to load wifi module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
