/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2016 RDK Management
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

#ifndef __RDK_TEST_AGENT_INTF__
#define __RDK_TEST_AGENT_INTF__

/* System Includes */
#include <json/json.h>
#include <jsonrpccpp/server.h>
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>
#include <jsonrpccpp/client.h>
#include <jsonrpccpp/client/connectors/tcpsocketclient.h>

#include <iostream>
#include <time.h>
#include <stdio.h>
#include <string.h>
#include <sys/time.h>
#include <stdlib.h>

using namespace jsonrpc;

/* debug message */
typedef enum _DEBUG_LEVEL_
{
	DEBUG_NONE,
	DEBUG_ERROR,
	DEBUG_LOG,
	DEBUG_TRACE
}_DEBUG_LEVEL_t;

#ifdef DEBUG_LEVEL_TRACE
#define DEBUG_ENABLE 3
#endif
#ifdef DEBUG_LEVEL_LOG
#define DEBUG_ENABLE 2
#endif
#ifdef DEBUG_LEVEL_ERROR
#define DEBUG_ENABLE 1
#endif
#ifndef DEBUG_ENABLE
#define DEBUG_ENABLE 1
#endif

#define DEBUG_PRINT(eDebugLevel,pui8Debugmsg...)\
        do{\
            if(eDebugLevel <= DEBUG_ENABLE)\
            {\
                char buffer[30];\
                struct timeval tv;\
                time_t curtime;\
                gettimeofday(&tv, NULL); \
                curtime=tv.tv_sec;\
                strftime(buffer,30,"%m-%d-%Y %T.",localtime(&curtime));\
                fprintf(stdout,"\n%s%ld [%s():%d] ",buffer,tv.tv_usec,__FUNCTION__,__LINE__);\
                fprintf(stdout,pui8Debugmsg);\
                fflush(stdout);\
            }\
        }while(0)


/**************************************************************************************
Description   : This Class provides interface for the module to enable RPC mechanism.

 **************************************************************************************/
class RDKTestAgent : public AbstractServer<RDKTestAgent>
{

	public:
		/* Constructor */
               RDKTestAgent(TcpSocketServer &ptrRpcServer) : AbstractServer <RDKTestAgent>(ptrRpcServer)
               {

               }
		virtual ~RDKTestAgent(){}

}; /* End of RDKTestAgent*/

#endif  //__RDK_TEST_AGENT_INTF__


