#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket
import re

def openPage(headers):
	regexp = re.search("Host:(.*)", headers)

	respuesta= ''

	if regexp:
		host = regexp.group(1).strip()
		vHost= host.split(":")
		port = 80
		if len(vHost) == 2:
			port = int(vHost[1])
			host = vHost[0]

		SO_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		SO_cliente.connect((host, port)) 	# Me conecto al servidor

		arrayHeaders= headers.split("\n")
		for h in arrayHeaders:
			SO_cliente.send(h+"\n")

		bufsize = 1024				# Size maximo que voy a recivir
		dataRec = ''

		while True:
			data = SO_cliente.recv(bufsize)	# Datos que recivo del servidor
			if not data: break
			dataRec += data
		SO_cliente.close()
		respuesta= dataRec

		return respuesta