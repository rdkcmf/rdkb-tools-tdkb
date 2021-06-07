/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
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
#include "json_hal_logger.h"
#include "jsonhal_wrp.h"
#include "jsonhal_lib_wrp.h"
#include "json_schema_validator_wrapper.h"

int get_ptm_link_stats(json_object *reply_msg, PDML_PTM_STATS link_stats);
int get_atm_link_stats(json_object *reply_msg, PDML_ATM_STATS link_stats);

/*****************************************************************************************************************
 * Function Name : dslhal_getlinestats
 * Description   : This function will get the Statistics value of DSL Line
 * @param [in]   : param_name  - Parameter Name
                 : pstLineStats - Structure to full DSL line Statistics
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int dslhal_getlinestats(char *param_name,PDML_XDSL_LINE_STATS pstLineStats)
{
    DEBUG_PRINT(DEBUG_TRACE,"Entry dslhal_getlinestats \n");
    int rc = RETURN_OK;
    int total_param_count = 0;

    json_object *jmsg = NULL;
    json_object *jreply_msg = NULL;
    json_object *jparams = NULL;

    hal_param_t req_param;
    hal_param_t resp_param;

    memset(&req_param, 0, sizeof(req_param));
    memset(&resp_param, 0, sizeof(resp_param));

    jmsg = json_hal_client_get_request_header(RPC_GET_PARAMETERS_REQUEST);
    CHECK(jmsg);

    snprintf(req_param.name, sizeof(req_param.name), param_name);
    if( json_hal_add_param(jmsg, GET_REQUEST_MESSAGE, &req_param) != RETURN_OK) {
        FREE_JSON_OBJECT(jmsg);
        return RETURN_ERR;
    }

    DEBUG_PRINT(DEBUG_TRACE,"JSON Request message = %s \n", json_object_to_json_string_ext(jmsg, JSON_C_TO_STRING_PRETTY));

    if( json_hal_client_send_and_get_reply(jmsg, &jreply_msg) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"[%s][%d] RPC message failed \n", __FUNCTION__, __LINE__);
        FREE_JSON_OBJECT(jmsg);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }

    if(jreply_msg == NULL) {
        FREE_JSON_OBJECT(jmsg);
        return RETURN_ERR;
    }

    if (json_object_object_get_ex(jreply_msg, JSON_RPC_FIELD_PARAMS, &jparams))
    {
        total_param_count = json_object_array_length(jparams);
    }

    if(jparams == NULL) {
        FREE_JSON_OBJECT(jmsg);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }

    for (int index = 0; index < total_param_count; index++)
    {
        if (json_hal_get_param(jreply_msg, index, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get required params from the response message \n", __FUNCTION__, __LINE__);
            FREE_JSON_OBJECT(jmsg);
            FREE_JSON_OBJECT(jreply_msg);
            return RETURN_ERR;
        }

        if (strstr (resp_param.name, "BytesSent")) {
            pstLineStats->BytesSent = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "BytesReceived")) {
            pstLineStats->BytesReceived = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "PacketsSent")) {
            if (strstr (resp_param.name, "DiscardPacketsSent")) {
                pstLineStats->DiscardPacketsSent = atol(resp_param.value);
            }
            else {
                pstLineStats->PacketsSent= atol(resp_param.value);
            }
        }
        else if (strstr (resp_param.name, "PacketsReceived")) {
            if (strstr (resp_param.name, "DiscardPacketsReceived")) {
                pstLineStats->DiscardPacketsReceived = atol(resp_param.value);
            }
            else {
                pstLineStats->PacketsReceived = atol(resp_param.value);
            }
        }
        else if (strstr (resp_param.name, "ErrorsSent")) {
            pstLineStats->ErrorsSent = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "ErrorsReceived")) {
            pstLineStats->ErrorsReceived = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "TotalStart")) {
            pstLineStats->TotalStart = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "ShowtimeStart")) {
            pstLineStats->ShowtimeStart = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "LastShowtimeStart")) {
            pstLineStats->LastShowtimeStart = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "QuarterHourStart")) {
            pstLineStats->QuarterHourStart = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentDayStart")) {
            pstLineStats->CurrentDayStart = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Stats.Total.ErroredSecs")) {
            pstLineStats->stTotal.ErroredSecs = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "Stats.Total.SeverelyErroredSecs")) {
            pstLineStats->stTotal.SeverelyErroredSecs = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "Stats.Showtime.ErroredSecs")) {
            pstLineStats->stShowTime.ErroredSecs = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "Stats.Showtime.SeverelyErroredSecs")) {
            pstLineStats->stShowTime.SeverelyErroredSecs = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "Stats.LastShowtime.ErroredSecs")) {
            pstLineStats->stLastShowTime.ErroredSecs = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "Stats.LastShowtime.SeverelyErroredSecs")) {
            pstLineStats->stLastShowTime.SeverelyErroredSecs = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "Stats.CurrentDay.ErroredSecs")) {
            pstLineStats->stCurrentDay.ErroredSecs = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "Stats.CurrentDay.SeverelyErroredSecs")) {
            pstLineStats->stCurrentDay.SeverelyErroredSecs = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "X_RDK_LinkRetrain")) {
            if (strstr (resp_param.name, "Stats.CurrentDay.X_RDK_LinkRetrain")) {
               pstLineStats->stCurrentDay.X_RDK_LinkRetrain = atoi(resp_param.value);
            }
            else {
               pstLineStats->stQuarterHour.X_RDK_LinkRetrain = atoi(resp_param.value);
            }
        }
        else if (strstr (resp_param.name, "Stats.CurrentDay.X_RDK_InitErrors")) {
            pstLineStats->stCurrentDay.X_RDK_InitErrors = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "Stats.CurrentDay.X_RDK_InitTimeouts")) {
            pstLineStats->stCurrentDay.X_RDK_InitTimeouts = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "Stats.QuarterHour.ErroredSecs")) {
            pstLineStats->stQuarterHour.ErroredSecs = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "Stats.QuarterHour.SeverelyErroredSecs")) {
            pstLineStats->stQuarterHour.SeverelyErroredSecs = atoi(resp_param.value);
        }
    }

    // Free json objects
    FREE_JSON_OBJECT(jmsg);
    FREE_JSON_OBJECT(jreply_msg);

    return rc;
}

/*****************************************************************************************************************
 * Function Name : dslhal_getXRdk_Nlm
 * Description   : This function will get the NLM value of the DSL Line
 * @param [in]   : param_name  - Parameter Name
                 : pstNlmInfo - Structure to full DSL NLM value
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int dslhal_getXRdk_Nlm( char *param_name,PDML_XDSL_X_RDK_NLNM pstNlmInfo )
{
    DEBUG_PRINT(DEBUG_TRACE,"Entry dslhal_getXRdk_Nlm function \n");
    int rc = RETURN_OK;
    int total_param_count = 0;

    hal_param_t req_param;
    hal_param_t resp_param;

    json_object *jmsg = NULL;
    json_object *jreply_msg = NULL;
    json_object *jparams = NULL;

    memset(&req_param, 0, sizeof(req_param));
    memset(&resp_param, 0, sizeof(resp_param));

    jmsg = json_hal_client_get_request_header(RPC_GET_PARAMETERS_REQUEST);
    CHECK(jmsg);

    snprintf(req_param.name, sizeof(req_param.name), param_name);
    if( json_hal_add_param(jmsg, GET_REQUEST_MESSAGE, &req_param) != RETURN_OK)
    {
        FREE_JSON_OBJECT(jmsg);
        return RETURN_ERR;
    }

    if( json_hal_client_send_and_get_reply(jmsg, &jreply_msg) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"[%s][%d] RPC message failed \n", __FUNCTION__, __LINE__);
        FREE_JSON_OBJECT(jmsg);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }

    if(jreply_msg == NULL)
    {
        FREE_JSON_OBJECT(jmsg);
        return RETURN_ERR;
    }

    if (json_object_object_get_ex(jreply_msg, JSON_RPC_FIELD_PARAMS, &jparams))
    {
        total_param_count = json_object_array_length(jparams);
    }

    if(jparams == NULL)
    {
        FREE_JSON_OBJECT(jmsg);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }

    for (int index = 0; index < total_param_count; index++)
    {
        rc = json_hal_get_param(jreply_msg, index, GET_RESPONSE_MESSAGE, &resp_param);
        if (rc != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get required params from the response message \n", __FUNCTION__, __LINE__);
            FREE_JSON_OBJECT(jmsg);
            FREE_JSON_OBJECT(jreply_msg);
            return rc;
        }
        if (strstr (resp_param.name, "echotonoiseratio")) {
            pstNlmInfo->echotonoiseratio = strtol(resp_param.value, NULL, 10);
        }
    }
    // Free json objects
    FREE_JSON_OBJECT(jmsg);
    FREE_JSON_OBJECT(jreply_msg);

    return rc;
}

/*****************************************************************************************************************
 * Function Name : dslhal_getlineinfo
 * Description   : This function will get the information of the DSL Line
 * @param [in]   : param_name  - Parameter Name
                 : pstLineInfo - Structure to full DSL Line Info
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int dslhal_getlineinfo(char *param_name, PDML_XDSL_LINE pstLineInfo)
{
    DEBUG_PRINT(DEBUG_TRACE,"Entry dslhal_getlineinfo function\n");
    int rc = RETURN_OK;
    hal_param_t req_param;
    hal_param_t resp_param;
    int total_param_count = 0;
    json_object *jmsg = NULL;
    json_object *jreply_msg = NULL;
    json_object *jparams = NULL;
    memset(&req_param, 0, sizeof(req_param));
    memset(&resp_param, 0, sizeof(resp_param));
    jmsg = json_hal_client_get_request_header(RPC_GET_PARAMETERS_REQUEST);
    CHECK(jmsg);
    snprintf(req_param.name, sizeof(req_param.name),param_name);
    if(json_hal_add_param(jmsg, GET_REQUEST_MESSAGE, &req_param) != RETURN_OK)
    {
        FREE_JSON_OBJECT(jmsg);
        return RETURN_ERR;
    }
    DEBUG_PRINT(DEBUG_TRACE,"JSON Request message = %s \n", json_object_to_json_string_ext(jmsg, JSON_C_TO_STRING_PRETTY));
    if (json_hal_client_send_and_get_reply(jmsg, &jreply_msg) != RETURN_OK )
    {
        DEBUG_PRINT(DEBUG_TRACE,"[%s][%d] RPC message failed \n", __FUNCTION__, __LINE__);
        FREE_JSON_OBJECT(jmsg);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }
    if(jreply_msg == NULL) {
        FREE_JSON_OBJECT(jmsg);
        return RETURN_ERR;
    }
    if (json_object_object_get_ex(jreply_msg, JSON_RPC_FIELD_PARAMS, &jparams))
    {
        total_param_count = json_object_array_length(jparams);
    }
    if(jparams == NULL) {
        FREE_JSON_OBJECT(jmsg);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }
    for (int index = 0; index < total_param_count; index++)
    {
        if (json_hal_get_param(jreply_msg, index, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get required params from the response message \n", __FUNCTION__, __LINE__);
            FREE_JSON_OBJECT(jmsg);
            FREE_JSON_OBJECT(jreply_msg);
            return RETURN_ERR;
        }
        if (strstr (resp_param.name, "Status")) {
            /**
             * LinkStatus
             */
            if (strstr(resp_param.name, "Link"))
            {
                if (strcmp(resp_param.value, "Up") == 0)
                {
                    pstLineInfo->LinkStatus = XDSL_LINK_STATUS_Up;
                }
                else if (strcmp(resp_param.value, "Initializing") == 0)
                {
                    pstLineInfo->LinkStatus = XDSL_LINK_STATUS_Initializing;
                }
                else if (strcmp(resp_param.value, "EstablishingLink") == 0)
                {
                    pstLineInfo->LinkStatus = XDSL_LINK_STATUS_EstablishingLink;
                }
                else if (strcmp(resp_param.value, "NoSignal") == 0)
                {
                    pstLineInfo->LinkStatus = XDSL_LINK_STATUS_NoSignal;
                }
                else if (strcmp(resp_param.value, "Disabled") == 0)
                {
                    pstLineInfo->LinkStatus = XDSL_LINK_STATUS_Disabled;
                }
                else if (strcmp(resp_param.value, "Error") == 0)
                {
                    pstLineInfo->LinkStatus = XDSL_LINK_STATUS_Error;
                }
            }
            else //IfStatus
            {
                if (strcmp(resp_param.value, "Up") == 0)
                {
                    pstLineInfo->Status = XDSL_IF_STATUS_Up;
                }
                else if (strcmp(resp_param.value, "Down") == 0)
                {
                    pstLineInfo->Status = XDSL_IF_STATUS_Down;
                }
                else if (strcmp(resp_param.value, "Unknown") == 0)
                {
                    pstLineInfo->Status = XDSL_IF_STATUS_Unknown;
                }
                else if (strcmp(resp_param.value, "Dormant") == 0)
                {
                    pstLineInfo->Status = XDSL_IF_STATUS_Dormant;
                }
                else if (strcmp(resp_param.value, "NotPresent") == 0)
                {
                    pstLineInfo->Status = XDSL_IF_STATUS_NotPresent;
                }
                else if (strcmp(resp_param.value, "LowerLayerDown") == 0)
                {
                    pstLineInfo->Status = XDSL_IF_STATUS_LowerLayerDown;
                }
                else if (strcmp(resp_param.value, "Error") == 0)
                {
                    pstLineInfo->Status = XDSL_IF_STATUS_Error;
                }
            }
        }
        else if (strstr (resp_param.name, "LastChange")) {
            pstLineInfo->LastChange = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "PowerManagementState")) {
            pstLineInfo->PowerManagementState = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "UpstreamMaxBitRate")) {
            pstLineInfo->UpstreamMaxBitRate= atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "DownstreamMaxBitRate")) {
            pstLineInfo->DownstreamMaxBitRate = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "SuccessFailureCause")) {
            pstLineInfo->SuccessFailureCause = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "RXTHRSHds")) {
            pstLineInfo->RXTHRSHds = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "ACTRAMODEds")) {
            pstLineInfo->ACTRAMODEds = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "ACTRAMODEus")) {
            pstLineInfo->ACTRAMODEus = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "ACTINPROCds")) {
            pstLineInfo->ACTINPROCds = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "ACTINPROCus")) {
            pstLineInfo->ACTINPROCus = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "SNRMROCds")) {
            pstLineInfo->SNRMROCds = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "SNRMROCus")) {
            pstLineInfo->SNRMROCus = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "LastStateTransmittedDownstream")) {
            pstLineInfo->LastStateTransmittedDownstream = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "LastStateTransmittedUpstream")) {
            pstLineInfo->LastStateTransmittedUpstream = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "UPBOKLER")) {
            pstLineInfo->UPBOKLER = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "UPBOKLE")) {
            pstLineInfo->UPBOKLE = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "LIMITMASK")) {
            pstLineInfo->LIMITMASK = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "US0MASK")) {
            pstLineInfo->US0MASK = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "UpstreamAttenuation")) {
            pstLineInfo->UpstreamAttenuation = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "DownstreamAttenuation")) {
            pstLineInfo->DownstreamAttenuation = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "UpstreamNoiseMargin")) {
            pstLineInfo->UpstreamNoiseMargin = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "DownstreamNoiseMargin")) {
            pstLineInfo->DownstreamNoiseMargin = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "UpstreamPower")) {
            pstLineInfo->UpstreamPower = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "DownstreamPower")) {
            pstLineInfo->DownstreamPower = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "LineEncoding")) {
            pstLineInfo->LineEncoding = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "TRELLISds")) {
            pstLineInfo->TRELLISds = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "TRELLISus")) {
            pstLineInfo->TRELLISus = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "ACTSNRMODEds")) {
            pstLineInfo->ACTSNRMODEds = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "ACTSNRMODEus")) {
            pstLineInfo->ACTSNRMODEus = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "ACTUALCE")) {
            pstLineInfo->ACTUALCE = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "LineNumber")) {
            pstLineInfo->LineNumber = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "INMIATOds")) {
            pstLineInfo->INMIATOds = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "INMIATSds")) {
            pstLineInfo->INMIATSds = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "INMCCds")) {
            pstLineInfo->INMCCds = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "INMINPEQMODEds")) {
            pstLineInfo->INMINPEQMODEds = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "XTURANSIStd")) {
            pstLineInfo->XTURANSIStd = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "XTURANSIRev")) {
            pstLineInfo->XTURANSIRev = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "XTUCANSIStd")) {
            pstLineInfo->XTUCANSIStd = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "XTUCANSIRev")) {
            pstLineInfo->XTUCANSIRev = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentProfile")) {
            snprintf_t(pstLineInfo->CurrentProfile, sizeof(pstLineInfo->CurrentProfile), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "AllowedProfiles")) {
            snprintf_t(pstLineInfo->AllowedProfiles, sizeof(pstLineInfo->AllowedProfiles), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "FirmwareVersion")) {
            snprintf_t(pstLineInfo->FirmwareVersion, sizeof(pstLineInfo->FirmwareVersion), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "StandardUsed")) {
            snprintf_t(pstLineInfo->StandardUsed, sizeof(pstLineInfo->StandardUsed), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "SNRMpbus")) {
            snprintf_t(pstLineInfo->SNRMpbus, sizeof(pstLineInfo->SNRMpbus), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "SNRMpbds")) {
            snprintf_t(pstLineInfo->SNRMpbds, sizeof(pstLineInfo->SNRMpbds), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "XTURVendor")) {
            snprintf_t(pstLineInfo->XTURVendor, sizeof(pstLineInfo->XTURVendor), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "XTURCountry")) {
            snprintf_t(pstLineInfo->XTURCountry, sizeof(pstLineInfo->XTURCountry), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "XTUCVendor")) {
            snprintf_t(pstLineInfo->XTUCVendor, sizeof(pstLineInfo->XTUCVendor), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "XTUCCountry")) {
            snprintf_t(pstLineInfo->XTUCCountry, sizeof(pstLineInfo->XTUCCountry), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "UPBOKLEPb")) {
            snprintf_t(pstLineInfo->UPBOKLEPb, sizeof(pstLineInfo->UPBOKLEPb), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "UPBOKLERPb")) {
            snprintf_t(pstLineInfo->UPBOKLERPb, sizeof(pstLineInfo->UPBOKLERPb), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "XTSE")) {
            snprintf_t(pstLineInfo->XTSE, sizeof(pstLineInfo->XTSE), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "XTSUsed")) {
            snprintf_t(pstLineInfo->XTSUsed, sizeof(pstLineInfo->XTSUsed), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "MREFPSDds")) {
            snprintf_t(pstLineInfo->MREFPSDds, sizeof(pstLineInfo->MREFPSDds), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "MREFPSDus")) {
            snprintf_t(pstLineInfo->MREFPSDus, sizeof(pstLineInfo->MREFPSDus), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "VirtualNoisePSDds")) {
            snprintf_t(pstLineInfo->VirtualNoisePSDds, sizeof(pstLineInfo->VirtualNoisePSDds), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "VirtualNoisePSDus")) {
            snprintf_t(pstLineInfo->VirtualNoisePSDus, sizeof(pstLineInfo->VirtualNoisePSDus), "%s", resp_param.value);
        }
    }
    FREE_JSON_OBJECT(jmsg);
    FREE_JSON_OBJECT(jreply_msg);
    return rc;
}

