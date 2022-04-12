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
#ifndef __WIFIHAL_STUB_H__
#define __WIFIHAL_STUB_H__
#include <json/json.h>
#include <unistd.h>
#include <string.h>
#include <dlfcn.h>
#include <stdlib.h>
#include "rdkteststubintf.h"
#include "rdktestagentintf.h"
#include <sys/types.h>
#include <sys/wait.h>
#include <fstream>
#include <sstream>
#include <jsonrpccpp/server/connectors/tcpsocketserver.h>
#define IN
#define OUT
#define TEST_SUCCESS true
#define TEST_FAILURE false

#define     MAX_BSR 32
#define     MAX_RU_ALLOCATIONS  74
#define     MAX_BTM_DEVICES     64
#define MAX_NUM_FREQ_BAND 4
#ifdef WIFI_HAL_VERSION_3
#define MAX_NUM_RADIOS           3
#else
#define MAX_NUM_RADIOS           2
#endif
#define MAXNUMSECONDARYCHANNELS     7
#define MAX_CHANNELS    64
#define MAXIFACENAMESIZE    64
#define MAX_VENDOR_SPECIFIC 32

typedef unsigned int    wifi_radio_index_t;
typedef unsigned int    wifi_vap_index_t;
typedef char    wifi_vap_name_t[64];
typedef struct _wifi_radius_setting_t
{
    int RadiusServerRetries;
    int RadiusServerRequestTimeout;
    int PMKLifetime;
    int PMKCaching;
    int PMKCacheInterval;
    int MaxAuthenticationAttempts;
    int BlacklistTableTimeout;
    int IdentityRequestRetryInterval;
    int QuietPeriodAfterFailedAuthentication;
}wifiRadiusSetting;

typedef struct _wifi_ssidTrafficStats2
{
    unsigned long ssid_BytesSent;
    unsigned long ssid_BytesReceived;
    unsigned long ssid_PacketsSent;
    unsigned long ssid_PacketsReceived;
    unsigned long ssid_RetransCount;
    unsigned long ssid_FailedRetransCount;
    unsigned long ssid_RetryCount;
    unsigned long ssid_MultipleRetryCount;
    unsigned long ssid_ACKFailureCount;
    unsigned long ssid_AggregatedPacketCount;
    unsigned long ssid_ErrorsSent;
    unsigned long ssid_ErrorsReceived;
    unsigned long ssid_UnicastPacketsSent;
    unsigned long ssid_DiscardedPacketsSent;
    unsigned long ssid_UnicastPacketsReceived;
    unsigned long ssid_DiscardedPacketsReceived;
    unsigned long ssid_MulticastPacketsSent;
    unsigned long ssid_MulticastPacketsReceived;
    unsigned long ssid_BroadcastPacketsSent;
    unsigned long ssid_BroadcastPacketsRecevied;
    unsigned long ssid_UnknownPacketsReceived;
}wifi_ssidTrafficStats2_t;

typedef struct _wifi_radioTrafficStats2_t
{
    unsigned long radio_BytesSent;
    unsigned long radio_BytesReceived;
    unsigned long radio_PacketsSent;
    unsigned long radio_ErrorsSent;
    unsigned long radio_PacketsReceived;
    unsigned long radio_ErrorsReceived;
    unsigned long radio_DiscardPacketsSent;
    unsigned long radio_DiscardPacketsReceived;
    unsigned long radio_PLCPErrorCount;
    unsigned long radio_FCSErrorCount;
    unsigned long radio_InvalidMACCount;
    unsigned long radio_PacketsOtherReceived;
    unsigned long radio_NoiseFloor;
    unsigned long radio_ChannelUtilization;
    unsigned long radio_ActivityFactor;
    unsigned long radio_CarrierSenseThreshold_Exceeded;
    unsigned long radio_RetransmissionMetirc;
    unsigned long radio_MaximumNoiseFloorOnChannel;
    unsigned long radio_MinimumNoiseFloorOnChannel;
    unsigned long radio_MedianNoiseFloorOnChannel;
    unsigned long radio_StatisticsStartTime;
}GetRadioTrafficStats2;

typedef struct _wifi_associated_dev
{
    unsigned char cli_MACAddress[6];
    char cli_IPAddress[64];
    int cli_AuthenticationState;
    unsigned int cli_LastDataDownlinkRate;
    unsigned int cli_LastDataUplinkRate;
    int cli_SignalStrength;
    unsigned int cli_Retransmissions;
    int cli_Active;
    char cli_OperatingStandard[64];
    char cli_OperatingChannelBandwidth[64];
    int cli_SNR;
    char cli_InterferenceSources[64];
    unsigned long cli_DataFramesSentAck;
    unsigned long cli_DataFramesSentNoAck;
    unsigned long cli_BytesSent;
    unsigned long cli_BytesReceived;
    int cli_RSSI;
    int cli_MinRSSI;
    int cli_MaxRSSI;
    unsigned int cli_Disassociations;
    unsigned int cli_AuthenticationFailures;
}wifi_associated_dev_t;

typedef struct _wifi_neighbor_ap2
{
    char ap_SSID[64];
    char ap_BSSID[64];
    char ap_Mode[64];
    unsigned int ap_Channel;
    int ap_SignalStrength;
    char ap_SecurityModeEnabled[64];
    char ap_EncryptionMode[64];
    char ap_OperatingFrequencyBand[16];
    char ap_SupportedStandards[64];
    char ap_OperatingStandards[16];
    char ap_OperatingChannelBandwidth[16];
    unsigned int ap_BeaconPeriod;
    int ap_Noise;
    char ap_BasicDataTransferRates[256];
    char ap_SupportedDataTransferRates[256];
    unsigned int ap_DTIMPeriod;
    unsigned int ap_ChannelUtilization;
}wifi_neighbor_ap2_t;
typedef struct _wifi_channelStats {
        int  ch_number;
        int ch_in_pool;
        int  ch_noise;
        int ch_radar_noise;
        int  ch_max_80211_rssi;
        int  ch_non_80211_noise;
        int  ch_utilization;
        unsigned long long ch_utilization_total;
        unsigned long long ch_utilization_busy;
        unsigned long long ch_utilization_busy_tx;
        unsigned long long ch_utilization_busy_rx;
        unsigned long long ch_utilization_busy_self;
        unsigned long long ch_utilization_busy_ext;
} wifi_channelStats_t;

typedef unsigned char mac_address_t[6];

typedef struct _wifi_rssi_snapshot {
        unsigned char  rssi[4];
        unsigned char  time_s[4];
        unsigned short count;
} wifi_rssi_snapshot_t;


typedef struct _wifi_associated_dev_rate_info_tx_stats {
        unsigned char nss;
        unsigned char mcs;
        unsigned short bw;
        unsigned long long flags;
        unsigned long long bytes;
        unsigned long long msdus;
        unsigned long long mpdus;
        unsigned long long ppdus;
        unsigned long long retries;
        unsigned long long attempts;
}wifi_associated_dev_rate_info_tx_stats_t;

typedef enum
{
    WIFI_RADIO_SCAN_MODE_NONE = 0,
    WIFI_RADIO_SCAN_MODE_FULL,
    WIFI_RADIO_SCAN_MODE_ONCHAN,
    WIFI_RADIO_SCAN_MODE_OFFCHAN,
    WIFI_RADIO_SCAN_MODE_SURVEY
} wifi_neighborScanMode_t;

typedef struct _wifi_associated_dev_rate_info_rx_stats {
        unsigned char nss;
        unsigned char mcs;
        unsigned short bw;
        unsigned long long flags;
        unsigned long long bytes;
        unsigned long long msdus;
        unsigned long long mpdus;
        unsigned long long ppdus;
        unsigned long long retries;
        unsigned char rssi_combined;
        unsigned char rssi_array[8][4];
}wifi_associated_dev_rate_info_rx_stats_t;

typedef struct _wifi_associated_dev_stats {
        unsigned long long  cli_rx_bytes;
        unsigned long long  cli_tx_bytes;
        unsigned long long  cli_rx_frames;
        unsigned long long  cli_tx_frames;
        unsigned long long  cli_rx_retries;
        unsigned long long  cli_tx_retries;
        unsigned long long  cli_rx_errors;
        unsigned long long  cli_tx_errors;
        double  cli_rx_rate;
        double  cli_tx_rate;
        wifi_rssi_snapshot_t cli_rssi_bcn;
        wifi_rssi_snapshot_t cli_rssi_ack;
} wifi_associated_dev_stats_t;

typedef struct _wifi_associated_dev2
{
  mac_address_t cli_MACAddress;
  char cli_IPAddress[64];
  bool cli_AuthenticationState;
  unsigned int cli_LastDataDownlinkRate;
  unsigned int cli_LastDataUplinkRate;
  int cli_SignalStrength;
  unsigned int cli_Retransmissions;
  bool cli_Active;
  char cli_OperatingStandard[64];
  char cli_OperatingChannelBandwidth[64];
  int  cli_SNR;
  char cli_InterferenceSources[64];
  unsigned long cli_DataFramesSentAck;
  unsigned long cli_DataFramesSentNoAck;
  unsigned long cli_BytesSent;
  unsigned long cli_BytesReceived;
  int cli_RSSI;
  int cli_MinRSSI;
  int cli_MaxRSSI;
  unsigned int cli_Disassociations;
  unsigned int cli_AuthenticationFailures;
  unsigned long long cli_Associations;
} wifi_associated_dev2_t;

typedef struct {
       unsigned int    wake_time;
    unsigned int    wake_interval;
    unsigned int    min_wake_duration;
    unsigned int    channel;
} wifi_twt_individual_params_t;

typedef struct {
       unsigned int    traget_beacon;
    unsigned int    listen_interval;
} wifi_twt_broadcast_params_t;

typedef enum {
       wifi_twt_agreement_type_individual,
       wifi_twt_agreement_type_broadcast,
} wifi_twt_agreement_type_t;

typedef struct {
       bool    implicit;
       bool    announced;
       bool    trigger_enabled;
} wifi_twt_operation_t;

typedef struct {
       wifi_twt_agreement_type_t       agreement;
       wifi_twt_operation_t    operation;
       union {
               wifi_twt_individual_params_t    individual;
               wifi_twt_broadcast_params_t     broadcast;
       } patams;
} wifi_twt_params_t;

typedef enum {
    WIFI_DL_MU_TYPE_NONE,
    WIFI_DL_MU_TYPE_HE,
    WIFI_DL_MU_TYPE_MIMO,
    WIFI_DL_MU_TYPE_HE_MIMO
} wifi_dl_mu_type_t;

typedef enum {
    wifi_access_category_background,
    wifi_access_category_best_effort,
    wifi_access_category_video,
    wifi_access_category_voice,
} wifi_access_category_t;

typedef struct {
    wifi_access_category_t  access_category;
    unsigned int        queue_size;
} wifi_bsr_t;

typedef enum {
    WIFI_RU_TYPE_26,
    WIFI_RU_TYPE_52,
    WIFI_RU_TYPE_106,
    WIFI_RU_TYPE_242,
    WIFI_RU_TYPE_484,
    WIFI_RU_TYPE_996,
    WIFI_RU_TYPE_1024,
} wifi_ru_type_t;

typedef struct {
    unsigned char   subchannels;
    wifi_ru_type_t  type;
} wifi_ru_allocation_t;

