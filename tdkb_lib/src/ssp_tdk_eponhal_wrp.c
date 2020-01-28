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

#include "ssp_tdk_eponhal_wrp.h"
#include "ssp_hal_logger.h"

/*******************************************************************************************
 *
 * Function Name        : ssp_EPONHAL_GetParamUlongValue
 * Description          : This function will invoke the hal api of epon to get the ulong values
 *
 * @param [in]          : paramName: specifies the name of the API
 *                        value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_EPONHAL_GetParamUlongValue(char* paramName, unsigned long* value)
{
    int return_status = RETURN_ERR;
    unsigned short llidEntry = 0;

    DEBUG_PRINT(DEBUG_TRACE,"\n ssp_EPONHAL_GetParamUlongValue ----> Entry\n");
    CHECK_PARAM_AND_RET(value);

    if( !(strcmp(paramName, "NumberOfNetworkPorts")) )
    {
        return_status = dpoe_getNumberOfNetworkPorts(value);
        DEBUG_PRINT(DEBUG_TRACE,"Return status of dpoe_getNumberOfNetworkPorts %d", return_status);

        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the EPON NumberOfNetworkPorts\n");
        }
    }
    else if( !(strcmp(paramName, "NumberOfS1Interfaces")) )
    {
        return_status = dpoe_getNumberOfS1Interfaces(value);
        DEBUG_PRINT(DEBUG_TRACE, "Return status of dpoe_getNumberOfS1Interfaces %d", return_status);
        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get the Number Of S1 Interfaces\n");
        }
    }
    else if( !(strcmp(paramName, "LlidForwardingStateGetEntryCount")) )
    {
        return_status = dpoe_LlidForwardingStateGetEntryCount(&llidEntry);
        *value = llidEntry;
        DEBUG_PRINT(DEBUG_TRACE, "Return status of dpoe_LlidForwardingStateGetEntryCount %d %u %lu", return_status, llidEntry, value);
        if ( return_status != RETURN_OK)
        {
            DEBUG_PRINT(DEBUG_ERROR,"ssp_EPONHAL_GetParamUlongValue : Failed to get LlidForwardingStateGetEntryCount\n");
        }
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR,"Invalid parameter name");
    }

    DEBUG_PRINT(DEBUG_TRACE,"\n ssp_EPONHAL_GetParamUlongValue ----> Exit\n");

    return return_status;
}