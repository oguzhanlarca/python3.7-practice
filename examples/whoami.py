#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, json, datetime, time
import urllib.request ## instead of urllib2 like in Python 2.7
from os import path
from urllib import request
from datetime import date, time, timedelta
from time import sleep

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

def main():

  ## Operation System
  print(' ')
  print('###### -*-  github.com/oguzhanlarca/practices/examples/whoami.py -*- ######')
  print('---------------------------------------------------------------------------')
  print('System               : ' + os.name)
  print('Executables          : ' + os.defpath)
  print('Null Device          : ' + os.devnull)
  print('Current Directory    : /' + os.curdir)
  print('Parent Directory     : /' + os.pardir)
  print("Real Path            : " + str(path.realpath(".")))
  
  ## Make request via ipinfo.io
  ## Define a variable to hold the source URL
  urlData1 = "json"
  
  try:
    data = json.load(request.urlopen(urlData1))
  except Exception as e:
    print(e)
  else:
    print(' ')
    print('IP INFO')
    print('---------------------------------------------------------------------------')
    print('Main ISP             : {org}'.format(**data))
    print('Location             : {}E'.format(data['loc'].replace(',','N, ')) + ' | ' + '{city}, {region}, {country}, {postal}'.format(**data))
  
  ## Make request via wtfismyip.com
  ## Define a variable to hold the source URL
  urlData2 = "https://wtfismyip.com/json"
  urlData3 = "https://get.geojs.io/v1/dns/ptr/"
  try:
    data = json.load(request.urlopen(urlData2))
    ptrData = json.load(request.urlopen(urlData3 + '{YourFuckingIPAddress}'.format(**data) + '.json'))

  except Exception as e:
    print(e)
  else:
    print(' ')
    print('WTF IS MY IP & GEOJS')
    print('---------------------------------------------------------------------------')
    print('Fucking IP Address   : {YourFuckingIPAddress}'.format(**data))
    print('Fucking Location     : {YourFuckingLocation}, {YourFuckingCountryCode}'.format(**data))
    print('Fucking Hostname     : {YourFuckingHostname}'.format(**data))
    print('Fucking Sub ISP      : {YourFuckingISP}'.format(**data))
    print('Fucking Tor Exit     : {YourFuckingTorExit}'.format(**data))
    print('Reverse DNS PTR      : {ptr}'.format(**ptrData))

  url = ("http://ipvigilante.com/8.8.8.8/full")
  response = urlopen(url)
  data = response.read().decode("utf-8")
  data = json.loads(data)

  print(' ')  
  print('IP VIGILANTE')
  print('---------------------------------------------------------------------------')
  print("IPv4                 : " + str(data["data"]["ipv4"]))
  print("Hostname             : " + str(data["data"]["hostname"]))
  print("Continent code       : " + str(data["data"]["continent_code"]))
  print("Continent name       : " + str(data["data"]["continent_name"]))
  print("Country ISO code     : " + str(data["data"]["country_iso_code"]))
  print("Country name         : " + str(data["data"]["country_name"]))
  print("Subdivision 1 ISO    : " + str(data["data"]["subdivision_1_iso_code"]))
  print("Subdivision 1 name   : " + str(data["data"]["subdivision_1_name"]))
  print("Subdivision 2 ISO    : " + str(data["data"]["subdivision_2_iso_code"]))
  print("Subdivision 2 name   : " + str(data["data"]["subdivision_2_name"]))
  print("City name            : " + str(data["data"]["city_name"]))
  print("Metro code           : " + str(data["data"]["metro_code"]))
  print("Time zone            : " + str(data["data"]["time_zone"]))
  print("Postal code          : " + str(data["data"]["postal_code"]))
  print("Latitude             : " + str(data["data"]["latitude"]))
  print("Longitude            : " + str(data["data"]["longitude"]))
  print("Accuracy radius      : " + str(data["data"]["accuracy_radius"]))

if __name__ == "__main__":
  main()
  print(' ')
