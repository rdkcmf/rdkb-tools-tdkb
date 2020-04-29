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

TDK_AGENT_RDM_PATH=/tmp/tdk-b-dl/usr/ccsp/tdk/
TDK_AGENT_PATH=/usr/ccsp/tdk/
TDK_AGENT_LIB_PATH=/tmp/tdk-b-dl/usr/lib/
DNLD_SCRIPT=/etc/rdm/downloadMgr.sh
LOG_FILE=/rdklogs/logs/tdkb_launcher.log
APP_NAME=tdk-b-dl
VALIDATION_METHOD=openssl
PKG_EXT=ipk

if [ -f /version.txt ]; then
        echo "version.txt exists" >> $LOG_FILE
        imgname=`cat /version.txt | grep -i 'imagename'`
        echo $imgname >> $LOG_FILE
        flag=`echo $imgname|awk '{print match($0,"TDK")}'`;
        if [ $flag -gt 0 ]; then
                if [ -f "$TDK_AGENT_PATH/StartTDK.sh" ]; then
                        echo "Found TDK-B Image but not RDM enabled" >> $LOG_FILE
                        echo "Invoking StartTDK.sh from $TDK_AGENT_PATH" >> $LOG_FILE
                        sh $TDK_AGENT_PATH/StartTDK.sh

                elif [ -f "$TDK_AGENT_RDM_PATH/StartTDK.sh" ]; then
                        echo "Found RDM enabled TDK-B Image" >> $LOG_FILE
                        echo "Invoking StartTDK.sh from $TDK_AGENT_RDM_PATH" >> $LOG_FILE
                        sh $TDK_AGENT_RDM_PATH/StartTDK.sh

                else
                        count=0
                        while [ "$count" -lt "12" ]
                        do
                                echo "Loop Count: $count" >> $LOG_FILE
                                if [ -f /tmp/.xconfssrdownloadurl ]; then
                                        echo "File /tmp/.xconfssrdownloadurl is present...." >> $LOG_FILE
                                        url_status=`cat /tmp/.xconfssrdownloadurl`
                                        if [[ $url_status =~ .*https.* ]]; then
                                                echo "URL found in /tmp/.xconfssrdownloadurl...." >> $LOG_FILE
                                                break
                                        else
                                                echo "URL not found in /tmp/.xconfssrdownloadurl...." >> $LOG_FILE
                                                echo "Waiting for another 60 seconds!!!!!!"
                                                sleep 60
                                        fi
                                else
                                        echo "File /tmp/.xconfssrdownloadurl is not present...." >> $LOG_FILE
                                        sleep 60
                                fi
                                count=`expr $count + 1`
                        done

                        echo "Download the TDK-B package" >> $LOG_FILE
                        sh $DNLD_SCRIPT $APP_NAME "" $VALIDATION_METHOD $PKG_EXT ""
                        DNLD_RES=$?
                        echo "TDK-B package download result is: $DNLD_RES" >> $LOG_FILE

                        if [ $DNLD_RES -eq 0 ]; then
                                echo "TDK-B package download is successful" >> $LOG_FILE
                                export PATH=$PATH:$TDK_AGENT_RDM_PATH
                                export LD_LIBRARY_PATH=/lib:/usr/lib:$TDK_AGENT_LIB_PATH
                                if [ -f "$TDK_AGENT_RDM_PATH/StartTDK.sh" ]; then
                                       echo "Invoking StartTDK.sh from $TDK_AGENT_RDM_PATH" >> $LOG_FILE
                                       sh $TDK_AGENT_RDM_PATH/StartTDK.sh
                                else
                                        echo "TDK-B startup script is not available under $TDK_AGENT_RDM_PATH" >> $LOG_FILE
                                fi
                        else
                                echo "TDK-B Download failed!!! result is: $DNLD_RES" >> $LOG_FILE
                        fi
                fi
        else
                echo "Current image is not TDK-B Image" >> $LOG_FILE
        fi
else
        echo "version.txt file is missing" >> $LOG_FILE
fi

