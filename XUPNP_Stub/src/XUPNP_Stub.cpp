/*
 * If not stated otherwise in this file or this component's Licenses.txt file the
 * following copyright and licenses apply:
 *
 * Copyright 2019 RDK Management
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

#include "XUPNP_Stub.h"
#include <string.h>
#include <fstream>
#include <sstream>
#include <unistd.h>

string g_tdkPath = getenv("TDK_PATH");
static char xdiscOutputFile[STR_LEN];

/***************************************************************************
 *Function name : readLogFile
 *Description   : Helper API to check if a log pattern is found in the file specified
 *Input         : Filename - Name of file where the log has to be searched
 *                parameter - pattern to be searched in the log file
 *Output        : true if pattern is found
 *                false if pattern not found or filename does not exist
 *****************************************************************************/

bool readLogFile(const char *filename, const string parameter)
{
    string line;
    ifstream logFile(filename);
    if(logFile.is_open())
    {
        while(logFile.good())
        {
            getline(logFile,line);
            if (line.find(parameter) != string::npos)
            {
                DEBUG_PRINT(DEBUG_LOG,"Parameter found: %s\n",line.c_str());
                logFile.close();
                return true;
            }
        }
        logFile.close();
        DEBUG_PRINT(DEBUG_ERROR,"Error! No Log found for parameter %s\n", parameter.c_str());
    }
    else
    {
        DEBUG_PRINT(DEBUG_ERROR,"Unable to open file %s\n", filename);
    }
    return false;
}

//Check if given process is running
bool checkRunningProcess(const char *processName)
{
    char output[LINE_LEN] = {'\0'};
    char strCmd[STR_LEN] = {'\0'};
    FILE *fp = NULL;
    bool running = false;

    sprintf(strCmd,"pidof %s",processName);
    fp = popen(strCmd, "r");
    /* Read the output */
    if (fp != NULL)
    {
        if (fgets(output, sizeof(output)-1, fp) != NULL) {
	    running = true;
        }
	DEBUG_PRINT(DEBUG_TRACE, "%s process id: %s\n",processName, output);
	pclose(fp);
    }
    else {
        DEBUG_PRINT(DEBUG_ERROR, "Failed to get status of process %s\n",processName);
    }

    return running;
}

/**************************************************************************
Function name : XUPNPStub::initialize

Arguments     : Input arguments are Version string and XUPNPStub obj ptr

Description   : Registering all the wrapper functions with the agent for using these functions in the script
***************************************************************************/

bool XUPNPStub::initialize(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE, "XUPNPStub Initialization Entry\n");
    DEBUG_PRINT(DEBUG_TRACE, "XUPNPStub Initialization Exit\n");
    return TEST_SUCCESS;
}

/***************************************************************************
 *Function name : testmodulepre_requisites
 *Description   : testmodulepre_requisites will be used for setting the
 *                pre-requisites that are necessary for this component
 *                1. Checks that xdiscovery process is running in the system
 *                2. Checks that xcal-device process is running in the system (on gateway only)
 *                3. Get the location of output.json file on the device
 *****************************************************************************/

std::string XUPNPStub::testmodulepre_requisites()
{
    DEBUG_PRINT(DEBUG_TRACE, "XUPNP testmodule pre_requisites --> Entry\n");
    char output[LINE_LEN] = {'\0'};
    char strCmd[STR_LEN] = {'\0'};
    FILE *fp = NULL;
    bool running = false;

    //1. Check if xdiscovery process is running
    running = checkRunningProcess(XDISCOVERY);
    if (false == running) {
            DEBUG_PRINT(DEBUG_TRACE, "%s process is not running\n",XDISCOVERY);
            DEBUG_PRINT(DEBUG_TRACE, "XUPNP testmodule pre_requisites --> Exit\n");
            return "FAILURE:xdiscovery process is not running";
    }

    //2. Check if xcal-device process is running
    running = checkRunningProcess(XCALDEVICE);
    if (false == running) {
            DEBUG_PRINT(DEBUG_TRACE, "%s process is not running\n",XCALDEVICE);
            DEBUG_PRINT(DEBUG_TRACE, "XUPNP testmodule pre_requisites --> Exit\n");
            return "FAILURE:xcal-device process is not running";
    }

    //3. Get the location of output.json file on the device
    fp = NULL;
    memset(output,'\0',sizeof(output));
    memset(strCmd,'\0',sizeof(strCmd));

    ifstream xdiscConfFile(XDISCONFIG);
    if (xdiscConfFile.good())
    {
        xdiscConfFile.close();
        DEBUG_PRINT(DEBUG_TRACE, "%s file found\n",XDISCONFIG);
        sprintf(strCmd,"cat %s | grep outputJsonFile | grep -v '#' |cut -d '=' -f2-",XDISCONFIG);
    }

    fp = popen(strCmd, "r");
    if (fp != NULL)
    {
        /* Read the output */
        if (fgets(output, sizeof(output)-1, fp) != NULL) {
            DEBUG_PRINT(DEBUG_TRACE, "outputJsonFile value = %s\n",output);
            //Removing trailing newline character from fgets() input
            char *pos;
            if ((pos=strchr(output, '\n')) != NULL) {
                *pos = '\0';
            }

            memset(xdiscOutputFile,'\0',sizeof(xdiscOutputFile));
            strncpy(xdiscOutputFile,output,strlen(output));
            DEBUG_PRINT(DEBUG_TRACE, "Path for output.json = %s\n",xdiscOutputFile);
            pclose(fp);
        }
        else {
            DEBUG_PRINT(DEBUG_ERROR, "Path for output.json could not be found\n");
            DEBUG_PRINT(DEBUG_TRACE, "XUPNP testmodule pre_requisites --> Exit\n");
            pclose(fp);
            return "FAILURE:Could not locate output.json file";
        }
    }
    else {
        DEBUG_PRINT(DEBUG_ERROR, "Failed to get output.json path \n");
        return "FAILURE:Failed to get path for output.json file";
    }

    DEBUG_PRINT(DEBUG_TRACE, "XUPNP testmodule pre_requisites --> Exit\n");
    return "SUCCESS";
}

