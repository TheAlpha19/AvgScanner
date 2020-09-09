#!/usr/bin/python3
#avgscanner.py -i <IP> --opt <1, 2, 3>
import argparse
import subprocess

def exit():
    print("\n\t\t[+] Quits [+]\n")
    quit()

def portFind(IP):
    print("\t\t[+] Running Port Find [+]\n")
    out = subprocess.run(['masscan', '-e', 'tun0', '--rate=1000', '-p', '0-65535', IP], capture_output = True)
    print("{}".format(out.stdout.decode()))
    print("\t\t[+] Port Find Complete [+]\n")

def Scan(IP):
    print("\t\t[+] Running Scan [+]\n")
    subprocess.run(["nmap -T4 -A -v {} -oN Scan.txt".format(IP)], shell = True)
    print("\t\t[+] NMAP Scan Complete [+]\n")

parser = argparse.ArgumentParser(description = 'Your Average Scanner', epilog = 'Use Responsibly!')
parser.add_argument('IP', help = "Target IP", nargs = '+')
parser.add_argument('--opt', help = "Options Mode [Default -> 2]: 1 -> Port find, 2 -> NMAP scan, 3 -> Port Find and Run Scan. [Only on TCP Ports]", metavar = 'OPTION', default = 2)
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
    if opt == 1:
        portFind(IP)
    elif opt == 2:
        Scan(IP)

print("\n\t\t[+] Scan Complete [+]")