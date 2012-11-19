# −*− coding: UTF−8 −*−
#/**
# * Software Name : libmich 
# * Version : 0.2.2
# *
# * Copyright © 2011. Benoit Michau. France Telecom.
# *
# * This program is free software: you can redistribute it and/or modify
# * it under the terms of the GNU General Public License version 2 as published
# * by the Free Software Foundation. 
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# * GNU General Public License for more details. 
# *
# * You will find a copy of the terms and conditions of the GNU General Public
# * License version 2 in the "license.txt" file or
# * see http://www.gnu.org/licenses/ or write to the Free Software Foundation,
# * Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
# *
# *--------------------------------------------------------
# * File Name : formats/L3Mobile.py
# * Created : 2011-08-28 
# * Authors : Benoit Michau 
# *--------------------------------------------------------
#*/ 

#!/usr/bin/env python

from libmich.core.element import RawLayer, Block, show, debug, \
    log, ERR, WNG, DBG
from L3Mobile_MM import *
from L3Mobile_CC import *
from L3GSM_RR import *
from L3Mobile_PS_MM import *
from L3Mobile_PS_SM import *
from L3Mobile_IE import *
from L3Mobile_24007 import PD_dict

# Handles commonly all defined L3Mobile_XYZ stacks

L3Call = {
# L3Mobile_CC, PD=3
3:{
    1:ALERTING,
    2:CALL_PROCEEDING,
    3:PROGRESS,
    4:CC_ESTABLISHMENT,
    5:SETUP,
    6:CC_ESTABLISHMENT_CONFIRMED,
    7:CONNECT,
    8:CALL_CONFIRMED,
    9:START_CC,
    11:RECALL,
    14:EMERGENCY_SETUP,
    15:CONNECT_ACKNOWLEDGE,
    16:USER_INFORMATION,
    19:MODIFY_REJECT,
    23:MODIFY,
    24:HOLD,
    25:HOLD_ACKNOWLEDGE,
    26:HOLD_REJECT,
    28:RETRIEVE,
    29:RETRIEVE_ACKNOWLEDGE,
    30:RETRIEVE_REJECT,
    31:MODIFY_COMPLETE,
    37:DISCONNECT,
    42:RELEASE_COMPLETE,
    45:RELEASE,
    49:STOP_DTMF,
    50:STOP_DTMF_ACKNOWLEDGE,
    52:STATUS_ENQUIRY,
    53:START_DTMF,
    54:START_DTMF_ACKNOWLEDGE,
    55:START_DTMF_REJECT,
    57:CONGESTION_CONTROL,
    58:FACILITY,
    61:STATUS,
    62:NOTIFY,
    },
# L3Mobile_MM, PD=5
5:{
    1:IMSI_DETACH_INDICATION,
    2:LOCATION_UPDATING_ACCEPT,
    4:LOCATION_UPDATING_REJECT,
    8:LOCATION_UPDATING_REQUEST,
    17:AUTHENTICATION_REJECT,
    18:AUTHENTICATION_REQUEST,
    20:AUTHENTICATION_RESPONSE,
    24:IDENTITY_REQUEST,
    25:IDENTITY_RESPONSE,
    26:TMSI_REALLOCATION_COMMAND,
    27:TMSI_REALLOCATION_COMPLETE,
    28:AUTHENTICATION_FAILURE,
    33:CM_SERVICE_ACCEPT,
    34:CM_SERVICE_REJECT,
    35:CM_SERVICE_ABORT,
    36:CM_SERVICE_REQUEST,
    37:CM_SERVICE_PROMPT,
    40:CM_REESTABLISHMENT_REQUEST,
    41:ABORT,
    48:MM_NULL,
    49:MM_STATUS,
    50:MM_INFORMATION,
    },
# L3GSM_RR, PD=6
6:{
    0:SI_13,
    2:SI_2bis,
    3:SI_2ter,
    5:SI_5bis,
    6:SI_5ter,
    7:SI_2quater,
    13:CHANNEL_RELEASE,
    19:CLASSMARK_ENQUIRY,
    21:MEASUREMENT_REPORT,
    22:CLASSMARK_CHANGE,
    25:SI_1,
    26:SI_2,
    27:SI_3,
    28:SI_4,
    29:SI_5,
    30:SI_6,
    33:PAGING_REQUEST_1,
    34:PAGING_REQUEST_2,
    36:PAGING_REQUEST_3,
    39:PAGING_RESPONSE,
    41:ASSIGNMENT_COMPLETE,
    46:ASSIGNMENT_COMMAND,
    47:ASSIGNMENT_FAILURE,
    50:CIPHERING_MODE_COMPLETE,
    53:CIPHERING_MODE_COMMAND,
    63:IMMEDIATE_ASSIGNMENT,
    },
# L3Mobile_PS_MM, PD=8
8:{
    1:GPRS_ATTACH_REQUEST,
    2:GPRS_ATTACH_ACCEPT,
    3:GPRS_ATTACH_COMPLETE,
    4:GPRS_ATTACH_REJECT,
    5:GPRS_DETACH_REQUEST,
    6:GPRS_DETACH_ACCEPT,
    8:ROUTING_AREA_UPDATE_REQUEST,
    9:ROUTING_AREA_UPDATE_ACCEPT,
    10:ROUTING_AREA_UPDATE_COMPLETE,
    11:ROUTING_AREA_UPDATE_REJECT,
    12:GPRS_SERVICE_REQUEST,
    13:GPRS_SERVICE_ACCEPT,
    14:GPRS_SERVICE_REJECT,
    16:PTMSI_REALLOCATION_COMMAND,
    17:PTMSI_REALLOCATION_COMPLETE,
    18:AUTHENTICATION_CIPHERING_REQUEST,
    19:AUTHENTICATION_CIPHERING_RESPONSE,
    20:AUTHENTICATION_CIPHERING_REJECT,
    28:AUTHENTICATION_CIPHERING_FAILURE,
    21:GPRS_IDENTITY_REQUEST,
    22:GPRS_IDENTITY_RESPONSE,
    32:GMM_STATUS,
    33:GMM_INFORMATION,
    },
# L3Mobile_PS_SM, PD=10
10:{
    65:ACTIVATE_PDP_CONTEXT_REQUEST,
    66:ACTIVATE_PDP_CONTEXT_ACCEPT,
    67:ACTIVATE_PDP_CONTEXT_REJECT,
    68:REQUEST_PDP_CONTEXT_ACTIVATION,
    69:REQUEST_PDP_CONTEXT_ACTIVATION_REJECT,
    70:DEACTIVATE_PDP_CONTEXT_REQUEST,
    71:DEACTIVATE_PDP_CONTEXT_ACCEPT,
    72:MODIFY_PDP_CONTEXT_REQUEST_NETTOMS,
    73:MODIFY_PDP_CONTEXT_ACCEPT_MSTONET,
    74:MODIFY_PDP_CONTEXT_REQUEST_MSTONET,
    75:MODIFY_PDP_CONTEXT_ACCEPT_NETTOMS,
    76:MODIFY_PDP_CONTEXT_REJECT,
    77:ACTIVATE_SECONDARY_PDP_CONTEXT_REQUEST,
    78:ACTIVATE_SECONDARY_PDP_CONTEXT_ACCEPT,
    79:ACTIVATE_SECONDARY_PDP_CONTEXT_REJECT,
    85:SM_STATUS,
    86:ACTIVATE_MBMS_CONTEXT_REQUEST,
    87:ACTIVATE_MBMS_CONTEXT_ACCEPT,
    88:ACTIVATE_MBMS_CONTEXT_REJECT,
    89:REQUEST_MBMS_CONTEXT_ACTIVATION,
    90:REQUEST_MBMS_CONTEXT_ACTIVATION_REJECT,
    91:REQUEST_SECONDARY_PDP_CONTEXT_ACTIVATION,
    92:REQUEST_SECONDARY_PDP_CONTEXT_ACTIVATION_REJECT,
    93:GPRS_NOTIFICATION,
    }
    # Nothing more yet...
}

