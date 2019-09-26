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
/**********************************************************************
  Copyright [2014] [Cisco Systems, Inc.]

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
 **********************************************************************/

#ifdef __GNUC__
#if (!defined _BUILD_ANDROID) && (!defined _NO_EXECINFO_H_)
#include <execinfo.h>
#endif
#endif

#include "ssp_global.h"
#include "stdlib.h"
#include "ccsp_dm_api.h"
#include "ssp_tdk_mbus_wrp.h"
#include "ssp_tdk_wrp.h"

extern char subsystem_prefix[32];
PDSLH_CPE_CONTROLLER_OBJECT     pDslhCpeController      = NULL;
PCOMPONENT_COMMON_DM            g_pComponent_Common_Dm  = NULL;
char                            g_Subsystem[32]         = {0};
PCCSP_COMPONENT_CFG             gpPnmStartCfg           = NULL;
PCCSP_FC_CONTEXT                pPnmFcContext           = (PCCSP_FC_CONTEXT           )NULL;
PCCSP_CCD_INTERFACE             pPnmCcdIf               = (PCCSP_CCD_INTERFACE        )NULL;
PCCC_MBI_INTERFACE              pPnmMbiIf               = (PCCC_MBI_INTERFACE         )NULL;
BOOL                            g_bActive               = FALSE;

#define DEBUG_INI_NAME "/etc/debug.ini"
char tdkDebugIniFile[100] = {0};

int  cmd_dispatch(int  command)
{
    ULONG                           ulInsNumber        = 0;
    parameterValStruct_t            val[3]             = {0};
    char*                           pParamNames[]      = {"Device."};
    parameterValStruct_t**          ppReturnVal        = NULL;
    parameterInfoStruct_t**         ppReturnValNames   = NULL;
    parameterAttributeStruct_t**    ppReturnvalAttr    = NULL;
    ULONG                           ulReturnValCount   = 0;
    ULONG                           i                  = 0;
    char *pParamName = pParamNames[0];
    switch ( command )
    {
        case	'e' :

#ifdef _ANSC_LINUX
            CcspTraceInfo(("Connect to bus daemon...\n"));

            {
                char                            CName[256];

                if ( g_Subsystem[0] != 0 )
                {
                    _ansc_sprintf(CName, "%s%s", g_Subsystem, gpPnmStartCfg->ComponentId);
                }
                else
                {
                    _ansc_sprintf(CName, "%s", gpPnmStartCfg->ComponentId);
                }

                ssp_PnmMbi_MessageBusEngage
                    (
                     CName,
                     CCSP_MSG_BUS_CFG,
                     gpPnmStartCfg->DbusPath
                    );
            }

#endif

            ssp_create_pnm(gpPnmStartCfg);
            ssp_engage_pnm(gpPnmStartCfg);

            g_bActive = TRUE;

            CcspTraceInfo(("TDK Agent Module loaded successfully...\n"));


            break;

        case    'r' :

            CcspCcMbi_GetParameterValues
                (
                 DSLH_MPA_ACCESS_CONTROL_ACS,
                 pParamNames,
                 1,
                 &ulReturnValCount,
                 &ppReturnVal,
                 NULL
                );



            for ( i = 0; i < ulReturnValCount; i++ )
            {
                CcspTraceWarning(("Parameter %d name: %s value: %s \n", i+1, ppReturnVal[i]->parameterName, ppReturnVal[i]->parameterValue));
            }
            break;

        case    'm':

            AnscPrintComponentMemoryTable(pComponentName);

            break;

        case    't':

            AnscTraceMemoryTable();

            break;

        case    'c':

            ssp_cancel_pnm(gpPnmStartCfg);

            break;

        default:
            break;
    }

    return 0;
}