typedef struct {
    wifi_dl_mu_type_t   cli_DownlinkMuType;
    wifi_bsr_t              cli_BufferStatus[MAX_BSR];
    unsigned char           cli_AllocatedDownlinkRuNum;
    wifi_ru_allocation_t    cli_DownlinkRuAllocations[MAX_RU_ALLOCATIONS];
} wifi_dl_mu_stats_t;


typedef enum {
    WIFI_UL_MU_TYPE_NONE,
    WIFI_UL_MU_TYPE_HE,
} wifi_ul_mu_type_t;

typedef struct {
    wifi_ul_mu_type_t   cli_UpinkMuType;
    unsigned char                   cli_ChannelStateInformation;
    wifi_bsr_t              cli_BufferStatus[MAX_BSR];
    unsigned char                   cli_AllocatedUplinkRuNum;
    wifi_ru_allocation_t    cli_UplinkRuAllocations[MAX_RU_ALLOCATIONS];
} wifi_ul_mu_stats_t;

typedef struct _wifi_GASConfiguration_t{   // Values correspond to the dot11GASAdvertisementEntry field definitions; see 802.11-2016 Annex C.3.
    unsigned int AdvertisementID;
    bool PauseForServerResponse;
    unsigned int ResponseTimeout;
    unsigned int ComeBackDelay;
    unsigned int ResponseBufferingTime;
    unsigned int QueryResponseLengthLimit;
} wifi_GASConfiguration_t;

typedef struct _wifi_associated_dev3
{
        mac_address_t cli_MACAddress;
        char  cli_IPAddress[64];
        bool  cli_AuthenticationState;
        unsigned int  cli_LastDataDownlinkRate;
        unsigned int  cli_LastDataUplinkRate;
        int   cli_SignalStrength;
        unsigned int  cli_Retransmissions;
        bool  cli_Active;
        char  cli_OperatingStandard[64];
        char  cli_OperatingChannelBandwidth[64];
        int   cli_SNR;
        char  cli_InterferenceSources[64];
        unsigned long cli_DataFramesSentAck;
        unsigned long cli_DataFramesSentNoAck;
        unsigned long cli_BytesSent;
        unsigned long cli_BytesReceived;
        int   cli_RSSI;
        int   cli_MinRSSI;
        int   cli_MaxRSSI;
        unsigned int  cli_Disassociations;
        unsigned int  cli_AuthenticationFailures;
        unsigned long long   cli_Associations;
        unsigned long cli_PacketsSent;
        unsigned long cli_PacketsReceived;
        unsigned long cli_ErrorsSent;
        unsigned long cli_RetransCount;
        unsigned long cli_FailedRetransCount;
        unsigned long cli_RetryCount;
        unsigned long cli_MultipleRetryCount;
        unsigned int  cli_MaxDownlinkRate;
        unsigned int  cli_MaxUplinkRate;
        wifi_ul_mu_stats_t  cli_DownlinkMuStats;
        wifi_dl_mu_stats_t  cli_UplinkMuStats;
        wifi_twt_params_t      cli_TwtParams;
} wifi_associated_dev3_t;

typedef struct _wifi_channelStats2 {
        unsigned int    ch_Frequency;
        int     ch_NoiseFloor;
        int     ch_Non80211Noise;
        int     ch_Max80211Rssi;
        unsigned int    ch_ObssUtil;
        unsigned int    ch_SelfBssUtil;
} wifi_channelStats2_t;

typedef struct wifi_associated_dev_tid_entry
{
    unsigned char  ac;
    unsigned char  tid;
    unsigned long long ewma_time_ms;
    unsigned long long sum_time_ms;
    unsigned long long num_msdus;
} wifi_associated_dev_tid_entry_t;

typedef struct wifi_associated_dev_tid_stats
{
  wifi_associated_dev_tid_entry_t tid_array[16];
} wifi_associated_dev_tid_stats_t;

typedef struct _wifi_device
{
     unsigned char wifi_devMacAddress[6];
     char wifi_devIPAddress[64];
     int wifi_devAssociatedDeviceAuthentiationState;
     int  wifi_devSignalStrength;
     int  wifi_devTxRate;
     int  wifi_devRxRate;
} wifi_device_t;

typedef struct _wifi_basicTrafficStats
{
     unsigned long wifi_BytesSent;
     unsigned long wifi_BytesReceived;
     unsigned long wifi_PacketsSent;
     unsigned long wifi_PacketsReceived;
     unsigned long wifi_Associations;
} wifi_basicTrafficStats_t;

typedef struct _wifi_trafficStats
{
     unsigned long wifi_ErrorsSent;
     unsigned long wifi_ErrorsReceived;
     unsigned long wifi_UnicastPacketsSent;
     unsigned long wifi_UnicastPacketsReceived;
     unsigned long wifi_DiscardedPacketsSent;
     unsigned long wifi_DiscardedPacketsReceived;
     unsigned long wifi_MulticastPacketsSent;
     unsigned long wifi_MulticastPacketsReceived;
     unsigned long wifi_BroadcastPacketsSent;
     unsigned long wifi_BroadcastPacketsRecevied;
     unsigned long wifi_UnknownPacketsReceived;
} wifi_trafficStats_t;

typedef enum {
    DISCONNECT_TYPE_UNKNOWN                 = 0,    /**< Unknown type               */
    DISCONNECT_TYPE_DISASSOC,                       /**< Disassociation             */
    DISCONNECT_TYPE_DEAUTH                          /**< Deauthentication           */
} wifi_disconnectType_t;

typedef struct {
    unsigned int        rssiProbeHWM;           /**< Probe response RSSI high water mark    */
    unsigned int        rssiProbeLWM;           /**< Probe response RSSI low water mark     */
    unsigned int        rssiAuthHWM;            /**< Auth response RSSI high water mark     */
    unsigned int        rssiAuthLWM;            /**< Auth response RSSI low water mark      */
    unsigned int        rssiInactXing;          /**< Inactive RSSI crossing threshold       */
    unsigned int        rssiHighXing;           /**< High RSSI crossing threshold           */
    unsigned int        rssiLowXing;            /**< Low RSSI crossing threshold            */
    unsigned int        authRejectReason;       /**< Inactive RSSI crossing threshold       */
} wifi_steering_clientConfig_t;

typedef struct {
    unsigned int        entries;                        // Number of entries in each of the following arrays.
    mac_address_t       peer[MAX_BTM_DEVICES];          // Array a peer device MAC addresses.
    unsigned char       capability[MAX_BTM_DEVICES];    // Array of bool indicating peer BSS transition capability.
} wifi_BTMCapabilities_t;

typedef struct {
    unsigned char    wifiRoamingConsortiumCount;
    unsigned char    wifiRoamingConsortiumOui[3][15+1];//only 3 OIS is allowed in beacon and probe responses OIS length is variable between 3-15
    unsigned char    wifiRoamingConsortiumLen[3];
}wifi_roamingConsortiumElement_t;

typedef char mac_addr_str_t[18];

typedef struct _wifi_InterworkingElement_t
{
    bool interworkingEnabled;
    unsigned int accessNetworkType;
    bool internetAvailable;
    bool asra;
    bool esra;
    bool uesa;
    bool venueOptionPresent;
    unsigned char venueType;
    unsigned char venueGroup;
    bool hessOptionPresent;
    mac_addr_str_t hessid;
}wifi_InterworkingElement_t;

typedef enum {
    wifi_data_priority_be,
    wifi_data_priority_bk,
    wifi_data_priority_ee,
    wifi_data_priority_ca,
    wifi_data_priority_vi,
    wifi_data_priority_vo,
    wifi_data_prioirty_ic,
    wifi_data_priority_nc
} wifi_data_priority_t;

typedef struct
{
    unsigned int txOverflow;
} wifi_VAPTelemetry_t;

typedef struct {
    unsigned int    major;
    unsigned int    minor;
} wifi_hal_version_t;

