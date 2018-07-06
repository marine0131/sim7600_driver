# sim7600_driver
sim7600 driver for ubuntu

put gprs-connect-chat, gprsdial, start_ppp.py to /etc/ppp/

if eth0 also needed, you need to set ppp0 as default route
add fllow lines to /etc/rc.local
    route del default
    route add default dev ppp0
