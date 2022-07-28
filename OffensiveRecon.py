#!/usr/bin/env python3

import sys
import subprocess

def nmap():
    
    ip = sys.argv[2]

    try:
        f_string = f'nmap -v -sV -sC -A -p- -oN nmap_enum {ip}'
        subprocess.check_output(['bash','-c', f_string])

    except:
        print('Could not execute the following request.')
        sys.exit()

def fuzz():

    wordlist = sys.argv[2]
    protocol = sys.argv[3]
    ip = sys.argv[4]

    try:
        f_string = f'ffuf -o fuzz_enum -w {wordlist} -u {protocol}://{ip}/FUZZ -H "Host: FUZZER"'
        subprocess.check_output(['bash','-c', f_string])

    except:
        print('Could not execute the following request.')
        sys.exit()
                
def dirbuster():

    wordlist = sys.argv[2]
    protocol = sys.argv[3]
    ip = sys.argv[4]

    try:
        f_string = f'dirbuster -H -v -l {wordlist} -u {protocol}://{ip}/'
        subprocess.check_output(['bash','-c', f_string])

    except:
        print('Could not execute the following request.')
        sys.exit()

if __name__ == '__main__':
    globals()[sys.argv[1]]()