typedef enum {
    wifi_countrycode_AC, /**< ASCENSION ISLAND */
    wifi_countrycode_AD, /**< ANDORRA */
    wifi_countrycode_AE, /**< UNITED ARAB EMIRATES */
    wifi_countrycode_AF, /**< AFGHANISTAN */
    wifi_countrycode_AG, /**< ANTIGUA AND BARBUDA */
    wifi_countrycode_AI, /**< ANGUILLA */
    wifi_countrycode_AL, /**< ALBANIA */
    wifi_countrycode_AM, /**< ARMENIA */
    wifi_countrycode_AN, /**< NETHERLANDS ANTILLES */
    wifi_countrycode_AO, /**< ANGOLA */
    wifi_countrycode_AQ, /**< ANTARCTICA */
    wifi_countrycode_AR, /**< ARGENTINA */
    wifi_countrycode_AS, /**< AMERICAN SAMOA */
    wifi_countrycode_AT, /**< AUSTRIA */
    wifi_countrycode_AU, /**< AUSTRALIA */
    wifi_countrycode_AW, /**< ARUBA */
    wifi_countrycode_AZ, /**< AZERBAIJAN */
    wifi_countrycode_BA, /**< BOSNIA AND HERZEGOVINA */
    wifi_countrycode_BB, /**< BARBADOS */
    wifi_countrycode_BD, /**< BANGLADESH */
    wifi_countrycode_BE, /**< BELGIUM */
    wifi_countrycode_BF, /**< BURKINA FASO */
    wifi_countrycode_BG, /**< BULGARIA */
    wifi_countrycode_BH, /**< BAHRAIN */
    wifi_countrycode_BI, /**< BURUNDI */
    wifi_countrycode_BJ, /**< BENIN */
    wifi_countrycode_BM, /**< BERMUDA */
    wifi_countrycode_BN, /**< BRUNEI DARUSSALAM */
    wifi_countrycode_BO, /**< BOLIVIA */
    wifi_countrycode_BR, /**< BRAZIL */
    wifi_countrycode_BS, /**< BAHAMAS */
    wifi_countrycode_BT, /**< BHUTAN */
    wifi_countrycode_BV, /**< BOUVET ISLAND */
    wifi_countrycode_BW, /**< BOTSWANA */
    wifi_countrycode_BY, /**< BELARUS */
    wifi_countrycode_BZ, /**< BELIZE */
    wifi_countrycode_CA, /**< CANADA */
    wifi_countrycode_CC, /**< COCOS (KEELING) ISLANDS */
    wifi_countrycode_CD, /**< CONGO, THE DEMOCRATIC REPUBLIC OF THE */
    wifi_countrycode_CF, /**< CENTRAL AFRICAN REPUBLIC */
    wifi_countrycode_CG, /**< CONGO */
    wifi_countrycode_CH, /**< SWITZERLAND */
    wifi_countrycode_CI, /**< COTE D'IVOIRE */
    wifi_countrycode_CK, /**< COOK ISLANDS */
    wifi_countrycode_CL, /**< CHILE */
    wifi_countrycode_CM, /**< CAMEROON */
    wifi_countrycode_CN, /**< CHINA */
    wifi_countrycode_CO, /**< COLOMBIA */
    wifi_countrycode_CP, /**< CLIPPERTON ISLAND */
    wifi_countrycode_CR, /**< COSTA RICA */
    wifi_countrycode_CU, /**< CUBA */
    wifi_countrycode_CV, /**< CAPE VERDE */
    wifi_countrycode_CY, /**< CYPRUS */
    wifi_countrycode_CX, /**< CHRISTMAS ISLAND */
    wifi_countrycode_CZ, /**< CZECH REPUBLIC */
    wifi_countrycode_DE, /**< GERMANY */
    wifi_countrycode_DJ, /**< DJIBOUTI */
    wifi_countrycode_DK, /**< DENMARK */
    wifi_countrycode_DM, /**< DOMINICA */
    wifi_countrycode_DO, /**< DOMINICAN REPUBLIC */
    wifi_countrycode_DZ, /**< ALGERIA */
    wifi_countrycode_EC, /**< ECUADOR */
    wifi_countrycode_EE, /**< ESTONIA */
    wifi_countrycode_EG, /**< EGYPT */
    wifi_countrycode_EH, /**< WESTERN SAHARA */
    wifi_countrycode_ER, /**< ERITREA */
    wifi_countrycode_ES, /**< SPAIN */
    wifi_countrycode_ET, /**< ETHIOPIA */
    wifi_countrycode_FI, /**< FINLAND */
    wifi_countrycode_FJ, /**< FIJI */
    wifi_countrycode_FK, /**< FALKLAND ISLANDS (MALVINAS) */
    wifi_countrycode_FM, /**< MICRONESIA, FEDERATED STATES OF */
    wifi_countrycode_FO, /**< FAROE ISLANDS */
    wifi_countrycode_FR, /**< FRANCE */
    wifi_countrycode_GA, /**< GABON */
    wifi_countrycode_GB, /**< UNITED KINGDOM */
    wifi_countrycode_GD, /**< GRENADA */
    wifi_countrycode_GE, /**< GEORGIA */
    wifi_countrycode_GF, /**< FRENCH GUIANA */
    wifi_countrycode_GG, /**< GUERNSEY */
    wifi_countrycode_GH, /**< GHANA */
    wifi_countrycode_GI, /**< GIBRALTAR */
    wifi_countrycode_GL, /**< GREENLAND */
    wifi_countrycode_GM, /**< GAMBIA */
    wifi_countrycode_GN, /**< GUINEA */
    wifi_countrycode_GP, /**< GUADELOUPE */
    wifi_countrycode_GQ, /**< EQUATORIAL GUINEA */
    wifi_countrycode_GR, /**< GREECE */
    wifi_countrycode_GS, /**< SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS */
    wifi_countrycode_GT, /**< GUATEMALA */
    wifi_countrycode_GU, /**< GUAM */
    wifi_countrycode_GW, /**< GUINEA-BISSAU */
    wifi_countrycode_GY, /**< GUYANA */
    wifi_countrycode_HR, /**< CROATIA */
    wifi_countrycode_HT, /**< HAITI */
    wifi_countrycode_HM, /**< HEARD ISLAND AND MCDONALD ISLANDS */
    wifi_countrycode_HN, /**< HONDURAS */
    wifi_countrycode_HK, /**< HONG KONG */
    wifi_countrycode_HU, /**< HUNGARY */
    wifi_countrycode_IS, /**< ICELAND */
    wifi_countrycode_IN, /**< INDIA */
    wifi_countrycode_ID, /**< INDONESIA */
    wifi_countrycode_IR, /**< IRAN, ISLAMIC REPUBLIC OF */
    wifi_countrycode_IQ, /**< IRAQ */
    wifi_countrycode_IE, /**< IRELAND */
    wifi_countrycode_IL, /**< ISRAEL */
    wifi_countrycode_IM, /**< MAN, ISLE OF */
    wifi_countrycode_IT, /**< ITALY */
    wifi_countrycode_IO, /**< BRITISH INDIAN OCEAN TERRITORY */
    wifi_countrycode_JM, /**< JAMAICA */
    wifi_countrycode_JP, /**< JAPAN */
    wifi_countrycode_JE, /**< JERSEY */
    wifi_countrycode_JO, /**< JORDAN */
    wifi_countrycode_KE, /**< KENYA */
    wifi_countrycode_KG, /**< KYRGYZSTAN */
    wifi_countrycode_KH, /**< CAMBODIA */
    wifi_countrycode_KI, /**< KIRIBATI */
    wifi_countrycode_KM, /**< COMOROS */
    wifi_countrycode_KN, /**< SAINT KITTS AND NEVIS */
    wifi_countrycode_KP, /**< KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF */
    wifi_countrycode_KR, /**< KOREA, REPUBLIC OF */
    wifi_countrycode_KW, /**< KUWAIT */
    wifi_countrycode_KY, /**< CAYMAN ISLANDS */
    wifi_countrycode_KZ, /**< KAZAKHSTAN */
    wifi_countrycode_LA, /**< LAO PEOPLE'S DEMOCRATIC REPUBLIC */
    wifi_countrycode_LB, /**< LEBANON */
    wifi_countrycode_LC, /**< SAINT LUCIA */
    wifi_countrycode_LI, /**< LIECHTENSTEIN */
    wifi_countrycode_LK, /**< SRI LANKA */
    wifi_countrycode_LR, /**< LIBERIA */
    wifi_countrycode_LS, /**< LESOTHO */
    wifi_countrycode_LT, /**< LITHUANIA */
    wifi_countrycode_LU, /**< LUXEMBOURG */
    wifi_countrycode_LV, /**< LATVIA */
    wifi_countrycode_LY, /**< LIBYAN ARAB JAMAHIRIYA */
    wifi_countrycode_MA, /**< MOROCCO */
    wifi_countrycode_MC, /**< MONACO */
    wifi_countrycode_MD, /**< MOLDOVA, REPUBLIC OF */
    wifi_countrycode_ME, /**< MONTENEGRO */
    wifi_countrycode_MG, /**< MADAGASCAR */
    wifi_countrycode_MH, /**< MARSHALL ISLANDS */
    wifi_countrycode_MK, /**< MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF */
    wifi_countrycode_ML, /**< MALI */
    wifi_countrycode_MM, /**< MYANMAR */
    wifi_countrycode_MN, /**< MONGOLIA */
    wifi_countrycode_MO, /**< MACAO */
    wifi_countrycode_MQ, /**< MARTINIQUE */
    wifi_countrycode_MR, /**< MAURITANIA */
    wifi_countrycode_MS, /**< MONTSERRAT */
    wifi_countrycode_MT, /**< MALTA */
    wifi_countrycode_MU, /**< MAURITIUS */
    wifi_countrycode_MV, /**< MALDIVES */
    wifi_countrycode_MW, /**< MALAWI */
    wifi_countrycode_MX, /**< MEXICO */
    wifi_countrycode_MY, /**< MALAYSIA */
    wifi_countrycode_MZ, /**< MOZAMBIQUE */
    wifi_countrycode_NA, /**< NAMIBIA */
    wifi_countrycode_NC, /**< NEW CALEDONIA */
    wifi_countrycode_NE, /**< NIGER */
    wifi_countrycode_NF, /**< NORFOLK ISLAND */
    wifi_countrycode_NG, /**< NIGERIA */
    wifi_countrycode_NI, /**< NICARAGUA */
    wifi_countrycode_NL, /**< NETHERLANDS */
    wifi_countrycode_NO, /**< NORWAY */
    wifi_countrycode_NP, /**< NEPAL */
    wifi_countrycode_NR, /**< NAURU */
    wifi_countrycode_NU, /**< NIUE */
    wifi_countrycode_NZ, /**< NEW ZEALAND */
    wifi_countrycode_MP, /**< NORTHERN MARIANA ISLANDS */
    wifi_countrycode_OM, /**< OMAN */
    wifi_countrycode_PA, /**< PANAMA */
    wifi_countrycode_PE, /**< PERU */
    wifi_countrycode_PF, /**< FRENCH POLYNESIA */
    wifi_countrycode_PG, /**< PAPUA NEW GUINEA */
    wifi_countrycode_PH, /**< PHILIPPINES */
    wifi_countrycode_PK, /**< PAKISTAN */
    wifi_countrycode_PL, /**< POLAND */
    wifi_countrycode_PM, /**< SAINT PIERRE AND MIQUELON */
    wifi_countrycode_PN, /**< PITCAIRN */
    wifi_countrycode_PR, /**< PUERTO RICO */
    wifi_countrycode_PS, /**< PALESTINIAN TERRITORY, OCCUPIED */
    wifi_countrycode_PT, /**< PORTUGAL */
    wifi_countrycode_PW, /**< PALAU */
    wifi_countrycode_PY, /**< PARAGUAY */
    wifi_countrycode_QA, /**< QATAR */
    wifi_countrycode_RE, /**< REUNION */
    wifi_countrycode_RO, /**< ROMANIA */
    wifi_countrycode_RS, /**< SERBIA */
    wifi_countrycode_RU, /**< RUSSIAN FEDERATION */
    wifi_countrycode_RW, /**< RWANDA */
    wifi_countrycode_SA, /**< SAUDI ARABIA */
    wifi_countrycode_SB, /**< SOLOMON ISLANDS */
    wifi_countrycode_SD, /**< SUDAN */
    wifi_countrycode_SE, /**< SWEDEN */
    wifi_countrycode_SC, /**< SEYCHELLES */
    wifi_countrycode_SG, /**< SINGAPORE */
    wifi_countrycode_SH, /**< SAINT HELENA */
    wifi_countrycode_SI, /**< SLOVENIA */
    wifi_countrycode_SJ, /**< SVALBARD AND JAN MAYEN */
    wifi_countrycode_SK, /**< SLOVAKIA */
    wifi_countrycode_SL, /**< SIERRA LEONE */
    wifi_countrycode_SM, /**< SAN MARINO */
    wifi_countrycode_SN, /**< SENEGAL */
    wifi_countrycode_SO, /**< SOMALIA */
    wifi_countrycode_SR, /**< SURINAME */
    wifi_countrycode_ST, /**< SAO TOME AND PRINCIPE */
    wifi_countrycode_SV, /**< EL SALVADOR */
    wifi_countrycode_SY, /**< SYRIAN ARAB REPUBLIC */
    wifi_countrycode_SZ, /**< SWAZILAND */
    wifi_countrycode_TA, /**< TRISTAN DA CUNHA */
    wifi_countrycode_TC, /**< TURKS AND CAICOS ISLANDS */
    wifi_countrycode_TD, /**< CHAD */
    wifi_countrycode_TF, /**< FRENCH SOUTHERN TERRITORIES */
    wifi_countrycode_TG, /**< TOGO */
    wifi_countrycode_TH, /**< THAILAND */
    wifi_countrycode_TJ, /**< TAJIKISTAN */
    wifi_countrycode_TK, /**< TOKELAU */
    wifi_countrycode_TL, /**< TIMOR-LESTE (EAST TIMOR) */
    wifi_countrycode_TM, /**< TURKMENISTAN */
    wifi_countrycode_TN, /**< TUNISIA */
    wifi_countrycode_TO, /**< TONGA */
    wifi_countrycode_TR, /**< TURKEY */
    wifi_countrycode_TT, /**< TRINIDAD AND TOBAGO */
    wifi_countrycode_TV, /**< TUVALU */
    wifi_countrycode_TW, /**< TAIWAN, PROVINCE OF CHINA */
    wifi_countrycode_TZ, /**< TANZANIA, UNITED REPUBLIC OF */
    wifi_countrycode_UA, /**< UKRAINE */
    wifi_countrycode_UG, /**< UGANDA */
    wifi_countrycode_UM, /**< UNITED STATES MINOR OUTLYING ISLANDS */
    wifi_countrycode_US, /**< UNITED STATES */
    wifi_countrycode_UY, /**< URUGUAY */
    wifi_countrycode_UZ, /**< UZBEKISTAN */
    wifi_countrycode_VA, /**< HOLY SEE (VATICAN CITY STATE) */
    wifi_countrycode_VC, /**< SAINT VINCENT AND THE GRENADINES */
    wifi_countrycode_VE, /**< VENEZUELA */
    wifi_countrycode_VG, /**< VIRGIN ISLANDS, BRITISH */
    wifi_countrycode_VI, /**< VIRGIN ISLANDS, U.S. */
    wifi_countrycode_VN, /**< VIET NAM */
    wifi_countrycode_VU, /**< VANUATU */
    wifi_countrycode_WF, /**< WALLIS AND FUTUNA */
    wifi_countrycode_WS, /**< SAMOA */
    wifi_countrycode_YE, /**< YEMEN */
    wifi_countrycode_YT, /**< MAYOTTE */
    wifi_countrycode_YU, /**< YUGOSLAVIA */
    wifi_countrycode_ZA, /**< SOUTH AFRICA */
    wifi_countrycode_ZM, /**< ZAMBIA */
    wifi_countrycode_ZW, /**< ZIMBABWE */
    wifi_countrycode_max /**< Max number of country code */
} wifi_countrycode_type_t;

