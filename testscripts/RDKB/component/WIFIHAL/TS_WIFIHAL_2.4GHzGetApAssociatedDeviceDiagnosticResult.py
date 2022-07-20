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
<?xml version="1.0" encoding="UTF-8"?><xml>
  <id/>
  <version>3</version>
  <name>TS_WIFIHAL_2.4GHzGetApAssociatedDeviceDiagnosticResult</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetApAssociatedDeviceDiagnosticResult</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the Ap Associated Device Diagnostic Result for 2.4GHz.</synopsis>
  <groups_id/>
  <execution_time>15</execution_time>
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
    <test_case_id>TC_WIFIHAL_295</test_case_id>
    <test_objective>To get the Ap Associated Device Diagnostic Result for 2.4GHz</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, Emulator, RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Connect a 2.4G wifi client</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDeviceDiagnosticResult()</api_or_interface_used>
    <input_parameters>radioIndex: 0</input_parameters>
    <automation_approch>1.Load the module
2.Using WIFIHAL_GetApAssociatedDeviceDiagnosticResult call wifi_getApAssociatedDeviceDiagnosticResult() and get the result
3.Check if the STA details retrieved are valid for each of the connected STAs
4.Unload the module.</automation_approch>
    <except_output>Should detect and return the neighboring access points and the diagnostic results</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzGetApAssociatedDeviceDiagnosticResult</test_script>
    <skipped>No</skipped>
    <release_version/>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzGetApAssociatedDeviceDiagnosticResult');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else: 
        #Prmitive test case which is associated to this Script
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDeviceDiagnosticResult');
        tdkTestObj.addParameter("radioIndex", idx);
        expectedresult="SUCCESS";
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

        print "\nTEST STEP 1: Invoke the HAL API wifi_getApAssociatedDeviceDiagnosticResult()";
        print "EXPECTED RESULT 1: Should successfully get the API wifi_getApAssociatedDeviceDiagnosticResult()";

        if expectedresult in actualresult and "Output Array Size" in details:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 1: wifi_getApAssociatedDeviceDiagnosticResult() API invocation was success";
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Retrieve the Associated Device Diagnostic Results
            output_array_size =  details.split("Output Array Size = ")[1].split(" ")[0];
            print "Number of associated devices : %s" %output_array_size;

            print "\nTEST STEP 2 : Check if the number of STAs connected > 0";
            print "EXPECTED RESULT 2 : The number of STAs connected should be > 0";

            if output_array_size.isdigit():
                if int(output_array_size) > 0:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 2: Number of STAs connected : %s" %output_array_size;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Check if the STA details retrieved are valid
                    print "\nTEST STEP 3 : Check if the STA details retrieved are valid values";
                    print "EXPECTED RESULT 3 : STA details retrieved should be valid values";

                    status = 0;
                    for sta in range(1, int(output_array_size)+1):
                        sta_to_check = "For STA " + str(sta) + " ";
                        sta_details = details.split(sta_to_check)[1].split(": ")[1];
                        sta_mac = sta_details.split("MAC=")[1].split(",")[0];
                        sta_auth = sta_details.split("AuthState=")[1].split(",")[0];
                        sta_downlink = sta_details.split("LastDataDownlinkRate=")[1].split(",")[0];
                        sta_uplink = sta_details.split("LastDataUplinkRate=")[1].split(",")[0];
                        sta_sigstrength = sta_details.split("SignalStrength=")[1].split(",")[0];
                        sta_retransmissions = sta_details.split("Retransmissions=")[1].split(",")[0];
                        sta_operstd = sta_details.split("OperatingStd=")[1].split(",")[0];
                        sta_operchanbw = sta_details.split("OperatingChBw=")[1].split(",")[0];
                        sta_snr = sta_details.split("SNR=")[1].split(",")[0];
                        sta_dataframessentack = sta_details.split("DataFramesSentAck=")[1].split(",")[0];
                        sta_dataframessentnoack = sta_details.split("DataFramesSentNoAck=")[1].split(",")[0];
                        sta_rssi = sta_details.split("RSSI=")[1].split(",")[0];
                        sta_dissasso = sta_details.split("Disassociations=")[1].split(",")[0];
                        sta_authfail = sta_details.split("AuthFailures=")[1].split(",")[0];

                        print "\n%s: MAC = %s, Authentication State = %s, Last Data Downlink Rate = %s, Last Data Uplink Rate : %s, Signal Strength = %s, Retransmissions = %s, Operating Standard = %s, Operating Channel Bandwidth = %s, SNR = %s, Data Frames Sent Ack = %s, Data Frames Sent No Ack = %s, RSSI = %s, Disassociations = %s, Authentication Failures = %s" %(sta_to_check, sta_mac, sta_auth, sta_downlink, sta_uplink, sta_sigstrength, sta_retransmissions, sta_operstd, sta_operchanbw, sta_snr, sta_dataframessentack, sta_dataframessentnoack, sta_rssi, sta_dissasso, sta_authfail)

                        if sta_mac != "" and sta_auth.isdigit() and sta_downlink.isdigit() and sta_uplink.isdigit() and sta_sigstrength.lstrip('-').isdigit() and sta_retransmissions.isdigit() and sta_operstd != "" and sta_operchanbw.isdigit() and sta_snr.isdigit() and  sta_dataframessentack.isdigit() and sta_dataframessentnoack.isdigit() and sta_rssi.lstrip('-').isdigit() and sta_dissasso.isdigit() and sta_authfail.isdigit():
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "The STA details are valid";
                        else:
                            status = 1;
                            tdkTestObj.setResultStatus("FAILURE");
                            print "The STA details are NOT valid";

                    if status == 0 :
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 3: STA details retrieved are valid for all connected STAs";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 3: STA details retrieved are NOT valid for all connected STAs";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 2: Number of STAs connected : %s" %output_array_size;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Number of STA devices retrieved is not valid";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 1: Details : %s" %details;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";

