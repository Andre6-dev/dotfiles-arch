#!/bin/sh
xrandr --output DVI-D-0 --off --output HDMI-0 --mode 1920x1080 --pos 760x0 --rotate normal --output DP-0 --primary --mode 3440x1440 --pos 0x1080 --rotate normal --output DP-1 --off

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & # start polkit agent from GNOME

xfce4-power-manager &
# ----- Fix cursor ----- #
picom --config $HOME/.config/picom/picom.conf &
xsetroot -cursor_name left_ptr &

/usr/lib/xfce4/notifyd/xfce4-notifyd &

feh --no-fehbg --bg-fill '/home/andre/Pictures/wallpapers/default.jpg' &
udiskie -t &
volumeicon &
nm-applet &