typedef enum{
    WIFI_FREQUENCY_2_4_BAND = 0x1,
    WIFI_FREQUENCY_5_BAND   = 0x2,
    WIFI_FREQUENCY_5L_BAND  = 0x4,
    WIFI_FREQUENCY_5H_BAND  = 0x8,
    WIFI_FREQUENCY_6_BAND   = 0x10,
    WIFI_FREQUENCY_60_BAND  = 0x20
} wifi_freq_bands_t;

typedef struct {
    int num_channels;                  /**< The number of available channels in channels_list. */
    int annels_list[MAX_CHANNELS];   /**< List of channels. */
} wifi_channels_list_t;

typedef enum{
    WIFI_CHANNELBANDWIDTH_20MHZ = 0x1,
    WIFI_CHANNELBANDWIDTH_40MHZ = 0x2,
    WIFI_CHANNELBANDWIDTH_80MHZ = 0x4,
    WIFI_CHANNELBANDWIDTH_160MHZ = 0x8,
    WIFI_CHANNELBANDWIDTH_80_80MHZ = 0x10
} wifi_channelBandwidth_t;

typedef enum {
    WIFI_80211_VARIANT_A = 0x01,
    WIFI_80211_VARIANT_B = 0x02,
    WIFI_80211_VARIANT_G = 0x04,
    WIFI_80211_VARIANT_N = 0x08,
    WIFI_80211_VARIANT_H = 0x10,
    WIFI_80211_VARIANT_AC = 0x20,
    WIFI_80211_VARIANT_AD = 0x40,
    WIFI_80211_VARIANT_AX = 0x80
} wifi_ieee80211Variant_t;

#define MAXNUMBEROFTRANSMIPOWERSUPPORTED 21
typedef struct {
    unsigned int transmitPowerSupported[MAXNUMBEROFTRANSMIPOWERSUPPORTED]; /**< List of transmit power supported. */
    unsigned int numberOfElements;                                         /**< The number of valid elements in transmitPowerSupported. */
} wifi_radio_trasmitPowerSupported_list_t;


typedef enum {
    wifi_guard_interval_400 = 0x01,
    wifi_guard_interval_800 = 0x02,
    wifi_guard_interval_1600 = 0x04,
    wifi_guard_interval_3200 = 0x08,
    wifi_guard_interval_auto = 0x10,
} wifi_guard_interval_t ;

typedef struct {
    bool enable;                                        /**< The radio enable. */
    wifi_freq_bands_t   band;                           /**< the radio frequency band. */
    bool autoChannelEnabled;                            /**< set bAutoChannelEnabled to TRUE to enable Auto Channel. */
    unsigned int channel;                                       /**< The radio primary channel. */
    unsigned int numSecondaryChannels;                          /**< The number odf secondary channels in the list */
    unsigned int channelSecondary[MAXNUMSECONDARYCHANNELS];     /**< The List of secondary radio channel. */
    wifi_channelBandwidth_t channelWidth;               /**< The channel bandwidth. */
    wifi_ieee80211Variant_t variant;                    /**< The radio operating mode */
    unsigned int csa_beacon_count;                              /**< Specifies how long CSA need to be announced. */
    wifi_countrycode_type_t countryCode;                /**< The country code. */
    bool DCSEnabled;                                    /**< set DCSEnabled to TRUE to enable DCS. */
    unsigned int dtimPeriod;                                    /**< The DTIM period. */
    unsigned int beaconInterval;                                /**< The beacon interval. */
    unsigned int operatingClass;                                /**< The Operating class. */
    unsigned int basicDataTransmitRates;                        /**< The basic data transmit rates in Mbps. It uses bitmask to return multiples bitrates and wifi_bitrate_t has the definition of valid values*/
    unsigned int operationalDataTransmitRates;                  /**< The operational data transmit rates in Mbps. It uses bitmask to return multiples bitrates and wifi_bitrate_t has the definition of valid values*/
    unsigned int fragmentationThreshold;                        /**< The fragmentation threshold in bytes. */
    wifi_guard_interval_t guardInterval;               /**< The guard interval. */
    unsigned int transmitPower;                                /**<  The transmit power in percentage, eg "75", "100". */
    unsigned int rtsThreshold;                                 /**< The packet size threshold in bytes to apply RTS/CTS backoff rules. */
    bool factoryResetSsid;
    unsigned int radioStatsMeasuringRate;
    unsigned int radioStatsMeasuringInterval;
    bool ctsProtection;
    bool obssCoex;
    bool stbcEnable;
    bool greenFieldEnable;
    unsigned int userControl;
    unsigned int adminControl;
    unsigned int chanUtilThreshold;
    bool chanUtilSelfHealEnable;
} wifi_radio_operationParam_t;

typedef enum {
    wifi_security_mode_none = 0x00000001,
    wifi_security_mode_wep_64 = 0x00000002,
    wifi_security_mode_wep_128 = 0x00000004,
    wifi_security_mode_wpa_personal = 0x00000008,
    wifi_security_mode_wpa2_personal = 0x00000010,
    wifi_security_mode_wpa_wpa2_personal = 0x00000020,
    wifi_security_mode_wpa_enterprise = 0x00000040,
    wifi_security_mode_wpa2_enterprise = 0x00000080,
    wifi_security_mode_wpa_wpa2_enterprise = 0x00000100,
    wifi_security_mode_wpa3_personal = 0x00000200,
    wifi_security_mode_wpa3_transition = 0x00000400,
    wifi_security_mode_wpa3_enterprise = 0x00000800
} wifi_security_modes_t;

typedef enum {
    wifi_mfp_cfg_disabled,
    wifi_mfp_cfg_optional,
    wifi_mfp_cfg_required,
} wifi_mfp_cfg_t;

typedef enum {
    wifi_encryption_none,
    wifi_encryption_tkip = 1,
    wifi_encryption_aes,
    wifi_encryption_aes_tkip,
} wifi_encryption_method_t;

typedef enum {
    wifi_ip_family_ipv4,
    wifi_ip_family_ipv6
} wifi_ip_family_t;

typedef struct {
    wifi_ip_family_t family;
    union { /* network byte ordered */
        unsigned int   IPv4addr;           /* 32-bit IPv4 address */
        unsigned char  IPv6addr[16];       /* 128-bit IPv6 address */
    } u;
}ip_addr_t;

typedef struct {
#ifdef WIFI_HAL_VERSION_3_PHASE2
    ip_addr_t       ip;                 /**< The primary RADIUS server IP address. */
#else
    unsigned char   ip[45];
#endif
    unsigned short  port;               /**< The primary RADIUS server port. */
    char            key[64];            /**< The primary secret. */
#ifdef WIFI_HAL_VERSION_3_PHASE2
    ip_addr_t       s_ip;                 /**< The secondary RADIUS server IP address. */
#else
    unsigned char   s_ip[45];
#endif
    unsigned short  s_port;             /**< The secondary RADIUS server port. */
    char            s_key[64];          /**< The secondary secret. */
    ip_addr_t       dasip;
    unsigned short          dasport;
    char            daskey[64];
    unsigned int            max_auth_attempts;
    unsigned int            blacklist_table_timeout;
    unsigned int            identity_req_retry_interval;
    unsigned int            server_retries;
} wifi_radius_settings_t;

typedef enum {
    wifi_security_key_type_psk,
    wifi_security_key_type_pass,
    wifi_security_key_type_sae,
    wifi_security_key_type_psk_sae
} wifi_security_key_type_t;

typedef struct {
    wifi_security_key_type_t type;
    char    key[256];
} wifi_security_key_t;

typedef struct {
    wifi_security_modes_t   mode;
    wifi_encryption_method_t    encr;
#if defined(WIFI_HAL_VERSION_3)
    wifi_mfp_cfg_t  mfp;
#else
    char    mfpConfig[32];
#endif
    bool  wpa3_transition_disable;
    unsigned int  rekey_interval;
    bool  strict_rekey;  // must be set for enterprise VAPs
    unsigned int  eapol_key_timeout;
    unsigned int  eapol_key_retries;
    unsigned int  eap_identity_req_timeout;
    unsigned int  eap_identity_req_retries;
    unsigned int  eap_req_timeout;
    unsigned int  eap_req_retries;
    bool  disable_pmksa_caching;
    union {
        wifi_radius_settings_t  radius;
        wifi_security_key_t key;
    } u;
} __attribute__((packed)) wifi_vap_security_t;

typedef struct {
     unsigned short capabilityList[64];
}__attribute__((packed)) wifi_capabilityListANQP_t;

typedef struct {
    unsigned char    length;
    unsigned char    language[3];
    unsigned char    name[256];
}__attribute__((packed)) wifi_venueName_t;

typedef struct {
    unsigned char            venueGroup;
    unsigned char            venueType;
    wifi_venueName_t venueNameTuples[16];
}__attribute__((packed)) wifi_venueNameElement_t;

typedef struct {
    unsigned char length;
    unsigned char oui[15];
}__attribute__((packed)) wifi_ouiDuple_t;

typedef struct {
    unsigned char   field_format;
}__attribute__((packed)) wifi_ipAddressAvailabality_t;

typedef struct {
    unsigned char  id;
    unsigned char   length;
    unsigned char   val[16];
}__attribute__((packed)) wifi_authMethod_t;

typedef struct {
    unsigned char   length;
    unsigned char   method;
    unsigned char   auth_param_count;
    wifi_authMethod_t   auth_method[16];
}__attribute__((packed)) wifi_eapMethod_t;

typedef struct {
    unsigned short            data_field_length;
    unsigned char             encoding;
    unsigned char             realm_length;
    unsigned char             realm[256];
    unsigned char             eap_method_count;
    wifi_eapMethod_t  eap_method[16];
} __attribute__((packed))wifi_naiRealm_t;

