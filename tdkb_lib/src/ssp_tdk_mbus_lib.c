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

#ifndef __SSP_MBUS_LIB_C__
#define __SSP_MBUS_LIB_C__

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <ccsp_message_bus.h>
#include <ccsp_base_api.h>
#include <sys/time.h>
#include <time.h>
#include <slap_definitions.h>
#include <ccsp_psm_helper.h>
#include "ssp_global.h"
#include "ansc_tso_interface.h"
#include "ssp_tdk_mbus_lib.h"

static const char* TDK_Introspect_msg =
"<xml version=\"1.0\" encoding=\"UTF-8\">\n"
"<node name=\"/com/cisco/spvtg/ccsp/PersistentStorage\">\n"
"    <interface name=\"com.cisco.spvtg.ccsp.baseInterface\">\n"
"        \n"
"        <method name=\"initialize\">\n"
"            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
"        </method>\n"
"        <method name=\"finalize\">\n"
"            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
"        </method>\n"
"        \n"
"        <!--\n"
"            This API frees up resources such as allocated memory, flush caches etc, if possible. \n"
"            This is invoked by Test and Diagnostic Manager, as a proactive measure, when it \n"
"            detects low memory conditions.     \n"
"        -->\n"
"        <method name=\"freeResources\">\n"
"            <arg type=\"i\" name=\"priority\" direction=\"in\" />\n"
"            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
"        </method>\n"
"        \n"
"        <!--\n"
"            DEPRECATED\n"
"            This API is used to retrieve the Component Metadata. The Component Metadata \n"
"            includes the following information: \n"
"            - Component Name\n"
"            - Component Author \n"
"            - Component Version \n"
"        -->\n"
"        <method name=\"getComponentMetadata\">\n"
"            <arg type=\"s\" name=\"component_name\" direction=\"out\" />\n"
"            <arg type=\"s\" name=\"component_author\" direction=\"out\" />\n"
"            <arg type=\"s\" name=\"component_version\" direction=\"out\" />\n"
"            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
"        </method>\n"
"        \n"
"        <!-- \n"
"            DEPRECATED \n"
"            Logging APIs  \n"
"        -->\n"
"        <method name=\"enableLogging\">\n"
"            <arg type=\"b\" name=\"enable\" direction=\"in\" />\n"
"            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
"        </method>\n"
"        <!-- DEPRECATED   -->\n"
"        <method name=\"setLoggingLevel\">\n"
"            <arg type=\"i\" name=\"level\" direction=\"in\" />\n"
"            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
"        </method>\n"
"\n"
"        <!-- \n"
"            DEPRECATED\n"
"            This API returns the internal state of the component. The state reflects the \n"
"            Component\'s internal lifecycle state\n"
"        -->\n"
"        <method name=\"queryStatus\">\n"
"            <arg type=\"i\" name=\"internalState\" direction=\"out\" />\n"
"            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
"        </method> \n"
"        \n"
"        <!-- \n"
"            DEPRECATED \n"
"            This API returns the health of the component as \'Red/Bad\', \'Yellow/warning\', \'Green/good\' \n"
"        -->\n"
"        <method name=\"healthCheck\">\n"
"            <arg type=\"i\" name=\"health\" direction=\"out\" />\n"
"            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
"        </method>  \n"
"        \n"
"        <!--\n"
"            DEPRECATED\n"
"            This API returns the amount of direct memory allocated by the component. Typically the \n"
"            Process statistics can be retrieved by querying the /proc/<PID> file system under    \n"
"            Linux OS. However, in cases where more than one component are grouped into a \n"
"            single process, this API provides component level memory usage which can be very \n"
"            useful to isolate low memory conditions. \n"
"        -->\n"
"        <method name=\"getAllocatedMemory\">\n"
"            <arg type=\"i\" name=\"directAllocatedMemory\" direction=\"out\" />\n"
"            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
"        </method>  \n"
"        \n"
"        <!-- \n"
"            DEPRECATED\n"
"            This API returns the mmaximum memory requirements for the component. It is the \n"
"            component owner\'s best estimates   \n"
"        -->\n"
"        <method name=\"getMaxMemoryUsage\">\n"
"            <arg type=\"i\" name=\"memoryUsage\" direction=\"out\" />\n"
"            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
"        </method>  \n"
" \n"
"        <!-- \n"
"            DEPRECATED\n"
"            This API returns the minimum memory requirements for the component. It is the \n"
"            component owner\'s best estimates   \n"
"        -->\n"
"        <method name=\"getMinMemoryUsage\">\n"
"            <arg type=\"i\" name=\"memoryUsage\" direction=\"out\" />\n"
"            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
"        </method>  \n"
" \n"
"        <!-- Data model parameters \"set\" APIs\n"
"            typedef struct {\n"
"                const char *parameterName; \n"
"                unsigned char *parameterValue;\n"
"                dataType_e type; \n"
"            } parameterValStruct_t; \n"
"            \n"
"            typedef enum {\n"
"                ccsp_string = 0, \n"
"                ccsp_int,\n"
"                ccsp_unsignedInt,\n"
"                ccsp_boolean,\n"
"                ccsp_dateTime,\n"
"                ccsp_base64,\n"
"                ccsp_long, \n"
"                ccsp_unsignedLong, \n"
"                ccsp_float, \n"
"                ccsp_double,\n"
"                ccsp_byte,  // char \n"
    "                (any other simple type that I may have missed),   \n"
    "                ccsp_none \n"
    "            } datatype_e\n"
    "        -->\n"
    "        <method name=\"setParameterValues\">\n"
    "            <arg type=\"i\" name=\"sessionId\" direction=\"in\" />\n"
    "            <arg type=\"i\" name=\"writeID\" direction=\"in\" />\n"
    "            <arg type=\"a(ssi)\" name=\"parameterValStruct\" direction=\"in\" />\n"
    "            <arg type=\"i\" name=\"size\" direction=\"in\" />\n"
    "            <arg type=\"b\" name=\"commit\" direction=\"in\" />\n"
    "            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
    "        </method>\n"
    "        \n"
    "        <method name=\"setCommit\">\n"
    "            <arg type=\"i\" name=\"sessionId\" direction=\"in\" />\n"
    "            <arg type=\"i\" name=\"writeID\" direction=\"in\" />\n"
    "            <arg type=\"b\" name=\"commit\" direction=\"in\" />\n"
    "            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
    "        </method>\n"
    "                \n"
    "        <!-- Data model parameters \"get\" APIs   -->\n"
    "        <method name=\"getParameterValues\">\n"
    "            <arg type=\"as\" name=\"parameterNames\" direction=\"in\" />\n"
    "            <arg type=\"i\" name=\"size\" direction=\"in\" />\n"
    "            <arg type=\"a(ss)\" name=\"parameterValStruct\" direction=\"out\" />\n"
    "            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
    "        </method>\n"
    "        \n"
    "        <!-- \n"
    "            This API sets the attributes on data model parameters\n"
    "            typedef struct { \n"
    "                const char* parameterName; \n"
    "                boolean notificationChanged; \n"
    "                boolean notification; \n"
    "                enum access_e access; // (CCSP_RO, CCSP_RW, CCSP_WO)\n"
    "                boolean accessControlChanged; \n"
    "                unsigned int accessControlBitmask;\n"
    "                  //  0x00000000 ACS\n"
    "                  //  0x00000001 XMPP\n"
    "                  //  0x00000002 CLI\n"
    "                  //  0x00000004 WebUI\n"
    "                  //  ... \n"
    "                  //  0xFFFFFFFF  ANYBODY (reserved and default value for all parameters)\n"
    "           } parameterAttribStruct_t; \n"
    "        -->\n"
    "        <method name=\"setParameterAttributes\">\n"
    "            <arg type=\"i\" name=\"sessionId\" direction=\"in\" />\n"
    "            <arg type=\"a(sbbibi)\" name=\"parameterAttributeStruct\" direction=\"in\" />\n"
    "            <arg type=\"i\" name=\"size\" direction=\"in\" />\n"
    "            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
    "        </method>\n"
    "        \n"
    "        <method name=\"getParameterAttributes\">\n"
    "            <arg type=\"as\" name=\"parameterNames\" direction=\"in\" />\n"
    "            <arg type=\"i\" name=\"size\" direction=\"in\" />\n"
    "            <arg type=\"a(sbii)\" name=\"parameterAttributeStruct\" direction=\"out\" />\n"
    "            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
    "        </method>\n"
    "        \n"
    "        <!-- \n"
    "            This API adds a row to a table object. The object name is a partial path \n"
    "            and must end with a \".\" (dot). The API returns the instance number of the \n"
    "            row.\n"
    "        -->\n"
    "        <method name=\"AddTblRow\">\n"
    "            <arg type=\"i\" name=\"sessionId\" direction=\"in\" />\n"
    "            <arg type=\"s\" name=\"objectName\" direction=\"in\" />\n"
    "            <arg type=\"i\" name=\"instanceNumber\" direction=\"out\" />\n"
    "            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
    "        </method>\n"
    "        \n"
    "        <!-- \n"
    "            This API deletes a row from the table object. The object name is a partial \n"
    "            path and must end with a \".\" (dot) after the instance number.\n"
    "        -->\n"
    "        <method name=\"DeleteTblRow\">\n"
    "            <arg type=\"i\" name=\"sessionId\" direction=\"in\" />\n"
    "            <arg type=\"s\" name=\"objectName\" direction=\"in\" />\n"
    "            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
    "        </method>\n"
    "        \n"
    "        <!--\n"
    "            This API is used to return the supported parameter names under a data model object\n"
    "            parameterName is either a complete Parameter name, or a partial path name of an object.            \n"
    "            nextLevel \n"
    "                If false, the response MUST contain the Parameter or object whose name exactly\n"
    "                matches the ParameterPath argument, plus all Parameters and objects that are\n"
    "                descendents of the object given by the ParameterPath argument, if any (all levels\n"
    "                below the specified object in the object hierarchy).\n"
    "            \n"
    "                If true, the response MUST contain all Parameters and objects that are next-level\n"
    "                children of the object given by the ParameterPath argument, if any.\n"
    "            parameterInfoStruct is defined as: \n"
    "                typedef struct {\n"
    "                    comst char *name; \n"
    "                    boolean writable; \n"
    "                }\n"
    "        -->\n"
    "        <method name=\"getParameterNames\">\n"
    "            <arg type=\"s\" name=\"parameterName\" direction=\"in\" />\n"
    "            <arg type=\"b\" name=\"nextLevel\" direction=\"in\" />\n"
    "            <arg type=\"a(sb)\" name=\"parameterInfoStruct\" direction=\"out\" />\n"
    "            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
    "        </method>\n"
    "        \n"
    "        <!-- \n"
    "            This API is used in diagnostic mode. This must be used asynchronously. \n"
    "            The use case is that the Test and Diagnostic Manager (TDM) CCSP component can leverage this feature \n"
    "            in the Component Registrar to validate parameter types. The TDM sends commands to other components to \n"
    "            run diagnostics. The TDM invokes a buscheck() request to each component one at a time in diagnostic mode. \n"
    "            When each component receives buscheck(), it invokes the namespace type check API in the Component \n"
    "            Registrar for each of the data model parameters accessed by this component and owned by another component. \n"
    "            The Component Registrar verifies that each data model parameter is registered by a component and that the \n"
    "            data model type specified in the API is the same as the data model type registered by the \'owner\' component. \n"
    "            The component sends TDM a response to buscheck() with all checked parameter names and PASS/FAIL for each \n"
    "            parameter. If during buscheck(), it is found that there are missing or unregistered parameters, \n"
    "            appropriate errors are flagged. \n"
    "        -->\n"
    "        <method name=\"busCheck\">\n"
    "            <arg type=\"i\" name=\"status\" direction=\"out\" />\n"
    "        </method>\n"
    "        \n"
    "        <!--\n"
    "            Signal contains the following information: \n"
    "            typedef struct {\n"
    "                const char *parameterName; \n"
    "                const char* oldValue; \n"
    "                const char* int newValue;\n"
    "                unsigned int writeID; \n"
    "            } parameterSigStruct_t; \n"
    "        -->\n"
    "        <signal name=\"parameterValueChangeSignal\">\n"
    "            <arg type=\"a(sssi)\" name=\"parameterSigStruct\" direction=\"out\" />\n"
    "            <arg type=\"i\" name=\"size\" direction=\"out\" />\n"
    "        </signal>\n"
    "        \n"
    "       \n"
    "    </interface>\n"
    "</node>\n"
    ;


    /*******************************************************************************************
     *
     * Function Name        : tdk_path_msg_func
     * Description          : This is a callback function that will listens to message invoked by ot                         her components and process the same
     *
     * @param [in]          : pCfg    - Config file name with absolute path
     * @param [in]          : busName - Meaningful name for the Bus getting created
     * @param [in]          : apitest - This flag will decide to invoke exit/deinit function
     incase for validating this api alone.
     * @param [out]         : return status an integer value 0-success and 1-Failure
     ********************************************************************************************/

    DBusHandlerResult
tdk_path_message_func (DBusConnection  *conn,
        DBusMessage     *message,
        void            *user_data)
{
    CCSP_MESSAGE_BUS_INFO *bus_info =(CCSP_MESSAGE_BUS_INFO *) user_data;
    const char *interface = dbus_message_get_interface(message);
    const char *method   = dbus_message_get_member(message);
    DBusMessage *reply;
    reply = dbus_message_new_method_return (message);
    if (reply == NULL)
    {
        return DBUS_HANDLER_RESULT_HANDLED;
    }

    if(!strcmp("org.freedesktop.DBus.Introspectable", interface)  && !strcmp(method, "Introspect"))
    {
        if ( !dbus_message_append_args (reply, DBUS_TYPE_STRING, &TDK_Introspect_msg, DBUS_TYPE_INVALID))
            printf ("No memory\n");

        if (!dbus_connection_send (conn, reply, NULL))
            printf ("No memory\n");

        dbus_message_unref (reply);
        return DBUS_HANDLER_RESULT_HANDLED;
    }

    return CcspBaseIf_base_path_message_func (conn,
            message,
            reply,
            interface,
            method,
            bus_info);

}

#endif
