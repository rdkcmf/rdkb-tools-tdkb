#!/bin/bash
##########################################################################
# If not stated otherwise in this file or this component's Licenses.txt
# file the following copyright and licenses apply:
#
# Copyright 2017 RDK Management
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

if [ -f "/tmp/TDK/usr/ccsp/tdk/StartTDK.sh" ]
then
    source /tmp/TDK/etc/tdk_platform.properties
else
    source /etc/tdk_platform.properties
fi

# Parse the variables inside tdk_platform.properties
parseConfigFile()
{
     eval echo \$$key
}

# Store the arguments to a variable
event=$1
key=$2

# Invoke the function based on the argument passed
case $event in
   "parseConfigFile")
        parseConfigFile;;
   *) echo "Invalid Argument passed";;
esac