typedef struct {
    wifi_ouiDuple_t ouiDuple[32];
}__attribute__((packed)) wifi_roamingConsortium_t;

typedef struct {
    unsigned short  nai_realm_count;
    wifi_naiRealm_t nai_realm_tuples[20];
}__attribute__((packed)) wifi_naiRealmElement_t;

typedef struct {
    unsigned char   PLMN[3];
}__attribute__((packed)) wifi_plmn_t;

typedef struct {
    unsigned char   iei;//copy zero for now.
    unsigned char   plmn_length;
    unsigned char number_of_plmns;
    wifi_plmn_t plmn[16];
}__attribute__((packed))wifi_3gpp_plmn_list_information_element_t;

typedef struct {
    unsigned char   gud;
    unsigned char   uhdLength;//Length of remaining fields
    wifi_3gpp_plmn_list_information_element_t plmn_information;
}__attribute__((packed)) wifi_3gppCellularNetwork_t;

typedef struct {
    unsigned char length;
    unsigned char domainName[255]; //max domain name allowed based on the spec.
}__attribute__((packed)) wifi_domainNameTuple_t;

typedef struct {
    wifi_domainNameTuple_t  domainNameTuple[4];
}__attribute__((packed)) wifi_domainName_t;

typedef struct {
    int capabilityInfoLength;
    wifi_capabilityListANQP_t capabilityInfo;
    int venueInfoLength;
    wifi_venueNameElement_t venueInfo;
    int roamInfoLength;
    wifi_roamingConsortium_t roamInfo;
    wifi_ipAddressAvailabality_t ipAddressInfo;
    int realmInfoLength;
    wifi_naiRealmElement_t realmInfo;
    int gppInfoLength;
    wifi_3gppCellularNetwork_t gppInfo;
    int domainInfoLength;
    wifi_domainName_t domainNameInfo;
    unsigned char  passpointStats[1024];
    unsigned int   domainRespCount;
    unsigned int   realmRespCount;
    unsigned int   gppRespCount;
    unsigned int   domainFailedCount;
    unsigned int   realmFailedCount;
    unsigned int   gppFailedCount;
    unsigned char  anqpParameters[4096];
} __attribute__((packed)) wifi_anqp_settings_t;

typedef struct
{
    unsigned char capabilityList[64];
} __attribute__((packed)) wifi_HS2_CapabilityList_t;

typedef struct _wifi_HS2_OperatorNameDuple_t // figure 9-595
{
    unsigned char length; //length is 3(language code)+number of octects in operator name field  eg. operatorName= aaaa length is 4+3 = 7
    unsigned char languageCode[3];
    unsigned char operatorName[252]; //based on spec the maximum length of operator name is 252
} __attribute__((packed)) wifi_HS2_OperatorNameDuple_t;

typedef struct
{
    wifi_HS2_OperatorNameDuple_t operatorNameDuple[16]; //putting 16 duples supported for now story RDKB-1317 does not tell how many duples we are supporting nor the spec (spec mentions n duples)
} __attribute__((packed)) wifi_HS2_OperatorFriendlyName_t;

typedef struct // figure 9-595
{
    unsigned char ipProtocol;
    unsigned short portNumber;
    unsigned char  status;
} __attribute__((packed)) wifi_HS2_Proto_Port_Tuple_t;

typedef struct // figure 9-595
{
    wifi_HS2_Proto_Port_Tuple_t protoPortTuple[16];//putting 16 duples supported for now. story RDKB-1317 does not tell how many duples we are supporting nor the spec (spec mentions n duples)
} __attribute__((packed)) wifi_HS2_ConnectionCapability_t;

typedef struct// figure 9-595
{
    unsigned char encoding;
    unsigned char length;
    unsigned char name[255];//per spec maximum length is 255
} __attribute__((packed)) wifi_HS2_NAI_Home_Realm_Data_t;

typedef struct// figure 9-595
{
    unsigned char realmCount;
    wifi_HS2_NAI_Home_Realm_Data_t homeRealmData[20];//as realm count is unsigned char we can put 255 realms here spec says n story does not define how many we support
} __attribute__((packed)) wifi_HS2_NAI_Home_Realm_Query_t;

typedef struct // figure 9-595
{
    unsigned char  wanInfo;
    unsigned int  downLinkSpeed;
    unsigned char upLinkSpeed;
    unsigned char downLinkLoad;
    unsigned char  upLinkLoad;
    unsigned short lmd;
} __attribute__((packed)) wifi_HS2_WANMetrics_t;

typedef struct {
    bool        enable;
    bool        gafDisable;
    bool        p2pDisable;
    bool        l2tif;
    bool        bssLoad;
    bool        countryIE;
    bool        proxyArp;

    int capabilityInfoLength;                           //should not be implemented in the hal
    wifi_HS2_CapabilityList_t capabilityInfo;           //should not be implemented in the hal
    int opFriendlyNameInfoLength;                       //should not be implemented in the hal
    wifi_HS2_OperatorFriendlyName_t opFriendlyNameInfo; //should not be implemented in the hal
    int connCapabilityLength;                           //should not be implemented in the hal
    wifi_HS2_ConnectionCapability_t connCapabilityInfo; //should not be implemented in the hal
    int realmInfoLength;                                //should not be implemented in the hal
    wifi_HS2_NAI_Home_Realm_Query_t realmInfo;          //should not be implemented in the hal
    wifi_HS2_WANMetrics_t wanMetricsInfo;               //should not be implemented in the hal
    unsigned char hs2Parameters[4096];                          //should not be implemented in the hal
} __attribute__((packed)) wifi_passpoint_settings_t;

typedef struct {
    wifi_InterworkingElement_t   interworking;
    wifi_roamingConsortiumElement_t roamingConsortium;
    wifi_anqp_settings_t        anqp;                   //should not be implemented in the hal
    wifi_passpoint_settings_t   passpoint;
} __attribute__((packed)) wifi_interworking_t;

#define MAX_NUM_VAP_PER_RADIO    8
#define WIFI_AP_MAX_SSID_LEN    33

typedef enum {
    wifi_mac_filter_mode_black_list,
    wifi_mac_filter_mode_white_list,
} wifi_mac_filter_mode_t;

typedef enum{
    WIFI_ONBOARDINGMETHODS_USBFLASHDRIVE = 0x0001,
    WIFI_ONBOARDINGMETHODS_ETHERNET = 0x0002,
    WIFI_ONBOARDINGMETHODS_LABEL = 0x0004,
    WIFI_ONBOARDINGMETHODS_DISPLAY = 0x0008,
    WIFI_ONBOARDINGMETHODS_EXTERNALNFCTOKEN = 0x0010,
    WIFI_ONBOARDINGMETHODS_INTEGRATEDNFCTOKEN = 0x0020,
    WIFI_ONBOARDINGMETHODS_NFCINTERFACE = 0x0040,
    WIFI_ONBOARDINGMETHODS_PUSHBUTTON = 0x0080,
    WIFI_ONBOARDINGMETHODS_PIN = 0x0100,
    WIFI_ONBOARDINGMETHODS_PHYSICALPUSHBUTTON = 0x0200,
    WIFI_ONBOARDINGMETHODS_PHYSICALDISPLAY = 0x0400,
    WIFI_ONBOARDINGMETHODS_VIRTUALPUSHBUTTON = 0x0800,
    WIFI_ONBOARDINGMETHODS_VIRTUALDISPLAY = 0x1000,
    WIFI_ONBOARDINGMETHODS_EASYCONNECT = 0x2000,
} wifi_onboarding_methods_t;

#define WIFI_AP_MAX_WPSPIN_LEN  9
typedef struct
{
    bool enable;
    wifi_onboarding_methods_t methods;
    char pin[WIFI_AP_MAX_WPSPIN_LEN];
}__attribute__((packed)) wifi_wps_t;

typedef enum {
    WIFI_BITRATE_DEFAULT = 0x0001,      /* WIFI_BITRATE_DEFAULT is used in the set api to default the bitrate configuration */
    WIFI_BITRATE_1MBPS   = 0x0002,
    WIFI_BITRATE_2MBPS   = 0x0004,
    WIFI_BITRATE_5_5MBPS = 0x0008,
    WIFI_BITRATE_6MBPS   = 0x0010,
    WIFI_BITRATE_9MBPS   = 0x0020,
    WIFI_BITRATE_11MBPS  = 0x0040,
    WIFI_BITRATE_12MBPS  = 0x0080,
    WIFI_BITRATE_18MBPS  = 0x0100,
    WIFI_BITRATE_24MBPS  = 0x0200,
    WIFI_BITRATE_36MBPS  = 0x0400,
    WIFI_BITRATE_48MBPS  = 0x0800,
    WIFI_BITRATE_54MBPS  = 0x1000
} wifi_bitrate_t;

typedef mac_address_t   bssid_t;

typedef struct {
    char    ssid[WIFI_AP_MAX_SSID_LEN];
    bool    enabled;
    bool    showSsid;
    bool    isolation;
    int     mgmtPowerControl;
    unsigned int    bssMaxSta;
    bool    bssTransitionActivated;
    bool    nbrReportActivated;
    bool    rapidReconnectEnable;       //should not be implemented in the hal
    unsigned int    rapidReconnThreshold;       //should not be implemented in the hal
    bool    vapStatsEnable;             //should not be implemented in the hal
    wifi_vap_security_t security;
    wifi_interworking_t interworking;
    bool    mac_filter_enable;
    wifi_mac_filter_mode_t mac_filter_mode;
    bool    sec_changed;                //should not be implemented in the hal
    wifi_wps_t   wps;
    bool    wmm_enabled;
    bool    UAPSDEnabled;
    wifi_bitrate_t beaconRate;
    mac_address_t bssid;                    /**< The BSSID. This variable should only be used in the get API. It can't used to change the interface MAC */
    unsigned int   wmmNoAck;
    unsigned int   wepKeyLength;
    bool   bssHotspot;
    unsigned int   wpsPushButton;
    char   beaconRateCtl[32];
} wifi_front_haul_bss_t;

typedef struct {

} __attribute__((packed)) wifi_back_haul_sta_t;

#define WIFI_BRIDGE_NAME_LEN  32

typedef struct {
    wifi_vap_index_t    vap_index;
    wifi_vap_name_t     vap_name;
    wifi_radio_index_t  radio_index;
    char  bridge_name[WIFI_BRIDGE_NAME_LEN];
    union {
        wifi_front_haul_bss_t   bss_info;
        wifi_back_haul_sta_t    sta_info;
    } u;
} __attribute__((packed)) wifi_vap_info_t;

typedef struct {
    unsigned int        num_vaps;
    wifi_vap_info_t vap_array[MAX_NUM_VAP_PER_RADIO];
} __attribute__((packed)) wifi_vap_info_map_t;

typedef struct {
    unsigned short              offset;
    unsigned short              interval;
} wifi_TSFInfo_t;

typedef struct {
    char                        condensedStr[3];
} wifi_CondensedCountryString_t;

typedef struct {
    unsigned char               preference;
} wifi_BSSTransitionCandidatePreference_t;

typedef struct {
    unsigned long               tsf;
    unsigned short              duration;
} wifi_BTMTerminationDuration_t;

typedef struct {
    unsigned short              bearing;
    unsigned int                dist;
    unsigned short              height;
} wifi_Bearing_t;

