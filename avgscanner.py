#!/usr/bin/python3
#avgscanner.py -i <IP> --opt <1, 2, 3>
import argparse

def exit():
    print("\n\t\t[+] Quits [+]\n")
    quit()

parser = argparse.ArgumentParser(description = 'Your Average Scanner', epilog = 'Use Responsibly!')
parser.add_argument('IP', help = "Target IP", nargs = '+')
parser.add_argument('--opt', help = "Options Mode [Default -> 3]: 1 -> Port find, 2 -> NMAP scan, 3 -> Port Find and Run Scan. [Only on TCP Ports]", metavar = 'OPTION', default = 3)
args = parser.parse_args()

IP = args.IP[0]
try:
    opt = int(args.opt)
except:
    print("Option Should Be An Integer: 1, 2, or 3. See --help for scan options")
    exit()

if (opt < 1) or (opt > 3):
    print("Option Should Be 1, 2, or 3 (see --help)")
    exit()
else:
    print("All good!")