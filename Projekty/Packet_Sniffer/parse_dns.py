#!/usr/bin/env python

import pprint
import socket
import struct


def decode_labels(message, offset):
    labels = []

    while True:
        length, = struct.unpack_from("!B", message, offset)
        
        if (length & 0xC0) == 0xC0:
            pointer, = struct.unpack_from("!H", message, offset)
            offset += 2
            return labels + decode_labels(message, pointer & 0x3FFF), offset

        if (length & 0xC0) != 0x00:
            raise Exception("unknown label encoding")

        offset += 1
        # print('Inside pointer')

        if length == 0:
            return labels, offset
       
        labels.append(*struct.unpack_from("!%ds" % length, message, offset))
        offset += length
  

def decode_question_section(message, offset, qdcount):
    DNS_QUERY_SECTION_FORMAT = struct.Struct("!2H")
    questions = []

    for _ in range(qdcount):
        qname, offset = decode_labels(message, offset)
        qtype, qclass = DNS_QUERY_SECTION_FORMAT.unpack_from(message, offset)
       # print(f'Qname - {qname} || Offset - {offset} || Qtype - {qtype} || Qclass - {qclass}')
        offset += DNS_QUERY_SECTION_FORMAT.size

        question = {"domain_name": qname,
                    "query_type": qtype,
                    "query_class": qclass}

        questions.append(question)

    return questions,offset



def decode_dns_message(message):
    
    DNS_QUERY_MESSAGE_HEADER = struct.Struct("!6H")
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
   # questions, offset = decode_question_section(message, offset, qdcount)

   #if qr == True:
   # answers, offset = decode_answers(message,offset,ancount)    
   
   
    # result = {"id": id,
    #           "is_response": qr,
    #           "opcode": opcode,
    #           "is_authoritative": aa,
    #           "is_truncated": tc,
    #           "recursion_desired": rd,
    #           "recursion_available": ra,
    #           "reserved": z,
    #           "response_code": rcode,
    #           "question_count": qdcount,
    #           "answer_count": ancount,
    #           "authority_count": nscount,
    #           "additional_count": arcount,
    #           "questions": questions}

    return [id,qr,opcode,aa,tc,rd,ra,z,rcode,qdcount,ancount,nscount,arcount]
    r#eturn result

def decode_answers(message,offset,ancount):
   
    DNS_ANSWER_HEADER = struct.Struct("!5H")
    answers = []

    for _ in range(ancount):
        qname,qtype,qclass,ttl,data_length = DNS_ANSWER_HEADER.unpack_from(message,offset)
        offset += DNS_ANSWER_HEADER.size
        
        answer =   {"domain_name": qname,
                    "query_type": qtype,
                    "query_class": qclass,
                    "ttl": ttl,
                    "data_length": data_length}
                     #qtype: 
        answers.append(answer)

def decode_cname(byte_stream, offset):
    pass

# def decode_a(byte_stream, offset):
#     pass
# def decode_aaaa(byte_stream, offset):
#     pass
# def decode_ns(byte_stream, offset):
#     pass
# def decode_mx(byte_stream, offset):
#     pass