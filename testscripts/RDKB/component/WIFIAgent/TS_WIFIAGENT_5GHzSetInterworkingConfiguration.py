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
  <version>1</version>
  <name>TS_WIFIAGENT_5GHzSetInterworkingConfiguration</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set_LargeValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if set operation of Interworking Configuration using Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters is successful when the Interworking RFC, Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable and the Interworking Service, Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable are enabled.</synopsis>
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
    <test_case_id>TC_WIFIAGENT_224</test_case_id>
    <test_objective>To check if set operation of Interworking Configuration using Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters is successful when the Interworking RFC, Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable and the Interworking Service, Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable are enabled.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable
paramValue : true/false
paramType : boolean
paramName : Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable
paramValue : true/false
paramType : boolean
ParmName : Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters
ParamValue : "{"ANQP":{"IPAddressTypeAvailabilityANQPElement":{"IPv6AddressType":0,"IPv4AddressType":0},"DomainANQPElement":{"DomainName":[]},"RoamingConsortiumANQPElement":{"OI":[{ "OI": "506f9a" }, { "OI": "001bc504bd" }, { "OI": "506f9b" }, { "OI": "506f9c" }]},"NAIRealmANQPElement":{"Realm":[]},"3GPPCellularANQPElement":{"GUD":0,"PLMN":[]},"VenueNameANQPElement":{"VenueInfo":[{ "Length": 7, "Language": "eng", "Name": "resi" }]}}}"
ParamType : string</input_parameters>
    <automation_approch>1. Load the wifiagent module.
2. Check if the Interworking RFC, Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable, is enabled. If not enabled, enable it and validate with get.
3. Check if the Interworking enable, Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable is enabled. If not, enable it and validate with get.
4. Check if the initial value of Interworking configuration can be retrieved using Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters.
5. Set Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters to a new configuration and validate the SET with GET.
6. Revert Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable if required.
7. Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable if required.
8. Unload the wifiagent module.</automation_approch>
    <expected_output>Set operation of Interworking Configuration using Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters should be successful when the Interworking RFC, Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable and the Interworking Service, Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable are enabled.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_5GHzSetInterworkingConfiguration</test_script>
    <skipped>No</skipped>
    <release_version>M105</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
def getParameter(tdkTestObj, param):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("paramName",param);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    return actualresult, details;

def setParameter(tdkTestObj, param, setValue, type):
    expectedresult = "SUCCESS";
    tdkTestObj.addParameter("paramName",param);
    tdkTestObj.addParameter("paramValue",setValue);
    tdkTestObj.addParameter("paramType",type);
    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
    return actualresult, details;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkutility import *;

#Test component to be tested
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
wifiobj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHzSetInterworkingConfiguration');

