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

//Defining this macro to avoid -Wformat-truncation issue from gcc
#define snprintf_t(...) (snprintf(__VA_ARGS__) < 0 ? abort() : (void)0)

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

#define TELCOVOICEMGR_CONF_FILE         "/etc/rdk/conf/telcovoice_manager_conf.json"
#define TELCOVOICEMGR_JSON_SCHEMA_PATH  "/etc/rdk/schemas/telcovoice_hal_schema.json"
#define HALINIT                         "Devices.Services.VoiceHalInit"
#define DML_VOICESERVICE                "Device.Services.VoiceService.%d."
#define DML_VOICESERVICE_PHYIFACE       "Device.Services.VoiceService.%d.PhyInterface.%d."
#define DML_VOICESERVICE_VOICEPROF      "Device.Services.VoiceService.%d.VoiceProfile.%d."
#define JSON_RPC_PARAM_ARR_INDEX        0

#define BUF_LEN_16                          16
#define BUF_LEN_512                         512
#define BUF_LEN_256                         256
#define  JSON_MAX_VAL_ARR_SIZE              256
#define  JSON_MAX_STR_ARR_SIZE              256

#define  TELCOVOICE_DATA_MAX                               1
#define  TELCOVOICEMGR_DML_NUMBER_OF_VOICE_SERVICES        1
#define  TELCOVOICEMGR_DML_NUMBER_OF_VOIP_PROFILE          1
#define  TELCOVOICEMGR_DML_NUMBER_OF_SIP_NETWORK           1
#define  TELCOVOICEMGR_DML_NUMBER_OF_SIP_CLIENTS           1
#define  TELCOVOICEMGR_DML_NUMBER_OF_CALLCONTROL_LINES     1


#define TELCOVOICEMGR_DATA_MAX_VOICE_SERVICES                1
#define TELCOVOICEMGR_DATA_MAX_VOICE_CAPABILITIES_CODECS     1
#define TELCOVOICEMGR_DATA_MAX_PROFILE                       1
#define TELCOVOICEMGR_DATA_MAX_LINE                          1
#define TELCOVOICEMGR_DATA_MAX_PHYintERFACE                  1
#define TELCOVOICEMGR_DATA_MAX_DML_LINE_CODECLIST            1
#define TELCOVOICEMGR_DATA_MAX_DML_LINE_RINGER_PATTERN       1
#define TELCOVOICEMGR_DATA_MAX_DML_LINE_RINGER_DESCRIPTION   1
#define TELCOVOICEMGR_DATA_MAX_DML_LINE_RINGER_EVENT         1
#define TELCOVOICEMGR_DATA_MAX_DML_LINE_SIP_EVENTSUBSCRIBE   1
#define TELCOVOICEMGR_DATA_MAX_DML_TONE_PATTERN              1
#define TELCOVOICEMGR_DATA_MAX_TONE_DESCRIPTION              1
#define TELCOVOICEMGR_DATA_MAX_TONE_EVENT                    1
#define TELCOVOICEMGR_DATA_MAX_DML_LINE_SESSION              1
#define TELCOVOICEMGR_DATA_MAX_DML_SIP_EVENTSUBSCRIBE        1
#define TELCOVOICEMGR_DATA_MAX_DML_SIP_RESPONSEMAP           1
#define TELCOVOICEMGR_DATA_MAX_NUMBERINGPLAN_PREFIXINFO      1
#define TELCOVOICEMGR_DATA_MAX_BUTTON                        1
#define TELCOVOICEMGR_DATA_MAX_PHYINTERFACE                  1

#define  STR_LEN_2                           2
#define  STR_LEN_4                           4
#define  STR_LEN_5                           5
#define  STR_LEN_13                          13
#define  STR_LEN_16                          16
#define  STR_LEN_20                          20
#define  STR_LEN_24                          24
#define  STR_LEN_32                          32
#define  STR_LEN_40                          40
#define  STR_LEN_42                          42
#define  STR_LEN_45                          45
#define  STR_LEN_64                          64
#define  STR_LEN_128                         128
#define  STR_LEN_256                         256
#define  STR_LEN_389                         389

#define telcovoicemgr_hal_get_voiceService_index                telcovoicemgr_hal_get_first_index
#define telcovoicemgr_hal_get_phyInterface_index                telcovoicemgr_hal_get_second_index
#define telcovoicemgr_hal_get_voiceProfile_index                telcovoicemgr_hal_get_second_index
#define telcovoicemgr_hal_get_voiceProfile_line_index           telcovoicemgr_hal_get_third_index
#define  TELCOVOICEMGR_DML_NUMBER_OF_PHY_INTERFACE       1
#define  TELCOVOICEMGR_DML_NUMBER_OF_VOICE_SERVICES      1
#define  TELCOVOICEMGR_DML_NUMBER_OF_VOICE_PROFILE       1
#define TELCOVOICEMGR_DATA_MAX_LINE                      1
#define FIRST_INDEX  1
#define SECOND_INDEX 2
#define THIRD_INDEX  3

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

typedef struct
{
    unsigned int                   id;
    unsigned char                  ResetStatistics;
    unsigned int                   PacketsSent;
    unsigned int                   PacketsReceived;
    unsigned int                   BytesSent;
    unsigned int                   BytesReceived;
    unsigned int                   PacketsLost;
    unsigned int                   Overruns;
    unsigned int                   Underruns;
    unsigned int                   IncomingCallsReceived;
    unsigned int                   IncomingCallsAnswered;
    unsigned int                   IncomingCallsConnected;
    unsigned int                   IncomingCallsFailed;
    unsigned int                   OutgoingCallsAttempted;
    unsigned int                   OutgoingCallsAnswered;
    unsigned int                   OutgoingCallsConnected;
    unsigned int                   OutgoingCallsFailed;
    unsigned int                   CallsDropped;
    unsigned int                   TotalCallTime;
    unsigned int                   ServerDownTime;
    unsigned int                   ReceivePacketLossRate;
    unsigned int                   FarEndPacketLossRate;
    unsigned int                   ReceiveInterarrivalJitter;
    unsigned int                   FarEndInterarrivalJitter;
    unsigned int                   RoundTripDelay;
    unsigned int                   AverageReceiveInterarrivalJitter;
    unsigned int                   AverageFarEndInterarrivalJitter;
    unsigned int                   AverageRoundTripDelay;
} TELCOVOICEMGR_DML_VOICESERVICE_STATS;

typedef enum _TONEFILEFORMATS_ENUM
{
    TONE_FILEFORMAT_G_711MuLaw,
    TONE_FILEFORMAT_G_711ALaw,
    TONE_FILEFORMAT_G_729,
    TONE_FILEFORMAT_MP3,
    TONE_FILEFORMAT_WAV,
    TONE_FILEFORMAT_AMR
} TONEFILEFORMATS_ENUM;

typedef enum _RINGFILEFORMATS_ENUM
{
    RING_FILEFORMAT_MIDI,
    RING_FILEFORMAT_SMAF_MMF,
    RING_FILEFORMAT_RTTTL,
    RING_FILEFORMAT_MP3,
    RING_FILEFORMAT_WAV,
    RING_FILEFORMAT_AMR
} RINGFILEFORMATS_ENUM;

typedef enum _CAPABILITIES_DIALTYPE_ENUM
{
    CAP_DIALTYPE_TONE,
    CAP_DIALTYPE_PULSE,
    CAP_DIALTYPE_TONE_PLUSE
} CAPABILITIES_DIALTYPE_ENUM;

typedef enum _POTS_DIALTYPE_ENUM
{
    POTS_DIALTYPE_TONE,
    POTS_DIALTYPE_PULSE
} POTS_DIALTYPE_ENUM;

typedef enum _CAPABILITIESCODEC_ENUM
{
   CAP_CODEC_AMR,
   CAP_CODEC_CLEARMODE,
   CAP_CODEC_EVRC1,
   CAP_CODEC_EVRCB1,
   CAP_CODEC_G_711MULAW,
   CAP_CODEC_G_711ALAW,
   CAP_CODEC_G_726,
   CAP_CODEC_G_729,
   CAP_CODEC_G_729_1,
   CAP_CODEC_G_729A,
   CAP_CODEC_G_729E,
   CAP_CODEC_G_728,
   CAP_CODEC_G_723_1,
   CAP_CODEC_G_722,
   CAP_CODEC_G_722_1,
   CAP_CODEC_G_722_2,
   CAP_CODEC_GENERICCOMFORTNOISE,
   CAP_CODEC_GSM_FR,
   CAP_CODEC_GSM_HR,
   CAP_CODEC_GSM_EFR,
   CAP_CODEC_ILBC,
   CAP_CODEC_SPEEX
} CAPABILITIESCODEC_ENUM;

typedef enum _FACILITYACTIONS_ENUM
{
    FACILITY_ACTION_AA_REGISTER,
    FACILITY_ACTION_AA_ERASE,
    FACILITY_ACTION_AA_intERROGATE,
    FACILITY_ACTION_CA_ACTIVATE,
    FACILITY_ACTION_CCBS_ACTIVATE,
    FACILITY_ACTION_CCBS_DEACTIVATE,
    FACILITY_ACTION_CCBS_intERROGATE,
    FACILITY_ACTION_CCNR_ACTIVATE,
    FACILITY_ACTION_CCNR_DEACTIVATE,
    FACILITY_ACTION_CCNR_intERROGATE,
    FACILITY_ACTION_CFB_REGISTER,
    FACILITY_ACTION_CFB_ACTIVATE,
    FACILITY_ACTION_CFB_DEACTIVATE,
    FACILITY_ACTION_CFB_ERASE,
    FACILITY_ACTION_CFB_intERROGATE,
    FACILITY_ACTION_CFNR_REGISTER,
    FACILITY_ACTION_CFNR_ACTIVATE,
    FACILITY_ACTION_CFNR_DEACTIVATE,
    FACILITY_ACTION_CFNR_ERASE,
    FACILITY_ACTION_CFNR_intERROGATE,
    FACILITY_ACTION_CFNR_TIMER,
    FACILITY_ACTION_CFT_ACTIVATE,
    FACILITY_ACTION_CFT_DEACTIVATE,
    FACILITY_ACTION_CFT_intERROGATE,
    FACILITY_ACTION_CFU_REGISTER,
    FACILITY_ACTION_CFU_ACTIVATE,
    FACILITY_ACTION_CFU_DEACTIVATE,
    FACILITY_ACTION_CFU_ERASE,
    FACILITY_ACTION_CFU_intERROGATE,
    FACILITY_ACTION_CLIR_ACTIVATE,
    FACILITY_ACTION_CLIR_DEACTIVATE,
    FACILITY_ACTION_CLIR_intERROGATE,
    FACILITY_ACTION_CP_INVOKE,
    FACILITY_ACTION_CW_ACTIVATE,
    FACILITY_ACTION_CW_DEACTIVATE,
    FACILITY_ACTION_CW_INVOKE,
    FACILITY_ACTION_DND_ACTIVATE,
    FACILITY_ACTION_DND_DEACTIVATE,
    FACILITY_ACTION_DND_intERROGATE,
    FACILITY_ACTION_EXT_INVOKE,
    FACILITY_ACTION_LINE_INVOKE,
    FACILITY_ACTION_MAILBOX_INVOKE,
    FACILITY_ACTION_OCB_ACTIVATE,
    FACILITY_ACTION_OCB_DEACTIVATE,
    FACILITY_ACTION_OCB_intERROGATE,
    FACILITY_ACTION_PSO_ACTIVATE,
    FACILITY_ACTION_PW_SET,
    FACILITY_ACTION_SCF_ACTIVATE,
    FACILITY_ACTION_SCF_DEACTIVATE,
    FACILITY_ACTION_SCF_intERROGATE,
    FACILITY_ACTION_SCREJ_ACTIVATE,
    FACILITY_ACTION_SCREJ_DEACTIVATE,
    FACILITY_ACTION_SCREJ_intERROGATE,
    FACILITY_ACTION_SR_ACTIVATE,
    FACILITY_ACTION_SR_DEACTIVATE,
    FACILITY_ACTION_SR_intERROGATE
} FACILITYACTIONS_ENUM;

typedef enum _H325AUTHMETHODS_ENUM
{
    H325_AUTH_DHEXCH,
    H325_AUTH_PWDSYMENC,
    H325_AUTH_PWDHASH,
    H325_AUTH_CERTSIGN,
    H325_AUTH_IPSEC,
    H325_AUTH_TLS
} H325AUTHMETHODS_ENUM;

typedef enum _TLSAUTHENTICATIONPROTOCOLS_ENUM
{
    TLS_AUTH_PROTOCOL_NULL,
    TLS_AUTH_PROTOCOL_MD5,
    TLS_AUTH_PROTOCOL_SHA_1,
    TLS_AUTH_PROTOCOL_SHA_2,
    TLS_AUTH_PROTOCOL_AEAD
} TLSAUTHENTICATIONPROTOCOLS_ENUM;

typedef enum _TLSENCRYPTIONPROTOCOLS_ENUM
{
    TLS_ENCRYPT_PROTOCOL_NULL,
    TLS_ENCRYPT_PROTOCOL_RC4,
    TLS_ENCRYPT_PROTOCOL_RC2,
    TLS_ENCRYPT_PROTOCOL_DES,
    TLS_ENCRYPT_PROTOCOL_3DES,
    TLS_ENCRYPT_PROTOCOL_AES,
    TLS_ENCRYPT_PROTOCOL_CAMELLIA
} TLSENCRYPTIONPROTOCOLS_ENUM;

typedef enum _TLSKEYEXCHANGEPROTOCOLS_ENUM
{
    TLS_EXCHANGE_PROTOCOL_RSA,
    TLS_EXCHANGE_PROTOCOL_DSS,
    TLS_EXCHANGE_PROTOCOL_DHE_RSA,
    TLS_EXCHANGE_PROTOCOL_DHE_DSS,
    TLS_EXCHANGE_PROTOCOL_ECDHE_RSA,
    TLS_EXCHANGE_PROTOCOL_ECDHE_ECDSA
} TLSKEYEXCHANGEPROTOCOLS_ENUM;

typedef enum _STATUS_ENUM
{
    STATUS_UP,
    STATUS_ERROR,
    STATUS_TESTING,
    STATUS_DISABLED
} STATUS_ENUM;

typedef enum _SIP_STATUS_ENUM
{
    SIP_STATUS_UP,
    SIP_STATUS_ERROR,
    SIP_STATUS_DISABLED
} SIP_STATUS_ENUM;

typedef enum _APPLICATIONintERFACE_ENUM
{
   APP_intERFACE_VOIP,
   APP_intERFACE_VOATM,
   APP_intERFACE_DATA
} APPLICATIONintERFACE_ENUM;

typedef enum _ISDN_BRI_PROTOCOL_ENUM
 {
    BRI_PROTOCOL_EUROISDN,
    BRI_PROTOCOL_NI_1,
    BRI_PROTOCOL_NI_2,
    BRI_PROTOCOL_5ESS,
    BRI_PROTOCOL_NTT,
    BRI_PROTOCOL_VN3,
    BRI_PROTOCOL_VN4,
    BRI_PROTOCOL_QSIG
} ISDN_BRI_PROTOCOL_ENUM;

typedef enum _ISDN_PRI_PROTOCOL_ENUM
{
    PRI_PROTOCOL_EUROISDN,
    PRI_PROTOCOL_NI_1,
    PRI_PROTOCOL_NI_2,
    PRI_PROTOCOL_4ESS,
    PRI_PROTOCOL_5ESS,
    PRI_PROTOCOL_NTT,
    PRI_PROTOCOL_QSIG
} ISDN_PRI_PROTOCOL_ENUM;

typedef enum _ISDN_PROTOCOL_ENUMULATION_ENUM
{
    ISDN_PROTO_ENUMULATION_TE,
    ISDN_PROTO_ENUMULATION_NT
} ISDN_PROTOCOL_ENUMULATION_ENUM;

typedef enum _ISDN_TEI_NEGOTIATION_ENUM
{
    ISDN_TEI_NEGO_STATIC,
    ISDN_TEI_NEGO_DYNAMIC
} ISDN_TEI_NEGOTIATION_ENUM;

typedef enum _ISDN_LINECODE_ENUM
{
    ISDN_LINECODE_AMI,
    ISDN_LINECODE_HDB3,
    ISDN_LINECODE_B8ZS
} ISDN_LINECODE_ENUM;

typedef enum _ISDN_ESF_ENUM
{
    ISDN_ESF_NONE,
    ISDN_ESF_DF,
    ISDN_ESF_MF,
    ISDN_ESF_EMF,
    ISDN_ESF_SF,
    ISDN_ESF_ESF,
    ISDN_ESF_AUTODETECT
}ISDN_ESF_ENUM;

typedef enum _ISDN_PHYintERFACETYPE_ENUM
{
    ISDN_PHYintERFACE_T1,
    ISDN_PHYintERFACE_E1
}ISDN_PHYintERFACETYPE_ENUM;

typedef enum _ISDN_CLOCKMODE_ENUM
{
    ISDN_CLKMODE_MASTER,
    ISDN_CLKMODE_SLAVE
} ISDN_CLOCKMODE_ENUM;

typedef enum _SIGNALING_MODE_ENUM
{
    SIGNALING_MODE_LOOPSTART,
    SIGNALING_MODE_GROUNDSTART
} SIGNALING_MODE_ENUM;

typedef enum _DIAG_STATE_ENUM
{
    DIAG_STATE_NONE,
    DIAG_STATE_REQUESTED,
    DIAG_STATE_COMPLETE,
    DIAG_STATE_ERROR_intERNAL,
    DIAG_STATE_ERROR_OTHER
} DIAG_STATE_ENUM;

typedef enum _FXO_TEST_SELECTOR_ENUM
{
    FXO_TEST_SELECTOR_BATTERY,
    FXO_TEST_SELECTOR_DIALTONE
} FXO_TEST_SELECTOR_ENUM;

typedef enum _FXS_TEST_SELECTOR_ENUM
{
    FXS_TEST_SELECTOR_HAZARD_POTENTIAL,
    FXS_TEST_SELECTOR_FOREIGN_VOLTAGE,
    FXS_TEST_SELECTOR_RESISTIVE_FAULTS,
    FXS_TEST_SELECTOR_OFF_HOOK,
    FXS_TEST_SELECTOR_REN
} FXS_TEST_SELECTOR_ENUM;

typedef enum _TEST_RESULT_ENUM
{
    TEST_RESULT_SUCCESS,
    TEST_RESULT_FAILURE
} TEST_RESULT_ENUM;

typedef enum _TERMINAL_TYPE_ENUM
{
    TERMINAL_AUDIO,
    TERMINAL_FAX,
    TERMINAL_MODEM,
    TERMINAL_ANY
} TERMINAL_TYPE_ENUM;

typedef enum _STREAM_TYPE_ENUM
{
    STREAM_AUDIO,
    STREAM_VIDEO,
    STREAM_FAX,
    STREAM_MODEM
} STREAM_TYPE_ENUM;


typedef enum _FUNCTION_TYPE_ENUM
{
    FUNCTION_DEFAULT,
    FUNCTION_CCBSCALLBACK,
    FUNCTION_CCNRCALLBACK,
    FUNCTION_intERNALCALL,
    FUNCTION_RINGSPLASH,
    FUNCTION_GROUP
} FUNCTION_TYPE_ENUM;

typedef enum _STANDARD_ENUM
{
    STANDARD_GAP,
    STANDARD_CAT_IQ_1_0,
    STANDARD_CAT_IQ_2_0,
    STANDARD_CAT_IQ_2_1,
    STANDARD_CAT_IQ_3_0,
    STANDARD_CAT_IQ_4_0
} STANDARD_ENUM, PORTABLE_TYPE_ENUM;

typedef enum _RF_POWER_CTRL_ENUM
{
    POWER_CTRL_NORMAL,
    POWER_CTRL_REDUCED
} RF_POWER_CTRL_ENUM;

typedef enum _ENCRYPTION_TYPE_ENUM
{
    ENCRYPTION_DSC,
    ENCRYPTION_DSC2,
    ENCRYPTION_CCM
} ENCRYPTION_TYPE_ENUM;

typedef enum _ORIGIN_ENUM
{
    ORIGIN_AUTOCONFIGURED,
    ORIGIN_STATIC
} ORIGIN_ENUM;

typedef enum _SIP_CLIENT_CONTACT_STATUS_ENUM
{
    SIP_CLIENT_CONTACT_STATUS_AUTOCONFIGURED,
    SIP_CLIENT_CONTACT_STATUS_STATIC
} SIP_CLIENT_CONTACT_STATUS_ENUM;

typedef enum _TRANSPORT_ENUM
{
    TRANSPORT_UDP,
    TRANSPORT_TCP,
    TRANSPORT_TLS,
    TRANSPORT_SCTP
} TRANSPORT_ENUM;

typedef enum _CODECPRIORITY_ENUM
{
    CODEC_PRIORITY_LOCAL,
    CODEC_PRIORITY_REMOTE
} CODECPRIORITY_ENUM;

typedef enum _PASS_THROUGH_ENUM
{
    PASS_THROUGH_DISABLE,
    PASS_THROUGH_AUTO,
    PASS_THROUGH_FORCE
}PASS_THROUGH_ENUM;

typedef enum _REGISTRATION_STATUS_ENUM
{
    REGISTRATION_IN_REACH,
    REGISTRATION_NOT_IN_REACH
} REGISTRATION_STATUS_ENUM;

typedef enum _CONTROL_ENUM
{
    CONTROL_UNREGISTER,
    CONTROL_DISABLE
}CONTROL_ENUM;

typedef enum _CLIENT_STATUS_ENUM
{
    CLIENT_STATUS_UP,
    CLIENT_STATUS_INITIALIZING,
    CLIENT_STATUS_REGISTERING,
    CLIENT_STATUS_DEREGISTERING,
    CLIENT_STATUS_ERROR_MISCONFIGURED,
    CLIENT_STATUS_ERROR_NETWORK,
    CLIENT_STATUS_ERROR_REGISTRATION,
    CLIENT_STATUS_QUIESCENT,
    CLIENT_STATUS_DISABLED
}CLIENT_STATUS_ENUM;

typedef enum _NETWORK_STATUS_ENUM
{
    NETWORK_STATUS_UP,
    NETWORK_STATUS_RESOLVING,
    NETWORK_STATUS_ERROR_DNS,
    NETWORK_STATUS_ERROR_OTHER,
    NETWORK_STATUS_DISABLED
}NETWORK_STATUS_ENUM;

typedef enum _TRUNK_STATUS_ENUM
{
    TRUNK_STATUS_UP,
    TRUNK_STATUS_INITIALIZING,
    TRUNK_STATUS_REGISTERING,
    TRUNK_STATUS_UNREGISTERING,
    TRUNK_STATUS_ERROR,
    TRUNK_STATUS_TESTING,
    TRUNK_STATUS_DISABLED
} TRUNK_STATUS_ENUM;

