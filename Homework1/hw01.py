import glob, re, ipaddress
from openpyxl import Workbook


def classify(line):
    if re.match('^.*ip address ((\d{1,3})\.?){4} ((\d{1,3})\.?){4}', line):
        m = re.match('(^.*ip address )(((\d{1,3})\.?){4}) (((\d{1,3})\.?){4})', line)
        ipstr = str(m.group(2)) + "/" + str(m.group(5))
        # l = [str(m.group(2)), str(m.group(5))]
        ip = ipaddress.ip_interface(ipstr)
        return ip


L1 = []

for file in glob.glob('..\\lab1.5\\config_files\\*.txt'):
    with open(file) as f:
        for line in f:
            L = classify(line)
            if L != None:
                L1.append(L)


L2 = set(L1)

wb = Workbook()
ws = wb.active
ws.append(['Subnet', 'mask'])

for i in L2:
    # ip = ipaddress.ip_interface(i).ip
    net = str(ipaddress.ip_interface(i).network).split('/')
    mask = ipaddress.ip_interface(i).netmask
    print(net[0], " ", mask)
    row = []
    row.append(net[0])
    row.append(str(mask))
    ws.append(row)

wb.save(filename="netplan.xlsx")
