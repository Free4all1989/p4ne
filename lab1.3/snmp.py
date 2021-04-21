from pysnmp.hlapi import *

snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_object2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result = getCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.107", 161)),
                ContextData(),
                ObjectType(snmp_object))

result2 = nextCmd(SnmpEngine(),
                  CommunityData("public", mpModel=0),
                  UdpTransportTarget(("10.31.70.107", 161)),
                  ContextData(),
                  ObjectType(snmp_object2), lexicographicMode=False)

L = []
L2 = []
for r in result:
    L.append(r)

for t in result2:
    L2.append(t)

for k in L[0][3]:
    print(k)

print("")

for j in range(len(L2)):
    try:
        for i in L2[j][3]:
            print(i)
    except:
        print("no interface")