/*****************************************************************************************************************
 * Function Name : get_ptm_link_stats
 * Description   : This function will get the information of the ptm link stats
 * @param [in]   : reply_msg - Pointer to get details
                 : link_stats - Structure to get PTM_STATS Info
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int get_ptm_link_stats(json_object *reply_msg, PDML_PTM_STATS link_stats)
{
    int  rc = RETURN_OK;
    int total_param_count = 0;
    total_param_count = json_hal_get_total_param_count(reply_msg);
    hal_param_t resp_param;
    /**
     * Traverse through each index and retrieve value.
     */
    for (int i = 0; i < total_param_count; ++i)
    {
        if (json_hal_get_param(reply_msg, i, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get the param from response message [index = %d] \n", __FUNCTION__, __LINE__, i);
            continue;
        }
        if (strstr(resp_param.name, "BytesSent"))
        {
            link_stats->BytesSent = atol(resp_param.value);
        }
        else if (strstr(resp_param.name, "BytesReceived"))
        {
            link_stats->BytesReceived = atol(resp_param.value);
        }
        else if (strstr(resp_param.name, "PacketsSent"))
        {
            if (strstr(resp_param.name, "Unicast"))
            {
                link_stats->UnicastPacketsSent = atol(resp_param.value);
            }
            else if (strstr(resp_param.name, "Discard"))
            {
                link_stats->DiscardPacketsSent = atoi(resp_param.value);
            }
            else if (strstr(resp_param.name, "Multicast"))
            {
                link_stats->MulticastPacketsSent = atol(resp_param.value);
            }
            else if (strstr(resp_param.name, "Broadcast"))
            {
                link_stats->BroadcastPacketsSent = atol(resp_param.value);
            }
            else
            {
                link_stats->PacketsSent = atol(resp_param.value);
            }
        }
        else if (strstr(resp_param.name, "PacketsReceived"))
        {
            if (strstr(resp_param.name, "Unicast"))
            {
                link_stats->UnicastPacketsReceived = atol(resp_param.value);
            }
            else if (strstr(resp_param.name, "Discard"))
            {
                link_stats->DiscardPacketsReceived = atoi(resp_param.value);
            }
            else if (strstr(resp_param.name, "Multicast"))
            {
                link_stats->MulticastPacketsReceived = atol(resp_param.value);
            }
            else if (strstr(resp_param.name, "Broadcast"))
            {
                link_stats->BroadcastPacketsReceived = atol(resp_param.value);
            }
            else if (strstr(resp_param.name, "UnknownProto"))
            {
                link_stats->UnknownProtoPacketsReceived = atoi(resp_param.value);
            }
            else
            {
                link_stats->PacketsReceived = atol(resp_param.value);
            }
        }
        else if (strstr(resp_param.name, "ErrorsSent"))
        {
            link_stats->ErrorsSent = atoi(resp_param.value);
        }
        else if (strstr(resp_param.name, "ErrorsReceived"))
        {
            link_stats->ErrorsReceived = atoi(resp_param.value);
        }
    }
    DEBUG_PRINT(DEBUG_TRACE,"%s - %d Statistics Information \n", __FUNCTION__, __LINE__);
    DEBUG_PRINT(DEBUG_TRACE,"BytesSent = %ld \n", link_stats->BytesSent);
    DEBUG_PRINT(DEBUG_TRACE,"BytesReceived = %ld \n", link_stats->BytesReceived);
    DEBUG_PRINT(DEBUG_TRACE,"PacketsSent = %ld \n", link_stats->PacketsSent);
    DEBUG_PRINT(DEBUG_TRACE,"PacketsReceived = %ld \n", link_stats->PacketsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"ErrorsSent = %d \n", link_stats->ErrorsSent);
    DEBUG_PRINT(DEBUG_TRACE,"ErrorsReceived = %d \n", link_stats->ErrorsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"UnicastPacketsSent = %d \n", link_stats->UnicastPacketsSent);
    DEBUG_PRINT(DEBUG_TRACE,"UnicastPacketsReceived = %d \n", link_stats->UnicastPacketsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"DiscardPacketsReceived = %d \n", link_stats->DiscardPacketsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"DiscardPacketsSent = %d \n", link_stats->DiscardPacketsSent);
    DEBUG_PRINT(DEBUG_TRACE,"DiscardPacketsReceived = %d \n", link_stats->DiscardPacketsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"MulticastPacketsSent = %ld \n", link_stats->MulticastPacketsSent);
    DEBUG_PRINT(DEBUG_TRACE,"MulticastPacketsReceived = %ld \n", link_stats->MulticastPacketsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"BroadcastPacketsSent = %ld \n", link_stats->BroadcastPacketsSent);
    DEBUG_PRINT(DEBUG_TRACE,"BroadcastPacketsReceived = %ld \n", link_stats->BroadcastPacketsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"UnknownProtoPacketsReceived = %d \n", link_stats->UnknownProtoPacketsReceived);
    return rc;
}
/*****************************************************************************************************************
 * Function Name : xtm_hal_getLinkStats
 * Description   : This function will get the statistics of the DSL Line
 * @param [in]   : param_name  - Parameter Name
                 : link_stats - Structure to full PTM link stats
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int xtm_hal_getLinkStats(char *param_name, PDML_PTM_STATS link_stats)
{
    CHECK(param_name != NULL);
    CHECK(link_stats != NULL);
    int rc = RETURN_OK;
    json_object *jreply_msg = NULL;
    json_object *jrequest = create_json_request_message(GET_REQUEST_MESSAGE, param_name, NULL_TYPE , NULL);
    CHECK(jrequest != NULL);
    if (json_hal_client_send_and_get_reply(jrequest, &jreply_msg) == RETURN_ERR)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get reply for the json request \n", __FUNCTION__, __LINE__);
        return RETURN_ERR;
    }
    rc = get_ptm_link_stats(jreply_msg, link_stats);
    if (rc != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get statistics data  \n", __FUNCTION__, __LINE__);
    }
        // Free json objects.
    if (jrequest)
    {
        json_object_put(jrequest);
        jrequest = NULL;
    }
    if (jreply_msg)
    {
        json_object_put(jreply_msg);
        jreply_msg = NULL;
    }
    return rc;
}

/*****************************************************************************************************************
 * Function Name : atm_hal_getLinkStats
 * Description   : This function will get the statistics of ATM Link
 * @param [in]   : param_name  - Parameter Name
                 : link_stats - Structure to full ATM link stats
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int atm_hal_getLinkStats(char *param_name, PDML_ATM_STATS link_stats)
{
    CHECK(param_name != NULL);
    CHECK(link_stats != NULL);
    int rc = RETURN_OK;
    json_object *jreply_msg = NULL;
    json_object *jrequest = create_json_request_message(GET_REQUEST_MESSAGE, param_name, NULL_TYPE , NULL);
    CHECK(jrequest != NULL);
    if (json_hal_client_send_and_get_reply(jrequest, &jreply_msg) == RETURN_ERR)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get reply for the json request \n", __FUNCTION__, __LINE__);
        return RETURN_ERR;
    }
    rc = get_atm_link_stats(jreply_msg, link_stats);
    if (rc != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get statistics data  \n", __FUNCTION__, __LINE__);
    }
        // Free json objects.
    if (jrequest)
    {
        json_object_put(jrequest);
        jrequest = NULL;
    }
    if (jreply_msg)
    {
        json_object_put(jreply_msg);
        jreply_msg = NULL;
    }
    return rc;
}

/*****************************************************************************************************************
 * Function Name : get_atm_link_stats
 * Description   : This function will get the statistics of ATM Link
 * @param [in]   : reply_msg  - Pointer to get the details
                 : link_stats - Structure to full ATM link stats
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int get_atm_link_stats(json_object *reply_msg, PDML_ATM_STATS link_stats)
{
    int rc = RETURN_OK;
    int total_param_count = 0;
    total_param_count = json_hal_get_total_param_count(reply_msg);
    hal_param_t resp_param;
    /**
     * Traverse through each index and retrieve value.
     */
    for (int i = 0; i < total_param_count; ++i)
    {
        if (json_hal_get_param(reply_msg, i, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get the param from response message [index = %d] \n", __FUNCTION__, __LINE__, i);
            continue;
        }
        if (strstr(resp_param.name, "BytesSent"))
        {
            link_stats->BytesSent = atol(resp_param.value);
        }
        else if (strstr(resp_param.name, "BytesReceived"))
        {
            link_stats->BytesReceived = atol(resp_param.value);
        }
        else if (strstr(resp_param.name, "PacketsSent"))
        {
            if (strstr(resp_param.name, "Unicast"))
            {
                link_stats->UnicastPacketsSent = atol(resp_param.value);
            }
            else if (strstr(resp_param.name, "Discard"))
            {
                link_stats->DiscardPacketsSent = atoi(resp_param.value);
            }
            else if (strstr(resp_param.name, "Multicast"))
            {
                link_stats->MulticastPacketsSent = atol(resp_param.value);
            }
            else if (strstr(resp_param.name, "Broadcast"))
            {
                link_stats->BroadcastPacketsSent = atol(resp_param.value);
            }
            else
            {
                link_stats->PacketsSent = atol(resp_param.value);
            }
        }
        else if (strstr(resp_param.name, "PacketsReceived"))
        {
            if (strstr(resp_param.name, "Unicast"))
            {
                link_stats->UnicastPacketsReceived = atol(resp_param.value);
            }
            else if (strstr(resp_param.name, "Discard"))
            {
                link_stats->DiscardPacketsReceived = atoi(resp_param.value);
            }
            else if (strstr(resp_param.name, "Multicast"))
            {
                link_stats->MulticastPacketsReceived = atol(resp_param.value);
            }
            else if (strstr(resp_param.name, "Broadcast"))
            {
                link_stats->BroadcastPacketsReceived = atol(resp_param.value);
            }
            else if (strstr(resp_param.name, "UnknownProto"))
            {
                link_stats->UnknownProtoPacketsReceived = atoi(resp_param.value);
            }
            else
            {
                link_stats->PacketsReceived = atol(resp_param.value);
            }
        }
        else if (strstr(resp_param.name, "ErrorsSent"))
        {
            link_stats->ErrorsSent = atoi(resp_param.value);
        }
        else if (strstr(resp_param.name, "ErrorsReceived"))
        {
            link_stats->ErrorsReceived = atoi(resp_param.value);
        }
    }
    DEBUG_PRINT(DEBUG_TRACE,"%s - %d Statistics Information \n", __FUNCTION__, __LINE__);
    DEBUG_PRINT(DEBUG_TRACE,"BytesSent = %ld \n", link_stats->BytesSent);
    DEBUG_PRINT(DEBUG_TRACE,"BytesReceived = %ld \n", link_stats->BytesReceived);
    DEBUG_PRINT(DEBUG_TRACE,"PacketsSent = %ld \n", link_stats->PacketsSent);
    DEBUG_PRINT(DEBUG_TRACE,"PacketsReceived = %ld \n", link_stats->PacketsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"ErrorsSent = %d \n", link_stats->ErrorsSent);
    DEBUG_PRINT(DEBUG_TRACE,"ErrorsReceived = %d \n", link_stats->ErrorsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"UnicastPacketsSent = %ld \n", link_stats->UnicastPacketsSent);
    DEBUG_PRINT(DEBUG_TRACE,"UnicastPacketsReceived = %ld \n", link_stats->UnicastPacketsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"DiscardPacketsReceived = %lu \n", link_stats->DiscardPacketsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"DiscardPacketsSent = %lu \n", link_stats->DiscardPacketsSent);
    DEBUG_PRINT(DEBUG_TRACE,"MulticastPacketsSent = %ld \n", link_stats->MulticastPacketsSent);
    DEBUG_PRINT(DEBUG_TRACE,"MulticastPacketsReceived = %ld \n", link_stats->MulticastPacketsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"BroadcastPacketsSent = %ld \n", link_stats->BroadcastPacketsSent);
    DEBUG_PRINT(DEBUG_TRACE,"BroadcastPacketsReceived = %ld \n", link_stats->BroadcastPacketsReceived);
    DEBUG_PRINT(DEBUG_TRACE,"UnknownProtoPacketsReceived = %d \n", link_stats->UnknownProtoPacketsReceived);
    return rc;
}

