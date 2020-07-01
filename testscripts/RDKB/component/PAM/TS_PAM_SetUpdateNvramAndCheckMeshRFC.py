##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2020 RDK Management
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
  <version>11</version>
  <name>TS_PAM_SetUpdateNvramAndCheckMeshRFC</name>
  <primitive_test_id/>
  <primitive_test_name>pam_SetParameterValues</primitive_test_name>
  <primitive_test_version>2</primitive_test_version>
  <status>FREE</status>
  <synopsis>To Check Mesh Enable.Ovs Enable.Mesh PodEthernetBackhaulEnable parameters are able to set when SysCfg.UpdateNvram was false</synopsis>
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
    <test_case_id>TC_PAM_198</test_case_id>
    <test_objective>To Check Mesh Enable.Ovs Enable.Mesh PodEthernetBackhaulEnable parameters are able to set when SysCfg.UpdateNvram was false</test_objective>
    <test_type>Positive</test_type>
    <test_setup>Broadband</test_setup>
    <pre_requisite>1.Ccsp Components  should be in a running state of DUT that includes component under test Cable Modem
2.TDK Agent should be in running state or invoke it through StartTdk.sh script
</pre_requisite>
    <api_or_interface_used>N/A</api_or_interface_used>
    <input_parameters>Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SysCfg.UpdateNvram, Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable, Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable, Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.PodEthernetBackhaulEnable</input_parameters>
    <automation_approch>1. Load the pam module
2. Get the initial values of SysCfg.UpdateNvram, Mesh.Enable, Ovs.Enable and Mesh.PodEthernetBackhaulEnable and store it
3. Do a factory Reset and verify the factory defaults value for the parameters (SysCfg.UpdateNvram as true, Mesh.Enable as false, Ovs.Enable as false and Mesh.PodEthernetBackhaulEnable as true)
4. Set the UpdateNvramvalue as false and verify the same using get function
5. Try to set the values to the parameters (Mesh.Enable as true, Ovs.Enable as true and Mesh.PodEthernetBackhaulEnable as false) and all set operations should success
6. Revert back to the original values
7. Unload the pam module
</automation_approch>
    <expected_output>Set Function to the parameters  SysCfg.UpdateNvram, Mesh.Enable, Ovs.Enable and Mesh.PodEthernetBackhaulEnable should success when UpdateNvram was false</expected_output>
    <priority>High</priority>
    <test_stub_interface>pam</test_stub_interface>
    <test_script>TS_PAM_SetUpdateNvramAndCheckMeshRFC</test_script>
    <skipped>No</skipped>
    <release_version>M78</release_version>
    <remarks>None</remarks>
  </test_cases>
  <script_tags/>
</xml>

