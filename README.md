# sim7600_driver
sim7600 driver for ubuntu

put gprs-connect-chat, gprsdial, startup.sh to /etc/ppp/

autorun with system startup, edit /etc/rc.local, add "sh etc/ppp/startup.sh"

auto check ppp status 
    edit .profile, add "/path/to/this/git/start_monitor.sh > 1.log"
