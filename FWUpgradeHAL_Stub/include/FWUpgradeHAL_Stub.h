/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2021 RDK Management
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

#ifndef __FWUPGRADEHAL_STUB_H__
#define __FWUPGRADEHAL_STUB_H__
#include <json/json.h>
#include <unistd.h>
#include <string.h>
#include <dlfcn.h>
#include <stdlib.h>
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>
#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include <sys/types.h>
#include <sys/wait.h>
#include <fstream>
#include <sstream>
#include "ssp_tdk_fwupgradehal_wrp.h"
#define IN
#define OUT
#define TEST_SUCCESS true
#define TEST_FAILURE false


class RDKTestAgent;

class FWUPGRADEHAL : public RDKTestStubInterface,  public AbstractServer<FWUPGRADEHAL>
{
        public:
                FWUPGRADEHAL(TcpSocketServer &ptrRpcServer) : AbstractServer <FWUPGRADEHAL>(ptrRpcServer)
                {
                    this->bindAndAddMethod(Procedure("FWUPGRADEHAL_GetParamUlongValue", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,"paramType", JSON_STRING,NULL), &FWUPGRADEHAL::FWUPGRADEHAL_GetParamUlongValue);
                    this->bindAndAddMethod(Procedure("FWUPGRADEHAL_Set_Download_Interface", PARAMS_BY_NAME, JSON_STRING,"interface", JSON_INTEGER,NULL), &FWUPGRADEHAL::FWUPGRADEHAL_Set_Download_Interface);
                    this->bindAndAddMethod(Procedure("FWUPGRADEHAL_Download", PARAMS_BY_NAME, JSON_STRING,NULL), &FWUPGRADEHAL::FWUPGRADEHAL_Download);
                    this->bindAndAddMethod(Procedure("FWUPGRADEHAL_Reboot_Now", PARAMS_BY_NAME, JSON_STRING,NULL), &FWUPGRADEHAL::FWUPGRADEHAL_Reboot_Now);
                    this->bindAndAddMethod(Procedure("FWUPGRADEHAL_Get_Download_Url", PARAMS_BY_NAME, JSON_STRING,NULL), &FWUPGRADEHAL::FWUPGRADEHAL_Get_Download_Url);
                    this->bindAndAddMethod(Procedure("FWUPGRADEHAL_Set_Download_Url", PARAMS_BY_NAME, JSON_STRING,"URL", JSON_STRING,"filename", JSON_STRING,NULL), &FWUPGRADEHAL::FWUPGRADEHAL_Set_Download_Url);
                    this->bindAndAddMethod(Procedure("FWUPGRADEHAL_Update_And_FactoryReset", PARAMS_BY_NAME, JSON_STRING,"URL", JSON_STRING, "imageName", JSON_STRING, NULL), &FWUPGRADEHAL::FWUPGRADEHAL_Update_And_FactoryReset);
                 }
        /*inherited functions*/
        bool initialize(IN const char* szVersion);
        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();
 
        /*FWUPGRADEHAL Stub Wrapper functions*/
        void FWUPGRADEHAL_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response);
        void FWUPGRADEHAL_Set_Download_Interface(IN const Json::Value& req, OUT Json::Value& response);
        void FWUPGRADEHAL_Download(IN const Json::Value& req, OUT Json::Value& response);
        void FWUPGRADEHAL_Reboot_Now(IN const Json::Value& req, OUT Json::Value& response);
        void FWUPGRADEHAL_Get_Download_Url(IN const Json::Value& req, OUT Json::Value& response);
        void FWUPGRADEHAL_Set_Download_Url(IN const Json::Value& req, OUT Json::Value& response);
        void FWUPGRADEHAL_Update_And_FactoryReset(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__FWUPGRADEHAL_STUB_H__


