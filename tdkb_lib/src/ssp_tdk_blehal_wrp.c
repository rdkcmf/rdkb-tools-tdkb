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

#include "ssp_tdk_blehal_wrp.h"
#include "ssp_hal_logger.h"

/*****************************************************************************************************************
 * Function Name : ssp_BLEHAL_GetStatus
 * Description   : This function will Retrieve the BLE status
 * @param [in]   : status - buffer to hold ble status value
                   isNegativeScenario - for negative scenario
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_BLEHAL_GetStatus( BLE_Status_e *status, int isNegativeScenario)
{
        int result = RETURN_ERR;

        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_BLEHAL_GetStatus wrapper\n");

        if(isNegativeScenario)
        {
                result = ble_GetStatus(NULL);
        }
        else
        {
                result = ble_GetStatus(status);
        }

        if(result == RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_TRACE, "ssp_BLEHAL_GetStatus function returns value : %d\n", *status);
        }
        else
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_BLEHAL_GetStatus function returns failure\n");
        }

        DEBUG_PRINT(DEBUG_TRACE, "Exiting ssp_BLEHAL_GetStatus wrapper\n");
        return result;
}


/*****************************************************************************************************************
 * Function Name : ssp_BLEHAL_Enable
 * Description   : This function will set ble enable state
 * @param [in]   : status - ble enable state to be set
 * @param [out]  : return status an integer value 0-success and 1-Failure
 ******************************************************************************************************************/
int ssp_BLEHAL_Enable( BLE_Status_e status)
{
        int result = RETURN_ERR;

        DEBUG_PRINT(DEBUG_TRACE, "Entering the ssp_BLEHAL_Enable wrapper\n");


        if( ble_Enable(status) == RETURN_OK)
        {
                DEBUG_PRINT(DEBUG_TRACE, "ssp_BLEHAL_Enable function returns success\n");
                result = RETURN_OK;
        }
        else
        {
                DEBUG_PRINT(DEBUG_ERROR, "ssp_BLEHAL_Enable function returns failure\n");
        }

        DEBUG_PRINT(DEBUG_TRACE, "Exiting ssp_BLEHAL_Enable wrapper\n");
        return result;
}

