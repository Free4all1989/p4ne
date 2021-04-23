import glob

L = []

for file in glob.glob('config_files\\*.txt'):
    with open(file) as f:
        for line in f:
            check = line.find('ip address')
            if check != -1:
                fline = line.replace('ip address ', '').strip()
                if fline[0] == '1' or fline[0] == '2':
                    L.append(fline)


L1 = set(L)
for i in L1:
    print(i)
