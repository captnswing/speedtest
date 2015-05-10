#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket
import json

if __name__ == '__main__':
    dropboxhome = '/volume1/storage/dropbox'
    if socket.gethostname().endswith('.local'):
        dropboxhome = os.path.expanduser('~/Dropbox')

    ping_ds = list()
    upload_ds = list()
    download_ds = list()

    for root, dirs, files in os.walk(os.path.join(dropboxhome, 'speedtest')):
        for fn in files:
            if not fn.endswith('.txt'):
                continue
            lines = open(os.path.join(root, fn)).read().splitlines()
            timestamp = fn.rstrip('.txt').split('_')[1]
            source = lines[3].split(':')[0]  # .replace(' ', '_')
            ping = lines[3].split(': ')[1].rstrip(' ms')
            download = lines[5].split(' ')[1]
            upload = lines[7].split(' ')[1]
            ping_ds.append([int(timestamp) * 1000, float(ping)])
            upload_ds.append([int(timestamp) * 1000, upload])
            download_ds.append([int(timestamp) * 1000, download])

    ping = [
        {
            'color': u'#FF0000',
            'lines': {u'show': True},
            'points': {
                'fillColor': u'#FF0000',
                'show': True
            },
            'data': ping_ds,
            'label': u'ping (ms)',
        }
    ]
    json.dump(ping, open(os.path.join(dropboxhome, "speedtest", "ping.json"), 'w'), indent=4)
    downup = [
        {
            'color': u'#23c200',
            'lines': {u'show': True},
            'points': {
                'fillColor': u'#23c200',
                'show': True
            },
            'data': download_ds,
            'label': u'download (Mbit/s)',
        },
        {
            'color': u'#2249c2',
            'lines': {u'show': True},
            'points': {
                'fillColor': u'#2249c2',
                'show': True
            },
            'data': upload_ds,
            'label': u'upload (Mbit/s)',
        }
    ]
    json.dump(downup, open(os.path.join(dropboxhome, "speedtest", "downup.json"), 'w'), indent=4)