typedef struct {
    unsigned char               bandwidth;
    unsigned char               centerSeg0;
    unsigned char               centerSeg1;
} wifi_WideBWChannel_t;

typedef struct {

    unsigned short               info;
    unsigned char                ampduParams;
    unsigned char                mcs[16];
    unsigned short               extended;
    unsigned int                 txBeamCaps;
    unsigned char                aselCaps;
} wifi_HTCapabilities_t;

typedef struct {
    unsigned int                  info;
    unsigned short                mcs;
    unsigned short                rxHighestSupportedRate;
    unsigned short                txVHTmcs;
    unsigned short                txHighestSupportedRate;
} wifi_VHTCapabilities_t;

typedef struct {
    unsigned char                 primary;
    unsigned char                 opInfo[5];
    unsigned char                 mcs[16];
} wifi_HTOperation_t;

typedef struct {
    wifi_WideBWChannel_t          opInfo;
    unsigned short                mcs_nss;
} wifi_VHTOperation_t;

typedef struct {
    unsigned char                 secondaryChOffset;
} wifi_SecondaryChannelOffset_t;

typedef struct {
    unsigned char                 capabilities[5];
} wifi_RMEnabledCapabilities_t;

typedef struct {
    unsigned char                 oui[5];
    unsigned char                 buff[MAX_VENDOR_SPECIFIC];
} wifi_VendorSpecific_t;

typedef struct {
    unsigned char                 pilot;
    wifi_VendorSpecific_t vendorSpecific;
} wifi_MeasurementPilotTransmission_t;

typedef struct {
    bssid_t                                         bssid;
    unsigned int                                    info;
    unsigned char                                   opClass;
    unsigned char                                   channel;
    unsigned char                                   phyTable;
    bool                                            tsfPresent;
    wifi_TSFInfo_t                                  tsfInfo;
    bool                                            condensedCountrySringPresent;
    wifi_CondensedCountryString_t                   condensedCountryStr;
    bool                                            bssTransitionCandidatePreferencePresent;
    wifi_BSSTransitionCandidatePreference_t         bssTransitionCandidatePreference;
    bool                                            btmTerminationDurationPresent;
    wifi_BTMTerminationDuration_t                   btmTerminationDuration;
    bool                                            bearingPresent;
    wifi_Bearing_t                                  bearing;
    bool                                            wideBandWidthChannelPresent;
    wifi_WideBWChannel_t                            wideBandwidthChannel;
    bool                                            htCapsPresent;
    wifi_HTCapabilities_t                           htCaps;
    bool                                            vhtCapsPresent;
    wifi_VHTCapabilities_t                          vbhtCaps;
    bool                                            htOpPresent;
    wifi_HTOperation_t                              htOp;
    bool                                            vhtOpPresent;
    wifi_VHTOperation_t                             vhtOp;
    bool                                            secondaryChannelOffsetPresent;
    wifi_SecondaryChannelOffset_t                   secondaryChannelOffset;
    bool                                            rmEnabledCapsPresent;
    wifi_RMEnabledCapabilities_t                    rmEnabledCaps;
    bool                                            msmtPilotTransmissionPresent;
    wifi_MeasurementPilotTransmission_t             msmtPilotTransmission;
    bool                                            vendorSpecificPresent;
    wifi_VendorSpecific_t                           vendorSpecific;
    bssid_t                                         target_ssid;
} wifi_NeighborReport_t;

typedef struct {
    bool rtsThresholdSupported;                                 /**< if bRtsThresholdSupported is TRUE, packet size threshold to apply RTS/CTS backoff rules is supported. */
    wifi_security_modes_t securityModesSupported;               /**< The security modes supported (uses bitmask to return multiples modes). */
    wifi_onboarding_methods_t methodsSupported;                 /**< The on boarding methods supported (uses bitmask to return multiples values). */
    bool WMMSupported;                                          /**< if bWMMSupported is TRUE, WiFi Multimedia (WMM) Access Categories (AC) is supported. */
    bool UAPSDSupported;                                        /**< if bUAPSDSupported is TRUE, WMM Unscheduled Automatic Power Save Delivery (U-APSD) is supported. */
    bool interworkingServiceSupported;                          /**< if bInterworkingServiceSupported is TRUE, indicates whether the access point supports interworking with external networks. */
    bool BSSTransitionImplemented;                              /**< if BSSTransitionImplemented is TRUE, BTM implemented. */
} wifi_ap_capabilities_t;

#define MAX_KEY_HOLDERS 8

typedef char            nas_id_t[49];
typedef unsigned char   r0r1_key_t[16];
typedef char            r0r1_key_str_t[33];

typedef enum {
    FT_SUPPORT_DISABLED,
    FT_SUPPORT_FULL,
    FT_SUPPORT_ADAPTIVE
} wifi_fastTrasitionSupport_t;

typedef struct {
    mac_address_t   mac;
    nas_id_t        nasId;
    r0r1_key_t      key;
} wifi_r0KH_t;

typedef struct {
    mac_address_t   mac;
    mac_address_t   r1khId;
    r0r1_key_t      key;
} wifi_r1KH_t;

typedef struct {
    wifi_fastTrasitionSupport_t support;
    unsigned short              mobilityDomain;
    bool                        overDS;
    nas_id_t                    r0KeyHolder;
    unsigned short              r0KeyLifeTime;
    mac_address_t               r1KeyHolder;
    unsigned short              reassocDeadLine;
    bool                        pmkR1Push;
    unsigned char               numR0KHs;
    wifi_r0KH_t                 r0KH[MAX_KEY_HOLDERS];
    unsigned char               numR1KHs;
    wifi_r1KH_t                 r1KH[MAX_KEY_HOLDERS];
} wifi_FastTransitionConfig_t;

/* To provide external linkage to C Functions defined in TDKB Component folder */
extern "C"
{
    int ssp_wifi_init();
    int ssp_WIFIHALApplySettings(int radioIndex, char* methodName);
    int ssp_WIFIHALGetOrSetParamBoolValue(int radioIndex, unsigned char *output, char* method);
    int ssp_WIFIHALGetOrSetParamULongValue(int radioIndex, unsigned long *uLongVar, char* methodName);
    int ssp_WIFIHALGetOrSetParamStringValue(int radioIndex, char *output, char* methodName);
    int ssp_WIFIHALGetOrSetRadioStandard(int radioIndex, char* output, char* method, unsigned char *gOnly, unsigned char *nOnly, unsigned char *acOnly);
    int ssp_WIFIHALGetOrSetParamIntValue(int radioIndex, int *output, char* methodName);
    int ssp_WIFIHALGetOrSetParamUIntValue(int radioIndex, unsigned int *output, char* methodName);
    int ssp_WIFIHALGetIndexFromName(char* ssidName, int *output);
    int ssp_WIFIHALGetApIndexFromName(char* ssidName, int *output);
    int ssp_WIFIHALClearRadioResetCount();
    int ssp_WIFIHALReset();
    int ssp_WIFIHALDown();
    int ssp_WIFIHALGetOrSetSecurityRadiusServer(int radioIndex, char* IPAddress, unsigned int* port, char* RadiusSecret, char* method);
    int ssp_WIFIHALGetOrSetApBridgeInfo(int radioIndex, char* bridgeName, char* IP, char* subnet, char* method);
    int ssp_WIFIHALGetOrSetRadioDCSScanTime(int radioIndex, int* output_interval_seconds,int* output_dwell_milliseconds, char* methodName);
    int ssp_WIFIHALAddorDelApAclDevice(int apIndex, char* DeviceMacAddress, char* method);
    int ssp_WIFIHALIfConfigUporDown(int apIndex, char* method);
    int ssp_WIFIHALParamRadioIndex(int radioIndex, char* method);
    int ssp_WIFIHALStartorStopHostApd(char* method);
    int ssp_WIFIHALFactoryReset(char* method);
    int ssp_WIFIHALGetOrSetSecurityRadiusSettings(int radioIndex, wifiRadiusSetting *radiusSetting, char* method);
    int ssp_WIFIHALGetSSIDTrafficStats2(int radioIndex,  wifi_ssidTrafficStats2_t *ssidTrafficStats2);
    int ssp_WIFIHALGetRadioTrafficStats2(int radioIndex, GetRadioTrafficStats2 *TrafficStats2);
    int ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult(int radioIndex, wifi_associated_dev_t **associated_dev, unsigned int *output_array_size);
    int ssp_WIFIHALCreateInitialConfigFiles();
    int ssp_WIFIHALGetNeighboringWiFiDiagnosticResult2(int radioIndex, wifi_neighbor_ap2_t **neighbor_ap2, unsigned int *output_array_size);
    int ssp_WIFIHALPushRadioChannel2(int radioIndex, unsigned int channel,unsigned int channel_width_MHz,unsigned int csa_beacon_count);
    int ssp_WIFIHALGetNeighboringWiFiStatus(int radioIndex, wifi_neighbor_ap2_t **neighbor_ap2, unsigned int *output_array_size);
    int ssp_WIFIHALGetRadioChannelStats(int radioIndex,  wifi_channelStats_t *channelStats, int array_size);
    int ssp_WIFIHALParamApIndex(int apIndex, char* method);
    int ssp_WIFIHALGetApAssociatedDevice(int apIndex, char* associated_dev , unsigned int output_array_size);
    int ssp_WIFIHALGetApDeviceRSSI(int ap_index, char *MAC, int *output_RSSI, char* method);
    int ssp_WIFIHAL_CreateAp(int apIndex, int radioIndex, char *essid, unsigned char hideSsid);
    int ssp_WIFIHALDelApAclDevices(int apIndex);
    int ssp_WIFIHALGetApAclDevices(int apIndex, char *mac_addr, unsigned int output_array_size);
    int ssp_WIFIHALStartNeighborScan(int apIndex, wifi_neighborScanMode_t scan_mode, int dwell_time, unsigned int chan_num, unsigned int* chan_list);
    int ssp_WIFIHALGetRadioChannelStats2(int radioIndex, wifi_channelStats2_t *outputChannelStats2);
    int ssp_WIFIHALGetApDeviceTxRxRate(int apIndex, char *MAC, int *output_TxRxMb, char* method);
    int ssp_WIFIHALSetApScanFilter(int apIndex, int mode, char* essid, char *method);
    int ssp_WIFIHALGetApAssociatedDeviceTxStatsResult(int radioIndex, mac_address_t *clientMacAddress, wifi_associated_dev_rate_info_tx_stats_t **stats_array, unsigned int *output_array_size, unsigned long long *handle);
    int ssp_WIFIHALGetApAssociatedDeviceRxStatsResult(int radioIndex, mac_address_t *clientMacAddress, wifi_associated_dev_rate_info_rx_stats_t **stats_array, unsigned int *output_array_size, unsigned long long *handle);
    int ssp_WIFIHALGetApAssociatedDeviceStats(int apIndex, mac_address_t *clientMacAddress, wifi_associated_dev_stats_t *associated_dev_stats, unsigned long long *handle);
    int ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult3(int apIndex, wifi_associated_dev3_t **associated_dev_array, unsigned int *output_array_size);
    int ssp_WIFIHALGetApAssociatedDeviceTidStatsResult(int  radioIndex,  mac_address_t *clientMacAddress, wifi_associated_dev_tid_stats_t *tid_stats,  unsigned long long *handle);
    int ssp_WIFIHALGetBandSteeringLog(int  record_index, unsigned long *pSteeringTime, char *pClientMAC, int *pSourceSSIDIndex, int *pDestSSIDIndex, int *pSteeringReason);
    int ssp_WIFIHALGetApAssociatedDeviceDiagnosticResult2(int apIndex, wifi_associated_dev2_t **associated_dev_array, unsigned int *dev_cnt);
    int ssp_WIFIHALGetRadioMode(int radioIndex, char* output_string, unsigned int *puremode);
    int ssp_WIFIHALSetRadioMode(int radioIndex, char* output_string, unsigned int puremode);
    int ssp_WIFIHALGetAssociatedDeviceDetail(int apIndex, int devIndex, wifi_device_t *dev);
    int ssp_WIFIHALGetBasicTrafficStats(int apIndex, wifi_basicTrafficStats_t *output_struct);
    int ssp_WIFIHALGetWifiTrafficStats(int apIndex, wifi_trafficStats_t *output_struct);
    int ssp_WIFIHALSteeringClientDisconnect(unsigned int steeringgroupIndex, int apIndex, mac_address_t client_mac, wifi_disconnectType_t type, unsigned int reason);
    int ssp_WIFIHALSteeringClientSet(unsigned int steeringgroupIndex, int apIndex, mac_address_t client_mac, wifi_steering_clientConfig_t *cli_cfg);
    int ssp_WIFIHALSteeringClientRemove(unsigned int steeringgroupIndex, int apIndex, mac_address_t client_mac);
    int ssp_WIFIHALGetBTMClientCapabilityList(int apIndex, wifi_BTMCapabilities_t* btm_caps);
    int ssp_WIFIHALGetApRoamingConsortiumElement(int apIndex, wifi_roamingConsortiumElement_t* roam);
    int ssp_WIFIHALPushApRoamingConsortiumElement(int apIndex, wifi_roamingConsortiumElement_t* roam);
    int ssp_WIFIHALGetBSSColorValue(int radioIndex, unsigned char *color);
    int ssp_WIFIHALApplyGASConfiguration(wifi_GASConfiguration_t *GASConfiguration);
    int ssp_WIFIHALGetApInterworkingElement(int radioIndex, wifi_InterworkingElement_t *element);
    int ssp_WIFIHALPushApInterworkingElement(int radioIndex, wifi_InterworkingElement_t *element);
    int ssp_WIFIHALEnableCSIEngine(int apIndex, mac_address_t sta, unsigned char * enable);
    int ssp_WIFIHALSendDataFrame(int apIndex, mac_address_t sta, unsigned char * data, unsigned int length, unsigned char * insert_llc, unsigned int protocol, wifi_data_priority_t prio);
    int ssp_WIFIHALGetVAPTelemetry(int apIndex, wifi_VAPTelemetry_t *VAPTelemetry);
    int ssp_WIFIHALGetRadioVapInfoMap(wifi_radio_index_t radioIndex ,wifi_vap_info_map_t *map);
    int ssp_WIFIHALSetNeighborReports(unsigned int apIndex, unsigned int reports, wifi_NeighborReport_t *neighborReports);
    int ssp_WIFIHALGetApAssociatedClientDiagnosticResult(int apIndex, char * mac_addr, wifi_associated_dev3_t *dev_conn);
    int ssp_WIFIHALGetAPCapabilities(int apIndex, wifi_ap_capabilities_t *apCapabilities, char * output_string);
    int ssp_WIFIHALGetAvailableBSSColor(int radio_index, int maxNumberColors, unsigned char* colorList, int *numColorReturned);
    int ssp_WIFIHALGetOrSetFTMobilityDomainID(int apIndex, unsigned char mobilityDomain[2], char * method);
    int ssp_WIFIHALGetOrSetFTR0KeyHolderID(int apIndex, unsigned char * KeyHolderID, char * method);
    int ssp_WIFIHALGetRMCapabilities(mac_address_t peer, unsigned char out_Capabilities[5]);
    int ssp_WIFIHALGetApSecurity(int apIndex, wifi_vap_security_t * security, char * output_string);
    int ssp_WIFIHALSetApSecurity(int apIndex, wifi_vap_security_t * security);
    int ssp_WIFIHALGetApWpsConfiguration(int apIndex, wifi_wps_t * wpsConfig, char * output_string);
    int ssp_WIFIHALSetApWpsConfiguration(int apIndex, wifi_wps_t * wpsConfig);
    int ssp_WIFIHALGetOrSetFTR1KeyHolderID(int apIndex, unsigned char * KeyHolderID, char * method);
    int ssp_WIFIHALSetBSSColor(int radio_index, unsigned char color);
    int ssp_WIFIHALPushApFastTransitionConfig(int apIndex, wifi_FastTransitionConfig_t * ftCfg);
};