# Define a dummy RAW L3 header / message for parts not implemented
class RawL3(Layer3):
    constructorList = [
        Bit('SI', ReprName='Skip Indicator', Pt=0, BitLen=4),
        Bit('PD', ReprName='Protocol Discriminator', \
            BitLen=4, Dict=PD_dict, Repr='hum'),
        Int('Type', Pt=0, Type='uint8'),
        Str('Msg', Pt='', Len=None, Repr='hex')]
#
#
def parse_L3(buf, L2_length_incl=0):
    '''
    This is a global parser for mobile layer 3 signalling.
    It works fine as is with MM, CC, GMM and SM protocols.
    For GSM RR signalling, the length of the L2 pseudo-length header (1 byte)
    needs to be passed as parameter "L2_length_incl" to retrieve correctly 
    the protocol discriminator and message type.
    E.g. for messages passed over GSM BCCH or CCCH: L2_length_incl=1
    
    parse_L3(string_buffer, L2_length_incl=0) -> L3Mobile_instance
    '''
    # select message from PD and Type
    if len(buf) < 2:
        log(ERR, '(parse_L3) message too short for L3 mobile')
        return RawLayer(buf)
    #
    # protocol is 4 last bits of 1st byte
    # type is 6 last bits of 2nd byte
    Prot, Type = ord(buf[L2_length_incl])&0x0F, ord(buf[L2_length_incl+1])
    # for MM, CC and GSM RR, only 6 1st bits for type
    if Prot in (3, 5, 6):
        Type = Type&0x3F
    # get the right protocol from PD
    #if Prot not in L3Call.keys():
    if Prot not in L3Call:
        #if Prot not in PD_dict.keys():
        if Prot not in PD_dict:
            log(ERR, '(parse_L3) unknown L3 prot discr PD: %i' % Prot)
        else:
            log(WNG, '(parse_L3) L3 protocol %s not implemented' % PD_dict[Prot])
        l3 = RawL3()
        l3.map(buf)
    # get the right type from Type
    #elif Type not in L3Call[Prot].keys():
    elif Type not in L3Call[Prot]:
        log(ERR, '(parse_L3) L3 message type %i undefined for protocol %s' \
              % (Type, PD_dict[Prot]))
        l3 = RawL3()
        l3.map(buf)
        # for L3GSM_RR, still use the msg type dict:
        # because GSM RR are not all implemented
        if Prot == 6:
            l3.Type.Dict = GSM_RR_dict
    # select the correct L3 signalling message
    else:
        l3 = L3Call[Prot][Type]()
        try:
            l3.map(buf)
        except:
            log(ERR, '(parse_L3) mapping buffer on L3 message failed')
            l3 = RawL3()
            l3.map(buf)
    return l3

