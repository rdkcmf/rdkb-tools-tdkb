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

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>
#include "ssp_tdk_mtahal_wrp.h"

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_GetParamCharValue
 * Description          : This function will invoke the hal api of MTA to get the char values
 *
 * @param [in]          : paramName: specifies the name of the API
 *                        value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_GetParamCharValue(char* paramName, char* value)
{
    int return_status = SSP_SUCCESS;
    char val[32];
    unsigned long len = sizeof(val);
    MTAMGMT_MTA_BATTERY_INFO batteryInfo;

    printf("\n ssp_MTAHAL_GetParamCharValue ----> Entry\n");

    if( !(strcmp(paramName, "BatteryPowerStatus")) )
    {
        return_status = mta_hal_BatteryGetPowerStatus(value, &len);
        printf("Return status of mta_hal_BatteryGetPowerStatus %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamCharValue : Failed to get the Battery Power Status\n");
            return SSP_FAILURE;
        }        
    }
    else if( !(strcmp(paramName, "BatteryCondition")) )
    {
        return_status = mta_hal_BatteryGetCondition(value, &len);
        printf("Return status of mta_hal_BatteryGetCondition %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamCharValue : Failed to get the Battery Condition\n");
            return SSP_FAILURE;
        }        
    }
    else if( !(strcmp(paramName, "BatteryStatus")) )
    {
        return_status = mta_hal_BatteryGetStatus(value, &len);
        printf("Return status of mta_hal_BatteryGetStatus %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamCharValue : Failed to get the Battery Status\n");
            return SSP_FAILURE;
        }        
    }
    else if( !(strcmp(paramName, "BatteryLife")) )
    {
        return_status = mta_hal_BatteryGetLife(value, &len);
        printf("Return status of mta_hal_BatteryGetLife %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamCharValue : Failed to get the Battery Life\n");
            return SSP_FAILURE;
        }        
    }
    else if( !(strcmp(paramName, "BatteryInfo")) )
    {
        if (value == NULL)
        {
           return_status = mta_hal_BatteryGetInfo(NULL);
        }
        else
        {
           return_status = mta_hal_BatteryGetInfo(&batteryInfo);
        }
        printf("Return status of mta_hal_BatteryGetInfo %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamCharValue : Failed to get the Battery Info\n");
            return SSP_FAILURE;
        }        
        sprintf( value, "Model Number: %s Serial Number: %s Part Number: %s Charger Firmware Revision: %s", batteryInfo.ModelNumber, batteryInfo.SerialNumber, batteryInfo.PartNumber, batteryInfo.ChargerFirmwareRevision );
    }
    else
    {
        printf("Invalid parameter name");
        return_status = SSP_FAILURE;
    }

    printf("\n ssp_MTAHAL_GetParamCharValue ----> Exit\n");

    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_GetParamUlongValue
 * Description          : This function will invoke the hal api of MTA to get the ulong values
 *
 * @param [in]          : paramName: specifies the name of the API
 *                        value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_GetParamUlongValue(char* paramName, unsigned long* value)
{
    int return_status = SSP_SUCCESS;
    unsigned long lineTableNumOfEntries = 0;
    BOOLEAN dectEnable = FALSE;
    BOOLEAN batteryInstalled = FALSE;
    unsigned long val = 0;

    printf("\n ssp_MTAHAL_GetParamUlongValue ----> Entry\n");

    if( !(strcmp(paramName, "LineTableNumberOfEntries")) )
    {
        lineTableNumOfEntries = mta_hal_LineTableGetNumberOfEntries();
        printf("Return status of mta_hal_LineTableGetNumberOfEntries %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the MTA Line Table Number of Entries\n");
            return SSP_FAILURE;
        }        
        *value = lineTableNumOfEntries;
    }    
    else if( !(strcmp(paramName, "DSXLogEnable")) )
    {
        return_status = mta_hal_GetDSXLogEnable((unsigned char*)value);
        printf("Return status of mta_hal_GetDSXLogEnable %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the MTA DSX Log Enable\n");
            return SSP_FAILURE;
        }        
    }    
    else if( !(strcmp(paramName, "CallSignallingLogEnable")) )
    {
        return_status = mta_hal_GetCallSignallingLogEnable((unsigned char*)value);
        printf("Return status of mta_hal_GetCallSignallingLogEnable %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_SetParamUlongValue : Failed to get the MTA Call Signalling Log Enable\n");
            return SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "DectEnable")) )
    {
        return_status = mta_hal_DectGetEnable(&dectEnable);
        printf("Return status of mta_hal_DectGetEnable %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_SetParamUlongValue : Failed to get the MTA DECT Enable\n");
            return SSP_FAILURE;
        }
        *value = dectEnable;
    }
    else if( !(strcmp(paramName, "BatteryInstalled")) )
    {
        return_status = mta_hal_BatteryGetInstalled(&batteryInstalled);
        printf("Return status of mta_hal_BatteryGetInstalled %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the Battery Installed\n");
            return SSP_FAILURE;
        }        
        *value = batteryInstalled;
    }
    else if( !(strcmp(paramName, "BatteryTotalCapacity")) )
    {
        return_status = mta_hal_BatteryGetTotalCapacity(&val);
        printf("Return status of mta_hal_BatteryGetTotalCapacity %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the Battery Total Capacity\n");
            return SSP_FAILURE;
        }        
        *value = val;
    }
    else if( !(strcmp(paramName, "BatteryActualCapacity")) )
    {
        return_status = mta_hal_BatteryGetActualCapacity(&val);
        printf("Return status of mta_hal_BatteryGetActualCapacity %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the Battery Actual Capacity\n");
            return SSP_FAILURE;
        }        
        *value = val;
    }
    else if( !(strcmp(paramName, "BatteryRemainingCharge")) )
    {
        return_status = mta_hal_BatteryGetRemainingCharge(value);
        printf("Return status of mta_hal_BatteryGetRemainingCharge %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the Battery Remaining Charge\n");
            return SSP_FAILURE;
        }        
    }
    else if( !(strcmp(paramName, "BatteryRemainingTime")) )
    {
        return_status = mta_hal_BatteryGetRemainingTime(value);
        printf("Return status of mta_hal_BatteryGetRemainingTime %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the Battery Remaining Time\n");
            return SSP_FAILURE;
        }        
    }
    else if( !(strcmp(paramName, "BatteryNumberofCycles")) )
    {
        return_status = mta_hal_BatteryGetNumberofCycles(value);
        printf("Return status of mta_hal_BatteryGetNumberofCycles %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the Battery Number of Cycles\n");
            return SSP_FAILURE;
        }        
    }
    else if( !(strcmp(paramName, "BatteryPowerSavingModeStatus")) )
    {
        return_status = mta_hal_BatteryGetPowerSavingModeStatus(&val);
        printf("Return status of mta_hal_BatteryGetPowerSavingModeStatus %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the Battery Power Saving Mode Status\n");
            return SSP_FAILURE;
        }        
        *value = val;
    }
    else if( !(strcmp(paramName, "MTAResetCount")) )
    {
        return_status = mta_hal_Get_MTAResetCount(value);
        printf("Return status of mta_hal_Get_MTAResetCount %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the MTA Reset Count\n");
            return SSP_FAILURE;
        }        
    }
    else if( !(strcmp(paramName, "LineResetCount")) )
    {
        return_status = mta_hal_Get_LineResetCount(value);
        printf("Return status of mta_hal_Get_LineResetCount %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the Line Reset Count\n");
            return SSP_FAILURE;
        }        
    }
    else
    {
        printf("Invalid parameter name");
        return_status = SSP_FAILURE;
    }

    printf("\n ssp_MTAHAL_GetParamUlongValue ----> Exit\n");

    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_SetParamUlongValue
 * Description          : This function will invoke the hal api of MTA to set the ulong values
 *
 * @param [in]          : paramName: specifies the name of the API
 *                        value: the value to set the hal api
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_SetParamUlongValue(char* paramName, unsigned long value)
{
    int return_status = SSP_SUCCESS;

    printf("\n ssp_MTAHAL_SetParamUlongValue ----> Entry\n");

    if( !(strcmp(paramName, "DSXLogEnable")) )
    {
        return_status = mta_hal_SetDSXLogEnable((BOOLEAN)value);
        printf("Return status of mta_hal_SetDSXLogEnable(%lu) %d", value, return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_SetParamUlongValue : Failed to set the MTA DSX Log Enable\n");
            return SSP_FAILURE;
        }        
    }    
    else if( !(strcmp(paramName, "ClearDSXLog")) )
    {
        return_status = mta_hal_ClearDSXLog((BOOLEAN)value);
        printf("Return status of mta_hal_ClearDSXLog(%lu) %d", value, return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_SetParamUlongValue : Failed to set the MTA DSX Log Enable\n");
            return SSP_FAILURE;
        }        
    }
    else if( !(strcmp(paramName, "CallSignallingLogEnable")) )
    {
        return_status = mta_hal_SetCallSignallingLogEnable((BOOLEAN)value);
        printf("Return status of mta_hal_SetCallSignallingLogEnable(%lu) %d", value, return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_SetParamUlongValue : Failed to set the MTA Call Signalling Log Enable\n");
            return SSP_FAILURE;
        }        
    }
    else if( !(strcmp(paramName, "ClearCallSignallingLog")) )
    {
        return_status = mta_hal_ClearCallSignallingLog((BOOLEAN)value);
        printf("Return status of mta_hal_ClearCallSignallingLog(%lu) %d", value, return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_SetParamUlongValue : Failed to set the MTA Call Signalling Log Enable\n");
            return SSP_FAILURE;
        }        
    }
    else
    {
        printf("Invalid parameter name");
        return_status = SSP_FAILURE;
    }

    printf("\n ssp_MTAHAL_SetParamUlongValue ----> Exit\n");
    return return_status;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_GetDHCPInfo
 * Description          : This function will invoke the hal api of MTA to get the MTA DHCP info
 * 
 * @param [in]          : pInfo: MTA DHCP info
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_GetDHCPInfo(PMTAMGMT_MTA_DHCP_INFO pInfo)
{
    int return_status = SSP_SUCCESS;

    printf("\n ssp_MTAHAL_GetDHCPInfo ----> Entry\n");

    return_status = mta_hal_GetDHCPInfo(pInfo);
    printf("return value from mta_hal_GetDHCPInfo is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_GetDHCPInfo::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_GetDHCPInfo::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_GetDHCPInfo ----> Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_GetLineTableGetEntry
 * Description          : This function will invoke the hal api of MTA to get the get entry 
 *                        of the line table at the given index
 *
 * @param [in]          : index: specifies the index of the line table
 *                        pEntry: MTA line table info
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_GetLineTableGetEntry(unsigned long index, PMTAMGMT_MTA_LINETABLE_INFO pEntry)
{
    int return_status = SSP_SUCCESS;
    
    printf("\n ssp_MTAHAL_GetLineTableGetEntry ----> Entry\n");

    return_status = mta_hal_LineTableGetEntry(index, pEntry);
    
    printf("return value from mta_hal_LineTableGetEntry is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_GetLineTableGetEntry::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_GetLineTableGetEntry::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_GetLineTableGetEntry ----> Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_TriggerDiagnostics
 * Description          : This function will Trigger GR909 Diagnostics 
 * 
 * @param [in]          : index - line number
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_TriggerDiagnostics(unsigned long index)
{
    int return_status = SSP_SUCCESS;
    
    printf("\n ssp_MTAHAL_TriggerDiagnostics ----> Entry\n");

    return_status = mta_hal_TriggerDiagnostics(index);
    
    printf("return value from mta_hal_TriggerDiagnostics is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_TriggerDiagnostics::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_TriggerDiagnostics::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_TriggerDiagnostics ----> Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_GetServiceFlow
 * Description          : This function will invoke the hal api of MTA to get all the 
 *                        service flow info
 * 
 * @param [in]          : Count - number of service flow entries, to be returned
 *                        ppCfg - service flow info, to be returned
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_GetServiceFlow(unsigned long* count, PMTAMGMT_MTA_SERVICE_FLOW *ppCfg)
{
    int return_status = SSP_SUCCESS;

    printf("\n ssp_MTAHAL_GetServiceFlow ----> Entry\n");

    return_status = mta_hal_GetServiceFlow(count, ppCfg);
    printf("return value from mta_hal_GetServiceFlow is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_GetServiceFlow::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_GetServiceFlow::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_GetServiceFlow ----> Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_GetCalls
 * Description          : This function will invoke the hal api of MTA to retrieve all call 
 *                        info for the given instance number of LineTable 
 * 
 * @param [in]          : instanceNumber - LineTable's instance number
 *                        count - number of entries(calls) for the call info array, to be returned
 *                        ppCfg - Array of call info, to be returned
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_GetCalls(unsigned long instanceNumber, unsigned long* count, PMTAMGMT_MTA_CALLS *ppCfg)
{
    int return_status = SSP_SUCCESS;

    printf("\n ssp_MTAHAL_GetCalls ----> Entry\n");

    return_status = mta_hal_GetCalls(instanceNumber, count, ppCfg);
    printf("return value from mta_hal_GetCalls is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_GetCalls::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_GetCalls::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_GetCalls ----> Exit\n");

}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_GetCALLP
 * Description          : This function will invoke the hal api of MTA to retrieve the CALLP  
 *                        status info for the line number 
 * 
 * @param [in]          : instanceNumber - LineTable's instance number
 *                        count - number of entries(calls) for the call info array, to be returned
 *                        ppCfg - Array of call info, to be returned
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_GetCALLP(unsigned long lineNumber, PMTAMGMT_MTA_CALLP pCallp)
{
    int return_status = SSP_SUCCESS;

    printf("\n ssp_MTAHAL_GetCALLP ----> Entry\n");

    return_status = mta_hal_GetCALLP(lineNumber, pCallp);
    printf("return value from mta_hal_GetCALLP is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_GetCALLP::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_GetCALLP::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_GetCALLP ----> Exit\n");

}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_GetDSXLogs
 * Description          : This function will invoke the hal api of MTA to retrieve the CALLP  
 *                        status info for the line number 
 * 
 * @param [in]          : count - number of entries in the log, to be returned
 *                        ppDSXLog - array of log entries, to be returned
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_GetDSXLogs(unsigned long* count, PMTAMGMT_MTA_DSXLOG* ppDSXLog)
    {
        int return_status = SSP_SUCCESS;
    
        printf("\n ssp_MTAHAL_GetDSXLogs ----> Entry\n");
    
        return_status = mta_hal_GetDSXLogs(count, ppDSXLog);
        printf("return value from mta_hal_GetDSXLogs is %d\n",return_status);
        
        if(return_status != SSP_SUCCESS)
        {
            printf("\nssp_MTAHAL_GetDSXLogs::Failed\n");
            return SSP_FAILURE;
        }
        else
        {
            printf("\nssp_MTAHAL_GetDSXLogs::Success\n");
            return return_status;
        }
        printf("\n ssp_MTAHAL_GetDSXLogs ----> Exit\n");
    
    }

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_GetMtaLog
 * Description          : This function will invoke the hal api of MTA to retrieve Get all 
 *                        log entries from the MTA Log  
 * 
 * @param [in]          : count - number of entries in the log, to be returned
 *                        ppConf - array of log entries, to be returned
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_GetMtaLog(unsigned long* count, PMTAMGMT_MTA_MTALOG_FULL* ppConf)
    {
        int return_status = SSP_SUCCESS;
    
        printf("\n ssp_MTAHAL_GetMtaLog ----> Entry\n");
    
        return_status = mta_hal_GetMtaLog(count, ppConf);
        printf("return value from mta_hal_GetMtaLog is %d\n",return_status);
        
        if(return_status != SSP_SUCCESS)
        {
            printf("\nssp_MTAHAL_GetMtaLog::Failed\n");
            return SSP_FAILURE;
        }
        else
        {
            printf("\nssp_MTAHAL_GetMtaLog::Success\n");
            return return_status;
        }
        printf("\n ssp_MTAHAL_GetMtaLog ----> Exit\n");
    
    }

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_getDhcpStatus
 * Description          : This function will invoke the hal api of MTA to get the DHCP status
 *                        for MTA
 * 
 * @param [in]          : output_pIpv4status - ipv4 dhcp status, to be returned
 *                        output_pIpv6status - ipv6 dhcp status, to be returned
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_getDhcpStatus(MTAMGMT_MTA_STATUS *output_pIpv4status, MTAMGMT_MTA_STATUS *output_pIpv6status)
{
    int return_status = SSP_SUCCESS;

    printf("\n ssp_MTAHAL_getDhcpStatus ----> Entry\n");

    return_status = mta_hal_getDhcpStatus(output_pIpv4status, output_pIpv6status);
    printf("return value from mta_hal_getDhcpStatus is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_getDhcpStatus::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_getDhcpStatus::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_getDhcpStatus ----> Exit\n");

}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_getConfigFileStatus
 * Description          : This function will invoke the hal api of MTA to get the the config 
 *                        file status
 * 
 * @param [in]          : poutput_status - config file status
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_getConfigFileStatus(MTAMGMT_MTA_STATUS *poutput_status)
{
    int return_status = SSP_SUCCESS;

    printf("\n ssp_MTAHAL_getConfigFileStatus ----> Entry\n");

    return_status = mta_hal_getConfigFileStatus(poutput_status);
    printf("return value from mta_hal_getConfigFileStatus is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_getConfigFileStatus::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_getConfigFileStatus::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_getConfigFileStatus ----> Exit\n");

}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_getLineRegisterStatus
 * Description          : This function will invoke the hal api of MTA to get the register 
 *                        status for all lines 
 * 
 * @param [in]          : poutput_status - array buffer for all line register status
 *                        array_size - buffer size (total line number)
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_getLineRegisterStatus(MTAMGMT_MTA_STATUS *output_status_array, int array_size)
{
    int return_status = SSP_SUCCESS;

    printf("\n ssp_MTAHAL_getLineRegisterStatus ----> Entry\n");

    return_status = mta_hal_getLineRegisterStatus(output_status_array, array_size);
    printf("return value from mta_hal_getLineRegisterStatus is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_getLineRegisterStatus::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_getLineRegisterStatus::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_getLineRegisterStatus ----> Exit\n");

}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_GetHandsets
 * Description          : This function will invoke the hal api of MTA to retrieve the CALLP
 *                        status info for the line number
 *
 * @param [in]          : count - number of handset instances, to be returned
 *                        ppHandsets - array of handset entries, to be returned
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_MTAHAL_GetHandsets(unsigned long* count, PMTAMGMT_MTA_HANDSETS_INFO* ppHandsets)
{
    int return_status = SSP_SUCCESS;

    printf("\n ssp_MTAHAL_GetHandsets ----> Entry\n");

    return_status = mta_hal_GetHandsets(count, ppHandsets);
    printf("return value from mta_hal_GetHandsets is %d\n",return_status);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_GetHandsets::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_GetHandsets::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_GetHandsets ----> Exit\n");

}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_InitDB
 * Description          : This function will invoke the hal api of MTA to init the MTA
 *
 * @param [in]          :  paramName:

 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_MTAHAL_InitDB(void)
{
    int return_status = 0;
    printf("\n ssp_MTAHAL_InitDB ----> Entry\n");

    return_status = mta_hal_InitDB();
    printf("return value from ssp_MTAHAL_InitDB is %d\n",return_status);

    if( return_status != SSP_SUCCESS )
    {
        printf("\nssp_MTAHAL_InitDB::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_InitDB::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_InitDB ----> Exit\n");

}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_devResetNow
 * Description          : This function will invoke the hal api of MTA to reset MTA device
 *
 * @param [in]          :  paramName:

 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_MTAHAL_devResetNow(void)
{
    int return_status = 0;
    printf("\n ssp_MTAHAL_devResetNow ----> Entry\n");

    return_status = mta_hal_devResetNow(TRUE);
    printf("return value from ssp_MTAHAL_devResetNow is %d\n",return_status);

    if( return_status != SSP_SUCCESS )
    {
        printf("\nssp_MTAHAL_devResetNow::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_devResetNow::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_devResetNow ----> Exit\n");

}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_getMtaOperationalStatus
 * Description          : This function will invoke the hal api of MTA to get the operational 
 *                        status for the MTA device
 * 
 * @param [in]          : poperationalStatus - MTA operational status
 *
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_MTAHAL_getMtaOperationalStatus(MTAMGMT_MTA_STATUS *operationalStatus)
{
    int return_status = SSP_SUCCESS;

    printf("\n ssp_MTAHAL_getMtaOperationalStatus ----> Entry\n");

    return_status = mta_hal_getMtaOperationalStatus(operationalStatus);
    printf("return value from mta_hal_getMtaOperationalStatus is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_getMtaOperationalStatus::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_getMtaOperationalStatus::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_getMtaOperationalStatus ----> Exit\n");

}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_start_provisioning
 * Description          : This API call will start IP provisioning for all the lines for IPv4/IPv6 , or dual mode 
 * 
 * @param [in]   : mtaIPMode
 *                      dhcpOption122Suboption1
 *                      dhcpOption122Suboption2
 *                      dhcpOption2171CccV6DssID1
 *                      dhcpOption2171CccV6DssID2
 *
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

static char convert(char c)
{
    char a = 0;
    
    if (isxdigit(c))
        a = isdigit(c) ? (c - 48) : isupper(c) ? (c - 55) : (c - 87);
    else 
        printf("!!! The input is not a hexadecimal digit !!!\n");

    return a;
}

static void str2hex(char *s, char *n)
{
    int i, j, len = strlen(s);
    char c1, c2;

    for (i = 0, j = 0; i < len; i+=2, j++)
    {
        c1 = s[i];
        c2 = s[i+1];
        n[j] = convert(c1) << 4 | convert(c2);
    }
}
 
int ssp_MTAHAL_start_provisioning(int mtaIPMode, char* dhcpOption122Suboption1, char* dhcpOption122Suboption2, char* dhcpOption2171CccV6DssID1, char* dhcpOption2171CccV6DssID2)
{
    int return_status = SSP_SUCCESS;
    MTAMGMT_PROVISIONING_PARAMS parameters;
    int i;

    printf("\n ssp_MTAHAL_start_provisioning ----> Entry\n");

    parameters.MtaIPMode = mtaIPMode;
    str2hex(dhcpOption122Suboption1, parameters.DhcpOption122Suboption1);
    str2hex(dhcpOption122Suboption2, parameters.DhcpOption122Suboption2);
    str2hex(dhcpOption2171CccV6DssID1, parameters.DhcpOption2171CccV6DssID1);
    str2hex(dhcpOption2171CccV6DssID2, parameters.DhcpOption2171CccV6DssID2);

    printf("parameters.MtaIPMode: %u\n", parameters.MtaIPMode);

    printf("parameters.DhcpOption122Suboption1: ");
    for (i=0; i<MTA_DHCPOPTION122SUBOPTION1_MAX; i++)
        printf("%02X ", parameters.DhcpOption122Suboption1[i]);
    printf("\n");

    printf("parameters.DhcpOption122Suboption2: ");
    for (i=0; i<MTA_DHCPOPTION122SUBOPTION2_MAX; i++)
        printf("%02X ", parameters.DhcpOption122Suboption2[i]);
    printf("\n");

    printf("parameters.DhcpOption2171CccV6DssID1: ");
    for (i=0; i<MTA_DHCPOPTION122CCCV6DSSID1_MAX; i++)
        printf("%02X ", parameters.DhcpOption2171CccV6DssID1[i]);
    printf("\n");

    printf("parameters.DhcpOption2171CccV6DssID2: ");
    for (i=0; i<MTA_DHCPOPTION122CCCV6DSSID2_MAX; i++)
        printf("%02X ", parameters.DhcpOption2171CccV6DssID2[i]);
    printf("\n");

    return_status = mta_hal_start_provisioning(&parameters);
    printf("return value from mta_hal_start_provisioning is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_start_provisioning::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_start_provisioning::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_start_provisioning ----> Exit\n");

}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_LineRegisterStatus_callback_register
 * Description          : This call back will be invoked to returing MTA line 
 * 
 * @param [in]          : N/A
 *
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

static int lineRegisterStatus_callback(MTAMGMT_MTA_STATUS *output_status_array, int array_size)
{
    int i;

    if (output_status_array == NULL || array_size < 1)
    {
        printf("The output_status_array array is empty\n");
        return SSP_FAILURE;
    }

    printf("==== Line Register Status Callback ====\n");
    for (i = 0; i < array_size; i++)
    {
        printf("Successfully Getting callback, array_size = %d, output_status_array[%d] = %d\n", array_size, i, output_status_array[i]);
    }
    printf("==== Line Register Status Callback ====\n");

    return SSP_SUCCESS;
}

int ssp_MTAHAL_LineRegisterStatus_callback_register(void)
{
    int return_status = SSP_SUCCESS;

    printf("\n ssp_MTAHAL_LineRegisterStatus_callback_register ----> Entry\n");

    mta_hal_LineRegisterStatus_callback_register(lineRegisterStatus_callback);
    printf("return value from mta_hal_getMtaOperationalStatus is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_LineRegisterStatus_callback_register::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_MTAHAL_LineRegisterStatus_callback_register::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_LineRegisterStatus_callback_register ----> Exit\n");

}

/*******************************************************************************************
 *
 * Function Name        : ssp_MTAHAL_getMtaProvisioningStatus
 * Description          : This function will invoke the hal api of MTA to get the Provisioning
 *                        status for the MTA device
 *
 * @param [in]          : status - MTA operational status
 *
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_MTAHAL_getMtaProvisioningStatus(MTAMGMT_MTA_PROVISION_STATUS *status)
{
    int return_status = SSP_SUCCESS;
    printf("\n ssp_MTAHAL_getMtaProvisioningStatus ----> Entry\n");
    return_status = mta_hal_getMtaProvisioningStatus(status);
    printf("return value from mta_hal_getMtaProvisioningStatus is %d\n",return_status);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_MTAHAL_getMtaProvisioningStatus::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_getMtaProvisioningStatus::Success\n");
        return return_status;
    }
    printf("\n ssp_MTAHAL_getMtaProvisioningStatus ----> Exit\n");
}
