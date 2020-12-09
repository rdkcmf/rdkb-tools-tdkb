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

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <unistd.h>
#include<netdb.h>
#include <arpa/inet.h>
#include <sys/stat.h>
#include <signal.h>

using namespace std;

#define IP "127.0.0.1"
#define PORT 8088
#define BUFFER_LENGTH 3072

int headerEnd;
bool f = true;
string moduleName,command;
char jsonMsg[BUFFER_LENGTH];

//Function to display the available options
static void printOptions (string file,string moduleName,string choice)
{
    cout <<"\nMenu \n\n";
    string text,value,val,var,var1;
    var = moduleName + "_start";
    var1 = moduleName + "_end";
    int lineno = 1;
    int headerEnd=0;
    bool isFound=0;
    ifstream ifs(file.c_str());

    if (ifs.is_open())
    {
        while(!ifs.eof())
        {
            getline(ifs,text);
            if (text.find("#") != std::string::npos or text.empty())
            {
                headerEnd++;
                continue;
            }
            else
            {
                for(int i=0;i<var.size();i++)
                {
                    if(text[i] == var[i])
                        isFound = 1;
                    else
                    {
                        isFound =0;
                        break;
                    }
                }
                if(isFound)
                {
                    for(lineno = 1;text!=var1;lineno++)
                    {
                        headerEnd++;
                        getline(ifs,text);
                        if(text == var1)
                            break;
                        else
                        {
                            value = text;
                            std::size_t found = value.find_last_of(":\\");
                            value = value.substr(0,found);
                            if(choice == "no")
                            {
                                cout << lineno <<"."<<value << "\n" ;
                                if(lineno % 10 == 0)
                                {
                                    cout << "\nPlease enter \"n\" for next api list else \"q\" to quit and choose from available list : ";
                                    cin >> val;
                                    if ( val == "n")
                                        continue;
                                    else if(val == "q")
                                        break;
                                    else
                                    {
                                        cout << "\nINVALID INPUT.Displaying next 10 apis.Next time please enter valid input(n/q)" << endl;
                                        continue;
                                    }
                                }
                            }
                            else if(choice == "yes")
                            {
                                cout << lineno <<"."<<value << "\n" ;
                                continue;
                            }
                            else
                            {
                                cout << "\nINVALID INPUT.Next time please enter valid input.\n";
                                break;
                            }

                        }
                    }
                }
            }
        }
    ifs.close();
    }
    else
        cout << "\n\nUnable to open the configuration file\n\n";

    cout <<"500.Unload and Exit\n\n";

    headerEnd--;
    return;
}

//Function to get the user selection from available options
static int getUserSelection (void)
{
    int mychoice = 0;
    cout << "\nEnter a choice : ";
    cin >> mychoice;
    getchar();
    return mychoice;
}

//Function to get the reponse of JSON message
string getAgentResponse(char *cmd)
{
    int sock = 0 ;
    int bytesRead = 0, bytesWritten = 0;
    struct sockaddr_in serv_addr;
    char buffer[BUFFER_LENGTH] = {0};
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        cout << "\nSocket creation error \n";
        return "Socket error";
    }
    memset(&serv_addr, '0', sizeof(serv_addr));

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert IPv4 and IPv6 addresses from text to binary form
    if(inet_pton(AF_INET, IP , &serv_addr.sin_addr)<=0)
    {
        cout << "\nInvalid address/ Address not supported \n";
        return "Invalid IP Address";
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    {
        cout << "\nConnection Failed \n";
        return "Connection Failed";
    }
    bytesWritten += send(sock , cmd , strlen(cmd) , 0 );
    bytesRead += read( sock , buffer, BUFFER_LENGTH);
    close(sock);
    return buffer;
}

//Function to get the stub function name from configuration file
string getStubFunctionName(int lineNo,string file,string moduleName)
{
    bool isFound=0;
    string text,var;
    var = moduleName + "_start";
    ifstream ifs(file.c_str());

    if (ifs.is_open())
    {
        while(!ifs.eof())
        {
            getline(ifs,text);
            if (text.find("#") != std::string::npos or text.empty())
            {
                headerEnd++;
                continue;
            }
            else
            {
                for(int i=0;i<var.size();i++)
                {
                    if(text[i] == var[i])
                        isFound = 1;
                    else
                    {
                        isFound =0;
                        break;
                    }
                }
                if(isFound)
                {
                   for (int i = 1; i <= lineNo; i++)
                       std::getline(ifs, text);
                       return text;
                }
            }
        }
        ifs.close();
    }
    else
        cout << "\n\nUnable to open the configuration file\n\n";
    return "";
}


