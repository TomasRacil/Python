from itertools import count
import queue
from scapy.all import *

from scapy.layers.http import *
from scapy.layers.dns import *
import time
from csv_parser import CSVParser
from datetime import datetime


packet_num = 0
username = ''
password = ''
start_time = time.time()


class Sniffer(Thread):

    def __init__(self, id, q,exit_flag,interface):
     super().__init__()
     self.id = id
     self.q = q
     self.interface = interface
     self.csvQueue = queue.Queue(20)
     self.flag = exit_flag
     print(f"{id}: Sniffer vytvoren")

    def run(self):
        print(f"{self.id} spousteni ... ")
        self.sniff_packet(self.interface)
        print(f"{self.id}: ukoncuji se...")

    def sniff_packet(self,iface=None):
  
        if iface and self.flag == False:
          data = AsyncSniffer(filter="port 80 or port 21 or port 53",prn=self.process_packet, iface=iface, store=False)
          data.start()
        else:
          data = AsyncSniffer(filter="port 80 or port 21 or port 53",prn=self.process_packet, store=False)
          data.start()
          csvThread = None
        while True:
            
            # print(data.results)
            if(self.csvQueue.full()):
                csvThread = Thread(target=CSVParser.write,args=[str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),self.csvQueue])
                csvThread.start()
                csvThread.join()
            if self.flag:
                data.stop()
            
                break

    def process_packet(self,packet):
        print(self.id)
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
            credentials = ''
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
                        postedData = str(packet[Raw].load)
                        keywords = ["login", "password", "username", "user", "pass"]
                        for keyword in keywords:
                            if keyword in postedData:
                                credentials = "&".join(postedData.split("&",2)[:2])
                            payload+=postedData
                    # self.q.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])
                    self.csvQueue.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])
                elif packet.haslayer(HTTPResponse):
                    code = packet[HTTPResponse].Status_Code.decode()
                    reason_phrase = packet[HTTPResponse].Reason_Phrase.decode()
                    version = packet[HTTPResponse].Http_Version.decode()
                    
                    payload = code+" "+reason_phrase+" "+version 
                    self.q.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])
                    self.csvQueue.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])

            if (dst_port == 21 or src_port == 21) and (packet.haslayer(Raw)):
                protocol = "FTP"
                payload= str(packet[Raw].load)
                global username, password

                if 'USER' in payload:
                    username = payload.split('USER ')[1].strip().replace("\\r\\n'","")
                elif 'PASS' in payload:
                    password = payload.split('PASS ')[1].strip().replace("\\r\\n'","")
                else:
                    if '230' in payload:
                        credentials = username+"&"+password
                        username = ''
                        password = ''
                        print(credentials)
                self.q.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])
                self.csvQueue.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])

        if packet.haslayer(UDP):    
            if packet.haslayer(DNS):
                protocol = "DNS"

                if packet.haslayer(DNSQR):
                    payload = "Standard query " + str(dnstypes[packet[DNSQR].qtype])+ " " + str(packet[DNSQR].qname)
                
                if packet.haslayer(DNSRR):
                    payload = "Standard response " + str(dnstypes[packet[DNSRR].type]) + " " + str(packet[DNSRR].rrname)+ " " + str(packet[DNSRR].rdata)

            self.q.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])
            self.csvQueue.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])


def main():
    
    sniffer = Sniffer('Sniffer ID',queue.Queue,False)
    sniffer.start()
if __name__  == "__main__":
    main()
   