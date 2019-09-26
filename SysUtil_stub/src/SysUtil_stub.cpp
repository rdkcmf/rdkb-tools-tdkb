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

#include "SysUtil_stub.h"
#include "ssp_tdk_wrp.h"

/* To provide external linkage to C Functions defined in TDKB Component folder */
extern "C"
{
    int ssp_register(bool);
};

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Descrption    : testmodulepre_requisites will  be used for setting the
 *                pre-requisites that are necessary for this component
 *
 *****************************************************************************/
std::string SysUtilAgent::testmodulepre_requisites()
{
    int returnValue = 0;
    int bStart = 1;
    returnValue = ssp_register(bStart);

    if(0 != returnValue)
    {
        DEBUG_PRINT(DEBUG_TRACE,"\n testmodulepre_requisites --->Error invoking TDK Agent in DUT !!! \n");
        return "TEST_FAILURE";
    }

    return "SUCCESS";
}

/***************************************************************************
 *Function name : testmodulepost_requisites
 *Descrption    : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/
bool SysUtilAgent::testmodulepost_requisites()
{
        return true;
}

/**************************************************************************
Function name : SysUtilAgent::initialize

Arguments     : Input arguments are Version string and SysUtilAgent obj ptr

Description   : Registering all the wrapper functions with the agent for using these functions in the script
 ***************************************************************************/
bool SysUtilAgent::initialize(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "SysUtilAgent Initialize\n");

        return TEST_SUCCESS;
}

/**************************************************************************
Function name : SysUtilAgent::SysUtilAgent_ExecuteCmd

Arguments     : Input arguments are json request object and json response object

Description   : This method queries for the parameter requested through curl and returns the value.
***************************************************************************/
void SysUtilAgent::SysUtilAgent_ExecuteCmd(IN const Json::Value& req, OUT Json::Value& response)
{
        DEBUG_PRINT(DEBUG_TRACE, "SysUtilAgent_ExecuteCmd -->Entry\n");

        string fileinfo = req["command"].asCString();

        FILE *fp = NULL;
        char readRespBuff[BUFF_LENGTH] = { '\0' };

        /*Frame the command  */
        string path = "";
        path.append(fileinfo);

        DEBUG_PRINT(DEBUG_TRACE, "Command Request Framed: %s\n",path.c_str());

        fp = popen(path.c_str(),"r");

        /*Check for popen failure*/
        if(fp == NULL)
        {
                response["result"] = "FAILURE";
                response["details"] = "popen() failure";
                DEBUG_PRINT(DEBUG_ERROR, "popen() failure\n");

                return;
        }

        /*copy the response to a buffer */
        while(fgets(readRespBuff,sizeof(readRespBuff),fp) != NULL)
        {
                DEBUG_PRINT(DEBUG_TRACE, "Command Response:\n");
                cout<<readRespBuff<<endl;
        }

        pclose(fp);

        string respResult(readRespBuff);
        DEBUG_PRINT(DEBUG_TRACE, "\n\nResponse: %s\n",respResult.c_str());
        response["result"] = "SUCCESS";
        response["details"] = respResult;
        DEBUG_PRINT(DEBUG_LOG, "Execution success\n");
        DEBUG_PRINT(DEBUG_TRACE, "SysUtilAgent_ExecuteCmd -->Exit\n");
        return;

}

/**************************************************************************
Function Name   : CreateObject

Arguments       : NULL

Description     : This function is used to create a new object of the class "SysUtilAgent".
 **************************************************************************/

extern "C" SysUtilAgent* CreateObject(TcpSocketServer &ptrtcpServer)
{
        DEBUG_PRINT(DEBUG_TRACE, "Creating SysUtil Agent Object\n");

        return new SysUtilAgent(ptrtcpServer);
}

/**************************************************************************
Function Name   : cleanup

Arguments       : NULL

Description     : This function will be used to the close things cleanly.
 **************************************************************************/
bool SysUtilAgent::cleanup(IN const char* szVersion)
{
        DEBUG_PRINT(DEBUG_TRACE, "cleaningup\n");

        return TEST_SUCCESS;
}

/**************************************************************************
Function Name : DestroyObject

Arguments     : Input argument is SysUtilAgent Object

Description   : This function will be used to destory the SysUtilAgent object.
 **************************************************************************/
extern "C" void DestroyObject(SysUtilAgent *stubobj)
{
        DEBUG_PRINT(DEBUG_TRACE, "Destroying SysUtilAgent object\n");
        delete stubobj;
}

