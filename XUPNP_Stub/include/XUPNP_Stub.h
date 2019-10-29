/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2019 RDK Management
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

#ifndef __XUPNP_STUB_H__
#define __XUPNP_STUB_H__

#include <json/json.h>
#include "rdkteststubintf.h"
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>
#include "rdktestagentintf.h"
#include "rdkteststubintf.h"

#define IN
#define OUT

#define TEST_SUCCESS true
#define TEST_FAILURE false

#define STR_LEN                128
#define LINE_LEN               1024
#define MAX_DATA_LEN           8192
#define XCALDEVICE             "xcal-device"
#define XDISCOVERY             "xdiscovery"
#define XDISC_LOG_FILE         "/rdklogs/logs/xdiscovery.log"
#define XCALDEV_LOG_FILE       "/rdklogs/logs/xdevice.log"
#define XDISCONFIG             "/etc/xdiscovery.conf"

using namespace std;

class RDKTestAgent;
class XUPNPStub : public RDKTestStubInterface, public AbstractServer<XUPNPStub>
{
public:
	XUPNPStub(TcpSocketServer &ptrRpcServer) : AbstractServer <XUPNPStub>(ptrRpcServer)
	{
	   this->bindAndAddMethod(Procedure("XUPNPStub_ReadXDiscOutputFile", PARAMS_BY_NAME, JSON_STRING,"paramName",JSON_STRING,NULL), &XUPNPStub::XUPNPStub_ReadXDiscOutputFile);
	   this->bindAndAddMethod(Procedure("XUPNPStub_CheckXDiscOutputFile", PARAMS_BY_NAME, JSON_STRING,NULL), &XUPNPStub::XUPNPStub_CheckXDiscOutputFile);
	}

    //Inherited functions
    bool initialize(IN const char* szVersion);

    bool cleanup(const char* szVersion);
    std::string testmodulepre_requisites();
    bool testmodulepost_requisites();

    //XXUPNPAgent Wrapper functions
    void XUPNPStub_ReadXDiscOutputFile(IN const Json::Value& req, OUT Json::Value& response);
    void XUPNPStub_CheckXDiscOutputFile(IN const Json::Value& req, OUT Json::Value& response);
};

#endif //__XUPNP_STUB_H__