static void _print_stack_backtrace(void)
{
#ifdef __GNUC__
#if (!defined _BUILD_ANDROID) && (!defined _NO_EXECINFO_H_) && (!defined _COSA_SIM_)
    void* tracePtrs[100];
    char** funcNames = NULL;
    int i, count = 0;

    int fd;
    const char* path = "/nvram/CMAgentSsp_backtrace";
    fd = open(path, O_RDWR | O_CREAT);
    if (fd < 0)
    {
        fprintf(stderr, "failed to open backtrace file: %s", path);
        return;
    }

    count = backtrace( tracePtrs, 100 );

    backtrace_symbols_fd( tracePtrs, count, fd);

    close(fd);

    funcNames = backtrace_symbols( tracePtrs, count );

    if ( funcNames ) {
        // Print the stack trace
        for( i = 0; i < count; i++ )
            printf("%s\n", funcNames[i] );

        // Free the string pointers
        free( funcNames );
    }
#endif
#endif
}

#if defined(_ANSC_LINUX)
static void daemonize(void) {
    int fd;
    switch (fork()) {
        case 0:
            break;
        case -1:
            // Error
            CcspTraceInfo(("Error daemonizing (fork)! %d - %s\n", errno, strerror(
                            errno)));
            exit(0);
            break;
        default:
            _exit(0);
    }

    if (setsid() < 	0) {
        CcspTraceInfo(("Error demonizing (setsid)! %d - %s\n", errno, strerror(errno)));
        exit(0);
    }


#ifndef  _DEBUG

    fd = open("/dev/null", O_RDONLY);
    if (fd != 0) {
        dup2(fd, 0);
        close(fd);
    }
    fd = open("/dev/null", O_WRONLY);
    if (fd != 1) {
        dup2(fd, 1);
        close(fd);
    }
    fd = open("/dev/null", O_WRONLY);
    if (fd != 2) {
        dup2(fd, 2);
        close(fd);
    }
#endif
}

void sig_handler(int sig)
{

    CcspBaseIf_deadlock_detection_log_print(sig);

    if ( sig == SIGINT ) {
        signal(SIGINT, sig_handler); /* reset it to this function */
        CcspTraceInfo(("SIGINT received!\n"));
        exit(0);
    }
    else if ( sig == SIGUSR1 ) {
        signal(SIGUSR1, sig_handler); /* reset it to this function */
        CcspTraceInfo(("SIGUSR1 received!\n"));
    }
    else if ( sig == SIGUSR2 ) {
        CcspTraceInfo(("SIGUSR2 received!\n"));
    }
    else if ( sig == SIGCHLD ) {
        signal(SIGCHLD, sig_handler); /* reset it to this function */
        CcspTraceInfo(("SIGCHLD received!\n"));
    }
    else if ( sig == SIGPIPE ) {
        signal(SIGPIPE, sig_handler); /* reset it to this function */
        CcspTraceInfo(("SIGPIPE received!\n"));
    }
    else if ( sig == SIGTERM )
    {
        CcspTraceInfo(("SIGTERM received!\n"));
        exit(0);
    }
    else if ( sig == SIGKILL )
    {
        CcspTraceInfo(("SIGKILL received!\n"));
        exit(0);
    }
    else {
        /* get stack trace first */
        _print_stack_backtrace();
        CcspTraceInfo(("Signal %d received, exiting!\n", sig));
        exit(0);
    }
}

static int is_core_dump_opened(void)
{
    FILE *fp;
    char path[256];
    char line[1024];
    char *start, *tok, *sp;
#define TITLE   "Max core file size"

    snprintf(path, sizeof(path), "/proc/%d/limits", getpid());
    if ((fp = fopen(path, "rb")) == NULL)
        return 0;

    while (fgets(line, sizeof(line), fp) != NULL) {
        if ((start = strstr(line, TITLE)) == NULL)
            continue;

        start += strlen(TITLE);
        if ((tok = strtok_r(start, " \t\r\n", &sp)) == NULL)
            break;

        fclose(fp);

        if (strcmp(tok, "0") == 0)
            return 0;
        else
            return 1;
    }

    fclose(fp);
    return 0;
}

#endif


/***************************************************************************
 *Function name : createTdkDebugIniFile
 *Descrption    : Create TEST module in debug.ini for TDK testing
 *
 *****************************************************************************/
