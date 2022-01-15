from itertools import count
from struct import pack
from scapy.all import *

from scapy.layers.http import *
from scapy.layers.dns import *

import os 
import sys
import time

packet_num = 0
start_time = time.time()

def sniff_packet(iface=None):

    if iface:
        sniff(filter="port 80 or port 21",prn=process_packet, iface=iface, store=False)
    else:
        sniff(prn=process_packet, store=False)


def process_packet(packet):
   
    timestmap = time.time() - start_time
    timestmap = int(timestmap * 1000)/1000.0
    packet_len = len(packet)

    dst_ip = packet[IP].dst
    src_ip = packet[IP].src

    dst_port = packet.dport
    src_port = packet.sport

    protocol = ''
    payload = ''

    if packet.haslayer(TCP) or packet.haslayer(UDP):
        global packet_num
        packet_num +=1

    if packet.haslayer(TCP):

        if packet.haslayer(HTTP):
            protocol = "HTTP"
            if packet.haslayer(HTTPRequest):
                url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
            #     # get the requester's IP Address
            #     # get the request method
                method = packet[HTTPRequest].Method.decode()
                version = packet[HTTPRequest].Http_Version.decode()
                # print(f"\n  {method} {url} {version}")
                payload = method+" "+url+" "+version

                if packet.haslayer(Raw) and method == "POST":
                   payload += packet[Raw].load.decode('utf-8')

            elif packet.haslayer(HTTPResponse):
                code = packet[HTTPResponse].Status_Code.decode()
                reason_phrase = packet[HTTPResponse].Reason_Phrase.decode()
                version = packet[HTTPResponse].Http_Version.decode()
                
                payload = code+" "+reason_phrase+" "+version 

 
            return [packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload]
        #FTP
        if (dst_port == 21 or src_port == 21) and (packet.haslayer(Raw)):
            protocol = "FTP"
            payload= packet[Raw].load

            return [packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload]
    
    if packet.haslayer(UDP):    
        if packet.haslayer(DNS):
            protocol = "DNS"

            if packet.haslayer(DNSQR):
                payload = "Standard query " + str(dnstypes[packet[DNSQR].qtype])+ " " + str(packet[DNSQR].qname)
            
            if packet.haslayer(DNSRR):
                payload = "Standard response " + str(dnstypes[packet[DNSRR].type]) + " " + str(packet[DNSRR].rrname)+ " " + str(packet[DNSRR].rdata)

        return [packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload]

def main():
    sniff_packet('eth0')


if __name__  == "__main__":
    main()
   