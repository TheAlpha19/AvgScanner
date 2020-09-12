#!/usr/bin/python3
#avgscanner.py <IP> --opt <1, 2, 3>
import argparse
import subprocess
from avgPort import Portscan

def exit():
    print("\n\t\t[+] Quits [+]\n")
    quit()

'''
def portFind(IP, iface):
    print("\t\t[+] Running Port Find [+]\n")
    out = subprocess.run(['sudo', 'masscan', '-e', iface, '--rate=1000', '-p', '0-65535', IP], capture_output = True)
    #if out.stderr.decode() == '':
    print("{}".format(out.stdout.decode()))
    print("\n\t\t[+] Port Find Complete [+]\n")
    print("Error: {}".format(out.stderr.decode()))
    #else:
    #    print("[-] Error Encountered: {}\nMake sure to use a proper IP and Interface! [-]\n".format(out.stderr.decode()))
'''

def portFind(IP):
    obj = Portscan()
    ports = obj.PortFind(IP)
    print("Total Open Ports: {} [ ".format(len(ports)), end = '')
    for port in ports:
        print("{} ".format(port), end = '')
    print("]\n")
    if opt == 3:
        return ports

def Scan(IP):
    print("\t\t[+] Running Scan [+]\n")
    subprocess.run(["nmap -T4 -A -v {} -oN Scan.txt".format(IP)], shell = True)
    print("\t\t[+] NMAP Scan Complete [+]\n")

parser = argparse.ArgumentParser(description = 'Your Average Scanner', epilog = 'Use Responsibly!')
parser.add_argument('IP', help = "Target IP", nargs = '+')
parser.add_argument('--opt', help = "Options Mode [Default -> 2]: 1 -> Port find, 2 -> NMAP scan, 3 -> Port Find and Run Scan. [Only on TCP Ports]", metavar = 'OPTION', default = 2)
#parser.add_argument('--iface', help = "Network Adapter To Use [Default -> tun0]", default = 'tun0')
args = parser.parse_args()

IP = args.IP[0]
#iface = args.iface
try:
    opt = int(args.opt)
except:
    print("Option Should Be An Integer: 1, 2, or 3. See --help for scan options")
    exit()


if opt == 1:
    portFind(IP)

elif opt == 2:
    Scan(IP)

elif opt == 3:
    ret = portFind(IP)
    ports = str(ret)[1:-1].replace(" ", "")
    obj = Portscan()
    obj.ScanWPorts(IP, ports)

else:
    print("[-] Option Should Be 1, 2, or 3 (see --help) [-]")

print("\n\t\t[+] Scan Complete [+]")