# -*- coding: utf-8 -*-


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    print get_hmm()


def hmm():
    """Contemplation..."""

if __name__ == '__main__':
    from ssh_handler import SSHClientHandler
    ssh_client = SSHClientHandler('vagrant', 'vagrant', port=2222)
    print ssh_client.run_command("uptime")

    from helpers.xml_parser import xml_to_list

    print xml_to_list('../resources/config.xml')
