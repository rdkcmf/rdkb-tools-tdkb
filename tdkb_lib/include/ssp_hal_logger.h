/*
 * Copyright 2016-2017 Intel Corporation
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
#ifndef  _SSP_HAL_LOGGER_
#define  _SSP_HAL_LOGGER_
#include <time.h>
#include <stdio.h>
#include <string.h>
#include <sys/time.h>
#include <stdlib.h>

/* debug message */
typedef enum _DEBUG_LEVEL_
{
        DEBUG_NONE,
        DEBUG_ERROR,
        DEBUG_LOG,
        DEBUG_TRACE
}_DEBUG_LEVEL_t;

#define MAX_BUFFER_LENGTH 64

#ifndef RETURN_OK
#define RETURN_OK 0
#endif

#ifndef RETURN_ERR
#define RETURN_ERR 1
#endif

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
                char buffer[MAX_BUFFER_LENGTH];\
                struct timeval tv;\
                time_t curtime;\
                gettimeofday(&tv, NULL); \
                curtime=tv.tv_sec;\
                strftime(buffer,MAX_BUFFER_LENGTH,"%m-%d-%Y %T.",localtime(&curtime));\
                fprintf(stdout,"\n%s%ld [%s():%d] ",buffer,tv.tv_usec,__FUNCTION__,__LINE__);\
                fprintf(stdout,pui8Debugmsg);\
                fflush(stdout);\
            }\
        }while(0)

#define CHECK_PARAM_AND_RET(x)  if ((x) == NULL) \
{ \
      DEBUG_PRINT(DEBUG_ERROR,"NULL Value passed to function:: %s:%d\n", __func__, __LINE__); \
      return RETURN_ERR; \
}

#endif
