import time

from core import SysInfoClientApp


def run():
    sysinfo_client_app = SysInfoClientApp()

    print 'SysInfo Client App Running'

    # Daemon Process
    while True:
        sysinfo_client_app.check_usage()
        time.sleep(60)


if __name__ == '__main__':
    run()
