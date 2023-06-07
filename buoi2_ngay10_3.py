# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:03:11 2023

@author: Admin
"""


import requests
if __name__=='__main__':
    url = 'https://facebook.com'
    req = {'smartkey':'somevalue'}
    r = requests.post(url,json=req)
    print(r.text)


# from bs4 import BeautifulSoup
# import requests
# from urllib.request import urlopen
# from urllib.request import Request
# if __name__=='__main__':
#    # query = {'q':'river','order':'popular','min_width':'800','min_height':'600'}
    
#     headers = requests.utils.default_headers()
#     url = 'https://forecast.weather.gov/MapClick.php?lat=44.12519983400006&lon=-84.19669749999997#.Y7zhVnZBxnI'
#     #headers = {'Content-Type':'application/json'}
#     req = requests.get(url,headers)
#     s = BeautifulSoup(req.content,'html.parser')
#     ngay = s.find(id = 'seven-day-forecast')
#     dubao = ngay.find_all(class_='tombstone-container')
#     tonight = dubao[0]
#     img=tonight.find('img')
#     mota = img['title']
#     print(mota)

#     req = Request(url)
#     r = urlopen(req)
#     #r = requests.get(url,auth=('thinh7','Thinh1911'))
#     print(req.redirect_dict)
