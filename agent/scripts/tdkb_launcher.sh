#!/bin/sh

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

TDK_AGENT_RDM_PATH=/tmp/TDK/usr/ccsp/tdk/
TDK_AGENT_PATH=/usr/ccsp/tdk/

if [ -f "$TDK_AGENT_PATH/StartTDK.sh" ]; then
        echo "Found TDK-B Image but not RDM enabled"
        echo "Invoking StartTDK.sh from $TDK_AGENT_PATH"
        sh $TDK_AGENT_PATH/StartTDK.sh

elif [ -f "$TDK_AGENT_RDM_PATH/StartTDK.sh" ]; then
        echo "Found RDM enabled TDK-B/RDK-B Image"
        echo "Invoking StartTDK.sh from $TDK_AGENT_RDM_PATH"
        sh $TDK_AGENT_RDM_PATH/StartTDK.sh
else
	echo "TDK-B startup script is not available under $TDK_AGENT_PATH or $TDK_AGENT_RDM_PATH"
	echo "TDK-B Binaries are not available!!!! Failed to start TDK!!!!"
fi

