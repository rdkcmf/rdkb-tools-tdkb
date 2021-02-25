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

#ifndef __JSONHAL_WRP_H__
#define __JSONHAL_WRP_H__

#define CHECK(expr)                                                \
    if (!(expr))                                                   \
    {                                                              \
        return RETURN_ERR;                                         \
    }

#define FREE_JSON_OBJECT(expr) \
    if(expr)                   \
    {                          \
        json_object_put(expr); \
    }                          \

#define NULL_TYPE 0

#define XDSL_JSON_CONF_PATH "/etc/rdk/conf/xdsl_manager_conf.json"
#define XDSL_JSON_SCHEMA_PATH "/etc/rdk/schemas/xdsl_hal_schema.json"

#define RPC_GET_PARAMETERS_REQUEST "getParameters"
#define RPC_SET_PARAMETERS_REQUEST "setParameters"
#define JSON_RPC_FIELD_PARAMS "params"
#define HAL_CONNECTION_RETRY_MAX_COUNT 10
#define GET_PARAMETER_METHOD "getParameters"
#define SET_PARAMETER_METHOD "setParameters"

#define XDSL_STANDARD_USED_STR_MAX          64
/* Collection */
typedef enum
_DML_XDSL_IF_STATUS
{
    XDSL_IF_STATUS_Up               = 1,
    XDSL_IF_STATUS_Down,
    XDSL_IF_STATUS_Unknown,
    XDSL_IF_STATUS_Dormant,
    XDSL_IF_STATUS_NotPresent,
    XDSL_IF_STATUS_LowerLayerDown,
    XDSL_IF_STATUS_Error
} DML_XDSL_IF_STATUS;

typedef enum
_DML_XDSL_LINK_STATUS
{
    XDSL_LINK_STATUS_Up 		     = 1,
    XDSL_LINK_STATUS_Initializing,
    XDSL_LINK_STATUS_EstablishingLink,
    XDSL_LINK_STATUS_NoSignal,
    XDSL_LINK_STATUS_Disabled,
    XDSL_LINK_STATUS_Error
} DML_XDSL_LINK_STATUS;

/** enum wan status */
typedef enum
_DML_XDSL_LINE_WAN_STATUS
{
    XDSL_LINE_WAN_UP          = 1,
    XDSL_LINE_WAN_DOWN        = 2,
} DML_XDSL_LINE_WAN_STATUS;

/** enum line encoding */
typedef enum
_XDSL_LINE_ENCODING_ENUM
{
    DML_LINE_ENCODING_DMT = 1,
    DML_LINE_ENCODING_CAP,
    DML_LINE_ENCODING_2B1Q,
    DML_LINE_ENCODING_43BT,
    DML_LINE_ENCODING_PAM,
    DML_LINE_ENCODING_QAM
} XDSL_LINE_ENCODING_ENUM;

/** enum line power management */
typedef enum
_XDSL_LINE_POWER_MGMT_ENUM
{
    PM_STATE_L0 = 1,
    PM_STATE_L1,
    PM_STATE_L2,
    PM_STATE_L3,
    PM_STATE_L4
} XDSL_LINE_POWER_MGMT_ENUM;

/*
    PTM Part
*/
typedef enum { Up = 1,
               Down,
               Unknown,
               Dormant,
               NotPresent,
               LowerLayerDown,
               Error
}xtm_link_status_e;

/* ATM Link types */
typedef enum
{
    EOA            = 1,
    IPOA,
    PPPOA,
    CIP,
    UNCONFIGURED,
} linktype_e;

/* ATM Encapsulation*/
typedef enum
{
    LLC            = 1,
    VCMUX
} encapsulation_e;

/* ATM AAL types */
typedef enum
{
    AAL1            = 1,
    AAL2,
    AAL3,
    AAL4,
    AAL5
} aal_e;

/* ATM QOS Class */
typedef enum
{
    UBR            = 1,
    CBR,
    GFR,
    VBR_NRT,
    VBR_RT,
    UBR_PLUS,
    ABR
} QOS_CLASS_TYPE;

typedef  struct
_DML_ATM_QOS
{
    QOS_CLASS_TYPE                         QoSClass;
    unsigned int                           PeakCellRate;
    unsigned int                           MaximumBurstSize;
    unsigned int                           SustainableCellRate;
}DML_ATM_QOS , *PDML_ATM_QOS;

