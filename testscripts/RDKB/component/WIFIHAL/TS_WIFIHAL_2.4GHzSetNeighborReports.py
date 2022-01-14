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
  <name>TS_WIFIHAL_2.4GHzSetNeighborReports</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_SetNeighborReports</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Invoke the HAL API wifi_setNeighborReports() to set the neighbor reports for the connected client when Neighbor Reports Activation is enabled for 2.4G private radio AP.</synopsis>
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
    <test_case_id>TC_WIFIHAL_717</test_case_id>
    <test_objective>Invoke the HAL API wifi_setNeighborReports() to set the neighbor reports for the connected client when Neighbor Reports Activation is enabled for 2.4G private radio AP.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Connect a client to 2.4G radio private AP</pre_requisite>
    <api_or_interface_used>wifi_getApAssociatedDeviceDiagnosticResult3()
wifi_setNeighborReportActivation()
wifi_getNeighborReportActivation()
wifi_getRadioChannel()
wifi_setNeighborReports()</api_or_interface_used>
    <input_parameters>methodname : getNeighborReportActivation
methodname : setNeighborReportActivation
radioIndex : 2.4G radio private AP index
apIndex : 2.4G radio private AP index
param : 0 or 1
methodname : getRadioChannel
reports  : 1
bssid : client mac address
info : 2180
opClass : 5
channel : 2.4G radio channel
phyTable : 1</input_parameters>
    <automation_approch>1. Load the module
2. Invoke the HAL API wifi_getApAssociatedDeviceDiagnosticResult3() to get the connected client details and fetch the MAC address.
3. Invoke the HAL API wifi_getNeighborReportActivation() and check if the neighbor report activation is enabled
4. If not enabled, invoke wifi_setNeighborReportActivation() and set the enable status to true.
5. Invoke wifi_getNeighborReportActivation() to check if the enable is set properly.
6. Get the current radio channel using wifi_getRadioChannel().
7. Invoke the HAL API wifi_setNeighborReports() to set the neighbor reports by passing the parameters apIndex, reports, bssid, info, opClass, channel and phyTable and check if the API returns success.
8. Revert to initial values if required.
9. Unload the module.</automation_approch>
    <expected_output>The HAL API wifi_setNeighborReports() to set the neighbor reports for the connected client when Neighbor Reports Activation is enabled for 2.4G private radio AP should be invoked successfully.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifihal</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetNeighborReports</test_script>
    <skipped>No</skipped>
    <release_version>M97</release_version>
    <remarks/>
  </test_cases>
</xml>