typedef enum _TERMINAL_STATUS_ENUM
{
    TERMINAL_STATUS_UP,
    TERMINAL_STATUS_INITIALIZING,
    TERMINAL_STATUS_REGISTERING,
    TERMINAL_STATUS_UNREGISTERING,
    TERMINAL_STATUS_ERROR,
    TERMINAL_STATUS_TESTING,
    TERMINAL_STATUS_QUIESCENT,
    TERMINAL_STATUS_DISABLED
} TERMINAL_STATUS_ENUM;

typedef enum _LINE_STATUS_ENUM
{
    LINE_STATUS_UP,
    LINE_STATUS_ERROR,
    LINE_STATUS_TESTING,
    LINE_STATUS_QUIESCENT,
    LINE_STATUS_DISABLED
} LINE_STATUS_ENUM;


typedef enum _intERWORK_STATUS_ENUM
{
    intERWORK_STATUS_UP,
    intERWORK_STATUS_ERROR,
    intERWORK_STATUS_QUIESCENT,
    intERWORK_STATUS_DISABLED
} intERWORK_STATUS_ENUM;

typedef enum _CALLCTRL_EXT_STATUS_ENUM
{
    CALLCTRL_CALLSTATUS_UP,
    CALLCTRL_CALLSTATUS_INITIALIZING,
    CALLCTRL_CALLSTATUS_ERROR,
    CALLCTRL_CALLSTATUS_TESTING,
    CALLCTRL_CALLSTATUS_QUIESCENT,
    CALLCTRL_CALLSTATUS_DISABLED
} CALLCTRL_EXT_STATUS_ENUM;

typedef enum _MGCP_REGISTER_MODE_ENUM
{
   MGCP_REGISTER_WILDCARD,
   MGCP_REGISTER_INDIVIDUAL
} MGCP_REGISTER_MODE_ENUM;

typedef enum _CALLSTATUS_ENUM
{
    CALLSTATUS_IDLE,
    CALLSTATUS_DIALING,
    CALLSTATUS_DELIVERED,
    CALLSTATUS_CONNECTED,
    CALLSTATUS_ALERTING,
    CALLSTATUS_DISCONNECTED
} CALLSTATUS_ENUM;

typedef enum _CALLCTRL_EXT_CALLSTATUS_ENUM
{
    CALLCTRL_STATUS_IDLE,
    CALLCTRL_STATUS_DIALING,
    CALLCTRL_STATUS_DELIVERED,
    CALLCTRL_STATUS_CONNECTED,
    CALLCTRL_STATUS_ALERTING,
    CALLCTRL_STATUS_DISCONNECTED
} CALLCTRL_EXT_CALLSTATUS_ENUM;

typedef enum _ACC_REGISTRATION_STATUS_ENUM
{
    ACC_REGISTERED,
    ACC_UNREGISTERED
} ACC_REGISTRATION_STATUS_ENUM;


typedef enum _SIP_REGISTRAR_ACC_ENABLE_ENUM
{
    SIP_REGISTRAR_ACC_ENABLE,
    SIP_REGISTRAR_ACC_QUIESCENT,
    SIP_REGISTRAR_ACC_DISABLE
} SIP_REGISTRAR_ACC_ENABLE_ENUM;

typedef enum _REGISTER_MODE_ENUM
{
    REGISTER_MODE_RFC3261,
    REGISTER_MODE_STATIC,
    REGISTER_MODE_RFC6140,
    REGISTER_MODE_TISPAN
} REGISTER_MODE_ENUM;

typedef enum _MGCP_NETWORK_REG_STATUS_ENUM
{
    MGCP_NETWORK_REG_STATUS_UP,
    MGCP_NETWORK_REG_STATUS_RESOLVING,
    MGCP_NETWORK_REG_STATUS_ERROR_DNS,
    MGCP_NETWORK_REG_STATUS_ERROR_OTHER,
    MGCP_NETWORK_REG_STATUS_DISABLED
} MGCP_NETWORK_REG_STATUS_ENUM;

typedef struct _DML_VOICESERVICE_CAPABILITIES_SIP_CLIENT
{
    char                                 Extensions[STR_LEN_256];
    char                                 URISchemes[STR_LEN_256];
    char                                 EventTypes[STR_LEN_256];
    TLSAUTHENTICATIONPROTOCOLS_ENUM      TLSAuthenticationProtocols;
    char                                 TLSAuthenticationKeySizes[STR_LEN_256];
    TLSENCRYPTIONPROTOCOLS_ENUM          TLSEncryptionProtocols;
    char                                 TLSEncryptionKeySizes[STR_LEN_256];
    TLSKEYEXCHANGEPROTOCOLS_ENUM         TLSKeyExchangeProtocols;
} DML_VOICESERVICE_CAPABILITIES_SIP_CLIENT,*PDML_VOICESERVICE_CAPABILITIES_SIP_CLIENT;

typedef struct _DML_VOICESERVICE_CAPABILITIES_SIP_REGISTRAR
{
    char                                Extensions[STR_LEN_256];
    char                                URISchemes[STR_LEN_256];
    char                                EventTypes[STR_LEN_256];
    TLSAUTHENTICATIONPROTOCOLS_ENUM     TLSAuthenticationProtocols;
    char                                TLSAuthenticationKeySizes[STR_LEN_256];
    TLSENCRYPTIONPROTOCOLS_ENUM         TLSEncryptionProtocols;
    char                                TLSEncryptionKeySizes[STR_LEN_256];
    TLSKEYEXCHANGEPROTOCOLS_ENUM        TLSKeyExchangeProtocols;
} DML_VOICESERVICE_CAPABILITIES_SIP_REGISTRAR, *PDML_VOICESERVICE_CAPABILITIES_SIP_REGISTRAR;


typedef struct _DML_VOICESERVICE_CAPABILITIES_SIP
 {
    DML_VOICESERVICE_CAPABILITIES_SIP_CLIENT        Client_Obj;
    DML_VOICESERVICE_CAPABILITIES_SIP_REGISTRAR     Registrar_Obj;
 } DML_VOICESERVICE_CAPABILITIES_SIP, *PDML_VOICESERVICE_CAPABILITIES_SIP;

typedef struct _DML_VOICESERVICE_CAPABILITIES_MGCP
 {
    char Extensions[STR_LEN_256];
 } DML_VOICESERVICE_CAPABILITIES_MGCP,*PDML_VOICESERVICE_CAPABILITIES_MGCP;


typedef struct _DML_VOICESERVICE_CAPABILITIES_H323
 {
    unsigned char FastStart;
    H325AUTHMETHODS_ENUM H235AuthenticationMethods;
 } DML_VOICESERVICE_CAPABILITIES_H323,*PDML_VOICESERVICE_CAPABILITIES_H323;

typedef struct _DML_VOICESERVICE_CAPABILITIES_ISDN
 {
    unsigned char    MSN;
    unsigned char    DDI;
    unsigned char    MCID;
    unsigned char    MWI;
    unsigned char    AoC;
    unsigned char    ECT;
 } DML_VOICESERVICE_CAPABILITIES_ISDN, *PDML_VOICESERVICE_CAPABILITIES_ISDN;

typedef struct _DML_VOICESERVICE_CAPABILITIES_POTS
 {
    CAPABILITIES_DIALTYPE_ENUM      DialType;
    unsigned char                   ClipGeneration;
    unsigned char                   chargingPulse;
 } DML_VOICESERVICE_CAPABILITIES_POTS, *PDML_VOICESERVICE_CAPABILITIES_POTS;

typedef struct _DML_VOICESERVICE_CAPABILITIES_QUALITYINDICATOR
 {
    char              QIModelsSupported[STR_LEN_256];
    unsigned int      MaxQIValues;
    unsigned int      MaxWorstQIValues;
 } DML_VOICESERVICE_CAPABILITIES_QUALITYINDICATOR, *PDML_VOICESERVICE_CAPABILITIES_QUALITYINDICATOR;

typedef struct _DML_VOICESERVICE_CAPABILITIES_CODEC
 {
    unsigned long               uInstanceNumber;
    void*                       pParentVoiceService;
    char                        Alias[STR_LEN_64];
    CAPABILITIESCODEC_ENUM      Codec;
    unsigned int                BitRate;
    char                        PacketizationPeriod[STR_LEN_256];
    unsigned char               SilenceSuppression;
 } DML_VOICESERVICE_CAPABILITIES_CODEC, *PDML_VOICESERVICE_CAPABILITIES_CODEC;

typedef  struct _DML_VOICESERVICE_CAPABILITIES_CODEC_CTRL_T_
 {
    DML_VOICESERVICE_CAPABILITIES_CODEC     dml;
    unsigned char                           updated;
 } DML_VOICESERVICE_CAPABILITIES_CODEC_CTRL_T,*PDML_VOICESERVICE_CAPABILITIES_CODEC_CTRL_T;


typedef  struct _DML_VOICESERVICE_CAPABILITIES_CODEC_LIST_T_
 {
    unsigned int                                    ulQuantity;
    PDML_VOICESERVICE_CAPABILITIES_CODEC_CTRL_T     pdata[TELCOVOICE_DATA_MAX];
 } DML_VOICESERVICE_CAPABILITIES_CODEC_LIST_T,*PDML_VOICESERVICE_CAPABILITIES_CODEC_LIST_T;

typedef struct _DML_VOICESERVICE_CAPABILITIES
 {
    int                                              MaxLineCount;
    int                                              MaxExtensionCount;
    int                                              MaxCallLogCount;
    int                                              MaxSessionsPerLine;
    int                                              MaxSessionsPerExtension;
    int                                              MaxSessionCount;
    char                                             NetworkConnectionModes[STR_LEN_256];
    char                                             UserConnectionModes[STR_LEN_256];
    TONEFILEFORMATS_ENUM                             ToneFileFormats;
    RINGFILEFORMATS_ENUM                             RingFileFormats;
    FACILITYACTIONS_ENUM                             FacilityActions;
    DML_VOICESERVICE_CAPABILITIES_SIP                SIP;
    DML_VOICESERVICE_CAPABILITIES_MGCP               MGCP;
    DML_VOICESERVICE_CAPABILITIES_H323               H323;
    DML_VOICESERVICE_CAPABILITIES_ISDN               ISDN;
    DML_VOICESERVICE_CAPABILITIES_POTS               POTS;
    DML_VOICESERVICE_CAPABILITIES_CODEC_LIST_T       Codec;
    DML_VOICESERVICE_CAPABILITIES_QUALITYINDICATOR   QualityIndicator;
 } DML_VOICESERVICE_CAPABILITIES, *PDML_VOICESERVICE_CAPABILITIES;

typedef struct _DML_RESERVEDPORTS
{
    void*      pParentVoiceService;
    char       WANPortRange[STR_LEN_256];
    char       LANPortRange[STR_LEN_256];
} DML_RESERVEDPORTS,*PDML_RESERVEDPORTS;


typedef struct _DML_ISDN_BRI
{
    unsigned long                    uInstanceNumber;
    void*                            pParentVoiceService;
    unsigned char                    Enable;
    STATUS_ENUM                      Status;
    char                             Alias[STR_LEN_64];
    char                             Name[STR_LEN_64];
    char                             ToneEventProfile[STR_LEN_256];
    APPLICATIONintERFACE_ENUM        Applicationinterface;
    ISDN_BRI_PROTOCOL_ENUM           Protocol;
    ISDN_PROTOCOL_ENUMULATION_ENUM   ProtocolEmulation;
    unsigned char                    PermanentLayer2;
    unsigned char                    PermanentLayer1;
    unsigned char                    LapdDisconnectionTimeout;
    ISDN_TEI_NEGOTIATION_ENUM        TEINegotiation;
    unsigned int                     StaticTEI;
    unsigned char                    LifeLineHold;
    unsigned char                    PowerSourceOne;
    unsigned int                     MaxNumBChannels;
    char                             OutboundOnlyBChannels[STR_LEN_256];
    char                             InboundOnlyBChannels[STR_LEN_256];
    char                             BidirectionalBChannels[STR_LEN_256];
} DML_ISDN_BRI, *PDML_ISDN_BRI;

typedef struct _DML_ISDN_PRI
{
    unsigned long                     uInstanceNumber;
    void*                             pParentVoiceService;
    unsigned char                     Enable;
    STATUS_ENUM                       Status;
    char                              Alias[STR_LEN_64];
    char                              Name[STR_LEN_64];
    char                              ToneEventProfile[STR_LEN_256];
    APPLICATIONintERFACE_ENUM         Applicationinterface;
    ISDN_PRI_PROTOCOL_ENUM            Protocol;
    ISDN_PROTOCOL_ENUMULATION_ENUM    ProtocolEmulation;
    unsigned char                     PermanentLayer2;
    ISDN_LINECODE_ENUM                Linecode;
    ISDN_ESF_ENUM                     ESF;
    ISDN_PHYintERFACETYPE_ENUM        PhysicalinterfaceType;
    unsigned int                      MaxNumBChannels;
    char                              OutboundOnlyBChannels[STR_LEN_256];
    char                              InboundOnlyBChannels[STR_LEN_256];
    char                              BidirectionalBChannels[STR_LEN_256];
    ISDN_CLOCKMODE_ENUM               ClockMode;

} DML_ISDN_PRI, *PDML_ISDN_PRI;

typedef  struct _DML_ISDN_BRI_CTRL_
 {
    DML_ISDN_BRI     dml;
    unsigned char    updated;
 } DML_ISDN_BRI_CTRL_T, *PDML_ISDN_BRI_CTRL_T;

