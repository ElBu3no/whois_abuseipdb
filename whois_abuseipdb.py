import requests
import whois
import json

def consultar_geolocalizacao(ip):
    try:
        url = f"http://ipinfo.io/{ip}/json"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            return f"IP: {dados['ip']}, País: {dados['country']}, Cidade: {dados['city']}, Região: {dados['region']}"
        else:
            return f"Erro ao consultar a geolocalização do IP {ip}. Código de status: {resposta.status_code}"
    except Exception as e:
        return f"Erro ao consultar a geolocalização do IP {ip}: {str(e)}"

def consultar_abuseipdb(ip, chave_api):
    try:
        url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90"
        headers = {
            "Key": chave_api,
            "Accept": "application/json"
        }
        resposta = requests.request("GET", url, headers=headers)
        if resposta.status_code == 200:
            dados = resposta.json()
            if dados['data']['abuseConfidenceScore'] >= 75:
                return f"O IP {ip} foi listado como abusivo com uma pontuação de confiança de abuso de {dados['data']['abuseConfidenceScore']}."
            else:
                return f"O IP {ip} não foi listado como abusivo."
        else:
            return f"Erro ao consultar o AbuseIPDB para o IP {ip}. Código de status: {resposta.status_code}"
    except Exception as e:
        return f"Erro ao consultar o AbuseIPDB para o IP {ip}: {str(e)}"

def consultar_whois(ip):
    try:
        w = whois.whois(ip)
        return str(w)
    except Exception as e:
        return f"Erro ao consultar o WHOIS para o IP {ip}: {str(e)}"

def get_ip_info(ip_address, token):
    url = f"https://ipinfo.io/{ip_address}/json?token={token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"Erro": f"Erro ao obter informações do IP {ip_address}. Código de status: {response.status_code}"}

def consultar_ips_arquivo(nome_arquivo, chave_api_abuseipdb, token_ipinfo):
    try:
        with open(nome_arquivo, 'r') as file:
            ips = file.read().splitlines()
        resultados = []
        for ip in ips:
            resultado_geolocalizacao = consultar_geolocalizacao(ip)
            resultado_abuseipdb = consultar_abuseipdb(ip, chave_api_abuseipdb)
            resultado_ipinfo = get_ip_info(ip, token_ipinfo)
            resultado_combinado = f"{resultado_abuseipdb}\nIPinfo:\n{json.dumps(resultado_ipinfo, indent=4)}"
            resultados.append(resultado_combinado)
        return resultados
    except Exception as e:
        return f"Erro ao ler o arquivo {nome_arquivo}: {str(e)}"

# Nome do arquivo contendo os IPs
nome_arquivo_ips = 'ips.txt'

# Sua chave de API do AbuseIPDB
chave_api_abuseipdb = 'XXXXX'

# Seu token de acesso à API do ipinfo.io
token_ipinfo = 'XXXXX'

# Consulta geolocalização, AbuseIPDB e IPinfo para os IPs no arquivo
resultado = consultar_ips_arquivo(nome_arquivo_ips, chave_api_abuseipdb, token_ipinfo)

# Imprime os resultados
for r in resultado:
    print(r)
