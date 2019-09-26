/*
 *If not stated otherwise in this file or this component's Licenses.txt file the
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

#ifndef __MTAHAL_STUB_H__
#define __MTAHAL_STUB_H__
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
#include "mta_hal.h"

#define IN
#define OUT

#define TEST_SUCCESS true
#define TEST_FAILURE false

/* To provide external linkage to C Functions defined in TDKB Component folder */

extern "C"
{
    int ssp_MTAHAL_GetParamCharValue(char* paramName, char* value);
    int ssp_MTAHAL_GetParamUlongValue(char* paramName, unsigned long* value);
    int ssp_MTAHAL_SetParamUlongValue(char* paramName, unsigned long value);
    int ssp_MTAHAL_GetDHCPInfo(PMTAMGMT_MTA_DHCP_INFO pInfo);
    int ssp_MTAHAL_GetLineTableGetEntry(unsigned long index, PMTAMGMT_MTA_LINETABLE_INFO pEntry);
    int ssp_MTAHAL_TriggerDiagnostics(unsigned long index);
    int ssp_MTAHAL_GetServiceFlow(unsigned long* count, PMTAMGMT_MTA_SERVICE_FLOW *ppCfg);    
    int ssp_MTAHAL_GetCalls(unsigned long instanceNumber, unsigned long* count, PMTAMGMT_MTA_CALLS* ppCfg);
    int ssp_MTAHAL_GetCALLP(unsigned long lineNumber, PMTAMGMT_MTA_CALLP pCallp);
    int ssp_MTAHAL_GetDSXLogs(unsigned long* count, PMTAMGMT_MTA_DSXLOG* ppDSXLog);
    int ssp_MTAHAL_GetMtaLog(unsigned long* count, PMTAMGMT_MTA_MTALOG_FULL* ppConf);
    int ssp_MTAHAL_getDhcpStatus(MTAMGMT_MTA_STATUS *output_pIpv4status, MTAMGMT_MTA_STATUS *output_pIpv6status);
    int ssp_MTAHAL_getConfigFileStatus(MTAMGMT_MTA_STATUS *poutput_status);
    int ssp_MTAHAL_getLineRegisterStatus(MTAMGMT_MTA_STATUS *output_status_array, int array_size);
    int ssp_MTAHAL_GetHandsets(unsigned long* count, PMTAMGMT_MTA_HANDSETS_INFO* info);
    int ssp_MTAHAL_InitDB(void);
    int ssp_MTAHAL_devResetNow(void);
    int ssp_MTAHAL_getMtaOperationalStatus(MTAMGMT_MTA_STATUS *operationalStatus);
    int ssp_MTAHAL_start_provisioning(int mtaIPMode, char* dhcpOption122Suboption1, char* dhcpOption122Suboption2, char* dhcpOption2171CccV6DssID1, char* dhcpOption2171CccV6DssID2);
    int ssp_MTAHAL_LineRegisterStatus_callback_register(void);
};

class RDKTestAgent;

class MTAHAL : public RDKTestStubInterface,  public AbstractServer<MTAHAL>
{
    public:

	MTAHAL(TcpSocketServer &ptrRpcServer) : AbstractServer <MTAHAL>(ptrRpcServer)
    {
        this->bindAndAddMethod(Procedure("MTAHAL_GetParamCharValue", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &MTAHAL::MTAHAL_GetParamCharValue);
        this->bindAndAddMethod(Procedure("MTAHAL_GetParamUlongValue", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, NULL), &MTAHAL::MTAHAL_GetParamUlongValue);
        this->bindAndAddMethod(Procedure("MTAHAL_SetParamUlongValue", PARAMS_BY_NAME, JSON_STRING, "paramName", JSON_STRING, "value", JSON_INTEGER, NULL), &MTAHAL::MTAHAL_SetParamUlongValue);
        this->bindAndAddMethod(Procedure("MTAHAL_GetDHCPInfo", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_GetDHCPInfo);
        this->bindAndAddMethod(Procedure("MTAHAL_GetLineTableGetEntry", PARAMS_BY_NAME, JSON_STRING, "value", JSON_INTEGER, NULL), &MTAHAL::MTAHAL_GetLineTableGetEntry);
        this->bindAndAddMethod(Procedure("MTAHAL_TriggerDiagnostics", PARAMS_BY_NAME, JSON_STRING, "value", JSON_INTEGER, NULL), &MTAHAL::MTAHAL_TriggerDiagnostics);
        this->bindAndAddMethod(Procedure("MTAHAL_GetServiceFlow", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_GetServiceFlow);
        this->bindAndAddMethod(Procedure("MTAHAL_GetCalls", PARAMS_BY_NAME, JSON_STRING, "value", JSON_INTEGER, NULL), &MTAHAL::MTAHAL_GetCalls);
        this->bindAndAddMethod(Procedure("MTAHAL_GetCALLP", PARAMS_BY_NAME, JSON_STRING, "value", JSON_INTEGER, NULL), &MTAHAL::MTAHAL_GetCALLP);
        this->bindAndAddMethod(Procedure("MTAHAL_GetDSXLogs", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_GetDSXLogs);
        this->bindAndAddMethod(Procedure("MTAHAL_GetMtaLog", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_GetMtaLog);
        this->bindAndAddMethod(Procedure("MTAHAL_GetDhcpStatus", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_GetDhcpStatus);
        this->bindAndAddMethod(Procedure("MTAHAL_GetConfigFileStatus", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_GetConfigFileStatus);
        this->bindAndAddMethod(Procedure("MTAHAL_GetLineRegisterStatus", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_GetLineRegisterStatus);
	this->bindAndAddMethod(Procedure("MTAHAL_GetHandsets", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_GetHandsets);
        this->bindAndAddMethod(Procedure("MTAHAL_InitDB", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_InitDB);
        this->bindAndAddMethod(Procedure("MTAHAL_devResetNow", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_devResetNow);
        this->bindAndAddMethod(Procedure("MTAHAL_getMtaOperationalStatus", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_getMtaOperationalStatus);
        this->bindAndAddMethod(Procedure("MTAHAL_start_provisioning", PARAMS_BY_NAME, JSON_STRING, "mtaIPMode", JSON_INTEGER, "dhcpOption122Suboption1", JSON_STRING, "dhcpOption122Suboption2", JSON_STRING, "dhcpOption2171CccV6DssID1", JSON_STRING, "dhcpOption2171CccV6DssID2", JSON_STRING, NULL), &MTAHAL::MTAHAL_start_provisioning);
        this->bindAndAddMethod(Procedure("MTAHAL_LineRegisterStatus_callback_register", PARAMS_BY_NAME, JSON_STRING, NULL), &MTAHAL::MTAHAL_LineRegisterStatus_callback_register);
	}

    /*inherited functions*/
    bool initialize(IN const char* szVersion);

    bool cleanup(IN const char* szVersion);
    std::string testmodulepre_requisites();
    bool testmodulepost_requisites();

    /*MTAHAL Stub Wrapper functions*/
    void MTAHAL_GetParamCharValue(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response);    
    void MTAHAL_SetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetDHCPInfo(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetLineTableGetEntry(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_TriggerDiagnostics(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetServiceFlow(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetCalls(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetCALLP(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetDSXLogs(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetMtaLog(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetDhcpStatus(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetConfigFileStatus(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetLineRegisterStatus(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_GetHandsets(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_InitDB(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_devResetNow(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_getMtaOperationalStatus(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_start_provisioning(IN const Json::Value& req, OUT Json::Value& response);
    void MTAHAL_LineRegisterStatus_callback_register(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__MTAHAL_STUB_H__

