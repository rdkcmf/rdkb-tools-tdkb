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

#include "ssp_tdk_mso_mgmt_hal_wrp.h"
#include "ssp_hal_logger.h"
#include "mso_mgmt_hal.h"
/*******************************************************************************************
 *
 * Function Name        : ssp_mso_mgmt_hal_GetMsoPodSeed
 * Description          : This function will invoke the hal api of mso_mgmt_hal to get the MSO POD seed value
 *
 * @param [in]          : value: returns the value of the parameter
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mso_mgmt_hal_GetMsoPodSeed(char* value)
{
    int return_status = RETURN_ERR;

    printf("\nEntering ssp_ function ssp_mso_mgmt_hal_GetMsoPodSeed\n\n");

    return_status = mso_get_pod_seed(value);
    printf("Return status of mso_get_pod_seed %d", return_status);

    if ( return_status != RETURN_OK)
    {
        printf("ssp_mso_mgmt_hal_GetMsoPodSeed : Failed to get the mso pod seed\n");
        printf("\n MSO_POD_Seed value is %s",value);

    }
    else
    {
         printf("\n ssp_mso_mgmt_hal_GetMsoPodSeed::Success\n");
         printf("\n MSO_POD_Seed value is %s",value);
    }
    return return_status;

}

/*******************************************************************************************
 *
 * Function Name        : ssp_mso_set_pod_seed
 * Description          : This function will invoke the hal api of mso_mgmt_hal to set the MSO POD seed value
 *
 * @param [in]          : value: value of the seed to be set
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/
int ssp_mso_mgmt_hal_SetMsoPodSeed(char* value)
{
    int return_status = RETURN_ERR;

    printf("\nEntering ssp_ function ssp_mso_set_pod_seed\n\n");

    return_status = mso_set_pod_seed(value);
    printf("Return status of mso_get_pod_seed %d", return_status);

    if ( return_status != RETURN_OK)
    {
        printf("ssp_mso_set_pod_seed : Failed to set the mso pod seed\n");
    }
    else
    {
         printf("\n ssp_mso_set_pod_seed::Success\n");
    }
    return return_status;
}

/*******************************************************************************************
 *
 * Function Name        : ssp_mso_mgmt_hal_MsoValidatePwd
 * Description          : This function will invoke the hal api of mso_mgmt_hal to validate the password
 *
 * @param [in]          : paramValue: returns the value of the parameter
                          output    : returns the output 
 * @param [out]         : return status an integer value 0-success and 1-Failure
 ********************************************************************************************/

int ssp_mso_mgmt_hal_MsoValidatePwd(char* paramValue,char* output)
{
    int return_status = 0;
    int return_value = 0;

    printf("\nEntering ssp_mso_mgmt_hal_MsoValidatePwd function\n\n");

    return_status = mso_validatepwd(paramValue);
	
    printf("return_status:%d\n",return_status);
	
	switch(return_status)
	{
	     case 0:
	     {
		    strcpy(output,"Invalid_PWD");
                    break;
	     }
	     case 1:
	     {
		    strcpy(output,"Good_PWD");		 
            	    break;		 
	     }
	     case 2:
	     {
		    strcpy(output,"Unique_PWD");		 
                    break;		 
	     }
	     case 3:
	     {
		    strcpy(output,"Expired_PWD");		 
                    break;		 
	     }
	     case 4:
	     {
   	            strcpy(output,"TimeError");		 
                    break;		 
	     }
             default:
             {
                    DEBUG_PRINT(DEBUG_TRACE, "Invalid value provided\n");
                    printf("return_status:%d\n",return_status);
	            strcpy(output,"FAILURE");	
		    return_value = -1;
             }
	
    }		
    printf("Return value of mso_validatepwd %s", output);
	

    return return_value;

}

