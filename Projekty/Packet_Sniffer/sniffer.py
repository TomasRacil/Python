# if anyone is worndering, the undescores are here to prevent namespace conflictions.
import os as _os
import sys as _sys
import time as _time
import socket as _socket
import pdb

from struct import Struct as _Struct
from ipaddress import IPv4Address as _IPv4Address

import parse_dns

# assigning variables to direct function references.
_fast_time = _time.time
_write_err = _sys.stdout.write

tcp_header_unpack = _Struct('!2H2LB').unpack_from
udp_header_unpack = _Struct('!4H').unpack_from



class RawPacket:
    '''tcp/ip packet represented in class form. packet fields can be accessed via their corresponding attribute.'''

    def __init__(self, data):
        self.timestamp = _fast_time()
        self.protocol  = 0

        self._name = self.__class__.__name__

        self._dlen = len(data)

        # parsing ethernet header here because it is more efficient
        self.dst_mac = data[:6].hex()
        self.src_mac = data[6:12].hex()
        self._data   = data[14:]

    def __str__(self):
        return '\n'.join([
            f'{"="*32}',
            f'{" "*8}packet',
            f'{"="*32}',
            f'{" "*8}ethernet',
            f'{"-"*32}',
            f'src mac: {":".join(self.src_mac[i:i+2] for i in range(0, len(self.src_mac), 2))}',
            f'dst mac: {":".join(self.dst_mac[i:i+2] for i in range(0, len(self.dst_mac), 2))}',
            f'{"-"*32}',
            f'{" "*8}ip',
            f'{"-"*32}',
            f'header length: {self.header_len}',
            f'protocol: {self.protocol}',
            f'src ip: {self.src_ip}',
            f'dst ip: {self.dst_ip}',
            f'{"-"*32}',
            f'{" "*8}protocol',
            f'{"-"*32}',
            f'src port: {self.src_port}',
            f'dst port: {self.dst_port}',
            f'{"-"*32}',
            f'{" "*8}payload',
            f'{"-"*32}',
            f'{self.payload}'
        ])

    def parse(self):
        '''index tcp/ip packet layers 3 & 4 for use as instance objects.'''

        self._ip()
        if (self.protocol == 6):
            self._tcp()

        elif (self.protocol == 17):
            self._udp()

        else:
            _write_err('non tcp/udp packet!\n')

    def _ip(self):
        data = self._data

        self.src_ip = _IPv4Address(data[12:16])
        self.dst_ip = _IPv4Address(data[16:20])

        self.header_len = (data[0] & 15) * 4
        self.protocol  = data[9]
        self.ip_header = data[:self.header_len]

        # removing ip header from data
        self._data = data[self.header_len:]

    # tcp header max len 32 bytes
    def _tcp(self):
        data = self._data

        tcp_header = tcp_header_unpack(data)
        self.src_port   = tcp_header[0]
        self.dst_port   = tcp_header[1]
        self.seq_number = tcp_header[2]
        self.ack_number = tcp_header[3]

        header_len = (tcp_header[4] >> 4 & 15) * 4
        self.proto_header = data[:header_len]
        self.payload = data[header_len:]


    # udp header 8 bytes
    def _udp(self):
        data = self._data

        udp_header = udp_header_unpack(data)
        self.src_port = udp_header[0]
        self.dst_port = udp_header[1]
        self.udp_len  = udp_header[2]
        self.udp_chk  = udp_header[3]

        source_port = self.src_port
        destination_port = self.dst_port

        self.proto_header = data[:8]
        self.payload = data[8:]
        if source_port or destination_port == 53:
            self._dns()
        # elif source_port or destination_port == 80:
        #     self._http()

    def _dns(self):
          parsed_dns = self.decode_dns_message(self.payload)
          print(parsed_dns)
    

    def decode_labels(self,message, offset):
        labels = []
        length = 0

        dns_label_len_unpack = _Struct('!B').unpack_from
        dns_label_pointer_unpack = _Struct('!H').unpack_from
        
       
        while True:
            length, = dns_label_len_unpack(message, offset)
            dns_label_unpack = _Struct('!%ds' % length).unpack_from
        
            if (length & 0xC0) == 0xC0:
                pointer, = dns_label_pointer_unpack(message, offset)
                offset += 2
                return labels + self.decode_labels(message, pointer & 0x3FFF), offset

            if (length & 0xC0) != 0x00:
                raise Exception("unknown label encoding")

            offset += 1

            if length == 0:
                return labels, offset

            labels.append(*dns_label_unpack(message, offset))
            offset += length

    def decode_question_section(self,message, offset, qdcount):
        DNS_QUERY_SECTION_FORMAT = _Struct("!2H")
        questions = []
        record_types = {1:"A",28:"AAAA",5:"CNAME",15:"MX",2:"NS",12:"PTR",6:"SOA",33:"SRV",16:"TXT"}
        
        for _ in range(qdcount):
          
            qname, offset = self.decode_labels(message, offset)
            name = '.'.join([label.decode('ascii') for label in qname])
            
            qtype, _ = DNS_QUERY_SECTION_FORMAT.unpack_from(message, offset)
            offset += DNS_QUERY_SECTION_FORMAT.size

            #print(record_types[qtype])

            question = {"domain_name": name,
                        "query_type": record_types[qtype],
                        "query_class": "IN"}

            questions.append(question)
        
        return questions, offset


    def decode_dns_message(self,message):
        DNS_QUERY_MESSAGE_HEADER = _Struct("!6H")
        id, misc, qdcount, ancount, nscount, arcount = DNS_QUERY_MESSAGE_HEADER.unpack_from(message)
        
        qr = (misc & 0x8000) != 0
        opcode = (misc & 0x7800) >> 11
        aa = (misc & 0x0400) != 0
        tc = (misc & 0x200) != 0
        rd = (misc & 0x100) != 0
        ra = (misc & 0x80) != 0
        z = (misc & 0x70) >> 4
        rcode = misc & 0xF

        offset = DNS_QUERY_MESSAGE_HEADER.size
        questions, offset = self.decode_question_section(message, offset, qdcount)
       
        result = {"id": hex(id),
                  "is_response": qr,
                  "opcode": opcode,
                  "is_authoritative": aa,
                  "is_truncated": tc,
                  "recursion_desired": rd,
                  "recursion_available": ra,
                  "reserved": z,
                  "response_code": rcode,
                  "question_count": qdcount,
                  "answer_count": ancount,
                  "authority_count": nscount,
                  "additional_count": arcount,
                  "questions": questions}
        return result

   
    # def _http(self):
    #     pass

def parse(data):
    try:
        packet = RawPacket(data)
        packet.parse()

    except:
        pass

def main(intf):
    sock = _socket.socket(_socket.AF_PACKET, _socket.SOCK_RAW)
    try:
        sock.bind((intf, 3))
    except OSError:
        _sys.exit(f'cannot bind interface: {intf}! exiting...')
    else:
        _write_err(f'now listening on {intf}!')

    while True:
        try:
            data = sock.recv(2048)
        except OSError:
            pass

        else:
            parse(data)

if __name__ == '__main__':
    if _os.geteuid():
        _sys.exit('listener must be ran as root! exiting...')

    main('eth0')