class RDKTestAgent;
class WIFIHAL : public RDKTestStubInterface, public AbstractServer<WIFIHAL>
{
    public:
	 WIFIHAL(TcpSocketServer &ptrRpcServer) : AbstractServer <WIFIHAL>(ptrRpcServer)
                {
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetParamBoolValue", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER,"param", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetParamBoolValue);
		  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetParamULongValue", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER,"param", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetParamULongValue);
		  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetParamStringValue", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "param", JSON_STRING, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetParamStringValue);
		  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetRadioStandard", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "param", JSON_STRING, "paramType",  JSON_STRING, "gOnly",JSON_INTEGER, "nOnly",JSON_INTEGER, "acOnly",JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetOrSetRadioStandard);
		  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetParamIntValue", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "param", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetParamIntValue);
	 	  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetParamUIntValue", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "param", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetParamUIntValue);
		  this->bindAndAddMethod(Procedure("WIFIHAL_GetIndexFromName", PARAMS_BY_NAME, JSON_STRING, "param", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetIndexFromName);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetApIndexFromName", PARAMS_BY_NAME, JSON_STRING, "param", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetApIndexFromName);

		  this->bindAndAddMethod(Procedure("WIFIHAL_ClearRadioResetCount", PARAMS_BY_NAME, JSON_STRING, NULL), &WIFIHAL::WIFIHAL_ClearRadioResetCount);
                  this->bindAndAddMethod(Procedure("WIFIHAL_Reset", PARAMS_BY_NAME, JSON_STRING, NULL), &WIFIHAL::WIFIHAL_Reset);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetSecurityRadiusServer", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "port", JSON_INTEGER, "IPAddress", JSON_STRING, "RadiusSecret", JSON_STRING, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetSecurityRadiusServer);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetApBridgeInfo", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "bridgeName", JSON_STRING, "IP", JSON_STRING, "subnet", JSON_STRING, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetApBridgeInfo);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetRadioDCSScanTime", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "output_interval_seconds", JSON_INTEGER, "output_dwell_milliseconds", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetOrSetRadioDCSScanTime);
                  this->bindAndAddMethod(Procedure("WIFIHAL_AddorDelApAclDevice", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"apIndex", JSON_INTEGER, "DeviceMacAddress", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_AddorDelApAclDevice);
                  this->bindAndAddMethod(Procedure("WIFIHAL_IfConfigUporDown", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"apIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_IfConfigUporDown);
                  this->bindAndAddMethod(Procedure("WIFIHAL_ParamRadioIndex", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,"radioIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_ParamRadioIndex);
                  this->bindAndAddMethod(Procedure("WIFIHAL_StartorStopHostApd", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_StartorStopHostApd);
                  this->bindAndAddMethod(Procedure("WIFIHAL_FactoryReset", PARAMS_BY_NAME, JSON_STRING,"methodName", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_FactoryReset);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetSecurityRadiusSettings",PARAMS_BY_NAME, JSON_STRING, "methodName", JSON_STRING,"radioIndex", JSON_INTEGER, "RadiusServerRetries", JSON_INTEGER, "RadiusServerRequestTimeout", JSON_INTEGER, "PMKLifetime", JSON_INTEGER, "PMKCaching", JSON_INTEGER, "PMKCacheInterval", JSON_INTEGER, "MaxAuthenticationAttempts", JSON_INTEGER, "BlacklistTableTimeout", JSON_INTEGER, "IdentityRequestRetryInterval", JSON_INTEGER, "QuietPeriodAfterFailedAuthentication", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetOrSetSecurityRadiusSettings);
		  this->bindAndAddMethod(Procedure("WIFIHAL_GetSSIDTrafficStats2",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetSSIDTrafficStats2);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioTrafficStats2",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetRadioTrafficStats2);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceDiagnosticResult",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult);
                  this->bindAndAddMethod(Procedure("WIFIHAL_Down", PARAMS_BY_NAME, JSON_STRING, NULL), &WIFIHAL::WIFIHAL_Down);
                  this->bindAndAddMethod(Procedure("WIFIHAL_Init", PARAMS_BY_NAME, JSON_STRING, NULL), &WIFIHAL::WIFIHAL_Init);
                  this->bindAndAddMethod(Procedure("WIFIHAL_CreateInitialConfigFiles", PARAMS_BY_NAME, JSON_STRING, NULL), &WIFIHAL::WIFIHAL_CreateInitialConfigFiles);
		  this->bindAndAddMethod(Procedure("WIFIHAL_GetNeighboringWiFiDiagnosticResult2",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetNeighboringWiFiDiagnosticResult2);
		  this->bindAndAddMethod(Procedure("WIFIHAL_PushRadioChannel2",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER, "channel",JSON_INTEGER, "channel_width_MHz",JSON_INTEGER, "csa_beacon_count",JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_PushRadioChannel2);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetNeighboringWiFiStatus",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetNeighboringWiFiStatus);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioChannelStats",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetRadioChannelStats);
		  this->bindAndAddMethod(Procedure("WIFIHAL_ParamApIndex", PARAMS_BY_NAME, JSON_STRING, "methodName", JSON_STRING, "apIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_ParamApIndex);
		  this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDevice", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDevice);
		  this->bindAndAddMethod(Procedure("WIFIHAL_GetApDeviceRSSI", PARAMS_BY_NAME, JSON_STRING, "methodName", JSON_STRING, "apIndex", JSON_INTEGER, "MAC", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetApDeviceRSSI);
                  this->bindAndAddMethod(Procedure("WIFIHAL_DelApAclDevices", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_DelApAclDevices);
                 this->bindAndAddMethod(Procedure("WIFIHAL_GetApAclDevices", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetApAclDevices);
                  this->bindAndAddMethod(Procedure("WIFIHAL_CreateAp", PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "radioIndex", JSON_INTEGER, "essid", JSON_STRING, "hideSsid", JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_CreateAp);

                 this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceStats",PARAMS_BY_NAME, JSON_STRING, "apIndex",JSON_INTEGER, "MAC", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceStats);

                  this->bindAndAddMethod(Procedure("WIFIHAL_StartNeighborScan", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER,"scan_mode", JSON_INTEGER,"dwell_time", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_StartNeighborScan);
                 this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceTxStatsResult",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER, "MAC", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceTxStatsResult);
                 this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceRxStatsResult",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER, "MAC", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceRxStatsResult);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetApDeviceTxRxRate", PARAMS_BY_NAME, JSON_STRING, "methodName", JSON_STRING, "apIndex", JSON_INTEGER, "MAC", JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetApDeviceTxRxRate);
                  this->bindAndAddMethod(Procedure("WIFIHAL_SetApScanFilter", PARAMS_BY_NAME, JSON_STRING, "methodName", JSON_STRING, "apIndex", JSON_INTEGER, "essid", JSON_STRING,"mode", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SetApScanFilter);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceDiagnosticResult3",PARAMS_BY_NAME, JSON_STRING, "apIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult3);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioChannelStats2",PARAMS_BY_NAME, JSON_STRING, "radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetRadioChannelStats2);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceTidStatsResult",PARAMS_BY_NAME,JSON_STRING,"radioIndex",JSON_INTEGER,"MAC",JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceTidStatsResult);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetBandSteeringLog",PARAMS_BY_NAME,JSON_STRING,"record_index",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetBandSteeringLog);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedDeviceDiagnosticResult2",PARAMS_BY_NAME,JSON_STRING,"apIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetApAssociatedDeviceDiagnosticResult2);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioMode",PARAMS_BY_NAME,JSON_STRING,"radioIndex",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_GetRadioMode);
                  this->bindAndAddMethod(Procedure("WIFIHAL_SetRadioMode",PARAMS_BY_NAME,JSON_STRING,"radioIndex",JSON_INTEGER,"chnmode",JSON_STRING,"puremode",JSON_INTEGER,NULL), &WIFIHAL::WIFIHAL_SetRadioMode);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetAssociatedDeviceDetail", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER, "devIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetAssociatedDeviceDetail);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetBasicTrafficStats", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetBasicTrafficStats);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetWifiTrafficStats", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetWifiTrafficStats);
                  this->bindAndAddMethod(Procedure("WIFIHAL_SteeringClientDisconnect", PARAMS_BY_NAME, JSON_STRING, "steeringgroupIndex", JSON_INTEGER, "apIndex", JSON_INTEGER, "clientMAC", JSON_STRING, "disconnectType", JSON_INTEGER, "reason", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SteeringClientDisconnect);
                  this->bindAndAddMethod(Procedure("WIFIHAL_SteeringClientSet", PARAMS_BY_NAME, JSON_STRING, "steeringgroupIndex", JSON_INTEGER, "apIndex", JSON_INTEGER, "clientMAC", JSON_STRING, "rssiProbeHWM", JSON_INTEGER, "rssiProbeLWM", JSON_INTEGER, "rssiAuthHWM", JSON_INTEGER, "rssiAuthLWM", JSON_INTEGER, "rssiInactXing", JSON_INTEGER, "rssiHighXing", JSON_INTEGER, "rssiLowXing", JSON_INTEGER, "authRejectReason", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SteeringClientSet);
                  this->bindAndAddMethod(Procedure("WIFIHAL_SteeringClientRemove", PARAMS_BY_NAME, JSON_STRING, "steeringgroupIndex", JSON_INTEGER, "apIndex", JSON_INTEGER, "clientMAC", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_SteeringClientRemove);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetBTMClientCapabilityList", PARAMS_BY_NAME, JSON_STRING, "count", JSON_INTEGER, "apIndex", JSON_INTEGER, "clientMAC", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetBTMClientCapabilityList);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetApRoamingConsortiumElement", PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetApRoamingConsortiumElement);
                  this->bindAndAddMethod(Procedure("WIFIHAL_PushApRoamingConsortiumElement", PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "ouiCount", JSON_INTEGER, "ouiList", JSON_STRING, "ouiLen", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_PushApRoamingConsortiumElement);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetBSSColorValue", PARAMS_BY_NAME, JSON_STRING,"radioIndex", JSON_INTEGER, "paramType",  JSON_STRING,NULL), &WIFIHAL::WIFIHAL_GetBSSColorValue);
                  this->bindAndAddMethod(Procedure("WIFIHAL_ApplyGASConfiguration",PARAMS_BY_NAME, JSON_STRING, "advertisementID", JSON_INTEGER, "pauseForServerResponse", JSON_INTEGER, "responseTimeout", JSON_INTEGER, "comeBackDelay", JSON_INTEGER, "responseBufferingTime", JSON_INTEGER, "queryResponseLengthLimit", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_ApplyGASConfiguration);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetApInterworkingElement", PARAMS_BY_NAME, JSON_STRING,"radioIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetApInterworkingElement);
                  this->bindAndAddMethod(Procedure("WIFIHAL_PushApInterworkingElement",PARAMS_BY_NAME, JSON_STRING, "radioIndex", JSON_INTEGER, "interworkingEnabled", JSON_INTEGER, "accessNetworkType", JSON_INTEGER, "internetAvailable", JSON_INTEGER, "asra", JSON_INTEGER, "esra", JSON_INTEGER, "uesa", JSON_INTEGER, "venueOptionPresent", JSON_INTEGER, "venueType", JSON_INTEGER, "venueGroup", JSON_INTEGER, "hessOptionPresent", JSON_INTEGER, "hessid", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_PushApInterworkingElement);
                  this->bindAndAddMethod(Procedure("WIFIHAL_EnableCSIEngine",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "MacAddress", JSON_STRING, "enable", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_EnableCSIEngine);
                  this->bindAndAddMethod(Procedure("WIFIHAL_SendDataFrame",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "MacAddress", JSON_STRING, "length", JSON_INTEGER, "insert_llc", JSON_INTEGER, "protocol", JSON_INTEGER, "priority", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SendDataFrame);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetVAPTelemetry", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetVAPTelemetry);
		  this->bindAndAddMethod(Procedure("WIFIHAL_GetRadioVapInfoMap", PARAMS_BY_NAME, JSON_STRING,"apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetRadioVapInfoMap);
                  this->bindAndAddMethod(Procedure("WIFIHAL_SetNeighborReports",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "reports", JSON_INTEGER, "bssid", JSON_STRING, "info", JSON_INTEGER, "opClass", JSON_INTEGER, "channel", JSON_INTEGER, "phyTable", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SetNeighborReports);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetApAssociatedClientDiagnosticResult",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "mac_addr", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetApAssociatedClientDiagnosticResult);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetAPCapabilities",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetAPCapabilities);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetAvailableBSSColor",PARAMS_BY_NAME, JSON_STRING, "radioIndex", JSON_INTEGER, "maxNumberColors", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetAvailableBSSColor);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetFTMobilityDomainID",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "radioIndex", JSON_INTEGER, "mobilityDomain", JSON_INTEGER, "methodName", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetOrSetFTMobilityDomainID);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetFTR0KeyHolderID",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "radioIndex", JSON_INTEGER, "KeyHolderID", JSON_STRING, "methodName", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetOrSetFTR0KeyHolderID);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetRMCapabilities",PARAMS_BY_NAME, JSON_STRING, "peer", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetRMCapabilities);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetApSecurity",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetApSecurity);
                  this->bindAndAddMethod(Procedure("WIFIHAL_SetApSecurity",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "mode", JSON_INTEGER, "mfp", JSON_INTEGER, "encr", JSON_INTEGER, "key_type", JSON_INTEGER, "key", JSON_STRING, "wpa3_transition_disable", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SetApSecurity);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetApWpsConfiguration",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_GetApWpsConfiguration);
                  this->bindAndAddMethod(Procedure("WIFIHAL_SetApWpsConfiguration",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "radioIndex", JSON_INTEGER, "enable", JSON_INTEGER, "pin", JSON_STRING, "methods", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SetApWpsConfiguration);
                  this->bindAndAddMethod(Procedure("WIFIHAL_GetOrSetFTR1KeyHolderID",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "radioIndex", JSON_INTEGER, "KeyHolderID", JSON_STRING, "methodName", JSON_STRING, NULL), &WIFIHAL::WIFIHAL_GetOrSetFTR1KeyHolderID);
                  this->bindAndAddMethod(Procedure("WIFIHAL_SetBSSColor",PARAMS_BY_NAME, JSON_STRING, "radioIndex", JSON_INTEGER, "color", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_SetBSSColor);
                  this->bindAndAddMethod(Procedure("WIFIHAL_PushApFastTransitionConfig",PARAMS_BY_NAME, JSON_STRING, "apIndex", JSON_INTEGER, "support", JSON_INTEGER, "mobilityDomain", JSON_INTEGER, "overDS", JSON_INTEGER, "radioIndex", JSON_INTEGER, NULL), &WIFIHAL::WIFIHAL_PushApFastTransitionConfig);
		}
        /*inherited functions*/
        bool initialize(IN const char* szVersion);
        bool cleanup(IN const char* szVersion);
        std::string testmodulepre_requisites();
        bool testmodulepost_requisites();

        /*WIFIHAL Stub Wrapper functions*/
        void WIFIHAL_GetOrSetParamULongValue(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetParamBoolValue(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetParamStringValue(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_GetOrSetRadioStandard(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetParamIntValue(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetParamUIntValue(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_GetIndexFromName(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApIndexFromName(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_ClearRadioResetCount(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_Reset(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_GetOrSetSecurityRadiusServer(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_GetOrSetApBridgeInfo(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetRadioDCSScanTime(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_AddorDelApAclDevice(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_IfConfigUporDown(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_ParamRadioIndex(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_StartorStopHostApd(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_FactoryReset(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetSecurityRadiusSettings(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_GetSSIDTrafficStats2(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRadioTrafficStats2(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_Down(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_Init(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_CreateInitialConfigFiles(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceDiagnosticResult(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_GetNeighboringWiFiDiagnosticResult2(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_PushRadioChannel2(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetNeighboringWiFiStatus(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRadioChannelStats(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_ParamApIndex(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_GetApAssociatedDevice(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_GetApDeviceRSSI(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_DelApAclDevices(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAclDevices(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRadioChannelStats2 (IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceTxStatsResult(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceRxStatsResult(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApDeviceTxRxRate(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceStats(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetApScanFilter(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_CreateAp(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceDiagnosticResult3(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_StartNeighborScan(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceTidStatsResult(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetBandSteeringLog(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedDeviceDiagnosticResult2(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRadioMode(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetRadioMode(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetAssociatedDeviceDetail(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetBasicTrafficStats(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetWifiTrafficStats(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SteeringClientDisconnect(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SteeringClientSet(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SteeringClientRemove(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetBTMClientCapabilityList(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApRoamingConsortiumElement(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_PushApRoamingConsortiumElement(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetBSSColorValue(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_ApplyGASConfiguration(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApInterworkingElement(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_PushApInterworkingElement(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_EnableCSIEngine(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SendDataFrame(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetVAPTelemetry(IN const Json::Value& req, OUT Json::Value& response);
	void WIFIHAL_GetRadioVapInfoMap(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetNeighborReports(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApAssociatedClientDiagnosticResult(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetAPCapabilities(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetAvailableBSSColor(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetFTMobilityDomainID(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetFTR0KeyHolderID(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetRMCapabilities(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApSecurity(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetApSecurity(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetApWpsConfiguration(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetApWpsConfiguration(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_GetOrSetFTR1KeyHolderID(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_SetBSSColor(IN const Json::Value& req, OUT Json::Value& response);
        void WIFIHAL_PushApFastTransitionConfig(IN const Json::Value& req, OUT Json::Value& response);
};
#endif //__WIFIHAL_STUB_H__



