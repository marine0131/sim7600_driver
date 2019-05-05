#! /usr/bin/env python


import os
import subprocess as sp
import time


def detect_route():
	sp.call('ip route list > ./ipout' , shell=True)

	route = []
	with open("./ipout") as f:
	    for ll in f.readlines():
		route.append(ll.split())

        if len(route) == 0:
            print "no route detected"
            return 0

	elif route[0][4]=='eth0':
	    # get ppp0 dev but default is not ppp0
	    print(route)
	    print "set ppp0 as default"
	    sp.call('sudo ip route change to default dev ppp0', shell=True)

	elif len(route) <= 2:
            for r in route:
                if 'ppp0' in r:
                    print('test ok')
                    return 0
	    # ppp0 dev not found
	    print route
	    print "restart ppp startup.sh"
	    sp.call('sudo sh /etc/ppp/startup.sh', shell=True)
	else:
            print('test ok')
	    return 0

if __name__ == "__main__":
        time.sleep(10)
	while True:
		print("time: ", time.strftime('%Y-%m-%d,%H:%M:%S',time.localtime(time.time())))
		detect_route()
		time.sleep(30)
