/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2020 RDK Management
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
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
#include <inttypes.h>
#include <rbus/rbus.h>
#include "ssp_tdk_rbus_wrp.h"
#include "ssp_hal_logger.h"


static rbusHandle_t bus_handle;

/*****************************************************************************************************************
 * Function Name : ssp_rbus_checkStatus
 * Description   : This function will Retrieve the RBUS status
 * @param [in]   : status - buffer to hold RBUS status value
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_checkStatus( rbusStatus_t *status)
{
        int result = RETURN_ERR;

        DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_checkStatus wrapper\n");

        rbusStatus_t rbus_status = RBUS_DISABLED;
        rbus_status = rbus_checkStatus();

        DEBUG_PRINT(DEBUG_ERROR, "RBUS Status is %d\n",rbus_status);
        *status = rbus_status;

        if(rbus_status == RBUS_ENABLED || rbus_status == RBUS_ENABLE_PENDING || rbus_status == RBUS_DISABLE_PENDING || rbus_status == RBUS_DISABLED )
        {
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_checkStatus function returns value : %d\n", rbus_status);
            result = RETURN_OK;
        }
        else
        {
            DEBUG_PRINT(DEBUG_ERROR, "ssp_rbus_checkStatus function returns failure, %d\n", rbus_status);
            result = RETURN_ERR;
        }

        DEBUG_PRINT(DEBUG_ERROR, "Exiting ssp_rbus_checkStatus wrapper\n");
        return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_rbus_open
 * Description   : This function will open the RBUS connection
 * @param [in]   : none
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_open() {
    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_open wrapper\n");

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;

    if (bus_handle == NULL)
    {
        ret = rbus_open(&bus_handle, "tdk_b");

        if(ret != RBUS_ERROR_SUCCESS)
        {
            DEBUG_PRINT(DEBUG_ERROR, "rbus_open failed with error code %d \n", ret);
            result = RETURN_ERR;
        }
	else
	{
            DEBUG_PRINT(DEBUG_ERROR, "rbus_open was successful, return value is %d \n",ret);
            result = RETURN_OK;
	}
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "rbus was already opened and not closed properly \n");
        result = RETURN_ERR;
    }
    return result;
}

/*****************************************************************************************************************
 * Function Name : ssp_rbus_close
 * Description   : This function will close the rbus connection
 * @param [in]   : None
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_rbus_close( ) {
    DEBUG_PRINT(DEBUG_ERROR, "Entering the ssp_rbus_close wrapper\n");

    int result = RETURN_ERR;
    int ret = RBUS_ERROR_SUCCESS;

    if (bus_handle != NULL)
    {
        ret = rbus_close(bus_handle);

        if(ret != RBUS_ERROR_SUCCESS)
        {
            DEBUG_PRINT(DEBUG_ERROR, "rbus_close failed with error code %d \n", ret);
            result = RETURN_ERR;
        }
	else
	{
            DEBUG_PRINT(DEBUG_ERROR, "rbus_close was successful, return value is %d \n",ret);
            result = RETURN_OK;
	}
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR, "rbus was not opened properly, bus_handle was null");
        result = RETURN_ERR;
    }
    return result;
}

