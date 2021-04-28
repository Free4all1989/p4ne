from flask import Flask, jsonify
import glob, re, ipaddress, os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/configs')
def configs():
    return jsonify(L3)

@app.route('/config/<host>')
def confighost(host):
    return jsonify(D[host])


def classify(line):
    if re.match('^.*ip address ((\d{1,3})\.?){4} ((\d{1,3})\.?){4}', line):
        m = re.match('(^.*ip address )(((\d{1,3})\.?){4}) (((\d{1,3})\.?){4})', line)
        ipstr = str(m.group(2))+"/"+str(m.group(5))
        ip = str(m.group(2))
        return {"ip": ip}
    elif re.match('^.*interface G.+', line):
        m = re.match('^.*interface (G.+\d)', line)
        intstr = str(m.group(1))
        return {"int": intstr}
    elif re.match('^.*hostname .+', line):
        m = re.match('^.*hostname (.+)$', line)
        hoststr = str(m.group(1))
        # print(hoststr)
        return {"HOST": hoststr}
    else:
        return {}

if __name__ == '__main__':
    L1 = []
    L3 = []
    D = {}
    for file in glob.glob('..\\lab1.5\\config_files\\*.txt'):
        with open(file) as f:
            for line in f:
                L = classify(line)
                if "ip" in L:
                    L1.append(L["ip"])
            f.seek(0)
            for line in f:
                L = classify(line)
                if "HOST" in L:
                    L3.append(L["HOST"])
                    D[L["HOST"]] = L1
    print(D.keys())
    app.run(debug=True)