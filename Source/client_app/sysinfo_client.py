# -*- coding: utf-8 -*-

"""
SysInfo Client

Author: Matheus Santos <vorj.dux@gmail.com>
"""


import time, json, psutil


class Config:
    # Time constants
    MINUTE = 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24


class Helpers:

    @staticmethod
    def get_uptime_formatted(initial_time):
        """
        Funcation to make the difference between this current time and initial time and return formatted
        :param initial_time: timestamp
        :return: uptime: string
        """

        seconds = int(time.time()) - int(initial_time)

        days = seconds / Config.DAY
        seconds -= days * Config.DAY
        hours = seconds / Config.HOUR
        seconds -= hours * Config.HOUR
        minutes = seconds / Config.MINUTE
        seconds -= minutes * Config.MINUTE

        if days > 1:
            uptime = "%d days, " % days
        elif days == 1:
            uptime = "1 day, "
        else:
            uptime = ""

        return "%s%d:%02d:%02d" % (uptime, hours, minutes, seconds)


class SysInfoClientApp:

    def __init__(self):
        self.config_dict = {}
        self.alerts = []

        self.usage = {
            'cpu_usage': 0,
            'memory_usage': 0,
            'uptime_total': 0
        }

        self.bootstrap()

    def bootstrap(self):
        self.load_config_json()

    def load_config_json(self):
        with open('/tmp/client_config.json') as data_file:
            self.config_dict = json.load(data_file)
            self.alerts = self.config_dict.get('alerts')

    def check_usage(self):
        self.usage['cpu_usage'] = psutil.cpu_percent()
        print 'cpu_usage:', self.usage['cpu_usage']
        self.usage['memory_usage'] = psutil.virtual_memory().percent
        print 'memory_usage:', self.usage['memory_usage']
        self.usage['uptime_total'] = Helpers.get_uptime_formatted(psutil.boot_time())
        print 'uptime:', self.usage['uptime_total']


def run():
    sysinfo_client_app = SysInfoClientApp()

    print 'SysInfo Client App Running'

    # Daemon Process
    while True:
        sysinfo_client_app.check_usage()
        time.sleep(60)


if __name__ == '__main__':
    run()
