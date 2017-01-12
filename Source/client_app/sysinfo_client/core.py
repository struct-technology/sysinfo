# -*- coding: utf-8 -*-

import json, psutil, helpers


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
        self.usage['uptime_total'] = helpers.get_uptime_formatted(psutil.boot_time())
        print 'uptime:', self.usage['uptime_total']
