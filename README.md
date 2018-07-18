# sim7600_driver
sim7600 driver for ubuntu

put gprs-connect-chat, gprsdial, startup.sh to /etc/ppp/

autorun with system startup, edit /etc/rc.local, add "sh etc/ppp/startup.sh"

auto check ppp status 
    edit .profile, add " nohup python /path/to/this/git/monitor_ppp.py 2>&1 &"
