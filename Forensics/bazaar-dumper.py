#!/usr/bin/env python3
import subprocess

def run_cmd(cmd):
    return subprocess.check_output([cmd], shell=True).decode()

last_rev = int(run_cmd('bzr revno'))

for revno in range(1, last_rev + 1):
    filenames = run_cmd(f'bzr ls -r {revno}').split(' ')
    for filename in filenames:
        if filename.strip() != '':
            content = run_cmd(f'bzr cat -r {revno} {filename}')
            if content.strip() != '':
                print(f'{revno} - {filename.strip()}\n\n{content}')
                print('='*80)
