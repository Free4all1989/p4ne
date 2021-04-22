import ipaddress
import random

random.seed()
# net = random.randint(0x0b000000, 0xdf000000)
# mask = random.randint(8, 24)

# net1 = ipaddress.IPv4Network((random.randint(0x0b000000, 0xdf000000), random.randint(8, 24)), strict=False)

# print(net1)


class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        ipaddress.IPv4Network.__init__(self, (random.randint(0x0b000000, 0xdf000000), random.randint(8, 24)), strict=False)

i = 0
L = []
while i < 50:
    net = IPv4RandomNetwork()
    if not net.is_private and not net in L:
        L.append(net)
        # print(net.network_address, net.hostmask)
        i += 1
    else:
        print("Private or double net detected:", net)

# def netsort(nwa):
#    return nwa.network_address

print(L)
L2 = sorted(L, key=lambda nwsort: (nwsort.hostmask, nwsort.network_address))
print(L2)