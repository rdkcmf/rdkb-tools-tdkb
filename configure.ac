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
dnl                                               -*- Autoconf -*-
dnl Process this file with autoconf to produce a configure script.

dnl AC_PREREQ([2.69])
AC_INIT(tdk-b, 1.0, praveensnair@tataelxsi.co.in,tdk-b)
AC_CONFIG_SRCDIR([agent/src/agentmain.cpp])
AM_CONFIG_HEADER(config.h)
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([foreign no-dist-gzip dist-bzip2 subdir-objects 1.9])
LT_INIT

dnl subdirectories.

dnl Checks for programs.
AC_PROG_CXX
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_CPP
AC_PROG_CXXCPP

dnl use pretty build output with automake >= 1.11
m4_ifdef([AM_SILENT_RULES],[AM_SILENT_RULES([yes])],
  [AM_DEFAULT_VERBOSITY=1
   AC_SUBST(AM_DEFAULT_VERBOSITY)])


dnl **********************************
dnl checks for dependencies
dnl **********************************
AC_HEADER_STDC

dnl Checks for header files.
AC_CHECK_HEADERS([limits.h memory.h stdlib.h string.h sys/socket.h unistd.h])

dnl Checks for typedefs, structures, and compiler characteristics.
dnl AC_CHECK_HEADER_STDBOOL
AC_TYPE_UINT8_T

dnl Checks for library functions.
AC_FUNC_MALLOC
AC_CHECK_FUNCS([memset strdup strerror])

COPTS="-DDEBUG_LEVEL_TRACE"
AM_CXXFLAGS="$AM_CXXFLAGS -DDEBUG_LEVEL_TRACE"
AGENT_FLAGS=" "
CONFIG_PREFIX="/etc/"
RDK_VERSION="RDKB"
SUBDIR_HYBRID=" "
SUBDIR_CLIENT=" "
SUBDIR_WANMANAGER= " "

ERT_VALUE=0

AC_ARG_ENABLE([ert],
        AS_HELP_STRING([--enable-ert],[enable ert]),
        [
          case "${enableval}" in
             yes) ERT_VALUE=1 ;;
           no) ERT_VALUE=0 ;;
          *) AC_MSG_ERROR([bad value ${enableval} for --enable-ert ]) ;;
           esac
           ],
         [echo "ert is enabled"])


AC_SUBST(ERT_VALUE)

AC_ARG_ENABLE([platform],
[  --enable-platform    Enable platform],
[case "${enableval}" in
  yes) platform=true ;;
  no)  platform=false ;;
  *) AC_MSG_ERROR([bad value ${enableval} for --enable-platform]) ;;
esac],[platform=false])
AM_CONDITIONAL([PLATFORM_ENABLED], [test x$platform = xtrue])


REDIRECT_FLAG=0

AC_ARG_ENABLE([redirect],
        AS_HELP_STRING([--enable-redirect],[enable redirect]),
        [
          case "${enableval}" in
             yes) REDIRECT_FLAG=1 ;;
           no) REDIRECT_FLAG=0 ;;
          *) AC_MSG_ERROR([bad value ${enableval} for --enable-redirect ]) ;;
           esac
           ],
         [echo "Redirect Flag enabled"])

AC_SUBST(REDIRECT_FLAG)

AC_ARG_ENABLE([nonCM],
        AS_HELP_STRING([--enable-nonCM],[enable nonCM]),
        [
          case "${enableval}" in
             yes) nonCM=true
                  echo dsl based platform;;
             no) nonCM=false;;
          *) AC_MSG_ERROR([bad value ${enableval} for --enable-dsl ]) ;;
           esac
           ],
         [echo "DSL is not enabled"])

AM_CONDITIONAL([NON_CM], [test x$nonCM = xtrue])


