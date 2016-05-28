#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
from scapy.error import Scapy_Exception

print """"
     ____           _                   ___
    / ___|__ _  ___| |_ _   _ ___      / _ \__      ___ __   ___ _ _
   | |   / _` |/ __| __| | | / __|    | | | \ \ /\ / / '_ \ / _ \ '__|
   | |__| (_| | (__| |_| |_| \__ \    | |_| |\ V  V /| | | |  __/ |
    \____\__,_|\___|\__|\__,_|___/_____\___/  \_/\_/ |_| |_|\___|_|
                                 |_____|
"""
print "Selecione umas das interfaces de rede disponiveis: "
net_interface = raw_input("Insira sua Interface de Rede: ")
print "Sua interface de rede foi adicionada"
filter_message = raw_input("Insira seu protocolo de rede: ")
arquivo = open("sniffer_output", "a") # gerando log. do arquivo


def s0ph0s_TCP(snin):
        if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 21 and snin.haslayer(Raw): # FTP service
                print snin.getlayer(Raw).load
		arquivo.write("%s \r\n" % snin.getlayer(Raw))
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 22 and snin.haslayer(Raw): # SSH service
                print snin.getlayer(Raw).load
		arquivo.write("%s \r\n" % snin.getlayer(Raw))
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 23 and snin.haslayer(Raw): # TELNET service
                print snin.getlayer(Raw).load
		arquivo.write("%s \r\n" % snin.getlayer(Raw))
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 25 and snin.haslayer(Raw): # SMTP service
                print snin.getlayer(Raw).load
		arquivo.write("%s \r\n" % snin.getlayer(Raw))
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 80 and snin.haslayer(Raw): # HTTP service
                print snin.getlayer(Raw).load
		arquivo.write("%s \r\n" % snin.getlayer(Raw))
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 110 and snin.haslayer(Raw): # POP3 service
                print snin.getlayer(Raw).load
		arquivo.write("%s \r\n" % snin.getlayer(Raw))
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 143 and snin.haslayer(Raw): # IMAP service
                print snin.getlayer(Raw).load
		arquivo.write("%s \r\n" % snin.getlayer(Raw))
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 133 and snin.haslayer(Raw): # IRC service
                print snin.getlayer(Raw).load
		arquivo.write("%s \r\n" % snin.getlayer(Raw))
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 161 and snin.haslayer(Raw): # SNMP service
                print snin.getlayer(Raw).load
		arquivo.write("%s \r\n" % snin.getlayer(Raw))
	if snin.haslayer(TCP) and snin.getlayer(TCP).dport == 194 and snin.haslayer(Raw): # IRC service
                print snin.getlayer(Raw).load
		arquivo.write("%s \r\n" % snin.getlayer(Raw))
sniff(iface=net_interface, prn=s0ph0s_TCP, store=0) # store = 0; not allocate in memory
arq.close() 
