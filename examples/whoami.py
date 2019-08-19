#!/usr/bin/python3
import sys, os, json, datetime, time
import urllib.request ## instead of urllib2 like in Python 2.7
from os import path
from urllib import request
from datetime import date, time, timedelta
from time import sleep

def main():
  ## Operation System
  print(' ')  
  print('System               : ' + os.name)
  print('Executables          : ' + os.defpath)
  print('Null Device          : ' + os.devnull)
  print('Current Directory    : /' + os.curdir)
  print('Parent Directory     : /' + os.pardir)
  print("Real Path            : " + str(path.realpath(".")))
  
  ## Make request via ipinfo.io
  ## Define a variable to hold the source URL
  urlData1 = "http://ipinfo.io/json"
  
  try:
    data = json.load(request.urlopen(urlData1))
  except Exception as e:
    print(e)
  else:
    print(' ')  
    print('IP Address           : {ip}'.format(**data))
    print('Location             : {}E'.format(data['loc'].replace(',','N, ')) + ' | ' + '{city}, {region}, {country}, {postal}'.format(**data))
    print('Main ISP             : {org}'.format(**data))
  
  ## Make request via wtfismyip.com
  ## Define a variable to hold the source URL
  urlData2 = "https://wtfismyip.com/json"
  
  try:
    data = json.load(request.urlopen(urlData2))
  except Exception as e:
    print(e)
  else:
    print(' ')
    print('Fucking IP Address   : {YourFuckingIPAddress}'.format(**data))
    print('Fucking Location     : {YourFuckingLocation}, {YourFuckingCountryCode}'.format(**data))
    print('Fucking Hostname     : {YourFuckingHostname}'.format(**data))
    print('Fucking Sub ISP      : {YourFuckingISP}'.format(**data))
    print('Fucking Tor Exit     : {YourFuckingTorExit}'.format(**data))    

if __name__ == "__main__":
  main()
  print(' ')
