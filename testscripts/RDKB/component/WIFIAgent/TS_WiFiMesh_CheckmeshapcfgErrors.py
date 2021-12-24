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
  <version>6</version>
  <name>TS_WiFiMesh_CheckmeshapcfgErrors</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To run the shell scripts /usr/ccsp/wifi/mesh_status.sh and /usr/ccsp/wifi/meshapcfg.sh and to check if the error log "cfg: command not found" is found under /rdklogs/logs/ when Mesh is enabled and the device is in router mode.</synopsis>
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
    <test_case_id>TC_WiFiMesh_161</test_case_id>
    <test_objective>To run the shell scripts /usr/ccsp/wifi/mesh_status.sh and /usr/ccsp/wifi/meshapcfg.sh and to check if the error log "cfg: command not found" is found under /rdklogs/logs/ when Mesh is enabled and the device is in router mode.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1. Ccsp Components  should be in a running state of DUT
2. TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None</api_or_interface_used>
    <input_parameters>paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
mode : router or bridge-static
Type : string
paramName : Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable
enable : true or false
Type : boolean</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode. If its not router, change to router mode and validate the SET with GET.
3. Get the initial value of Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable and check if it is enabled. If not, enable Mesh and verify the SET with the GET.
4. Check if the shell script /usr/ccsp/wifi/mesh_status.sh is present in the DUT. If so, run the shell script.
5. Check if the shell script /usr/ccsp/wifi/meshapcfg.sh is present in the DUT. If so, run the shell script.
6. Check if "cfg: command not found" is present  in any log files under /rdklogs/logs corresponding to the execution of the shell script meshapcfg.sh. If yes, return failure.
7. Revert the Mesh Enable and Lan Mode if required.
8. Unload the modules</automation_approch>
    <expected_output>The shell scripts /usr/ccsp/wifi/mesh_status.sh and /usr/ccsp/wifi/meshapcfg.sh should be run successfully and the error log "cfg: command not found" should not be found under /rdklogs/logs/ when Mesh is enabled and the device is in router mode.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WiFiMesh_CheckmeshapcfgErrors</test_script>
    <skipped>No</skipped>
    <release_version>M96</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("wifiagent","1");
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_WiFiMesh_CheckmeshapcfgErrors');
sysobj.configureTestCase(ip,port,'TS_WiFiMesh_CheckmeshapcfgErrors');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
loadmodulestatus1 =sysobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1

def setLanMode(mode, obj, step):
    expectedresult = "SUCCESS";
    status = 1;
    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    tdkTestObj.addParameter("paramValue", mode)
    tdkTestObj.addParameter("paramType","string")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Change Lan Mode to %s" %(step, mode);
    print "EXPECTED RESULT %d: Should change Lan Mode to %s" %(step, mode);

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Set operation success; Details: %s " %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        #Sleeping for the Lan Mode change to take effect
        sleep(120);

        #Cross check SET with GET
        step = step + 1;
        tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        newValue = details.split("VALUE:")[1].split(' ')[0];

        print "\nTEST STEP %d: Check if the Lan Mode is set successfully" %step;
        print "EXPECTED RESULT %d: The Lan Mode should be set successfully " %step;

        if expectedresult in actualresult and newValue == mode:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Lanmode is set successfully, current Lan Mode is : %s" %(step, newValue);
            print "[TEST EXECUTION RESULT] : SUCCESS";
            status = 0;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Lanmode is not set successfully, current Lan Mode is : %s" %(step, newValue);
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT : Set operation failed; Details: %s " %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status, newValue, step;