/***************************************************************************
 *Function name : testmodulepost_requisites
 *Description   : testmodulepost_requisites will be used for resetting the
 *                pre-requisites that are set
 *
 *****************************************************************************/

bool XUPNPStub::testmodulepost_requisites()
{
    return TEST_SUCCESS;
}

/**************************************************************************
Function name : XUPNPStub_ReadXDiscOutputFile

Arguments     : Input argument is parameter name.
                Output argument is "SUCCESS" or "FAILURE".

Description   : Receives the request from Test Manager to get the value for
                parameter name from xdiscovery output file (output.json)
**************************************************************************/

void XUPNPStub::XUPNPStub_ReadXDiscOutputFile(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE, "XUPNPStub_ReadXDiscOutputFile --->Entry\n");

    string parameter = req["paramName"].asString();
    string value;

    DEBUG_PRINT(DEBUG_TRACE, "Reading parameter %s in file %s\n",parameter.c_str(),xdiscOutputFile);

    ifstream outputFile(xdiscOutputFile);
    if(outputFile.is_open())
    {
        string line;
        size_t start = 0;
        int numberOfOccurence = 0;
        while(outputFile.good())
        {
            getline(outputFile,line);
            if ((start = line.find(parameter)) != string::npos)
            {
                DEBUG_PRINT(DEBUG_LOG,"Parameter found: %s\n",line.c_str());
                value += line;
                start += parameter.length();
                numberOfOccurence++;
            }
        }
        outputFile.close();

        if (!numberOfOccurence) {
            char strCmd[STR_LEN] = {'\0'};
            //Parameter not found, print the output file
            DEBUG_PRINT(DEBUG_ERROR,"Requested param (%s) not found in %s file \n",parameter.c_str(),xdiscOutputFile);
            value.assign("Parameter not found in output.json file");
            sprintf(strCmd,"cat %s",xdiscOutputFile);
            system(strCmd);
        }
        else {
            DEBUG_PRINT(DEBUG_TRACE, "value  = %s\n",value.c_str());
            response["result"] = "SUCCESS";
            //Truncate value beyond 512 characters
            if (value.length() > 512)
                response["details"] = value.substr (0,512) + "...";
            else
                response["details"] = value;
            DEBUG_PRINT(DEBUG_TRACE, "XUPNPStub_ReadXDiscOutputFile -->Exit\n");
            return;
        }
    }
    else
    {
        value.assign("Unable to open output.json file");
        DEBUG_PRINT(DEBUG_ERROR,"Unable to open file %s\n",xdiscOutputFile);
    }

    response["result"] = "FAILURE";
    response["details"] = value;

    DEBUG_PRINT(DEBUG_TRACE, "XUPNPStub_ReadXDiscOutputFile -->Exit\n");
    return;
}

/**************************************************************************
Function name : XUPNPStub_CheckXDiscOutputFile

Arguments     : Input argument is NONE. Output argument is "SUCCESS" or "FAILURE".

Description   : Receives the request from Test Manager to check if xdiscovery output file is
                created or not.
**************************************************************************/
void XUPNPStub::XUPNPStub_CheckXDiscOutputFile(IN const Json::Value& req, OUT Json::Value& response)
{
    DEBUG_PRINT(DEBUG_TRACE, "XUPNPStub_CheckXDiscOutputFile --->Entry\n");
    char stringDetails[STR_LEN] = {'\0'};

    // Check if xdiscovery output file is created
    ifstream xdiscOutFile(xdiscOutputFile);
    if (xdiscOutFile.good()) {
        xdiscOutFile.close();
        sprintf(stringDetails,"%s file found", xdiscOutputFile);
        DEBUG_PRINT(DEBUG_TRACE, "%s file found\n",xdiscOutputFile);
        response["result"] = "SUCCESS";
        response["details"] = stringDetails;
    }
    else {
        sprintf(stringDetails,"xdiscovery output file %s file not found", xdiscOutputFile);
        DEBUG_PRINT(DEBUG_TRACE, "xdiscovery output file %s file not found\n",xdiscOutputFile);
        response["result"] = "FAILURE";
        response["details"] = stringDetails;
    }

    DEBUG_PRINT(DEBUG_TRACE, "XUPNPStub_CheckXDiscOutputFile -->Exit\n");
    return;
}

/************************************************************************
Function Name   : CreateObject

Arguments       : NULL

Description     : This function is used to create a new object of the class "XUPNPStub".
**************************************************************************/

extern "C" XUPNPStub* CreateObject(TcpSocketServer &ptrtcpServer)
{
    return new XUPNPStub(ptrtcpServer);
}

/**************************************************************************
Function Name   : cleanup

Arguments       : NULL

Description     : This function will be used to the close things cleanly.
**************************************************************************/

bool XUPNPStub::cleanup(IN const char* szVersion)
{
    DEBUG_PRINT(DEBUG_TRACE, "cleaningup\n");
    return TEST_SUCCESS;
}

/**************************************************************************
Function Name : DestroyObject

Arguments     : Input argument is XUPNPStub Object

Description   : This function will be used to destory the XUPNPStub object.
**************************************************************************/
extern "C" void DestroyObject(XUPNPStub *stubobj)
{
    DEBUG_PRINT(DEBUG_LOG, "Destroying XUPNPStub object\n");
    delete stubobj;
}
