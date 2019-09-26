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

SCRIPT_PATH=$TDK_PATH/script/
LOG_PATH=$TDK_PATH/
LOGFILE=output_json_parser_details.log
STREAMING_IP=$1
BASE_URL=$2
echo "Base Url : " $BASE_URL
echo "Streaming IP :" $STREAMING_IP

#check for xdiscovery.conf file
cmd=`cat $XDISCOVERY_PATH/xdiscovery.conf|grep outputJsonFile=|grep -v "#"|awk -F "=" '{print $2}'`
if [ $? == 0 ] && [ "$cmd" != "" ]; then
        echo $cmd
        echo "output.json location has parsed successfully"
        echo SUCCESS > $LOG_PATH/$LOGFILE
else
	echo $cmd
        echo "Not able to parse xdiscovery.conf "
        echo FAILURE > $LOG_PATH/$LOGFILE
        exit 1
fi

if [ "$STREAMING_IP" == "mdvr" ]; then
	Parse_out=`cat $cmd |grep playbackUrl|cut -f2- -d":"|cut -f1 -d "&"|cut -f2 -d "\""|head -1`
        if [ $? == 0 ] && [ "$Parse_out" != "" ]; then
        	echo $Parse_out
                echo "Got proper play url from output.json"
                echo SUCCESS > $LOG_PATH/$LOGFILE
        else
        	echo $Parse_out
                echo "Not able to parse output.json "
                echo FAILURE > $LOG_PATH/$LOGFILE
                exit 1
        fi
else 
                                                                                                                                        
#Parse the play url from output.json
Parse_out=`cat $cmd |grep playbackUrl|cut -f2- -d":"|cut -f1 -d "&"|grep $STREAMING_IP|cut -f2 -d "\""`
if [ $? == 0 ] && [ "$Parse_out" != "" ]; then
	echo $Parse_out
        echo "Got proper play url from output.json"
        echo SUCCESS > $LOG_PATH/$LOGFILE
else
	Parse_out=`cat $cmd |grep playbackUrl|cut -f2- -d":"|cut -f1 -d "&"|grep 127.0.0.1|cut -f2 -d "\""`
        if [ $? == 0 ] && [ "$Parse_out" != "" ]; then
        	echo $Parse_out
                echo "Got proper play url from output.json"
                echo SUCCESS > $LOG_PATH/$LOGFILE
        else
        	echo $Parse_out
                echo "Not able to parse output.json "
                echo FAILURE > $LOG_PATH/$LOGFILE
                exit 1
        fi
 fi
fi                                                                                                                                             
#parse the base URL
Parse_base=`echo $BASE_URL |cut -f2 -d "?"`
if [ $? == 0 ] && [ "$Parse_base" != "" ]; then
	echo $Parse_base
	echo "Parsed the base url properly"
        echo SUCCESS > $LOG_PATH/$LOGFILE
else
        echo $Parse_base
        echo "Not able to parse base url "
        echo FAILURE > $LOG_PATH/$LOGFILE
        exit 1
fi
                                                                                                                                                                                                                                                                                                                        
#Concat the final url
final_url=$Parse_out"&"$Parse_base
echo $final_url > $LOG_PATH/$LOGFILE



                                                                                                                                                                                                        