/*****************************************************************************************************************
 * Function Name : xdsl_hal_dslGetChannelInfo
 * Description   : This function will get the DSL Channel Info
 * @param [in]   : param_name - Parameter name
                 : pstChannelInfo - Srructure to fill the data
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int xdsl_hal_dslGetChannelInfo( char *param_name, PDML_XDSL_CHANNEL pstChannelInfo)
{
    int rc = RETURN_OK;
    int total_param_count = 0;
    hal_param_t req_param;
    hal_param_t resp_param;
    json_object *jmsg = NULL;
    json_object *jreply_msg = NULL;
    json_object *jparams = NULL;
    memset(&req_param, 0, sizeof(req_param));
    memset(&resp_param, 0, sizeof(resp_param));
    jmsg = json_hal_client_get_request_header(RPC_GET_PARAMETERS_REQUEST);
    CHECK(jmsg);
    snprintf(req_param.name, sizeof(req_param.name), param_name);
    if( json_hal_add_param(jmsg, GET_REQUEST_MESSAGE, &req_param) != RETURN_OK)
    {
        FREE_JSON_OBJECT(jmsg);
        return RETURN_ERR;
    }
   DEBUG_PRINT(DEBUG_TRACE,"JSON Request message = %s \n", json_object_to_json_string_ext(jmsg, JSON_C_TO_STRING_PRETTY));
    if( json_hal_client_send_and_get_reply(jmsg, &jreply_msg) != RETURN_OK)
    {
        DEBUG_PRINT(DEBUG_TRACE,"[%s][%d] RPC message failed \n", __FUNCTION__, __LINE__);
        FREE_JSON_OBJECT(jmsg);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }
    if(jreply_msg == NULL)
    {
        FREE_JSON_OBJECT(jmsg);
        return RETURN_ERR;
    }
    if (json_object_object_get_ex(jreply_msg, JSON_RPC_FIELD_PARAMS, &jparams))
    {
        total_param_count = json_object_array_length(jparams);
    }
    if(jparams == NULL)
    {
        FREE_JSON_OBJECT(jmsg);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }
    for (int index = 0; index < total_param_count; index++)
    {
        rc = json_hal_get_param(jreply_msg, index, GET_RESPONSE_MESSAGE, &resp_param);
        if (rc != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get required params from the response message \n", __FUNCTION__, __LINE__);
            FREE_JSON_OBJECT(jmsg);
            FREE_JSON_OBJECT(jreply_msg);
            return rc;
        }
        if (strstr (resp_param.name, "Status")) {
            if (strcmp(resp_param.value, "Up") == 0)
            {
                pstChannelInfo->Status = XDSL_IF_STATUS_Up;
            }
            else if (strcmp(resp_param.value, "Down") == 0)
            {
                pstChannelInfo->Status = XDSL_IF_STATUS_Down;
            }
            else if (strcmp(resp_param.value, "Unknown") == 0)
            {
                pstChannelInfo->Status = XDSL_IF_STATUS_Unknown;
            }
            else if (strcmp(resp_param.value, "Dormant") == 0)
            {
                pstChannelInfo->Status = XDSL_IF_STATUS_Dormant;
            }
            else if (strcmp(resp_param.value, "NotPresent") == 0)
            {
                pstChannelInfo->Status = XDSL_IF_STATUS_NotPresent;
            }
            else if (strcmp(resp_param.value, "LowerLayerDown") == 0)
            {
                pstChannelInfo->Status = XDSL_IF_STATUS_LowerLayerDown;
            }
            else if (strcmp(resp_param.value, "Error") == 0)
            {
                pstChannelInfo->Status = XDSL_IF_STATUS_Error;
            }
        }
        else if (strstr (resp_param.name, "LastChange")) {
            pstChannelInfo->LastChange = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "LPATH")) {
            pstChannelInfo->LPATH = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "INTLVDEPTH")) {
            pstChannelInfo->INTLVDEPTH = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "INTLVBLOCK")) {
            pstChannelInfo->INTLVBLOCK = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "ActualInterleavingDelay")) {
            pstChannelInfo->ActualInterleavingDelay = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "ACTINP")) {
            pstChannelInfo->ACTINP = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "INPREPORT")) {
            pstChannelInfo->INPREPORT = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "NFEC")) {
            pstChannelInfo->NFEC = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "RFEC")) {
            pstChannelInfo->RFEC = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "LSYMB")) {
            pstChannelInfo->LSYMB = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "UpstreamCurrRate")) {
            pstChannelInfo->UpstreamCurrRate = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "DownstreamCurrRate")) {
            pstChannelInfo->DownstreamCurrRate = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "ACTNDR")) {
            pstChannelInfo->ACTNDR = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "ACTINPREIN")) {
            pstChannelInfo->ACTINPREIN = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "LinkEncapsulationSupported")) {
            snprintf_t(pstChannelInfo->LinkEncapsulationSupported, sizeof(pstChannelInfo->LinkEncapsulationSupported), "%s", resp_param.value);
        }
        else if (strstr (resp_param.name, "LinkEncapsulationUsed")) {
            snprintf_t(pstChannelInfo->LinkEncapsulationUsed, sizeof(pstChannelInfo->LinkEncapsulationUsed), "%s", resp_param.value);
        }
    }
    // Free json objects
    FREE_JSON_OBJECT(jmsg);
    FREE_JSON_OBJECT(jreply_msg);
    return rc;
}

/*****************************************************************************************************************
 * Function Name : xdsl_hal_dslGetChannelStats
 * Description   : This function will get the DSL Channel Statistics
 * @param [in]   : param_name - Parameter name
                 : pstChannelStats - Srructure to fill the data
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int xdsl_hal_dslGetChannelStats(char *param_name, PDML_XDSL_CHANNEL_STATS pstChannelStats)
{
    int rc = RETURN_OK;
    int total_param_count = 0;
    json_object *jmsg = NULL;
    json_object *jparams = NULL;
    json_object *jreply_msg = NULL;
    hal_param_t req_param;
    hal_param_t resp_param;
    memset(&req_param, 0, sizeof(req_param));
    memset(&resp_param, 0, sizeof(resp_param));
    jmsg = json_hal_client_get_request_header(RPC_GET_PARAMETERS_REQUEST);
    CHECK(jmsg);
    snprintf(req_param.name, sizeof(req_param.name),param_name);
    if( json_hal_add_param(jmsg, GET_REQUEST_MESSAGE, &req_param) != RETURN_OK) {
        FREE_JSON_OBJECT(jmsg);
        return RETURN_ERR;
    }
    DEBUG_PRINT(DEBUG_TRACE,"JSON Request message = %s \n", json_object_to_json_string_ext(jmsg, JSON_C_TO_STRING_PRETTY));
    if( json_hal_client_send_and_get_reply(jmsg, &jreply_msg) != RETURN_OK )
    {
        DEBUG_PRINT(DEBUG_TRACE,"[%s][%d] RPC message failed \n", __FUNCTION__, __LINE__);
        FREE_JSON_OBJECT(jmsg);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }
    if(jreply_msg == NULL) {
        FREE_JSON_OBJECT(jmsg);
        return RETURN_ERR;
    }
    if (json_object_object_get_ex(jreply_msg, JSON_RPC_FIELD_PARAMS, &jparams))
    {
        total_param_count = json_object_array_length(jparams);
    }
    if(jparams == NULL) {
        FREE_JSON_OBJECT(jmsg);
        FREE_JSON_OBJECT(jreply_msg);
        return RETURN_ERR;
    }
    for (int index = 0; index < total_param_count; index++)
    {
        if (json_hal_get_param(jreply_msg, index, GET_RESPONSE_MESSAGE, &resp_param) != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_TRACE,"%s - %d Failed to get required params from the response message \n", __FUNCTION__, __LINE__);
            FREE_JSON_OBJECT(jmsg);
            FREE_JSON_OBJECT(jreply_msg);
            return RETURN_ERR;
        }
        if (strstr (resp_param.name, "BytesSent")) {
            pstChannelStats->BytesSent = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "BytesReceived")) {
            pstChannelStats->BytesReceived = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "PacketsSent")) {
            if (strstr (resp_param.name, "DiscardPacketsSent")) {
                pstChannelStats->DiscardPacketsSent = atol(resp_param.value);
            }
            else {
                pstChannelStats->PacketsSent= atol(resp_param.value);
            }
        }
        else if (strstr (resp_param.name, "PacketsReceived")) {
            if (strstr (resp_param.name, "DiscardPacketsReceived")) {
                pstChannelStats->DiscardPacketsReceived = atol(resp_param.value);
            }
            else {
                pstChannelStats->PacketsReceived = atol(resp_param.value);
            }
        }
        else if (strstr (resp_param.name, "ErrorsSent")) {
            pstChannelStats->ErrorsSent = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "ErrorsReceived")) {
            pstChannelStats->ErrorsReceived = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "TotalStart")) {
            pstChannelStats->TotalStart = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "ShowtimeStart")) {
            pstChannelStats->ShowtimeStart = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "LastShowtimeStart")) {
            pstChannelStats->LastShowtimeStart = atoi(resp_param.value);
        }
        else if (strstr (resp_param.name, "QuarterHourStart")) {
            pstChannelStats->QuarterHourStart = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentDayStart")) {
            pstChannelStats->CurrentDayStart = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Total.XTURFECErrors")) {
            pstChannelStats->stTotal.XTURFECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Total.XTUCFECErrors")) {
            pstChannelStats->stTotal.XTUCFECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Total.XTURHECErrors")) {
            pstChannelStats->stTotal.XTURHECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Total.XTUCHECErrors")) {
            pstChannelStats->stTotal.XTUCHECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Total.XTURCRCErrors")) {
            pstChannelStats->stTotal.XTURCRCErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Total.XTUCCRCErrors")) {
            pstChannelStats->stTotal.XTUCCRCErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Showtime.XTURFECErrors")) {
            pstChannelStats->stShowTime.XTURFECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Showtime.XTUCFECErrors")) {
            pstChannelStats->stShowTime.XTUCFECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Showtime.XTURHECErrors")) {
            pstChannelStats->stShowTime.XTURHECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Showtime.XTUCHECErrors")) {
            pstChannelStats->stShowTime.XTUCHECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Showtime.XTURCRCErrors")) {
            pstChannelStats->stShowTime.XTURCRCErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "Showtime.XTUCCRCErrors")) {
            pstChannelStats->stShowTime.XTUCCRCErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "LastShowtime.XTURFECErrors")) {
            pstChannelStats->stLastShowTime.XTURFECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "LastShowtime.XTUCFECErrors")) {
            pstChannelStats->stLastShowTime.XTUCFECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "LastShowtime.XTURHECErrors")) {
            pstChannelStats->stLastShowTime.XTURHECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "LastShowtime.XTUCHECErrors")) {
            pstChannelStats->stLastShowTime.XTUCHECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "LastShowtime.XTURCRCErrors")) {
            pstChannelStats->stLastShowTime.XTURCRCErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "LastShowtime.XTUCCRCErrors")) {
            pstChannelStats->stLastShowTime.XTUCCRCErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentDay.XTURFECErrors")) {
            pstChannelStats->stCurrentDay.XTURFECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentDay.XTUCFECErrors")) {
            pstChannelStats->stCurrentDay.XTUCFECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentDay.XTURHECErrors")) {
            pstChannelStats->stCurrentDay.XTURHECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentDay.XTUCHECErrors")) {
            pstChannelStats->stCurrentDay.XTUCHECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentDay.XTURCRCErrors")) {
            pstChannelStats->stCurrentDay.XTURCRCErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentDay.XTUCCRCErrors")) {
            pstChannelStats->stCurrentDay.XTUCCRCErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "X_RDK_LinkRetrain")) {
            if (strstr (resp_param.name, "CurrentDay.X_RDK_LinkRetrain")) {
               pstChannelStats->stCurrentDay.X_RDK_LinkRetrain = atoi(resp_param.value);
            }
            else {
               pstChannelStats->stQuarterHour.X_RDK_LinkRetrain = atoi(resp_param.value);
            }
        }
        else if (strstr (resp_param.name, "CurrentDay.X_RDK_InitErrors")) {
            pstChannelStats->stCurrentDay.X_RDK_InitErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentDay.X_RDK_InitTimeouts")) {
            pstChannelStats->stCurrentDay.X_RDK_InitTimeouts = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentDay.X_RDK_SeverelyErroredSecs")) {
            pstChannelStats->stCurrentDay.X_RDK_SeverelyErroredSecs = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "CurrentDay.X_RDK_ErroredSecs")) {
            pstChannelStats->stCurrentDay.X_RDK_ErroredSecs = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "QuarterHour.XTURFECErrors")) {
            pstChannelStats->stQuarterHour.XTURFECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "QuarterHour.XTUCFECErrors")) {
            pstChannelStats->stQuarterHour.XTUCFECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "QuarterHour.XTURHECErrors")) {
            pstChannelStats->stQuarterHour.XTURHECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "QuarterHour.XTUCHECErrors")) {
            pstChannelStats->stQuarterHour.XTUCHECErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "QuarterHour.XTURCRCErrors")) {
            pstChannelStats->stQuarterHour.XTURCRCErrors = atol(resp_param.value);
        }
        else if (strstr (resp_param.name, "QuarterHour.XTUCCRCErrors")) {
            pstChannelStats->stQuarterHour.XTUCCRCErrors = atol(resp_param.value);
        }
    }
    // Free json objects
    FREE_JSON_OBJECT(jmsg);
    FREE_JSON_OBJECT(jreply_msg);
    return rc;
}

