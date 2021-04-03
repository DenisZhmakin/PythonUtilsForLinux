#!/usr/bin/env python3
import os
import subprocess

NAME_OF_THE_GAME = 'WRATH: Aeon of Ruin'
GAME_PATH = '/home/dragon/Games/AeonOfRuin/wrath.exe'
MANGOHUD_OPENGL = True

if __name__ == '__main__':
    args = ['zenity', '--question', f'--title={NAME_OF_THE_GAME}',
            '--text=Запустить вместе с mangohud?', '--width=250', '--height=80']
    process = subprocess.Popen(args, text=True)

    process.communicate()
    if not process.returncode:
        if MANGOHUD_OPENGL:
            # subprocess.run(['', ' mangohud', 'wine', GAME_PATH])
            os.system(f'env MANGOHUD_DLSYM=1 mangohud wine {GAME_PATH}')
        else:
            subprocess.run(['mangohud', 'wine', GAME_PATH])
    else:
        subprocess.run(['wine', GAME_PATH])