#
# OpenBTS typical sequence:
_bts_test = \
['\x05$\x11\x033Y\x90\x05\xf4T\x01\x98\xcb',
 '\x05\x18\x01',
 '\x05Y\x08)\x80\x10\x13\x10w6R',
 '\x05!',
 '\x03\x05\x04\x06`\x04\x02\x00\x05\x81^\x08\x81\x00\x12cy65\x16',
 '\x83\x02',
 '\x06.\n@3\x00c\x01',
 '\x06)\x00',
 '\x83%\x02\xe1\xff',
 '\x83*',
 '\x06\r\x00',
 '\x03m\x08\x02\xe0\x90',
 '\x05$\x11\x033Y\x90\x05\xf4T\x01\x98\xcb',
 '\x05\x18\x01',
 '\x05Y\x08)\x80\x10\x13\x10w6R',
 '\x05!',
 '\x03\x05\x04\x06`\x04\x02\x00\x05\x81^\x03\x81\x120',
 '\x83\x02',
 '\x06.\n@3\x00c\x01',
 '\x06)\x00',
 '\x83\x03\x02\xe1\x80',
 '\x83\x01',
 '\x83\x07',
 '\x03O',
 '\x03%\x02\xe0\x90',
 '\x83-',
 '\x03j\x08\x02\xe0\x90',
 '\x06\r\x00',
 '\x83%\x02\xe1\x90',
 '\x83*',
 '\x06\r\x00',
 '\x06\r\x01',
 '\x05\x08\x11\x00\xf2 \x03\xe83\x05\xf4T\x01\x98\xcb',
 '\x05\x18\x01',
 '\x05Y\x08)\x80\x10\x13\x10w6R',
 '\x052E\x06\x8dAt\xbbL\x06G\x11\x80\x90AE\x91\xe1',
 '\x05\x02\x00\xf2 \x03\xe8\x17\x05\xf4M\xf7\xba8',
 '\x06\r\x00',
 '\x06?\x00 @3B\xbbW\x01\x00',
 '\x06!\x10\x08)\x80\x10D\x02\x00B\x13',
 '\x06.\n@3\x00c\x01',
 '\x06!\x10\x08)\x80\x10D\x02\x00B\x13',
 '\x06?\x00(@3\x12\xbc`\x00\x00',
 '\x06!\x10\x08)\x80\x10D\x02\x00B\x13',
 "\x06'\x07\x033Y\xa6\x08)\x80\x10D\x02\x00B\x13",
 '\x06!\x10\x08)\x80\x10D\x02\x00B\x13',
 '\x06?\x00 @3\x17\xeb!\x01\x00',
 '\x06!\x10\x08)\x80\x10D\x02\x00B\x13',
 "\x06'\x07\x033Y\xa6\x08)\x80\x10D\x02\x00B\x13"]
#
