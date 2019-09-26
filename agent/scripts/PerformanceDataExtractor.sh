#!/bin/sh
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

export PATH=$PATH:/usr/local/bin:/usr/local/lib:/usr/local/lib/sa

cd $TDK_PATH

ITERATION=`cat sysStatAvg.log | awk ' /ITERATION/ { print $0 }' | wc -l`
TOTAL_LINES=`cat sysStatAvg.log | wc -l`
LINE_COUNT=$(($TOTAL_LINES / $ITERATION))


while read line
do

    sed -e '/ITERATION/,$d' sysStatAvg.log > performance.temp

    cat performance.temp | awk 'BEGIN { RS="" ; FS="\n" } { print $2 }' | awk '{print $8}' >> cpu.log

    cat performance.temp  | awk 'BEGIN { RS="" ; FS="\n" } { print $4 }' | awk '{print$2,$3,$4}' >> memused.log

    sed -e '1,'$LINE_COUNT'd' < sysStatAvg.log > temp

    mv temp sysStatAvg.log

done < sysStatAvg.log

echo "Performance data Extracted"
