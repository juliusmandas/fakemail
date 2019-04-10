#!/usr/bin/python3

import sys
import socket

if(len(sys.argv) != 5):
	print("Usage: ./fakemail.py <MAIL_SERVER> <FAKE_MAIL> <TARGET_MAIL> <\"MESSAGE\">")

else:
	HOST = sys.argv[1]
	FAKEMAIL = sys.argv[2]
	TARGET = sys.argv[3]
	MESSAGE = sys.argv[4]

	# SMTP Protocol build
	HELO = ("HELO " + HOST + "\r\n").encode()
	FROM = ("MAIL FROM: <" + FAKEMAIL + ">\r\n").encode()
	TO = ("RCPT TO: <" + TARGET + ">\r\n").encode()
	DATA = ("DATA\r\nFrom: " + FAKEMAIL[0:FAKEMAIL.find("@")] + " <" + FAKEMAIL + ">\r\nTo: " + TARGET[0:TARGET.find("@")] + " <" + TARGET + ">\r\nSubject: " + TARGET[0:TARGET.find("@")] + "\r\n\r\n").encode()
	MSG = (MESSAGE + "\r\n.\r\n").encode()

	# Program start
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	sock.connect((HOST, 25))
	print(sock.recv(256).decode())

	sock.send(HELO)
	print(sock.recv(256).decode())

	sock.send(FROM)
	print(sock.recv(256).decode())

	sock.send(TO)
	print(sock.recv(256).decode())

	sock.send(DATA)
	print(sock.recv(256).decode())

	sock.send(MSG)
	print(sock.recv(256).decode())
	sock.close()