//Function to get string values
string getString (string name)
{
    cin>>name;
    return name;
}

//Function to check whether the configuration file exists
bool FileExists(const std::string& name)
{
  struct stat buffer;
  return (stat (name.c_str(), &buffer) == 0);
}

//Function to frame user inputs
string getuserin(string params,string userparam)
{
    int count1 =0;
    int n1 = userparam.length();
    char char_array1[n1+1];
    strcpy(char_array1, userparam.c_str());
    char * pch1;
    pch1 = strtok (char_array1,",");
    //Loop to frame JSON parameters after getting input from the user
    while (pch1 != NULL)
    {
        string str1(pch1);
        string parameterValue1;
        params.append("\""+str1+"\": ");
        pch1 = strtok (NULL, ",");
        string paramType1(pch1);
        if (paramType1 == "(type=string)")
        {
            cout << "\n\nPlease Enter the value that you want to set for " << str1  << ": ";
            parameterValue1 = getString(parameterValue1);
            params.append("\""+parameterValue1+"\"");
        }
        else if (paramType1 == "(type=integer)")
        {
            cout << "\n\nPlease Enter the value that you want to set for " << str1 << ": ";
            parameterValue1 = getString(parameterValue1);
            params.append(parameterValue1);
        }
        else
        {
            cout << "\n\nInvalid parameter option\n";
        }

        count1 ++;
        pch1= strtok (NULL, ",");
        if (pch1 != NULL)
        {
            params.append(",");
        }
    }
    return params;
}

//Function to frame required inputs
string getreqin(string params,string reqparam)
{
    int count=0;
    int n = reqparam.length();
    char char_array[n+1];
    strcpy(char_array, reqparam.c_str());
    char * pch;
    pch = strtok (char_array,",");
    //Loop to frame JSON parameters after getting input from the user
    while (pch != NULL)
    {
        string str(pch);
        string parameterValue;
        params.append("\""+str+"\": ");
        pch = strtok (NULL, ",");
        string paramType(pch);
        if (paramType == "(type=string)")
        {
            pch = strtok (NULL, ",");
            parameterValue = pch;
            params.append("\""+parameterValue+"\"");
        }
        else if (paramType == "(type=integer)")
        {
            pch = strtok (NULL, ",");
            parameterValue = pch;
            params.append(parameterValue);
        }
        else
        {
            cout << "\n\nInvalid parameter option\n";
        }

        count ++;
        pch= strtok (NULL, ",");
        if (pch != NULL)
        {
            params.append(",");
        }
    }
    return params;
}

//Function to handle exceptions
void sighandler(int sig)
{
    //JSON message to unload a module
    command = "{\"jsonrpc\":\"2.0\",\"id\":\"2\",\"method\":\"unloadModule\",\"params\":{\"param1\":\""+moduleName+"\",\"version\":\"1.3\",\"ScriptSuiteEnabled\":\"false\"}}\r\n";

    strcpy(jsonMsg, command.c_str());

    //Executing the JSON message
    string output = getAgentResponse(jsonMsg);

    cout << "\n\n" << moduleName << " Unload Module Details : " << output << "\n";
    f = false;
    exit(sig);
}

