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

#ifndef __SSP_TDK_WRP_H__
#define __SSP_TDK_WRP_H__

#define	MAX_ATTRIBUTE_SIZE	100

#ifndef MAX_PARAM_SIZE
#define MAX_PARAM_SIZE		200
#endif

#define MAX_PARAMS_COMP		100
#define MAX_COMP_ARRAY		20
#define MAX_PARAM_NAMES_ARRAY   1000

#define SSP_TDK_SUCCESS     0
#define SSP_TDK_FAILURE     -1
#define SSP_SUCCESS       0
#define SSP_FAILURE       1

#define  DIAG_CFG_REF_STRING_LENGTH  256
#ifdef IFNAMSIZ
 #undef IFNAMSIZ
#endif
#define  IFNAMSIZ  50
#define PING_DEF_COUNT        3
#define PING_DEF_TIMEO       1
#define PING_DEF_BSIZE       56

#ifndef ANSC_IPV4_ADDRESS
#define  ANSC_IPV4_ADDRESS                             \
         union                                         \
         {                                             \
            unsigned char                   Dot[4];    \
            unsigned long                   Value;     \
         }
#endif

#ifndef MTA_HAL_SHORT_VALUE_LEN
#define  MTA_HAL_SHORT_VALUE_LEN   16
#endif
enum
{
    SSP_STOP = 0,
    SSP_START
};

typedef struct GetNames_Struct
{
    char *pParamNames;
    bool writable;
}GETPARAMNAMES;

typedef struct GetValues_Struct
{
    char *pParamNames;
    char *pParamValues;
    int pParamType;
}GETPARAMVALUES;

typedef struct GetAttr_Struct
{
    char *pParamNames;
    char *pParamAccess;
    char *pParamNotify;

}GETPARAMATTR;
typedef struct _Config
{
        unsigned long InstanceNumber;
        char Alias[20];
        int bEnabled;
        char Interface[20];
        int PassthroughEnable;
        char PassthroughDHCPPool;
}CFG;

typedef struct _Info
{
         unsigned long Status;
         unsigned long DHCPStatus;
         char IPAddress;
         char SubnetMask;
         int NumIPRouters;
         int NumDnsServers;
}INFO;

typedef struct _Poolcfg
{
       unsigned long InstanceNumber;
       char Alias[20];
       int bEnabled;
       char Interface[20];
       int Order;
       int VendorClassIDExclude;
       int ClientIDExclude;
       int ChaddrExclude;
       int UserClassIDExclude;
       int DNSServersEnabled;
       int LeaseTime;
}POOLCFG;

typedef struct _Dns
{
        unsigned long InstanceNumber;
        char Alias[20];
        int bEnabled;
        char Interface[20];
}DNS;

typedef struct cfg {
    /* common configs */
    char        host[257];
    char        ifname[IFNAMSIZ];
    /* DH  Diag We have to be comptible with TR-181 -- it is not wise to do the opposite.*/
    char        Interface[DIAG_CFG_REF_STRING_LENGTH+1];
    unsigned    cnt;
    unsigned    timo;
    unsigned    size;
    unsigned    tos;
    unsigned    maxhop; /* trace route only */
} diag_cfg;

typedef struct _Docsis
{
        char version[64];
        char ConfigFileName[64];
        char DownstreamDataRate[64];
        char UpstreamDataRate[64];
}DOCSIS;

typedef struct _DsChannel
{
       char Frequency[64];
       char Modulation[64];
       char SNRLevel[64];
       char LockStatus[64];
       unsigned long ChannelID;
}DS_CHANNEL;

typedef struct _UsChannel
{
        char Frequency[64];
}US_CHANNEL;

typedef struct _Ipv6Dhcp
{
       char IPv6BootFileName[64];
       char IPv6Address[40];
}IPV6DHCP;

typedef struct _Ipv4Dhcp
{
       char BootFileName[64];
       ANSC_IPV4_ADDRESS IPAddress[40];
}IPV4DHCP;

typedef  struct
MTA_SERVICE_FLOW
{
    unsigned long                   SFID;
    char                            ServiceClassName[256];
    char                            Direction[16];
    unsigned long                   ScheduleType;
    bool                            DefaultFlow;
    unsigned long                   NomGrantInterval;
    unsigned long                   UnsolicitGrantSize;
    unsigned long                   TolGrantJitter;
    unsigned long                   NomPollInterval;
    unsigned long                   MinReservedPkt;
    unsigned long                   MaxTrafficRate;
    unsigned long                   MinReservedRate;
    unsigned long                   MaxTrafficBurst;
    char                            TrafficType[64];
    unsigned long                   NumberOfPackets;
}
MTA_SERVICE_FLOW, *PMTA_SERVICE_FLOW;

