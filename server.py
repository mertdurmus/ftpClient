# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:58:49 2020

@author: elifaskvav
"""

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "C:/Users/mert5/Desktop/ftp server", perm="elradfmw")
authorizer.add_anonymous("C:/Users/mert5/Desktop", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler)
server.encoding='utf-8'
server.serve_forever()