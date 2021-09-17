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
  <version>2</version>
  <name>TS_SANITY_ErrorInMeshServiceLogFile</name>
  <primitive_test_id/>
  <primitive_test_name>ExecuteCmd</primitive_test_name>
  <primitive_test_version>1</primitive_test_version>
  <status>FREE</status>
  <synopsis>To verify if relevant error logs are flooded in MeshService Log file</synopsis>
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
    <test_case_id>TC_SYSUTIL_55</test_case_id>
    <test_objective>To verify if relevant error logs are flooded in MeshService Log file</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components in DUT should be in a running state that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>Execute_Cmd</api_or_interface_used>
    <input_parameters>None</input_parameters>
    <automation_approch>1.Load the module .
2.Check if Mesh is enabled if not enable it
3.Check if MeshServiceLog.txt.0 file is present
4.Check for unexpected Error log messages from the file
5.Mark script as failure in case the Error log messages are present
6.Unload the module</automation_approch>
    <expected_output>Check if  no error log messages are present in MeshServiceLog.txt.0 file</expected_output>
    <priority>High</priority>
    <test_stub_interface>SYSUTIL</test_stub_interface>
    <test_script>TS_SANITY_ErrorInMeshServiceLogFile</test_script>
    <skipped>No</skipped>
    <release_version>M93</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