typedef  struct
MTA_DSXLOG
{
    char                            Time[64];
    char                            Description[128];
    unsigned long                   ID;
    unsigned long                   Level;
}
MTA_DSXLOG,  *PMTA_DSXLOG;

typedef  struct
DML_MTALOG_FULL
{
    unsigned long                   Index;
    unsigned long                   EventID;
    char                            EventLevel[64];
    char                            Time[64];
    char *                          pDescription;
}
DML_MTALOG_FULL,  *PDML_MTALOG_FULL;

typedef  struct
MTA_CALLS
{
    char                            Codec[64];
    char                            RemoteCodec[64];
    char                            CallStartTime[64];
    char                            CallEndTime[64];
    char                            CWErrorRate[MTA_HAL_SHORT_VALUE_LEN];
    char                            PktLossConcealment[MTA_HAL_SHORT_VALUE_LEN];
    bool                            JitterBufferAdaptive;
    bool                            Originator;
    ANSC_IPV4_ADDRESS               RemoteIPAddress;
    unsigned long                   CallDuration;
    char                            CWErrors[MTA_HAL_SHORT_VALUE_LEN];                     /* code word errors on this channel */
    char                            SNR[MTA_HAL_SHORT_VALUE_LEN];                          /* signal to noise ratio * 256 */
    char                            MicroReflections[MTA_HAL_SHORT_VALUE_LEN];             /* return loss measurement */
    char                            DownstreamPower[MTA_HAL_SHORT_VALUE_LEN];              /* downstream power in dbmv */
    char                            UpstreamPower[MTA_HAL_SHORT_VALUE_LEN];                /* upstream power in dbmv */
    char                            EQIAverage[MTA_HAL_SHORT_VALUE_LEN];                   /* EQI average */
    char                            EQIMinimum[MTA_HAL_SHORT_VALUE_LEN];                   /* EQI minimum */
    char                            EQIMaximum[MTA_HAL_SHORT_VALUE_LEN];                   /* EQI maximum */
    char                            EQIInstantaneous[MTA_HAL_SHORT_VALUE_LEN];             /* EQI instantaneous */
    char                            MOS_LQ[MTA_HAL_SHORT_VALUE_LEN];                       /* mean opinion score of listening quality, 10-50 */
    char                            MOS_CQ[MTA_HAL_SHORT_VALUE_LEN];                       /* mean opinion score of conversational quality, 10-50 */
    char                            EchoReturnLoss[MTA_HAL_SHORT_VALUE_LEN];               /* residual echo return loss, in db */
    char                            SignalLevel[MTA_HAL_SHORT_VALUE_LEN];                  /* voice signal relative level, in db */
    char                            NoiseLevel[MTA_HAL_SHORT_VALUE_LEN];                   /* noise relative level, in db */
    char                            LossRate[MTA_HAL_SHORT_VALUE_LEN];                     /* fraction of RTP data packet loss * 256 */
    char                            DiscardRate[MTA_HAL_SHORT_VALUE_LEN];                  /* fraction of RTP data packet discarded * 256 */
    char                            BurstDensity[MTA_HAL_SHORT_VALUE_LEN];                 /* fraction of bursting data packet * 256 */
    char                            GapDensity[MTA_HAL_SHORT_VALUE_LEN];                   /* fraction of packets within inter-burst gap * 256 */
    char                            BurstDuration[MTA_HAL_SHORT_VALUE_LEN];                /* mean duration of bursts, in milliseconds */
    char                            GapDuration[MTA_HAL_SHORT_VALUE_LEN];                  /* mean duration of gaps, in milliseconds */
    char                            RoundTripDelay[MTA_HAL_SHORT_VALUE_LEN];               /* most recent measured RTD, in milliseconds */
    char                            Gmin[MTA_HAL_SHORT_VALUE_LEN];                         /* local gap threshold */
    char                            RFactor[MTA_HAL_SHORT_VALUE_LEN];                      /* voice quality evaluation for this RTP session */
    char                            ExternalRFactor[MTA_HAL_SHORT_VALUE_LEN];              /* voice quality evaluation for segment on network external to this RTP session */
    char                            JitterBufRate[MTA_HAL_SHORT_VALUE_LEN];                /* adjustment rate of jitter buffer, in milliseconds */
    char                            JBNominalDelay[MTA_HAL_SHORT_VALUE_LEN];               /* nominal jitter buffer length, in milliseconds */
    char                            JBMaxDelay[MTA_HAL_SHORT_VALUE_LEN];                   /* maximum jitter buffer length, in milliseconds */
    char                            JBAbsMaxDelay[MTA_HAL_SHORT_VALUE_LEN];                /* absolute maximum delay, in milliseconds */
    char                            TxPackets[MTA_HAL_SHORT_VALUE_LEN];                    /* count of transmitted packets */
    char                            TxOctets[MTA_HAL_SHORT_VALUE_LEN];                     /* count of transmitted octet packets */
    char                            RxPackets[MTA_HAL_SHORT_VALUE_LEN];                    /* count of received packets */
    char                            RxOctets[MTA_HAL_SHORT_VALUE_LEN];                     /* count of received octet packets */
    char                            PacketLoss[MTA_HAL_SHORT_VALUE_LEN];                   /* count of lost packets */
    char                            IntervalJitter[MTA_HAL_SHORT_VALUE_LEN];               /* stat variance of packet interarrival time, in milliseconds */
    char                            RemoteIntervalJitter[MTA_HAL_SHORT_VALUE_LEN];         /* remote sie IntervalJitter (see local side) */
    char                            RemoteMOS_LQ[MTA_HAL_SHORT_VALUE_LEN];                 /* remote side MOS_LQ (see local side) */
    char                            RemoteMOS_CQ[MTA_HAL_SHORT_VALUE_LEN];                 /* remote side MOS_CQ (see local side) */
    char                            RemoteEchoReturnLoss[MTA_HAL_SHORT_VALUE_LEN];         /* remote side EchoReturnLoss (see local side) */
    char                            RemoteSignalLevel[MTA_HAL_SHORT_VALUE_LEN];            /* remote side SignalLevel (see local side) */
    char                            RemoteNoiseLevel[MTA_HAL_SHORT_VALUE_LEN];             /* remote side NoiseLevel (see local side) */
    char                            RemoteLossRate[MTA_HAL_SHORT_VALUE_LEN];               /* remote side LossRate (see local side) */
    char                            RemotePktLossConcealment[MTA_HAL_SHORT_VALUE_LEN];     /* remote side PktLossConcealment (see local side) */
    char                            RemoteDiscardRate[MTA_HAL_SHORT_VALUE_LEN];            /* remote side DiscardRate (see local side) */
    char                            RemoteBurstDensity[MTA_HAL_SHORT_VALUE_LEN];           /* remote side BurstDensity (see local side) */
    char                            RemoteGapDensity[MTA_HAL_SHORT_VALUE_LEN];             /* remote side GapDensity (see local side) */
    char                            RemoteBurstDuration[MTA_HAL_SHORT_VALUE_LEN];          /* remote side BurstDuration (see local side) */
    char                            RemoteGapDuration[MTA_HAL_SHORT_VALUE_LEN];            /* remote side GapDuration (see local side) */
    char                            RemoteRoundTripDelay[MTA_HAL_SHORT_VALUE_LEN];         /* remote side RoundTripDelay (see local side) */
    char                            RemoteGmin[MTA_HAL_SHORT_VALUE_LEN];                   /* remote side Gmin (see local side) */
    char                            RemoteRFactor[MTA_HAL_SHORT_VALUE_LEN];                /* remote side RFactore (see local side) */
    char                            RemoteExternalRFactor[MTA_HAL_SHORT_VALUE_LEN];        /* remote side ExternalRFactor (see local side) */
    bool                            RemoteJitterBufferAdaptive;           /* remote side JitterBufferAdaptive (see local side) */
    char                            RemoteJitterBufRate[MTA_HAL_SHORT_VALUE_LEN];          /* remote side JitterBufRate (see local side) */
    char                            RemoteJBNominalDelay[MTA_HAL_SHORT_VALUE_LEN];         /* remote side JBNominalDelay (see local side) */
    char                            RemoteJBMaxDelay[MTA_HAL_SHORT_VALUE_LEN];             /* remote side JBMaxDelay (see local side) */
    char                            RemoteJBAbsMaxDelay[MTA_HAL_SHORT_VALUE_LEN];          /* remote side JBAbsMaxDelay (see local side) */
}
MTA_CALLS, *PMTA_CALLS;

typedef  struct
MTA_HANDSETS_INFO
{
    unsigned long                   InstanceNumber;
    bool                            Status;
    char                            LastActiveTime[64];
    char                            HandsetName[64];
    char                            HandsetFirmware[64];
    char                            OperatingTN[64];
    char                            SupportedTN[64];
}
MTA_HANDSETS_INFO, *PMTA_HANDSETS_INFO;

int CcspBaseIf_getHealth(void* bus_handle, const char* dst_component_id, char* dbus_path, int *health);

#endif