bool createTdkDebugIniFile()
{
   printf("Entering createTdkDebugIniFile\n");

   int buf;
   FILE *src, *dst;
   char *g_tdkPath;
   char buffer[200]= {"LOG.RDK.TEST = ALL DEBUG TRACE\n\
LOG.RDK.TEST1 = ALL DEBUG TRACE\n\
LOG.RDK.TEST2 = NONE ALL\n\
LOG.RDK.TEST3 = ALL NONE\n\
LOG.RDK.TEST4 = TRACE\n\
LOG.RDK.TEST5 = !TRACE\n\
LOG.RDK.TEST6 =\n"};

   /* Open /etc/debug.ini to read the content */
   src = fopen(DEBUG_INI_NAME, "r");

   if( src == NULL )
   {
      printf("Failed to open the src file:%s\n",DEBUG_INI_NAME);
      return false;
   }

   /* Get the logger path where debug.ini for TDK testing to be created */
   g_tdkPath=getenv("TDK_LOGGER_PATH");

   strcpy(tdkDebugIniFile,g_tdkPath);
   strcat(tdkDebugIniFile,"/debug.ini");

   printf("TDK debug file:%s\n",tdkDebugIniFile);

   /* Open the TDK debug.ini file to copy the /etc/debug.ini file content */
   dst = fopen(tdkDebugIniFile, "w");

   if( dst == NULL )
   {
      fclose(src);
      printf("Failed to open the target file:%s\n",tdkDebugIniFile);
      return false;
   }

   /* Write the file content of /etc/debug.ini to TDK debug.ini */
   while( ( buf = fgetc(src) ) != EOF )
   {
      fputc(buf, dst);
   }

   fclose(src);
   fclose(dst);

   /* Open the TDK debug.ini to append TEST module log levels */
   dst = fopen(tdkDebugIniFile, "a");
   if( dst == NULL )
   {
      printf("Failed to open the file:%s\n",tdkDebugIniFile);
      return false;
   }

   fputs(buffer, dst);

   fclose(dst);

   printf("Exiting createTdkDebugIniFile\n");

   return true;
}

