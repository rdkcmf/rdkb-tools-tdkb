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
  <name>TS_TAD_CheckARPTable_LanIP</name>
  <primitive_test_id/>
  <primitive_test_name>TADstub_Get</primitive_test_name>
  <primitive_test_version>3</primitive_test_version>
  <status>FREE</status>
  <synopsis>Connect one lan client and check whether the lan client ip is updated in Device.IP.Diagnostics.X_CISCO_COM_ARP. table  or not.</synopsis>
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
    <test_case_id>TC_TAD_68</test_case_id>
    <test_objective>Connect one lan client and check whether the lan client ip is updated in Device.IP.Diagnostics.X_CISCO_COM_ARP. table  or not.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband,Emulator,RPI</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state else invoke cosa_start.sh manually that includes all the ccsp components.
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
3. Make sure LAN client is connected before running the script</pre_requisite>
    <api_or_interface_used>TADstub_Get</api_or_interface_used>
    <input_parameters>Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTableNumberOfEntries
Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTable.%d.IPAddress
Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTable.%d.MACAddress
Device.IP.Diagnostics.X_CISCO_COM_ARP.ARPTable.%d.Static</input_parameters>
    <automation_approch>1. Load TAD modules
2. From script invoke TADstub_Get to get the ARPTableNumberOfEntries
3. Get the details of each entry
4. Get the entry for LAN client from arp -a command
5. Validate the enry details with the details obtained from arp -a command
6.Unload module</automation_approch>
    <except_output>The LAN client entry should be there in ARP table as well as in arp -a command</except_output>
    <priority>High</priority>
    <test_stub_interface>TAD</test_stub_interface>
    <test_script>TS_TAD_CheckARPTable_LanIP</test_script>
    <skipped>No</skipped>
    <release_version>M64</release_version>
    <remarks>LAN</remarks>
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
obj.configureTestCase(ip,port,'TS_TAD_CheckARPTable_LanIP');
sysobj.configureTestCase(ip,port,'TS_TAD_CheckARPTable_LanIP');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
sysloadmodulestatus =sysobj.getLoadModuleResult();
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
		    obj.unloadModule("tad");
		    sysobj.unloadModule("sysutil");
		    exit()

		#Append all values to a list
		value = orgValue[0] + "|" + orgValue[1] + "|" + orgValue[2];
		ARPdetails.append(value);

	    print "The details retrieved from the ARP table is: %s" %ARPdetails;

	    #Get the ARP table details from 'arp -a' command
	    if ARPdetails:
  		commandDetails = [];
		brlan0Command = "arp -a | grep brlan0 | wc -l"
		tdkTestObj = sysobj.createTestStep('ExecuteCmd');
		tdkTestObj.addParameter("command", brlan0Command);
		tdkTestObj.executeTestCase(expectedresult);
		actualresult = tdkTestObj.getResult();
		numberofBrlan0 = tdkTestObj.getResultDetails().strip().replace("\\n", "");
		if int(numberofBrlan0) >0 :
		    for i in range(1,int(numberofBrlan0)+1):
	                arpCommand = "arp -a | grep brlan0| sed -n '"+ `i` +"p'"
		        tdkTestObj = sysobj.createTestStep('ExecuteCmd');
		        tdkTestObj.addParameter("command", arpCommand);
	                tdkTestObj.executeTestCase(expectedresult);
	                actualresult = tdkTestObj.getResult();
	                arpOutput = tdkTestObj.getResultDetails().strip();
		        ipaddress = arpOutput.split(" at ")[0].split(" ")[1].replace("(","").replace(")","")
		        macaddress = arpOutput.split(" at ")[1].split(" ")[0]
		        if "PERM" in arpOutput :
		    	    isstatic = "true";
		        else:
		    	    isstatic = "false"
		        #Append the values to a list
		        cmdvalue = ipaddress + "|" + macaddress + "|" + isstatic
		        commandDetails.append(cmdvalue)
		    print "The details retrieved from the arp -a command is: %s" %commandDetails;
		    #Check if the brlan0 entry is in ARP table
		    if set(ARPdetails).intersection(set(commandDetails)) == set(commandDetails):
			tdkTestObj.setResultStatus("SUCCESS");
			print "All brlan0 entries in arp-a command are available in ARP table also"
		    else:
			tdkTestObj.setResultStatus("FAILURE");
			print "All brlan0 entries in arp-a command are not available in ARP table"
		else:
		    tdkTestObj.setResultStatus("FAILURE");
		    print "FAILED:No entries for brlan0 in arp -a command"
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
