##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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
  <version>2</version>
  <name>TS_WIFIHAL_2.4GHzSetRadioExtChannel_BWAuto</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIHAL_GetOrSetParamStringValue</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>This is a positive scenario which sets the channel bandwidth to Auto, gets the current extension channel and then trying to change the extension channel from original one</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_WIFIHAL_110</test_case_id>
    <test_objective>To set the channel bandwidth to Auto, get the current extension channel and then try to change the extension channel from original one</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components and TDK Component
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>wifi_setRadioOperatingChannelBandwidth()
wifi_getRadioOperatingChannelBandwidth()
wifi_getRadioExtChannel()
wifi_setRadioExtChannel()</api_or_interface_used>
    <input_parameters>methodName   :   setChannelBandwidth
methodName   :   getChannelBandwidth
methodName   :   setRadioExtChannel
methodName   :   getRadioExtChannel
radioIndex   :   0</input_parameters>
    <automation_approch>1.Configure the Function info in Test Manager GUI  which needs to be tested
(WIFIHAL_GetOrSetParamStringValue  - func name - "If not exists already"
 WIFIHAL - module name
 Necessary I/P args as Mentioned in Input)
2.Python Script will be generated/overrided automatically by Test Manager with provided arguments in configure page (TS_WIFIHAL_2.4GHzSetRadioExtChannel_BW40MHz.py)
3.Execute the generated Script(TS_WIFIHAL_2.4GHzSetRadioExtChannel_BWAuto.py) using execution page of  Test Manager GUI
4.wifihalstub which is a part of TDK Agent process, will be in listening mode to execute TDK Component function named WIFIHAL_GetOrSetParamStringValue through registered TDK wifihalstub function along with necessary arguments
5.WIFIHAL_GetOrSetParamBoolValue function will call Ccsp Base Function named "ssp_WIFIHALGetOrSetParamStringValue", that inturn will call WIFIHAL Library Functions
wifi_setRadioOperatingChannelBandwidth() and wifi_getRadioOperatingChannelBandwidth()
6.Response(s)(printf) from TDK Component,Ccsp Library function and wifihalstub would be logged in Agent Console log based on the debug info redirected to agent console
7.wifihalstub will validate the available result (from agent console log and Pointer to instance as updated) with expected result
8.Test Manager will publish the result in GUI as SUCCESS/FAILURE based on the response from wifihalstub</automation_approch>
    <except_output>CheckPoint
1: wifi_setRadioOperatingChannelBandwidth() sets the channel bandwidth to Auto
2.wifi_getRadioOperatingChannelBandwidth() gets the currently set bandwidth as Auto
3.wifi_getRadioExtChannel() gets the current extension channel
4.wifi_setRadioExtChannel() sets the extension channel to a new value
5.wifi_getRadioExtChannel() gets the previously set extension channel and verifies that it is not the same as the initial channel.</except_output>
    <priority>High</priority>
    <test_stub_interface>WIFIHAL</test_stub_interface>
    <test_script>TS_WIFIHAL_2.4GHzSetRadioExtChannel_BWAuto</test_script>
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
radio2 = "2.4G"

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifihal","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIHAL_2.4GHzSetRadioExtChannel_BWAuto');


def ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, param, methodname):
    tdkTestObj = obj.createTestStep(primitive);
    tdkTestObj.addParameter("radioIndex", radioIndex);
    #'param' is valid for only set operations. It isdummy attribute for get functions
    tdkTestObj.addParameter("param", param);
    tdkTestObj.addParameter("methodName", methodname);
    expectedresult="SUCCESS";

    #Execute the test case in DUT
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    return (tdkTestObj, actualresult, details);


loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus

