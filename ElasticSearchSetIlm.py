#!/usr/bin/env python3

import requests
import re
import sys

def elk_set_ilm():

    ip =  sys.argv[1]
    port = sys.argv[2]
    protocol = sys.argv[3]
    f_host = f'{protocol}://{ip}:{port}'
    url = re.sub('\?|\!|\'|\n|\'|\;', '', f_host)
    beats = ['auditbeat','filebeat','metricbeat','packetbeat']
    
    header = {
      'Content-Type': 'application/json'
    }
    
    config = {
      "policy": {
        "phases": {
          "hot": {
            "actions": {
              "rollover": {
                "max_primary_shard_size": "50GB"
              }
            }
          },
          "delete": {
            "min_age": "30d",
            "actions": {
              "delete": {} 
            }
          }
        }
      }
    }

    for beat in beats:
        
        try:
            f_url = f'{url}/_ilm/policy/beat'
            r = requests.put(f_url, data=config, headers=header)
            print(r,'\n',r.content)

        except:
            print('Could not execute the following request.')
            sys.exit()

if __name__ == '__main__':            
    elk_set_ilm()
