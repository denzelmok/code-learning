# adapted from: https://www.geeksforgeeks.org/website-blocker-using-python/

import time
from datetime import datetime as dt

# hosts path, dependent on OS
# hosts_path = '/etc/hosts' # Max and Linux
hosts_path = 'C:\Windows\System32\drivers\etc'
# localhosts IP
redirect = '127.0.0.1'

# websites that you want to block
default_list = ['google.com',
                'facebook.com',
                'twitter.com'
                'reddit.com']

# additional websites to block
additional_list = []
while input('More websites? y or n') is not 'n':
    additional_list = additional_list.append(input('Enter site: '))

default_list = default_list.append(additional_list)

while True:
    # time of your work
    if dt(dt.now().year, dt.now().month, dt.now().day, 8)
        < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Working hours...')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in default_list:
                if website in content:
                    pass
                else:
                    # map hostnames to localhost IP address
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            # remove hostnames from host file
            file.truncate()
        print('Fun hours...')
    time.sleep(5)