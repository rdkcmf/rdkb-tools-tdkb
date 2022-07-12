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

AM_CFLAGS = -D_ANSC_LINUX
AM_CFLAGS += -D_ANSC_USER
AM_CFLAGS += -D_ANSC_LITTLE_ENDIAN_
AM_LDFLAGS = -lccsp_common
if PLATFORM_ENABLED
AM_LDFLAGS += -ltr181
endif
AM_CFLAGS += -DeRT=$(ERT_VALUE)
AM_CFLAGS += -Dplatform=$(PLATFORM_ENABLED)
AM_CPPFLAGS = -Wall
ACLOCAL_AMFLAGS = -I m4
hardware_platform = i686-linux-gnu
lib_LTLIBRARIES = libtdkagentssp.la
libtdkagentssp_la_CPPFLAGS = -I$(top_srcdir)/tdkb_lib/include \
                                -I${PKG_CONFIG_SYSROOT_DIR}$(includedir)/ \
                                -I${PKG_CONFIG_SYSROOT_DIR}$(includedir)/ccsp \
                                -I${PKG_CONFIG_SYSROOT_DIR}$(includedir)/trower-base64 \
                                -I${PKG_CONFIG_SYSROOT_DIR}$(includedir)/rbus \
                                -I${PKG_CONFIG_SYSROOT_DIR}$(includedir)/rtmessage

if PLATFORM_ENABLED
if NON_CM
libtdkagentssp_la_SOURCES = src/ssp_messagebus_interface.c src/ssp_tdk_mbus_wrp.c src/ssp_tdk_mbus_lib.c src/ssp_action.c src/ssp_main.c src/ssp_tdk_wrp.c src/ssp_pam_bridge.c src/ssp_tdk_Ethsw_wrp.c src/ssp_tdk_dhcp_hal_wrp.c src/ssp_tdk_platform_hal_wrp.c src/ssp_tdk_eponhal_wrp.c src/ssp_tdk_mso_mgmt_hal_wrp.c src/ssp_tdk_blehal_wrp.c src/ssp_tdk_rbus_wrp.c src/ssp_tdk_fwupgradehal_wrp.c
else
libtdkagentssp_la_SOURCES = src/ssp_messagebus_interface.c src/ssp_tdk_mbus_wrp.c src/ssp_tdk_mbus_lib.c src/ssp_action.c src/ssp_main.c src/ssp_tdk_CosaCM_wrp.c src/ssp_tdk_wrp.c src/ssp_tdk_CosaMTA_wrp.c src/ssp_pam_bridge.c src/ssp_tdk_cmhal_wrp.c src/ssp_tdk_Ethsw_wrp.c src/ssp_tdk_dhcp_hal_wrp.c src/ssp_tdk_platform_hal_wrp.c src/ssp_tdk_mocahal_wrp.c src/ssp_tdk_mtahal_wrp.c src/ssp_tdk_eponhal_wrp.c src/ssp_tdk_mso_mgmt_hal_wrp.c src/ssp_tdk_blehal_wrp.c src/ssp_tdk_rbus_wrp.c src/ssp_tdk_fwupgradehal_wrp.c
endif
else
libtdkagentssp_la_SOURCES = src/ssp_messagebus_interface.c src/ssp_tdk_mbus_wrp.c src/ssp_tdk_mbus_lib.c src/ssp_action.c src/ssp_main.c src/ssp_tdk_CosaCM_wrp.c src/ssp_tdk_wrp.c src/ssp_tdk_CosaMTA_wrp.c src/ssp_tdk_cmhal_wrp.c src/ssp_tdk_Ethsw_wrp.c src/ssp_tdk_dhcp_hal_wrp.c src/ssp_tdk_platform_hal_wrp.c src/ssp_tdk_mocahal_wrp.c src/ssp_tdk_mtahal_wrp.c src/ssp_tdk_eponhal_wrp.c src/ssp_tdk_mso_mgmt_hal_wrp.c src/ssp_tdk_blehal_wrp.c src/ssp_tdk_rbus_wrp.c src/ssp_tdk_fwupgradehal_wrp.c
endif
if PLATFORM_ENABLED
libtdkagentssp_la_LDFLAGS =  -lccsp_common -ltr181 -ldmltad -lhal_wifi -lrbus
else
libtdkagentssp_la_LDFLAGS =  -lccsp_common -lhal_wifi -lrbus
endif
