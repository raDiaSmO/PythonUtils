#!/usr/bin/env python3

import requests
import json
import sys

def check_url():
    
    endpoint = 'https://urlscan.io/api/v1/scan' 
    file = sys.argv[2]
    api = sys.argv[3]

    with open (file) as urls:
        for url in urls:

            data = {
                    'url': url,
                    'visibility': "public"
            }

            http_headers = {
                    'API-Key': api,
                    'Content-Type': 'application/json'
            }

            try:
                r = requests.post(endpoint, headers=http_headers, data=json.dumps(data))
                r_dict = (r.json())
                print('The following link will be accessible in a few minutes and will contain the scan result.\n\n', r_dict['result'], end='\n\n')

            except:
                print('Could not execute the following request.')
                sys.exit()
                
def check_ip():

    endpoint = 'https://api.abuseipdb.com/api/v2/check'
    file = sys.argv[2]
    api = sys.argv[3]

    with open (file) as ips:
        for ip in ips:

            data = {
                    'ipAddress': ip
            }

            http_headers = {
                    'Accept': 'application/json',
                    'Key': api
            }

            try:
                r = requests.request(method='GET', url=endpoint, headers=http_headers, params=data)
                decoded_r = json.loads(r.text)
                print(json.dumps(decoded_r, sort_keys=True, indent=3))

            except:
                print('Could not execute the following request.')
                sys.exit()

if __name__ == '__main__':
    globals()[sys.argv[1]]()