'''
def InvokeAPI(tdkTestObj, methodName, param, idx) :
    #Giving the method name to invoke the api
    tdkTestObj.addParameter("methodName",methodName);
    tdkTestObj.addParameter("radioIndex", idx);
    tdkTestObj.addParameter("param",param);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return (actualresult, details);

# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from wifiUtility import *;

radio = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetNeighborReports');

loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    tdkTestObjTemp, idx = getIndex(obj, radio);

    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Get the connected client MAC
        step = 1;
        tdkTestObj = obj.createTestStep('WIFIHAL_GetApAssociatedDeviceDiagnosticResult3');
        tdkTestObj.addParameter("apIndex", idx);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();

        print "\nTEST STEP %d: Invoke the HAL API wifi_getApAssociatedDeviceDiagnosticResult3()" %step;
        print "EXPECTED RESULT %d: Should successfully invoke wifi_getApAssociatedDeviceDiagnosticResult3()" %step;

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d : wifi_getApAssociatedDeviceDiagnosticResult3() invoked successfully; Details : %s" %(step, details);
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Check if the number of associated client is greater than 0
            step = step + 1;
            size = details.split(":")[1].strip();
            output_array_size = size.split("=")[1].split(",")[0].strip();
            print "\nTEST STEP %d: The number of associated clients should be greater than 0" %step;
            print "EXPECTED RESULT %d: The number of associated clients should be greater than 0" %step;

            if int(output_array_size) != 0:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d: Number of associated clients : %d" %(step, int(output_array_size));
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Get the MAC address of the client
                mac = details.split("MAC")[1].split(",")[0].split("=")[1].strip();

                if mac != " ":
                    print "MAC Address of the client : %s" %mac;

                    #Check if the Neighbor Report is activated
                    step = step + 1;
                    revert_flag = 0;
                    setReport_flag = 0;
                    methodName = "getNeighborReportActivation";
                    param = 0;
                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                    actualresult, details = InvokeAPI(tdkTestObj, methodName, param, idx);

                    print "\nTEST STEP %d: Invoke the wifi_getNeighborReportActivation API to get the initial enable state of neighbor report activation" %step;
                    print "EXPECTED RESULT %d:Invocation of wifi_getNeighborReportActivation should be success" %step;

                    if expectedresult in actualresult :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: Invocation of wifi_getNeighborReportActivation was success. Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        enable = details.split(":")[1].strip()
                        print "\nInitial enable status is : %s" %enable;

                        if "Disabled" in enable:
                            step = step + 1;
                            #Enable the Neighbor report activation
                            methodName = "setNeighborReportActivation";
                            param = 1;
                            tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                            actualresult, details = InvokeAPI(tdkTestObj, methodName, param, idx);

                            print "\nTEST STEP %d: Invoke the wifi_setNeighborReportActivation API to set the neighbor report activation to enabled state" %step;
                            print "EXPECTED RESULT %d:Invocation of wifi_setNeighborReportActivation should be success" %step;

                            if expectedresult in actualresult :
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "ACTUAL RESULT %d: Invocation of wifi_setNeighborReportActivation was success. Details : %s" %(step, details);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                #Cross check the set with get
                                step = step + 1;
                                methodName = "getNeighborReportActivation";
                                param = 0;
                                tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                                actualresult, details = InvokeAPI(tdkTestObj, methodName, param, idx);

                                print "\nTEST STEP %d: Invoke the wifi_getNeighborReportActivation API to check if the Neighbor report is activated" %step;
                                print "EXPECTED RESULT %d:Invocation of wifi_getNeighborReportActivation should be success" %step;

                                if expectedresult in actualresult :
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: Invocation of wifi_getNeighborReportActivation was success. Details : %s" %(step, details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                    enable = details.split(":")[1].strip()
                                    print "\nCurrent enable status is : %s" %enable;

                                    if "Enabled" in enable:
                                        revert_flag = 1;
                                        setReport_flag = 1;
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "Successfully enabled the Neighbor Report Activation";
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "Unable to enable the Neighbor Report Activation";
                                else :
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: Invocation of wifi_getNeighborReportActivation was failed. Details : %s" %(step, details);
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";
                            else :
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "ACTUAL RESULT %d: Invocation of wifi_setNeighborReportActivation was failed. Details : %s" %(step, details);
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        else :
                            setReport_flag = 1;
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "Neighbor report Activation is already enabled";
                    else :
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: Invocation of wifi_getNeighborReportActivation was failed. Details : %s" %(step, details);
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";

                    if setReport_flag == 1:
                        #Channel to be set
                        step = step + 1;
                        print "\n*********************Parameters to set the Neighbor Report***********************";
                        tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamULongValue");
                        methodName = "getRadioChannel";
                        param = 0;
                        actualresult, details = InvokeAPI(tdkTestObj, methodName, param, idx);

                        print "\nTEST STEP %d: Get the current radio channel using the HAL API wifi_getRadioChannel()" %step;
                        print "EXPECTED RESULT %d: Should get the current channel using the HAL API wifi_getRadioChannel()" %step;

                        if expectedresult in actualresult:
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: API invocation was success; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                            currentChannel = details.split(":")[1].strip();

                            if currentChannel != "" and currentChannel.isdigit():
                                print "\nChannel parameter to be set : ", currentChannel;
                                currentChannel = int(currentChannel);
                                tdkTestObj.setResultStatus("SUCCESS");

                                #Access Point index
                                print "AP index parameter to be set : ", idx;
                                #Number of reports
                                reports = 1;
                                print "Reports parameter to be set : ", reports;
                                #Mac address of client
                                print "MAC Address parameter to be set : ", mac;
                                #BSSID Info
                                info = 2180;
                                print "BSSID info parameter to be set : ", info;
                                #Regulatory data
                                opClass = 5;
                                print "opClass parameter to be set : ", opClass;
                                #Physical type
                                phyTable = 1;
                                print "PhyTable parameter to be set : ", phyTable;

                                #Send Neighbor reports
                                step = step + 1;
                                tdkTestObj = obj.createTestStep('WIFIHAL_SetNeighborReports');
                                tdkTestObj.addParameter("apIndex", idx);
                                tdkTestObj.addParameter("reports", reports);
                                tdkTestObj.addParameter("bssid", mac);
                                tdkTestObj.addParameter("info", info);
                                tdkTestObj.addParameter("opClass", opClass);
                                tdkTestObj.addParameter("channel", currentChannel);
                                tdkTestObj.addParameter("phyTable", phyTable);
                                tdkTestObj.executeTestCase(expectedresult);
                                actualresult = tdkTestObj.getResult();
                                details = tdkTestObj.getResultDetails();

                                print "\nTEST STEP %d: Invoke the HAL API wifi_setNeighborReports() to set the neighbor reports" %step;
                                print "EXPECTED RESULT %d: wifi_setNeighborReports() should be invoked successfully" %step;

                                if expectedresult in actualresult :
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d : wifi_setNeighborReports() invoked successfully" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";
                                else :
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d : wifi_setNeighborReports() not invoked successfully" %step;
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";

                                #Revert operation
                                if revert_flag == 1:
                                    #Disable the Neighbor report activation
                                    methodName = "setNeighborReportActivation";
                                    param = 0;
                                    tdkTestObj = obj.createTestStep("WIFIHAL_GetOrSetParamBoolValue");
                                    actualresult, details = InvokeAPI(tdkTestObj, methodName, param, idx);

                                    if expectedresult in actualresult :
                                        print "Reverting Neighbor Report Activation is success";
                                        tdkTestObj.setResultStatus("SUCCESS");
                                    else :
                                        print "Reverting Neighbor Report Activation failed";
                                        tdkTestObj.setResultStatus("FAILURE");
                                else:
                                    print "Revert operation is not required";
                            else:
                                print "Channel parameter to be set is null or invalid ", currentChannel;
                                tdkTestObj.setResultStatus("FAILURE");
                        else :
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: API invocation was failed; Details : %s" %(step, details);
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else :
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Neighbor Reports cannot be set as Neighbor Report Activation is not in enabled state";
                else :
                    tdkTestObj.setResultStatus("FAILURE");
                    print "MAC Address is not fetched successfully";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Number of associated clients : %d" %(step, int(output_array_size));
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Failed to invoke wifi_getApAssociatedDeviceDiagnosticResult3()" %step;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");
else:
    print "Failed to load the module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
