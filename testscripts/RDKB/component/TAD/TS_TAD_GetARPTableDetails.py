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
  <name>TS_TAD_GetARPTableDetails</name>
  <primitive_test_id/>
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>To get the contents from Device.IP.Diagnostics.X_CISCO_COM_ARP. table and validate them with the ip neigh command output.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
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
    <test_case_id>TC_TAD_67</test_case_id>
    <test_objective>To get the contents from Device.IP.Diagnostics.X_CISCO_COM_ARP. table and validate them with the ip neigh command output.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>TADstub_Get</api_or_interface_used>
    <input_parameters>Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTableNumberOfEntries
Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTable.%d.IPAddress
Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTable.%d.MACAddress
Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTable.%d.Static</input_parameters>
    <automation_approch>1. Load TAD modules
2. From script invoke TADstub_Get to get the ARPTableNumberOfEntries
3. Get the details of each entry
4. Validate the enry details with the details obtained from ip neigh command
5.Unload module</automation_approch>
    <except_output>The details in ARP table and ip neigh command should be same</except_output>
    <priority>High</priority>
    <test_stub_interface>TAD</test_stub_interface>
    <test_script>TS_TAD_GetARPTableDetails</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>None</remarks>
  </test_cases>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import tdkutility
from tdkutility import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("tad","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_TAD_GetARPTableDetails');
sysobj.configureTestCase(ip,port,'TS_TAD_GetARPTableDetails');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus = sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %sysloadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in sysloadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    tdkTestObj = obj.createTestStep('TADstub_Get');
    tdkTestObj.addParameter("paramName","Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTableNumberOfEntries");
    expectedresult="SUCCESS";

    #Execute the test case in STB
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    numberofEntries = tdkTestObj.getResultDetails();

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the number of entries in ARP table";
        print "EXPECTED RESULT 1: Should get the number of entries in ARP table";
        print "ACTUAL RESULT 1: The number of entries in ARP table is %s" %numberofEntries;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        if int(numberofEntries) > 0:
            ARPdetails = [];
            for i in range(1,int(numberofEntries)+1):
                #Get the ARP table entries and store them in a list
                ipAddressParam = "Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTable.%d.IPAddress" %i
                macAddressParam = "Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTable.%d.MACAddress" %i
                isStaticParam = "Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTable.%d.Static" %i
                paramList = [ipAddressParam,macAddressParam,isStaticParam]
                tdkTestObj,status,orgValue = getMultipleParameterValues(obj,paramList)
                if expectedresult in status:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP %d: Get the ipaddress, macaddress and type of ARP table entry %d" %(i,i)
                    print "EXPECTED RESULT %d: Should retrieve the ipaddress, macaddress and type of ARP table entry %d" %(i,i)
                    print "ACTUAL RESULT %d: %s" %(i,orgValue);
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP %d: Get the ipaddress, macaddress and type of ARP table entry %d" %(i,i)
                    print "EXPECTED RESULT %d: Should retrieve the ipaddress, macaddress and type of ARP table entry %d" %(i,i)
                    print "ACTUAL RESULT %d: %s" %(i,orgValue);
                    print "[TEST EXECUTION RESULT] : FAILURE";
                    break;

                #Append all values to a list
                value = orgValue[0] + "|" + orgValue[1] + "|" + orgValue[2];
                ARPdetails.append(value);

            print "The details retrieved from the ARP table is: %s" %ARPdetails;

            #Get the ARP table details from 'ip neigh' command
            if ARPdetails:
                commandDetails = [];
                brlan0Command = "ip neigh show | wc -l"
                tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                tdkTestObj.addParameter("command", brlan0Command);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                numberofBrlan0 = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if int(numberofBrlan0) >0 :
                    for i in range(1,int(numberofBrlan0)+1):
                        arpCommand = "ip neigh show | sed -n '"+ `i` +"p'"
                        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                        tdkTestObj.addParameter("command", arpCommand);
                        tdkTestObj.executeTestCase(expectedresult);
                        actualresult = tdkTestObj.getResult();
                        arpOutput = tdkTestObj.getResultDetails().strip();
                        ipaddress = arpOutput.split(" ")[0]
                        macaddress = arpOutput.split(" ")[4]
                        if "PERMANENT" in arpOutput :
                            isstatic = "true";
                        else:
                            isstatic = "false"
                        #Append the values to a list
                        cmdvalue = ipaddress + "|" + macaddress + "|" + isstatic
                        commandDetails.append(cmdvalue)
                    print "The details retrieved from the ip neigh command is: %s" %commandDetails;
                    #Check if both lists are same or not
                    if commandDetails:
                        if list(set(ARPdetails) - set(commandDetails)) == []:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP : Check if the entries in ARP table and ip neigh command are same";
                            print "EXPECTED RESULT : Should get the entries in ARP table and ip neigh command as same";
                            print "ACTUAL RESULT : SUCCESS";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP : Check if the entries in ARP table and ip neigh command are same";
                            print "EXPECTED RESULT : Should get the entries in ARP table and ip neigh command as same";
                            print "ACTUAL RESULT : FAILURE";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "Failed to get the entries from ip neigh command"
                        print "List generated from ip neigh command is :%s" %commandDetails
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Failed to get the number of entries in ip neigh command"
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Failed to get the entries from ARP table"
                print "List generated from ARP table is :%s" %ARPdetails
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: The number of entries in ARP table is zero";
            print "EXPECTED RESULT 2: Should get the number of entries in ARP table as greater than zero";
            print "ACTUAL RESULT 2: The number of entries in ARP table %s" %numberofEntries;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the number of entries in ARP table";
        print "EXPECTED RESULT 1: Should get the number of entries in ARP table";
        print "ACTUAL RESULT 1: The number of entries in ARP table is %s" %numberofEntries;
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("tad");
    sysobj.unloadModule("sysutil");

else:
        print "Failed to load tad module";
        obj.setLoadModuleStatus("FAILURE");
        print "Module loading failed";
