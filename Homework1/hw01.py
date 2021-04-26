import glob, re
from openpyxl import Workbook


def classify(line):
    if re.match('^.*ip address ((\d{1,3})\.?){4} ((\d{1,3})\.?){4}', line):
        m = re.match('(^.*ip address )(((\d{1,3})\.?){4}) (((\d{1,3})\.?){4})', line)
        ipstr = str(m.group(2))+";"+str(m.group(5))
        # l = [str(m.group(2)), str(m.group(5))]
        # ip = ipaddress.ip_interface(ipstr)
        return ipstr


L1 = []

for file in glob.glob('..\\lab1.5\\config_files\\*.txt'):
    with open(file) as f:
        for line in f:
            L = classify(line)
            if L != None:
                L1.append(L)


L2 = set(L1)
print(len(L1), len(L2))
print(L2)

wb = Workbook()
ws = wb.active
ws.append(['ip', 'mask'])

for i in L2:
    row =  i.split(";")
    print(row)
    ws.append(row)

wb.save(filename="netplan.xlsx")