typedef  struct
_DML_XDSL_LINE_STATS_TIME
{
    unsigned int                            ErroredSecs;
    unsigned int                            SeverelyErroredSecs;
}
DML_XDSL_LINE_STATS_TIME, *PDML_XDSL_LINE_STATS_TIME;

typedef  struct
_DML_XDSL_LINE_STATS_QUARTERHOUR
{
    unsigned int                            ErroredSecs;
    unsigned int                            SeverelyErroredSecs;
    unsigned int                            X_RDK_LinkRetrain;
}
DML_XDSL_LINE_STATS_QUARTERHOUR, *PDML_XDSL_LINE_STATS_QUARTERHOUR;

typedef  struct
_DML_XDSL_LINE_STATS_CURRENTDAY
{
    unsigned int                            ErroredSecs;
    unsigned int                            SeverelyErroredSecs;
    unsigned int                            X_RDK_LinkRetrain;
    unsigned int                            X_RDK_InitErrors;
    unsigned int                            X_RDK_InitTimeouts;
    unsigned int                            X_RDK_SuccessfulRetrains;
}
DML_XDSL_LINE_STATS_CURRENTDAY, *PDML_XDSL_LINE_STATS_CURRENTDAY;

typedef  struct
_DML_XDSL_LINE_STATS
{
    unsigned long                           BytesSent;
    unsigned long                           BytesReceived;
    unsigned long                           PacketsSent;
    unsigned long                           PacketsReceived;
    unsigned long                           ErrorsSent;
    unsigned long                           ErrorsReceived;
    unsigned long                           DiscardPacketsSent;
    unsigned long                           DiscardPacketsReceived;
    unsigned long                           TotalStart;
    unsigned long                           ShowtimeStart;
    unsigned int                            LastShowtimeStart;
    unsigned long                           QuarterHourStart;
    unsigned long                           CurrentDayStart;
    DML_XDSL_LINE_STATS_TIME         stTotal;
    DML_XDSL_LINE_STATS_TIME         stShowTime;
    DML_XDSL_LINE_STATS_TIME         stLastShowTime;
    DML_XDSL_LINE_STATS_CURRENTDAY   stCurrentDay;
    DML_XDSL_LINE_STATS_QUARTERHOUR  stQuarterHour;
}
DML_XDSL_LINE_STATS, *PDML_XDSL_LINE_STATS;

typedef  struct
_DML_XDSL_LINE
{
    unsigned char                           Enable;
    unsigned char                           EnableDataGathering;
    unsigned long                           ulInstanceNumber;
    char                                    LowerLayers[128];
    char                                    Alias[64];
    char                                    Name[64];
    char                                    LastChange;
    char                                    StandardsSupported[512];
    char                                    XTSE[17];
    char                                    AllowedProfiles[256];
    char                                    StandardUsed[XDSL_STANDARD_USED_STR_MAX];
    char                                    XTSUsed[17];
    char                                    FirmwareVersion[64];
    DML_XDSL_IF_STATUS                      Status;
    DML_XDSL_LINK_STATUS                    LinkStatus;
    unsigned char                           Upstream;
    char                                    CurrentProfile[64];
    XDSL_LINE_POWER_MGMT_ENUM               PowerManagementState;
    unsigned int                            UpstreamMaxBitRate;
    unsigned int                            DownstreamMaxBitRate;
    unsigned int                            SuccessFailureCause;
    DML_XDSL_LINE_WAN_STATUS                WanStatus;
    unsigned int                            UPBOKLER;
    char                                    UPBOKLEPb[256];
    char                                    UPBOKLERPb[256];
    int                                     RXTHRSHds;
    unsigned int                            ACTRAMODEds;
    unsigned int                            ACTRAMODEus;
    unsigned int                            ACTINPROCds;
    unsigned int                            ACTINPROCus;
    unsigned int                            SNRMROCds;
    unsigned int                            SNRMROCus;
    unsigned int                            LastStateTransmittedDownstream;
    unsigned int                            LastStateTransmittedUpstream;
    unsigned int                            UPBOKLE;
    char                                    MREFPSDds[145];
    char                                    MREFPSDus[145];
    unsigned int                            LIMITMASK;
    unsigned int                            US0MASK;
    int                                     UpstreamAttenuation;
    int                                     UpstreamNoiseMargin;
    int                                     UpstreamPower;
    XDSL_LINE_ENCODING_ENUM                 LineEncoding;
    int                                     TRELLISds;
    int                                     TRELLISus;
    unsigned int                            ACTSNRMODEds;
    unsigned int                            ACTSNRMODEus;
    char                                    VirtualNoisePSDds[97];
    char                                    VirtualNoisePSDus[49];
    unsigned int                            ACTUALCE;
    int                                     LineNumber;
    char                                    SNRMpbus[24];
    char                                    SNRMpbds[24];
    unsigned long                           INMIATOds;
    unsigned long                           INMIATSds;
    unsigned long                           INMCCds;
    int                                     INMINPEQMODEds;
    int                                     DownstreamAttenuation;
    int                                     DownstreamNoiseMargin;
    int                                     DownstreamPower;
    char                                    XTURVendor[9];
    char                                    XTURCountry[5];
    unsigned int                            XTURANSIStd;
    unsigned int                            XTURANSIRev;
    char                                    XTUCVendor[9];
    char                                    XTUCCountry[5];
    unsigned int                            XTUCANSIStd;
    unsigned int                            XTUCANSIRev;
    DML_XDSL_LINE_STATS                     stLineStats;
}
DML_XDSL_LINE, *PDML_XDSL_LINE;

