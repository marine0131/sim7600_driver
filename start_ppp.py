#! /usr/bin/env python

import subprocess as sb

sb.call('sudo pppd file /etc/ppp/gprsdial', shell=True)
