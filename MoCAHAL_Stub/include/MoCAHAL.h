/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2018 RDK Management
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
#ifndef __MoCAHAL_STUB_H__
#define __MoCAHAL_STUB_H__
#include <json/json.h>
#include <unistd.h>
#include <string.h>
#include <dlfcn.h>
#include <stdlib.h>
#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include "ssp_tdk_mocahal_wrp.h"
#include <sys/types.h>
#include <sys/wait.h>
#include <fstream>
#include <sstream>
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>
#define IN
#define OUT
#define TEST_SUCCESS true
#define TEST_FAILURE false


class RDKTestAgent;
class MoCAHAL : public RDKTestStubInterface, public AbstractServer<MoCAHAL>
{
    public:
         MoCAHAL(TcpSocketServer &ptrRpcServer) : AbstractServer <MoCAHAL>(ptrRpcServer)
                {
                  this->bindAndAddMethod(Procedure("MoCAHAL_GetIfConfig", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_GetIfConfig);
                  this->bindAndAddMethod(Procedure("MoCAHAL_SetIfConfig", PARAMS_BY_NAME, JSON_STRING, "ifIndex", JSON_INTEGER, "paramType", JSON_STRING, "privacyEnable", JSON_INTEGER, "keyPassphrase", JSON_STRING, "autoPowerEnable", JSON_INTEGER, "autoPowerRate", JSON_INTEGER, NULL), &MoCAHAL::MoCAHAL_SetIfConfig);
                  this->bindAndAddMethod(Procedure("MoCAHAL_IfGetDynamicInfo", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_IfGetDynamicInfo);
                  this->bindAndAddMethod(Procedure("MoCAHAL_IfGetStaticInfo", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_IfGetStaticInfo);
                  this->bindAndAddMethod(Procedure("MoCAHAL_IfGetStats", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_IfGetStats);
                  this->bindAndAddMethod(Procedure("MoCAHAL_GetNumAssociatedDevices", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_GetNumAssociatedDevices);
                  this->bindAndAddMethod(Procedure("MoCAHAL_IfGetExtCounter", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_IfGetExtCounter);
                  this->bindAndAddMethod(Procedure("MoCAHAL_IfGetExtAggrCounter", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_IfGetExtAggrCounter);
                  this->bindAndAddMethod(Procedure("MoCAHAL_GetMocaCPEs", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_GetMocaCPEs);
                  this->bindAndAddMethod(Procedure("MoCAHAL_GetAssociatedDevices", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "devCount", JSON_INTEGER, NULL), &MoCAHAL::MoCAHAL_GetAssociatedDevices);
		  this->bindAndAddMethod(Procedure("MoCAHAL_FreqMaskToValue", PARAMS_BY_NAME, JSON_STRING,"mask", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_FreqMaskToValue);
                  this->bindAndAddMethod(Procedure("MoCAHAL_HardwareEquipped", PARAMS_BY_NAME, JSON_STRING, NULL), &MoCAHAL::MoCAHAL_HardwareEquipped);
                  this->bindAndAddMethod(Procedure("MoCAHAL_GetFullMeshRates", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "count", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_GetFullMeshRates);
                  this->bindAndAddMethod(Procedure("MoCAHAL_GetFlowStatistics", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_GetFlowStatistics);
                  this->bindAndAddMethod(Procedure("MoCAHAL_GetResetCount", PARAMS_BY_NAME, JSON_STRING, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_GetResetCount);
                  this->bindAndAddMethod(Procedure("MoCAHAL_GetIfAcaConfig", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_GetIfAcaConfig);
                  this->bindAndAddMethod(Procedure("MoCAHAL_GetIfScmod", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_GetIfScmod);
                  this->bindAndAddMethod(Procedure("MoCAHAL_GetIfAcaStatus", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "paramType", JSON_STRING, NULL), &MoCAHAL::MoCAHAL_GetIfAcaStatus);
                  this->bindAndAddMethod(Procedure("MoCAHAL_CancelIfAca", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, NULL), &MoCAHAL::MoCAHAL_CancelIfAca);
                  this->bindAndAddMethod(Procedure("MoCAHAL_SetIfAcaConfig", PARAMS_BY_NAME, JSON_STRING,"ifIndex", JSON_INTEGER, "nodeId", JSON_INTEGER, "probeType", JSON_INTEGER, "channel", JSON_INTEGER, "reportNodes", JSON_INTEGER, "ACAStart", JSON_INTEGER, NULL), &MoCAHAL::MoCAHAL_SetIfAcaConfig);
		}

        /*inherited functions*/
        bool initialize(IN const char* szVersion);
        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

        /*MoCAHAL Stub Wrapper functions*/
        void MoCAHAL_GetIfConfig(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_SetIfConfig(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_IfGetStaticInfo(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_IfGetDynamicInfo(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_IfGetStats(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_GetNumAssociatedDevices(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_IfGetExtCounter(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_IfGetExtAggrCounter(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_GetMocaCPEs(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_GetAssociatedDevices(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_FreqMaskToValue(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_HardwareEquipped(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_GetFullMeshRates(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_GetFlowStatistics(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_GetResetCount(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_GetIfAcaConfig(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_GetIfAcaStatus(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_CancelIfAca(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_GetIfScmod(IN const Json::Value& req, OUT Json::Value& response);
        void MoCAHAL_SetIfAcaConfig(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__MoCAHAL_STUB_H__
