#!/usr/bin/python3
import logging
from scapy.all import *

class Portscan:
    def __init__(self):
        None

    def PortFind(IP_addr = None):           # Going to be Multi-Threaded for efficiency.
        logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
        print("\t\t[+] Running Port Find [+]\n")

        ip = IP_addr
        dest_ports = range(1, 65535)        # Use range(1, 1024) or reasonable till the dev of Multi-Threaded scanner!
        open_ports = []
        conf.verb = 0
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

        #print("Open Ports: {}".format(open_ports))
        print("\t\t[+] Port Scan Complete [+]\n")
        return open_ports

if __name__ == '__main__':
    Portscan