typedef  struct
_DML_XDSL_X_RDK_NLNM
{
    int           echotonoiseratio;
}
DML_XDSL_X_RDK_NLNM, *PDML_XDSL_X_RDK_NLNM;

typedef  struct
_DML_PTM_STATS
{
    unsigned long                           BytesSent;
    unsigned long                           BytesReceived;
    unsigned long                           PacketsSent;
    unsigned long                           PacketsReceived;
    unsigned int                            ErrorsSent;
    unsigned int                            ErrorsReceived;
    unsigned int                            UnicastPacketsSent;
    unsigned int                            UnicastPacketsReceived;
    unsigned int                            DiscardPacketsSent;
    unsigned int                            DiscardPacketsReceived;
    unsigned long                           MulticastPacketsSent;
    unsigned long                           MulticastPacketsReceived;
    unsigned long                           BroadcastPacketsSent;
    unsigned long                           BroadcastPacketsReceived;
    unsigned int                            UnknownProtoPacketsReceived;
}
DML_PTM_STATS , *PDML_PTM_STATS;

typedef  struct
_DML_ATM_STATS
{
    unsigned long                           BytesSent;
    unsigned long                           BytesReceived;
    unsigned long                           PacketsSent;
    unsigned long                           PacketsReceived;
    unsigned int                            ErrorsSent;
    unsigned int                            ErrorsReceived;
    unsigned long                           UnicastPacketsSent;
    unsigned long                           UnicastPacketsReceived;
    unsigned long                           DiscardPacketsSent;
    unsigned long                           DiscardPacketsReceived;
    unsigned long                           MulticastPacketsSent;
    unsigned long                           MulticastPacketsReceived;
    unsigned long                           BroadcastPacketsSent;
    unsigned long                           BroadcastPacketsReceived;
    unsigned int                            UnknownProtoPacketsReceived;
    unsigned int                            TransmittedBlocks;
    unsigned int                            ReceivedBlocks;
    unsigned int                            CRCErrors;
    unsigned int                            HECErrors;
}
DML_ATM_STATS , *PDML_ATM_STATS;

typedef  struct
_DML_ATM
{
    unsigned long                          InstanceNumber;
    unsigned char                          Enable;
    xtm_link_status_e                      Status;
    char                                   Alias[64];
    char                                   Name[64];
    char                                   Path[128];
    linktype_e                             LinkType;
    encapsulation_e                        Encapsulation;
    aal_e                                  AAL;
    unsigned char                          AutoConfig;
    unsigned char                          FCSPreserved;
    char                                   DestinationAddress[256];
    unsigned int                           LastChange;
    char                                   LowerLayers[1024];
    char                                   VCSearchList[256];
    DML_ATM_QOS                            Qos;
    DML_ATM_STATS                          Statistics;
}
DML_ATM,  *PDML_ATM;