#Get the result of connection with test component and DUT
loadmodulestatus1=wifiobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    wifiobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Check if the Interworking RFC is enabled
    step = 1
    param_rfc = "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable";
    print "\nTEST STEP %d : Get the initial enable status of Interworking RFC using Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable" %step;
    print "EXPECTED RESULT %d : Should retrieve the value of Interworking RFC successfully" %step;

    tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
    actualresult, details = getParameter(tdkTestObj, param_rfc);

    if expectedresult in actualresult and details != "" :
        rfc_initial = details.split("VALUE:")[1].split(" ")[0].strip();
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Initial Interworking RFC is retrieved successfully as : %s" %(step, rfc_initial);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #If the interworking RFC is not enabled initially, set it to "true"
        proceed_flag = 0;
        rfc_revert = 0;
        if rfc_initial != "true":
            step = step + 1;
            setValue = "true";
            type = "boolean";

            print "\nTEST STEP %d: Set Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable to %s" %(step, setValue);
            print "EXPECTED RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable should be set to %s successfully" %(step, setValue);

            tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
            actualresult, details = setParameter(tdkTestObj, param_rfc, setValue, type);

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Interworking RFC enabled successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Revalidate with GET
                step = step + 1;
                print "\nTEST STEP %d : Validate the Interworking RFC SET operation with GET" %step;
                print "EXPECTED RESULT %d : RFC value set should be successfully validated with GET" %step;

                tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
                actualresult, details = getParameter(tdkTestObj, param_rfc);

                if expectedresult in actualresult and details != "" :
                    rfc_curr = details.split("VALUE:")[1].split(" ")[0].strip();
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d: Current Interworking RFC is retrieved successfully as : %s" %(step, rfc_curr);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    if rfc_curr == setValue:
                        rfc_revert = 1;
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "RFC SET operation validated successfully";
                    else:
                        proceed_flag = 1;
                        tdkTestObj.setResultStatus("FAILURE");
                        print "RFC SET operation NOT validated successfully";
                else :
                    proceed_flag = 1;
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d: Current Interworking RFC NOT retrieved successfully; Details : %s" %(step, details);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                proceed_flag = 1;
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Interworking RFC NOT enabled successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable is already enabled, SET operation not required";

        #Get the interworking enable status for AP 10
        if proceed_flag == 0 :
            step = step + 1;
            param_service = "Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable";
            print "\nTEST STEP %d : Get the initial enable status of Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable" %step;
            print "EXPECTED RESULT %d : Should retrieve the value of Interworking Service Enable successfully" %step;

            tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
            actualresult, details = getParameter(tdkTestObj, param_service);

            if expectedresult in actualresult and details != "" :
                service_enable_initial = details.split("VALUE:")[1].split(" ")[0].strip();
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Initial Interworking Service Enable is retrieved successfully as : %s" %(step, service_enable_initial);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #If the interworking service enable is not enabled initially, set it to "true"
                service_revert = 0;
                if service_enable_initial != "true":
                    step = step + 1;
                    setValue = "true";
                    type = "boolean";

                    print "\nTEST STEP %d: Set Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable to %s" %(step, setValue);
                    print "EXPECTED RESULT %d: Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable should be set to %s successfully" %(step, setValue);

                    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
                    actualresult, details = setParameter(tdkTestObj, param_service, setValue, type);

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Interworking Service enabled successfully; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Revalidate with GET
                        step = step + 1;
                        print "\nTEST STEP %d : Validate the Interworking Service enable SET operation with GET" %step;
                        print "EXPECTED RESULT %d : Interworking Service enable value set should be successfully validated with GET" %step;

                        tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get");
                        actualresult, details = getParameter(tdkTestObj, param_service);

                        if expectedresult in actualresult and details != "" :
                            service_curr = details.split("VALUE:")[1].split(" ")[0].strip();
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Current Interworking Service enable is retrieved successfully as : %s" %(step, service_curr);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            if service_curr == setValue:
                                service_revert = 1;
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "Interworking Service enable SET operation validated successfully";
                            else:
                                proceed_flag = 1;
                                tdkTestObj.setResultStatus("FAILURE");
                                print "Interworking Service enable SET operation NOT validated successfully";
                        else :
                            proceed_flag = 1;
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Current Interworking Service enable NOT retrieved successfully; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        proceed_flag = 1;
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Interworking Service NOT enabled successfully; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable is already enabled, SET operation not required";

                #Get the Interworking configuration
                if proceed_flag == 0:
                    step = step + 1;
                    param_config = "Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters"
                    print "\nTEST STEP %d : Get the initial Interworking configuration using Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters" %step;
                    print "EXPECTED RESULT %d : Should retrieve the Interworking configuration successfully" %step;

                    tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get_LargeValue");
                    tdkTestObj.addParameter("ParamName",param_config);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    if expectedresult in actualresult and details != "" :
                        interworking_initial = details.split("VALUE:")[1].split(" TYPE")[0].replace('\\', '');
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Initial Interworking configuration is retrieved successfully as : %s" %(step, interworking_initial);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Set to a new configuration
                        step = step + 1;
                        setValue = "{\"ANQP\":{\"IPAddressTypeAvailabilityANQPElement\":{\"IPv6AddressType\":0,\"IPv4AddressType\":0},\"DomainANQPElement\":{\"DomainName\":[]},\"RoamingConsortiumANQPElement\":{\"OI\":[{ \"OI\": \"506f9a\" }, { \"OI\": \"001bc504bd\" }, { \"OI\": \"506f9b\" }, { \"OI\": \"506f9c\" }]},\"NAIRealmANQPElement\":{\"Realm\":[]},\"3GPPCellularANQPElement\":{\"GUD\":0,\"PLMN\":[]},\"VenueNameANQPElement\":{\"VenueInfo\":[{ \"Length\": 7, \"Language\": \"eng\", \"Name\": \"resi\" }]}}}"
                        print "\nTEST STEP %d: Set Interworking Configuration to %s" %(step, setValue);
                        print "EXPECTED RESULT %d: Interworking Configuration should be set successfully" %(step);

                        tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set_LargeValue');
                        tdkTestObj.addParameter("ParamName",param_config);
                        tdkTestObj.addParameter("ParamValue",setValue);
                        tdkTestObj.addParameter("ParamType","string");
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                        if expectedresult in actualresult:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: Interworking Configuration set successfully; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Revalidate with GET
                            step = step + 1;
                            print "\nTEST STEP %d : Get the current Interworking configuration using Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingService.Parameters" %step;
                            print "EXPECTED RESULT %d : Should retrieve the current Interworking configuration successfully" %step;

                            tdkTestObj = wifiobj.createTestStep("WIFIAgent_Get_LargeValue");
                            tdkTestObj.addParameter("ParamName",param_config);
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                            if expectedresult in actualresult and details != "" :
                                interworking_curr = details.split("VALUE:")[1].split(" TYPE")[0].replace('\\', '');
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: Current Interworking configuration is retrieved successfully as : %s" %(step, interworking_curr);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                if interworking_curr == setValue:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "Interworking Configuration SET operation validated successfully";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "Interworking Configuration SET operation NOT validated successfully";
                            else :
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: Current Interworking configuration NOT retrieved successfully; Details : %s" %(step, details);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: Interworking Configuration NOT set successfully; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Initial Interworking configuration is NOT retrieved successfully as : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable is not enabled successfully, cannot proceed...";

                #Revert the interworking service enable
                if service_revert == 1:
                    step = step + 1;
                    print "\nTEST STEP %d: Revert Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable to %s" %(step, service_enable_initial);
                    print "EXPECTED RESULT %d: Device.WiFi.AccessPoint.10.X_RDKCENTRAL-COM_InterworkingServiceEnable should be reverted to %s successfully" %(step, service_enable_initial);

                    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
                    actualresult, details = setParameter(tdkTestObj, param_service, service_enable_initial, type);

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Interworking Service reverted successfully; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Interworking Service NOT reverted successfully; Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    print "Interworking Service Enable revert operation is not required";
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Initial Interworking Service Enable is NOT retrieved successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable is not enabled successfully, cannot proceed...";

        #Revert the interworking RFC
        if rfc_revert == 1:
            step = step + 1;
            print "\nTEST STEP %d: Revert Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable to %s" %(step, rfc_initial);
            print "EXPECTED RESULT %d: Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.WiFi-Interworking.Enable should be reverted to %s successfully" %(step, rfc_initial);

            tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
            actualresult, details = setParameter(tdkTestObj, param_rfc, rfc_initial, type);

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Interworking RFC reverted successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Interworking RFC NOT reverted successfully; Details : %s" %(step, details);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            print "Interworking Feature RFC revert operation is not required";
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Initial Interworking RFC is NOT retrieved successfully; Details :  %s" %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    wifiobj.unloadModule("wifiagent")
else:
    print "Failed to load module";
    wifiobj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
