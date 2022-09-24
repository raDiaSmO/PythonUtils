#!/usr/bin/env python3

import requests
import re
import sys

def elk_set_ilm():

    ip =  sys.argv[1]
    port = sys.argv[2]
    protocol = sys.argv[3]
    f_host = f'{protocol}://{ip}:{port}'
    url = re.sub('\?|\!|\'|\n|\;', '', f_host)
    beats = ['auditbeat','filebeat','metricbeat','packetbeat']
    
    header = {
      'Content-Type': 'application/json'
    }
    
    config = {
      "policy": {
        "phases": {
          "hot": {
            "min_age": "0ms",
            "actions": {
              "rollover": {
                "max_primary_shard_size": "50gb"
              }
            }
          },
          "warm": {
            "min_age": "3d",
            "actions": {
              "set_priority": {
                "priority": 50
              }
            }
          },
          "cold": {
            "min_age": "7d",
            "actions": {
              "set_priority": {
                "priority": 0
              }
            }
          },
          "delete": {
            "min_age": "30d",
            "actions": {
              "delete": {
                "delete_searchable_snapshot": True
              }
            }
          }
        }
      }
    }

    for beat in beats:
        
        try:
            f_url = f'{url}/_ilm/policy/{beat}'
            r = requests.put(f_url, json=config, headers=header)
            print(r,'\n',r.content)

        except:
            print('Could not execute the following request.')
            sys.exit()

if __name__ == '__main__':            
    elk_set_ilm()
