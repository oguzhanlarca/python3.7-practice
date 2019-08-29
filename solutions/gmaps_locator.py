#!/usr/bin/python3
""" Geolocation via Google Maps API by Barron Stone for Code Clinic: Python """
import re
import subprocess
import requests

API_URL = 'https://www.googleapis.com/geolocation/v1/geolocate?key='
API_KEY = 'AIzaSyDcx8H9R5u5y5OKlnESfp1dZO0YtrEaMfM' # replace with your own Google Maps API key

# add wifi info to request if available
payload = {'considerIp': 'true'}
try:
    cmdout = subprocess.check_output('netsh wlan show networks mode=bssid').decode(encoding='utf_8')
    macs = re.findall(r'(?:[0-9a-fA-F]:?){12}', cmdout)
    signals = re.findall(r'([\d]+)(%)', cmdout)
    channels = re.findall(r'(Channel[\W]+: )([\d]+)', cmdout)
    if not (len(macs) == len(signals) == len(channels)):
        raise
except:
    print('Could not retrieve WiFi Access Points...')
else:
    print('Using {0} WiFi Access Point{1}...'.format(len(macs), 's' if (len(macs) > 1) else ''))
    wifi_list = []
    for i in range(len(macs)):
        wifi_list.append({'macAddress': macs[i],
                                            # convert signal strength to RSSI dBm
                          'signalStrength': str(int(signals[i][0]) / 2 - 100),
                          'channel': channels[i][1]})
    payload['wifiAccessPoints'] = wifi_list

# make request via Google Maps API
try:
    response = requests.post(API_URL+API_KEY, json=payload)
    data = response.json()
    if 'error' in data.keys():
        raise requests.RequestException('Error {0}: {1}'.format(data['error']['code'],data['error']['message']))
except Exception as e:
    print(e)
else:
    lat = data['location']['lat']
    lng = data['location']['lng']
    accuracy = data['accuracy']
    print('You are within {0}m of {1}N {2}E'.format(accuracy, lat, lng))
