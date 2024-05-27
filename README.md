# zabbix_api_add_hosts
Dois scripts em pyton para adicionarem IC com informações de IP Hostname HostGroup e Template ao Zabbix.

# Como utilizar
Configurar os valores das variaveis "URL", "USERNAME" e "PASSWORD" com as credenciais de acesso Zabbix.
Informar o ID do template na variavel "templateids"

A lista de Hosts deve ser passada por um arquivo .csv com a seguinte ordem de colunas:

Hostname; ip; id_group.
