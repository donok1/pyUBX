"""Various tables collected from the datasheet."""

# map gnssId to GNSS string. §31.6
GNSS_Identifiers = [
    'GPS',
    'SBAS',
    'Galileo',
    'BeiDou',
    'IMES',
    'QZSS',
    'GLONASS',
    ]

# 1.5.2 GNSS identifiers
GNSS_ID = {
    0: 'GPS',
    1: 'SBAS',
    2: 'Galileo',
    3: 'BeiDou',
    4: 'IMES',
    5: 'QZSS',
    6: 'GLONASS',
    }

# 1.5.2 GNSS identifiers
GNSS_ID_RNX = {
    0: 'G',
    1: 'S',
    2: 'E',
    3: 'B',
    4: 'I',
    5: 'Q',
    6: 'R',
    }

def gnssIdRNXfromCode(code: int):
    return GNSS_ID_RNX[code]

#1.5.4 Signal identifiers
SIG_ID_GPS = {
    0:'L1C',
    3:'L2CL',
    4:'L2CM',
}
SIG_ID_SBAS = {
    0:'L1C',
}
SIG_ID_GAL = {
    0:'E1C',
    1:'E1B',
    5:'E5bI',
    6:'E5bQ',
}
SIG_ID_BDS = {
    0:'B1ID1',
    1:'B1ID2',
    2:'B2ID1',
    3:'B2ID2',
}
SIG_ID_QZSS = {
    0:'L1C',
    1:'L1S',
    4:'L2CM',
    5:'L2CL',
}
SIG_ID_GLO = {
    0:'L1',
    2:'L2',
}
SIG_ID = {
    0:SIG_ID_GPS,
    1:SIG_ID_SBAS,
    2:SIG_ID_GAL,
    3:SIG_ID_BDS,
    5:SIG_ID_QZSS,
    6:SIG_ID_GLO,
}
