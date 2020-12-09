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


#ifndef __SSP_COSAMTA_WRP_C__
#define __SSP_COSAMTA_WRP_C__

#include "ssp_global.h"
#include "ccsp_dm_api.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include "pthread.h"
#include "ssp_tdk_wrp.h"
#include <pthread.h>
#include <ccsp_message_bus.h>
#include <ccsp_base_api.h>
#include <sys/time.h>
#include <time.h>
#include <signal.h>
#include "ccsp_memory.h"
#include <ccsp_custom.h>
#include <dslh_definitions_database.h>
#include <sys/ucontext.h>


#include "cosa_x_cisco_com_mta_apis.h"

#define BUFFER_LEN 32
#endif

int CosaDmlMTAGetMtaLog(ANSC_HANDLE handle, unsigned long* count, PCOSA_DML_MTALOG_FULL* ppConf);

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMtaGetResetCount
 * Description          : This function will invoke the cosa api of MTA to retrieve the reset count
 *                        value for the specified reset type.
 *
 * @param [in]          : handleType - message bus handle
 * @param [in]          : bufferType - Valid or NULL pointer
 * @param [in]          : pResetType - reset type can be MTAResetcount, LineResetCount or invalid
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMtaGetResetCount(int handleType, int bufferType, char *pResetType, unsigned long* ResetCount)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    MTA_RESET_TYPE resetType = 0;
    ULONG resetCount = 0;

    printf("\n Entering ssp_CosaDmlMtaGetResetCount function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    if((strcmp(pResetType,"MTAResetCount")==0))
    {
        resetType = MTA_RESET;
    }
    else if((strcmp(pResetType,"LineResetCount")==0))
    {
        resetType = LINE_RESET;
    }

    printf("ssp_CosaDmlMtaGetResetCount: Reset Type:%d\n",resetType);

    if(bufferType == 0)
    {
        return_status = CosaDmlMtaGetResetCount(mta_handle,resetType,&resetCount);
    }
    else
    {
        return_status = CosaDmlMtaGetResetCount(mta_handle,resetType,NULL);
    }

    printf("ssp_CosaDmlMtaGetResetCount: ResetCount retrieved:%lu\n",resetCount);
    *ResetCount=(unsigned long)resetCount;

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMtaGetResetCount:Failed to retrieve the reset count\n");
        return SSP_FAILURE;
    }
    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetDHCPInfo
 * Description          : This function will invoke the cosa api of MTA to retrieve the DHCP
 *                        information
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTAGetDHCPInfo(int handleType, int bufferType, void* DHCPInfo)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    PCOSA_MTA_DHCP_INFO *dhcp = NULL;

    printf("\n Entering ssp_CosaDmlMTAGetDHCPInfo function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }
    if(bufferType == 0)
    {
        dhcp = ((PCOSA_MTA_DHCP_INFO *) malloc(sizeof(COSA_MTA_DHCP_INFO)));
        return_status = CosaDmlMTAGetDHCPInfo(mta_handle,(PCOSA_MTA_DHCP_INFO)dhcp);
    }

    else
    {
        return_status = CosaDmlMTAGetDHCPInfo(mta_handle,NULL);
    }


    printf("ssp_CosaDmlMTAGetDHCPInfo: DHCP Info:%p\n",dhcp);
    DHCPInfo=(void*)dhcp;

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTAGetDHCPInfo:Failed to retrieve the DHCP information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTATriggerDiagnostics
 * Description          : This function will invoke the cosa api of MTA to check the index value
 *
 * @param [in]          : index - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTATriggerDiagnostics()
{
    int return_status = 0;
    ULONG index = 0;

    printf("\n Entering ssp_CosaDmlMTATriggerDiagnostics function\n\n");
    return_status = CosaDmlMTATriggerDiagnostics(index);

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTATriggerDiagnostics:Index value is invalid  \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMtaBatteryGetInfo
 * Description          : This function will invoke the cosa api of MTA to retrieve the Battery
 *                        information
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMtaBatteryGetInfo(int handleType, int bufferType, char* BatteryInfo)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    COSA_DML_BATTERY_INFO battery;
    memset(&battery, 0, sizeof(COSA_DML_BATTERY_INFO));

    printf("\n Entering ssp_CosaDmlMtaBatteryGetInfo function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    if(bufferType == 0)
    {
        return_status = CosaDmlMtaBatteryGetInfo(mta_handle,&battery);
	strcpy(BatteryInfo,battery.ModelNumber);

        printf("ssp_CosaDmlMtaBatteryGetInfo: BATTERY Info:\n");
        printf("ModelNumber:%s\n",battery.ModelNumber);
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMtaBatteryGetInfo:Failed to retrieve the BATTERY information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/********************************************************************************************
 *Parameter Name        : ssp_CosaDmlMtaBatteryGetStatus
 * Description          : This function will invoke the cosa api of MTA which will get the
 *                        battery status
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMtaBatteryGetStatus(int handleType, int bufferType, char* BatteryStatus)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    CHAR *value = NULL;
    ULONG size = 0;

    printf("\n Entering ssp_CosaDmlMtaBatteryGetStatus function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    if(bufferType == 0)
    {
        value  = ((CHAR *) malloc(BUFFER_LEN));
        size = BUFFER_LEN;
    }

    return_status = CosaDmlMtaBatteryGetStatus(mta_handle,value,&size);

    printf("ssp_CosaDmlMtaBatteryGetStatus: Battery Status is:%s\n",value);
    strcpy(BatteryStatus ,value);

    if(value)
    {
	free(value);
	value = NULL;
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMtaBatteryGetStatus:Failed to retrieve the BATTERY information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/********************************************************************************************
 *Parameter Name        : ssp_CosaDmlMtaBatteryGetPowerStatus
 * Description          : This function will invoke the cosa api of MTA to retrieve the battery
 *                        power status
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMtaBatteryGetPowerStatus(int handleType, int bufferType,char* Power)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    CHAR *value = NULL;
    ULONG size = 0;

    printf("\n Entering ssp_CosaDmlMtaBatteryGetPowerStatus function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    if(bufferType == 0)
    {
        value  = ((CHAR *) malloc(BUFFER_LEN));
        size = BUFFER_LEN;
    }

    return_status = CosaDmlMtaBatteryGetPowerStatus(mta_handle,value,&size);

    printf("ssp_CosaDmlMtaBatteryGetPowerStatus: Battery Power Status is:%s\n",value);
    strcpy(Power ,value);

    if(value)
    {
        free(value);
        value = NULL;
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMtaBatteryGetPowerStatus:Failed to retrieve the BATTERY information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/********************************************************************************************
 *Parameter Name        : ssp_CosaDmlMtaLineTableGetNumberOfEntries
 * Description          : This function will invoke the cosa api of MTA to retrieve the Line
 *                        table number of entries
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMtaLineTableGetNumberOfEntries(int handleType, unsigned long* lineTableNumOfEntries)
{
    ANSC_HANDLE mta_handle = NULL;
    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
        if(lineTableNumOfEntries)
        {
             *lineTableNumOfEntries = CosaDmlMTALineTableGetNumberOfEntries(mta_handle);
             printf("ssp_CosaDmlMtaLineTableGetNumberOfEntries info:%lu\n",*lineTableNumOfEntries);
        }
        else
        {
            printf("ssp_CosaDmlMtaLineTableGetNumberOfEntries: Error, NULL buffer passed  \n");
            return SSP_FAILURE;
        }
    }
    return SSP_SUCCESS;
}
/********************************************************************************************
 * Parameter Name       : ssp_CosaDmlMtaLineTableGetEntry
 * Description          : This function will invoke the cosa api of MTA to retrieve the Line
 *                        table get entry
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMtaLineTableGetEntry(int handleType,int bufferType, unsigned long* TableEntry)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    ULONG value = 0;
    COSA_MTA_LINETABLE_INFO entry = {0};

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;

    }
    if(bufferType == 0)
    {
        return_status = CosaDmlMTALineTableGetEntry(mta_handle,value,&entry);
        printf("ssp_CosaDmlMtaLineTableGetEntry: Line Table Status:%lu\n",entry.Status);
	*TableEntry=(unsigned long)entry.Status;
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTALineTableGetEntry:Failed to retrieve the Line Table information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetServiceClass
 * Description          : This function will invoke the cosa api of MTA to retrieve the
 *                        Service class
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTAGetServiceClass(int handleType, void* SerClass)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    ULONG *Count=NULL;
    PCOSA_MTA_SERVICE_CLASS *pfg = NULL;
    mta_handle = bus_handle_client;

    printf("\n Entering ssp_CosaDmlMTAGetServiceClass function\n\n");

    if(handleType == 0)
    {
        Count=(ULONG*)malloc(20*sizeof(ULONG));
        return_status = CosaDmlMTAGetServiceClass(mta_handle,Count,pfg);
    }

    printf("ssp_CosaDmlMTAGetServiceClass: %p\n",pfg);
    SerClass=(void*)pfg;

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTAGetServiceClass:Failed to retrieve the Service class \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTADectGetEnable
 * Description          : This function will invoke the cosa api of MTA to retrieve the
 *                        enable value of Dect
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTADectGetEnable(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    BOOLEAN *bValue = NULL;

    printf("\n Entering ssp_CosaDmlMTADectGetEnable function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }
    if(Value == 0)
    {
        bValue = ((BOOLEAN *) malloc(sizeof(BOOLEAN) * 10));
    }
    return_status = CosaDmlMTADectGetEnable(mta_handle, bValue);
    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTADectGetEnable: Failed to retrieve the Dect enable value\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;

}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTADectSetEnable
 * Description          : This function will invoke the cosa api of MTA to retrieve the
 *                        Set Enable of Dect
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTADectSetEnable(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    UCHAR bValue = TRUE;
    printf("\n Entering ssp_CosaDmlMTADectSetEnable function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;

    }
//    if (Value == 0)
//    {
//        bValue = ((char *) malloc(100));
//    }


    return_status = CosaDmlMTADectSetEnable(mta_handle,bValue);
    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTADectSetEnable:Failed to retrieve the Dect enable\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;


}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTADectGetRegistrationMode
 * Description          : This function will invoke the cosa api of MTA to retrieve the
 *                        Dect registration mode
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTADectGetRegistrationMode(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    BOOLEAN *bValue = NULL;
    printf("\n Entering ssp_CosaDmlMTADectGetRegistrationMode function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;

    }
    if (Value == 0)
    {
        bValue = ((BOOLEAN *) malloc(sizeof(BOOLEAN) * 10));
    }
    return_status = CosaDmlMTADectGetRegistrationMode(mta_handle,bValue);
    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTADectGetRegistrationMode:Failed to retrieve the Dect registration mode\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;


}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTADectSetRegistrationMode
 * Description          : This function will invoke the cosa api of MTA to set the
 *                        dect registration mode
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

 int ssp_CosaDmlMTADectSetRegistrationMode(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    UCHAR bValue = TRUE;
    printf("\n Entering ssp_CosaDmlMTADectSetRegistrationMode function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;

    }

    return_status = CosaDmlMTADectSetRegistrationMode(mta_handle,bValue);
    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTADectSetRegistrationMode:Failed to set the dect registration mode\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;

}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetDect
 * Description          : This function will invoke the cosa api of MTA to retrieve the dect
 *                        information
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
********************************************************************************************/

int ssp_CosaDmlMTAGetDect(int handleType, int bufferType,void* DectInfo)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    PCOSA_MTA_DECT *dect = NULL;

    printf("\n Entering ssp_CosaDmlMTAGetDect function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
        dect = ((PCOSA_MTA_DECT *) malloc(sizeof(COSA_MTA_DECT)));
        return_status = CosaDmlMTAGetDect(mta_handle,(PCOSA_MTA_DECT)dect);

    }
    else
    {
        return_status = CosaDmlMTAGetDect(mta_handle,NULL);
    }

    printf("ssp_CosaDmlMTAGetDect: Dect Info:%p\n",dect);
    DectInfo=(void*)dect;

    if ( return_status != SSP_SUCCESS)

    {
        printf("ssp_CosaDmlMTAGetDect:Failed to retrieve the Dect information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetDectPIN
 * Description          : This function will invoke the cosa api of MTA to retrieve the Dect
 *                        information
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMTAGetDectPIN(int handleType, int bufferType,char *pin)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;

    printf("\n Entering ssp_CosaDmlMTAGetDectPIN function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    if(pin == NULL)
    {
       printf("Pointer passed is NULL\n");
       return SSP_FAILURE;
    }

    printf("Invoking CosaDmlMTAGetDectPIN function\n");
    return_status = CosaDmlMTAGetDectPIN(mta_handle, pin);
    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTAGetDectPIN:Failed to retrieve the Dect pin information \n");
        return SSP_FAILURE;
    }

    printf("value retrieved from CosaDmlMTAGetDectPIN:%s\n",pin);
    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTASetDectPIN
 * Description          : This function will invoke the cosa api of MTA to set the
 *                        dect pin
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMTASetDectPIN(int handleType, int bufferType, char *pin)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;

    printf("\n Entering ssp_CosaDmlMTASetDectPIN function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    if(pin == NULL)
    {
       printf("Pointer passed is NULL\n");
       return SSP_FAILURE;
    }

    printf("Dect Pin to be set:%s\n",pin);
    return_status = CosaDmlMTASetDectPIN(mta_handle, pin);
    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTASetDectPIN:Failed to retrieve the Dect pin information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetDSXLogEnable
 * Description          : This function will invoke the cosa api of MTA to retrieve the DSX Log
 *                        enable
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Invalid or NULL pointer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTAGetDSXLogEnable(int handleType, int Value, int *Bool)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    BOOLEAN bValue = 0;
    printf("\n Entering ssp_CosaDmlMTAGetDSXLogEnable function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    if (Value == 0)
    {
        return_status = CosaDmlMTAGetDSXLogEnable(mta_handle,&bValue);
        printf("DSX Log Status is:%d\n",bValue);
	*Bool=(int)bValue;
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTAGetDSXLogEnable:Failed to retrieve the dsx log enable\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;

}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTASetDSXLogEnable
 * Description          : This function will invoke the cosa api of MTA to set the
 *                        DSX log enable
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTASetDSXLogEnable(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    BOOLEAN bValue = 0;
    printf("\n Entering ssp_CosaDmlMTASetDSXLogEnable function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    return_status = CosaDmlMTASetDSXLogEnable(mta_handle,bValue);
    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTASetDSXLogEnable:Failed to set the DSX log enable\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAClearDSXLog
 * Description          : This function will invoke the cosa api of MTA to clear the DSX log
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTAClearDSXLog(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    BOOLEAN bValue = FALSE;

    printf("\n Entering ssp_CosaDmlMTAClearDSXLog function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    return_status = CosaDmlMTAClearDSXLog(mta_handle,bValue);

    printf("Clear DSX Log:%d\n",bValue);

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTAClearDSXLog:Failed to clear the DSX log\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;


}
/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetCallSignallingLogEnable
 * Description          : This function will invoke the cosa api of MTA to retrieve the
 *                        Call signalling log
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTAGetCallSignallingLogEnable(int handleType, int Value,int *Bool)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    BOOLEAN bValue = 0;
    printf("\n Entering ssp_CosaDmlMTAGetCallSignallingLogEnable function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    if (Value == 0)
    {
        return_status = CosaDmlMTAGetCallSignallingLogEnable(mta_handle,&bValue);
        printf("Call Signalling Log Status:%d\n",bValue);
	*Bool=(int)bValue;
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTAGetCallSignallingLogEnable:Failed to retrieve the call signalling log\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTASetCallSignallingLogEnable
 * Description          : This function will invoke the cosa api of MTA to
 *                        set the call signalling log
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTASetCallSignallingLogEnable(int handleType, int Value)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    BOOLEAN bValue = 0;
    printf("\n Entering ssp_CosaDmlMTASetCallSignallingLogEnable function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    return_status = CosaDmlMTASetCallSignallingLogEnable(mta_handle,bValue);

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTASetCallSignallingLogEnable:Failed to  set the call signalling log\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAClearCallSignallingLog
 * Description          : This function will invoke the cosa api of MTA to clear the
 *                        call signalling log
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTAClearCallSignallingLog(int handleType, int Value)
{

    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    BOOLEAN bValue = FALSE;

    printf("\n Entering ssp_CosaDmlMTAClearCallSignallingLog function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    return_status = CosaDmlMTAClearCallSignallingLog(mta_handle,bValue);

    printf("Clear Call Signalling Log is :%d\n", bValue);
    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMTAClearCallSignallingLog:Failed to clear the call signalling log\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMtaBatteryGetNumberofCycles
 * Description          : This function will invoke the cosa api of MTA to retrieve
 *                        the number of battery cy  Ccles
 *
 * @param [in]          : handleType - Message bus handle
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMtaBatteryGetNumberofCycles(int handleType,unsigned long* Num)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    ULONG val  = 0;

    printf("\n Entering ssp_CosaDmlMtaBatteryGetNumberofCycles function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    return_status = CosaDmlMtaBatteryGetNumberofCycles(mta_handle,&val);

    printf("ssp_CosaDmlMtaBatteryGetNumberofCycles: Number of cycles retrieved:%lu\n",val);
    *Num=(unsigned long)val;

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMtaBatteryGetNumberofCycles:Failed to retrieve the number of cycles\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;

}


/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMtaBatteryGetLife
 * Description          : This function will invoke the cosa api of MTA to retrieve
 *                        the Battery Life
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMtaBatteryGetLife(int handleType, int bufferType,char *Life)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    CHAR *value = NULL;
    ULONG size = 0;

    printf("\n Entering ssp_CosaDmlMtaBatteryGetLife function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    if(bufferType == 0)
    {
        value  = ((CHAR *) malloc(BUFFER_LEN));
	size = BUFFER_LEN;
    }

    return_status = CosaDmlMtaBatteryGetLife(mta_handle,value,&size);

    printf("ssp_CosaDmlMtaBatteryGetLife: Battery Life is:%s\n",value);
    strcpy(Life ,value);

    if(value)
    {
        free(value);
        value = NULL;
    }


    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMtaBatteryGetLife:Failed to retrieve the BATTERY information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMtaBatteryGetCondition
 * Description          : This function will invoke the cosa api of MTA to retrieve
 *                        the Battery Condition
 *
 * @param [in]          : handleType - Message bus handle
 * @param [in]          : bufferType - Value - 0
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMtaBatteryGetCondition(int handleType, int bufferType,char *Cond)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    CHAR *value = NULL;
    ULONG size = 0;

    printf("\n Entering ssp_CosaDmlMtaBatteryGetCondition function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    if(bufferType == 0)
    {
        value  = ((CHAR *) malloc(BUFFER_LEN));
	size = BUFFER_LEN;
    }

    return_status = CosaDmlMtaBatteryGetCondition(mta_handle,value,&size);

    printf("ssp_CosaDmlMtaBatteryGetCondition: BATTERY Condition is:%s\n",value);
    strcpy(Cond ,value);

    if(value)
    {
        free(value);
        value = NULL;
    }

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMtaBatteryGetCondition:Failed to retrieve the BATTERY information \n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}


/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMtaBatteryGetRemainingTime
 * Description          : This function will invoke the cosa api of MTA to retrieve
 *                        the Battery Condition
 *
 * @param [in]          : handleType - Message bus handle
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMtaBatteryGetRemainingTime(int handleType,unsigned long* Num)
{
    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;
    ULONG val  = 0;

    printf("\n Entering ssp_CosaDmlMtaBatteryGetRemainingTime function\n\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    return_status = CosaDmlMtaBatteryGetRemainingTime(mta_handle,&val);

    printf("ssp_CosaDmlMtaBatteryGetRemainingTime: Battery Remaining Time is:%lu\n",val);
    *Num=(unsigned long)val;

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMtaBatteryGetRemainingTime:Failed to retrieve the Battery Remaining Time\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;

}


/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMtaInit
 * Description          : This function will initialize the DML of Cosa Mta
 *
 * @param [in]          : None
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMtaInit(void)
{

    int return_status = 0;
    ANSC_HANDLE mta_handle = NULL;

    printf("\n Entering ssp_CosaDmlMtaInit function\n\n");

    mta_handle = bus_handle_client;

    return_status = CosaDmlMTAInit(NULL,(PANSC_HANDLE)mta_handle);

    if ( return_status != SSP_SUCCESS)
    {
        printf("ssp_CosaDmlMtaInit:Failed to Initialize the DML of Cosa Mta\n");
        return SSP_FAILURE;
    }

    return SSP_SUCCESS;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetServiceFlow
 * Description          : This function will invoke the cosa api of MTA to retrieve
 *                        the ServiceFlow
 *
 * @param [in]                       : handleType - Message bus handle
 * @param [unsigned long*]           : count - No: of service flow entries
 * @param [PCOSA_MTA_SERVICE_FLOW *] : ppCfg - Service flow buffer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMTAGetServiceFlow(int handleType, unsigned long* count, PMTA_SERVICE_FLOW *ppCfg)
{
    int return_status = SSP_SUCCESS;
    ANSC_HANDLE mta_handle = NULL;
    printf("\n ssp_CosaDmlMTAGetServiceFlow -----> Entry\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    return_status = CosaDmlMTAGetServiceFlow(mta_handle, count, (PCOSA_MTA_SERVICE_FLOW *)ppCfg);
    printf("return value from ssp_CosaDmlMTAGetServiceFlow is %d\n",return_status);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_CosaDmlMTAGetServiceFlow::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_CosaDmlMTAGetServiceFlow::Success\n");
        return return_status;
    }
    printf("\n ssp_CosaDmlMTAGetServiceFlow ----> Exit\n");
}


/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetDSXLogs
 * Description          : This function will invoke the cosa api of MTA to retrieve
 *                        the DSXLogs
 *
 * @param [in]                       : handleType - Message bus handle
 * @param [unsigned long*]           : count - No: of DSX log entries
 * @param [PCOSA_MTA_SERVICE_FLOW *] : ppDSXLog - DSX log buffer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMTAGetDSXLogs(int handleType, unsigned long* count, PMTA_DSXLOG *ppDSXLog)
{
    int return_status = SSP_SUCCESS;
    ANSC_HANDLE mta_handle = NULL;
    printf("\n ssp_CosaDmlMTAGetDSXLog -----> Entry\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    return_status = CosaDmlMTAGetDSXLogs(mta_handle, count, (PCOSA_MTA_DSXLOG *)ppDSXLog);
    printf("return value from ssp_CosaDmlMTAGetDSXLogs is %d\n",return_status);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_CosaDmlMTAGetDSXLogs::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_CosaDmlMTAGetDSXLogs::Success\n");
        return return_status;
    }
    printf("\n ssp_CosaDmlMTAGetDSXLogs ----> Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetMtaLog
 * Description          : This function will invoke the cosa api of MTA to retrieve
 *                        the MTALog
 *
 * @param [in]                       : handleType - Message bus handle
 * @param [unsigned long*]           : count - No: of MTA log entries
 * @param [PCOSA_MTA_SERVICE_FLOW *] : ppConf - MTA log buffer
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMTAGetMtaLog(int handleType, unsigned long* count, PDML_MTALOG_FULL *ppConf)
{
    int return_status = SSP_SUCCESS;
    ANSC_HANDLE mta_handle = NULL;
    printf("\n ssp_CosaDmlMTAGetMtaLog -----> Entry\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }
    return_status = CosaDmlMTAGetMtaLog(mta_handle, count, (PCOSA_DML_MTALOG_FULL *)ppConf);
    printf("return value from ssp_CosaDmlMTAGetMtaLog is %d\n",return_status);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_ssp_CosaDmlMTAGetMtaLog::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_ssp_CosaDmlMTAGetMtaLog::Success\n");
        return return_status;
    }
    printf("\n ssp_ssp_CosaDmlMTAGetMtaLog ----> Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetDhcpStatus
 * Description          : This function will invoke the cosa api of MTA to retrieve
 *                        the DhcpStatus
 *
 * @param [unsigned long*]           : output_pIpv4status - IPV4 status
 * @param [unsigned long*]           : output_pIpv6status - IPV6 status
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMTAGetDhcpStatus(unsigned long* output_pIpv4status, unsigned long* output_pIpv6status)
{
    int return_status = SSP_SUCCESS;
    printf("\n ssp_CosaDmlMTAGetDhcpStatus -----> Entry\n");

    return_status = CosaDmlMtaGetDhcpStatus(output_pIpv4status, output_pIpv6status);
    printf("return value from CosaDmlMtaGetDhcpStatus is %d\n",return_status);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_CosaDmlMTAGetDhcpStatus::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_CosaDmlMTAGetDhcpStatus::Success\n");
        return return_status;
    }
    printf("\n ssp_CosaDmlMTAGetDhcpStatus ----> Exit\n");
}


/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetConfigFileStatus
 * Description          : This function will invoke the cosa api of MTA to retrieve
 *                        the ConfigFileStatus
 *
 * @param [in]                       
 * @param [unsigned long*]           : poutput_status - ConfigFileStatus
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMTAGetConfigFileStatus(unsigned long* poutput_status)
{
    int return_status = SSP_SUCCESS;
    printf("\n ssp_CosaDmlMTAGetConfigFileStatus -----> Entry\n");

    return_status = CosaDmlMtaGetConfigFileStatus(poutput_status);
    printf("return value from CosaDmlMtaGetConfigFileStatus is %d\n",return_status);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_CosaDmlMTAGetConfigFileStatus::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_CosaDmlMTAGetConfigFileStatus::Success\n");
        return return_status;
    }
    printf("\n ssp_CosaDmlMTAGetConfigFileStatus ----> Exit\n");
}


/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetLineRegisterStatus
 * Description          : This function will invoke the cosa api of MTA to retrieve
 *                        the LineRegisterStatus
 *
 * @param [in]                       : 
 * @param [unsigned long*]           : pcLineRegisterStatus- LineRegisterStatus
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMTAGetLineRegisterStatus(char* pcLineRegisterStatus)
{
    int return_status = SSP_SUCCESS;
    printf("\n ssp_CosaDmlMTAGetLineRegisterStatus ----> Entry\n");

    return_status = CosaDmlMtaGetLineRegisterStatus(pcLineRegisterStatus);
    printf("return value from CosaDmlMtaGetLineRegisterStatus is %d\n",return_status);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_CosaDmlMTAGetLineRegisterStatus::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_CosaDmlMTAGetLineRegisterStatus::Success\n");
        return return_status;
    }
    printf("\n ssp_CosaDmlMTAGetLineRegisterStatus ----> Exit\n");
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetParamUlongValue
 * Description          : This function will invoke the hal api of MTA to get the ulong values
 *
 * @param [in]          : paramName: specifies the name of the API
                        : handleType - Message bus handle
 *                        value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMTAGetParamUlongValue(int handleType, char* paramName, unsigned long* value)
{
    int return_status = SSP_SUCCESS;
    ANSC_HANDLE mta_handle = NULL;
    BOOL batteryInstalled = FALSE;

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    if( !(strcmp(paramName, "BatteryInstalled")) )
    {
        return_status = CosaDmlMtaBatteryGetInstalled(mta_handle, &batteryInstalled);
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
        return_status = CosaDmlMtaBatteryGetTotalCapacity(mta_handle, value);
        printf("Return status of CosaDmlMtaBatteryGetTotalCapacity %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("CosaDmlMtaBatteryGetTotalCapacity : Failed to get the Battery Total Capacity\n");
            return SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "BatteryActualCapacity")) )
    {
        return_status = CosaDmlMtaBatteryGetActualCapacity(mta_handle, value);
        printf("Return status of CosaDmlMtaBatteryGetActualCapacity %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the Battery Actual Capacity\n");
            return SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "BatteryRemainingCharge")) )
    {
        return_status = CosaDmlMtaBatteryGetRemainingCharge(mta_handle, value);
        printf("Return status of mta_hal_BatteryGetRemainingCharge %d", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("ssp_MTAHAL_GetParamUlongValue : Failed to get the Battery Remaining Charge\n");
            return SSP_FAILURE;
        }
    }
    else
    {
        printf("Invalid parameter name");
        return_status = SSP_FAILURE;
    }
    printf("\n ssp_CosaDmlMTAGetParamUlongValue--> Exit\n");
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetCalls
 * Description          : This function will invoke the cosa api of MTA to retrieve all call 
 *                        info for the given instance number of LineTable 
 * 
 * @param [in]          : handleType - Message bus handle
			  instanceNumber - LineTable's instance number
 *                        count - number of entries(calls) for the call info array, to be returned
 *                        ppCall - Array of call info, to be returned
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_CosaDmlMTAGetCalls(int handleType, unsigned long instanceNumber, unsigned long* count, PMTA_CALLS *ppCall)
{
    int return_status = SSP_SUCCESS;
    ANSC_HANDLE mta_handle = NULL;


    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    printf("\n ssp_CosaDmlMTAGetCalls ----> Entry\n");

    return_status = CosaDmlMTAGetCalls(mta_handle, instanceNumber, count, (PCOSA_MTA_CALLS*)ppCall);
    printf("return value from ssp_CosaDmlMTAGetCalls is %d\n",return_status);
    
    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_CosaDmlMTAGetCalls::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_CosaDmlMTAGetCalls::Success\n");
        return return_status;
    }
    printf("\n ssp_CosaDmlMTAGetCalls ----> Exit\n");

}


/*******************************************************************************************
 *
 * Function Name        : ssp_CosaDmlMTAGetHandsets
 * Description          : This function will invoke the cosa api of MTA to retrieve
 *                        the DSXLogs
 *
 * @param [in]                       : handleType - Message bus handle
 * @param [unsigned long*]           : count -  number of handset instances, to be returned
 * @param [PCOSA_MTA_SERVICE_FLOW *] : ppDSXLog - array of handset entries, to be returned
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_CosaDmlMTAGetHandsets(int handleType, unsigned long* count, PMTA_HANDSETS_INFO *ppHandsets)
{
    int return_status = SSP_SUCCESS;
    ANSC_HANDLE mta_handle = NULL;
    printf("\n ssp_CosaDmlMTAGetHandsets----> Entry\n");

    if(handleType == 0)
    {
        mta_handle = bus_handle_client;
    }

    return_status = CosaDmlMTAGetHandsets(mta_handle, count, (PCOSA_MTA_HANDSETS_INFO *)ppHandsets);
    printf("return value from ssp_CosaDmlMTAGetHandsets is %d\n",return_status);

    if(return_status != SSP_SUCCESS)
    {
        printf("\nssp_CosaDmlMTAGetHandsets::Failed\n");
        return SSP_FAILURE;
    }
    else
    {
        printf("\nssp_CosaDmlMTAGetHandsets::Success\n");
        return return_status;
    }
    printf("\n ssp_CosaDmlMTAGetHandsets ----> Exit\n");
}
