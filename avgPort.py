#!/usr/bin/python3
import logging
import subprocess
from scapy.all import *

class Portscan:
    def __init__(self):
        None

    def PortFind(self, IP_addr = None):           # Going to be Multi-Threaded for efficiency.
        logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
        print("\t\t[+] Running Port Find [+]\n")

        ip = IP_addr
        open_ports = []
        conf.verb = 0
        if self.ping_targ(ip):
            dest_ports = range(1, 1024)        # Use range(1, 1024) or reasonable till the dev of Multi-Threaded scanner!
            src = RandShort()

            for port in dest_ports:
                pack = IP(dst = ip)/TCP(sport = src, dport = port, flags = 'S')
                resp = sr1(pack, timeout = 2)

                if str(type(resp)) == "<type 'NoneType'>" or str(type(resp)) == "<class 'NoneType'>":#if str(type(resp)) == "<class 'NoneType'>":
                    continue
                elif resp.haslayer(TCP):
                    if resp.getlayer(TCP).flags == 0x12:
                        send_rst = sr(IP(dst = ip)/TCP(sport = src, dport = port, flags = 'AR'), timeout = 1)
                        open_ports.append(port)
                        print("[+] Found Open Port: {}".format(port))
                    elif resp.getlayer(TCP).flags == 0x14:
                        continue
        else:
            print("\t\t[!] Host is not Up! [!]")

        #print("Open Ports: {}".format(open_ports))
        print("\n\t\t[+] Port Scan Complete [+]\n")
        return open_ports

    def ScanWPorts(self, IP_addr, ports):
        print("\t\t[+] Running Port Scan { NMAP } [+]\n")
        subprocess.run(["nmap -T4 -A -v -p{} {} -oN Scan_Ports.txt".format(ports, IP_addr)], shell = True)
        print("\n\t\t[+] NMAP Port Scan Complete [+]")
    
    def ping_targ(self, IP_addr):
        ping = IP(dst = IP_addr)/ICMP()
        resp = sr1(ping, timeout = 10)
        if resp == None:
            return False
        return True

if __name__ == '__main__':
    Portscan