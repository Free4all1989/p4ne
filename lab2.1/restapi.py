import requests, pprint

login = 'restapi'
password = 'j0sg1280-7@'
host_url = 'https://10.31.70.210:55443'

r = requests.post(host_url + '/api/v1/auth/token-services', auth=(login, password), verify=False)
token = r.json()['token-id']

print(token)

header = {"content-type": "application/json", "X-Auth-Token": token}
r = requests.get(host_url + '/api/v1/interfaces', headers=header, verify=False)
# pprint.pprint(r.json())


D = {}
for item in r.json()['items']:
    r2 = requests.get(host_url + '/api/v1/interfaces/' + item['if-name'] + '/statistics', headers=header, verify=False)
    D[item['if-name']] = {'in bps': r2.json()['in-packet-rate-bps'], 'in pps': r2.json()['in-packet-rate-pps'], 'out bps': r2.json()['out-packet-rate-bps'], 'out pps': r2.json()['out-packet-rate-pps']}


print(D)
