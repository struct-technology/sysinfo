# -*- coding: utf-8 -*-

import time
import config


def get_uptime_formatted(initial_time):
    """
    Funcation to make the difference between this current time and initial time and return formatted
    :param initial_time: timestamp
    :return: uptime: string
    """

    seconds = int(time.time()) - int(initial_time)

    days = seconds / config.DAY
    seconds -= days * config.DAY
    hours = seconds / config.HOUR
    seconds -= hours * config.HOUR
    minutes = seconds / config.MINUTE
    seconds -= minutes * config.MINUTE

    if days > 1:
        uptime = "%d days, " % days
    elif days == 1:
        uptime = "1 day, "
    else:
        uptime = ""

    return "%s%d:%02d:%02d" % (uptime, hours, minutes, seconds)