typedef  struct
_DML_XDSL_CHANNEL_STATS_TIME
{
    unsigned int                            XTURFECErrors;
    unsigned int                            XTUCFECErrors;
    unsigned int                            XTURHECErrors;
    unsigned int                            XTUCHECErrors;
    unsigned int                            XTURCRCErrors;
    unsigned int                            XTUCCRCErrors;
}
DML_XDSL_CHANNEL_STATS_TIME, *PDML_XDSL_CHANNEL_STATS_TIME;

typedef  struct
_DML_XDSL_CHANNEL_STATS_QUARTERHOUR
{
    unsigned int                            XTURFECErrors;
    unsigned int                            XTUCFECErrors;
    unsigned int                            XTURHECErrors;
    unsigned int                            XTUCHECErrors;
    unsigned int                            XTURCRCErrors;
    unsigned int                            XTUCCRCErrors;
    unsigned int                            X_RDK_LinkRetrain;
}
DML_XDSL_CHANNEL_STATS_QUARTERHOUR, *PDML_XDSL_CHANNEL_STATS_QUARTERHOUR;

typedef  struct
_DML_XDSL_CHANNEL_STATS_CURRENTDAY
{
    unsigned int                           XTURFECErrors;
    unsigned int                           XTUCFECErrors;
    unsigned int                           XTURHECErrors;
    unsigned int                           XTUCHECErrors;
    unsigned int                           XTURCRCErrors;
    unsigned int                           XTUCCRCErrors;
    unsigned int                           X_RDK_LinkRetrain;
    unsigned int                           X_RDK_InitErrors;
    unsigned int                           X_RDK_InitTimeouts;
    unsigned int                           X_RDK_SeverelyErroredSecs;
    unsigned int                           X_RDK_ErroredSecs;
}
DML_XDSL_CHANNEL_STATS_CURRENTDAY, *PDML_XDSL_CHANNEL_STATS_CURRENTDAY;

typedef  struct
_DML_XDSL_CHANNEL_STATS
{
    unsigned long                        BytesSent;
    unsigned long                        BytesReceived;
    unsigned long                        PacketsSent;
    unsigned long                        PacketsReceived;
    unsigned int                         ErrorsSent;
    unsigned int                         ErrorsReceived;
    unsigned int                         DiscardPacketsSent;
    unsigned int                         DiscardPacketsReceived;
    unsigned int                         TotalStart;
    unsigned int                         ShowtimeStart;
    unsigned int                         LastShowtimeStart;
    unsigned int                         CurrentDayStart;
    unsigned int                         QuarterHourStart;
    DML_XDSL_CHANNEL_STATS_TIME          stTotal;
    DML_XDSL_CHANNEL_STATS_TIME          stShowTime;
    DML_XDSL_CHANNEL_STATS_TIME          stLastShowTime;
    DML_XDSL_CHANNEL_STATS_CURRENTDAY    stCurrentDay;
    DML_XDSL_CHANNEL_STATS_QUARTERHOUR   stQuarterHour;
}
DML_XDSL_CHANNEL_STATS, *PDML_XDSL_CHANNEL_STATS;

typedef  struct
_DML_XDSL_CHANNEL
{
    unsigned char                       Enable;
    unsigned int                        ulInstanceNumber;
    int                                 LineIndex;
    unsigned int                        LastChange;
    char                                LowerLayers[1024];
    char                                Alias[64];
    char                                Name[64];
    DML_XDSL_IF_STATUS                  Status;
    char                                LinkEncapsulationSupported[256];
    char                                LinkEncapsulationUsed[32];
    unsigned int                        LPATH;
    unsigned int                        INTLVDEPTH;
    int                                 INTLVBLOCK;
    unsigned int                        ActualInterleavingDelay;
    int                                 ACTINP;
    unsigned char                       INPREPORT;
    int                                 NFEC;
    int                                 RFEC;
    int                                 LSYMB;
    unsigned int                        UpstreamCurrRate;
    unsigned int                        DownstreamCurrRate;
    unsigned int                        ACTNDR;
    unsigned int                        ACTINPREIN;
    DML_XDSL_CHANNEL_STATS             stChannelStats;
}
DML_XDSL_CHANNEL, *PDML_XDSL_CHANNEL;

#endif