typedef  struct _DML_ISDN_BRI_LIST_
 {
     unsigned int             ulQuantity;
     DML_ISDN_BRI_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_ISDN_BRI_LIST_T,*PDML_ISDN_BRI_LIST_T;

typedef  struct _DML_ISDN_PRI_CTRL_
 {
     DML_ISDN_PRI     dml;
     unsigned char    updated;
 } DML_ISDN_PRI_CTRL_T,*PDML_ISDN_PRI_CTRL_T;

typedef  struct _DML_ISDN_PRI_LIST_
 {
     unsigned int             ulQuantity;
     DML_ISDN_PRI_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_ISDN_PRI_LIST_T,*PDML_ISDN_PRI_LIST_T;

typedef struct _DML_ISDN
{
    DML_ISDN_BRI_LIST_T BRI;
    DML_ISDN_PRI_LIST_T PRI;
} DML_ISDN,*PDML_ISDN;


typedef struct _DML_POTS_FXO_DIAGTESTS
{
    DIAG_STATE_ENUM        DiagnosticsState;
    FXO_TEST_SELECTOR_ENUM TestSelector;
    TEST_RESULT_ENUM       TestResult;
} DML_POTS_FXO_DIAGTESTS,*PDML_POTS_FXO_DIAGTESTS;


typedef struct _DML_POTS_FXO
{
    unsigned long           uInstanceNumber;
    void*                   pParentVoiceService;
    unsigned char           Enable;
    STATUS_ENUM             Status;
    char                    Alias[STR_LEN_64];
    char                    Name[STR_LEN_64];
    char                    ToneEventProfile[STR_LEN_256];
    unsigned char           SecondStepDialing;
    unsigned int            TimeoutBeforeDialing;
    unsigned int            RingingTimeout;
    unsigned int            RingNumber;
    unsigned int            OnHookMinDuration;
    SIGNALING_MODE_ENUM     SignalingMode;
    unsigned int            DTMFDialoutinterval;
    unsigned char           CallerIdDetectionEnable;
    unsigned char           Active;
    DML_POTS_FXO_DIAGTESTS  DiagTests;
} DML_POTS_FXO,*PDML_POTS_FXO;

typedef struct _DML_POTS_FXS_DIAGTESTS
{
    DIAG_STATE_ENUM        DiagnosticsState;
    FXS_TEST_SELECTOR_ENUM TestSelector;
    TEST_RESULT_ENUM       TestResult;
} DML_POTS_FXS_DIAGTESTS,*PDML_POTS_FXS_DIAGTESTS;

typedef struct _DML_POTS_FXS_VOICEPROCESSING
{
    int                TransmitGain;
    int                ReceiveGain;
    unsigned char      EchoCancellationEnable;
    unsigned char      EchoCancellationInUse;
    unsigned int       EchoCancellationTail;
} DML_POTS_FXS_VOICEPROCESSING,*PDML_POTS_FXS_VOICEPROCESSING;

typedef struct _DML_POTS_FXS
{
    unsigned long                 uInstanceNumber;
    void*                         pParentVoiceService;
    unsigned char                 Enable;
    STATUS_ENUM                   Status;
    char                          Alias[STR_LEN_64];
    char                          Name[STR_LEN_64];
    char                          ToneEventProfile[STR_LEN_256];
    PASS_THROUGH_ENUM             FaxPassThrough;
    PASS_THROUGH_ENUM             ModemPassThrough;
    POTS_DIALTYPE_ENUM            DialType;
    unsigned char                 ClipGeneration;
    unsigned char                 chargingPulse;
    unsigned char                 Active;
    TERMINAL_TYPE_ENUM            TerminalType;
    DML_POTS_FXS_VOICEPROCESSING  VoiceProcessing;
    DML_POTS_FXS_DIAGTESTS        DiagTests;
} DML_POTS_FXS,*PDML_POTS_FXS;


typedef  struct  _DML_POTS_FXS_CTRL_
 {
    DML_POTS_FXS     dml;
    unsigned char    updated;
 } DML_POTS_FXS_CTRL_T, *PDML_POTS_FXS_CTRL_T;

typedef  struct _DML_POTS_FXS_LIST_
 {
    unsigned int             ulQuantity;
    DML_POTS_FXS_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_POTS_FXS_LIST_T, *PDML_POTS_FXS_LIST_T;

typedef  struct _DML_POTS_FXO_CTRL_
 {
    DML_POTS_FXO     dml;
    unsigned char    updated;
 } DML_POTS_FXO_CTRL_T, *PDML_POTS_FXO_CTRL_T;

typedef  struct _DML_POTS_FXO_LIST_
 {
    unsigned int             ulQuantity;
    DML_POTS_FXO_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_POTS_FXO_LIST_T, *PDML_POTS_FXO_LIST_T;

typedef  struct _DML_POTS_RINGER_EVT
 {
    unsigned long                 uInstanceNumber;
    void*                         pParentVoiceService;
    char                          Alias[STR_LEN_64];
    FUNCTION_TYPE_ENUM            Function;
    char                          Cadence[STR_LEN_256];
 } DML_POTS_RINGER_EVT,*PDML_POTS_RINGER_EVT;

typedef  struct _DML_POTS_RINGER_EVT_CTRL_
 {
    DML_POTS_RINGER_EVT     dml;
    unsigned char           updated;
 } DML_POTS_RINGER_EVT_CTRL_T, *PDML_POTS_RINGER_EVT_CTRL_T;

typedef  struct _DML_POTS_RINGER_EVT_LIST_
 {
    unsigned int                    ulQuantity;
    DML_POTS_RINGER_EVT_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_POTS_RINGER_EVT_LIST_T, *PDML_POTS_RINGER_EVT_LIST_T;

typedef struct _DML_POTS_RINGER
{
    DML_POTS_RINGER_EVT_LIST_T Event;
} DML_POTS_RINGER,*PDML_POTS_RINGER;

typedef struct _DML_POTS
{
    char                 Region[STR_LEN_2];
    DML_POTS_RINGER      Ringer_Obj;
    DML_POTS_FXO_LIST_T  FXO;
    DML_POTS_FXS_LIST_T  FXS;
} DML_POTS,*PDML_POTS;

typedef struct _DML_DECT_BASE_STATS
{
    unsigned int   Handovers;
    unsigned int   HandoverFailures;
    unsigned int   ControlFieldErrors;
    unsigned int   PayloadFieldErrors;
    unsigned int   SyncFailures;
} DML_DECT_BASE_STATS,*PDML_DECT_BASE_STATS;

typedef struct _DML_DECT_BASE
{
    unsigned long             uInstanceNumber;
    void*                     pParentVoiceService;
    unsigned char             Enable;
    STATUS_ENUM               Status;
    char                      Alias[STR_LEN_64];
    char                      Name[STR_LEN_64];
    char                      ToneEventProfile[STR_LEN_256];
    STANDARD_ENUM             Standard;
    char                      RFPI[STR_LEN_5];
    unsigned int              MaxSupportedPP;
    char                      PIN[STR_LEN_4];
    unsigned char             RepeaterSupportEnabled;
    unsigned char             NEMOEnable;
    unsigned char             SubscriptionEnable;
    unsigned char             CipheringEnable;
    ENCRYPTION_TYPE_ENUM      EncryptionType;
    RF_POWER_CTRL_ENUM        RFPowerControl;
    char                      FirmwareVersion[STR_LEN_20];
    char                      EepromVersion[STR_LEN_20];
    char                      HardwareVersion[STR_LEN_20];
    DML_DECT_BASE_STATS       Stats;
} DML_DECT_BASE,*PDML_DECT_BASE;

typedef struct _DML_DECT_PORTABLE
{
    unsigned long               uInstanceNumber;
    void*                       pParentVoiceService;
    unsigned char               Enable;
    STATUS_ENUM                 Status;
    char                        Alias[STR_LEN_64];
    char                        CodecList[STR_LEN_256];
    REGISTRATION_STATUS_ENUM    RegistrationStatus;
    char                        IPUI[STR_LEN_13];
    unsigned int                IPUILength;
    char                        IPEI[STR_LEN_5];
    char                        PARK[STR_LEN_5];
    char                        BaseAttachedTo[STR_LEN_256];
    PORTABLE_TYPE_ENUM          PortableType;
    char                        SubscriptionTime[STR_LEN_24];
    CONTROL_ENUM                Control;
    char                        HardwareVersion[STR_LEN_20];
    char                        SoftwareVersion[STR_LEN_20];
    unsigned char               SoftwareUpgrade;
    char                        LastUpdateDateTime[STR_LEN_24];
    char                        OperatorName[STR_LEN_32];
} DML_DECT_PORTABLE,*PDML_DECT_PORTABLE;

typedef  struct _DML_DECT_BASE_CTRL_
 {
    DML_DECT_BASE       dml;
    unsigned char       updated;
 } DML_DECT_BASE_CTRL_T, *PDML_DECT_BASE_CTRL_T;

typedef  struct _DML_DECT_BASE_LIST_
 {
    unsigned int                ulQuantity;
    DML_DECT_BASE_CTRL_T*       pdata[TELCOVOICE_DATA_MAX];
 } DML_DECT_BASE_LIST_T, *PDML_DECT_BASE_LIST_T;

typedef  struct _DML_DECT_PORTABLE_CTRL_
 {
    DML_DECT_PORTABLE      dml;
    unsigned char          updated;
 } DML_DECT_PORTABLE_CTRL_T, *PDML_DECT_PORTABLE_CTRL_T;

typedef  struct _DML_DECT_PORTABLE_LIST_
 {
    unsigned int                    ulQuantity;
    DML_DECT_PORTABLE_CTRL_T*       pdata[TELCOVOICE_DATA_MAX];
 } DML_DECT_PORTABLE_LIST_T, *PDML_DECT_PORTABLE_LIST_T;

typedef struct _DML_DECT
{
    DML_DECT_BASE_LIST_T        Base;
    DML_DECT_PORTABLE_LIST_T    Portable;
} DML_DECT,*PDML_DECT;

typedef struct _DML_SIP_CLIENT_CONTACT
{
    unsigned long                   uInstanceNumber;
    void*                           pParentVoiceService;
    void*                           pParentSipClient;
    unsigned char                   Enable;
    SIP_STATUS_ENUM                 Status;
    char                            Alias[STR_LEN_64];
    ORIGIN_ENUM                     Origin;
    char                            IPAddress[STR_LEN_45];
    unsigned int                    Port;
    char                            ContactURI[STR_LEN_256];
    char                            ExpireTime[STR_LEN_24];
    unsigned int                    Pinginterval;
    char                            UserAgent[STR_LEN_256];
} DML_SIP_CLIENT_CONTACT, *PDML_SIP_CLIENT_CONTACT;

typedef struct _DML_SIP_CLIENT_SIPEVENT
{
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentSipClient;
    unsigned char   Enable;
    char            Alias[STR_LEN_64];
    char            Event[STR_LEN_32];
    char            AuthUserName[STR_LEN_128];
    char            AuthPassword[STR_LEN_128];
} DML_SIP_CLIENT_SIPEVENTSUB, *PDML_SIP_CLIENT_SIPEVENTSUB;

typedef  struct _DML_SIP_CLIENT_CONTACT_CTRL_
 {
    DML_SIP_CLIENT_CONTACT      dml;
    unsigned char               updated;
 } DML_SIP_CLIENT_CONTACT_CTRL_T, *PDML_SIP_CLIENT_CONTACT_CTRL_T;

typedef  struct _DML_SIP_CLIENT_CONTACT_LIST_
 {
    unsigned int                        ulQuantity;
    DML_SIP_CLIENT_CONTACT_CTRL_T*      pdata[TELCOVOICE_DATA_MAX];
 }  DML_SIP_CLIENT_CONTACT_LIST_T, *PDML_SIP_CLIENT_CONTACT_LIST_T;

typedef  struct _DML_SIP_CLIENT_SIPEVENTSUB_CTRL_
 {
    DML_SIP_CLIENT_SIPEVENTSUB      dml;
    unsigned char                   updated;
 } DML_SIP_CLIENT_SIPEVENTSUB_CTRL_T, *PDML_SIP_CLIENT_SIPEVENTSUB_CTRL_T;

typedef  struct _DML_SIP_CLIENT_SIPEVENTSUB_LIST_
 {
    unsigned int                            ulQuantity;
    DML_SIP_CLIENT_SIPEVENTSUB_CTRL_T*      pdata[TELCOVOICE_DATA_MAX];
 } DML_SIP_CLIENT_SIPEVENTSUB_LIST_T, *PDML_SIP_CLIENT_SIPEVENTSUB_LIST_T;

typedef  struct _DML_SIP_CLIENT
 {
    unsigned long                     uInstanceNumber;
    void*                             pParentVoiceService;
    unsigned char                     Enable;
    unsigned char                     QuiescentMode;
    CLIENT_STATUS_ENUM                Status;
    char                              Alias[STR_LEN_64];
    ORIGIN_ENUM                       Origin;
    REGISTER_MODE_ENUM                RegisterMode;
    char                              AuthUserName[STR_LEN_128];
    char                              AuthPassword[STR_LEN_128];
    char                              Network[STR_LEN_256];
    unsigned int                      MaxSessions;
    char                              RegisterURI[STR_LEN_389];
    unsigned char                     E164Format;
    unsigned char                     T38Enable;
    DML_SIP_CLIENT_CONTACT_LIST_T     Contact;
    DML_SIP_CLIENT_SIPEVENTSUB_LIST_T SIPEventSub;
 } DML_SIP_CLIENT,*PDML_SIP_CLIENT;

typedef struct _SIP_NETWORK_FQDNSERVER
{
    unsigned long           uInstanceNumber;
    void*                   pParentVoiceService;
    void*                   pParentSipNetwork;
    unsigned char           Enable;
    char                    Alias[STR_LEN_64];
    ORIGIN_ENUM             Origin;
    char                    Domain[STR_LEN_256];
    unsigned int            Weight;
    unsigned int            Priority;
    unsigned int            Port;
    char IPAddresses[STR_LEN_256];
} DML_SIP_NETWORK_FQDNSERVER,*PDML_SIP_NETWORK_FQDNSERVER;


typedef struct _SIP_NETWORK_EVENTSUBSCRIBE
{
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentSipNetwork;
    unsigned char   Enable;
    char            Alias[STR_LEN_64];
    char            Event[STR_LEN_32];
    char            Notifier[STR_LEN_256];
    unsigned int    NotifierPort;
    TRANSPORT_ENUM  NotifierTransport;
    unsigned int    ExpireTime;
} DML_SIP_NETWORK_EVENTSUBSCRIBE,*PDML_SIP_NETWORK_EVENTSUBSCRIBE;

typedef struct _SIP_NETWORK_RESPMAP
{
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentSipNetwork;
    char            Alias[STR_LEN_64];
    unsigned int    SIPResponseNumber;
    unsigned char   Enable;
    char            TextMessage[STR_LEN_64];
    char            Tone[STR_LEN_256];
} DML_SIP_NETWORK_RESPMAP,*PDML_SIP_NETWORK_RESPMAP;

typedef  struct _DML_SIP_NETWORK_FQDNSERVER_CTRL_
 {
    DML_SIP_NETWORK_FQDNSERVER      dml;
    unsigned char                   updated;
 } DML_SIP_NETWORK_FQDNSERVER_CTRL_T, *PDML_SIP_NETWORK_FQDNSERVER_CTRL_T;

typedef  struct _DML_SIP_NETWORK_FQDNSERVER_LIST_
 {
    unsigned int                            ulQuantity;
    DML_SIP_NETWORK_FQDNSERVER_CTRL_T*      pdata[TELCOVOICE_DATA_MAX];
 } DML_SIP_NETWORK_FQDNSERVER_LIST_T, *PDML_SIP_NETWORK_FQDNSERVER_LIST_T;

typedef  struct _DML_SIP_NETWORK_EVENTSUBSCRIBE_CTRL_
 {
    DML_SIP_NETWORK_EVENTSUBSCRIBE     dml;
    unsigned char                      updated;
 } DML_SIP_NETWORK_EVENTSUBSCRIBE_CTRL_T, *PDML_SIP_NETWORK_EVENTSUBSCRIBE_CTRL_T;

typedef  struct _DML_SIP_NETWORK_EVENTSUBSCRIBE_LIST_
 {
    unsigned int                                ulQuantity;
    DML_SIP_NETWORK_EVENTSUBSCRIBE_CTRL_T*      pdata[TELCOVOICE_DATA_MAX];
 } DML_SIP_NETWORK_EVENTSUBSCRIBE_LIST_T, *PDML_SIP_NETWORK_EVENTSUBSCRIBE_LIST_T;

typedef  struct _DML_SIP_NETWORK_RESPMAP_CTRL_
 {
    DML_SIP_NETWORK_RESPMAP     dml;
    unsigned char               updated;
 } DML_SIP_NETWORK_RESPMAP_CTRL_T, *PDML_SIP_NETWORK_RESPMAP_CTRL_T;

typedef  struct _DML_SIP_NETWORK_RESPMAP_LIST_
 {
    unsigned int                        ulQuantity;
    DML_SIP_NETWORK_RESPMAP_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_SIP_NETWORK_RESPMAP_LIST_T, *PDML_SIP_NETWORK_RESPMAP_LIST_T;

typedef enum _PRECEDENCE_ENUM
{
    PRECEDENCE_STATIC,
    PRECEDENCE_DHCP
} PRECEDENCE_ENUM;

typedef enum _INBOUNDAUTH_ENUM
{
    INBOUNDAUTH_NONE,
    INBOUNDAUTH_DIGEST,
    INBOUNDAUTH_SOURCEFILTER
}INBOUNDAUTH_ENUM;

typedef  struct _DML_SIP_NETWORK
 {
    unsigned long                           uInstanceNumber;
    void*                                   pParentVoiceService;
    unsigned char                           Enable;
    unsigned char                           QuiescentMode;
    NETWORK_STATUS_ENUM                     Status;
    char                                    Alias[STR_LEN_64];
    char                                    X_RDK_Firewall_Rule_Data[STR_LEN_256];
    char                                    ProxyServer[STR_LEN_256];
    unsigned int                            ProxyServerPort;
    TRANSPORT_ENUM                          ProxyServerTransport;
    char                                    RegistrarServer[STR_LEN_256];
    unsigned int                            RegistrarServerPort;
    TRANSPORT_ENUM                          RegistrarServerTransport;
    char                                    ServerDomain[STR_LEN_256];
    char                                    ChosenDomain[STR_LEN_256];
    char                                    ChosenIPAddress[STR_LEN_45];
    unsigned int                            ChosenPort;
    char                                    UserAgentDomain[STR_LEN_256];
    unsigned int                            UserAgentPort;
    TRANSPORT_ENUM                          UserAgentTransport;
    char                                    OutboundProxy[STR_LEN_256];
    char                                    OutboundProxyResolvedAddress[STR_LEN_45];
    PRECEDENCE_ENUM                         OutboundProxyPrecedence;
    unsigned int                            OutboundProxyPort;
    unsigned char                           STUNEnable;
    char                                    STUNServer[STR_LEN_256];
    unsigned int                            NonVoiceBandwidthReservedUpstream;
    unsigned int                            NonVoiceBandwidthReservedDownstream;
    char                                    Organization[STR_LEN_256];
    unsigned int                            RegistrationPeriod;
    char                                    Realm[STR_LEN_256];
    unsigned int                            TimerT1;
    unsigned int                            TimerT2;
    unsigned int                            TimerT4;
    unsigned int                            TimerA;
    unsigned int                            TimerB;
    unsigned int                            TimerC;
    unsigned int                            TimerD;
    unsigned int                            TimerE;
    unsigned int                            TimerF;
    unsigned int                            TimerG;
    unsigned int                            TimerH;
    unsigned int                            TimerI;
    unsigned int                            TimerJ;
    unsigned int                            TimerK;
    unsigned int                            InviteExpires;
    unsigned int                            ReInviteExpires;
    unsigned int                            RegisterExpires;
    unsigned int                            RegisterRetryinterval;
    INBOUNDAUTH_ENUM                        InboundAuth;
    char                                    InboundAuthUsername[STR_LEN_256];
    char                                    InboundAuthPassword[STR_LEN_256];
    unsigned char                           UseCodecPriorityInSDPResponse;
    unsigned int                            DSCPMark;
    int                                     VLANIDMark;
    int                                     EthernetPriorityMark;
    char                                    ConferenceCallDomainURI[STR_LEN_256];
    unsigned int                            TimerLoginRejected;
    unsigned char                           NoLoginRetry;
    unsigned int                            TimerRegistrationFailed;
    unsigned int                            TimerSubscriptionFailed;
    unsigned int                            UnansweredRegistrationAttempts;
    char                                    VoIPProfile[STR_LEN_256];
    char                                    CodecList[STR_LEN_256];
    unsigned int                            MaxSessions;
    unsigned int                            X_RDK_SKBMark;
    unsigned char                           X_RDK_Central_COM_NetworkDisconnect;
    char                                    X_RDK_Central_COM_ConferencingURI[STR_LEN_256];
    unsigned char                           X_RDK_PRACKRequired;
    DML_SIP_NETWORK_FQDNSERVER_LIST_T       FQDNServer;
    DML_SIP_NETWORK_EVENTSUBSCRIBE_LIST_T   EventSubscribe;
    DML_SIP_NETWORK_RESPMAP_LIST_T          ResponseMap;
 } DML_SIP_NETWORK, *PDML_SIP_NETWORK;

typedef  struct _DML_SIP_NETWORK_CTRL_
 {
    DML_SIP_NETWORK     dml;
    unsigned char       updated;
 } DML_SIP_NETWORK_CTRL_T, *PDML_SIP_NETWORK_CTRL_T;

typedef  struct _DML_SIP_NETWORK_LIST_
 {
    unsigned int                ulQuantity;
    DML_SIP_NETWORK_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_SIP_NETWORK_LIST_T, *PDML_SIP_NETWORK_LIST_T;

typedef  struct _DML_SIP_CLIENT_CTRL_
 {
    DML_SIP_CLIENT      dml;
    unsigned char       updated;
 } DML_SIP_CLIENT_CTRL_T,*PDML_SIP_CLIENT_CTRL_T;

typedef  struct _DML_SIP_CLIENT_LIST_
 {
    unsigned int               ulQuantity;
    DML_SIP_CLIENT_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_SIP_CLIENT_LIST_T, *PDML_SIP_CLIENT_LIST_T;

typedef struct _DML_SIP_PROXY
{
    unsigned long       uInstanceNumber;
    void*               pParentVoiceService;
    unsigned char       Enable;
    SIP_STATUS_ENUM     Status;
    char                Alias[STR_LEN_64];
    ORIGIN_ENUM         Origin;
    char                ProxyIPAddress[STR_LEN_45];
    unsigned int        ProxyPort;
    char                ContactURI[STR_LEN_256];
    char                VoIPProfile[STR_LEN_256];
} DML_SIP_PROXY, *PDML_SIP_PROXY;

typedef  struct _DML_SIP_PROXY_CTRL_
 {
    DML_SIP_PROXY       dml;
    unsigned char       updated;
 } DML_SIP_PROXY_CTRL_T, *PDML_SIP_PROXY_CTRL_T;

typedef  struct _DML_SIP_PROXY_LIST_
 {
    unsigned int              ulQuantity;
    DML_SIP_PROXY_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_SIP_PROXY_LIST_T, *PDML_SIP_PROXY_LIST_T;

typedef  struct _DML_SIP_REGISTRAR_ACCOUNT_CONTACT
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentSipRegistrar;
    void*           pParentSipRegistrarAccount;
    unsigned char   Enable;
    SIP_STATUS_ENUM Status;
    char            Alias[STR_LEN_64];
    ORIGIN_ENUM     Origin;
    char            IPAddress[STR_LEN_45];
    unsigned int    Port;
    char            ContactURI[STR_LEN_256];
    char            ExpireTime[STR_LEN_24];
    char            UserAgent[STR_LEN_64];
 } DML_SIP_REGISTRAR_ACCOUNT_CONTACT,*PDML_SIP_REGISTRAR_ACCOUNT_CONTACT;

typedef  struct _DML_SIP_REGISTRAR_ACCOUNT_CONTACT_CTRL_
 {
    DML_SIP_REGISTRAR_ACCOUNT_CONTACT       dml;
    unsigned char                           updated;
 } DML_SIP_REGISTRAR_ACCOUNT_CONTACT_CTRL_T, *PDML_SIP_REGISTRAR_ACCOUNT_CONTACT_CTRL_T;

typedef  struct _DML_SIP_REGISTRAR_ACCOUNT_CONTACT_LIST_
 {
    unsigned int                                    ulQuantity;
    DML_SIP_REGISTRAR_ACCOUNT_CONTACT_CTRL_T*       pdata[TELCOVOICE_DATA_MAX];
 } DML_SIP_REGISTRAR_ACCOUNT_CONTACT_LIST_T, *PDML_SIP_REGISTRAR_ACCOUNT_CONTACT_LIST_T;

typedef  struct _DML_SIP_REGISTRAR_ACCOUNT
 {
    unsigned long                               uInstanceNumber;
    void*                                       pParentVoiceService;
    void*                                       pParentSipRegistrar;
    SIP_REGISTRAR_ACC_ENABLE_ENUM               Enable;
    unsigned char                               QuiescentMode;
    CLIENT_STATUS_ENUM                          Status;
    char                                        Alias[STR_LEN_64];
    ORIGIN_ENUM                                 Origin;
    CALLSTATUS_ENUM                             CallStatus;
    char                                        AuthUserName[STR_LEN_128];
    char                                        AuthPassword[STR_LEN_128];
    ACC_REGISTRATION_STATUS_ENUM                RegistrationStatus;
    char                                        URI[STR_LEN_389];
    char                                        Domain[STR_LEN_256];
    char                                        CodecList[STR_LEN_256];
    char                                        VoIPProfile[STR_LEN_256];
    DML_SIP_REGISTRAR_ACCOUNT_CONTACT_LIST_T    Contact;
 } DML_SIP_REGISTRAR_ACCOUNT,*PDML_SIP_REGISTRAR_ACCOUNT;

typedef  struct _DML_SIP_REGISTRAR_ACCOUNT_CTRL_
 {
    DML_SIP_REGISTRAR_ACCOUNT       dml;
    unsigned char                   updated;
 } DML_SIP_REGISTRAR_ACCOUNT_CTRL_T, *PDML_SIP_REGISTRAR_ACCOUNT_CTRL_T;

typedef  struct _DML_SIP_REGISTRAR_ACCOUNT_LIST_
 {
    unsigned int                            ulQuantity;
    DML_SIP_REGISTRAR_ACCOUNT_CTRL_T*       pdata[TELCOVOICE_DATA_MAX];
 } DML_SIP_REGISTRAR_ACCOUNT_LIST_T, *PDML_SIP_REGISTRAR_ACCOUNT_LIST_T;

typedef struct _DML_SIP_REGISTRAR
{
    unsigned long                       uInstanceNumber;
    void*                               pParentVoiceService;
    unsigned char                       Enable;
    unsigned char                       QuiescentMode;
    SIP_STATUS_ENUM                     Status;
    char                                Alias[STR_LEN_64];
    ORIGIN_ENUM                         Origin;
    char                                RegistrarIPAddress[STR_LEN_45];
    unsigned int                        RegistrarPort;
    unsigned int                        RegisterExpires;
    unsigned int                        Pinginterval;
    char                                Organization[STR_LEN_256];
    char                                Realm[STR_LEN_256];
    char                                VoIPProfile[STR_LEN_256];
    char                                ContactURI[STR_LEN_256];
    DML_SIP_REGISTRAR_ACCOUNT_LIST_T    Account;
} DML_SIP_REGISTRAR, *PDML_SIP_REGISTRAR;

typedef  struct _DML_SIP_REGISTRAR_CTRL_
 {
    DML_SIP_REGISTRAR       dml;
    unsigned char           updated;
 } DML_SIP_REGISTRAR_CTRL_T, *PDML_SIP_REGISTRAR_CTRL_T;

typedef  struct _DML_SIP_REGISTRAR_LIST_
 {
    unsigned int                  ulQuantity;
    DML_SIP_REGISTRAR_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_SIP_REGISTRAR_LIST_T, *PDML_SIP_REGISTRAR_LIST_T;

typedef struct _DML_SIP
{
    DML_SIP_NETWORK_LIST_T      Network;
    DML_SIP_CLIENT_LIST_T       Client;
    DML_SIP_PROXY_LIST_T        Proxy;
    DML_SIP_REGISTRAR_LIST_T    Registrar;
} DML_SIP,*PDML_SIP;

typedef  struct _DML_MGCP_CLIENT
 {
    unsigned long           uInstanceNumber;
    void*                   pParentVoiceService;
    unsigned char           Enable;
    unsigned char           QuiescentMode;
    CLIENT_STATUS_ENUM      Status;
    char                    Alias[STR_LEN_64];
    MGCP_REGISTER_MODE_ENUM RegisterMode;
    unsigned int            LocalPort;
    char                    Domain[STR_LEN_256];
    char                    User[STR_LEN_64];
    char                    Network[STR_LEN_256];
    unsigned int                    MaxSessions;
 } DML_MGCP_CLIENT,*PDML_MGCP_CLIENT;

typedef  struct _DML_MGCP_CLIENT_CTRL_
 {
    DML_MGCP_CLIENT             dml;
    unsigned char               updated;
 } DML_MGCP_CLIENT_CTRL_T, *PDML_MGCP_CLIENT_CTRL_T;

typedef  struct _DML_MGCP_CLIENT_LIST_
 {
    unsigned int               ulQuantity;
    DML_MGCP_CLIENT_CTRL_T*    pdata[TELCOVOICE_DATA_MAX];
 } DML_MGCP_CLIENT_LIST_T, *PDML_MGCP_CLIENT_LIST_T;

typedef  struct _DML_MGCP_NETWORK
 {
    unsigned long                   uInstanceNumber;
    void*                           pParentVoiceService;
    unsigned char                   Enable;
    unsigned char                   QuiescentMode;
    MGCP_NETWORK_REG_STATUS_ENUM    Status;
    char                            Alias[STR_LEN_64];
    char                            CallAgent1[STR_LEN_256];
    unsigned int                    CallAgentPort1;
    char                            CallAgent2[STR_LEN_256];
    unsigned int                    CallAgentPort2;
    unsigned int                    RetranintervalTimer;
    unsigned int                    MaxRetranCount;
    unsigned int                    DSCPMark;
    int                             VLANIDMark;
    int                             EthernetPriorityMark;
    unsigned char                   AllowPiggybackEvents;
    unsigned char                   SendRSIPImmediately;
    unsigned char                   STUNEnable;
    char                            STUNServer[STR_LEN_256];
    unsigned int                    NonVoiceBandwidthReservedUpstream;
    unsigned int                    NonVoiceBandwidthReservedDownstream;
    unsigned int                    MaxSessions;
    char                            VoIPProfile[STR_LEN_256];
    char                            CodecList[STR_LEN_256];
 } DML_MGCP_NETWORK,*PDML_MGCP_NETWORK;

typedef  struct _DML_MGCP_NETWORK_CTRL_
 {
    DML_MGCP_NETWORK            dml;
    unsigned char               updated;
 } DML_MGCP_NETWORK_CTRL_T, *PDML_MGCP_NETWORK_CTRL_T;

typedef  struct _DML_MGCP_NETWORK_LIST_
 {
    unsigned int                 ulQuantity;
    DML_MGCP_NETWORK_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_MGCP_NETWORK_LIST_T, *PDML_MGCP_NETWORK_LIST_T;

typedef struct _DML_MGCP
{
    DML_MGCP_CLIENT_LIST_T      Client;
    DML_MGCP_NETWORK_LIST_T     Network;
} DML_MGCP,*PDML_MGCP;

typedef  struct _DML_H323_CLIENT
 {
    unsigned long       uInstanceNumber;
    void*               pParentVoiceService;
    unsigned char       Enable;
    unsigned char       QuiescentMode;
    CLIENT_STATUS_ENUM  Status;
    char                Alias[STR_LEN_256];
    unsigned char       H235Authentication;
    char                AuthPassword[STR_LEN_128];
    char                SendersID[STR_LEN_256];
    char                Network[STR_LEN_256];
    char                H323ID[STR_LEN_32];
    unsigned int        MaxSessions;
 } DML_H323_CLIENT,*PDML_H323_CLIENT;

typedef  struct _DML_H323_CLIENT_CTRL_
 {
    DML_H323_CLIENT     dml;
    unsigned char       updated;
 } DML_H323_CLIENT_CTRL_T, *PDML_H323_CLIENT_CTRL_T;

typedef  struct _DML_H323_CLIENT_LIST_
 {
    unsigned int                ulQuantity;
    DML_H323_CLIENT_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_H323_CLIENT_LIST_T, *PDML_H323_CLIENT_LIST_T;

typedef  struct _DML_H323_NETWORK
 {
    unsigned long           uInstanceNumber;
    void*                   pParentVoiceService;
    unsigned char           Enable;
    unsigned char           QuiescentMode;
    NETWORK_STATUS_ENUM     Status;
    char                    Alias[STR_LEN_256];
    char                    Gatekeeper[STR_LEN_256];
    unsigned int            GatekeeperPort;
    char                    GatekeeperID[STR_LEN_256];
    unsigned int            TimeToLive;
    unsigned int            DSCPMark;
    int                     VLANIDMark;
    int                     EthernetPriorityMark;
    unsigned char           STUNEnable;
    char                    STUNServer[STR_LEN_256];
    unsigned int            NonVoiceBandwidthReservedUpstream;
    unsigned int            NonVoiceBandwidthReservedDownstream;
    unsigned int            MaxSessions;
    char                    VoIPProfile[STR_LEN_256];
    char                    CodecList[STR_LEN_256];
 } DML_H323_NETWORK,*PDML_H323_NETWORK;

typedef  struct _DML_H323_NETWORK_CTRL_
 {
    DML_H323_NETWORK     dml;
    unsigned char        updated;
 } DML_H323_NETWORK_CTRL_T, *PDML_H323_NETWORK_CTRL_T;

typedef  struct _DML_H323_NETWORK_LIST_
 {
    unsigned int                 ulQuantity;
    DML_H323_NETWORK_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_H323_NETWORK_LIST_T, *PDML_H323_NETWORK_LIST_T;

typedef struct _DML_H323
{
    DML_H323_CLIENT_LIST_T      Client;
    DML_H323_NETWORK_LIST_T     Network;
} DML_H323,*PDML_H323;

typedef enum _LINE_ORIGIN_ENUM
{
    LINE_ORIGIN_STATIC,
    LINE_ORIGIN_DDI_RANGE
} LINE_ORIGIN_ENUM;

typedef struct _DML_TRUNK
{
   unsigned long           uInstanceNumber;
   void*                   pParentVoiceService;
   unsigned char           Enable;
   unsigned char           QuiescentMode;
   TRUNK_STATUS_ENUM       Status;
   char                    Alias[STR_LEN_64];
   ORIGIN_ENUM             Origin;
   char                    Name[STR_LEN_16];
   char                    DDIRange[STR_LEN_256];
   unsigned char           LineObjectCreation;
   unsigned int            MaxChannels;
   int                     MaxOutboundChannelCount;
   int                     MaxInboundChannelCount;
   CODECPRIORITY_ENUM      CodecPriority;
   char                    Provider[STR_LEN_256];
} DML_TRUNK,*PDML_TRUNK;


typedef  struct _DML_TRUNK_CTRL_
 {
    DML_TRUNK                   dml;
    unsigned char               updated;
 } DML_TRUNK_CTRL_T, *PDML_TRUNK_CTRL_T;

typedef  struct _DML_TRUNK_LIST_
 {
    unsigned int                 ulQuantity;
    DML_TRUNK_CTRL_T*            pdata[TELCOVOICE_DATA_MAX];
 } DML_TRUNK_LIST_T, *PDML_TRUNK_LIST_T;

typedef enum _GROUP_RINGTYPE_ENUM
{
    GROUP_RINGTYPE_SIMULTANEOUS,
    GROUP_RINGTYPE_HIERARCHICAL,
    GROUP_RINGTYPE_CYCLIC
} GROUP_RINGTYPE_ENUM;

typedef  struct _DML_CALLCONTROL_GROUP
 {
    unsigned long           uInstanceNumber;
    void*                   pParentVoiceService;
    char                    Alias[STR_LEN_64];
    char                    Extensions[STR_LEN_256];
    GROUP_RINGTYPE_ENUM     RingType;
    unsigned int            RingTimeout;
 } DML_CALLCONTROL_GROUP,*PDML_CALLCONTROL_GROUP;

typedef  struct _DML_CALLCONTROL_GROUP_CTRL_
 {
    DML_CALLCONTROL_GROUP       dml;
    unsigned char               updated;
 } DML_CALLCONTROL_GROUP_CTRL_T, *PDML_CALLCONTROL_GROUP_CTRL_T;

typedef  struct _DML_CALLCONTROL_GROUP_LIST_
 {
    unsigned int                      ulQuantity;
    DML_CALLCONTROL_GROUP_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_GROUP_LIST_T, *PDML_CALLCONTROL_GROUP_LIST_T;

typedef  struct _DML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO
 {
    unsigned long       uInstanceNumber;
    void*               pParentVoiceService;
    void*               pParentCallCtrlNumPlan;
    char                Alias[STR_LEN_64];
    unsigned char       Enable;
    char                PrefixRange[STR_LEN_42];
    unsigned int        PrefixMinNumberOfDigits;
    unsigned int        PrefixMaxNumberOfDigits;
    unsigned int        NumberOfDigitsToRemove;
    unsigned int        PosOfDigitsToRemove;
    char                DialTone[STR_LEN_256];
    char                FacilityAction[STR_LEN_64];
    char                FacilityActionArgument[STR_LEN_256];
 } DML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO,*PDML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO;

typedef  struct _DML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO_CTRL
 {
    DML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO    dml;
    unsigned char                               updated;
 } DML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO_CTRL_T, *PDML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO_CTRL_T;

typedef  struct _DML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO_LIST_
 {
    unsigned int                                        ulQuantity;
    DML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO_CTRL_T*    pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO_LIST_T, *PDML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO_LIST_T;

typedef  struct _DML_CALLCONTROL_NUMBERINGPLAN
 {
    unsigned long                                       uInstanceNumber;
    void*                                               pParentVoiceService;
    char                                                Alias[STR_LEN_64];
    unsigned int                                        MinimumNumberOfDigits;
    unsigned int                                        MaximumNumberOfDigits;
    unsigned int                                        interDigitTimerStd;
    unsigned int                                        interDigitTimerOpen;
    char                                                TerminationDigit;
    char                                                InvalidNumberTone[STR_LEN_256];
    unsigned int                                        PrefixInfoMaxEntries;
    DML_CALLCONTROL_NUMBERINGPLAN_PREFIXINFO_LIST_T     PrefixInfo;
 } DML_CALLCONTROL_NUMBERINGPLAN,*PDML_CALLCONTROL_NUMBERINGPLAN;

typedef  struct _DML_CALLCONTROL_NUMBERINGPLAN_CTRL_
 {
    DML_CALLCONTROL_NUMBERINGPLAN       dml;
    unsigned char                       updated;
 } DML_CALLCONTROL_NUMBERINGPLAN_CTRL_T, *PDML_CALLCONTROL_NUMBERINGPLAN_CTRL_T;

typedef  struct _DML_CALLCONTROL_NUMBERINGPLAN_LIST_
 {
    unsigned int                            ulQuantity;
    DML_CALLCONTROL_NUMBERINGPLAN_CTRL_T*   pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_NUMBERINGPLAN_LIST_T, *PDML_CALLCONTROL_NUMBERINGPLAN_LIST_T;

typedef  struct _DML_CALLCONTROL_OUTGOINGMAP
 {
    unsigned long       uInstanceNumber;
    void*               pParentVoiceService;
    unsigned char       Enable;
    char                Alias[STR_LEN_64];
    char                CLIPNoScreeningNumber[STR_LEN_32];
    char                Extension[STR_LEN_256];
    char                Line[STR_LEN_256];
    unsigned int        Order;
 } DML_CALLCONTROL_OUTGOINGMAP,*PDML_CALLCONTROL_OUTGOINGMAP;

typedef  struct _DML_CALLCONTROL_OUTGOINGMAP_CTRL_
 {
    DML_CALLCONTROL_OUTGOINGMAP     dml;
    unsigned char                   updated;
 } DML_CALLCONTROL_OUTGOINGMAP_CTRL_T, *PDML_CALLCONTROL_OUTGOINGMAP_CTRL_T;

typedef  struct _DML_CALLCONTROL_OUTGOINGMAP_LIST_
 {
    unsigned int                            ulQuantity;
    DML_CALLCONTROL_OUTGOINGMAP_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_OUTGOINGMAP_LIST_T, *PDML_CALLCONTROL_OUTGOINGMAP_LIST_T;

typedef  struct _DML_CALLCONTROL_INCOMINGMAP
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    unsigned char   Enable;
    char            Alias[STR_LEN_64];
    char            Line[STR_LEN_256];
    char            Extension[STR_LEN_256];
    unsigned int    Order;
    unsigned int    Timeout;
 } DML_CALLCONTROL_INCOMINGMAP,*PDML_CALLCONTROL_INCOMINGMAP;

typedef  struct _DML_CALLCONTROL_INCOMINGMAP_CTRL_
 {
    DML_CALLCONTROL_INCOMINGMAP     dml;
    unsigned char                   updated;
 } DML_CALLCONTROL_INCOMINGMAP_CTRL_T, *PDML_CALLCONTROL_INCOMINGMAP_CTRL_T;

typedef  struct _DML_CALLCONTROL_INCOMINGMAP_LIST_
 {
    unsigned int                            ulQuantity;
    DML_CALLCONTROL_INCOMINGMAP_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_INCOMINGMAP_LIST_T, *PDML_CALLCONTROL_INCOMINGMAP_LIST_T;

typedef enum _SMTP_AUTH_TYPE_ENUM
 {
    SMTP_AUTH_NONE,
    SMTP_AUTH_SSL,
    SMTP_AUTH_TLS,
    SMTP_AUTH_AUTO
 } SMTP_AUTH_TYPE_ENUM;

typedef  struct _DML_CALLCONTROL_MAILBOX
 {
    unsigned long           uInstanceNumber;
    void*                   pParentVoiceService;
    unsigned char           Enable;
    char                    Alias[STR_LEN_64];
    unsigned int            MaxMsg;
    unsigned int            MaxMessageTime;
    unsigned int            MinSize;
    char                    SMTPServerAddress[STR_LEN_256];
    unsigned int            SMTPServerPort;
    char                    SMTPUser[STR_LEN_256];
    char                    SMTPPassword[STR_LEN_256];
    SMTP_AUTH_TYPE_ENUM     SMTPAuthenticationType;
    char                    SMTPFrom[STR_LEN_256];
 } DML_CALLCONTROL_MAILBOX,*PDML_CALLCONTROL_MAILBOX;

typedef  struct _DML_CALLCONTROL_MAILBOX_CTRL_
 {
    DML_CALLCONTROL_MAILBOX     dml;
    unsigned char               updated;
 } DML_CALLCONTROL_MAILBOX_CTRL_T, *PDML_CALLCONTROL_MAILBOX_CTRL_T;

typedef  struct _DML_CALLCONTROL_MAILBOX_LIST_
 {
    unsigned int                        ulQuantity;
    DML_CALLCONTROL_MAILBOX_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_MAILBOX_LIST_T, *PDML_CALLCONTROL_MAILBOX_LIST_T;

typedef  struct _DML_CALLCONTROL_STATS_DSP
 {
    unsigned int    Overruns;
    unsigned int    Underruns;
 } DML_CALLCONTROL_STATS_DSP,*PDML_CALLCONTROL_STATS_DSP;

typedef  struct _DML_CALLCONTROL_STATS_INCALLS
 {
    unsigned int    CallsReceived;
    unsigned int    CallsConnected;
    unsigned int    CallsFailed;
    unsigned int    CallsDropped;
    unsigned int    TotalCallTime;
 } DML_CALLCONTROL_STATS_INCALLS,*PDML_CALLCONTROL_STATS_INCALLS;

typedef  struct _DML_CALLCONTROL_STATS_OUTCALLS
 {
    unsigned int    CallsAttempted;
    unsigned int    CallsConnected;
    unsigned int    CallsFailed;
    unsigned int    CallsDropped;
    unsigned int    TotalCallTime;
 }  DML_CALLCONTROL_STATS_OUTCALLS,*PDML_CALLCONTROL_STATS_OUTCALLS;

typedef  struct _DML_CALLCONTROL_STATS_RTP
 {
    unsigned int    PacketsReceived;
    unsigned int    PacketsSent;
    unsigned int    PacketsLost;
    unsigned int    BytesSent;
    unsigned int    BytesReceived;
 } DML_CALLCONTROL_STATS_RTP,*PDML_CALLCONTROL_STATS_RTP;

typedef  struct _DML_CALLCONTROL_EXTENSION_STATS
 {
    DML_CALLCONTROL_STATS_INCALLS   IncomingCalls;
    DML_CALLCONTROL_STATS_OUTCALLS  OutgoingCalls;
    DML_CALLCONTROL_STATS_RTP       RTP;
    DML_CALLCONTROL_STATS_DSP       DSP;
 } DML_CALLCONTROL_EXTENSION_STATS,*PDML_CALLCONTROL_EXTENSION_STATS;

typedef enum _CALL_WAITING_STATUS_ENUM
{
    CALL_WAITING_STATUS_DISABLED,
    CALL_WAITING_STATUS_IDLE,
    CALL_WAITING_STATUS_SECONDARYRINGING,
    CALL_WAITING_STATUS_SECONDARYCONNECTING,
    CALL_WAITING_STATUS_SECONDARYCONNECTED
} CALL_WAITING_STATUS_ENUM;

typedef enum _CONF_CALLING_STATUS_ENUM
{
    CONF_CALLING_STATUS_DISABLED,
    CONF_CALLING_STATUS_IDLE,
    CONF_CALLING_STATUS_SECONDARYCALLING,
    CONF_CALLING_STATUS_SECONDARYCONNECTING,
    CONF_CALLING_STATUS_SECONDARYCONNECTED,
    CONF_CALLING_STATUS_INCONFERENCECALL
} CONF_CALLING_STATUS_ENUM;

typedef  struct _DML_CALLCONTROL_EXTENSION
 {
    unsigned long                       uInstanceNumber;
    void*                               pParentVoiceService;
    unsigned char                       Enable;
    unsigned char                       QuiescentMode;
    CALLCTRL_EXT_STATUS_ENUM            Status;
    char                                Alias[STR_LEN_64];
    CALLCTRL_EXT_CALLSTATUS_ENUM        CallStatus;
    ORIGIN_ENUM                         Origin;
    char                                Name[STR_LEN_256];
    char                                ExtensionNumber[STR_LEN_32];
    char                                Provider[STR_LEN_256];
    char                                NumberingPlan[STR_LEN_256];
    char                                CallingFeatures[STR_LEN_256];
    CALL_WAITING_STATUS_ENUM            CallWaitingStatus;
    CONF_CALLING_STATUS_ENUM            ConferenceCallingStatus;
    unsigned int                        ConferenceCallingSessionCount;
    char                                VoiceMail[STR_LEN_256];
    DML_CALLCONTROL_EXTENSION_STATS     Stats;
 }  DML_CALLCONTROL_EXTENSION,*PDML_CALLCONTROL_EXTENSION;

typedef  struct _DML_CALLCONTROL_EXTENSION_CTRL_
 {
    DML_CALLCONTROL_EXTENSION     dml;
    unsigned char                 updated;
 } DML_CALLCONTROL_EXTENSION_CTRL_T, *PDML_CALLCONTROL_EXTENSION_CTRL_T;

typedef  struct _DML_CALLCONTROL_EXTENSION_LIST_
 {
    unsigned int                            ulQuantity;
    DML_CALLCONTROL_EXTENSION_CTRL_T*       pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_EXTENSION_LIST_T, *PDML_CALLCONTROL_EXTENSION_LIST_T;

typedef enum _TELCOVOICEMGR_LINE_STATUS_ENUM
{
    VOICE_LINE_STATE_UP = 0,
    VOICE_LINE_STATE_INITIALIZING,
    VOICE_LINE_STATE_REGISTERING,
    VOICE_LINE_STATE_UNREGISTERING,
    VOICE_LINE_STATE_ERROR,
    VOICE_LINE_STATE_TESTING,
    VOICE_LINE_STATE_QUIESCENT,
    VOICE_LINE_STATE_DISABLED
} TELCOVOICEMGR_LINE_STATUS_ENUM;

typedef  struct _DML_CALLCONTROL_LINE_STATS
 {
    DML_CALLCONTROL_STATS_INCALLS   IncomingCalls;
    DML_CALLCONTROL_STATS_OUTCALLS  OutgoingCalls;
    DML_CALLCONTROL_STATS_RTP       RTP;
    DML_CALLCONTROL_STATS_DSP       DSP;
 } DML_CALLCONTROL_LINE_STATS,*PDML_CALLCONTROL_LINE_STATS;

typedef enum _TELCOVOICEMGR_CALL_STATE_ENUM
{
    VOICE_CALL_STATE_IDLE = 0,
    VOICE_CALL_STATE_CALLING,
    VOICE_CALL_STATE_RINGING,
    VOICE_CALL_STATE_CONNECTING,
    VOICE_CALL_STATE_INCALL,
    VOICE_CALL_STATE_HOLD,
    VOICE_CALL_STATE_DISCONNECTING
} TELCOVOICEMGR_CALL_STATE_ENUM;

typedef  struct _DML_CALLCONTROL_LINE
 {
    unsigned long                         uInstanceNumber;
    void*                                 pParentVoiceService;
    unsigned char                         Enable;
    unsigned char                         QuiescentMode;
    TELCOVOICEMGR_LINE_STATUS_ENUM        Status;
    char                                  Alias[STR_LEN_64];
    TELCOVOICEMGR_CALL_STATE_ENUM         CallStatus;
    LINE_ORIGIN_ENUM                      Origin;
    char                                  DirectoryNumber[STR_LEN_32];
    char                                  Provider[STR_LEN_256];
    char                                  CallingFeatures[STR_LEN_256];
    DML_CALLCONTROL_LINE_STATS            Stats;
 } DML_CALLCONTROL_LINE,*PDML_CALLCONTROL_LINE;

typedef  struct _DML_CALLCONTROL_LINE_CTRL_
 {
    DML_CALLCONTROL_LINE     dml;
    unsigned char            updated;
 } DML_CALLCONTROL_LINE_CTRL_T, *PDML_CALLCONTROL_LINE_CTRL_T;

typedef  struct _DML_CALLCONTROL_LINE_LIST_
 {
    unsigned int                     ulQuantity;
    DML_CALLCONTROL_LINE_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_LINE_LIST_T, *PDML_CALLCONTROL_LINE_LIST_T;

typedef enum _DAY_ENUM
 {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY,
    ALL
 } DAY_ENUM;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_CFT
 {
    unsigned long       uInstanceNumber;
    void*               pParentVoiceService;
    void*               pParentCallCtrlSet;
    unsigned char       Enable;
    char                Alias[STR_LEN_64];
    DAY_ENUM            Day;
    char                StartTime[STR_LEN_5];
    char                EndTime[STR_LEN_5];
    char                ForwardedToNumber[STR_LEN_32];
 } DML_CALLCONTROL_CALLINGFEATURES_SET_CFT,*PDML_CALLCONTROL_CALLINGFEATURES_SET_CFT;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_CFT_CTRL
 {
    DML_CALLCONTROL_CALLINGFEATURES_SET_CFT     dml;
    unsigned char                               updated;
 }  DML_CALLCONTROL_CALLINGFEATURES_SET_CFT_CTRL_T, *PDML_CALLCONTROL_CALLINGFEATURES_SET_CFT_CTRL_T;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_CFT_LIST_
 {
    unsigned int                                        ulQuantity;
    DML_CALLCONTROL_CALLINGFEATURES_SET_CFT_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_CALLINGFEATURES_SET_CFT_LIST_T, *PDML_CALLCONTROL_CALLINGFEATURES_SET_CFT_LIST_T;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_SCF
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentCallCtrlSet;
    unsigned char   Enable;
    char            Alias[STR_LEN_64];
    char            CallingNumber[STR_LEN_32];
    char            ForwardedToNumber[STR_LEN_32];
 } DML_CALLCONTROL_CALLINGFEATURES_SET_SCF,*PDML_CALLCONTROL_CALLINGFEATURES_SET_SCF;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_SCF_CTRL
 {
    DML_CALLCONTROL_CALLINGFEATURES_SET_SCF     dml;
    unsigned char                               updated;
 } DML_CALLCONTROL_CALLINGFEATURES_SET_SCF_CTRL_T, *PDML_CALLCONTROL_CALLINGFEATURES_SET_SCF_CTRL_T;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_SCF_LIST_
 {
    unsigned int                                        ulQuantity;
    DML_CALLCONTROL_CALLINGFEATURES_SET_SCF_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_CALLINGFEATURES_SET_SCF_LIST_T, *PDML_CALLCONTROL_CALLINGFEATURES_SET_SCF_LIST_T;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ
 {
    unsigned long       uInstanceNumber;
    void*               pParentVoiceService;
    void*               pParentCallCtrlSet;
    unsigned char       Enable;
    char                Alias[STR_LEN_64];
    char                CallingNumber[STR_LEN_32];
 } DML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ,*PDML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ_CTRL
 {
    DML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ       dml;
    unsigned char                                   updated;
 } DML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ_CTRL_T, *PDML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ_CTRL_T;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ_LIST_
 {
    unsigned int                                            ulQuantity;
    DML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ_CTRL_T*       pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ_LIST_T, *PDML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ_LIST_T;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentCallCtrlSet;
    unsigned char   Enable;
    char            Alias[STR_LEN_64];
    unsigned int    Delay;
    char            Number[STR_LEN_32];
    unsigned int    Order;
 } DML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME,*PDML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME_CTRL
 {
    DML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME    dml;
    unsigned char                                   updated;
 } DML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME_CTRL_T, *PDML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME_CTRL_T;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME_LIST_
 {
     unsigned int                                             ulQuantity;
     DML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME_LIST_T, *PDML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME_LIST_T;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_VOICE2MAIL
 {
    unsigned char        Enable;
    unsigned int         MaxMessageLength;
    unsigned char        Attach;
    unsigned char        KeepLocal;
    char        EMailAddress[STR_LEN_256];
 } DML_CALLCONTROL_CALLINGFEATURES_SET_VOICE2MAIL, *PDML_CALLCONTROL_CALLINGFEATURES_SET_VOICE2MAIL;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET
 {
    unsigned long                                                    uInstanceNumber;
    void*                                                            pParentVoiceService;
    char                                                             Alias[STR_LEN_64];
    unsigned char                                                    CallerIDEnable;
    unsigned char                                                    CallerIDNameEnable;
    unsigned char                                                    CallWaitingEnable;
    unsigned char                                                    CallForwardUnconditionalEnable;
    char                                                             CallForwardUnconditionalNumber[STR_LEN_32];
    unsigned char                                                    CallForwardOnBusyEnable;
    char                                                             CallForwardOnBusyNumber[STR_LEN_32];
    unsigned int                                                     CallForwardOnBusyRingTimeout;
    unsigned char                                                    CallForwardOnNoAnswerEnable;
    char                                                             CallForwardOnNoAnswerNumber[STR_LEN_32];
    unsigned int                                                     CallForwardOnNoAnswerRingTimeout;
    unsigned char                                                    CallTransferEnable;
    unsigned char                                                    MWIEnable;
    unsigned char                                                    VMWIEnable;
    unsigned int                                                     LineMessagesWaiting;
    unsigned char                                                    AnonymousCallRejectionEnable;
    unsigned char                                                    AnonymousCallEnable;
    unsigned char                                                    DoNotDisturbEnable;
    unsigned char                                                    RepeatDialEnable;
    unsigned char                                                    VoiceMailEnable;
    unsigned char                                                    CallPickUpEnable;
    unsigned char                                                    CCBSEnable;
    unsigned char                                                    IIFCEnable;
    unsigned char                                                    BlockForwardEnable;
    unsigned char                                                    SecretForwarderEnable;
    unsigned char                                                    FollowMeEnable;
    unsigned char                                                    X_RDK_Central_COM_ConferenceCallingEnable;
    unsigned char                                                    X_RDK_Central_COM_HoldEnable;
    unsigned char                                                    X_RDK_Central_COM_PhoneCallerIDEnable;
    DML_CALLCONTROL_CALLINGFEATURES_SET_CFT_LIST_T          CFT;
    DML_CALLCONTROL_CALLINGFEATURES_SET_SCF_LIST_T          SCF;
    DML_CALLCONTROL_CALLINGFEATURES_SET_SCREJ_LIST_T        SCREJ;
    DML_CALLCONTROL_CALLINGFEATURES_SET_FOLLOWME_LIST_T     FollowMe;
    DML_CALLCONTROL_CALLINGFEATURES_SET_VOICE2MAIL          Voice2Mail;
 } DML_CALLCONTROL_CALLINGFEATURES_SET,*PDML_CALLCONTROL_CALLINGFEATURES_SET;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_CTRL_
 {
    DML_CALLCONTROL_CALLINGFEATURES_SET     dml;
    unsigned char                           updated;
 } DML_CALLCONTROL_CALLINGFEATURES_SET_CTRL_T, *PDML_CALLCONTROL_CALLINGFEATURES_SET_CTRL_T;

typedef  struct _DML_CALLCONTROL_CALLINGFEATURES_SET_LIST_
 {
    unsigned int                                    ulQuantity;
    DML_CALLCONTROL_CALLINGFEATURES_SET_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLCONTROL_CALLINGFEATURES_SET_LIST_T, *PDML_CALLCONTROL_CALLINGFEATURES_SET_LIST_T;

typedef struct _DML_CALLCONTROL_CALLINGFEATURES
{
    DML_CALLCONTROL_CALLINGFEATURES_SET_LIST_T  Set;
} DML_CALLCONTROL_CALLINGFEATURES,*PDML_CALLCONTROL_CALLINGFEATURES;

typedef struct _DML_CALLCONTROL
{
    unsigned int                            MaxNumberOfLines;
    unsigned int                            MaxNumberOfExtensions;
    DML_CALLCONTROL_LINE_LIST_T             Line;
    DML_CALLCONTROL_EXTENSION_LIST_T        Extension;
    DML_CALLCONTROL_MAILBOX_LIST_T          Mailbox;
    DML_CALLCONTROL_INCOMINGMAP_LIST_T      IncommingMap;
    DML_CALLCONTROL_OUTGOINGMAP_LIST_T      OutgoingMap;
    DML_CALLCONTROL_NUMBERINGPLAN_LIST_T    NumberingPlan;
    DML_CALLCONTROL_GROUP_LIST_T            Group;
    DML_CALLCONTROL_CALLINGFEATURES         CallingFeatures;
} DML_CALLCONTROL,*PDML_CALLCONTROL;

typedef  struct _DML_intERWORK_USERintERFACE
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentinterwork;
    unsigned char   Enable;
    char            Alias[STR_LEN_64];
    char            Registrar[STR_LEN_256];
    char            Network[STR_LEN_256];
 } DML_intERWORK_USERintERFACE,*PDML_intERWORK_USERintERFACE;

typedef  struct _DML_intERWORK_USERintERFACE_CTRL
 {
    DML_intERWORK_USERintERFACE     dml;
    unsigned char                   updated;
 } DML_intERWORK_USERintERFACE_CTRL_T, *PDML_intERWORK_USERintERFACE_CTRL_T;

typedef  struct _DML_intERWORK_USERintERFACE_LIST_
 {
    unsigned int                            ulQuantity;
    DML_intERWORK_USERintERFACE_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_intERWORK_USERintERFACE_LIST_T, *PDML_intERWORK_USERintERFACE_LIST_T;

typedef enum _MAP_STATUS_ENUM
{
    MAP_STATUS_ACTIVE,
    MAP_STATUS_INACTIVE
} MAP_STATUS_ENUM;

typedef  struct _DML_intERWORK_MAP
 {
    unsigned long       uInstanceNumber;
    void*               pParentVoiceService;
    void*               pParentinterwork;
    unsigned char       Enable;
    MAP_STATUS_ENUM     Status;
    char                Alias[STR_LEN_64];
    char                StatusDescription[STR_LEN_256];
    char                LastTime[STR_LEN_24];
    ORIGIN_ENUM         Origin;
    char                NetworkConnection[STR_LEN_256];
    char                UserConnection[STR_LEN_256];
    char                DigitMap[STR_LEN_256];
    unsigned char       DigitMapEnable;
    unsigned int        Priority;
 } DML_intERWORK_MAP,*PDML_intERWORK_MAP;

typedef  struct _DML_intERWORK_MAP_CTRL
 {
    DML_intERWORK_MAP     dml;
    unsigned char         updated;
 } DML_intERWORK_MAP_CTRL_T, *PDML_intERWORK_MAP_CTRL_T;

typedef  struct _DML_intERWORK_MAP_LIST_
 {
    unsigned int                  ulQuantity;
    DML_intERWORK_MAP_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_intERWORK_MAP_LIST_T, *PDML_intERWORK_MAP_LIST_T;

typedef enum _OPER_STATUS_ENUM
 {
    OPER_STATUS_INSERVICE,
    OPER_STATUS_OUTOFSERVICE,
    OPER_STATUS_NETWORK_SERVERS_OFFLINE
 } OPER_STATUS_ENUM;

typedef enum _NETWORK_CONNECTION_MODE_ENUM
 {
    NETWORK_CONN_MODE_STATIC,
    NETWORK_CONN_MODE_REGISTERDYNAMIC,
    NETWORK_CONN_MODE_REGISTERLEARN,
    NETWORK_CONN_MODE_REGISTERSTATIC
 } NETWORK_CONNECTION_MODE_ENUM;

typedef enum _USER_CONNECTION_MODE_ENUM
 {
    USER_CONN_MODE_STATIC,
    USER_CONN_MODE_REGISTERDYNAMIC,
    USER_CONN_MODE_REGISTERLEARN
 } USER_CONNECTION_MODE_ENUM;

typedef enum _CHALLENGE_MODE_ENUM
 {
    CHALLENGE_MODE_PASSTHRU,
    CHALLENGE_MODE_RESPONDLOCAL,
    CHALLENGE_MODE_HOP_BY_HOP
 } CHALLENGE_MODE_ENUM;

typedef struct _DML_intERWORK
{
    unsigned long                           uInstanceNumber;
    void*                                   pParentVoiceService;
    unsigned char                           Enable;
    unsigned char                           QuiescentMode;
    intERWORK_STATUS_ENUM                   Status;
    char                                    Alias[STR_LEN_64];
    OPER_STATUS_ENUM                        OperationalStatus;
    char                                    OperationalStatusReason[STR_LEN_256];
    NETWORK_CONNECTION_MODE_ENUM            NetworkConnectionMode;
    USER_CONNECTION_MODE_ENUM               UserConnectionMode;
    unsigned char                           E164Mode;
    CHALLENGE_MODE_ENUM                     NetworkAuthChallengeMode;
    char                                    NetworkIPAddress[STR_LEN_45];
    char                                    interworkingRuleSetURI[STR_LEN_256];
    unsigned int                            interworkingRuleSetinterval;
    char                                    interworkingRuleSetTime[STR_LEN_24];
    char                                    FirewallRuleSetURI[STR_LEN_256];
    unsigned int                            FirewallRuleSetinterval;
    char                                    FirewallRuleSetTime[STR_LEN_24];
    char                                    interworkName[STR_LEN_256];
    char                                    ProxyServer[STR_LEN_256];
    char                                    Networks[STR_LEN_256];
    char                                    E164Client[STR_LEN_256];
    DML_intERWORK_USERintERFACE_LIST_T      Userinterface;
    DML_intERWORK_MAP_LIST_T                Map;
} DML_intERWORK,*PDML_intERWORK;

typedef  struct _DML_intERWORK_CTRL
 {
    DML_intERWORK            dml;
    unsigned char            updated;
 } DML_intERWORK_CTRL_T, *PDML_intERWORK_CTRL_T;

typedef  struct _DML_intERWORK_LIST_
 {
    unsigned int                     ulQuantity;
    DML_intERWORK_CTRL_T*            pdata[TELCOVOICE_DATA_MAX];
 } DML_intERWORK_LIST_T, *PDML_intERWORK_LIST_T;

typedef enum _PROTOCOL_ENUM
{
    H323_PROTOCOL,
    SIP_PROTOCOL
}PROTOCOL_ENUM;

typedef  struct _DML_CALLLOG_SIGNALINGPERF
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentCallLog;
    PROTOCOL_ENUM   Protocol;
    unsigned int    CallSetupDelay;
    int             OutgoingMediaEstablishDelay;
    int             IncomingMediaEstablishDelay;
 } DML_CALLLOG_SIGNALINGPERF,*PDML_CALLLOG_SIGNALINGPERF;

typedef  struct _DML_CALLLOG_SIGNALINGPERF_CTRL
 {
    DML_CALLLOG_SIGNALINGPERF       dml;
    unsigned char                   updated;
 }  DML_CALLLOG_SIGNALINGPERF_CTRL_T, *PDML_CALLLOG_SIGNALINGPERF_CTRL_T;

typedef  struct _DML_CALLLOG_SIGNALINGPERF_LIST_
 {
    unsigned int                            ulQuantity;
    DML_CALLLOG_SIGNALINGPERF_CTRL_T*       pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLLOG_SIGNALINGPERF_LIST_T, *PDML_CALLLOG_SIGNALINGPERF_LIST_T;

typedef struct _DML_CALLLOG_SESSION_RTP
{
    char            FarEndIPAddress[STR_LEN_45];
    unsigned int    FarEndUDPPort;
    unsigned int    LocalUDPPort;
    int             MinJitter;
    int             MaxJitter;
    int             MeanJitter;
    int             PacketDelayVariation;
    int             BufferDelay;
    unsigned int    BurstCount;
    unsigned int    PacketsReceived;
    unsigned int    PacketsSent;
    unsigned int    PacketsLost;
    unsigned int    PacketsDiscarded;
    unsigned int    BytesReceived;
    unsigned int    BytesSent;
    unsigned int    ReceivePacketLossRate;
    unsigned int    FarEndPacketLossRate;
    int             ReceiveinterarrivalJitter;
    int             FarEndinterarrivalJitter;
    int             AverageReceiveinterarrivalJitter;
    int             AverageFarEndinterarrivalJitter;
    int             RoundTripDelay;
    int             AverageRoundTripDelay;
    unsigned int    SamplingFrequency;
} DML_CALLLOG_SESSION_RTP,*PDML_CALLLOG_SESSION_RTP;

typedef struct _DML_CALLLOG_SESSION_DSP_RXCODEC
{
    char                Codec[STR_LEN_256];
    unsigned char       SilenceSuppression;
    unsigned int        Overruns;
    unsigned int        Underruns;
} DML_CALLLOG_SESSION_DSP_RXCODEC,*PDML_CALLLOG_SESSION_DSP_RXCODEC;

typedef struct _DML_CALLLOG_SESSION_DSP_TXCODEC
{
    char                Codec[STR_LEN_256];
    unsigned char       SilenceSuppression;
    unsigned int        PacketizationPeriod;
    unsigned int        Overruns;
    unsigned int        Underruns;
} DML_CALLLOG_SESSION_DSP_TXCODEC,*PDML_CALLLOG_SESSION_DSP_TXCODEC;

typedef struct _DML_CALLLOG_SESSION_DSP
{
    DML_CALLLOG_SESSION_DSP_RXCODEC     ReceiveCodec;
    DML_CALLLOG_SESSION_DSP_TXCODEC     TransmitCodec;
} DML_CALLLOG_SESSION_DSP,*PDML_CALLLOG_SESSION_DSP;

typedef struct _DML_CALLLOG_SESSION_VOICEQUALITY
{
    char        VoIPQualityIndicator[STR_LEN_256];
    char        WorstVoIPQualityIndicatorsValues[STR_LEN_256];
    char        WorstVoIPQualityIndicatorTimestamps[STR_LEN_256];
} DML_CALLLOG_SESSION_VOICEQUALITY,*PDML_CALLLOG_SESSION_VOICEQUALITY;

typedef struct _DML_CALLLOG_SESSION_SOURCE
{
    DML_CALLLOG_SESSION_RTP             RTP;
    DML_CALLLOG_SESSION_DSP             DSP;
    DML_CALLLOG_SESSION_VOICEQUALITY    VoiceQuality;
} DML_CALLLOG_SESSION_SOURCE,*PDML_CALLLOG_SESSION_SOURCE;

typedef struct _DML_CALLLOG_SESSION_DESTINATION
{
    DML_CALLLOG_SESSION_RTP             RTP;
    DML_CALLLOG_SESSION_DSP             DSP;
    DML_CALLLOG_SESSION_VOICEQUALITY    VoiceQuality;
} DML_CALLLOG_SESSION_DESTINATION,*PDML_CALLLOG_SESSION_DESTINATION;

typedef  struct _DML_CALLLOG_SESSION
 {
    unsigned long                   uInstanceNumber;
    void*                           pParentVoiceService;
    void*                           pParentCallLog;
    STREAM_TYPE_ENUM                StreamType;
    char                            Start[STR_LEN_24];
    unsigned int                    Duration;
    char                            SessionID[STR_LEN_16];
    DML_CALLLOG_SESSION_SOURCE      Source;
    DML_CALLLOG_SESSION_DESTINATION Destination;
 } DML_CALLLOG_SESSION,*PDML_CALLLOG_SESSION;

typedef  struct _DML_CALLLOG_SESSION_CTRL
 {
    DML_CALLLOG_SESSION      dml;
    unsigned char            updated;
 } DML_CALLLOG_SESSION_CTRL_T, *PDML_CALLLOG_SESSION_CTRL_T;

typedef  struct _DML_CALLLOG_SESSION_LIST_
 {
    unsigned int                     ulQuantity;
    DML_CALLLOG_SESSION_CTRL_T*      pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLLOG_SESSION_LIST_T, *PDML_CALLLOG_SESSION_LIST_T;

typedef enum _DIRECTION_ENUM
{
    DIRECTION_INCOMING,
    DIRECTION_OUTGOING
} DIRECTION_ENUM;

typedef enum _CALL_TERMINATION_CAUSE_ENUM
{
    CALL_TERMINAL_CAUSE_NOEXTENSIONSMAPPED,
    CALL_TERMINAL_CAUSE_NOEXTENSIONSAVAILABLE,
    CALL_TERMINAL_CAUSE_ANONYMOUSCALLREJECTION,
    CALL_TERMINAL_CAUSE_CALLWAITINGREJECTED,
    CALL_TERMINAL_CAUSE_CALLFORWARDINGUNCONDITIONAL,
    CALL_TERMINAL_CAUSE_CALLFORWARDINGBUSY,
    CALL_TERMINAL_CAUSE_CALLFORWARDINGNOREPLY,
    CALL_TERMINAL_CAUSE_LOCALDISCONNECT,
    CALL_TERMINAL_CAUSE_LOCALFORBIDDEN,
    CALL_TERMINAL_CAUSE_LOCALTIMEOUT,
    CALL_TERMINAL_CAUSE_LOCALMEDIAERROR,
    CALL_TERMINAL_CAUSE_LOCALPRIORITY,
    CALL_TERMINAL_CAUSE_LOCALREJECT,
    CALL_TERMINAL_CAUSE_LOCALTRANSFER,
    CALL_TERMINAL_CAUSE_LOCALintERNALERROR,
    CALL_TERMINAL_CAUSE_REMOTEDISCONNECT,
    CALL_TERMINAL_CAUSE_REMOTEBADREQUEST,
    CALL_TERMINAL_CAUSE_REMOTEFORBIDDEN,
    CALL_TERMINAL_CAUSE_REMOTENOTFOUND,
    CALL_TERMINAL_CAUSE_REMOTEREJECT,
    CALL_TERMINAL_CAUSE_REMOTENOTALLOWED,
    CALL_TERMINAL_CAUSE_REMOTENOTACCEPTABLE,
    CALL_TERMINAL_CAUSE_REMOTETIMEOUT,
    CALL_TERMINAL_CAUSE_REMOTEUNAVAILABLE,
    CALL_TERMINAL_CAUSE_REMOTEBUSY,
    CALL_TERMINAL_CAUSE_REMOTENOTSUPPORTED,
    CALL_TERMINAL_CAUSE_REMOTENETWORKFAILURE
} CALL_TERMINATION_CAUSE_ENUM;

typedef  struct _DML_CALLLOG
{
    unsigned long                      uInstanceNumber;
    void*                              pParentVoiceService;
    char                               Alias[STR_LEN_64];
    char                               CallingPartyNumber[STR_LEN_256];
    char                               CalledPartyNumber[STR_LEN_256];
    char                               Source[STR_LEN_256];
    char                               Destination[STR_LEN_256];
    char                               RemoteParty[STR_LEN_32];
    char                               UsedLine[STR_LEN_256];
    char                               UsedExtensions[STR_LEN_256];
    DIRECTION_ENUM                     Direction;
    char                               Start[STR_LEN_24];
    unsigned int                       Duration;
    CALL_TERMINATION_CAUSE_ENUM        CallTerminationCause;
    DML_CALLLOG_SIGNALINGPERF_LIST_T   SignalingPerformance;
    DML_CALLLOG_SESSION_LIST_T         Session;
} DML_CALLLOG,*PDML_CALLLOG;

typedef  struct  _DML_CALLLOG_CTRL
 {
    DML_CALLLOG     dml;
    unsigned char   updated;
 }  DML_CALLLOG_CTRL_T, *PDML_CALLLOG_CTRL_T;

typedef  struct _DML_CALLLOG_LIST_
 {
    unsigned int            ulQuantity;
    DML_CALLLOG_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_CALLLOG_LIST_T, *PDML_CALLLOG_LIST_T;

typedef struct _DML_VOIPPROFILE_RTP_RTCP
{
   unsigned char      Enable;
   unsigned int       TxRepeatinterval;
   char       LocalCName[STR_LEN_64];
}DML_VOIPPROFILE_RTP_RTCP,*PDML_VOIPPROFILE_RTP_RTCP;

typedef enum _KEYING_METHODS_ENUM
{
    KEYING_METHOD_NULL,
    KEYING_METHOD_STATIC,
    KEYING_METHOD_SDP,
    KEYING_METHOD_IKE
} KEYING_METHODS_ENUM;

typedef struct _DML_VOIPPROFILE_RTP_SRTP
{
    unsigned char           Enable;
    KEYING_METHODS_ENUM     KeyingMethods;
    char                    EncryptionKeySizes[STR_LEN_256];
} DML_VOIPPROFILE_RTP_SRTP,*PDML_VOIPPROFILE_RTP_SRTP;

typedef struct _DML_VOIPPROFILE_RTP_REDUNDANCY
{
    unsigned char       Enable;
    unsigned int        PayloadType;
    unsigned int        BlockPayloadType;
    int                 FaxAndModemRedundancy;
    int                 ModemRedundancy;
    int                 DTMFRedundancy;
    int                 VoiceRedundancy;
    unsigned int        MaxSessionsUsingRedundancy;
} DML_VOIPPROFILE_RTP_REDUNDANCY,*PDML_VOIPPROFILE_RTP_REDUNDANCY;

typedef enum _JITTER_TYPE_ENUM
{
    JITTER_STATIC,
    JITTER_DYNAMIC
} JITTER_TYPE_ENUM;

typedef struct _DML_VOIPPROFILE_RTP
{
    unsigned int                    LocalPortMin;
    unsigned int                    LocalPortMax;
    unsigned int                    Gmin;
    unsigned int                    DSCPMark;
    int                             VLANIDMark;
    int                             EthernetPriorityMark;
    unsigned int                    TelephoneEventPayloadType;
    JITTER_TYPE_ENUM                JitterBufferType;
    unsigned int                    JitterBufferMaxSize;
    unsigned int                    JitterBufferMinSize;
    unsigned int                    JitterBufferActualSize;
    unsigned int                    X_RDK_SKBMark;
    char                            X_RDK_Firewall_Rule_Data[STR_LEN_256];
    DML_VOIPPROFILE_RTP_RTCP        RTCP;
    DML_VOIPPROFILE_RTP_SRTP        SRTP;
    DML_VOIPPROFILE_RTP_REDUNDANCY  Redundancy;
} DML_VOIPPROFILE_RTP,*PDML_VOIPPROFILE_RTP;

typedef enum _TCF_METHOD
{
    TCF_LOCAL,
    TCF_NETWORK
} TCF_METHOD_ENUM;

typedef struct _DML_VOIPPROFILE_FAXT38
{
    unsigned int                MaxBitRate;
    unsigned int                HighSpeedRedundancy;
    unsigned int                LowSpeedRedundancy;
    TCF_METHOD_ENUM             TCFMethod;
}DML_VOIPPROFILE_FAXT38, *PDML_VOIPPROFILE_FAXT38;

typedef enum _DTMF_METHOD
{
    DTMF_INBAND,
    DTMF_RFC4733,
    DTMF_SIPINFO
}DTMF_METHOD_ENUM;

typedef enum _DTMF_METHOD_G711
{
    DTMF_G711_INBAND,
    DTMF_G711_RFC4733,
    DTMF_G711_SIPINFO,
    DTMF_G711_EMPTY
}DTMF_METHOD_G711_ENUM;

typedef  struct  _DML_VOIPPROFILE
 {
    unsigned long           uInstanceNumber;
    void*                   pParentVoiceService;
    unsigned char           Enable;
    unsigned char           QuiescentMode;
    char                    Name[STR_LEN_64];
    char                    Alias[STR_LEN_64];
    DTMF_METHOD_ENUM        DTMFMethod;
    DTMF_METHOD_G711_ENUM   DTMFMethodG711;
    char                    QIModelUsed[STR_LEN_128];
    unsigned int            QICalculationinterval;
    unsigned int            NumberOfWorstQIValues;
    char                    X_RDK_Central_COM_DigitMap[STR_LEN_256];
    char                    X_RDK_Central_COM_EmergencyDigitMap[STR_LEN_256];
    unsigned int            X_RDK_Central_COM_SDigitTimer;
    unsigned int            X_RDK_Central_COM_ZDigitTimer;
    DML_VOIPPROFILE_RTP     RTP;
    DML_VOIPPROFILE_FAXT38  FaxT38;
 } DML_VOIPPROFILE,*PDML_VOIPPROFILE;

typedef  struct  _DML_VOIPPROFILE_CTRL
 {
    DML_VOIPPROFILE     dml;
    unsigned char       updated;
 } DML_VOIPPROFILE_CTRL_T, *PDML_VOIPPROFILE_CTRL_T;

typedef  struct  _DML_VOIPPROFILE_LIST_
 {
    unsigned int                ulQuantity;
    DML_VOIPPROFILE_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_VOIPPROFILE_LIST_T, *PDML_VOIPPROFILE_LIST_T;

typedef  struct  _DML_CODECPROFILE
 {
    unsigned long           uInstanceNumber;
    void*                   pParentVoiceService;
    unsigned char           Enable;
    char                    Alias[STR_LEN_64];
    char                    Codec[STR_LEN_256];
    char                    PacketizationPeriod[STR_LEN_64];
    unsigned char           SilenceSuppression;
 } DML_CODECPROFILE,*PDML_CODECPROFILE;

typedef  struct  _DML_CODECPROFILE_CTRL
 {
    DML_CODECPROFILE            dml;
    unsigned char               updated;
 } DML_CODECPROFILE_CTRL_T, *PDML_CODECPROFILE_CTRL_T;

typedef  struct _DML_CODECPROFILE_LIST_
 {
    unsigned int                     ulQuantity;
    DML_CODECPROFILE_CTRL_T*         pdata[TELCOVOICE_DATA_MAX];
 } DML_CODECPROFILE_LIST_T, *PDML_CODECPROFILE_LIST_T;

typedef  struct  _DML_TONE_DESCRIPTION
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    unsigned char   ToneEnable;
    char            Alias[STR_LEN_64];
    char            ToneName[STR_LEN_64];
    char            TonePattern[STR_LEN_256];
    char            ToneFile[STR_LEN_256];
    unsigned int    ToneRepetitions;
    char            ToneText[STR_LEN_64];
 } DML_TONE_DESCRIPTION,*PDML_TONE_DESCRIPTION;

typedef  struct _DML_TONE_PATTERN
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    unsigned char   Enable;
    char            Alias[STR_LEN_64];
    unsigned char   ToneOn;
    unsigned int    Frequency1;
    int             Power1;
    unsigned int    Frequency2;
    int             Power2;
    unsigned int    Frequency3;
    int             Power3;
    unsigned int    Frequency4;
    int             Power4;
    unsigned int    ModulationFrequency;
    int             ModulationPower;
    unsigned int    Duration;
    char            NextPattern[STR_LEN_256];
 } DML_TONE_PATTERN,*PDML_TONE_PATTERN;

typedef enum _FUNCTION_ENUM
{
    FUNCTION_BUSY,
    FUNCTION_CONFIRMATION,
    FUNCTION_DIAL,
    FUNCTION_LINEMESSAGESWAITING,
    FUNCTION_OFFHOOKWARNING,
    FUNCTION_RINGBACK,
    FUNCTION_REORDER,
    FUNCTION_STUTTERDIAL,
    FUNCTION_CALLWAITING1,
    FUNCTION_CALLWAITING2,
    FUNCTION_CALLWAITING3,
    FUNCTION_CALLWAITING4,
    FUNCTION_ALERTINGSIGNAL,
    FUNCTION_SPECIALDIAL,
    FUNCTION_SPECIALINFO,
    FUNCTION_RELEASE,
    FUNCTION_CONGESTION,
    FUNCTION_USERDEFINED1,
    FUNCTION_USERDEFINED2,
    FUNCTION_USERDEFINED3,
    FUNCTION_USERDEFINED4
} FUNCTION_ENUM;

typedef  struct _DML_TONE_EVENTPROFILE_EVENT
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentToneEvtProfile;
    char            Alias[STR_LEN_64];
    FUNCTION_ENUM   Function;
    char            Tone[STR_LEN_256];
 } DML_TONE_EVENTPROFILE_EVENT,*PDML_TONE_EVENTPROFILE_EVENT;

typedef  struct _DML_TONE_EVENTPROFILE_EVENT_CTRL
 {
     DML_TONE_EVENTPROFILE_EVENT     dml;
     unsigned char                   updated;
 } DML_TONE_EVENTPROFILE_EVENT_CTRL_T, *PDML_TONE_EVENTPROFILE_EVENT_CTRL_T;

typedef  struct _DML_TONE_EVENTPROFILE_EVENT_LIST_
 {
    unsigned int                            ulQuantity;
    DML_TONE_EVENTPROFILE_EVENT_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_TONE_EVENTPROFILE_EVENT_LIST_T, *PDML_TONE_EVENTPROFILE_EVENT_LIST_T;

typedef  struct _DML_TONE_EVENTPROFILE
 {
    unsigned long                       uInstanceNumber;
    void*                               pParentVoiceService;
    char                                Alias[STR_LEN_64];
    DML_TONE_EVENTPROFILE_EVENT_LIST_T  Event;
 } DML_TONE_EVENTPROFILE,*PDML_TONE_EVENTPROFILE;

typedef  struct _DML_TONE_EVENTPROFILE_CTRL
 {
    DML_TONE_EVENTPROFILE     dml;
    unsigned char             updated;
 } DML_TONE_EVENTPROFILE_CTRL_T, *PDML_TONE_EVENTPROFILE_CTRL_T;

typedef  struct _DML_TONE_EVENTPROFILE_LIST_
 {
    unsigned int                      ulQuantity;
    DML_TONE_EVENTPROFILE_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_TONE_EVENTPROFILE_LIST_T, *PDML_TONE_EVENTPROFILE_LIST_T;

typedef struct _TELCOVOICEMGR_DML_TONE_DESCRIPTION
{
    unsigned int          InstanceNumber;
    char                  Alias[64];
    unsigned int          EntryID;
    unsigned char         ToneEnable;
    char                  ToneName[64];
    unsigned int          TonePattern;
    char                  ToneFile[BUF_LEN_256];
    unsigned int          ToneRepetitions;
    char                  ToneText[64];
} TELCOVOICEMGR_DML_TONE_DESCRIPTION, *PTELCOVOICEMGR_DML_TONE_DESCRIPTION;

typedef struct _DML_TONE_DESCRIPTION_CTRL_
{
    TELCOVOICEMGR_DML_TONE_DESCRIPTION    dml;
    unsigned char                         updated;
} DML_TONE_DESCRIPTION_CTRL_T;

typedef  struct _DML_TONE_DESCRIPTION_LIST_
 {
    unsigned int                     ulQuantity;
    DML_TONE_DESCRIPTION_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_TONE_DESCRIPTION_LIST_T, *PDML_TONE_DESCRIPTION_LIST_T;

typedef struct _TELCOVOICEMGR_DML_TONE_PATTERN
{
    unsigned int          InstanceNumber;
    char                  Alias[64];
    unsigned int          EntryID;
    unsigned char         ToneOn;
    unsigned int          Frequency1;
    int                   Power1;
    unsigned int          Frequency2;
    int                   Power2;
    unsigned int          Frequency3;
    int                   Power3;
    unsigned int          Frequency4;
    int                   Power4;
    unsigned int          ModulationFrequency;
    int                   ModulationPower;
    unsigned int          Duration;
    unsigned int          NextEntryID;
} TELCOVOICEMGR_DML_TONE_PATTERN, *PTELCOVOICEMGR_DML_TONE_PATTERN;

typedef struct _DML_TONE_PATTERN_CTRL_
{
    TELCOVOICEMGR_DML_TONE_PATTERN    dml;
    unsigned char                     updated;
} DML_TONE_PATTERN_CTRL_T;

typedef  struct _DML_TONE_PATTERN_LIST_
 {
    unsigned int                     ulQuantity;
    DML_TONE_PATTERN_CTRL_T*         pdata[TELCOVOICE_DATA_MAX];
 } DML_TONE_PATTERN_LIST_T, *PDML_TONE_PATTERN_LIST_T;

typedef struct _DML_TONE
{
    char                            DefautEventProfile[STR_LEN_256];
    DML_TONE_DESCRIPTION_LIST_T     Description;
    DML_TONE_PATTERN_LIST_T         Pattern;
    DML_TONE_EVENTPROFILE_LIST_T    EventProfile;
} DML_TONE, *PDML_TONE;

typedef struct _DML_TERMINAL_AUDIO_VOICEPROCESSING
{
    int                  TransmitGain;
    int                  ReceiveGain;
    unsigned char        EchoCancellationEnable;
    unsigned char        EchoCancellationInUse;
    unsigned int         EchoCancellationTail;
} DML_TERMINAL_AUDIO_VOICEPROCESSING, *PDML_TERMINAL_AUDIO_VOICEPROCESSING;

typedef  struct _DML_TERMINAL_AUDIO
 {
    unsigned long                       uInstanceNumber;
    void*                               pParentVoiceService;
    void*                               pParentTerminal;
    char                                Alias[STR_LEN_64];
    char                                Name[STR_LEN_256];
    DML_TERMINAL_AUDIO_VOICEPROCESSING  VoiceProcessing;
 } DML_TERMINAL_AUDIO,*PDML_TERMINAL_AUDIO;

typedef  struct _DML_TERMINAL_AUDIO_CTRL
 {
    DML_TERMINAL_AUDIO     dml;
    unsigned char          updated;
 } DML_TERMINAL_AUDIO_CTRL_T, *PDML_TERMINAL_AUDIO_CTRL_T;

typedef  struct _DML_TERMINAL_AUDIO_LIST_
 {
    unsigned int                     ulQuantity;
    DML_TERMINAL_AUDIO_CTRL_T*       pdata[TELCOVOICE_DATA_MAX];
 } DML_TERMINAL_AUDIO_LIST_T, *PDML_TERMINAL_AUDIO_LIST_T;

typedef  struct _DML_TERMINAL_BUTTONMAP_BUTTON
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentTerminal;
    char            Alias[STR_LEN_64];
    char            ButtonName[STR_LEN_16];
    char            FacilityAction[STR_LEN_64];
    char            FacilityActionArgument[STR_LEN_256];
    char            QuickDialNumber[STR_LEN_40];
    char            ButtonMessage[STR_LEN_64];
    unsigned char   UserAccess;
 } DML_TERMINAL_BUTTONMAP_BUTTON,*PDML_TERMINAL_BUTTONMAP_BUTTON;

typedef  struct _DML_TERMINAL_BUTTONMAP_BUTTON_CTRL
 {
    DML_TERMINAL_BUTTONMAP_BUTTON       dml;
    unsigned char                       updated;
 } DML_TERMINAL_BUTTONMAP_BUTTON_CTRL_T, *PDML_TERMINAL_BUTTONMAP_BUTTON_CTRL_T;

typedef  struct _DML_TERMINAL_BUTTONMAP_BUTTON_LIST_
 {
    unsigned int                              ulQuantity;
    DML_TERMINAL_BUTTONMAP_BUTTON_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_TERMINAL_BUTTONMAP_BUTTON_LIST_T, *PDML_TERMINAL_BUTTONMAP_BUTTON_LIST_T;

typedef struct _DML_TERMINAL_BUTTONMAP
 {
    DML_TERMINAL_BUTTONMAP_BUTTON_LIST_T Button;
 } DML_TERMINAL_BUTTONMAP, *PDML_TERMINAL_BUTTONMAP;

typedef  struct _DML_TERMINAL_RINGER_DESCRIPTION
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentTerminal;
    unsigned char   RingEnable;
    char            Alias[STR_LEN_64];
    char            RingName[STR_LEN_64];
    char            RingPattern[STR_LEN_256];
    char            RingFile[STR_LEN_256];
 } DML_TERMINAL_RINGER_DESCRIPTION,*PDML_TERMINAL_RINGER_DESCRIPTION;

typedef  struct _DML_TERMINAL_RINGER_DESCRIPTION_CTRL
 {
    DML_TERMINAL_RINGER_DESCRIPTION     dml;
    unsigned char                       updated;
 }  DML_TERMINAL_RINGER_DESCRIPTION_CTRL_T, *PDML_TERMINAL_RINGER_DESCRIPTION_CTRL_T;

typedef  struct _DML_TERMINAL_RINGER_DESCRIPTION_LIST_
 {
    unsigned int                                ulQuantity;
    DML_TERMINAL_RINGER_DESCRIPTION_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_TERMINAL_RINGER_DESCRIPTION_LIST_T, *PDML_TERMINAL_RINGER_DESCRIPTION_LIST_T;

typedef  struct _DML_TERMINAL_RINGER_PATTERN
 {
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    void*           pParentTerminal;
    unsigned char   Enable;
    char            Alias[STR_LEN_64];
    unsigned char   RingerOn;
    unsigned int    Duration;
    char    NextPattern[STR_LEN_256];
 } DML_TERMINAL_RINGER_PATTERN,*PDML_TERMINAL_RINGER_PATTERN;

typedef  struct _DML_TERMINAL_RINGER_PATTERN_CTRL
 {
    DML_TERMINAL_RINGER_PATTERN     dml;
    unsigned char                   updated;
 } DML_TERMINAL_RINGER_PATTERN_CTRL_T, *PDML_TERMINAL_RINGER_PATTERN_CTRL_T;

typedef  struct _DML_TERMINAL_RINGER_PATTERN_LIST_
 {
    unsigned int                            ulQuantity;
    DML_TERMINAL_RINGER_PATTERN_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 } DML_TERMINAL_RINGER_PATTERN_LIST_T, *PDML_TERMINAL_RINGER_PATTERN_LIST_T;

typedef struct _DML_TERMINAL_RINGER
 {
    DML_TERMINAL_RINGER_DESCRIPTION_LIST_T  Description;
    DML_TERMINAL_RINGER_PATTERN_LIST_T      Pattern;
 } DML_TERMINAL_RINGER, *PDML_TERMINAL_RINGER;

typedef enum _DIAG_TESTSELECTOR_ENUM
{
    DIAG_TESTSELECTOR_PHONE_CONNECTIVITY_TEST = 0,
    DIAG_TESTSELECTOR_HAZARD_POTENTIAL,
    DIAG_TESTSELECTOR_FOREIGN_VOLTAGE,
    DIAG_TESTSELECTOR_RESISTIVE_FAULTS,
    DIAG_TESTSELECTOR_OFF_HOOK,
    DIAG_TESTSELECTOR_REN
} DIAG_TESTSELECTOR_ENUM;

typedef struct _DML_TERMINAL_DIAGTESTS
 {
    DIAG_STATE_ENUM           DiagnosticsState;
    DIAG_TESTSELECTOR_ENUM    TestSelector;
    unsigned char             PhoneRinging;
    char                      X_RDK_TestResult[STR_LEN_256];
 } DML_TERMINAL_DIAGTESTS,*PDML_TERMINAL_DIAGTESTS;

typedef  struct _DML_VOICESERVICE_TERMINAL
{
    unsigned long               uInstanceNumber;
    void*                       pParentVoiceService;
    unsigned char               Enable;
    unsigned char               QuiescentMode;
    TERMINAL_STATUS_ENUM        Status;
    char                        Alias[STR_LEN_64];
    char                        ToneEventProfile[STR_LEN_256];
    DML_TERMINAL_AUDIO_LIST_T   Audio;
    DML_TERMINAL_BUTTONMAP      ButtonMap;
    DML_TERMINAL_RINGER         Ringer;
    DML_TERMINAL_DIAGTESTS      DiagTests;
} DML_VOICESERVICE_TERMINAL,*PDML_VOICESERVICE_TERMINAL;

typedef  struct _DML_VOICESERVICE_TERMINAL_CTRL
 {
    DML_VOICESERVICE_TERMINAL       dml;
    unsigned char                   updated;
 } DML_VOICESERVICE_TERMINAL_CTRL_T,*PDML_VOICESERVICE_TERMINAL_CTRL_T;

typedef  struct _DML_VOICESERVICE_TERMINAL_LIST_
{
   unsigned int                          ulQuantity;
   DML_VOICESERVICE_TERMINAL_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
} DML_VOICESERVICE_TERMINAL_LIST_T,*PDML_VOICESERVICE_TERMINAL_LIST_T;

typedef  struct _DML_VOICESERVICE_CLOCKSYNC_CLOCKSOURCE
{
    unsigned long   uInstanceNumber;
    void*           pParentVoiceService;
    unsigned char   Enable;
    char            Alias[STR_LEN_64];
    unsigned int    Order;
    char            interface[STR_LEN_256];
} DML_VOICESERVICE_CLOCKSYNC_CLOCKSOURCE,*PDML_VOICESERVICE_CLOCKSYNC_CLOCKSOURCE;

typedef  struct _DML_VOICESERVICE_CLOCKSYNC_CLOCKSOURCE_CTRL
 {
    DML_VOICESERVICE_CLOCKSYNC_CLOCKSOURCE      dml;
    unsigned char                               updated;
 } DML_VOICESERVICE_CLOCKSYNC_CLOCKSOURCE_CTRL_T, *PDML_VOICESERVICE_CLOCKSYNC_CLOCKSOURCE_CTRL_T;

typedef  struct _DML_VOICESERVICE_CLOCKSYNCICE_CLOCKSYNC_CLOCKSOURCE_LIST_
 {
    unsigned int                                       ulQuantity;
    DML_VOICESERVICE_CLOCKSYNC_CLOCKSOURCE_CTRL_T*     pdata[TELCOVOICE_DATA_MAX];
 }  DML_VOICESERVICE_CLOCKSYNC_CLOCKSOURCE_LIST_T, *PDML_VOICESERVICE_CLOCKSYNC_CLOCKSOURCE_LIST_T;

typedef struct _DML_VOICESERVICE_CLOCKSYNC
{
    char                                            CurrentSource[STR_LEN_256];
    char                                            Description[STR_LEN_64];
    unsigned char                                   AutoRevert;
    DML_VOICESERVICE_CLOCKSYNC_CLOCKSOURCE_LIST_T   ClockSource;
}DML_VOICESERVICE_CLOCKSYNC, *PDML_VOICESERVICE_CLOCKSYNC;

typedef enum _TELCOVOICEMGR_VOICE_ENABLE_ENUM
{
    VOICE_SERVICE_DISABLE = 0,
    VOICE_SERVICE_ENABLE
} TELCOVOICEMGR_VOICE_ENABLE_ENUM;

typedef enum _TELCOVOICEMGR_VOICE_STATUS_ENUM
{
    VOICE_PROCESS_STATUS_STOPPED = 0,
    VOICE_PROCESS_STATUS_STARTING,
    VOICE_PROCESS_STATUS_STARTED,
    VOICE_PROCESS_STATUS_STOPPING,
    VOICE_PROCESS_STATUS_ERROR
} TELCOVOICEMGR_VOICE_STATUS_ENUM;

typedef struct _TELCOVOICEMGR_DML_X_RDK_DEBUG
{
    char                                     CCTKTraceGroup[BUF_LEN_256];
    char                                     CCTKTraceLevel[BUF_LEN_256];
    char                                     ModuleLogLevels[BUF_LEN_256];
    char                                     LogServer[BUF_LEN_256];
    unsigned int                             LogServerPort;
} TELCOVOICEMGR_DML_X_RDK_DEBUG, *PTELCOVOICEMGR_DML_X_RDK_DEBUG;

typedef struct _TELCOVOICEMGR_DML_VOICESERVICE
 {
    unsigned long                           InstanceNumber;
    char                                    Alias[STR_LEN_64];
    unsigned char                           X_RDK_DisableLoopCurrentUntilRegistered;
    char                                    X_RDK_BoundIfName[STR_LEN_256];
    char                                    X_RDK_IpAddressFamily[STR_LEN_256];
    char                                    X_RDK_BoundIpAddr[STR_LEN_256];
    TELCOVOICEMGR_VOICE_ENABLE_ENUM         X_RDK_Enable;
    TELCOVOICEMGR_VOICE_STATUS_ENUM         X_RDK_Status;
    unsigned char                           X_RDK_FactoryReset;
    TELCOVOICEMGR_DML_X_RDK_DEBUG           X_RDK_DebugObj;
    DML_VOICESERVICE_CAPABILITIES           Capabilities;
    DML_RESERVEDPORTS                       ReservedPorts;
    DML_ISDN                                ISDN_obj;
    DML_POTS                                POTS_obj;
    DML_DECT                                DECT_obj;
    DML_SIP                                 SIP_obj;
    DML_MGCP                                MGCP_obj;
    DML_H323                                H323_obj;
    PDML_TRUNK_LIST_T                       Trunk;
    DML_CALLCONTROL                         CallControl_obj;
    PDML_intERWORK_LIST_T                   interwork;
    PDML_CALLLOG_LIST_T                     CallLog;
    PDML_VOIPPROFILE_LIST_T                 VoIPProfile;
    PDML_CODECPROFILE_LIST_T                CodecProfile;
    DML_TONE                                Tone_obj;
    PDML_VOICESERVICE_TERMINAL_LIST_T       Terminal;
    DML_VOICESERVICE_CLOCKSYNC              ClockSynchronization_obj;
 } TELCOVOICEMGR_DML_VOICESERVICE, *PTELCOVOICEMGR_DML_VOICESERVICE;

typedef enum _PROTOCOL_TYPE
{
  SIP,
  RTP,
}PROTOCOL_TYPE;

typedef struct {
  PROTOCOL_TYPE     protocol;
  int32_t           iEthPriorityMark;
  unsigned char     iUpdateStatus;
}ethPriorityValStruct_t;

typedef struct {
  unsigned char bSipMarkRead;
  unsigned char bRtpMarkRead;
  unsigned int  sipSkbMark;
  unsigned int  rtpSkbMark;
  char aIpStateParamName[16];
}retSkbMarksStruct_t;

typedef enum
{
    VOICE_HAL_AUTH_UNAME = 0,
    VOICE_HAL_AUTH_PWD
} TELCOVOICEMGR_VOICE_CREDENTIAL_TYPE_ENUM;

typedef enum
{
    VOICE_HAL_AF_INET_V4 = 0,
    VOICE_HAL_AF_INET_V6
}  TELCOVOICEMGR_VOICE_IP_ADD_FAMILY;

typedef enum
{
    VOICE_HAL_IP_LINK_STATE_DOWN = 0,
    VOICE_HAL_IP_LINK_STATE_UP
}  TELCOVOICEMGR_VOICE_IP_LINK_STATE;

typedef  enum
{
    VOICE_CALLING_FEATURE_CALL_WAITING = 0,
    VOICE_CALLING_FEATURE_MSG_WAIT_INDICATOR,
    VOICE_CALLING_FEATURE_CONF_CALL,
    VOICE_CALLING_FEATURE_HOLD,
    VOICE_CALLING_FEATURE_CALLER_ID,
} TELCOVOICEMGR_VOICE_CALL_FEATURE_TYPE_ENUM;

typedef enum _TELCOVOICEMGR_ENABLE_ENUM
{
    DISABLED = 0,
    QUIESCENT,
    ENABLED
} TELCOVOICEMGR_ENABLE_ENUM;

typedef enum _TELCOVOICEMGR_PROFILE_DTMF_METHOD_ENUM
{
    VOICE_PROFILE_DTMF_METHOD_INBAND = 0,
    VOICE_PROFILE_DTMF_METHOD_RFC2833,
    VOICE_PROFILE_DTMF_METHOD_SIPINFO
} TELCOVOICEMGR_PROFILE_DTMF_METHOD_ENUM;

typedef enum _TELCOVOICEMGR_PROFILE_DTMF_METHODG711_ENUM
{
    VOICE_PROFILE_DTMF_METHODG711_INBAND = 0,
    VOICE_PROFILE_DTMF_METHODG711_RFC2833,
    VOICE_PROFILE_DTMF_METHODG711_SIPINFO
} TELCOVOICEMGR_PROFILE_DTMF_METHODG711_ENUM;

typedef enum _TELCOVOICEMGR_PROFILE_FAXPASSTHROUGH_ENUM
{
    VOICE_PROFILE_FAXPASSTHROUGH_DISABLE = 0,
    VOICE_PROFILE_FAXPASSTHROUGH_AUTO,
    VOICE_PROFILE_FAXPASSTHROUGH_FORCE
} TELCOVOICEMGR_PROFILE_FAXPASSTHROUGH_ENUM;

typedef enum _TELCOVOICEMGR_PROFILE_MODEMPASSTHROUGH_ENUM
{
    VOICE_PROFILE_MODEMPASSTHROUGH_DISABLE = 0,
    VOICE_PROFILE_MODEMPASSTHROUGH_AUTO,
    VOICE_PROFILE_MODEMPASSTHROUGH_FORCE
} TELCOVOICEMGR_PROFILE_MODEMPASSTHROUGH_ENUM;

typedef enum _TELCOVOICEMGR_PHYintERFACE_TESTSTATE_ENUM
{
    PHYintERFACE_TESTSTATE_NONE = 0,
    PHYintERFACE_TESTSTATE_REQUESTED,
    PHYintERFACE_TESTSTATE_COMPLETE,
    PHYintERFACE_TESTSTATE_ERROR_TESTNOTSUPPORTED
} TELCOVOICEMGR_PHYintERFACE_TESTSTATE_ENUM;

typedef enum _TELCOVOICEMGR_PHYintERFACE_TESTSELECTOR_ENUM
{
    PHYintERFACE_TESTSELECTOR_PHONE_CONNECTIVITY_TEST = 0,
    PHYintERFACE_TESTSELECTOR_HAZARD_POTENTIAL,
    PHYintERFACE_TESTSELECTOR_FOREIGN_VOLTAGE,
    PHYintERFACE_TESTSELECTOR_RESISTIVE_FAULTS,
    PHYintERFACE_TESTSELECTOR_OFF_HOOK,
    PHYintERFACE_TESTSELECTOR_REN
} TELCOVOICEMGR_PHYintERFACE_TESTSELECTOR_ENUM;

typedef enum _TELCOVOICEMGR_SIP_INBOUNDAUTH_ENUM
{
    SIP_INBOUNDAUTH_NONE = 0,
    SIP_INBOUNDAUTH_DIGEST
} TELCOVOICEMGR_SIP_INBOUNDAUTH_ENUM;

typedef enum _TELCOVOICEMGR_MGCP_REGISTERMODE_ENUM
{
    MGCP_REGISTERMODE_WILDCARD= 0,
    MGCP_REGISTERMODE_INDIVIDUAL
} TELCOVOICEMGR_MGCP_REGISTERMODE_ENUM;

typedef enum _TELCOVOICEMGR_LINE_CWSTATUS_ENUM
{
    VOICE_CW_STATE_DISABLED = 0,
    VOICE_CW_STATE_IDLE,
    VOICE_CW_STATE_SECONDARY_RINGING,
    VOICE_CW_STATE_SECONDARY_CONNECTING,
    VOICE_CW_STATE_SECONDARY_CONNECTED
} TELCOVOICEMGR_LINE_CWSTATUS_ENUM;

typedef enum _TELCOVOICEMGR_LINE_CONFERENCE_CALLING_STATUS_ENUM
{
    VOICE_CONFERENCE_CALLING_STATE_DISABLED = 0,
    VOICE_CONFERENCE_CALLING_STATE_IDLE,
    VOICE_CONFERENCE_CALLING_STATE_SECONDARY_RINGING,
    VOICE_CONFERENCE_CALLING_STATE_SECONDARY_CONNECTING,
    VOICE_CONFERENCE_CALLING_STATE_SECONDARY_CONNECTED,
    VOICE_CONFERENCE_CALLING_STATE_IN_CONFERENCE_CALL
} TELCOVOICEMGR_LINE_CONFERENCE_CALLING_STATUS_ENUM;

typedef enum _TELCOVOICEMGR_TCFMETHOD_ENUM
{
    TCFMETHOD_LOCAL = 0,
    TCFMETHOD_NETWORK
} TELCOVOICEMGR_TCFMETHOD_ENUM;

typedef enum _TELCOVOICEMGR_CAPABILITIES_SIP_ROLE_ENUM
{
    SIP_ROLE_USER_AGENT = 0,
    SIP_ROLE_B2B_USER_AGENT,
    SIP_ROLE_OUTBOUND_PROXY
} TELCOVOICEMGR_CAPABILITIES_SIP_ROLE_ENUM;

typedef struct _TELCOVOICEMGR_DML_SERVICE_PROVIDER_INFO
{
    char          Name[BUF_LEN_256];
    char          URL[BUF_LEN_256];
    char          ContactPhoneNumber[BUF_LEN_256];
    char          EmailAddress[BUF_LEN_256];
} TELCOVOICEMGR_DML_SERVICE_PROVIDER_INFO, *PTELCOVOICEMGR_DML_SERVICE_PROVIDER_INFO;

typedef struct _TELCOVOICEMGR_DML_SIP_EVENTSUBSCRIBE
{
    unsigned long         InstanceNumber;
    char                  Alias[64];
    char                  Event[32];
    char                  Notifier[BUF_LEN_256];
    unsigned int          NotifierPort;
    char                  NotifierTransport[BUF_LEN_256];
    unsigned int          ExpireTime;
} TELCOVOICEMGR_DML_SIP_EVENTSUBSCRIBE, *PTELCOVOICEMGR_DML_SIP_EVENTSUBSCRIBE;

typedef struct _DML_SIP_EVENTSUBSCRIBE_CTRL_
{
    TELCOVOICEMGR_DML_SIP_EVENTSUBSCRIBE     dml;
    unsigned char                            updated;
} DML_SIP_EVENTSUBSCRIBE_CTRL_T;

typedef  struct _DML_SIP_EVENTSUBSCRIBE_LIST__
{
    unsigned int                          ulQuantity;
    DML_SIP_EVENTSUBSCRIBE_CTRL_T*        pdata[TELCOVOICEMGR_DATA_MAX_DML_SIP_EVENTSUBSCRIBE];
} DML_SIP_EVENTSUBSCRIBE_LIST_T;


typedef struct _TELCOVOICEMGR_DML_SIP_RESPONSEMAP
{
    unsigned long         InstanceNumber;
    char                  Alias[64];
    unsigned int          SIPResponseNumber;
    char                  TextMessage[64];
    unsigned int          Tone;
} TELCOVOICEMGR_DML_SIP_RESPONSEMAP, *PTELCOVOICEMGR_DML_SIP_RESPONSEMAP;


typedef struct _DML_SIP_RESPONSEMAP_CTRL_
{
    TELCOVOICEMGR_DML_SIP_RESPONSEMAP     dml;
    unsigned char                         updated;
} DML_SIP_RESPONSEMAP_CTRL_T;

typedef struct _DML_SIP_RESPONSEMAP_LIST__
{
    unsigned int                    ulQuantity;
    DML_SIP_RESPONSEMAP_CTRL_T*     pdata[TELCOVOICEMGR_DATA_MAX_DML_SIP_RESPONSEMAP];
} DML_SIP_RESPONSEMAP_LIST_T;


typedef struct _TELCOVOICEMGR_DML_SIP
{
    char                ProxyServer[BUF_LEN_256];
    unsigned int        ProxyServerPort;
    char                ProxyServerTransport[BUF_LEN_256];
    char                RegistrarServer[BUF_LEN_256];
    unsigned int        RegistrarServerPort;
    char                RegistrarServerTransport[BUF_LEN_256];
    char                UserAgentDomain[BUF_LEN_256];
    unsigned int        UserAgentPort;
    char                UserAgentTransport[BUF_LEN_256];
    char                OutboundProxy[BUF_LEN_256];
    unsigned int        OutboundProxyPort;
    char                Organization[BUF_LEN_256];
    unsigned int        RegistrationPeriod;
    unsigned int        TimerT1;
    unsigned int        TimerT2;
    unsigned int        TimerT4;
    unsigned int        TimerA;
    unsigned int        TimerB;
    unsigned int        TimerC;
    unsigned int        TimerD;
    unsigned int        TimerE;
    unsigned int        TimerF;
    unsigned int        TimerG;
    unsigned int        TimerH;
    unsigned int        TimerI;
    unsigned int        TimerJ;
    unsigned int        TimerK;
    unsigned int        InviteExpires;
    unsigned int        ReInviteExpires;
    unsigned int        RegisterExpires;
    unsigned int        RegistersMinExpires;
    unsigned int        RegisterRetryinterval;
    TELCOVOICEMGR_SIP_INBOUNDAUTH_ENUM   InboundAuth;
    char                InboundAuthUsername[BUF_LEN_256];
    char                InboundAuthPassword[BUF_LEN_256];
    unsigned char       UseCodecPriorityInSDPResponse;
    unsigned int        DSCPMark;
    int                 VLANIDMark;
    int                 EthernetPriorityMark;
    unsigned int        X_RDK_SKBMark;
    char                ConferencingURI[BUF_LEN_256];
    unsigned char       NetworkDisconnect;
    unsigned char       X_RDK_PRACKRequired;
    char                X_RDK_Firewall_Rule_Data[BUF_LEN_256];
    DML_SIP_EVENTSUBSCRIBE_LIST_T   SipEventSubscribeList;
    DML_SIP_RESPONSEMAP_LIST_T      SipResponseMapList;
} TELCOVOICEMGR_DML_SIP, *PTELCOVOICEMGR_DML_SIP;

typedef struct _TELCOVOICEMGR_DML_MGCP
{
    char                                  CallAgent1[BUF_LEN_256];
    unsigned int                          CallAgentPort1;
    char                                  CallAgent2[BUF_LEN_256];
    unsigned int                          CallAgentPort2;
    unsigned int                          RetranintervalTimer;
    unsigned int                          MaxRetranCount;
    TELCOVOICEMGR_MGCP_REGISTERMODE_ENUM  RegisterMode;
    unsigned int                          LocalPort;
    char                                  Domain[BUF_LEN_256];
    char                                  User[64];
    unsigned int                          DSCPMark;
    int                                   VLANIDMark;
    int                                   EthernetPriorityMark;
    unsigned char                         AllowPiggybackEvents;
    unsigned char                         SendRSIPImmediately;
} TELCOVOICEMGR_DML_MGCP, *PTELCOVOICEMGR_DML_MGCP;

typedef struct _TELCOVOICEMGR_DML_H323
{
    char                  Gatekeeper[BUF_LEN_256];
    unsigned int          GatekeeperPort;
    char                  GatekeeperID[BUF_LEN_256];
    unsigned int          TimeToLive;
    unsigned char         H235Authentication;
    char                  AuthPassword[BUF_LEN_256];
    char                  SendersID[BUF_LEN_256];
    unsigned int          DSCPMark;
    int                   VLANIDMark;
    int                   EthernetPriorityMark;
} TELCOVOICEMGR_DML_H323, *PTELCOVOICEMGR_DML_H323;

typedef struct _TELCOVOICEMGR_DML_RTP_RTCP
{
    unsigned char         Enable;
    unsigned int          TxRepeatinterval;
    char                  LocalCName[64];
} TELCOVOICEMGR_DML_RTP_RTCP, *PTELCOVOICEMGR_DML_RTP_RTCP;

typedef struct _TELCOVOICEMGR_DML_RTP_SRTP
{
    unsigned char          Enable;
    char                   KeyingMethods[BUF_LEN_256];
    char                   EncryptionKeySizes[BUF_LEN_256];
} TELCOVOICEMGR_DML_RTP_SRTP, *PTELCOVOICEMGR_DML_RTP_SRTP;

typedef struct _TELCOVOICEMGR_DML_RTP_REDUNDANCY
{
    unsigned char         Enable;
    unsigned int          PayloadType;
    unsigned int          BlockPayloadType;
    int                   FaxAndModemRedundancy;
    int                   ModemRedundancy;
    int                   DTMFRedundancy;
    int                   VoiceRedundancy;
    unsigned int          MaxSessionsUsingRedundancy;
} TELCOVOICEMGR_DML_RTP_REDUNDANCY, *PTELCOVOICEMGR_DML_RTP_REDUNDANCY;

typedef struct _TELCOVOICEMGR_DML_RTP
{
    unsigned int                      LocalPortMin;
    unsigned int                      LocalPortMax;
    unsigned int                      DSCPMark;
    int                               VLANIDMark;
    int                               EthernetPriorityMark;
    unsigned int                      TelephoneEventPayloadType;
    unsigned int                      X_RDK_SKBMark;
    char                              X_RDK_Firewall_Rule_Data[BUF_LEN_256];
    TELCOVOICEMGR_DML_RTP_RTCP        RTCPObj;
    TELCOVOICEMGR_DML_RTP_SRTP        SRTPObj;
    TELCOVOICEMGR_DML_RTP_REDUNDANCY  RedundancyObj;
} TELCOVOICEMGR_DML_RTP, *PTELCOVOICEMGR_DML_RTP;

typedef struct _TELCOVOICEMGR_DML_NUMBERINGPLAN_PREFIXINFO
{
    unsigned int           InstanceNumber;
    void                   *pParentVoiceProfile;
    char                   Alias[64];
    char                   PrefixRange[42];
    unsigned int           PrefixMinNumberOfDigits;
    unsigned int           PrefixMaxNumberOfDigits;
    unsigned int           NumberOfDigitsToRemove;
    unsigned int           PosOfDigitsToRemove;
    unsigned int           DialTone;
    char                   FacilityAction[64];
    char                   FacilityActionArgument[BUF_LEN_256];
} TELCOVOICEMGR_DML_NUMBERINGPLAN_PREFIXINFO, *PTELCOVOICEMGR_DML_NUMBERINGPLAN_PREFIXINFO;


typedef struct _DML_NUMBERINGPLAN_PREFIXINFO_CTRL_
{
    TELCOVOICEMGR_DML_NUMBERINGPLAN_PREFIXINFO    dml;
    unsigned char                                 updated;
} DML_NUMBERINGPLAN_PREFIXINFO_CTRL_T;

typedef struct _DML_NUMBERINGPLAN_PREFIXINFO_LIST_
{
    unsigned int                           ulQuantity;
    DML_NUMBERINGPLAN_PREFIXINFO_CTRL_T*   pdata[TELCOVOICEMGR_DATA_MAX_NUMBERINGPLAN_PREFIXINFO];
} DML_NUMBERINGPLAN_PREFIXINFO_LIST_T;

typedef struct _TELCOVOICEMGR_DML_NUMBERINGPLAN
{
    unsigned int                                    MinimumNumberOfDigits;
    unsigned int                                    MaximumNumberOfDigits;
    unsigned int                                    interDigitTimerStd;
    unsigned int                                    interDigitTimerOpen;
    unsigned int                                    InvalidNumberTone;
    unsigned int                                    PrefixInfoMaxEntries;
    DML_NUMBERINGPLAN_PREFIXINFO_LIST_T             PrefixInfoList;
} TELCOVOICEMGR_DML_NUMBERINGPLAN, *PTELCOVOICEMGR_DML_NUMBERINGPLAN;

typedef struct _TELCOVOICEMGR_DML_TONE_EVENT
{
    unsigned int          InstanceNumber;
    char                  Alias[64];
    char                  Function[64];
    unsigned int          ToneID;
} TELCOVOICEMGR_DML_TONE_EVENT, *PTELCOVOICEMGR_DML_TONE_EVENT;

typedef struct _DML_TONE_EVENT_CTRL_
{
    TELCOVOICEMGR_DML_TONE_EVENT    dml;
    unsigned char                   updated;
} DML_TONE_EVENT_CTRL_T;

typedef struct _DML_TONE_EVENT_LIST_
{
    unsigned int                     ulQuantity;
    DML_TONE_EVENT_CTRL_T*           pdata[TELCOVOICEMGR_DATA_MAX_TONE_EVENT];
} DML_TONE_EVENT_LIST_T;


typedef struct _TELCOVOICEMGR_DML_TONE
{
    DML_TONE_EVENT_LIST_T        ToneEventList;
    DML_TONE_DESCRIPTION_LIST_T  ToneDescriptionList;
    DML_TONE_PATTERN_LIST_T      TonePatternList;
} TELCOVOICEMGR_DML_TONE, *PTELCOVOICEMGR_DML_TONE;

typedef struct _TELCOVOICEMGR_DML_LINE_SIP_EVENTSUBSCRIBE
{
    unsigned long        InstanceNumber;
    char                 Alias[64];
    char                 Event[32];
    char                 AuthUserName[128];
    char                 AuthPassword[128];
} TELCOVOICEMGR_DML_LINE_SIP_EVENTSUBSCRIBE, *PTELCOVOICEMGR_DML_LINE_SIP_EVENTSUBSCRIBE;

typedef struct _DML_LINE_SIP_EVENTSUBSCRIBE_CTRL_
{
    TELCOVOICEMGR_DML_LINE_SIP_EVENTSUBSCRIBE    dml;
    unsigned char                                updated;
} DML_LINE_SIP_EVENTSUBSCRIBE_CTRL_T;

typedef struct _DML_LINE_SIP_EVENTSUBSCRIBE_LIST_
{
    unsigned int                             ulQuantity;
    DML_LINE_SIP_EVENTSUBSCRIBE_CTRL_T*      pdata[TELCOVOICEMGR_DATA_MAX_DML_LINE_SIP_EVENTSUBSCRIBE];
} DML_LINE_SIP_EVENTSUBSCRIBE_LIST_T;

typedef struct _TELCOVOICEMGR_DML_LINE_SIP
{
    char           AuthUserName[128];
    char           AuthPassword[128];
    char           URI[389];
    DML_LINE_SIP_EVENTSUBSCRIBE_LIST_T    LineSipEventSubscribeList;
} TELCOVOICEMGR_DML_LINE_SIP, *PTELCOVOICEMGR_DML_LINE_SIP;

typedef struct _TELCOVOICEMGR_DML_LINE_MGCP
{
    char           LineName[32];
} TELCOVOICEMGR_DML_LINE_MGCP, *PTELCOVOICEMGR_DML_LINE_MGCP;

typedef struct _TELCOVOICEMGR_DML_LINE_H323
{
    char           H323ID[32];
} TELCOVOICEMGR_DML_LINE_H323, *PTELCOVOICEMGR_DML_LINE_H323;

typedef struct _TELCOVOICEMGR_DML_LINE_RINGER_EVENT
{
    unsigned long         InstanceNumber;
    char                  Alias[64];
    char                  Function[64];
    unsigned int          RingID;
} TELCOVOICEMGR_DML_LINE_RINGER_EVENT, *PTELCOVOICEMGR_DML_LINE_RINGER_EVENT;

typedef struct _TELCOVOICEMGR_DML_LINE_RINGER_DESCRIPTION
{
    unsigned long         InstanceNumber;
    char                  Alias[64];
    unsigned int          EntryID;
    unsigned char         RingEnable;
    char                  RingName[64];
    unsigned int          RingPattern;
    char                  RingFile[BUF_LEN_256];
} TELCOVOICEMGR_DML_LINE_RINGER_DESCRIPTION, *PTELCOVOICEMGR_DML_LINE_RINGER_DESCRIPTION;

typedef struct _TELCOVOICEMGR_DML_LINE_RINGER_PATTERN
{
    unsigned long         InstanceNumber;
    char                  Alias[64];
    unsigned int          EntryID;
    unsigned char         RingerOn;
    unsigned int          Duration;
    unsigned int          NextEntryID;
} TELCOVOICEMGR_DML_LINE_RINGER_PATTERN, *PTELCOVOICEMGR_DML_LINE_RINGER_PATTERN;


typedef struct _DML_LINE_RINGER_DESCRIPTION_CTRL_
{
    TELCOVOICEMGR_DML_LINE_RINGER_DESCRIPTION    dml;
    unsigned char                                updated;
} DML_LINE_RINGER_DESCRIPTION_CTRL_T;

typedef struct _DML_LINE_RINGER_DESCRIPTION_LIST_
{
    unsigned int                             ulQuantity;
    DML_LINE_RINGER_DESCRIPTION_CTRL_T*      pdata[TELCOVOICEMGR_DATA_MAX_DML_LINE_RINGER_DESCRIPTION];
} DML_LINE_RINGER_DESCRIPTION_LIST_T;


typedef struct _DML_LINE_RINGER_EVENT_CTRL_
{
    TELCOVOICEMGR_DML_LINE_RINGER_EVENT    dml;
    unsigned char                          updated;
} DML_LINE_RINGER_EVENT_CTRL_T;

typedef struct _DML_LINE_RINGER_EVENT_LIST_
{
    unsigned int                             ulQuantity;
    DML_LINE_RINGER_EVENT_CTRL_T*            pdata[TELCOVOICEMGR_DATA_MAX_DML_LINE_RINGER_EVENT];
} DML_LINE_RINGER_EVENT_LIST_T;


typedef struct _DML_LINE_RINGER_PATTERN_CTRL_
{
    TELCOVOICEMGR_DML_LINE_RINGER_PATTERN    dml;
    unsigned char                            updated;
} DML_LINE_RINGER_PATTERN_CTRL_T;

typedef struct _DML_LINE_RINGER_PATTERN_LIST_
{
    unsigned int                         ulQuantity;
    DML_LINE_RINGER_PATTERN_CTRL_T*      pdata[TELCOVOICEMGR_DATA_MAX_DML_LINE_RINGER_PATTERN];
} DML_LINE_RINGER_PATTERN_LIST_T;

typedef struct _TELCOVOICEMGR_DML_LINE_RINGER
{
    DML_LINE_RINGER_EVENT_LIST_T        LineRingerEventList;
    DML_LINE_RINGER_DESCRIPTION_LIST_T  LineRingerDescriptionList;
    DML_LINE_RINGER_PATTERN_LIST_T      LineRingerPatternList;
} TELCOVOICEMGR_DML_LINE_RINGER, *PTELCOVOICEMGR_DML_LINE_RINGER;

typedef struct _TELCOVOICEMGR_DML_LINE_CALLINGFEATURES
{
    unsigned char         CallerIDEnable;
    unsigned char         CallerIDNameEnable;
    char                  CallerIDName[BUF_LEN_256];
    unsigned char         CallWaitingEnable;
    TELCOVOICEMGR_LINE_CWSTATUS_ENUM                    CallWaitingStatus;
    unsigned int          MaxSessions;
    TELCOVOICEMGR_LINE_CONFERENCE_CALLING_STATUS_ENUM   ConferenceCallingStatus;
    unsigned int         ConferenceCallingSessionCount;
    unsigned char        CallForwardUnconditionalEnable;
    char                 CallForwardUnconditionalNumber[32];
    unsigned char        CallForwardOnBusyEnable;
    char                 CallForwardOnBusyNumber[32];
    unsigned char        CallForwardOnNoAnswerEnable;
    char                 CallForwardOnNoAnswerNumber[32];
    unsigned int         CallForwardOnNoAnswerRingCount;
    unsigned char        CallTransferEnable;
    unsigned char        MWIEnable;
    unsigned char        MessageWaiting;
    unsigned char        AnonymousCallBlockEnable;
    unsigned char        AnonymousCalEnable;
    unsigned char        DoNotDisturbEnable;
    unsigned char        CallReturnEnable;
    unsigned char        RepeatDialEnable;
    unsigned char        ConferenceCallingEnable;
    unsigned char        HoldEnable;
    unsigned char        PhoneCallerIDEnable;
} TELCOVOICEMGR_DML_LINE_CALLINGFEATURES, *PTELCOVOICEMGR_DML_LINE_CALLINGFEATURES;

typedef struct _TELCOVOICEMGR_DML_LINE_VOICEPROCESSING
{
    int                   TransmitGain;
    int                   ReceiveGain;
    unsigned char         EchoCancellationEnable;
    unsigned char         EchoCancellationInUse;
    unsigned char         EchoCancellationTail;
} TELCOVOICEMGR_DML_LINE_VOICEPROCESSING, *PTELCOVOICEMGR_DML_LINE_VOICEPROCESSING;

typedef struct _TELCOVOICEMGR_DML_LINE_CODECLIST
{
    unsigned long        InstanceNumber;
    char                 Alias[64];
    unsigned int         EntryID;
    char                 Codec[64];
    unsigned int         BitRate;
    char                 PacketizationPeriod[64];
    unsigned char        SilenceSuppression;
    unsigned char        Enable;
    unsigned int         Priority;
} TELCOVOICEMGR_DML_LINE_CODECLIST, *PTELCOVOICEMGR_DML_LINE_CODECLIST;

typedef struct _DML_LINE_CODECLIST_CTRL_
{
    TELCOVOICEMGR_DML_LINE_CODECLIST         dml;
    unsigned char                            updated;
} DML_LINE_CODECLIST_CTRL_T;

typedef struct _DML_LINE_CODECLIST_LIST_
{
    unsigned int                         ulQuantity;
    DML_LINE_CODECLIST_CTRL_T*           pdata[TELCOVOICEMGR_DATA_MAX_DML_LINE_CODECLIST];
} DML_LINE_CODECLIST_LIST_T;

typedef struct _TELCOVOICEMGR_DML_LINE_CODEC
{
    char                 TransmitCodec[64];
    char                 ReceiveCodec[64];
    unsigned int         TransmitBitRate;
    unsigned int         ReceiveBitRate;
    unsigned char        TransmitSilenceSuppression;
    unsigned char        ReceiveSilenceSuppression;
    unsigned int         TransmitPacketizationPeriod;
    DML_LINE_CODECLIST_LIST_T  LineCodecList;
} TELCOVOICEMGR_DML_LINE_CODEC, *PTELCOVOICEMGR_DML_LINE_CODEC;

typedef struct _TELCOVOICEMGR_DML_LINE_SESSION
{
    unsigned long        InstanceNumber;
    char                 SessionStartTime[64];
    unsigned int         SessionDuration;
    char                 FarEndIPAddress[45];
    unsigned int         FarEndUDPPort;
    unsigned int         LocalUDPPort;
} TELCOVOICEMGR_DML_LINE_SESSION, *PTELCOVOICEMGR_DML_LINE_SESSION;

typedef struct _TELCOVOICEMGR_DML_LINE_STATS
{
    unsigned char        ResetStatistics;
    unsigned int         PacketsSent;
    unsigned int         PacketsReceived;
    unsigned int         BytesSent;
    unsigned int         BytesReceived;
    unsigned int         PacketsLost;
    unsigned int         Overruns;
    unsigned int         Underruns;
    unsigned int         IncomingCallsReceived;
    unsigned int         IncomingCallsAnswered;
    unsigned int         IncomingCallsConnected;
    unsigned int         IncomingCallsFailed;
    unsigned int         OutgoingCallsAttempted;
    unsigned int         OutgoingCallsAnswered;
    unsigned int         OutgoingCallsConnected;
    unsigned int         OutgoingCallsFailed;
    unsigned int         CallsDropped;
    unsigned int         TotalCallTime;
    unsigned int         ServerDownTime;
    unsigned int         ReceivePacketLossRate;
    unsigned int         FarEndPacketLossRate;
    unsigned int         ReceiveinterarrivalJitter;
    unsigned int         FarEndinterarrivalJitter;
    unsigned int         RoundTripDelay;
    unsigned int         AverageReceiveinterarrivalJitter;
    unsigned int         AverageFarEndinterarrivalJitter;
    unsigned int         AverageRoundTripDelay;
} TELCOVOICEMGR_DML_LINE_STATS, *PTELCOVOICEMGR_DML_LINE_STATS;

typedef struct _DML_LINE_SESSION_CTRL_
{
    TELCOVOICEMGR_DML_LINE_SESSION    dml;
    unsigned char                     updated;
} DML_LINE_SESSION_CTRL_T;

typedef struct _DML_LINE_SESSION_LIST_
{
    unsigned int                     ulQuantity;
    DML_LINE_SESSION_CTRL_T*         pdata[TELCOVOICEMGR_DATA_MAX_DML_LINE_SESSION];
} DML_LINE_SESSION_LIST_T;

typedef struct _TELCOVOICEMGR_DML_LINE
{
    unsigned long                              InstanceNumber;
    void                                       *pParentVoiceProfile;
    TELCOVOICEMGR_ENABLE_ENUM                  Enable;
    char                                       Alias[64];
    char                                       DirectoryNumber[32];
    TELCOVOICEMGR_LINE_STATUS_ENUM             Status;
    TELCOVOICEMGR_CALL_STATE_ENUM              CallState;
    char                                       X_RDK_OutboundProxyAddresses[BUF_LEN_256];
    char                                       PhyReferenceList[32];
    unsigned char                              RingMuteStatus;
    unsigned int                               RingVolumeStatus;
    TELCOVOICEMGR_DML_LINE_SIP                 LineSipObj;
    TELCOVOICEMGR_DML_LINE_MGCP                LineMGCPObj;
    TELCOVOICEMGR_DML_LINE_H323                LineH323Obj;
    TELCOVOICEMGR_DML_LINE_RINGER              LineRingerObj;
    TELCOVOICEMGR_DML_LINE_CALLINGFEATURES     LineCallingFeaturesObj;
    TELCOVOICEMGR_DML_LINE_VOICEPROCESSING     LineVoiceProcessingObj;
    TELCOVOICEMGR_DML_LINE_CODEC               LineCodecObj;
    DML_LINE_SESSION_LIST_T                    LineSessionList;
    TELCOVOICEMGR_DML_LINE_STATS               LineStatsObj;
} TELCOVOICEMGR_DML_LINE, *PTELCOVOICEMGR_DML_LINE;


typedef struct _DML_LINE_CTRL_
{
    TELCOVOICEMGR_DML_LINE    dml;
    unsigned char             updated;
} DML_LINE_CTRL_T;

typedef struct _DML_LINE_LIST_
{
    unsigned int                     ulQuantity;
    DML_LINE_CTRL_T*                 pdata[TELCOVOICEMGR_DATA_MAX_LINE];
} DML_LINE_LIST_T;


typedef struct _TELCOVOICEMGR_DML_FAXT38
{
    unsigned char                          Enable;
    unsigned int                           BitRate;
    unsigned int                           HighSpeedPacketRate;
    unsigned int                           HighSpeedRedundancy;
    unsigned int                           LowSpeedRedundancy;
    TELCOVOICEMGR_TCFMETHOD_ENUM           TCFMethod;
} TELCOVOICEMGR_DML_FAXT38,  *PTELCOVOICEMGR_DML_FAXT38;


typedef struct _TELCOVOICEMGR_DML_BUTTON
{
    unsigned long          InstanceNumber;
    char                   Alias[64];
    char                   ButtonName[16];
    char                   FacilityAction[64];
    char                   FacilityActionArgument[BUF_LEN_256];
    char                   QuickDialNumber[BUF_LEN_256];
    char                   ButtonMessage[64];
    unsigned char          UserAccess;
} TELCOVOICEMGR_DML_BUTTON,  *PTELCOVOICEMGR_DML_BUTTON;

typedef struct _DML_BUTTON_CTRL_
{
    TELCOVOICEMGR_DML_BUTTON    dml;
    unsigned char               updated;
} DML_BUTTON_CTRL_T;

typedef struct _DML_BUTTON_LIST_
{
    unsigned int                     ulQuantity;
    DML_BUTTON_CTRL_T*               pdata[TELCOVOICEMGR_DATA_MAX_BUTTON];
} DML_BUTTON_LIST_T;

typedef struct _TELCOVOICEMGR_DML_BUTTONMAP
{
    unsigned long                    NumberOfButtons;
    DML_BUTTON_LIST_T                ButtonList;
} TELCOVOICEMGR_DML_BUTTONMAP,  *PTELCOVOICEMGR_DML_BUTTONMAP;

typedef struct _TELCOVOICEMGR_DML_VOICEPROFILE
{
    unsigned long                                InstanceNumber;
    void*                                        *pParentVoiceService;
    TELCOVOICEMGR_ENABLE_ENUM                    Enable[64];
    char                                         Alias[64];
    unsigned char                                Reset;
    unsigned long                                NumberOfLines;
    char                                         Name[64];
    char                                         SignalingProtocol[128];
    unsigned int                                 MaxSessions;
    TELCOVOICEMGR_PROFILE_DTMF_METHOD_ENUM       DTMFMethod[64];
    TELCOVOICEMGR_PROFILE_DTMF_METHODG711_ENUM   DTMFMethodG711[64];
    char                                         Region[128];
    char                                         DigitMap[BUF_LEN_256];
    unsigned char                                DigitMapEnable;
    char                                         X_RDK_DigitMap[BUF_LEN_256];
    char                                         EmergencyDigitMap[BUF_LEN_256];
    unsigned int                                 SDigitTimer;
    unsigned int                                 ZDigitTimer;
    unsigned char                                STUNEnable;
    char                                         STUNServer[BUF_LEN_256];
    unsigned int                                 NonVoiceBandwidthReservedUpstream;
    unsigned int                                 NonVoiceBandwidthReservedDownstream;
    unsigned char                                PSTNFailOver;
    TELCOVOICEMGR_PROFILE_FAXPASSTHROUGH_ENUM    FaxPassThrough;
    TELCOVOICEMGR_PROFILE_MODEMPASSTHROUGH_ENUM  ModemPassThrough;
    TELCOVOICEMGR_DML_SERVICE_PROVIDER_INFO      ServiceProviderInfoObj;
    TELCOVOICEMGR_DML_SIP                        SIPObj;
    TELCOVOICEMGR_DML_MGCP                       MGCPObj;
    TELCOVOICEMGR_DML_H323                       H323Obj;
    TELCOVOICEMGR_DML_RTP                        RTPObj;
    TELCOVOICEMGR_DML_NUMBERINGPLAN              NumberingPlanObj;
    TELCOVOICEMGR_DML_TONE                       ToneObj;
    TELCOVOICEMGR_DML_BUTTONMAP                  ButtonMapObj;
    TELCOVOICEMGR_DML_FAXT38                     Fax38Obj;
    DML_LINE_LIST_T                              LineList;
} TELCOVOICEMGR_DML_VOICEPROFILE, *PTELCOVOICEMGR_DML_PROFILE;


typedef struct _DML_PROFILE_CTRL_
{
    TELCOVOICEMGR_DML_VOICEPROFILE     dml;
    unsigned char                      updated;
} DML_PROFILE_CTRL_T;

typedef struct _DML_PROFILE_LIST__
{
    unsigned int            ulQuantity;
    DML_PROFILE_CTRL_T*     pdata[TELCOVOICEMGR_DATA_MAX_PROFILE];
} DML_PROFILE_LIST_T;


typedef struct _TELCOVOICEMGR_DML_PHYintERFACE_TESTS
{
    TELCOVOICEMGR_PHYintERFACE_TESTSTATE_ENUM       TestState;
    TELCOVOICEMGR_PHYintERFACE_TESTSELECTOR_ENUM    TestSelector;
    char                                            X_RDK_TestResult[64];
    unsigned char                                   PhoneConnectivity;
} TELCOVOICEMGR_DML_PHYintERFACE_TESTS,  *PTELCOVOICEMGR_DML_PHYintERFACE_TESTS;

typedef struct _TELCOVOICEMGR_DML_PHYintERFACE
{
    unsigned long                            InstanceNumber;
    void*                                    *pParentVoiceService;
    char                                     Alias[64];
    char                                     PhyPort[2];
    unsigned int                             interfaceID;
    char                                     Description[32];
    TELCOVOICEMGR_DML_PHYintERFACE_TESTS     PhyinterfaceTestsObj;
} TELCOVOICEMGR_DML_PHYintERFACE, *PTELCOVOICEMGR_DML_PHYintERFACE;


typedef struct _DML_PHYintERFACE_CTRL_
{
    TELCOVOICEMGR_DML_PHYintERFACE    dml;
    unsigned char                     updated;
} DML_PHYintERFACE_CTRL_T;

typedef struct _DML_PHYintERFACE_LIST_
{
    unsigned int                ulQuantity;
    DML_PHYintERFACE_CTRL_T*    pdata[TELCOVOICEMGR_DATA_MAX_PHYintERFACE];
} DML_PHYintERFACE_LIST_T;

typedef struct _TELCOVOICEMGR_DML_CAPABILITIES_SIP
{
    TELCOVOICEMGR_CAPABILITIES_SIP_ROLE_ENUM   Role;
    char                                       Extensions[BUF_LEN_256];
    char                                       Transports[BUF_LEN_256];
    char                                       URISchemes[BUF_LEN_256];
    unsigned char                              EventSubscription;
    unsigned char                              ResponseMap;
    char                                       TLSAuthenticationProtocols[BUF_LEN_256];
    char                                       TLSAuthenticationKeySizes[BUF_LEN_256];
    char                                       TLSEncryptionProtocols[BUF_LEN_256];
    char                                       TLSEncryptionKeySizes[BUF_LEN_256];
    char                                       TLSKeyExchangeProtocols[BUF_LEN_256];
} TELCOVOICEMGR_DML_CAPABILITIES_SIP, *PTELCOVOICEMGR_DML_CAPABILITIES_SIP;

typedef struct _TELCOVOICEMGR_DML_CAPABILITIES_MGCP
{
    char                                       Extensions[BUF_LEN_256];
} TELCOVOICEMGR_DML_CAPABILITIES_MGCP, *PTELCOVOICEMGR_DML_CAPABILITIES_MGCP;

typedef struct _TELCOVOICEMGR_DML_CAPABILITIES_H323
{
    unsigned char                              FastStart;
    char                                       H235AuthenticationMethods[BUF_LEN_256];
} TELCOVOICEMGR_DML_CAPABILITIES_H323, *PTELCOVOICEMGR_DML_CAPABILITIES_H323;

typedef struct _TELCOVOICEMGR_DML_CAPABILITIES_CODECS
{
    unsigned long                              InstanceNumber;
    char                                       Alias[64];
    unsigned long                              EntryID;
    char                                       Codec[64];
    unsigned long                              BitRate;
    char                                       PacketizationPeriod[64];
    unsigned char                              SilenceSuppression;
} TELCOVOICEMGR_DML_CAPABILITIES_CODECS, *PTELCOVOICEMGR_DML_CAPABILITIES_CODECS;

typedef struct _DML_CAPABILITIES_CODECS_CTRL_
{
    TELCOVOICEMGR_DML_CAPABILITIES_CODECS      dml;
    unsigned char                              updated;
} DML_CAPABILITIES_CODECS_CTRL_T;

typedef struct _DML_CAPABILITIES_CODECS_LIST_
{
    unsigned int                          ulQuantity;
    DML_CAPABILITIES_CODECS_CTRL_T*       pdata[TELCOVOICEMGR_DATA_MAX_VOICE_CAPABILITIES_CODECS];
} DML_CAPABILITIES_CODECS_LIST_T;

typedef struct _TELCOVOICEMGR_DML_CAPABILITIES
{
    unsigned long                                       MaxProfileCount;
    unsigned long                                       MaxLineCount;
    unsigned long                                       MaxSessionsPerLine;
    unsigned long                                       MaxSessionCount;
    char                                                SignalingProtocols[BUF_LEN_256];
    char                                                Regions[BUF_LEN_256];
    unsigned char                                       RTCP;
    unsigned char                                       SRTP;
    char                                                SRTPKeyingMethods[BUF_LEN_256];
    char                                                SRTPEncryptionKeySizes[BUF_LEN_256];
    unsigned char                                       RTPRedundancy;
    unsigned char                                       DSCPCoupled;
    unsigned char                                       EthernetTaggingCoupled;
    unsigned char                                       PSTNSoftSwitchOver;
    unsigned char                                       FaxT38;
    unsigned char                                       FaxPassThrough;
    unsigned char                                       ModemPassThrough;
    unsigned char                                       ToneGeneration;
    unsigned char                                       ToneDescriptionsEditable;
    unsigned char                                       PatternBasedToneGeneration;
    unsigned char                                       FileBasedToneGeneration;
    char                                                ToneFileFormats[BUF_LEN_256];
    unsigned char                                       RingGeneration;
    unsigned char                                       RingDescriptionsEditable;
    unsigned char                                       PatternBasedRingGeneration;
    unsigned char                                       RingPatternEditable;
    unsigned char                                       FileBasedRingGeneration;
    char                                                RingFileFormats[BUF_LEN_256];
    unsigned char                                       DigitMap;
    unsigned char                                       NumberingPlan;
    unsigned char                                       ButtonMap;
    unsigned char                                       VoicePortTests;
    TELCOVOICEMGR_DML_CAPABILITIES_SIP                  CapabilitiesSIPObj;
    TELCOVOICEMGR_DML_CAPABILITIES_MGCP                 CapabilitiesMGCPObj;
    TELCOVOICEMGR_DML_CAPABILITIES_H323                 CapabilitiesH323Obj;
    DML_CAPABILITIES_CODECS_LIST_T                      CapabilitiesCodecList;
} TELCOVOICEMGR_DML_CAPABILITIES, *PTELCOVOICEMGR_DML_CAPABILITIES;

typedef struct _DML_VOICE_SERVICE_CTRL_
{
    TELCOVOICEMGR_DML_VOICESERVICE      dml;
    unsigned char                       updated;
} DML_VOICE_SERVICE_CTRL_T;

typedef struct _DML_VOICE_SERVICE_LIST_
{
    unsigned int                    ulQuantity;
    DML_VOICE_SERVICE_CTRL_T*       pdata[TELCOVOICEMGR_DATA_MAX_VOICE_SERVICES];
} DML_VOICE_SERVICE_LIST_T;


typedef struct _TELCOVOICEMGR_DML_SERVICE
{
    DML_VOICE_SERVICE_LIST_T    VoiceService;
} TELCOVOICEMGR_DML_SERVICE;

typedef struct _TELCOVOICEMGR_DML_DATA
{
    TELCOVOICEMGR_DML_SERVICE  Service;
    pthread_mutex_t            mDataMutex;
} TELCOVOICEMGR_DML_DATA;

typedef enum _TELCOVOICEMGR_PHYINTERFACE_TESTSTATE_ENUM
{
    PHYINTERFACE_TESTSTATE_NONE = 0,
    PHYINTERFACE_TESTSTATE_REQUESTED,
    PHYINTERFACE_TESTSTATE_COMPLETE,
    PHYINTERFACE_TESTSTATE_ERROR_TESTNOTSUPPORTED
} TELCOVOICEMGR_PHYINTERFACE_TESTSTATE_ENUM;

typedef enum _TELCOVOICEMGR_PHYINTERFACE_TESTSELECTOR_ENUM
{
    PHYINTERFACE_TESTSELECTOR_PHONE_CONNECTIVITY_TEST = 0,
    PHYINTERFACE_TESTSELECTOR_HAZARD_POTENTIAL,
    PHYINTERFACE_TESTSELECTOR_FOREIGN_VOLTAGE,
    PHYINTERFACE_TESTSELECTOR_RESISTIVE_FAULTS,
    PHYINTERFACE_TESTSELECTOR_OFF_HOOK,
    PHYINTERFACE_TESTSELECTOR_REN
} TELCOVOICEMGR_PHYINTERFACE_TESTSELECTOR_ENUM;

typedef struct _TELCOVOICEMGR_DML_PHYINTERFACE_TESTS
{
    TELCOVOICEMGR_PHYINTERFACE_TESTSTATE_ENUM       TestState;
    TELCOVOICEMGR_PHYINTERFACE_TESTSELECTOR_ENUM    TestSelector;
    char                                            X_RDK_TestResult[64];
    unsigned char                                   PhoneConnectivity;
} TELCOVOICEMGR_DML_PHYINTERFACE_TESTS,  *PTELCOVOICEMGR_DML_PHYINTERFACE_TESTS;

typedef struct _TELCOVOICEMGR_DML_PHYINTERFACE
{
    unsigned long                            InstanceNumber;
    void*                                    *pParentVoiceService;
    char                                     Alias[64];
    char                                     PhyPort[2];
    unsigned int                             InterfaceID;
    char                                     Description[32];
    TELCOVOICEMGR_DML_PHYINTERFACE_TESTS     PhyInterfaceTestsObj;
} TELCOVOICEMGR_DML_PHYINTERFACE, *PTELCOVOICEMGR_DML_PHYINTERFACE;

typedef struct _DML_PHYINTERFACE_CTRL_
{
    TELCOVOICEMGR_DML_PHYINTERFACE    dml;
    unsigned char                     updated;
} DML_PHYINTERFACE_CTRL_T;

typedef struct _DML_PHYINTERFACE_LIST_
{
    unsigned int                ulQuantity;
    DML_PHYINTERFACE_CTRL_T*    pdata[TELCOVOICEMGR_DATA_MAX_PHYINTERFACE];
} DML_PHYINTERFACE_LIST_T;


#endif



