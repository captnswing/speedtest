#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess as sp
import socket
import calendar
import datetime

if __name__ == '__main__':
    # No: timestamp = int(time.time())
    # Yes: https://github.com/flot/flot/blob/master/API.md#time-series-data
    timestamp = calendar.timegm(datetime.datetime.now().timetuple())
    server = '6061'
    filename = 'speedtest_{}.txt'.format(timestamp)
    speedtest = 'speedtest-cli'
    dropboxhome = '/volume1/storage/dropbox'
    if socket.gethostname().endswith('.local'):
        speedtest = os.path.expanduser('~/.virtualenvs/speedtest/bin/speedtest-cli')
        dropboxhome = os.path.expanduser('~/Dropbox')
    dropboxfolder = os.path.join(dropboxhome, 'speedtest')
    if not os.path.exists(dropboxfolder):
        os.mkdir(dropboxfolder)
    filename = os.path.join(dropboxfolder, filename)
    cmd = [speedtest, '--server', server]
    p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    output = p.communicate()[0]
    exit_code = p.returncode
    if exit_code:
        print "failed"
        print output
        sys.exit(-1)
    with open(filename, 'w') as f:
        f.write(output)
