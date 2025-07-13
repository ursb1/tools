import subprocess
import os

os.system('!chmod +x ./frpc')

command1 = [
    './frpc',
    '-c',
    'frpc01.ini'
]

command2 = [
    './frpc',
    '-c',
    'frpc02.ini'
]

process = subprocess.Popen(
    command1,
    text=True,
    start_new_session=True
)

process = subprocess.Popen(
    command2,
    text=True,
    start_new_session=True
)

text = '''
http://sj.frp.one:58000 ——> 8000
xg-4.frp.one:58080 ——> 8080
'''

print(text)