import tdklib;
from time import sleep;
#Test component to be tested
sysObj = tdklib.TDKScriptingLibrary("sysutil","RDKB");
obj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
sysObj.configureTestCase(ip,port,'TS_SANITY_ErrorInMeshServiceLogFile');
obj.configureTestCase(ip,port,'TS_SANITY_ErrorInMeshServiceLogFile');
#Get the result of connection with test component and DUT
sysutilloadmodulestatus=sysObj.getLoadModuleResult();
loadmodulestatus=obj.getLoadModuleResult();
MAX_RETRY = 4;
if "SUCCESS" in (sysutilloadmodulestatus.upper() and loadmodulestatus.upper()):
        #Set the result status of execution
        sysObj.setLoadModuleStatus("SUCCESS");
        obj.setLoadModuleStatus("SUCCESS");
        expectedresult="SUCCESS";
        tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        if expectedresult in actualresult:
            #Set the result status of execution
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 1: Get the Mesh enable state";
            print "EXPECTED RESULT 1: Should get the Mesh enable state";
            orgState = details.split("VALUE:")[1].split(' ')[0];
            print "ACTUAL RESULT 1: Initial mesh state is %s" %orgState;
            #Get the result of execution
            print "[TEST EXECUTION RESULT] : SUCCESS";
            if orgState == "false":
                #Enable Mesh and check its status
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
                tdkTestObj.addParameter("paramValue","true")
                tdkTestObj.addParameter("paramType","boolean")
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 2: Enable Mesh";
                    print "EXPECTED RESULT 2: Should enable Mesh"
                    print "ACTUAL RESULT 2: Mesh state is %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                    print "Check for every 20 secs whether the mesh status became Init"
		    sleep(20);
                    retryCount = 1;
                    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
                    tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Status")
                    while retryCount < MAX_RETRY:
                     	  #check if Mesh status becomes Init immediately after enabling mesh
                          tdkTestObj.executeTestCase("expectedresult");
	                  actualresult = tdkTestObj.getResult();
        	          details = tdkTestObj.getResultDetails();
                	  status = details.split("VALUE:")[1].split(' ')[0];
                          if expectedresult in actualresult and ("Init" in status or "Full" in status):
			      break;
			  else:
			      sleep(20)
			      retryCount = retryCount + 1;
                    if expectedresult in actualresult and ("Init" in status or "Full" in status):
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 3: Check if Mesh status is Init/Full";
                        print "EXPECTED RESULT 3: Mesh status should be Init/Full";
                        print "ACTUAL RESULT 3: Status is %s" %status;
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                        sleep(60);
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 3: Check if Mesh status is Init/Full";
                        print "EXPECTED RESULT 3: Mesh status should be Init/Full";
                        print "ACTUAL RESULT 3: Status is %s " %status;
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 2: Enable Mesh";
                    print "EXPECTED RESULT 2: Should enable Mesh"
                    print "ACTUAL RESULT 2: Mesh state is %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            	    obj.unloadModule("wifiagent");
                    exit()
            #check if Mesh status is Full
            tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Status")
            tdkTestObj.executeTestCase("expectedresult");
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();
            if expectedresult in actualresult and "Full" in details:
                status = details.split("VALUE:")[1].split(' ')[0];
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 4: Check if Mesh status is Full";
                print "EXPECTED RESULT 4: Mesh status should be Full";
                print "ACTUAL RESULT 4: Mesh Status is %s " %status;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";


                #Check whether the file is present or not
                tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                cmd = "[ -f /rdklogs/logs/MeshServiceLog.txt.0 ] && echo \"File exist\" || echo \"File does not exist\"";
                tdkTestObj.addParameter("command",cmd);
                expectedresult="SUCCESS";
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails().strip().replace("\\n", "");
                if details == "File exist":
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 5: Check for existence of MeshServiceLog.txt.0";
                    print "EXPECTED RESULT 5: MeshServiceLog.txt.0 file should be present";
                    print "ACTUAL RESULT 5:MeshServiceLog.txt.0 file is present";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    logFile = "/rdklogs/logs/MeshServiceLog.txt.0";
                    logMsg = ["WIFI_ERROR_channelChangeFail","Failed to push new channel"];
                    markerfound = 0;
                    for list in logMsg:
                        if markerfound == 1:
                           break;
                        else:
                            query="cat %s | grep -i \"%s\"" %(logFile,list);
                            print "query:%s" %query
                            tdkTestObj = sysObj.createTestStep('ExecuteCmd');
                            tdkTestObj.addParameter("command", query)
                            expectedresult="SUCCESS";
                            tdkTestObj.executeTestCase(expectedresult);
                            actualresult = tdkTestObj.getResult();
                            details = tdkTestObj.getResultDetails().strip().replace("\\n","");
                            print "Marker Detail Found fromLog file is: %s "%details;
                            if (len(details) == 0)  or list  not in details:
                               markerfound = 0;
                            else:
                                markerfound = 1;
                    if expectedresult in actualresult and markerfound == 1:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 6: Check if Error Log Message present in MeshServiceLog.txt.0";
                        print "EXPECTED RESULT 6:  Error log Message should not be present";
                        print "ACTUAL RESULT 6: ",details
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 6: Check if Error Message present in MeshServiceLog.txt.0";
                        print "EXPECTED RESULT 6:  Error log Message should not be present";
                        print "ACTUAL RESULT 6: Log Message not found";
                        #Get the result of execution
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 5: Check for existence of MeshServiceLog.txt.0";
                    print "EXPECTED RESULT 5: MeshServiceLog.txt.0 file should be present";
                    print "ACTUAL RESULT 5:MeshServiceLog.txt.0 file is not present";
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "TEST STEP 4: Check if Mesh status is Full";
                print "EXPECTED RESULT 4: Mesh status should be Full";
                print "ACTUAL RESULT 4: Status is %s " %details;
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : FAILURE";
            if orgState == "false":
                #change mesh state to previous one
                tdkTestObj = obj.createTestStep('WIFIAgent_Set');
                tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
                tdkTestObj.addParameter("paramValue",orgState)
                tdkTestObj.addParameter("paramType","boolean")
                tdkTestObj.executeTestCase("expectedresult");
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();
                if expectedresult in actualresult:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 7: Restore Enable state of Mesh";
                    print "EXPECTED RESULT 7: Should Restore Enable state of Mesh";
                    print "ACTUAL RESULT5 7: Details: %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : SUCCESS";
                else:
                    #Set the result status of execution
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 7: Restore Enable state of Mesh";
                    print "EXPECTED RESULT 7: Should Restore Enable state of Mesh";
                    print "ACTUAL RESULT 7: Details: %s " %details;
                    #Get the result of execution
                    print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 1: Get the state of Mesh"
            print "EXPECTED RESULT 1: Failure in getting the state of Mesh"
            print "ACTUAL RESULT 1: Initial mesh state is %s" %details;
            print "[TEST EXECUTION RESULT] : FAILURE";

        sysObj.unloadModule("sysutil");
        obj.unloadModule("wifiagent");
else:
     print "Failed to load module";
     sysObj.setLoadModuleStatus("FAILURE");
     obj.setLoadModuleStatus("FAILURE");
