##########################################################################
# Copyright 2016-2017 Intel Corporation
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
AM_CPPFLAGS = -fPIC ${COPTS}
AM_CXXFLAGS = -I${PKG_CONFIG_SYSROOT_DIR}$(includedir) \
	      -I${PKG_CONFIG_SYSROOT_DIR}$(includedir)/ccsp \
	      -I${top_srcdir}/ethsw_hal_stub/include -I${top_srcdir}/agent/include -I${top_srcdir}/tdkb_lib/include \
	      -Wall -Werror

lib_LTLIBRARIES = libhalethswstub.la
libhalethswstub_la_SOURCES = src/ethsw_stub_hal.cpp
libhalethswstub_la_LIBADD = -lhal_ethsw
libhalethswstub_la_DEPENDENCIES= ${top_builddir}/tdkb_lib/.libs/libtdkagentssp.la
libhalethswstub_la_LIBADD =  $(libhalethswstub_la_DEPENDENCIES)
libhalethswstub_la_includedir = ${includedir}
libhalethswstub_la_include_HEADERS = ${top_srcdir}/ethsw_hal_stub/include/ethsw_stub_hal.h
