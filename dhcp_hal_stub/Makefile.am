#****************************************************************************
#Copyright 2016-2017 Intel Corporation

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#******************************************************************************

ACLOCAL_AMFLAGS = -Im4 --install
AM_CPPFLAGS = -fPIC ${COPTS}
AM_CXXFLAGS = -I${PKG_CONFIG_SYSROOT_DIR}$(includedir) \
	      -I${PKG_CONFIG_SYSROOT_DIR}$(includedir)/ccsp \
	      -I${top_srcdir}/dhcp_hal_stub/include -I${top_srcdir}/agent/include -I${top_srcdir}/tdkb_lib/include \
	      -Wall -Werror

lib_LTLIBRARIES = libdhcpstub.la
libdhcpstub_la_SOURCES = src/dhcp_stub_hal.cpp
libdhcpstub_la_LIBADD = -lapi_dhcpv4c
libdhcpstub_la_DEPENDENCIES= ${top_builddir}/tdkb_lib/.libs/libtdkagentssp.la
libdhcpstub_la_LIBADD =  $(libdhcpstub_la_DEPENDENCIES)
libdhcpstub_la_includedir = ${includedir}
libdhcpstub_la_include_HEADERS = ${top_srcdir}/dhcp_hal_stub/include/dhcp_stub_hal.h