//Main
int main(int argc, char *argv[])
{
    signal(SIGABRT, &sighandler);
    signal(SIGTERM, &sighandler);
    signal(SIGINT, &sighandler);
    while(f)
    {
        if ( argc <= 1 )
        {
            cout << "\n\nUsage : <binary name> <configuration file name> \n\n";
            break;
        }
        else if ( argc ==2 )
        {
            int loop = 1, i = 0 , paramType = 0, pos = 0;
            string choice;
            string stubFnName,stubFunWithParameters,stubFunWithParametersNew,parameters,boxIP,configFile;
            configFile = argv[1];
            if(FileExists(configFile))
            {
                cout << "\n\nEnter the module name to load ( Example : Enter \"wifihal\" to load wifihal module ) : ";
                moduleName = getString(moduleName);

                //JSON message to load a module
                command = "{\"jsonrpc\":\"2.0\",\"id\":\"2\",\"method\":\"loadModule\",\"params\":{\"param1\":\""+moduleName+"\",\"version\":\"2.0\", \"execID\":\"31253\",\"deviceID\":\"568\",\"testcaseID\":\"4664\", \"execDevID\":\"30873\",\"resultID\":\"914855\", \"performanceBenchMarkingEnabled\":\"false\", \"performanceSystemDiagnosisEnabled\":\"false\"}}\r\n";

                strcpy(jsonMsg, command.c_str());

                //Executing the JSON message
                string output = getAgentResponse(jsonMsg);

                cout << "\n\n" << moduleName << " Load Module Details : " << output << "\n";

                do
                {
                    cout << "\n If u wish to display all available apis please enter \"yes\" else \"no\" to display 10 apis at a time : ";
                    cin >> choice;
                    printOptions(configFile,moduleName,choice);
                    i = getUserSelection();
                    stubFnName = getStubFunctionName(i,configFile,moduleName);
                    string check = moduleName + "_start";
                    if ( i == 500 )
                        break;
                    if ( stubFnName == "" || stubFnName == check)
                    {
                        cout <<"\n\nInvalid Menu Choice : Next time please choose from the available options. Unloading and exiting..... \n\n";
                        break;
                    }
                    pos = stubFnName.find("=");
                    if ( pos <= 1 )
                    {

                        pos = stubFnName.find(":");
                        if ( pos <=1)
                        {
                            cout << "\n" << "=====INVALID PARAMETERS MAPPING IN CONFIGURATION FILE FOR NO INPUT API.PLEASE CHECK CONFIGURATION FILE=====";
                            break;
                        }
                        else
                        {
                            string apiname = stubFnName.substr(0,pos-1);
                            stubFnName = stubFnName.substr(pos+2);
                            //JSON message for stub function which is not needed any parameters as input
                            command = "{\"params\": {\"method\": \""+stubFnName+"\", \"module\": \""+moduleName+"\"}, \"jsonrpc\": \"2.0\", \"id\": \"2\", \"method\": \"executeTestCase\"}\r\n";
                            strcpy(jsonMsg, command.c_str());

                            //Executing the JSON message
                            output = getAgentResponse(jsonMsg);

                            cout << "\n\n" << apiname << " -- Execution Response : " << output << "\n";
                        }
                    }
                    else
                    {
                        stubFunWithParameters = stubFnName.substr (0,pos-1);
                        parameters = stubFnName.substr (pos+2);

                        pos = stubFunWithParameters.find(":");
                        if ( pos <=1 )
                        {
                            cout << "\n" << "=====INVALID PARAMETERS MAPPING IN CONFIGURATION FILE FOR INPUT API.PLEASE CHECK CONFIGURATION FILE=====";
                            break;
                        }
                        else
                        {
                            stubFunWithParametersNew = stubFunWithParameters.substr(pos+2);
                            string apiname = stubFunWithParameters.substr(0,pos-1);

                            std::size_t found = parameters.find_last_of(";\\");

                            string userparam = parameters.substr(0,found);
                            string reqparam = parameters.substr(found+1);

                            cout <<"\n\nParameters of " << apiname << " api are : "<< userparam;

                            string params="";
                            params.append("{");
                            if(reqparam == "")
                            {
                                params = getuserin(params,userparam);
                            }
                            else if(userparam == "")
                            {
                                params = getreqin(params,reqparam);
                            }
                            else
                            {
                                params = getreqin(params,reqparam);
                                params.append(",");
                                params = getuserin(params,userparam);
                            }
                            params.append("}");

                            //JSON message for stub function which needed parameters as input
                            command = "{\"jsonrpc\": \"2.0\", \"params\": {\"params\":"+params+", \"method\": \""+stubFunWithParametersNew+"\", \"module\": \""+moduleName+"\"}, \"id\": \"2\", \"method\": \"executeTestCase\"}\r\n";

                            strcpy(jsonMsg, command.c_str());

                            //Executing the JSON message
                            output = getAgentResponse(jsonMsg);

                            cout << "\n\n" << apiname << " -- Execution Response : " << output << "\n";
                        }

                    }

                }while(i != 500);

                //JSON message to unload a module
                command = "{\"jsonrpc\":\"2.0\",\"id\":\"2\",\"method\":\"unloadModule\",\"params\":{\"param1\":\""+moduleName+"\",\"version\":\"1.3\",\"ScriptSuiteEnabled\":\"false\"}}\r\n";

                strcpy(jsonMsg, command.c_str());

                //Executing the JSON message
                output = getAgentResponse(jsonMsg);

                cout << "\n\n" << moduleName << " Unload Module Details : " << output << "\n";
                break;
            }
            else
            {
                cout << "\n\n Configuration file is missing. Please check \n\n";
                break;
            }
        }

        else
           cout << "\n\nUsage : <binary name> <configuration file name> \n\n";
           break;
    }
    return 0;
}
