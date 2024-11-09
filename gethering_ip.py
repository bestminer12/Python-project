import redis
import requests
import json
import time

redis_client = redis.Redis(host='localhost', port=6379, db=0)

API_KEYS = {'abuseipdb': 'ac038c63606987d64b8d86bd50b8595afc321911a2dd88ae72d0f14067cb10488e0dacf3f97241fb'}

def make_request(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"HTTP 요청 에러: {e}")
        return None


def get_ipinfo(ip):
    reputation_data={}

    abuseipdb_url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90'
    abuseipdb_headers = {'Key': API_KEYS['abuseipdb'], 'Accept': 'application/json'}
    reputation_data['abuseipdb'] = make_request(abuseipdb_url, abuseipdb_headers)

    return reputation_data

def ipinfo_parsing(ip):
    result_parsing = {}
    ipAddr=ip['abuseipdb']['data']['ipAddress']
    isPublic = ip['abuseipdb']['data']['isPublic']
    ipVersion=ip['abuseipdb']['data']['ipVersion']
    abuseConfidenceScore=ip['abuseipdb']['data']['abuseConfidenceScore']
    countryCode=ip['abuseipdb']['data']['countryCode']
    isp=ip['abuseipdb']['data']['isp']
    domain=ip['abuseipdb']['data']['domain']
    totalReports=ip['abuseipdb']['data']['totalReports']

    result_parsing["IPAddress"]=ipAddr
    result_parsing["IsPublic"] = isPublic
    result_parsing["IPVersion"] = ipVersion
    result_parsing["CountryCode"] = countryCode
    result_parsing["ISP"] = isp
    result_parsing["Domain"] = domain
    result_parsing["AbuseConfidenceScore"] = abuseConfidenceScore
    result_parsing["TotalReports"] = totalReports

    return result_parsing

if __name__ == "__main__":
    ip_addr="192.111.22.21"
    reputation = get_ipinfo(ip_addr)

    result=ipinfo_parsing(reputation)

    for key, value in result.items():
        print(f"{key}: {value}")

