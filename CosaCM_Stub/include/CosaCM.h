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

#ifndef __CosaCM_STUB_H__
#define __CosaCM_STUB_H__
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
#define IN
#define OUT

#define TEST_SUCCESS true
#define TEST_FAILURE false
#define MAX_PARAM_SIZE	100
#define MAX_PARAM_NAMES_ARRAY	1000

class RDKTestAgent;

class CosaCM : public RDKTestStubInterface, public AbstractServer<CosaCM>
{
	public:

                 CosaCM(TcpSocketServer &ptrRpcServer) : AbstractServer <CosaCM>(ptrRpcServer)
                {
                  this->bindAndAddMethod(Procedure("CosaCM_GetResetCount", PARAMS_BY_NAME,JSON_STRING, "handleType",JSON_INTEGER,"bufferType",JSON_INTEGER,"resetType",JSON_STRING,NULL), &CosaCM::CosaCM_GetResetCount);
                  this->bindAndAddMethod(Procedure("CosaCM_GetUpstreamChannelId", PARAMS_BY_NAME,JSON_STRING,"handleType",JSON_INTEGER,NULL), &CosaCM::CosaCM_GetUpstreamChannelId);
                  this->bindAndAddMethod(Procedure("CosaCM_SetUpstreamChannelId", PARAMS_BY_NAME,JSON_STRING,"handleType", JSON_INTEGER,"channelId", JSON_INTEGER,NULL), &CosaCM::CosaCM_SetUpstreamChannelId);
                  this->bindAndAddMethod(Procedure("CosaCM_GetStartDSFrequency", PARAMS_BY_NAME,JSON_STRING,"handleType",JSON_INTEGER,NULL), &CosaCM::CosaCM_GetStartDSFrequency);
                  this->bindAndAddMethod(Procedure("CosaCM_SetStartDSFrequency", PARAMS_BY_NAME,JSON_STRING,"handleType", JSON_INTEGER,"frequency",JSON_INTEGER,NULL), &CosaCM::CosaCM_SetStartDSFrequency);
                  this->bindAndAddMethod(Procedure("CosaCM_GetProvType", PARAMS_BY_NAME,JSON_STRING,"handleType", JSON_INTEGER,"bufferType", JSON_INTEGER,NULL), &CosaCM::CosaCM_GetProvType);
                  this->bindAndAddMethod(Procedure("CosaCM_GetIPv6DHCPInfo", PARAMS_BY_NAME,JSON_STRING,"handleType", JSON_INTEGER,"bufferType", JSON_INTEGER,NULL), &CosaCM::CosaCM_GetIPv6DHCPInfo);
                  this->bindAndAddMethod(Procedure("COSACM_GetMarket", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetMarket);
                  this->bindAndAddMethod(Procedure("COSACM_SetMDDIPOverride", PARAMS_BY_NAME, JSON_STRING,"value", JSON_STRING,NULL), &CosaCM::COSACM_SetMDDIPOverride);
                  this->bindAndAddMethod(Procedure("COSACM_GetMDDIPOverride", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetMDDIPOverride);
                  this->bindAndAddMethod(Procedure("COSACM_GetCMCert", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetCMCert);
                  this->bindAndAddMethod(Procedure("COSACM_GetCMErrorCodewords", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetCMErrorCodewords);
                  this->bindAndAddMethod(Procedure("COSACM_GetCMCertStatus", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetCMCertStatus);
                  this->bindAndAddMethod(Procedure("COSACM_GetCPEList", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetCPEList);
                  this->bindAndAddMethod(Procedure("COSACM_GetMarket_ArgMemory_unalloc", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetMarket_ArgMemory_unalloc);
                  this->bindAndAddMethod(Procedure("COSACM_SetMDDIPOverride_ArgMemory_unalloc", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_SetMDDIPOverride_ArgMemory_unalloc);
                  this->bindAndAddMethod(Procedure("COSACM_GetMDDIPOverride_ArgMemory_unalloc", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetMDDIPOverride_ArgMemory_unalloc);
                  this->bindAndAddMethod(Procedure("COSACM_GetCMCert_ArgMemory_unalloc", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetCMCert_ArgMemory_unalloc);
                  this->bindAndAddMethod(Procedure("COSACM_GetCMErrorCodewords_InvalidArg", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetCMErrorCodewords_InvalidArg);
                  this->bindAndAddMethod(Procedure("COSACM_GetCMCertStatus_InvalidArg", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetCMCertStatus_InvalidArg);
                  this->bindAndAddMethod(Procedure("COSACM_GetCPEList_InvalidArg", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_GetCPEList_InvalidArg);
                  this->bindAndAddMethod(Procedure("CosaCM_GetStatus", PARAMS_BY_NAME,JSON_STRING,"handleType", JSON_INTEGER,"Value",JSON_INTEGER,NULL), &CosaCM::CosaCM_GetStatus);
                  this->bindAndAddMethod(Procedure("CosaCM_GetLoopDiagnosticsStart", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,"boolValue", JSON_INTEGER,NULL), &CosaCM::CosaCM_GetLoopDiagnosticsStart);
                  this->bindAndAddMethod(Procedure("CosaCM_GetLoopDiagnosticsDetails", PARAMS_BY_NAME, JSON_STRING,"handleType", JSON_INTEGER,"bufferType", JSON_INTEGER,NULL), &CosaCM::CosaCM_GetLoopDiagnosticsDetails);
                  this->bindAndAddMethod(Procedure("CosaCM_GetTelephonyRegistrationStatus", PARAMS_BY_NAME,JSON_STRING,"handleType", JSON_INTEGER,"bufferType", JSON_INTEGER,NULL), &CosaCM::CosaCM_GetTelephonyRegistrationStatus);
                  this->bindAndAddMethod(Procedure("CosaCM_GetTelephonyDHCPStatus", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,"Value", JSON_INTEGER,NULL), &CosaCM::CosaCM_GetTelephonyDHCPStatus);
                  this->bindAndAddMethod(Procedure("CosaCM_GetTelephonyTftpStatus", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,"Value", JSON_INTEGER,NULL), &CosaCM::CosaCM_GetTelephonyTftpStatus);
                  this->bindAndAddMethod(Procedure("CosaCM_SetLoopDiagnosticsStart", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,"boolValue", JSON_INTEGER,NULL), &CosaCM::CosaCM_SetLoopDiagnosticsStart);
                  this->bindAndAddMethod(Procedure("COSACM_GetDHCPInfo", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,"bufferType", JSON_INTEGER,NULL), &CosaCM::COSACM_GetDHCPInfo);
                  this->bindAndAddMethod(Procedure("COSACM_GetDOCSISInfo", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,"bufferType", JSON_INTEGER,NULL), &CosaCM::COSACM_GetDOCSISInfo);
                  this->bindAndAddMethod(Procedure("COSACM_GetLog", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,"bufferType", JSON_INTEGER,NULL), &CosaCM::COSACM_GetLog);
                  this->bindAndAddMethod(Procedure("COSACM_SetLog", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,"bufferType", JSON_INTEGER,NULL), &CosaCM::COSACM_SetLog);
                  this->bindAndAddMethod(Procedure("COSACM_GetDocsisLog", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,"bufferType", JSON_INTEGER,NULL), &CosaCM::COSACM_GetDocsisLog);
                  this->bindAndAddMethod(Procedure("COSACM_GetDownstreamChannel", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,"bufferType", JSON_INTEGER,NULL), &CosaCM::COSACM_GetDownstreamChannel);
                  this->bindAndAddMethod(Procedure("COSACM_GetUpstreamChannel", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,"bufferType", JSON_INTEGER,NULL), &CosaCM::COSACM_GetUpstreamChannel);
                  this->bindAndAddMethod(Procedure("COSACM_CableModemCreate", PARAMS_BY_NAME, JSON_STRING,NULL), &CosaCM::COSACM_CableModemCreate);
                  this->bindAndAddMethod(Procedure("COSACM_CableModemInitialize", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,NULL), &CosaCM::COSACM_CableModemInitialize);
                  this->bindAndAddMethod(Procedure("COSACM_CableModemRemove", PARAMS_BY_NAME,JSON_STRING ,"handleType", JSON_INTEGER,NULL), &CosaCM::COSACM_CableModemRemove);
                  this->bindAndAddMethod(Procedure("CMHal_GetCharValues", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CosaCM::CMHal_GetCharValues);
                  this->bindAndAddMethod(Procedure("CMHal_GetUlongValues", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CosaCM::CMHal_GetUlongValues);
                  this->bindAndAddMethod(Procedure("CMHal_GetStructValues", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,NULL), &CosaCM::CMHal_GetStructValues);
		}
        /*Ctor*/
//		CosaCM ();

		/*inherited functions*/
		bool initialize(IN const char* szVersion);

		bool cleanup(IN const char* szVersion);
		std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

        /*CosaCM Stub Wrapper functions*/
		void CosaCM_GetResetCount(IN const Json::Value& req, OUT Json::Value& response);
		void CosaCM_GetUpstreamChannelId(IN const Json::Value& req, OUT Json::Value& response);
		void CosaCM_SetUpstreamChannelId(IN const Json::Value& req, OUT Json::Value& response);
		void CosaCM_GetStartDSFrequency(IN const Json::Value& req, OUT Json::Value& response);
       		void CosaCM_SetStartDSFrequency(IN const Json::Value& req, OUT Json::Value& response);
		void CosaCM_GetProvType(IN const Json::Value& req, OUT Json::Value& response);
                void CosaCM_GetIPv6DHCPInfo(IN const Json::Value& req, OUT Json::Value& response);
                void CosaCM_GetStatus(IN const Json::Value& req, OUT Json::Value& response);
                void CosaCM_GetLoopDiagnosticsStart(IN const Json::Value& req, OUT Json::Value& response);
                void CosaCM_GetLoopDiagnosticsDetails(IN const Json::Value& req, OUT Json::Value& response);
                void CosaCM_GetTelephonyRegistrationStatus(IN const Json::Value& req, OUT Json::Value& response);
                void CosaCM_GetTelephonyTftpStatus(IN const Json::Value& req, OUT Json::Value& response);
                void CosaCM_GetTelephonyDHCPStatus(IN const Json::Value& req, OUT Json::Value& response);
                void CosaCM_SetLoopDiagnosticsStart(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetDHCPInfo(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetDOCSISInfo(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetLog(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_SetLog(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetDocsisLog(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetDownstreamChannel(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetUpstreamChannel(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_CableModemCreate(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_CableModemInitialize(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_CableModemRemove(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetMarket_ArgMemory_unalloc(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_SetMDDIPOverride_ArgMemory_unalloc(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetMDDIPOverride_ArgMemory_unalloc(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetCMCert_ArgMemory_unalloc(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetCMErrorCodewords_InvalidArg(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetCMCertStatus_InvalidArg(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetCPEList_InvalidArg(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetMarket(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_SetMDDIPOverride(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetMDDIPOverride(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetCMCert(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetCMErrorCodewords(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetCMCertStatus(IN const Json::Value& req, OUT Json::Value& response);
                void COSACM_GetCPEList(IN const Json::Value& req, OUT Json::Value& response);
                void CMHal_GetCharValues(IN const Json::Value& req, OUT Json::Value& response);
                void CMHal_GetUlongValues(IN const Json::Value& req, OUT Json::Value& response);
                void CMHal_GetStructValues(IN const Json::Value& req, OUT Json::Value& response);

};
#endif //__CosaCM_STUB_H__
