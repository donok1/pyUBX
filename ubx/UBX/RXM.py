"""The messages in the UBX-RXM class are used to output status and result data from the receiver manager as well as sending commands to the receiver manager. """

from ubx.UBXMessage import initMessageClass, addGet, _mkFieldInfo, _mkNamesAndTypes
from ubx.Types import CH, U, U1, U2, I1, U4, R4, R8, X1, X4
from ubx.Tables import GNSS_ID, GNSS_ID_RNX, gnssIdRNXfromCode, SIG_ID


@initMessageClass
class RXM:
    """Message class RXM."""

    _class = 0x02

    @addGet
    class RAWX:
        """3.16.3.1 Multi-GNSS raw measurements. protocle 27.13"""
        _id = 0x15

        class Fields:
            rcvTow  = R8(1)     # Measurement time of week (s)
            week    = U2(2)     # GPS week number
            leapS   = I1(3)     # GPS leap seconds (GPS-UTC) (s)
            numMeas = U1(4)     # Number of measurements to follow
            recStat = X1(5)     # Receiver tracking status bitfield
            version = U1(6)#, allowed={1: "RAWX Message V 1"}) # Message version (0x01 for this version)
            reserved0=U(7,2)  # Reserved
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

        def __str__(self):
            """Return human readable string."""
            fieldInfo = _mkFieldInfo(self.Fields)
            varNames, varTypes = _mkNamesAndTypes(fieldInfo, self._len)
            header = "\n  RXM-{}:".format(type(self).__name__)
            header+= f' {self.rcvTow:15.9f} {self.week:5d} {self.leapS:3d}'\
                     f' {self.numMeas:3d} {self.recStat:08b} x\{self.version:02x}'
            s = header
            for i in range(self.numMeas):
                s += f'\n{gnssIdRNXfromCode(getattr(self,varNames[7+3+i*14])):1s}'   # gnssId
                s += f'{getattr(self, varNames[7+4+i*14])%100:2d}'   # svId
                s += f' {SIG_ID[getattr(self,varNames[7+3+i*14])][getattr(self, varNames[7+5+i*14])]:5s}'   # sigId
                
                s += f' {getattr(self, varNames[7+0+i*14]):14.3f}'   # prMes
                s += f' {getattr(self, varNames[7+1+i*14]):14.3f}'   # cpMes
                s += f' {getattr(self, varNames[7+8+i*14]):14.3f}'   # cno
                s += f' {getattr(self, varNames[7+2+i*14]):14.3f}'   # doMes
#                s += f' {getattr(self, varNames[7+9+i*14]):08b}'   # prStdev
#                s += f' {getattr(self, varNames[7+9+i*14]):4d}'   # prStdev
                s += f' {0.01*(2.0**getattr(self, varNames[7+9+i*14])):7.3f}'   # prStdev
#                s += f' {getattr(self, varNames[7+10+i*14]):08b}'   # cpStdev
                s += f' {0.004*getattr(self, varNames[7+10+i*14]):7.3f}'   # cpStdev
#                s += f' {getattr(self, varNames[7+11+i*14]):08b}'   # doStdev
#                s += f' {getattr(self, varNames[7+11+i*14]):4d}'   # doStdev
                s += f' {0.002*(2.0**getattr(self, varNames[7+11+i*14])):7.3f}'   # prStdev
                s += f' {getattr(self, varNames[7+12+i*14]):08b}'   # trkStat

#                    varName,
#                    varType.toString(getattr(self, varName))    # prettify
#                    )
#            for (varName, varType) in zip(varNames, varTypes):
##                    print(f'varName:{varName}   varType:{varType}   getattr(self, varName):{getattr(self, varName)}'  )
#                s += "\n  {}={}".format(
#                    varName,
#                    varType.toString(getattr(self, varName))    # prettify
#                    )
            return s
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