if "SUCCESS" in loadmodulestatus.upper():
    obj.setLoadModuleStatus("SUCCESS");
    #Validate wifi_getApAssociatedDeviceDiagnosticResult2() for 2.4GHZ
    tdkTestObjTemp, idx = getIndex(obj, radio2);
    ## Check if a invalid index is returned
    if idx == -1:
        print "Failed to get radio index for radio %s\n" %radio2;
        tdkTestObjTemp.setResultStatus("FAILURE");
    else:
        #Calling the method to execute wifi_getRadioOperatingChannelBandwidth() inorder to get the initial channel bandwidth
        expectedresult = "SUCCESS";
        radioIndex = idx
        getMethod = "getChannelBandwidth"
        primitive = 'WIFIHAL_GetOrSetParamStringValue'

        #Calling the method to execute wifi_getRadioExtChannel()
        tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
        initBandwidth = details.split(":")[1].strip()

        if expectedresult in actualresult :
           #Set the result status of execution
           tdkTestObj.setResultStatus("SUCCESS");
           print "TEST STEP : To get the initial operating channel bandwidth"
           print "EXPECTED RESULT : To successfully get the initial channel bandwidth"
           print "ACTUAL RESULT : %s " %details
           #Get the result of execution
           print "[TEST EXECUTION RESULT] : SUCCESS";

           expectedresult="SUCCESS";
           radioIndex = idx
           setMethod = "setChannelBandwidth"
           primitive = 'WIFIHAL_GetOrSetParamStringValue'

           #Calling the method to execute wifi_setRadioOperatingChannelBandwidth()
           tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, 'Auto', setMethod)

           if expectedresult in actualresult :
              #Set the result status of execution
              tdkTestObj.setResultStatus("SUCCESS");
              print "TEST STEP : To set the operating channel bandwidth to Auto"
              print "EXPECTED RESULT : To successfully set the channel bandwidth to Auto"
              print "ACTUAL RESULT : %s " %details
              #Get the result of execution
              print "[TEST EXECUTION RESULT] : SUCCESS";

              expectedresult = "SUCCESS";
              radioIndex = idx
              getMethod = "getChannelBandwidth"
              primitive = 'WIFIHAL_GetOrSetParamStringValue'

              #Calling the method to execute wifi_getRadioOperatingChannelBandwidth()
              tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
              bandWidth = details.split(":")[1].strip()

              bandWidthList = ['20MHz','40MHz','80MHz','160MHz','Auto'];
              if expectedresult in actualresult and bandWidth in bandWidthList:
                 #Set the result status of execution
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "TEST STEP : To get the operating channel bandwidth as a value from the list %s"%bandWidthList
                 print "EXPECTED RESULT : To successfully get the channel bandwidth as a value from the list %s"%bandWidthList
                 print "ACTUAL RESULT : %s " %details
                 #Get the result of execution
                 print "[TEST EXECUTION RESULT] : SUCCESS";

                 expectedresult = "SUCCESS";
                 radioIndex = idx
                 getMethod = "getRadioExtChannel"
                 primitive = 'WIFIHAL_GetOrSetParamStringValue'

                 #Calling the method to execute wifi_getRadioExtChannel()
                 tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)

                 possibleExtChannels = ['AboveControlChannel', 'BelowControlChannel', 'Auto']
                 initGetExtCh = details.split(":")[1].strip()

                 if expectedresult in actualresult and initGetExtCh in possibleExtChannels and len(initGetExtCh) <= 64:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP : Get the Radio Extension Channel";
                    print "EXPECTED RESULT : wifi_getRadioExtChannel should return a string value either AboveControlChannel or BelowControlChannel or Auto";
                    print "ACTUAL RESULT : Ext Channel value string received: %s"%initGetExtCh;
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    for setExtCh in possibleExtChannels:
                        if initGetExtCh == setExtCh:
                            continue;
                        else:
                            expectedresult = "SUCCESS";
                            radioIndex = idx
                            setMethod = "setRadioExtChannel"
                            primitive = 'WIFIHAL_GetOrSetParamStringValue'

                            #Calling the method to execute wifi_setRadioExtChannel()
                            tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, setExtCh, setMethod)

                            if expectedresult in actualresult:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP : To set the radio extension channel as %s " %setExtCh;
                                print "EXPECTED RESULT : Setting the radio extension channel returns SUCCESS"
                                print "ACTUAL RESULT : %s " %details
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : SUCCESS";

                                expectedresult = "SUCCESS";
                                radioIndex = idx
                                setMethod = "getRadioExtChannel"
                                primitive = 'WIFIHAL_GetOrSetParamStringValue'

                                #Calling the method to execute wifi_getRadioExtChannel()
                                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, "0", getMethod)
                                getExtCh = details.split(":")[1].strip()

                                if expectedresult in actualresult and getExtCh == setExtCh:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "TEST STEP : To get the radio extension channel as %s " %setExtCh;
                                    print "EXPECTED RESULT : Get radio extension channel returns %s" %setExtCh;
                                    print "ACTUAL RESULT : %s " %details
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

                                else:
                                    #Set the result status of execution
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "TEST STEP : To get the radio extension channel as %s " %setExtCh;
                                    print "EXPECTED RESULT : Get radio extension channel returns %s" %setExtCh;
                                    print "ACTUAL RESULT : %s " %details
                                    #Get the result of execution
                                    print "[TEST EXECUTION RESULT] : FAILURE";

                                #Reverting the extension channel
                                expectedresult = "SUCCESS";
                                radioIndex = idx
                                setMethod = "setRadioExtChannel"
                                primitive = 'WIFIHAL_GetOrSetParamStringValue'

                                #Calling the method to execute wifi_setRadioExtChannel()
                                tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, initGetExtCh, setMethod)

                                if expectedresult in actualresult:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "Extension channel is successfully reverted to initial value"

                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "Unable to revert the extension channel to initial value"

                            else:
                                #Set the result status of execution
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP : To set the radio extension channel as %s " %setExtCh;
                                print "EXPECTED RESULT : Setting the radio extension channel returns SUCCESS"
                                print "ACTUAL RESULT : %s " %details
                                #Get the result of execution
                                print "[TEST EXECUTION RESULT] : FAILURE";
                        break;
                 else:
                     tdkTestObj.setResultStatus("FAILURE");
                     print "TEST STEP : Checking if %s is a possible radio extension channel" %initGetExtCh;
                     print "EXPECTED RESULT : wifi_getRadioExtChannel should return a string value either AboveControlChannel or BelowControlChannel or Auto";
                     print "ACTUAL RESULT : Failed to get an extension channel from the possible channel list";
                     print "Ext Channel value string received: %s"%initGetExtCh;
                     print "[TEST EXECUTION RESULT] : FAILURE";
              else:
                  #Set the result status of execution
                  tdkTestObj.setResultStatus("FAILURE");
                  print "TEST STEP : To get the operating channel bandwidth as a value from the list %s"%bandWidthList
                  print "EXPECTED RESULT : To successfully get the channel bandwidth as a value from the list %s"%bandWidthList
                  print "ACTUAL RESULT : %s " %details
                  #Get the result of execution
                  print "[TEST EXECUTION RESULT] : FAILURE";

              #Reverting the channel bandwidth
              expectedresult="SUCCESS";
              radioIndex = idx
              setMethod = "setChannelBandwidth"
              primitive = 'WIFIHAL_GetOrSetParamStringValue'

              #Calling the method to execute wifi_setRadioOperatingChannelBandwidth()
              tdkTestObj, actualresult, details = ExecuteWIFIHalCallMethod(obj, primitive, radioIndex, initBandwidth, setMethod)

              if expectedresult in actualresult:
                 tdkTestObj.setResultStatus("SUCCESS");
                 print "Radio Operating Channel Bandwidth is successfully reverted to initial value"
              else:
                  tdkTestObj.setResultStatus("FAILURE");
                  print "Unable to revert the Radio Opertaing Channel Bandwidth to initial value"

           else:
               #Set the result status of execution
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP : To set the operating channel bandwidth to Auto"
               print "EXPECTED RESULT : To successfully set the channel bandwidth to Auto"
               print "ACTUAL RESULT : %s " %details
               #Get the result of execution
               print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP : To get the initial operating channel bandwidth"
            print "EXPECTED RESULT : To successfully get the initial channel bandwidth"
            print "ACTUAL RESULT : %s " %details
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifihal");

else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
