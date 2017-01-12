import socket

import paramiko

from time import sleep


class SSHClientHandler(object):
    def __init__(self, username, password, ip='127.0.0.1', port=22):
        """
        Constructor to create a SSH Client instance and handle all operations
        :param username: string
        :param password: string
        :param ip: string
        :param port: int
        """
        self.ssh_client = paramiko.SSHClient()
        self.username = username
        self.password = password
        self.ip = ip
        self.port = port

        self.connect()

    def connect(self):
        """
        Connect method
        :return: connected: bool
        """
        try:
            self.set_key_policy()
            self.ssh_client.connect(self.ip, port=self.port, username=self.username, password=self.password)
        except (paramiko.BadHostKeyException, paramiko.AuthenticationException,
                paramiko.SSHException, socket.error), e:
            print 'Error to connect with \'%s:%s\':' % (self.ip, self.port), e
        except Exception, e:
            print 'Unexpected error to connect with \'%s:%s\':' % (self.ip, self.port), e
        finally:
            return self.is_connected()

    def disconnect(self):
        """
        Disconnect method
        """
        self.ssh_client.close()

    def is_connected(self):
        return self.ssh_client.get_transport() is not None and self.ssh_client.get_transport().is_active()

    def set_key_policy(self):
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def run_command(self, command, max_tries=5):
        """
        Execute command into client machine and return the stdout result
        :param command: string
        :param max_tries: int
        :return: stdout: list[unicode]
        """

        result = []

        if max_tries == 0:
            print 'Max tries exceeded.'
            return result

        if self.is_connected():
            try:
                stdin, stdout, stderr = self.ssh_client.exec_command(command)
                result = stdout.readlines()
            except paramiko.SSHException, e:
                print 'Error to execute command \'%s\' into \'%s:%s\':' % (command, self.ip, self.port), e
            except Exception, e:
                print 'Unexpected error to execute command \'%s\' into \'%s:%s\':' % (command, self.ip, self.port), e
            finally:
                return u''.join(result)
        else:
            self.connect()

            sleep(0.60)

            print 'Trying to reconnect #%d to \'%s:%s\'' % (max_tries, self.ip, self.port)
            # Recursion to try reconnect max_tries countdown times
            return self.run_command(command, max_tries=max_tries - 1)

    def send_file(self, local_path, remote_path):
        sftp = self.ssh_client.open_sftp()
        sftp.put(local_path, remote_path)
        sleep(1)
        sftp.close()
