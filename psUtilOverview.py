# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:14:59 2022

@author: SamuelJames
"""

pid_utils = '''
>>> p.name()

>>> p.exe() --> this can be used to find any .exe location

>>> p.cwd()

>>> p.cmdline()

>>> p.parent()

>>> p.children(recursive=True)

>>> p.status()

>>> p.create_time()

>>> p.terminal()

>>> p.uids()

>>> p.gids()

>>> p.open_files()

--changing running processes:
>>> p.suspend()
>>> p.resume()
>>> p.terminate()
>>> p.kill()
>>> p.wait(timeout=3)    

print all process info:
    for proc in psutil.process_iter(['pid', 'name']):
...     print(proc.info)
'''

import psutil

addrs = psutil.net_if_addrs()

print('Processes:')
print(psutil.pids())

print('Addresses:')
for add in (addrs.keys()):
    print(add)
print('\n')

print('CPU Times:')
print(psutil.cpu_times())

print('\nUsers')
print(psutil.users())

print("\nNumber of cores in system", psutil.cpu_count())
print("\nCPU Statistics:")
print(psutil.cpu_stats())

print('\nCPU Frequency:')
print(psutil.cpu_freq())

print('\nLoad Average:')
print(psutil.getloadavg())

print('\nVmem:')
print(psutil.virtual_memory())

print('\nPartitions:')
print(psutil.disk_partitions())

print('\nDisk Usage:')
print(psutil.disk_usage('/'))

print('\nNetwork I/O stats:')
print(psutil.net_io_counters())

print('\nBattery:')
print(psutil.sensors_battery())

inp = input('\nWant to see all sockets? (there are over 20) [y/n]')
if inp == 'y' or inp == 'Y':
    print('\nSockets:')
    print(psutil.net_connections())

inp = input('\nWant to see all net interface cards? (there are over 20) [y/n]')
if inp == 'y' or inp == 'Y':
    print('\nCards:')
    print(psutil.net_if_addrs())
