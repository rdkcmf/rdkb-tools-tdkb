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

#ifndef __PAM_H__
#define __PAM_H__
#include <json/json.h>
#include <unistd.h>
#include <iostream>
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

using namespace std;

class RDKTestAgent;

class pam : public RDKTestStubInterface, public AbstractServer<pam>
{
	public:

                 pam(TcpSocketServer &ptrRpcServer) : AbstractServer <pam>(ptrRpcServer)
                {
                  this->bindAndAddMethod(Procedure("pam_bridge_GetParamUlongValue", PARAMS_BY_NAME, JSON_STRING,"paramName", JSON_STRING,"module", JSON_STRING,NULL), &pam::pam_bridge_GetParamUlongValue);
                  this->bindAndAddMethod(Procedure("pam_GetParameterNames", PARAMS_BY_NAME, JSON_STRING,"ParamName", JSON_STRING,"ParamList", JSON_STRING,NULL), &pam::pam_GetParameterNames);
                  this->bindAndAddMethod(Procedure("pam_SetParameterValues", PARAMS_BY_NAME,JSON_STRING,"ParamName", JSON_STRING,"ParamValue", JSON_STRING, "Type", JSON_STRING, NULL), &pam::pam_SetParameterValues);
		  this->bindAndAddMethod(Procedure("pam_Setparams", PARAMS_BY_NAME,JSON_STRING,"ParamName", JSON_STRING,"ParamValue", JSON_STRING, "Type", JSON_STRING, NULL), &pam::pam_Setparams);
                  this->bindAndAddMethod(Procedure("pam_GetParameterValues", PARAMS_BY_NAME, JSON_STRING,"ParamName", JSON_STRING,NULL), &pam::pam_GetParameterValues);
                  this->bindAndAddMethod(Procedure("pam_MTAAgentRestart", PARAMS_BY_NAME, JSON_STRING,NULL), &pam::pam_MTAAgentRestart);
                  this->bindAndAddMethod(Procedure("pam_CRRestart", PARAMS_BY_NAME, JSON_STRING,NULL), &pam::pam_CRRestart);
                  this->bindAndAddMethod(Procedure("pam_Init", PARAMS_BY_NAME, JSON_STRING,NULL), &pam::pam_Init);
                  this->bindAndAddMethod(Procedure("COSAPAM_DmlMlanGetParamValue", PARAMS_BY_NAME, JSON_STRING,"MethodName", JSON_STRING,NULL), &pam::COSAPAM_DmlMlanGetParamValue);
                  this->bindAndAddMethod(Procedure("COSAPAM_DmlEthGetParamValue", PARAMS_BY_NAME, JSON_STRING,"MethodName", JSON_STRING,NULL), &pam::COSAPAM_DmlEthGetParamValue);
                  this->bindAndAddMethod(Procedure("COSAPAM_DmlDiGetParamValue", PARAMS_BY_NAME, JSON_STRING,"MethodName", JSON_STRING,NULL), &pam::COSAPAM_DmlDiGetParamValue);
                  this->bindAndAddMethod(Procedure("COSAPAM_UpnpEnable", PARAMS_BY_NAME, JSON_STRING,"MethodName",JSON_STRING,"Value", JSON_INTEGER,NULL), &pam::COSAPAM_UpnpEnable);
                  this->bindAndAddMethod(Procedure("COSAPAM_UpnpGetState", PARAMS_BY_NAME, JSON_STRING,"MethodName", JSON_STRING,NULL), &pam::COSAPAM_UpnpGetState);
                  this->bindAndAddMethod(Procedure("COSAPAM_DhcpGet", PARAMS_BY_NAME, JSON_STRING,"MethodName", JSON_STRING,NULL), &pam::COSAPAM_DhcpGet);
                  this->bindAndAddMethod(Procedure("COSAPAM_DhcpsEnable", PARAMS_BY_NAME,JSON_STRING ,"Value", JSON_INTEGER,NULL), &pam::COSAPAM_DhcpsEnable);
                  this->bindAndAddMethod(Procedure("COSAPAM_DnsGet", PARAMS_BY_NAME, JSON_STRING,"MethodName", JSON_STRING,NULL), &pam::COSAPAM_DnsGet);
                  this->bindAndAddMethod(Procedure("COSAPAM_DnsEnable", PARAMS_BY_NAME, JSON_STRING,"MethodName",JSON_STRING ,"Value", JSON_INTEGER,NULL), &pam::COSAPAM_DnsEnable);
	 	}

	/*inherited functions*/
	bool initialize(IN const char* szVersion);

	bool cleanup(IN const char* szVersion);
	std::string testmodulepre_requisites();
        bool testmodulepost_requisites();
        /*pam Stub Wrapper functions*/
	void pam_bridge_GetParamUlongValue(IN const Json::Value& req, OUT Json::Value& response);
        void pam_GetParameterNames(IN const Json::Value& req, OUT Json::Value& response);
	void pam_SetParameterValues(IN const Json::Value& req, OUT Json::Value& response);
	void pam_Setparams(IN const Json::Value& req, OUT Json::Value& response);
	void pam_GetParameterValues(IN const Json::Value& req, OUT Json::Value& response);
	void pam_MTAAgentRestart(IN const Json::Value& req, OUT Json::Value& response);
	void pam_CRRestart(IN const Json::Value& req, OUT Json::Value& response);
	void pam_Init(IN const Json::Value& req, OUT Json::Value& response);
        void COSAPAM_DmlMlanGetParamValue(IN const Json::Value& req, OUT Json::Value& response);
        void COSAPAM_DmlEthGetParamValue(IN const Json::Value& req, OUT Json::Value& response);
        void COSAPAM_DmlDiGetParamValue(IN const Json::Value& req, OUT Json::Value& response);
        void COSAPAM_UpnpEnable(IN const Json::Value& req, OUT Json::Value& response);
        void COSAPAM_UpnpGetState(IN const Json::Value& req, OUT Json::Value& response);
        void COSAPAM_DhcpGet(IN const Json::Value& req, OUT Json::Value& response);
        void COSAPAM_DhcpsEnable(IN const Json::Value& req, OUT Json::Value& response);
        void COSAPAM_DnsGet(IN const Json::Value& req, OUT Json::Value& response);
        void COSAPAM_DnsEnable(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__PAM_STUB_H__