def setMeshEnable(enable, obj, step):
    expectedresult = "SUCCESS";
    status = 1;
    tdkTestObj = obj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
    tdkTestObj.addParameter("paramValue", enable)
    tdkTestObj.addParameter("paramType","boolean")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Set Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable to %s" %(step, enable);
    print "EXPECTED RESULT %d: Should set the mesh enable successfully" %step;

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Set operation success; Mesh state is %s " %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #Cross check SET with GET
        sleep(10);
        step = step + 1;
        tdkTestObj = obj.createTestStep('WIFIAgent_Get');
        tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
        tdkTestObj.executeTestCase("expectedresult");
        actualresult = tdkTestObj.getResult();
        details = tdkTestObj.getResultDetails();
        newValue = details.split("VALUE:")[1].split(' ')[0];

        print "\nTEST STEP %d: Check if the Mesh Enable is set successfully" %step;
        print "EXPECTED RESULT %d: The Mesh Enable should be set successfully " %step;

        if expectedresult in actualresult and newValue == enable:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Mesh Enable is set successfully, current enable status is : %s" %(step, newValue);
            print "[TEST EXECUTION RESULT] : SUCCESS";
            status = 0;
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Mesh Enable is not set successfully, current enable status is : %s" %(step, newValue);
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT : Set operation failed; Details: %s " %details;
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status, newValue, step;

def checkFileExists(sysobj, file, step):
    expectedresult = "SUCCESS";
    status = 1;
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    cmd = "[ -f " + file + " ] && echo \"File exist\" || echo \"File does not exist\"";
    print "\nCommand : ", cmd;
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d: Check for %s file presence" %(step, file);
    print "EXPECTED RESULT %d: %s file should be present" %(step, file);

    if expectedresult in actualresult and details == "File exist":
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: %s file is present" %(step, file);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        status = 0;
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: %s file is not present" %(step, file);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status;

def executeScript(sysobj, file, step):
    expectedresult = "SUCCESS";
    status = 1;
    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
    cmd = "sh " + file;
    print "\nCommand : ", cmd;
    tdkTestObj.addParameter("command",cmd);
    tdkTestObj.executeTestCase(expectedresult);
    sleep(10);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

    print "\nTEST STEP %d: Run the shell script %s" %(step, file);
    print "EXPECTED RESULT %d: Should run the shell script successfully" %step;

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: The shell script is executed successfully" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
        status = 0;
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: The shell script is not executed successfully" %step;
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return status;


