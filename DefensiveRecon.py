#!/usr/bin/env python3

import sys
import requests
import json

payloads = []
tool = sys.argv[1]
file = sys.argv[2]
api = sys.argv[3]

def defensive_recon(tool):

    with open (file) as items:

        for item in items:

            match tool:

                case 'shodan':
                    endpoint = f"https://api.shodan.io/shodan/host/{item}"

                    data = {
                        'key': api
                    }

                    r = requests.request(method='GET', url=endpoint, params=data)
                    decoded_r = json.loads(r.text)
                    payloads.append(json.dumps(decoded_r, sort_keys=True, indent=3))                

                case 'urlscan':
                    endpoint = 'https://urlscan.io/api/v1/scan'

                    data = {
                        'url': item,
                        'visibility': "public"
                    }

                    http_headers = {
                        'API-Key': api,
                        'Content-Type': 'application/json'
                    }

                    r = requests.post(url=endpoint, headers=http_headers, data=json.dumps(data))
                    r_dict = (r.json())
                    payloads.append(f"The following link will be accessible in a few minutes and will contain the scan result.\n\n',{r_dict}['result'], end='\n\n")

                case 'abuseipdb':
                    endpoint = 'https://api.abuseipdb.com/api/v2/check'

                    data = {
                        'ipAddress': item
                    }

                    http_headers = {
                        'Accept': 'application/json',
                        'Key': api
                    }

                    r = requests.request(method='GET', url=endpoint, headers=http_headers, params=data)
                    decoded_r = json.loads(r.text)
                    payloads.append(json.dumps(decoded_r, sort_keys=True, indent=3))                                       

                case _:
                    print('Provided tool does not exist.')
                    sys.exit()

        for payload in payloads:

            try:
                print(payload)

            except:
                print('Could not execute the following request.')
                sys.exit()

if __name__ == '__main__':
    defensive_recon(tool)
