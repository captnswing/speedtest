#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket

if __name__ == '__main__':
    dropboxhome = '/volume1/storage/dropbox'
    if socket.gethostname().endswith('.local'):
        dropboxhome = os.path.expanduser('~/Dropbox')

    for root, dirs, files in os.walk(os.path.join(dropboxhome, 'speedtest')):
        for fn in files:
            lines = open(os.path.join(root, fn)).read().splitlines()
            timestamp = fn.rstrip('.txt').split('_')[1]
            label = lines[3].split(':')[0].replace(' ', '_')
            datapoints = {
                'ping': lines[3].split(': ')[1].rstrip(' ms'),
                'upload': lines[5].split(' ')[1],
                'download': lines[7].split(' ')[1]
            }
            for label, metric in datapoints.items():
                print "{} {} {}".format(timestamp, label, metric)
