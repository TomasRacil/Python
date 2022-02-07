

from scapy.all import *
from scapy.layers.http import *
from scapy.layers.dns import *

import time
from time import sleep
from threading import Thread
from queue import Queue

# Intialization of global variables

packet_num = 0
username = ''
password = ''
start_time = time.time()

# This module utilizes a scapy utility to captures packet on specified network interface. 
# On class intialization run funciton starts async scapy function "AsyncSniffer" in a new thread a captures communication on ports 80, 53 and 21.
# In order to pass captured packets into the gui module and the recorder module, two queues(graphicalQueue and fileQueue) are filled.

class Sniffer(Thread):
    """ Constructor - it takes graphicalQueue and fileQueue which are filled with captured packets.
	    Args:
		    parameters: graphicalQueue: Queue, fileQueue: Queue, interface(str) - sets network interface which will be sniffed
    """
    def __init__(self, graphicalQueue: Queue, fileQueue: Queue, interface):
     super().__init__()
     self.gq = graphicalQueue
     self.fq = fileQueue
     self.pauseFlag = False
     self.stopFlag = False
    
     self.interface = interface

    def run(self):
        """ Fucntion - it starts sniffPacket function in new thread.
	        Args:
		        parameters: instance of Sniffer
        """
        print("Spousteni Snifferu... ")
        self.sniff_packet(self.interface)
        print("Ukonceni Snifferu...")

    def sniff_packet(self,iface=None):
        """ Function - Initializes packet counter and initializes async class AsyncSniffer, which captures packet in non-blocking way. 
	        Args:
		        parameters: instance of Sniffer, iface(str) - interface name
        """
        global packet_num
        packet_num =0
        data = None
# docs https://scapy.readthedocs.io/en/latest/usage.html#asynchronous-sniffing
        if iface:
          data = AsyncSniffer(filter="port 80 or port 21 or port 53",prn=self.process_packet, iface=iface, store=False)
 
        else:
          data = AsyncSniffer(filter="port 80 or port 21 or port 53",prn=self.process_packet, store=False)

        data.start()
     
        while not self.stopFlag:
            if self.pauseFlag:
                sleep(0.05)
                data.stop()
                break


    def process_packet(self,packet):
        """ Callback funciton - it measure elapsed time of sniffing, parses captured packet by layers and application protocol.
	        Args:
		        parameters: instance of Sniffer, rawSocket output
        """
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
                    payload = method+" "+url+" "+version
                   
                    if packet.haslayer(Raw) and method == "POST":
                        postedData = str(packet[Raw].load)
                        keywords = ["login", "password", "username", "user", "pass"]
                        for keyword in keywords:
                            if keyword in postedData:
                                credentials = "&".join(postedData.split("&",2)[:2])
                            payload+=postedData
                    self.gq.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])
                    self.fq.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,packet_num,credentials])
               
                elif packet.haslayer(HTTPResponse):
                    code = packet[HTTPResponse].Status_Code.decode()
                    reason_phrase = packet[HTTPResponse].Reason_Phrase.decode()
                    version = packet[HTTPResponse].Http_Version.decode()
                    
                    payload = code+" "+reason_phrase+" "+version 
                    self.gq.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])
                    self.fq.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,packet_num,credentials])

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
                        "230 message  = successful login - capture data only if the credentials are valid"
                        credentials = username+"&"+password
                        username = ''
                        password = ''
                # Fill graphical and file queue with parsed packet strings
                self.gq.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])
                self.fq.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,packet_num,credentials])

        if packet.haslayer(UDP):    
            if packet.haslayer(DNS):
                protocol = "DNS"

                if packet.haslayer(DNSQR):
                    payload = "Standard query " + str(dnstypes[packet[DNSQR].qtype])+ " " + str(packet[DNSQR].qname)
                
                if packet.haslayer(DNSRR):
                    payload = "Standard response " + str(dnstypes[packet[DNSRR].type]) + " " + str(packet[DNSRR].rrname)+ " " + str(packet[DNSRR].rdata)
             # Fill graphical and file queue with parsed packet strings
            self.gq.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,credentials])
            self.fq.put([packet_num,timestmap,src_ip,dst_ip,protocol,packet_len,payload,packet_num,credentials])
            sleep(0.012)


