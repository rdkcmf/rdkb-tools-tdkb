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
  <version>7</version>
  <name>TS_WIFIAGENT_CheckGRETAPsPersistence_RouterToBridgeTransition</name>
  <primitive_test_id/>
  <primitive_test_name>WIFIAgent_Set</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>Enable the Xfinity WiFi in router mode and check if the GRETAP interfaces created persist when the Lan Mode is transitioned to bridge-static.</synopsis>
  <groups_id/>
  <execution_time>30</execution_time>
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
    <test_case_id>TC_WIFIAGENT_167</test_case_id>
    <test_objective>Enable the Xfinity WiFi in router mode and check if the GRETAP interfaces created persist when the Lan Mode is transitioned to bridge-static.</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT
2.TDK Agent should be in running state or invoke it through StartTdk.sh script</pre_requisite>
    <api_or_interface_used>None </api_or_interface_used>
    <input_parameters>paramName : Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode
paramValue : mode(router or bridge-static)
paramType : string
</input_parameters>
    <automation_approch>1. Load the modules
2. Get the initial LanMode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode and store it.
3. Check if the initial Lan Mode is router, else set to router mode and cross  verify with GET operation
4. Get the initial Public WiFi parameters and store it.
5. Enable the Public WiFi and check if the CcspHotSpot process is running.
6. Then check if the GRETAP interfaces - ["gretap0.102", "gretap0.103", "gretap0.104", "gretap0.105"] and created in the device.
7. Change the Lan Mode to bridge-static and check if the mode change is successful with GET operation.
8. Check if the CcspHotSpot process is running in the DUT and the GRETAP interfaces created persist in the bridge-static mode as well.
9. Revert the Public WiFi parameters to initial values
10. Revert the Lan Mode to initial value if required.
11 Unload the modules.</automation_approch>
    <expected_output>Enable the Xfinity WiFi in router mode and check if the GRETAP interfaces - ["gretap0.102", "gretap0.103", "gretap0.104", "gretap0.105"] created persist when the Lan Mode is transitioned to bridge-static.</expected_output>
    <priority>High</priority>
    <test_stub_interface>wifiagent</test_stub_interface>
    <test_script>TS_WIFIAGENT_CheckGRETAPsPersistence_RouterToBridgeTransition</test_script>
    <skipped>No</skipped>
    <release_version>M97</release_version>
    <remarks/>
  </test_cases>
  <script_tags/>
</xml>

