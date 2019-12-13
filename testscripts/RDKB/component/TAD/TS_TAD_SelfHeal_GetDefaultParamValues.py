##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2019 RDK Management
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
  <version>1</version>
  <name>TS_TAD_SelfHeal_GetDefaultParamValues</name>
  <primitive_test_id/>
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if all the selfheal parameters have default values after factory reset.</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_TAD_72</test_case_id>
    <test_objective>Check if all the selfheal parameters have default values after factory reset.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Get</api_or_interface_used>
    <input_parameters>"Device.SelfHeal.X_RDKCENTRAL-COM_MaxRebootCount","Device.SelfHeal.X_RDKCENTRAL-COM_MaxResetCount","Device.SelfHeal.ConnectivityTest.X_RDKCENTRAL-COM_PingInterval","Device.SelfHeal.ConnectivityTest.X_RDKCENTRAL-COM_NumPingsPerServer","Device.SelfHeal.ConnectivityTest.X_RDKCENTRAL-COM_MinNumPingServer","Device.SelfHeal.ConnectivityTest.X_RDKCENTRAL-COM_PingRespWaitTime","Device.SelfHeal.ConnectivityTest.X_RDKCENTRAL-COM_CorrectiveAction","Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTableNumberOfEntries","Device.SelfHeal.ConnectivityTest.PingServerList.IPv6PingServerTableNumberOfEntries","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgCPUThreshold","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold"</input_parameters>
    <automation_approch>1. Load TAD modules
2. Get and save the default values from platform property file
3. Initiate factory reset to obtain the default values of all parameters
5. Check if the values of each param is default value by comparing the values from tdk_platform.properties
6.Unload module</automation_approch>
    <except_output>All params should contain the default values after factory reset</except_output>
    <priority>High</priority>
    <test_stub_interface>TAD</test_stub_interface>
    <test_script>TS_TAD_SelfHeal_GetDefaultParamValues</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from tdkbVariables import *;
import tdkutility
from tdkutility import *
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
pamobj = tdklib.TDKScriptingLibrary("pam","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_SelfHeal_CheckDefaultStatus');
pamobj.configureTestCase(ip,port,'TS_TAD_SelfHeal_CheckDefaultStatus');
sysobj.configureTestCase(ip,port,'TS_TAD_SelfHeal_CheckDefaultStatus');
#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
pamloadmodulestatus =pamobj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %pamloadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;
if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in pamloadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    pamobj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    #save device's current state before it goes for reboot
    obj.saveCurrentState();
    #Initiate Factory reset before checking the default value
    tdkTestObj = pamobj.createTestStep('pam_Setparams');
    tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
    tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
    tdkTestObj.addParameter("Type","string");
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    if expectedresult in actualresult:
       #Set the result status of execution
       tdkTestObj.setResultStatus("SUCCESS");
       print "TEST STEP 1: Initiate factory reset ";
       print "EXPECTED RESULT 1: Should inititate factory reset";
       print "ACTUAL RESULT 1: %s" %details;
       #Get the result of execution
       print "[TEST EXECUTION RESULT] : SUCCESS";
       #Restore the device state saved before reboot
       obj.restorePreviousStateAfterReboot();

       tdkTestObj = sysobj.createTestStep('ExecuteCmd');
       expectedresult="SUCCESS";
       defaults= "sh %s/tdk_utility.sh parseConfigFile DEFAULT_SELFHEAL_VALUES" %TDK_PATH;
       print defaults;
       expectedresult="SUCCESS";
       tdkTestObj.addParameter("command", defaults);
       tdkTestObj.executeTestCase(expectedresult);
       actualresult = tdkTestObj.getResult();
       defaultValues = tdkTestObj.getResultDetails().strip().replace("\\n", "");
       if expectedresult in actualresult and defaultValues!= "":
          tdkTestObj.setResultStatus("SUCCESS");
          print "TEST STEP: Should get the default self heal parameter values from properties file"
          print "ACTUAL RESULT :Default self heal parameter values from properties file:%s" %defaultValues;
          #Get the result of execution
          print "[TEST EXECUTION RESULT] : SUCCESS";
          defaultValues= defaultValues.split(",");

          #Check the default status of selfheal
          paramList = ["Device.SelfHeal.X_RDKCENTRAL-COM_MaxRebootCount","Device.SelfHeal.X_RDKCENTRAL-COM_MaxResetCount","Device.SelfHeal.ConnectivityTest.X_RDKCENTRAL-COM_PingInterval","Device.SelfHeal.ConnectivityTest.X_RDKCENTRAL-COM_NumPingsPerServer","Device.SelfHeal.ConnectivityTest.X_RDKCENTRAL-COM_MinNumPingServer","Device.SelfHeal.ConnectivityTest.X_RDKCENTRAL-COM_PingRespWaitTime","Device.SelfHeal.ConnectivityTest.X_RDKCENTRAL-COM_CorrectiveAction","Device.SelfHeal.ConnectivityTest.PingServerList.IPv4PingServerTableNumberOfEntries","Device.SelfHeal.ConnectivityTest.PingServerList.IPv6PingServerTableNumberOfEntries","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_UsageComputeWindow","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgCPUThreshold","Device.SelfHeal.ResourceMonitor.X_RDKCENTRAL-COM_AvgMemoryThreshold"]
          tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)
          if expectedresult in status:
             tdkTestObj.setResultStatus("SUCCESS");
             print "TEST STEP 3: Get the values of each selfheal param"
             print "EXPECTED RESULT 3: Should get the values of each selfheal param"
             print "ACTUAL RESULT 3: values of each selfheal param :%s" %orgValue
             print "[TEST EXECUTION RESULT] : SUCCESS";
             #Check if the retrieved selfheal params have the default values or not
             for i in range(0,12):
                 if orgValue[i] == defaultValues[i]:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print orgValue[i],defaultValues[i]
                    print "Step %d :The param %s has the default value of %s" %(i+1,paramList[i],orgValue[i]);
                 else:
                      tdkTestObj.setResultStatus("FAILURE");
                      print orgValue[i],defaultValues[i]
                      print "Step %d :The param %s is not having the default value of %s" %(i+1,paramList[i],orgValue[i]);
                      break;
          else:
               tdkTestObj.setResultStatus("FAILURE");
               print "TEST STEP 3: Get the values of each selfheal param"
               print "EXPECTED RESULT 3: Should get the values of each selfheal param"
               print "ACTUAL RESULT 3: values of each selfheal param :%s" %orgValue
               print "[TEST EXECUTION RESULT] : FAILURE";
       else:
           tdkTestObj.setResultStatus("FAILURE");
           print "TEST STEP : Should get the default self heal parameter values from properties file"
           print "ACTUAL RESULT :Default self heal parameter values from properties file:%s" %defaultValues;
           #Get the result of execution
           print "[TEST EXECUTION RESULT] :FAILURE";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Initiate factory reset ";
        print "EXPECTED RESULT 1: Should inititate factory reset";
        print "ACTUAL RESULT 1: %s" %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tad");
    pamobj.unloadModule("pam");
    obj.unloadModule("sysutil");

else:
        print "Failed to load tad module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";