int ssp_register(bool bexecVal)
{


    ANSC_STATUS                     returnStatus       = ANSC_STATUS_SUCCESS;
    int                             cmdChar            = 0;
    BOOL                            bRunAsDaemon       = FALSE;
    int                             idx                = 0;
    char                            cmd[1024]          = {0};
    FILE                           *fd                 = NULL;
    DmErr_t                         err;
    char                            *subSys            = NULL;
    extern ANSC_HANDLE bus_handle;
    int nReturnValue = 0;

    printf("\n***************************************** \n");
    printf("\n Entering ssp register TDK Main function\n");
    printf("\n***************************************** \n");

    if(SSP_STOP == (int)bexecVal)
    {
        printf("\n Closing SSP TDK main Function");
        cmd_dispatch('q');
        return 1;
    }

    /* Invoke createTdkDebugIniFile to create debug.ini for TDK testing */
    if (false == createTdkDebugIniFile())
    {
         return 1;
    }

    printf("Created debug.ini with TEST modules\n");

    /* Initialize logger for TDK testing */
    nReturnValue = rdk_logger_init(tdkDebugIniFile);
    if (nReturnValue != 0)
    {
         printf("Alert!!! Failed to init rdk logger. ErrCode = %d\n", nReturnValue);
    }
    else
    {
         printf("Initialized RDK Logger\n");
    }

    printf("\n ssp_register :: Make file option for subsytem flag eRT is set to %d",eRT);
    if(eRT == 1)
    {
        strcpy(subsystem_prefix,"eRT.");
    }
    /*
     *  Load the start configuration
     */
    gpPnmStartCfg = (PCCSP_COMPONENT_CFG)AnscAllocateMemory(sizeof(CCSP_COMPONENT_CFG));

    if ( gpPnmStartCfg )
    {
        CcspComponentLoadCfg(CCSP_PNM_TDK_START_CFG_FILE, gpPnmStartCfg);
    }
    else
    {
        printf("Insufficient resources for start configuration, quit!\n");
        exit(1);
    }

    /* Set the global pComponentName */
    if(eRT == 1)
    {
        strcpy(gpPnmStartCfg->ComponentId,"eRT.");
        strcpy(gpPnmStartCfg->ComponentName,"eRT.");
        strcat(gpPnmStartCfg->ComponentId,"com.cisco.spvtg.ccsp.tdkb");
        strcat(gpPnmStartCfg->ComponentName,"com.cisco.spvtg.ccsp.tdkb");
    }
    else
    {
        strcpy(gpPnmStartCfg->ComponentId,"com.cisco.spvtg.ccsp.tdkb");
        strcpy(gpPnmStartCfg->ComponentName,"com.cisco.spvtg.ccsp.tdkb");
    }

    sprintf(gpPnmStartCfg->DbusPath,"/com/cisco/spvtg/ccsp/tdkb");
    pComponentName = gpPnmStartCfg->ComponentName;
    printf("\ngpPnmStartCfg->ComponentId is %s",gpPnmStartCfg->ComponentId);
    printf("\ngpPnmStartCfg->ComponentName is %s",gpPnmStartCfg->ComponentName);
    printf("\ngpPnmStartCfg->DbusPath is %s",gpPnmStartCfg->DbusPath);
    printf("\ngpPnmStartCfg->Version is %d",gpPnmStartCfg->Version);
    AnscSetTraceLevel(CCSP_TRACE_LEVEL_INFO);

#if defined(_DEBUG) && defined(_COSA_SIM_)
    AnscSetTraceLevel(CCSP_TRACE_LEVEL_INFO);
#endif


#if  defined(_ANSC_WINDOWSNT)

    AnscStartupSocketWrapper(NULL);

    display_info();

    cmd_dispatch('e');


#elif defined(_ANSC_LINUX)
    if ( bRunAsDaemon )
        daemonize();

    /*This is used for ccsp recovery manager */
    fd = fopen("/var/tmp/TDKB.pid", "w+");
    if ( !fd )
    {
        CcspTraceWarning(("Create /var/tmp/TDKB.pid error. \n"));
        return 1;
    }
    sprintf(cmd, "%d", getpid());
    fputs(cmd, fd);
    fclose(fd);

    if (is_core_dump_opened())
    {
        signal(SIGUSR1, sig_handler);
        CcspTraceWarning(("Core dump is opened, do not catch signal\n"));
    }
    else
    {
        CcspTraceWarning(("Core dump is NOT opened, backtrace if possible\n"));
        signal(SIGTERM, sig_handler);
        signal(SIGINT, sig_handler);
        signal(SIGUSR1, sig_handler);
        signal(SIGUSR2, sig_handler);

        signal(SIGSEGV, sig_handler);
        signal(SIGBUS, sig_handler);
        signal(SIGKILL, sig_handler);
        signal(SIGFPE, sig_handler);
        signal(SIGILL, sig_handler);
        signal(SIGQUIT, sig_handler);
        signal(SIGHUP, sig_handler);
    }

    cmd_dispatch('e');

#ifdef _COSA_SIM_
    subSys = "";        /* PC simu use empty string as subsystem */
#else
    subSys = NULL;      /* use default sub-system */
#endif
    err = Cdm_Init(bus_handle, subSys, NULL, NULL, pComponentName);
    if (err != CCSP_SUCCESS)
    {
        fprintf(stderr, "Cdm_Init: %s\n", Cdm_StrError(err));
        exit(1);
    }

    system("touch /tmp/TDK_initialized");

    printf("Entering TDK loop\n");
#endif

    bus_handle_client = bus_handle;

    if ( bRunAsDaemon )
    {
        while(1)
        {
            sleep(30);
        }
    }
    else
    {
        cmd_dispatch('q');
    }

    return 0;
}

int ssp_terminate()
{

    printf("\nEntering ssp terminate function\n");

    DmErr_t                         err;

    err = Cdm_Term();
    if (err != CCSP_SUCCESS)
    {
        fprintf(stderr, "Cdm_Term: %s\n", Cdm_StrError(err));
        return 1;
    }

    if ( g_bActive )
    {
        ssp_cancel_pnm(gpPnmStartCfg);

        g_bActive = FALSE;
    }

    return 0;
}

int tdk_ssp_main()
{
    int return_status =-1;
    printf("\n Enetering tdk_ssp_main Function ...");

    return_status = ssp_register(1);

    if(return_status == 0)
    {
        printf("\n TDK Component creation::ssp_register function success");
    }
    else
    {
        printf("\n TDK Component Creation:: ssp_register function failure");
    }
    return 0;
}
