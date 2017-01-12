"""
SysInfo Server

Author: Matheus Santos <vorj.dux@gmail.com>
"""

from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()

CLIENTS_XML_FILE = './resources/config.xml'

MAKE_PACKAGE_CLIENT_COMMAND = 'cd ../client_app && make package'

# API URL to allow the clients to post the encrypted data
SERVER_API = 'http://127.0.0.1:5000/'
