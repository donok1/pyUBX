"""The messages in the UBX-RXM class are used to output status and result data from the receiver manager as well as sending commands to the receiver manager. """

from ubx.UBXMessage import initMessageClass, addGet
from ubx.Types import CH, U, U1, U2, I1, U4, R4, R8, X1, X4
from ubx.Tables import GNSS_ID


@initMessageClass
class RXM:
    """Message class RXM."""

    _class = 0x02

    @addGet
    class RAWX:
        """3.16.3.1 Multi-GNSS raw measurements. protocle 27.13"""
        _id = 0x15

        class Fields:
            rcvTow  = R8(0)      # Measurement time of week (s)
            week    = U2(1)        # GPS week number
            leapS   = I1(2)       # GPS leap seconds (GPS-UTC) (s)
            numMeas = U1(3)     # Number of measurements to follow
            recStat = X1(4)     # Receiver tracking status bitfield
            version = U1(5)#, allowed={1: "RAWX Message V 1"}) # Message version (0x01 for this version)
            reserved0=U(6,2)  # Reserved
            class Repeated:
                prMes = R8(1)   # Pseudorange measurement [m]
                cpMes = R8(2)   # Carrier phase measurement [cycles]
                doMes = R4(3)   # Doppler measurement [Hz]
                gnssId= U1(4, allowed=GNSS_ID)  # GNSS identifier
                svId  = U1(5)   # Satellite identifier
                sigId = U1(6)   # New style signal identifier
                freqId= U1(7)   # GLONASS: This is the frequency slot + 7
                locktime=U2(8)  # Carrier phase locktime counter (maximum 64500ms)
                cno   = U1(9)   # Carrier-to-noise density ratio [dB-Hz]
                prStdev=X1(10)  # Estimated pseudorange measurement std [m]
                cpStdev=X1(11)  # Estimated carrier phase measurement std [cycle]
                doStdev=X1(12)  # Estimated Doppler measurement [Hz]
                trkStat=X1(13)  # Tracking status bitfield
                reserved1=U1(14)# Reserved

#        @property
#        def spectra(self):
#            return [{
#                "centerFreq": self.__getattribute__(f'center_{blockNum}'),
#                "span": self.__getattribute__(f'span_{blockNum}'),
#                "res": self.__getattribute__(f'res_{blockNum}'),
#                "pga": self.__getattribute__(f'pga_{blockNum}'),
#                "spectrumBinCenterFreqs": [ self.__getattribute__(f'center_{blockNum}') + self.__getattribute__(f'span_{blockNum}') * (i - 128) / 256 for i in range(256)],
#                "spectrum": [rfBin for rfBin in self.__getattribute__(f'spectrum_{blockNum}')]
#            } for blockNum in range(1,self.numRfBlocks+1) ]
