/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
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

#ifndef __CMHAL_STUB_H__
#define __CMHAL_STUB_H__
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
#include "ssp_tdk_cmhal_wrp.h"
#define IN
#define OUT

#define TEST_SUCCESS true
#define TEST_FAILURE false
#define DOCSIS_EVENT_LOG_SIZE 50

class RDKTestAgent;

class CMHAL : public RDKTestStubInterface,  public AbstractServer<CMHAL>
{
        public:

		CMHAL(TcpSocketServer &ptrRpcServer) : AbstractServer <CMHAL>(ptrRpcServer)
                {
                  this->bindAndAddMethod(Procedure("CMHAL_GetParamCharValue", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,"paramType", JSON_STRING,NULL), &CMHAL::CMHAL_GetParamCharValue);
                  this->bindAndAddMethod(Procedure("CMHAL_GetParamUlongValue", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,"paramType", JSON_STRING,NULL), &CMHAL::CMHAL_GetParamUlongValue);
		  this->bindAndAddMethod(Procedure("CMHAL_GetErrorCodeWords", PARAMS_BY_NAME, JSON_STRING,"flag", JSON_INTEGER,NULL), &CMHAL::CMHAL_GetErrorCodeWords);
                  this->bindAndAddMethod(Procedure("CMHAL_Init", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CMHAL::CMHAL_Init);
		  this->bindAndAddMethod(Procedure("CMHAL_GetDocsisEventLogItems", PARAMS_BY_NAME, JSON_STRING,"flag", JSON_INTEGER,NULL), &CMHAL::CMHAL_GetDocsisEventLogItems);
		  this->bindAndAddMethod(Procedure("CMHAL_SetLEDFlashStatus", PARAMS_BY_NAME, JSON_STRING,"LEDFlash", JSON_STRING,NULL), &CMHAL::CMHAL_SetLEDFlashStatus);
		  this->bindAndAddMethod(Procedure("CMHAL_ClearDocsisEventLog", PARAMS_BY_NAME, JSON_STRING,NULL), &CMHAL::CMHAL_ClearDocsisEventLog);
                  this->bindAndAddMethod(Procedure("CMHAL_GetCPEList", PARAMS_BY_NAME, JSON_STRING,"flag", JSON_INTEGER,"lanMode",JSON_STRING,NULL), &CMHAL::CMHAL_GetCPEList);
                  this->bindAndAddMethod(Procedure("CMHAL_SetMddIpModeOverride", PARAMS_BY_NAME, JSON_STRING,"value", JSON_STRING,NULL), &CMHAL::CMHAL_SetMddIpModeOverride);
                  this->bindAndAddMethod(Procedure("CMHAL_SetStartFreq", PARAMS_BY_NAME, JSON_STRING,"Value", JSON_INTEGER,NULL), &CMHAL::CMHAL_SetStartFreq);
                  this->bindAndAddMethod(Procedure("CMHAL_SetUSChannelId", PARAMS_BY_NAME, JSON_STRING,"Value", JSON_INTEGER,NULL), &CMHAL::CMHAL_SetUSChannelId);
		  this->bindAndAddMethod(Procedure("CMHAL_SetHTTP_Download_Interface", PARAMS_BY_NAME, JSON_STRING,"interface", JSON_INTEGER,NULL), &CMHAL::CMHAL_SetHTTP_Download_Interface);
                  this->bindAndAddMethod(Procedure("CMHAL_HTTP_Download", PARAMS_BY_NAME, JSON_STRING,NULL), &CMHAL::CMHAL_HTTP_Download);
                  this->bindAndAddMethod(Procedure("CMHAL_Reboot_Now", PARAMS_BY_NAME, JSON_STRING,NULL), &CMHAL::CMHAL_Reboot_Now);
                  this->bindAndAddMethod(Procedure("CMHAL_GetHTTP_Download_Url", PARAMS_BY_NAME, JSON_STRING,NULL), &CMHAL::CMHAL_GetHTTP_Download_Url);
                  this->bindAndAddMethod(Procedure("CMHAL_SetHTTP_Download_Url", PARAMS_BY_NAME, JSON_STRING,"httpURL", JSON_STRING,"filename", JSON_STRING,NULL), &CMHAL::CMHAL_SetHTTP_Download_Url);
                  this->bindAndAddMethod(Procedure("CMHAL_FWupdateAndFactoryReset", PARAMS_BY_NAME, JSON_STRING,"URL", JSON_STRING, "imageName", JSON_STRING, NULL), &CMHAL::CMHAL_FWupdateAndFactoryReset);
                  this->bindAndAddMethod(Procedure("CMHAL_GetDsOfdmChanTable", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CMHAL::CMHAL_GetDsOfdmChanTable);
                  this->bindAndAddMethod(Procedure("CMHAL_GetUsOfdmChanTable", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CMHAL::CMHAL_GetUsOfdmChanTable);
                  this->bindAndAddMethod(Procedure("CMHAL_GetStatusOfdmaUsTable", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CMHAL::CMHAL_GetStatusOfdmaUsTable);
                  this->bindAndAddMethod(Procedure("CMHAL_IsEnergyDetected", PARAMS_BY_NAME, JSON_STRING,NULL), &CMHAL::CMHAL_IsEnergyDetected);
		}

        /*inherited functions*/
        bool initialize(IN const char* szVersion);

        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();
        /*CMHAL Stub Wrapper functions*/
	void CMHAL_GetParamCharValue(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response);
	void CMHAL_GetErrorCodeWords(IN const Json::Value& req, OUT Json::Value& response);
	void CMHAL_Init(IN const Json::Value& req, OUT Json::Value& response);
	void CMHAL_GetDocsisEventLogItems(IN const Json::Value& req, OUT Json::Value& response);
	void CMHAL_SetLEDFlashStatus(IN const Json::Value& req, OUT Json::Value& response);
	void CMHAL_ClearDocsisEventLog(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_GetCPEList(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_SetMddIpModeOverride(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_SetStartFreq(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_SetUSChannelId(IN const Json::Value& req, OUT Json::Value& response);
	void CMHAL_SetHTTP_Download_Interface(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_HTTP_Download(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_Reboot_Now(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_GetHTTP_Download_Url(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_SetHTTP_Download_Url(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_FWupdateAndFactoryReset(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_GetDsOfdmChanTable(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_GetUsOfdmChanTable(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_GetStatusOfdmaUsTable(IN const Json::Value& req, OUT Json::Value& response);
        void CMHAL_IsEnergyDetected(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__CMHAL_STUB_H__
