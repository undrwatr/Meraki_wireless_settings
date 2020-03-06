 #!/usr/bin/env python

#imports
import cred
import requests
import re

#Meraki website info
MERAKI_DASHBOARD = 'https://api.meraki.com'
HEADERS = {'X-Cisco-Meraki-API-Key': (cred.key), 'Content-Type': 'application/json'}

#Regex for pulling in just the APs
REGEX = re.compile("MR")

#NETWORK = input(str("What network are we looking at? "))
NETWORK = cred.network

#pull in all of the data from the network
NETWORK_URL = MERAKI_DASHBOARD + '/api/v0/networks/%s/devices' % NETWORK
NETWORK_GET = requests.get(NETWORK_URL, headers=HEADERS)
NETWORK_RESPONSE = NETWORK_GET.json()

#program to pull in the information for a wireless device
def WIRELESS_SETTINGS():
    WIRELESS_SETTINGS_URL = MERAKI_DASHBOARD + '/api/v0/networks/%s/devices/%s/wireless/status' % (NETWORK, DEVICE['serial'])
    WIRELESS_SETTINGS_GET = requests.get(WIRELESS_SETTINGS_URL, headers=HEADERS)
    WIRELESS_SETTINGS_RESPONSE = WIRELESS_SETTINGS_GET.json()
    for SSIDS in WIRELESS_SETTINGS_RESPONSE['basicServiceSets']:
        if SSIDS['enabled'] == True:
            print("SSID "  + (SSIDS['ssidName']) + " BAND " + (SSIDS['band']) + " BSSID " + str(SSIDS['bssid']) + " Channel " + str(SSIDS['channel']) + " Power " + str(SSIDS['power']))

#Based on the network it will pull in the APs for the network and then run the function against the devices.
for DEVICE in NETWORK_RESPONSE:
    if REGEX.match(DEVICE["model"]):
        print("AP " + DEVICE['name'])
        WIRELESS_SETTINGS()
