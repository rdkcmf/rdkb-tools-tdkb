##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2016 RDK Management
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
if NON_CM
SUBDIRS = agent tdkb_lib RDKLogger_stub WIFIAgent_stub MBUS_Stub WECB_Stub TR069Pa_Stub AdvancedConfig_stub pam_stub SysUtil_stub TAD_stub LMLite_Stub WIFIHAL_stub ethsw_hal_stub dhcp_hal_stub tdkb_e2e_stub platform_hal_stub tdkb_tr181_stub XUPNP_Stub EPONHAL_Stub mso_mgmt_hal_stub BLEHAL_Stub RBUS_Stub  $(SUBDIR_WANMANAGER)
else
SUBDIRS = agent tdkb_lib RDKLogger_stub WIFIAgent_stub MBUS_Stub WECB_Stub TR069Pa_Stub AdvancedConfig_stub pam_stub SysUtil_stub TAD_stub LMLite_Stub WIFIHAL_stub ethsw_hal_stub dhcp_hal_stub tdkb_e2e_stub platform_hal_stub tdkb_tr181_stub XUPNP_Stub EPONHAL_Stub mso_mgmt_hal_stub BLEHAL_Stub RBUS_Stub CMAgent_stub CosaCM_Stub SNMP_PA_Stub Mta_agent_Stub CosaMTA_Stub Moca_Stub CMHAL_Stub MoCAHAL_Stub MTAHAL_Stub $(SUBDIR_WANMANAGER)
endif

DIST_SUBDIRS = @SUBDIRS@

distcleancheck_listfiles = *-libtool
