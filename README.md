# HackingScripts

## **ATTENTION**
**All scripts in this repo was created with educational purposes!** <br/>
**I am not responsible for using these scripts by other users**

### Preliminary preparations
If you want to use this script, you should install aircrack-ng from the official site https://www.aircrack-ng.org/ <br/>
or you may download it using package managers like apt-get, pacman

### Python Script
Instruction how to use python scripts (bash is recommended, but if you really want python)
  1. Open two shell terminals and run them as a root:
  ```
  su
  ```
  2. Run first python script to capture data
  ```
  python data_capturing.py
  ```
  3. While firt script is capturing data - run second script to attack hotspot:
  ```
  python attack_hotspot.py
  ```

### Shell Scripts
Instruction how to use bash scripts:
  1. Give yourself permission to execute .sh files: 
  ```
  chmod +x *.sh
  ```
  2. Open second terminal as a root:
  ```
  su
  ```
  3. Run file for capturing data with command:
  ```
  ./data_collection.sh
  ```
  4. Run file to attack hotspot and enumerate passwords:
  ```
  ./attack_hotspot.sh
  ```
  NOTE: You have to have /usr/share/wordlists/rockyou.txt file . Or you may change dictionary for cracking in the second scipt.s
