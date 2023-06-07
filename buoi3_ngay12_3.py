# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 07:20:25 2023

@author: Admin
"""
'''
from bs4 import BeautifulSoup
import requests
if __name__=='__main__':
    url = 'https://forecast.weather.gov/MapClick.php?lat=44.12519983400006&lon=-84.19669749999997#.Y7zhVnZBxnI'
    headers = requests.utils.default_headers()
    req = requests.get(url,headers)
    s = BeautifulSoup(req.content,'html.parser')
    ngay = s.find_all(class_='tombstone-container')
    for i in range(9):
        tonight = ngay[i]
        img=tonight.find('img')
        mota = img['title']
        print(mota)
    Check = s.find_all('img')
    #Humidity = Check.find('td')
    print(len(Check))
'''
'''
import ipaddress as ip

if __name__=='__main__':
    class_c = '192.168.0.0'
    source = int(input("Enter prefix (24-30): "))
    if(source not in range(23,31)):
        raise Exception("Error")
    network_address = class_c+'/'+str(source)
    print('Network address: '+network_address)
'''
import ipaddress as ip

if __name__=='__main__':
    class_c = '192.168.0.0'
    source = int(input("Enter prefix (24-30): "))
    if(source not in range(24,31)):
        raise Exception("Error")
    network_address = class_c+'/'+str(source)
    print('Network address: '+network_address)
    try:
        network = ip.ip_network(network_address)
    except:
        raise Exception('Error')
    print('Number of ip address: %s'%(network.num_addresses))
    print('\t Netmask %s: '%(network.netmask))
    print('\t Broadcast: %s'%(network.broadcast_address))
    start_ip = list(network.hosts())[0]
    end_ip=list(network.hosts())[-1]
    print('\t Host from %s to %s'%(start_ip,end_ip))
    