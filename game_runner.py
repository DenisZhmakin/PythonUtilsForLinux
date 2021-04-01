#!/usr/bin/env python3
import subprocess

NAME_OF_THE_GAME = 'Omega Strike'
GAME_PATH = '/home/dragon/Games/OmegaStrike/OmegaStrike.exe'

if __name__ == '__main__':
    args = ['zenity', '--question', f'--title={NAME_OF_THE_GAME}',
            '--text=Запустить вместе с mangohud?', '--width=250', '--height=80']
    process = subprocess.Popen(args, text=True)

    process.communicate()
    if process.returncode == 0:
        subprocess.run(['mangohud', 'wine', GAME_PATH])
    else:
        subprocess.run(['wine', GAME_PATH])
