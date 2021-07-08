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

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "ssp_tdk_fwupgradehal_wrp.h"

/*******************************************************************************************
 *
 * Function Name        : ssp_FWUPGRADEHAL_GetParamUlongValue
 * Description          : This function will invoke the hal api to get the ulong values
 *
 * @param [in]          :  paramName: specifies the name of the API
                           value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_FWUPGRADEHAL_GetParamUlongValue(char* paramName, unsigned long* value)
{
    int return_status = 0;

    printf("\nEntering ssp_FWUPGRADEHAL_GetParamUlongValue function\n\n");

    if( !(strcmp(paramName, "Download_Interface")) )
    {
        return_status = fwupgrade_hal_get_download_interface((unsigned int*)value);
        printf("\nReturn status of fwupgrade_hal_get_download_interface %d\n", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("\nssp_FWUPGRADEHAL_GetParamUlongValue : Failed to get fwupgrade_hal_get_download_interface\n");
            return_status =SSP_FAILURE;
        }
    }
    else if( !(strcmp(paramName, "Reboot_Ready")) )
    {
        return_status = fwupgrade_hal_reboot_ready(value);
        printf("\nReturn status of fwupgrade_hal_reboot_ready %d\n", return_status);
        if ( return_status != SSP_SUCCESS)
        {
            printf("\nssp_FWUPGRADEHAL_GetParamUlongValue : Failed to get fwupgrade_hal_reboot_ready\n");
            return_status =SSP_FAILURE;
        }
    }
    else if(!(strcmp(paramName, "Download_Status")))
    {
       *value = fwupgrade_hal_get_download_status();
        printf("\nssp_FWUPGRADEHAL_GetParamUlongValue : Download status is %lu\n", *value);
    }
    else
    {
        printf("\nInvalid parameter name\n");
        return_status = SSP_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_FWUPGRADEHAL_Set_Download_Interface
 * Description          : This function will invoke the hal api of fwupgrade_hal_set_download_interface()
 *
 * @param [in]          : interface - The value of download interface to set
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_FWUPGRADEHAL_Set_Download_Interface(unsigned int interface)
{
    int return_status = 0;
    printf("\nEntering ssp_FWUPGRADEHAL_Set_Download_Interface\n\n");
    return_status = fwupgrade_hal_set_download_interface(interface);
    printf("\n return_status of fwupgrade_hal_set_download_interface : %d",return_status);

    if(return_status != SSP_SUCCESS)
    {
         printf("\n ssp_FWUPGRADEHAL_Set_Download_Interface::Failed\n");
         return SSP_FAILURE;
    }
    else
    {
         printf("\n ssp_FWUPGRADEHAL_Set_Download_Interface::Success\n");
         return SSP_SUCCESS;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_FWUPGRADEHAL_Download
 * Description          : This function will invoke the hal api of fwupgrade_hal_download() to start the download
 *
 * @param [in]          : None
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_FWUPGRADEHAL_Download()
{
    int return_status = 0;
    printf("\nEntering ssp_FWUPGRADEHAL_Download\n\n");
    return_status = fwupgrade_hal_download();
    printf("return_status of fwupgrade_hal_download is %d",return_status);

    if(return_status != SSP_SUCCESS)
    {
         printf("\n ssp_FWUPGRADEHAL_Download::Failed\n");
         return SSP_FAILURE;
    }
    else
    {
         printf("\n ssp_FWUPGRADEHAL_Download::Success\n");
         return SSP_SUCCESS;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_FWUPGRADEHAL_Reboot_Now
 * Description          : This function will invoke the hal api of fwupgrade_hal_download_reboot_now() to start the reboot
 *
 * @param [in]          : None
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_FWUPGRADEHAL_Reboot_Now()
{
    int return_status = 0;
    printf("\nEntering ssp_FWUPGRADEHAL_Reboot_Now function\n\n");
    return_status = fwupgrade_hal_download_reboot_now();
    printf("return_status of fwupgrade_hal_download_reboot_now is %d",return_status);

    if(return_status != SSP_SUCCESS)
    {
         printf("\n ssp_FWUPGRADEHAL_Reboot_Now::Failed\n");
         return SSP_FAILURE;
    }
    else
    {
         printf("\n ssp_FWUPGRADEHAL_Reboot_Now::Success\n");
         return SSP_SUCCESS;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_FWUPGRADEHAL_Get_Download_Url
 * Description          : This function will invoke the hal api to get the Download_Url
 *
 * @param [in]          : URL : The URL of site from which the file should download
                          filename: The name of the file which is to be download
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_FWUPGRADEHAL_Get_Download_Url(char* URL, char* filename)
{
    int return_status = 0;
    printf("\nEntering ssp_FWUPGRADEHAL_Get_Download_Url function\n\n");
    printf("\nDownload URL : %s and Filename : %s\n", URL, filename);
    return_status = fwupgrade_hal_get_download_url(URL,filename);
    printf("Return status of fwupgrade_hal_get_download_url %d\n", return_status);

    if ( return_status != SSP_SUCCESS)
    {
        printf("\nssp_FWUPGRADEHAL_Get_Download_Url :Failed to get the Download_Url\n");
        return SSP_FAILURE;
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_FWUPGRADEHAL_Set_Download_Url
 * Description          : This function will invoke the hal api of fwupgrade_hal_set_download_url()
 *
 * @param [in]          :  Value : The value of HTTP_Download_Url to set
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_FWUPGRADEHAL_Set_Download_Url(char* URL, char* filename)
{
    int return_status = 0;
    printf("\nEntering ssp_FWUPGRADEHAL_Set_Download_Url function\n");
    return_status = fwupgrade_hal_set_download_url(URL,filename);

    if(return_status != SSP_SUCCESS)
    {
         printf("\n ssp_FWUPGRADEHAL_Set_Download_Url::Failed\n");
         return SSP_FAILURE;
    }
    else
    {
         printf("\n ssp_FWUPGRADEHAL_Set_Download_Url::Success\n");
         return SSP_SUCCESS;
    }
}

/*******************************************************************************************
 *
 * Function Name        : ssp_FWUPGRADEHAL_UpdateAndFactoryReset
 * Description          : This function will invoke the hal api of fwupgrade_hal_update_and_factoryreset()
 *
 * @param [in]          : None
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_FWUPGRADEHAL_UpdateAndFactoryReset(char* url, char* name)
{
    int return_status = 0;
    printf("\nEntering ssp_FWUPGRADEHAL_UpdateAndFactoryReset function\n\n");
    printf("\nssp_FWUPGRADEHAL_UpdateAndFactoryReset URL is %s and image name is %s \n\n",url,name);
    return_status = fwupgrade_hal_update_and_factoryreset(url,name);
    printf("return_status of fwupgrade_hal_update_and_factoryreset is %d",return_status);

    if(return_status != SSP_SUCCESS)
    {
         printf("\n ssp_FWUPGRADEHAL_UpdateAndFactoryReset::Failed\n");
         return SSP_FAILURE;
    }
    else
    {
         printf("\n ssp_FWUPGRADEHAL_UpdateAndFactoryReset::Success\n");
         return SSP_SUCCESS;
    }
}
