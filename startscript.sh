: <<'COMMENT'
# Refrence link https://www.raspberrypi.org/forums/viewtopic.php?t=27500

we need to add  a file called /etc/xdg/autostart/RPi-infoscreen.desktop
code is:

[Desktop Entry]
Type=Application
Name=RPi-infoscreen
Comment=Kivy RPI Infoscreen
NoDisplay=false
Exec=/usr/bin/lxterminal -e /home/pi/FuelProject1/startScript.sh
NotShowIn=GNOME;KDE;XFCE;

COMMENT


#!/bin/bash
cd /home/pi/FuelProject1
/usr/bin/python main.py