AC_ARG_ENABLE([rdkb_telcovoice_manager],
        AS_HELP_STRING([--enable-rdkb_telcovoice_manager],[enable rdkb_telcovoice_manager]),
        [
          case "${enableval}" in
             yes) rdkb_telcovoice_manager=true
                  SUBDIR_WANMANAGER+=" jsonhal_lib TELCOVOICEMgrHal_Stub"
                  echo Telco Voice Manager is enabled;;
             no) rdkb_telcovoice_manager=false ;;
          *) AC_MSG_ERROR([bad value ${enableval} for --enable-rdkb_telcovoice_manager ]) ;;
           esac
           ],
         [echo "Telco Voice Manager is not enabled"])

AM_CONDITIONAL([RDKB_TELCOVOICE_MANAGER], [test x$rdkb_telcovoice_manager = xtrue])


AC_ARG_ENABLE([fwupgrade_manager],
        AS_HELP_STRING([--enable-fwupgrade_manager],[enable fwupgrade_manager]),
        [
          case "${enableval}" in
             yes) fwupgrade_manager=true
                  SUBDIR_WANMANAGER+=" jsonhal_lib FWUpgradeHAL_Stub "
                  echo FWUpgrade Manager is enabled;;
             no) fwupgrade_manager=false ;;
          *) AC_MSG_ERROR([bad value ${enableval} for --enable-fwupgrade_manager ]) ;;
           esac
           ],
         [echo "FWUpgrade Manager is not enabled"])

AM_CONDITIONAL([FWUPGRADE_MANAGER], [test x$fwupgrade_manager = xtrue])


AC_ARG_ENABLE([rdkb_xdsl_ppp_manager],
        AS_HELP_STRING([--enable-rdkb_xdsl_ppp_manager],[enable rdkb_xdsl_ppp_manager]),
        [
          case "${enableval}" in
             yes) rdkb_xdsl_ppp_manager=true
                  SUBDIR_WANMANAGER+=" jsonhal_lib DSLHAL_Stub "
                  echo XDSL Manager is enabled;;
             no) rdkb_xdsl_ppp_manager=false ;;
          *) AC_MSG_ERROR([bad value ${enableval} for --enable-rdkb_xdsl_ppp_manager ]) ;;
           esac
           ],
         [echo "XDSL Manager is not enabled"])

AM_CONDITIONAL([RDKB_XDSL_PPP_MANAGER], [test x$rdkb_xdsl_ppp_manager = xtrue])

AC_SUBST(COPTS)
AC_SUBST(AGENT_FLAGS)
AC_SUBST(CONFIG_PREFIX)
AC_SUBST(RDK_VERSION)
AC_SUBST(SUBDIR_HYBRID)
AC_SUBST(SUBDIR_CLIENT)
AC_SUBST(SUBDIR_WANMANAGER)
AC_CONFIG_FILES([Makefile
	 agent/Makefile
         tdkb_lib/Makefile
         jsonhal_lib/Makefile
         CMAgent_stub/Makefile
	 WIFIAgent_stub/Makefile
	 MBUS_Stub/Makefile
	 WECB_Stub/Makefile
	 Mta_agent_Stub/Makefile
	 CosaCM_Stub/Makefile
         CosaMTA_Stub/Makefile
	 TR069Pa_Stub/Makefile
	 AdvancedConfig_stub/Makefile
	 SNMP_PA_Stub/Makefile
	 pam_stub/Makefile
	 SysUtil_stub/Makefile
         RDKLogger_stub/Makefile
	 TAD_stub/Makefile
	 Moca_Stub/Makefile
	 LMLite_Stub/Makefile
	 WIFIHAL_stub/Makefile
	 CMHAL_Stub/Makefile
	 ethsw_hal_stub/Makefile
	 dhcp_hal_stub/Makefile
	 platform_hal_stub/Makefile
	 tdkb_e2e_stub/Makefile
	 tdkb_tr181_stub/Makefile
	 MoCAHAL_Stub/Makefile
	 MTAHAL_Stub/Makefile
         XUPNP_Stub/Makefile
         EPONHAL_Stub/Makefile
         mso_mgmt_hal_stub/Makefile
         BLEHAL_Stub/Makefile
         RBUS_Stub/Makefile
         DSLHAL_Stub/Makefile
         FWUpgradeHAL_Stub/Makefile
         TELCOVOICEMgrHal_Stub/Makefile])
AC_OUTPUT

