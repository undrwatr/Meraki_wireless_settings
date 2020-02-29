 #!/usr/bin/env python

import cred
import requests

MERAKI_DASHBOARD = 'https://api.meraki.com'
HEADERS = {'X-Cisco-Meraki-API-Key': (cred.key), 'Content-Type': 'application/json'}

#NETWORK = input(str("What network are we looking at? "))
NETWORK = cred.network

NETWORK_URL = MERAKI_DASHBOARD + '/api/v0/networks/%s/devices' % NETWORK
NETWORK_GET = requests.get(NETWORK_URL, headers=HEADERS)
NETWORK_RESPONSE = NETWORK_GET.json()

def WIRELESS_SETTINGS():
    WIRELESS_SETTINGS_URL = MERAKI_DASHBOARD + '/api/v0/networks/%s/devices/%s/wireless/status' % (NETWORK, DEVICE['serial'])
    WIRELESS_SETTINGS_GET = requests.get(WIRELESS_SETTINGS_URL, headers=HEADERS)
    WIRELESS_SETTINGS_RESPONSE = WIRELESS_SETTINGS_GET.json()
    for SSIDS in WIRELESS_SETTINGS_RESPONSE['basicServiceSets']:
        if SSIDS['enabled'] == True:
            print("SSID "  + (SSIDS['ssidName']) + " BAND " + (SSIDS['band']) + " BSSID " + str(SSIDS['bssid']) + " Channel " + str(SSIDS['channel']) + " Power " + str(SSIDS['power']))

for DEVICE in NETWORK_RESPONSE:
    if DEVICE['model'] == "MR42":
        print("AP " + DEVICE['name'])
        WIRELESS_SETTINGS()