'''
#import statement
import tdklib;
from time import sleep;

#Test component to be tested
obj = tdklib.TDKScriptingLibrary("pam","RDKB");

#IP and Port of box, No need to change,
#This will be replaced with correspoing Box Ip and port while executing script
ip = <ipaddress>
port = <port>
obj.configureTestCase(ip,port,'TS_PAM_SetUpdateNvramAndCheckMeshRFC');

#Get the result of connection with test component and DUT
loadmodulestatus =obj.getLoadModuleResult();
print "[LIB LOAD STATUS]  :  %s" %loadmodulestatus ;

def pam_GetParameterValues(tdkTestObj,paramname):
    tdkTestObj.addParameter("ParamName",paramname);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult,details;

def pam_SetParameterValues(tdkTestObj,paramname,setvalue):
    tdkTestObj.addParameter("ParamName",paramname);
    tdkTestObj.addParameter("Type","boolean");
    tdkTestObj.addParameter("ParamValue",setvalue);
    expectedresult="SUCCESS";
    tdkTestObj.executeTestCase(expectedresult);
    actualresult = tdkTestObj.getResult();
    details = tdkTestObj.getResultDetails();
    return actualresult,details;

if "SUCCESS" in loadmodulestatus.upper():
    #Set the result status of execution
    obj.setLoadModuleStatus("SUCCESS");
    expectedresult="SUCCESS";

    #Get the initial values before Factory Reset
    tdkTestObj = obj.createTestStep("pam_GetParameterValues");
    nvram_initial_result,nvram_initial_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SysCfg.UpdateNvram");
    print "UpdateNvram Param Result %s and Current value %s" %(nvram_initial_result,nvram_initial_details);

    mesh_initial_result,mesh_initial_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable");
    print "Mesh Enable Param Result %s and Current value %s" %(mesh_initial_result,mesh_initial_details);

    ovs_initial_result,ovs_initial_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable");
    print "OVS Enable Param Result %s and Current value %s" %(ovs_initial_result,ovs_initial_details);

    podeth_initial_result,podeth_initial_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.PodEthernetBackhaulEnable");
    print "PodEthernetBackhaulEnable Param Result %s and Current value %s" %(podeth_initial_result,podeth_initial_details);

    if expectedresult in (nvram_initial_result and mesh_initial_result and ovs_initial_result and podeth_initial_result):
        tdkTestObj.setResultStatus("SUCCESS");
        print "TEST STEP 1: Get the Initial values of UpdateNvram,Mesh Enable, ovs Enable and Mesh PodEthernetBackhaulEnable"
        print "EXPECTED RESULT 1: Should Get the Initial values of UpdateNvram,Mesh Enable, ovs Enable and Mesh PodEthernetBackhaulEnable"
        print "ACTUAL RESULT 1: Get the Initial values are success"
        print "[TEST EXECUTION RESULT] : SUCCESS";

	#Do Factory Reset
    	obj.saveCurrentState();
	tdkTestObj = obj.createTestStep('pam_Setparams');
	tdkTestObj.addParameter("ParamName","Device.X_CISCO_COM_DeviceControl.FactoryReset");
	tdkTestObj.addParameter("ParamValue","Router,Wifi,VoIP,Dect,MoCA");
    	tdkTestObj.addParameter("Type","string");
	expectedresult="SUCCESS";
	tdkTestObj.executeTestCase(expectedresult);
        obj.restorePreviousStateAfterReboot();
        sleep(180);

	tdkTestObj = obj.createTestStep("pam_GetParameterValues");
        nvram_result,nvram_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SysCfg.UpdateNvram");
        print "UpdateNvram Param Result %s and Current value %s" %(nvram_result,nvram_details);

        mesh_result,mesh_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable");
        print "Mesh Enable Param Result %s and Current value %s" %(mesh_result,mesh_details);

        ovs_result,ovs_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable");
        print "OVS Enable Param Result %s and Current value %s" %(ovs_result,ovs_details);

        podeth_result,podeth_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.PodEthernetBackhaulEnable");
        print "PodEthernetBackhaulEnable Param Result %s and Current value %s" %(podeth_result,podeth_details);

        if expectedresult in (nvram_result and mesh_result and ovs_result and podeth_result):
            tdkTestObj.setResultStatus("SUCCESS");
            print "TEST STEP 2: Verify the get values after Factory Result "
            print "EXPECTED RESULT 2: Get function should be success"
            print "ACTUAL RESULT 2: Get functions was success after factory reset"
            print "[TEST EXECUTION RESULT] : SUCCESS";

	    if nvram_details == "true" and mesh_details == "false" and ovs_details == "false" and podeth_details == "true":
                tdkTestObj.setResultStatus("SUCCESS");
                print "TEST STEP 3: Verify the Values after Factory Result "
                print "EXPECTED RESULT 3: Factory Default values should be UpdateNvram as true,Mesh Enable as false, ovs Enable as false and Mesh PodEthernetBackhaulEnable as true"
                print "ACTUAL RESULT 3: Factory Defaults values verified successfully"
                print "[TEST EXECUTION RESULT] : SUCCESS";
                sleep(10);

		tdkTestObj = obj.createTestStep('pam_SetParameterValues');
		nvram_set_result,nvram_set_details = pam_SetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SysCfg.UpdateNvram","false");
		print "UpdateNvram Param set Result %s and Current value %s" %(nvram_set_result,nvram_set_details);

                if expectedresult in nvram_set_result:
                    tdkTestObj.setResultStatus("SUCCESS");
                    print "TEST STEP 4: Set Update Nvram value as False"
                    print "EXPECTED RESULT 4: Set Function should success to make update nvram as false"
                    print "ACTUAL RESULT 4: Set function was success and update nvram value set to false"
                    print "[TEST EXECUTION RESULT] : SUCCESS";

     		    sleep(10);
		    tdkTestObj = obj.createTestStep("pam_GetParameterValues");
		    nvram_get_result,nvram_get_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SysCfg.UpdateNvram");
		    print "UpdateNvram Param Result %s and Current value %s" %(nvram_get_result,nvram_get_details);

    		    if expectedresult in nvram_get_result:
                        tdkTestObj.setResultStatus("SUCCESS");
                        print "TEST STEP 5: Verify Update Nvram value as False"
                        print "EXPECTED RESULT 5: Get Function should success and update nvram value should be false"
                        print "ACTUAL RESULT 5: Update Nvram value verified successfully"
                        print "[TEST EXECUTION RESULT] : SUCCESS";

                        tdkTestObj = obj.createTestStep('pam_SetParameterValues');
        	        mesh_set_result,mesh_set_details = pam_SetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable",str(not mesh_details).lower());
		        print "Mesh Enable Param Result %s and Current value %s" %(mesh_set_result,mesh_set_details);

		        ovs_set_result,ovs_set_details = pam_SetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable",str(not ovs_details).lower());
		        print "OVS Enable Param Result %s and Current value %s" %(ovs_set_result,ovs_set_details);

		        podeth_set_result,podeth_set_details = pam_SetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.PodEthernetBackhaulEnable",str(not podeth_details).lower());
		        print "PodEthernetBackhaulEnable Param Result %s and Current value %s" %(podeth_set_result,podeth_set_details);

		        if expectedresult in (mesh_set_result and ovs_set_result and podeth_set_result):
                            tdkTestObj.setResultStatus("SUCCESS");
                            print "TEST STEP 6: Set new values to Mesh enable,Mesh PodEthernetBackhaulEnable and Ovs enable when update nvram value was false"
                            print "EXPECTED RESULT 6: Set Function should success"
                            print "ACTUAL RESULT 6: Set function was success"
                            print "[TEST EXECUTION RESULT] : SUCCESS";

		            tdkTestObj = obj.createTestStep("pam_GetParameterValues");
		            nvram_get_result,nvram_get_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SysCfg.UpdateNvram");
		            print "UpdateNvram Param Result %s and Current value %s" %(nvram_get_result,nvram_get_details);

        		    mesh_get_result,mesh_get_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable");
	        	    print "Mesh Enable Param Result %s and Current value %s" %(mesh_get_result,mesh_get_details);

        		    ovs_get_result,ovs_get_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable");
	        	    print "OVS Enable Param Result %s and Current value %s" %(ovs_get_result,ovs_get_details);

        		    podeth_get_result,podeth_get_details = pam_GetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.PodEthernetBackhaulEnable");
	        	    print "PodEthernetBackhaulEnable Param Result %s and Current value %s" %(podeth_get_result,podeth_get_details);

            		    if expectedresult in (nvram_get_result and mesh_get_result and ovs_get_result and podeth_get_result):
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 7: Get new values of Mesh enable,Mesh PodEthernetBackhaulEnable and Ovs enable"
                                print "EXPECTED RESULT 7: Get Function should success"
                                print "ACTUAL RESULT 7: Get function was success"
                                print "[TEST EXECUTION RESULT] : SUCCESS";

        			if mesh_get_details.upper() == str(not mesh_details).upper()  and ovs_get_details.upper() == str(not ovs_details).upper() and podeth_get_details.upper() == str(not podeth_details).upper():
	        		    print "Get Values Verified after set";
                                    tdkTestObj.setResultStatus("SUCCESS");
                                    print "TEST STEP 8: Verify the new values of Mesh enable,Mesh PodEthernetBackhaulEnable and Ovs enable"
                                    print "EXPECTED RESULT 8: The values should be mesh enable as true ,PodEthernetBackhaulEnable as true and ovs enable as false "
                                    print "ACTUAL RESULT 8: Verification was success"
                                    print "[TEST EXECUTION RESULT] : SUCCESS";

        			else:
                                    tdkTestObj.setResultStatus("FAILURE");
                                    print "TEST STEP 8: Verify the new values of Mesh enable,Mesh PodEthernetBackhaulEnable and Ovs enable"
                                    print "EXPECTED RESULT 8: The values should be mesh enable as true ,PodEthernetBackhaulEnable as true and ovs enable as false "
                                    print "ACTUAL RESULT 8: Verification was Failed"
      		                    print "[TEST EXECUTION RESULT] : FAILURE";
    		            else:
			        tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 7: Get new values of Mesh enable,Mesh PodEthernetBackhaulEnable and Ovs enable"
                                print "EXPECTED RESULT 7: Get Function should success"
                                print "ACTUAL RESULT 7: Get function was Failed"
    		                print "[TEST EXECUTION RESULT] : FAILURE";

		            #Revert the values
	    	            tdkTestObj = obj.createTestStep('pam_SetParameterValues');
		            nvram_revert_result,nvram_revert_details = pam_SetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.SysCfg.UpdateNvram",nvram_initial_details);
		            print "UpdateNvram Param set Result %s and Current value %s" %(nvram_revert_result,nvram_revert_details);
		            sleep(10);

		            mesh_revert_result,mesh_revert_details = pam_SetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.Enable",mesh_initial_details);
		            print "Mesh Enable Param Result %s and Current value %s" %(mesh_revert_result,mesh_revert_details);

		            ovs_revert_result,ovs_revert_details = pam_SetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_RFC.Feature.OVS.Enable",ovs_initial_details);
		            print "OVS Enable Param Result %s and Current value %s" %(ovs_revert_result,ovs_revert_details);

		            podeth_revert_result,podeth_revert_details = pam_SetParameterValues(tdkTestObj,"Device.DeviceInfo.X_RDKCENTRAL-COM_xOpsDeviceMgmt.Mesh.PodEthernetBackhaulEnable",podeth_initial_details);
		            print "PodEthernetBackhaulEnable Param Result %s and Current value %s" %(podeth_revert_result,podeth_revert_details);

	    	            if expectedresult in (nvram_revert_result and mesh_revert_result and ovs_revert_result and podeth_revert_result):
                                tdkTestObj.setResultStatus("SUCCESS");
                                print "TEST STEP 9: Revert the values to initial values"
                                print "EXPECTED RESULT 9: Revert set operation should success"
                                print "ACTUAL RESULT 9: Revert operation  was success"
                                print "[TEST EXECUTION RESULT] : SUCCESS";
	    	            else:
                                tdkTestObj.setResultStatus("FAILURE");
                                print "TEST STEP 9: Revert the values to initial values"
                                print "EXPECTED RESULT 9: Revert set operation should success"
                                print "ACTUAL RESULT 9: Revert operation  was Failed"
                                print "[TEST EXECUTION RESULT] : FAILURE";
		        else:
                            tdkTestObj.setResultStatus("FAILURE");
                            print "TEST STEP 6: Set new values to Mesh enable,Mesh PodEthernetBackhaulEnable and Ovs enable when update nvram value was false"
                            print "EXPECTED RESULT 6: Set Function should success"
                            print "ACTUAL RESULT 6: Set function was success"
                            print "[TEST EXECUTION RESULT] : FAILURE";
	            else:
                        tdkTestObj.setResultStatus("FAILURE");
                        print "TEST STEP 5: Verify Update Nvram value as False"
                        print "EXPECTED RESULT 5: Get Function should success and update nvram value should be false"
                        print "ACTUAL RESULT 5: Update Nvram value verification Failed"
                        print "[TEST EXECUTION RESULT] : FAILURE";
                else:
                    tdkTestObj.setResultStatus("FAILURE");
                    print "TEST STEP 4: Set Update Nvram value as False"
                    print "EXPECTED RESULT 4: Set Function should success to make update nvram as false"
                    print "ACTUAL RESULT 4: Set function was Failed"
                    print "[TEST EXECUTION RESULT] : FAILURE";
            else:
                tdkTestObj.setResultStatus("FAILURE")
                print "[TEST EXECUTION RESULT] : FAILURE";
                print "TEST STEP 3: Verify the Values after Factory Result "
                print "EXPECTED RESULT 3: Factory Default values should be UpdateNvram as true,Mesh Enable as false, ovs Enable as false and Mesh PodEthernetBackhaulEnable as true"
                print "ACTUAL RESULT 3: Factory Defaults values verification Failed"
                print "[TEST EXECUTION RESULT] : FAILURE";
        else:
            tdkTestObj.setResultStatus("FAILURE");
            print "TEST STEP 2: Verify the get values after Factory Result "
            print "EXPECTED RESULT 2: Get function should be success"
            print "ACTUAL RESULT 2: Get functions was Failed after factory reset"
            print "[TEST EXECUTION RESULT] : FAILURE";
    else:
        tdkTestObj.setResultStatus("FAILURE");
        print "TEST STEP 1: Get the Initial values of UpdateNvram,Mesh Enable, ovs Enable and Mesh PodEthernetBackhaulEnable"
        print "EXPECTED RESULT 1: Should Get the Initial values of UpdateNvram,Mesh Enable, ovs Enable and Mesh PodEthernetBackhaulEnable"
        print "ACTUAL RESULT 1: Get the Initial values were failed"
        print "[TEST EXECUTION RESULT] : FAILURE";
    obj.unloadModule("pam");
else:
    print "Failed to load wifi module";
    obj.setLoadModuleStatus("FAILURE");
    print "Module loading failed";
