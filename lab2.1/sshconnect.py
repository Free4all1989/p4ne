import paramiko, time, re

login = 'restapi'
password = 'j0sg1280-7@'
host_ip = '10.31.70.209'

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect(host_ip, username=login, password=password, look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()


session.send("terminal length 0\n")
# time.sleep(0.5)
session.send("show interface\n")
time.sleep(2)
resp = session.recv(20000).decode()
L1 = []
L2 = []
L3 = []
L4 = []
L5 = []
L6 = []

for line in resp.splitlines():
    if re.match('^(.*) is (.*), line protocol .*', line):
        m = re.match('^(.*) is (.*), line protocol .*', line)
        interface = str(m.group(1))
        state = str(m.group(2))
        L1.append(interface)
        L2.append(state)
    elif re.match('^.*?(\d+).*packets input,\s(\d+).*', line):
        m = re.match('^.*?(\d+).*packets input,\s(\d+).*', line)
        inputp = str(m.group(1))
        inputb = str(m.group(2))
        L3.append(inputp)
        L4.append(inputb)
    elif re.match('^.*?(\d+).*packets output,\s(\d+).*', line):
        m = re.match('^.*?(\d+).*packets output,\s(\d+).*', line)
        outputp = str(m.group(1))
        outputb = str(m.group(2))
        L5.append(outputp)
        L6.append(outputb)
ssh_connection.close()

D = {}
for i in range(len(L1)):
    D[L1[i]] = {'state': L2[i], 'in pack': L3[i], 'in byte': L4[i], 'out pack': L5[i], 'out byte': L6[i]}

print(D)