if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    obj.setLoadModuleStatus("SUCCESS");
    sysobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Get the initial Lan Mode
    step = 1;
    revert_lanmode = 0;
    revert_mesh = 0;
    tdkTestObj = obj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    orgLanMode = details.split("VALUE:")[1].split(' ')[0];

    print "\nTEST STEP %d: Get the current Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
    print "EXPECTED RESULT %d: Should retrieve the current Lan Mode successfully" %step;

    if expectedresult in actualresult:
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Lanmode is %s" %(step, orgLanMode);
        print "[TEST EXECUTION RESULT] : SUCCESS";

        #if bridge mode is enabled, disable it before trying to enable mesh
        newMode = "";
        if "bridge-static" == orgLanMode:
            step = step + 1;
            mode = "router";
            status, newMode, step = setLanMode(mode, obj, step);

            if status == 1:
                print "Failed to disable bridge mode, cannot enable mesh in bridge mode, exiting script...";
                tdkTestObj.setResultStatus("FAILURE");
            else:
                revert_lanmode = 1;

        if orgLanMode == "router" or newMode == "router":
            #Get the Mesh Enable
            step = step + 1;
            tdkTestObj = obj.createTestStep('WIFIAgent_Get');
            tdkTestObj.addParameter("paramName","Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable")
            tdkTestObj.executeTestCase("expectedresult");
            actualresult = tdkTestObj.getResult();
            details = tdkTestObj.getResultDetails();

            print "\nTEST STEP %d: Get the Mesh enable state using Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable" %step;
            print "EXPECTED RESULT %d: Should get the Mesh enable state successfully" %step;

            if expectedresult in actualresult:
                #Set the result status of execution
                tdkTestObj.setResultStatus("SUCCESS");
                orgState = details.split("VALUE:")[1].split(' ')[0];
                print "ACTUAL RESULT %d: Initial mesh state is %s" %(step, orgState);
                #Get the result of execution
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Enable Mesh is not in enabled state initially
                newState = "";
                if orgState == "false":
                    step = step + 1;
                    enable = "true";
                    status, newState, step = setMeshEnable(enable, obj, step);
                    revert_mesh = 1;

                    if status == 1:
                        print "Failed to enable Mesh, exiting script...";
                        tdkTestObj.setResultStatus("FAILURE");
                    else :
                        revert_mesh = 1;

                if  orgState == "true" or newState == "true":
                    #Check if the file /usr/ccsp/wifi/mesh_status.sh exists
                    step = step + 1;
                    file = "/usr/ccsp/wifi/mesh_status.sh";
                    status = checkFileExists(sysobj, file, step);

                    if status == 0:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "File is present";

                        #Execute /usr/ccsp/wifi/mesh_status.sh
                        step = step + 1;
                        status = executeScript(sysobj, file, step);

                        if status == 0:
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "Shell script executed";

                            #Check if the file /usr/ccsp/wifi/meshapcfg.sh exists
                            step = step + 1;
                            file = "/usr/ccsp/wifi/meshapcfg.sh";
                            status = checkFileExists(sysobj, file, step);

                            if status == 0:
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "File is present";

                                #Execute /usr/ccsp/wifi/meshapcfg.sh
                                step = step + 1;
                                status = executeScript(sysobj, file, step);

                                if status == 0:
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "Shell script executed";

                                    #Check for the presence of error logs "cfg: command not found" due to execution of /usr/ccsp/wifi/meshapcfg.sh
                                    step = step + 1;
                                    tdkTestObj = sysobj.createTestStep('ExecuteCmd');
                                    cmd = "grep -i \"cfg: command not found\" /rdklogs/logs/*";
                                    print "\nCommand : ", cmd;
                                    tdkTestObj.addParameter("command",cmd);
                                    tdkTestObj.executeTestCase(expectedresult);
                                    actualresult = tdkTestObj.getResult();
                                    details = tdkTestObj.getResultDetails().strip().replace("\\n", "");

                                    print "\nTEST STEP %d: Check if there is any instance of \"cfg: command not found\" under /rdklogs/logs/ due to execution of /usr/ccsp/wifi/meshapcfg.sh" %step;
                                    print "EXPECTED RESULT %d: There should not be any instance of \"cfg: command not found\" under /rdklogs/logs/ due to execution of /usr/ccsp/wifi/meshapcfg.sh" %step;

                                    #To ensure that only those log lines are captured which are due to execution of /usr/ccsp/wifi/meshapcfg.sh
                                    if expectedresult in actualresult and "/usr/ccsp/wifi/meshapcfg.sh" not in details:
                                        tdkTestObj.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT %d: No instances found; Details : %s" %(step, details);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : SUCCESS";
                                    else:
                                        tdkTestObj.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT %d: Details : %s" %(step, details);
                                        #Get the result of execution
                                        print "[TEST EXECUTION RESULT] : FAILURE";
                                else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "Shell script not executed";
                            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "File is not present";
                        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "Shell script not executed";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "File is not present";

                    #Revert operation
                    if revert_mesh == 1:
                        step = step + 1;
                        status, newState, step = setMeshEnable(orgState, obj, step);

                        if status == 0:
                            print "Revert operation of Mesh Enable is success";
                            tdkTestObj.setResultStatus("SUCCESS");
                        else :
                            print "Revert operation of Mesh Enable failed";
                            tdkTestObj.setResultStatus("FAILURE");
                    else:
                        print "Revert operation of Mesh Enable not required";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "Mesh not enabled";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d: Initial mesh state is not retrieved; Details : %s" %(step, details);
                print "[TEST EXECUTION RESULT] : FAILURE";

            #Revert operation
            if revert_lanmode == 1:
                step = step + 1;
                status, newMode, step = setLanMode(orgLanMode, obj, step);

                if status == 1:
                    print "Revert operation of Lan Mode is success";
                    tdkTestObj.setResultStatus("SUCCESS");
                else:
                    print "Revert operation of Lan Mode failed";
                    tdkTestObj.setResultStatus("FAILURE");
            else:
                print "Revert operation of Lan Mode is not required";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "Lan Mode is not router";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Initial Lan Mode is not retrieved; Details : %s" %(step, details);
        print "[TEST EXECUTION RESULT] : FAILURE";

    obj.unloadModule("wifiagent");
    sysobj.unloadModule("sysutil");
else:
    print "Failed to load module";
    obj.setLoadModuleStatus("FAILURE");
    sysobj.setLoadModuleStatus("FAILURE");
