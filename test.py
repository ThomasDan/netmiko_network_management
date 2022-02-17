from pysnmp.smi import builder

mibBuilder = builder.MibBuilder()
MacAddress, = mibBuilder.importSymbols('SNMPv2-TC', 'MacAddress')
macAddress = MacAddress(hexValue='05056bdafc'.zfill(12))
print(macAddress)
print(macAddress.prettyPrint())