from pyzabbix import ZabbixAPI
import csv
import time

URL = 'http://127.0.0.1/zabbix'
USERNAME = 'zabbix'
PASSWORD = 'password'

try:
    zapi = ZabbixAPI(URL, timeout=15)
    zapi.login(USERNAME,PASSWORD)
    print(f'Conectado na API do Zabbix, versão {zapi.api_version()}')
except Exception as err:
    print(f'Falha ao conectar na API do zabbix, erro: {err}')

info_interfaces = {
    "1": {"type": "agent", "id": "1", "port": "10050"},
    "2": {"type": "SNMP", "id": "2", "port": "161"},
    }

templateids = ['']
templates = [{"templateid": templateid} for templateid in templateids]

def create_host(templates, host, ip, groupid):
    try:
        create_host = zapi.host.create({
            "templates": templates,
            "host": host,
            "status": 1,
            "groups": [{"groupid": groupid}],
            "interfaces": [{
                "type": info_interfaces['1']['id'],
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "",
                "port": info_interfaces['1']['port'],
            }]
        })
        print(f'Host cadastrado com sucesso {host}')
    except Exception as err:
        print(f'Falha ao cadastrar o host: erro {err}')

start_time = time.time()

#caminho csv
with open('hosts.csv') as file:
    file_csv = csv.reader(file, delimiter=';')
    for [hostname,ipaddress,groupids] in file_csv:
        create_host(host=hostname,ip=ipaddress,groupid=groupids)
end_time = time.time()
total_time = (end_time-start_time)*1000
print(f'Total time = {total_time:.2f} ms')





