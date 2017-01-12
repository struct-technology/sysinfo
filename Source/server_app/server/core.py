# -*- coding: utf-8 -*-
import json

import config
import hashlib

from subprocess import call

from helpers.xml_parser import xml_to_list

from helpers.ssh_handler import SSHClientHandler


class SysInfoApp:
    def __init__(self):
        self.config = config
        self.clients = []
        self.ssh_clients = {}

        self.bootstrap()

    def bootstrap(self):
        self.make_package_client_app()
        self.load_xml_clients()
        self.compute_hash_to_clients()
        self.connect_and_install_clients()

    def load_xml_clients(self, file_path=None):
        self.clients = xml_to_list(self.config.CLIENTS_XML_FILE if file_path is None else file_path)

    def compute_hash_to_clients(self):
        for client in self.clients:
            hash_object = hashlib.sha1(str(client))
            hex_dig = hash_object.hexdigest()
            client['hash'] = '%s' % hex_dig

    def make_package_client_app(self):
        call(self.config.MAKE_PACKAGE_CLIENT_COMMAND, shell=True)

    @staticmethod
    def open_file_get_content(file_path):
        f = open(file_path, 'r')
        result = f.readlines()[0]
        f.close()
        return result

    def connect_and_install_clients(self):
        for client in self.clients:
            ssh_client = self.ssh_clients[client.get('hash')] = SSHClientHandler(
                client.get('username'),
                client.get('password'),
                ip=client.get('ip'),
                port=int(client.get('port'))
            )

            if ssh_client.is_connected():

                client_config_object = {
                    'server_api_url': self.config.SERVER_API,
                    'hash': client.get('hash'),
                    'alerts': client.get('alerts')
                }

                client_config_path = '/tmp/client_config.json'

                package_path = '/tmp/package.txt'

                call('ls ../client_app/dist/*.tar.gz > %s' % package_path, shell=True)
                call('echo \'%s\' > %s' % (json.dumps(client_config_object), client_config_path), shell=True)

                package_file = self.open_file_get_content(package_path)
                package_file = package_file.replace('\n', '')
                file_name = package_file.split('/')[-1]
                ssh_client.send_file(package_file, '/tmp/%s' % file_name)

                ssh_client.send_file(client_config_path, client_config_path)

                print ssh_client.run_command('sudo pip uninstall sysinfo_client_app -y')
                print ssh_client.run_command('sudo pip install /tmp/%s' % file_name)

                print ssh_client.run_command('cat %s' % client_config_path)

                ssh_client.disconnect()
