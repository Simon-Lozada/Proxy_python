#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket
import threading
import ServerConnect


class ProxyServer ( threading.Thread ):
	def__init__(self):
		threading.Thread.__init__ ( self )
		puerto = 8000;
		self.soc = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.soc.bind( (socket.gethostname(), puerto ) )
		self.soc.listen(100)
	
	def run ( self ):
	while True:
		channel, details = self.soc.accept()
		recibido = channel.recv(2048)
		print recibido
		respondo = ServerConnect.openPage(recibido)
		channel.send(respondo)
		channel.close()
		print respondo

ProxyServer().start()
