# Mikkel Kode

from pysnmp.entity.rfc3413.oneliner import cmdgen
#from pysnmp.proto import rfc1155, rfc1902, api
#from pyasn1.codec.ber import encoder, decoder

def mikkel_mac_address_get():
    hostname = '10.10.1.1'
    dot1dTpFdbTable = ('1.3.6.1.2.1.3.1.1.2')   #1,3,6,1,2,1,17,4,3
    cmdGen = cmdgen.CommandGenerator()
    cmdGen.ignoreNonIncreasingOid = True
    
    errorIndication, errorStatus, errorIndex, \
        varBindTable = cmdGen.nextCmd(
            cmdgen.CommunityData('ciscolab', 'ciscolab'),        #('tlk-read', 'tlk-read')
            cmdgen.UdpTransportTarget((hostname, 161)),
            dot1dTpFdbTable
            )
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s\n' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                ))
        else:
            for varBindTableRow in varBindTable:
                for name, val in varBindTableRow:
                    # Making MAC Address readable
                    temp = val.prettyPrint()[2:].upper()
                    mac_address = ':'.join([temp[i:i+2] for i in range(0, len(temp), 2)])
                    # Making IP Address readable
                    temp = name.prettyPrint().split('.')
                    ip_address = temp[-4] + '.' + temp[-3] + '.' + temp[-2] + '.' + temp[-1]
                    
                    print('%s: %s' % (ip_address, mac_address))