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
ACLOCAL_AMFLAGS = -Im4 --install
AM_CPPFLAGS = -c -Wall -shared ${COPTS} -fPIC
AM_CXXFLAGS = -I${top_srcdir}/SNMP_PA_Stub/include -I${top_srcdir}/agent/include -I${top_srcdir}/tdkb_lib/include
lib_LTLIBRARIES = libsnmp_pastub.la
libsnmp_pastub_la_SOURCES = src/SNMPProtocolAgent.cpp
libsnmp_pastub_la_DEPENDENCIES= ${top_builddir}/tdkb_lib/.libs/libtdkagentssp.la
libsnmp_pastub_la_LIBADD =  $(libSNMP_PAstub_la_DEPENDENCIES)
libsnmp_pastub_la_includedir = ${includedir}
libsnmp_pastub_la_include_HEADERS = ${top_srcdir}/SNMP_PA_Stub/include/SNMPProtocolAgent.h
