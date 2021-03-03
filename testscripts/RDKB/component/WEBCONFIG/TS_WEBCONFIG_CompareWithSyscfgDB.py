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
<?xml version='1.0' encoding='utf-8'?>
<xml>
  <id></id>
  <!-- Do not edit id. This will be auto filled while exporting. If you are adding a new script keep the id empty -->
  <version>2</version>
  <!-- Do not edit version. This will be auto incremented while updating. If you are adding a new script you can keep the vresion as 1 -->
  <name>TS_WEBCONFIG_CompareWithSyscfgDB</name>
  <!-- If you are adding a new script you can specify the script name. Script Name should be unique same as this file name with out .py extension -->
  <primitive_test_id></primitive_test_id>
  <!-- Do not change primitive_test_id if you are editing an existing script. -->
  <primitive_test_name>Webconfig_DoNothing</primitive_test_name>
  <!--  -->
  <primitive_test_version>1</primitive_test_version>
  <!--  -->
  <status>FREE</status>
  <!--  -->
  <synopsis>To check if the Webconfig parameters from Tr-181 and the value configured in syscfg.db are equal</synopsis>
  <!--  -->
  <groups_id />
  <!--  -->
  <execution_time>10</execution_time>
  <!--  -->
  <long_duration>false</long_duration>
  <!--  -->
  <advanced_script>false</advanced_script>
  <!-- execution_time is the time out time for test execution -->
  <remarks></remarks>
  <!-- Reason for skipping the tests if marked to skip -->
  <skip>false</skip>
  <!--  -->
  <box_types>
    <box_type>Broadband</box_type>
    <!--  -->
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
    <!--  -->
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WEBCONFIG_07</test_case_id>
    <test_objective>This test case is to check if the Webconfig parameters from Tr-181 and the value configured in syscfg.db are equal</test_objective>
    <test_type>Positive</test_type>
    <test_setup>BroadBand</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3.Webconfig distro should be enabled else enable with custom image</pre_requisite>
    <api_or_interface_used>TDKB_TR181Stub_Get</api_or_interface_used>
    <input_parameters>Device.X_RDK_WebConfig.ConfigFile.1.URL
Device.X_RDK_WebConfig.RfcEnable
Device.X_RDK_WebConfig.ConfigFileNumberOfEntries
Device.X_RDK_WebConfig.ConfigFile.1.SyncCheckOK</input_parameters>
    <automation_approch>1.Load the module
2.Get the WebConfig parameters value via Tr181 query
3.Get the WebConfig parameters value configured in syscfg.db and the values are expected to be equal
4.Unload the module
</automation_approch>
    <expected_output>The values configured in syscf.db and the values received via Tr181 query are expected to be equal</expected_output>
    <priority>High</priority>
    <test_stub_interface>WEBCONFIG</test_stub_interface>
    <test_script>TS_WEBCONFIG_CompareWithSyscfgDB</test_script>
    <skipped>No</skipped>
    <release_version>M86</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags />
</xml>
'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tdkbtr181","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WEBCONFIG_CompareWithSyscfgDB');
sysobj.configureTestCase(ip,port,'TS_WEBCONFIG_CompareWithSyscfgDB');

#Get the result of connection with test component and DUT
loadmodulestatus=obj.getLoadModuleResult();
loadmodulestatus1=sysobj.getLoadModuleResult();

def Validate(dbVariables,parameters):
    statusflag=0;
    index =0;
    expectedresult ="SUCCESS";
    for item in parameters:
        tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Get");
        tdkTestObj.addParameter("ParamName",item);
        tdkTestObj.executeTestCase(expectedresult);
        actualresult = tdkTestObj.getResult();
        details  = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            print "%s value is %s" %(item,details);
            tdkTestObj = sysobj.createTestStep("ExecuteCmd");
            cmd = "syscfg get %s" %dbVariables[index];
            print cmd;
            tdkTestObj.addParameter("command", cmd);
            expectedresult="SUCCESS"
            tdkTestObj.executeTestCase(expectedresult);
            actualresult=tdkTestObj.getResult();
            dbValue = tdkTestObj.getResultDetails().replace("\\n", "");
            if expectedresult in actualresult :
                print "****Checking if the value in syscfg.db and Tr181 are equal****";
                if dbValue == details:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "value in syscfg.db is %s and via tr181 is %s" %(dbValue,details);
                    print "TEST EXECUTION RESULT :SUCCESS"
                    print "\n";
                else:
                    statusflag =1;
                    tdkTestObj.setResultStatus("FAILURE");
                    print "value in syscfg.db is %s and via tr181 is %s" %(dbValue,details);
                    print "TEST EXECUTION RESULT :FAILURE";
                    print "\n";
        else:
            statusflag =1;
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "%s query failed" %item;
        index=index+1;
    return statusflag;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    tdkTestObj = obj.createTestStep("TDKB_TR181Stub_Get");
    tdkTestObj.addParameter("ParamName","Device.X_RDK_WebConfig.ConfigFileNumberOfEntries");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    noOfEntries  = tdkTestObj.getResultDetails();
    if expectedresult in actualresult and  int(noOfEntries) > 0:
         noOfEntries = int(noOfEntries);
         tdkTestObj.setResultStatus("SUCCESS");
         print "TEST STEP 1: Get the Config file number of entries";
         print "EXPECTED RESULT 1: Should get the Config file number of entries";
         print "ACTUAL RESULT 1: Config file number of entries is : %s" %noOfEntries;
         #Get the result of execution
         print "[TEST EXECUTION RESULT] : SUCCESS";

         statusflag = 0;
         dbVariables = ["WebConfigRfcEnabled","ConfigFileNumberOfEntries"];
         parameters = ["Device.X_RDK_WebConfig.RfcEnable","Device.X_RDK_WebConfig.ConfigFileNumberOfEntries"];
         #Calling function to Validate
         statusflag = Validate(dbVariables,parameters);
         #In case there are more than one instance number
         while noOfEntries > 0:
               configfile_Url = "configfile_"+str(noOfEntries)+"_Url";
               configfile_SyncCheckOk = "configfile_"+str(noOfEntries)+"_SyncCheckOk";
               tr181configfile_Url = "Device.X_RDK_WebConfig.ConfigFile."+str(noOfEntries)+".URL";
               tr181configfile_SyncCheckOk = "Device.X_RDK_WebConfig.ConfigFile."+str(noOfEntries)+".SyncCheckOK"

               dbVariables = [configfile_Url,configfile_SyncCheckOk];
               parameters = [tr181configfile_Url,tr181configfile_SyncCheckOk];
               statusflag = Validate(dbVariables,parameters);
               noOfEntries = noOfEntries -1 ;
    else:
         noOfEntries = int(noOfEntries);
         tdkTestObj.setResultStatus("FAILURE");
         print "TEST STEP 1: Get the Config file number of entries";
         print "EXPECTED RESULT 1: Should get the Config file number of entries";
         print "ACTUAL RESULT 1: Config file number of entries is : %s" %noOfEntries;
         #Get the result of execution
         print "[TEST EXECUTION RESULT] : FAILURE";
    # setting the script status as FAILURE in case any condition in the loop was failed
    if statusflag == 1:
       tdkTestObj.setResultStatus("FAILURE");
    obj.unloadModule("tdkbtr181");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    obj1.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
