#!/usr/bin/env python3

import sys
import subprocess
import re

payloads = []
tool = sys.argv[1]
ip = sys.argv[2]

def offensive_recon(tool):

    match tool:

        case 'nmap':
            payloads.append(f'nmap -v -sV -sC -A -p- -oN nmap_enum {ip}')

        case 'fuzz':
            protocol = sys.argv[3]
            wordlist = sys.argv[4]
            payloads.append(f'ffuf -o fuzz_enum -w {wordlist} -u {protocol}://{ip}/FUZZ -H "Host: FUZZER"')

        case 'dirbuster':
            protocol = sys.argv[3]
            wordlist = sys.argv[4]
            payloads.append(f'dirbuster -H -v -l {wordlist} -u {protocol}://{ip}/')

        case 'wpscan':
            protocol = sys.argv[3]
            api = sys.argv[4]
            payloads.append(f'wpscan --url {protocol}://{ip}/ --random-user-agent --disable-tls-checks --detection-mode aggressive --api-token {api} -e vp,vt,dbe --output wpscan_enum --format cli')      

        case _:
            print('Provided tool does not exist.')
            sys.exit()

    for payload in payloads:

        try:
            command = re.sub('\?|\!|\'|\n|\'|\;', '', payload)
            subprocess.check_output(['bash','-c', command])

        except:
            print('Could not execute the following request.')
            sys.exit()

if __name__ == '__main__':
    offensive_recon(tool)
