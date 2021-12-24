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
  <version>9</version>
  <name>TS_SNMP_GetErouterOperationalStatus</name>
  <primitive_test_id/>
  <primitive_test_name>GetCommString</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>Check if the erouter operational status fetched using the OID 1.3.6.1.2.1.2.2.1.8.1 is same as the operational status stored in the device erouter status file.</synopsis>
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
    <test_case_id>TC_SNMP_43</test_case_id>
    <test_objective>Check if the erouter operational status fetched using the OID 1.3.6.1.2.1.2.2.1.8.1 is same as the operational status stored in the device erouter status file.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>SnmpMethod : snmpget
SnmpVersion : v2c
OID : 1.3.6.1.2.1.2.2.1.2.1
OID : 1.3.6.1.2.1.2.2.1.8.1</input_parameters>
    <automation_approch>1. Load the modules
2. Get the erouter details using the snmpget command with the OID 1.3.6.1.2.1.2.2.1.2.1.
3. If the erouter details obtained indicate "eRouter Embedded Interface" get the erouter operational status using the snmpget command with the OID 1.3.6.1.2.1.2.2.1.8.1. The status will be either "up" or "down".
4. Get the erouter operational status file location from the platform property file and check if the required file exists in that location.
5. Check if the operational status retrieved from the file is same as the operational status retrieved from the OID.
6. Unload the modules</automation_approch>
    <expected_output>The erouter operational status fetched using the OID 1.3.6.1.2.1.2.2.1.8.1 should be the same as the operational status stored in the device erouter status file.</expected_output>
    <priority>High</priority>
    <test_stub_interface>snmp</test_stub_interface>
    <test_script>TS_SNMP_GetErouterOperationalStatus</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
import snmplib;
from tdkbVariables import *

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_SNMP_GetErouterOperationalStatus');

#Get the result of connection with test component and DUT
loadmodulestatus1 =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

if "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult = "SUCCESS";
    #Get the Community String
    communityString = snmplib.getCommunityString(obj,"snmpget");
    #Get the IP Address
    ipaddress = snmplib.getIPAddress(obj);

    #Get the erouter interface details
    actResponse =snmplib.SnmpExecuteCmd("snmpget", communityString, "-v 2c", "1.3.6.1.2.1.2.2.1.2.1", ipaddress);
    tdkTestObj = obj.createTestStep('ExecuteCmd');
    tdkTestObj.executeTestCase("SUCCESS");

    print "\nTEST STEP 1 : Get the erouter0 interface details";
    print "EXPECTED RESULT 1 : Should get the erouter0 interface details successfully"

    if "eRouter Embedded Interface" in actResponse:
        erouter_details = actResponse.split("STRING:")[1].strip()
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: erouter0 details obtained as : %s" %erouter_details;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS" ;

        #Get the erouter operational status
        actResponse =snmplib.SnmpExecuteCmd("snmpget", communityString, "-v 2c", "1.3.6.1.2.1.2.2.1.8.1", ipaddress);
        tdkTestObj = obj.createTestStep('ExecuteCmd');
        tdkTestObj.executeTestCase("SUCCESS");

        print "\nTEST STEP 2 : Get the erouter operational status";
        print "EXPECTED RESULT 2 : Should get the erouter operational status successfully"

        if "up" in actResponse or "down" in actResponse:
            erouter_operationalStatus = actResponse.strip().replace("\\n", "").split("INTEGER: ")[1].split("(")[0];
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT 2: erouter operational status obtained as : %s" %erouter_operationalStatus;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS" ;

            #Get the atom side erouter file location from platform properties
            tdkTestObj = obj.createTestStep('ExecuteCmd');
            cmd = "sh %s/tdk_utility.sh parseConfigFile EROUTER_OPERATIONAL_STATUS_FILE" %TDK_PATH;
            print "\nCommand : ", cmd;
            tdkTestObj.addParameter("command", cmd);
            tdkTestObj.executeTestCase(expectedresult);
            actualresult = tdkTestObj.getResult();
            file = tdkTestObj.getResultDetails().strip().replace("\\n", "");

            print "TEST STEP 3: Get the erouter operational status file location from platform property file";
            print "EXPECTED RESULT 3: Should successfully get the erouter operational status file location from platform property file";

            if expectedresult in actualresult and file != "":
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 3: File location: %s" %file;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Check if the erouter operational status file exists in the given location
                cmd = "[ -f " + file + " ] && echo \"File exist\" || echo \"File does not exist\"";
                print "\nCommand : ", cmd;
                tdkTestObj.addParameter("command",cmd);
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                print "\nTEST STEP 4: Check for %s file presence" %(file);
                print "EXPECTED RESULT 4: %s file should be present" %(file);

                if expectedresult in actualresult and details == "File exist":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: %s file is present" %(file);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Get the erouter operational status from file
                    cmd = "cat " + file;
                    print "\nCommand : ", cmd;
                    tdkTestObj.addParameter("command",cmd);
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                    print "TEST STEP 5: Get the erouter operational status from %s" %(file);
                    print "EXPECTED RESULT 5: Should get the erouter operational from %s successfully" %(file);

                    if expectedresult in actualresult and details != "":
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT 5: The erouter operational status from file is : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Check if the operational status is same in both cases
                        operStatus = details.strip();
                        print "\nTEST STEP 6 : Check if the erouter operational status from SNMP OID is same as the status from device file";
                        print "EXPECTED RESULT 6 : The erouter operational status from SNMP OID should be same as the status from device file"
                        print "Erouter Operational status from SNMP OID : %s" %erouter_operationalStatus;
                        print "Erouter Operational status from %s : %s" %(file, operStatus);

                        if operStatus == erouter_operationalStatus:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT 6: Both values are the same";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : SUCCESS";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "ACTUAL RESULT 6: Both values are not the same";
                            #Get the result of execution
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT 5: The erouter operational status from file is : %s" %details;
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: %s file is not present" %(file);
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 3: File location not obtained from platform property file";
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT 2: erouter operational status obtained as : %s" %actResponse;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : FAILURE" ;
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: erouter details obtained as : %s" %actResponse;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE" ;

    obj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
