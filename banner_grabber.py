#!/usr/bin/python3

import socket

# Using a function
def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(15)
    print(str(s.recv(1024)).strip('b'))

def main():
    ip = input("Enter an IP address:\n ")
    port = str(input("Enter a Port number:\n "))
    banner(ip, port)

main()