'''
def GetLanMode(wifiobj, step):
    expectedresult = "SUCCESS";
    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Get');
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();

    print "\nTEST STEP %d: Get the current Lan Mode using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %step;
    print "EXPECTED RESULT %d: Should retrieve the current Lan Mode successfully" %step;

    if expectedresult in actualresult:
        LanMode = details.split("VALUE:")[1].split(' ')[0];
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode retrieved successfully; Details : %s" %(step, LanMode);
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode not retrieved successfully; Details : %s" %(step, details);
        print "[TEST EXECUTION RESULT] : FAILURE";
    return tdkTestObj, actualresult, LanMode;

def SetLanMode(wifiobj, step, mode):
    expectedresult = "SUCCESS"
    tdkTestObj = wifiobj.createTestStep('WIFIAgent_Set');
    tdkTestObj.addParameter("paramName","Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode")
    tdkTestObj.addParameter("paramValue", mode)
    tdkTestObj.addParameter("paramType","string")
    tdkTestObj.executeTestCase("expectedresult");
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    sleep(120);

    print "\nTEST STEP %d : Change Lan Mode to %s using Device.X_CISCO_COM_DeviceControl.LanManagementEntry.1.LanMode" %(step, mode);
    print "EXPECTED RESULT %d: Should change Lan Mode to %s successfully" %(step, mode);

    if expectedresult in actualresult:
        #Set the result status of execution
        tdkTestObj.setResultStatus("SUCCESS");
        print "ACTUAL RESULT %d: Lan Mode SET operation returned success; Details: %s " %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : SUCCESS";
    else:
        #Set the result status of execution
        tdkTestObj.setResultStatus("FAILURE");
        print "ACTUAL RESULT %d: Lan Mode SET operation returned failure; Details: %s " %(step, details);
        #Get the result of execution
        print "[TEST EXECUTION RESULT] : FAILURE";
    return tdkTestObj, actualresult;

def SetGetMode(wifiobj, tdkTestObj, step, mode_to_check, mode_to_set):
    modeset_flag = 0;
    if mode_to_check != mode_to_set:
        tdkTestObj, actualresult = SetLanMode(wifiobj, step, mode_to_set);

        if expectedresult in actualresult :
            tdkTestObj.setResultStatus("SUCCESS");
            print "The set operation of new Lan Mode returned success";

            #Cross check with GET
            step = step + 1;
            tdkTestObj, actualresult, set_LanMode = GetLanMode(wifiobj, step);

            if set_LanMode == mode_to_set :
                modeset_flag = 1;
                tdkTestObj.setResultStatus("SUCCESS");
                print "The Lan Mode %s is set successfully" %mode_to_set;
            else :
                tdkTestObj.setResultStatus("FAILURE");
                print "The Lan Mode %s is not set successfully" %mode_to_set;
        else :
            tdkTestObj.setResultStatus("FAILURE");
            print "The set operation of new Lan Mode returned failure";
    else :
        modeset_flag = 1;
        set_LanMode = mode_to_check;
        tdkTestObj.setResultStatus("SUCCESS");
    return modeset_flag, step, set_LanMode;

def checkGRETAPs(tdkTestObj_Sys_ExeCmd, gretaps_list):
    found = 0;
    for gretap in gretaps_list:
        cmd = "brctl show | grep -i " + gretap;
        tdkTestObj_Sys_ExeCmd.addParameter("command",cmd);
        tdkTestObj_Sys_ExeCmd.executeTestCase(expectedresult);
        actualresult = tdkTestObj_Sys_ExeCmd.getResult();
        details = tdkTestObj_Sys_ExeCmd.getResultDetails().strip().replace("\\n", "");

        if expectedresult in actualresult and details != "":
            found = found + 1;
            tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
            print "%s is present" %gretap;
        else:
            tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
            print "%s is not present" %gretap;
    return found;


# use tdklib library,which provides a wrapper for tdk testcase script
import tdklib;
from time import sleep;
from tdkutility import *;
from xfinityWiFiLib import *;

#Test component to be tested
sysobj = tdklib.TDKScriptingLibrary("sysutil","1");
wifiobj = tdklib.TDKScriptingLibrary("wifiagent","1");

#IP and Port of box, No need to change,
#This will be replaced with corresponding DUT Ip and port while executing script
ip = <ipaddress>
port = <port>
sysobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckGRETAPsPersistence_RouterToBridgeTransition');
wifiobj.configureTestCase(ip,port,'TS_WIFIAGENT_CheckGRETAPsPersistence_RouterToBridgeTransition');

#Get the result of connection with test component and DUT
loadmodulestatus=sysobj.getLoadModuleResult();
loadmodulestatus1=wifiobj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus1 ;

if "SUCCESS" in loadmodulestatus.upper() and "SUCCESS" in loadmodulestatus1.upper():
    #Set the result status of execution
    sysobj.setLoadModuleStatus("SUCCESS");
    wifiobj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";
    modeset_flag = 0;

    #Get the initial LanMode
    step = 1;
    tdkTestObj, actualresult, initial_LanMode = GetLanMode(wifiobj, step);

    if expectedresult in actualresult and initial_LanMode != "":
        tdkTestObj.setResultStatus("SUCCESS");
        print "The device is initially in %s mode" %initial_LanMode;

        #Check if the mode is router initially, if not, set to router mode
        step = step + 1;
        mode_to_set = "router";
        mode_to_check = initial_LanMode;
        modeset_flag, step, set_LanMode = SetGetMode(wifiobj, tdkTestObj, step, mode_to_check, mode_to_set);
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "The device is initially in %s mode" %initial_LanMode;

    #Proceed if DUT in router mode
    if modeset_flag == 1 :
        #Reset the modeset_flag
        modeset_flag = 0;
        #Get the initial values of public wifi parameters
        paramList = ["Device.X_COMCAST-COM_GRE.Tunnel.1.DSCPMarkPolicy","Device.X_COMCAST-COM_GRE.Tunnel.1.PrimaryRemoteEndpoint","Device.X_COMCAST-COM_GRE.Tunnel.1.SecondaryRemoteEndpoint","Device.WiFi.SSID.5.SSID","Device.WiFi.SSID.6.SSID","Device.WiFi.SSID.5.Enable","Device.WiFi.SSID.6.Enable","Device.WiFi.AccessPoint.5.SSIDAdvertisementEnabled","Device.WiFi.AccessPoint.6.SSIDAdvertisementEnabled","Device.WiFi.SSID.10.SSID","Device.WiFi.SSID.10.Enable","Device.WiFi.AccessPoint.10.SSIDAdvertisementEnabled","Device.WiFi.AccessPoint.10.Security.ModeEnabled","Device.WiFi.AccessPoint.10.X_CISCO_COM_BssMaxNumSta","Device.WiFi.AccessPoint.10.Security.X_CISCO_COM_EncryptionMethod","Device.WiFi.AccessPoint.10.Security.RadiusServerIPAddr","Device.WiFi.AccessPoint.10.Security.RadiusServerPort","Device.WiFi.AccessPoint.10.Security.SecondaryRadiusServerIPAddr","Device.WiFi.AccessPoint.10.Security.SecondaryRadiusServerPort","Device.WiFi.SSID.9.SSID","Device.WiFi.SSID.9.Enable","Device.WiFi.AccessPoint.9.SSIDAdvertisementEnabled","Device.WiFi.AccessPoint.9.Security.ModeEnabled","Device.WiFi.AccessPoint.9.X_CISCO_COM_BssMaxNumSta","Device.WiFi.AccessPoint.9.Security.X_CISCO_COM_EncryptionMethod","Device.WiFi.AccessPoint.9.Security.RadiusServerIPAddr","Device.WiFi.AccessPoint.9.Security.RadiusServerPort","Device.WiFi.AccessPoint.9.Security.SecondaryRadiusServerIPAddr","Device.WiFi.AccessPoint.9.Security.SecondaryRadiusServerPort","Device.DeviceInfo.X_COMCAST_COM_xfinitywifiEnable"];
        step = step + 1;
        print "\nTEST STEP %d : Get the initial values of Public WiFi parameters" %step;
        print "EXPECTED RESULT %d : The initial Public WiFi parameters should be retrieved successfully" %step;
        tdkTestObj,actualresult,orgValue = GetPublicWiFiParamValues(wifiobj);

        if expectedresult in actualresult:
            tdkTestObj.setResultStatus("SUCCESS");
            print "ACTUAL RESULT %d: Initial Public WiFi parameter values are : %s" %(step, orgValue);
            print "[TEST EXECUTION RESULT] : SUCCESS";

            #Get the new values to be set
            step = step + 1;
            setvalues,tdkTestObj,actualresult  = parsePublicWiFiConfigValues(sysobj);
            print "\nTEST STEP %d : Get the set values to enable PublicWiFi" %step;
            print "EXPECTED RESULT %d : Should get the set values to enable PublicWiFi" %step;

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "ACTUAL RESULT %d : Successfully reteieved the Public WiFi parameters to be set" %step;
                print "[TEST EXECUTION RESULT] : SUCCESS";

                #Arrange the set values in order
                values = [setvalues[0],setvalues[1],setvalues[2],setvalues[3],setvalues[3],"true","true","true","true",setvalues[3],"true","true",setvalues[4],setvalues[5],setvalues[6],setvalues[7],setvalues[8],setvalues[7],setvalues[8],setvalues[3],"true","true",setvalues[4],setvalues[5],setvalues[6],setvalues[7],setvalues[8],setvalues[7],setvalues[8],"true"];
                index = 0;

                for param in paramList :
                    print "Parameter : ", paramList[index];
                    print "Value to be set : ", values[index];
                    index = index + 1;

                #Set Public WiFi parameters
                step = step + 1;
                tdkTestObj, actualresult, details = SetPublicWiFiParamValues(wifiobj,values);
                #Execute the test case in DUT
                tdkTestObj.executeTestCase(expectedresult);
                actualresult = tdkTestObj.getResult();
                details = tdkTestObj.getResultDetails();

                print "\nTEST STEP %d : Enable Public WiFi by setting the Public WiFi parameters" %step;
                print "EXPECTED RESULT %d : Public WiFi parameters should be set successfully" %step;

                if expectedresult in actualresult:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "ACTUAL RESULT %d : Prameters set successfully; Details : %s" %(step, details);
                    print "[TEST EXECUTION RESULT] : SUCCESS";

                    #Get PID of Hotspot process
                    step = step + 1;
                    sleep(120);
                    tdkTestObj_Sys_ExeCmd = sysobj.createTestStep('ExecuteCmd');
                    actualresult, details = getPID(tdkTestObj_Sys_ExeCmd,"CcspHotspot");

                    print "\nTEST STEP %d: Check if CcspHotspot process is running" %step;
                    print "EXPECTED RESULT %d:CcspHotspot  process should be running" %step;

                    if expectedresult in actualresult and details.isdigit():
                        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d: pid of CcspHotspot: %s" %(step, details);
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        #Check if all required GRETAPs are present
                        step = step + 1;
                        gretaps_list = ["gretap0.102", "gretap0.103", "gretap0.104", "gretap0.105"];
                        print "\nTEST STEP %d : Check if the required GRETAPs are present"  %step;
                        print "EXPECTED RESULT %d : All the required GRETAPs should be present" %step;
                        print "GRETAPs : ", gretaps_list;
                        gretaps_found = checkGRETAPs(tdkTestObj_Sys_ExeCmd, gretaps_list);

                        if gretaps_found == 4:
                            tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                            print "ACTUAL RESULT %d: All required GRETAPs are found" %step;
                            print "[TEST EXECUTION RESULT] : SUCCESS";

                            #Change Lan Mode to bridge mode
                            mode_to_set = "bridge-static";
                            mode_to_check = "router";
                            step = step + 1;
                            modeset_flag, step, set_LanMode = SetGetMode(wifiobj, tdkTestObj, step, mode_to_check, mode_to_set);

                            #Proceed if DUT in bridge-mode_to_set
                            if modeset_flag == 1:
                                #Ensure Hotspot process is running in bridge mode
                                step = step + 1;
                                actualresult, details = getPID(tdkTestObj_Sys_ExeCmd,"CcspHotspot");
                                print "\nTEST STEP %d: Check if CcspHotspot process is running in bridge mode" %step;
                                print "EXPECTED RESULT %d:CcspHotspot  process should be running in bridge mode" %step;

                                if expectedresult in actualresult and details.isdigit():
                                    tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                                    print "ACTUAL RESULT %d: pid of CcspHotspot: %s" %(step, details);
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

                                    #Check if the GRETAPs created are presisting on bridge mode
                                    step = step + 1;
                                    print "\nTEST STEP %d : Check if the required GRETAPs are persisting on bridge mode"  %step;
                                    print "EXPECTED RESULT %d : All the required GRETAPs should persist on bridge mode" %step;
                                    gretaps_found = checkGRETAPs(tdkTestObj_Sys_ExeCmd, gretaps_list);

                                    if gretaps_found == 4:
                                        tdkTestObj_Sys_ExeCmd.setResultStatus("SUCCESS");
                                        print "ACTUAL RESULT %d: All required GRETAPs are found on bridge mode" %step;
                                        print "[TEST EXECUTION RESULT] : SUCCESS";
                                    else:
                                        tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                                        print "ACTUAL RESULT %d: All required GRETAPs are not found on bridge mode" %step;
                                        print "[TEST EXECUTION RESULT] : FAILURE";
                                else:
                                    tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                                    print "ACTUAL RESULT %d: pid of CcspHotspot: %s" %(step, details);
                                    print "[TEST EXECUTION RESULT] :FAILURE";
                            else :
                                tdkTestObj.setResultStatus("FAILURE");
                                print "The Lan Mode could not be set to bridge-static";
                        else:
                            tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                            print "ACTUAL RESULT %d: All required GRETAPs are not found" %step;
                            print "[TEST EXECUTION RESULT] : FAILURE";
                    else:
                        tdkTestObj_Sys_ExeCmd.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d: pid of CcspHotspot: %s" %(step, details);
                        print "[TEST EXECUTION RESULT] :FAILURE";

                    #Revert Public WiFi parameters
                    step = step + 1;
                    tdkTestObj, actualresult, details = SetPublicWiFiParamValues(wifiobj,orgValue);

                    print "\nTEST STEP %d : Revert the Public WiFi parameter values" %step;
                    print "EXPECTED RESULT %d : Public WiFi parameters should be reverted back to their initial values successfully" %step;

                    if expectedresult in actualresult:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "ACTUAL RESULT %d : Revert operation success; Details : %s" %(step, details);
                        print "[TEST EXECUTION RESULT] : SUCCESS";
                    else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "ACTUAL RESULT %d : Revert operation failed; Details : %s" %(step, details);
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "ACTUAL RESULT %d : Prameters not set successfully; Details : %s" %(step, details);
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "ACTUAL RESULT %d : Unable to retrieve the Public WiFi parameters to be set" %step;
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "ACTUAL RESULT %d: Initial Public WiFi parameter values are : %s" %(step, orgValue);
            print "[TEST EXECUTION RESULT] : FAILURE";

        #Revert Lan Mode
        if set_LanMode != initial_LanMode :
            print "\n**************Reverting Lan Mode****************";
            step = step + 1;
            tdkTestObj, actualresult = SetLanMode(wifiobj, step, initial_LanMode);

            if expectedresult in actualresult:
                tdkTestObj.setResultStatus("SUCCESS");
                print "Lan Mode reverted successfully";
            else:
                tdkTestObj.setResultStatus("FAILURE");
                print "Lan Mode not reverted successfully";
        else:
            print "Lan Mode revert operation not required";
    else :
        tdkTestObj.setResultStatus("FAILURE");
        print "The Lan Mode could not be set to router";

    sysobj.unloadModule("sysutil");
    wifiobj.unloadModule("wifiagent");
else:
    print "Failed to load module";
    sysobj.setLoadModuleStatus("FAILURE");
    wifiobj.setLoadModuleStatus("FAILURE");
