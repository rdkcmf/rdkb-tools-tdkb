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
  <version>6</version>
  <name>TS_WIFIAGENT_5GHzSetManagementFramePowerControl_OutOfRange</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To check if the set operation of Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl is success for values out of the acceptable range -20db to 0db and if the value converts to 0db when values greater than 0db is set and to -20db when values less than -20db is set.</synopsis>
  <groups_id/>
  <execution_time>10</execution_time>
  <long_duration>false</long_duration>
  <advanced_script>false</advanced_script>
  <remarks/>
  <skip>false</skip>
  <box_types>
    <box_type>Broadband</box_type>
    <box_type>RPI</box_type>
  </box_types>
  <rdk_versions>
    <rdk_version>RDKB</rdk_version>
  </rdk_versions>
  <test_cases>
    <test_case_id>TC_WIFIAGENT_214</test_case_id>
    <test_objective>To check if the set operation of Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl is success for values out of the acceptable range -20db to 0db and if the value converts to 0db when values greater than 0db is set and to -20db when values less than -20db is set.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband, RPI</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl
paramValue : integer values beyond the applicable range of -20db to 0db
paramType : int</input_parameters>
    <automation_approch>1. Load the module
2. Get the initial value of Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl.
3. Check if the initial MFPC is in the range of -20db to 0db.
4. Set Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl to a list of values greater than 0db : ["1", "10", "23", "50", "100", "257", "1000"]. The SET operations are expected to return success.
5. After each set get the value of Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl and check if it is converted to 0db.
6. Set Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl to a list of values lesser than -20db : ["-21", "-30", "-53", "-80", "-100", "-257", "-1000"]. The SET operations are expected to return success.
7. After each set get the value of Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl and check if it is converted to -20db.
8. Revert Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl to the initial value if required.
9. Unload the module</automation_approch>
    <expected_output>Setting Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl to values beyond the MFPC range of -20db to 0db should return success and the get operation should return 0db and -20db when the set values are greater than 0db and lesser than -20db respectively.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_5GHzSetManagementFramePowerControl_OutOfRange</test_script>
    <skipped>No</skipped>
    <release_version>M104</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# tdklib library,which provides a wrapper for tdk testcase script
import tdklib;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WIFIAGENT_5GHzSetManagementFramePowerControl_OutOfRange');

#Get the result of connection with test component and DUT
loadmodulestatus = obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Get the initial MFPC value
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl");
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP 1: Get the initial ManagementFrame PowerControl value using Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl";
    print "EXPECTED RESULT 1: Should get the initial ManagementFrame PowerControl value successfully";

    if expectedresult in actualresult and details != "":
        initial_mfpc = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT 1: ManagementFrame PowerControl :%s" %initial_mfpc;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Check if the initial value is in the range -20 to 0 db
        if initial_mfpc.strip("-").isdigit() and int(initial_mfpc) <= 0 and int(initial_mfpc) >= -20:
            curr_mfpc = initial_mfpc;
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "The initial MFPC is in the acceptable range of -20db to 0db";

            #Set MFPC to values > 0db and check if the get value is the upper limit 0db
            flag = 0;
            upper_bound = "0";
            #All MFPC values set above the upper limit of 0db should be converted to 0db
            upper_OutofBound = ["1", "10", "23", "50", "100", "257", "1000"];

            print "\nTEST STEP 2: Set Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl to values > 0db and check if the get operation gives the value 0db";
            print "EXPECTED RESULT 2: The set operation should be success and the get operation should give 0db as all values > 0db should be converted to the upper limit 0db";

            for mfpc in upper_OutofBound:
                print "\n-----For Management Frame Power Control : %s-----" %mfpc
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl");
                tdkTestObj.addParameter("paramValue",mfpc);
                tdkTestObj.addParameter("paramType","int");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    print "MFPC Set operation success";
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");

                    #Get operation to see if MFPC is 0db
                    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details != "":
                        curr_mfpc = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                        if curr_mfpc.strip("-").isdigit() and curr_mfpc == upper_bound:
                            print "MFPC Get operation returns : %s" %curr_mfpc;
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            flag = 1;
                            print "MFPC Get operation returns : %s" %curr_mfpc;
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            break;
                    else:
                        flag = 1;
                        print "MFPC Get operation failed; Details : %s" %details;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        break;
                else:
                    flag = 1;
                    print "MFPC Set operation failed; Details : %s" %details;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    break;

            if flag == 0:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: The MFPC set operations with values > 0db is success and the get operations returned the upper bound value of 0db";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: The MFPC conditions for values > 0db is not validated successfully";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";

            #Set MFPC to values < -20db and check if the get value is the lower limit -20db
            flag = 0;
            lower_bound = "-20";
            #All MFPC values set above the upper limit of 0db should be converted to 0db
            lower_OutofBound = ["-21", "-30", "-53", "-80", "-100", "-257", "-1000"];

            print "\nTEST STEP 3: Set Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl to values < -20db and check if the get operation gives the value -20db";
            print "EXPECTED RESULT 3: The set operation should be success and the get operation should give -20db as all values < -20db should be converted to the lower limit -20db";

            for mfpc in lower_OutofBound:
                print "\n-----For Management Frame Power Control : %s-----" %mfpc
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl");
                tdkTestObj.addParameter("paramValue",mfpc);
                tdkTestObj.addParameter("paramType","int");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                if expectedresult in actualresult:
                    print "MFPC Set operation success";
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");

                    #Get operation to see if MFPC is -20db
                    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                    tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl");
                    tdkTestObj.executeTestCase(expectedresult);
                    actualresult = tdkTestObj.getResult();
                    details = tdkTestObj.getResultDetails();

                    if expectedresult in actualresult and details != "":
                        curr_mfpc = details.split("VALUE:")[1].split(' ')[0].split(',')[0];
                        if curr_mfpc.strip("-").isdigit() and curr_mfpc == lower_bound:
                            print "MFPC Get operation returns : %s" %curr_mfpc;
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("SUCCESS");
                        else:
                            flag = 1;
                            print "MFPC Get operation returns : %s" %curr_mfpc;
                            #Set the result status of execution
                            tdkTestObj.setResultStatus("FAILURE");
                            break;
                    else:
                        flag = 1;
                        print "MFPC Get operation failed; Details : %s" %details;
                        #Set the result status of execution
                        tdkTestObj.setResultStatus("FAILURE");
                        break;
                else:
                    flag = 1;
                    print "MFPC Set operation failed; Details : %s" %details;
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    break;

            if flag == 0:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT 2: The MFPC set operations with values < -20db is success and the get operations returned the lower bound value of -20db";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";
            else:
                #Set the result status of execution
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT 2: The MFPC conditions for values < -20db is not validated successfully";
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";


            #Reverting to initial MFPC
            if curr_mfpc != initial_mfpc:
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl");
                tdkTestObj.addParameter("paramValue",mfpc);
                tdkTestObj.addParameter("paramType","int");
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP 4: Revert Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl to the initial value";
                print "EXPECTED RESULT 4: Revert of Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl should be success";

                if expectedresult in  expectedresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT 4: Revert operation is success; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS"
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT 4: Revert operation failed; Details : %s" %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE"
            else:
                print "Revert operation of Device.WiFi.AccessPoint.2.X_RDKCENTRAL-COM_ManagementFramePowerControl not required";
        else:
            #Set the result status of execution
            tdkTestObj.setResultStatus("FAILURE");
            print "The initial MFPC is NOT in the acceptable range of -20db to 0db";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT 1: Get operation failed";
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
