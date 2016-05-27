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
