import json
from napalm import get_network_driver

bgplist = ['192.168.122.226',
           '192.168.122.2',
           ]

for ip_address in bgplist:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv = driver(ip_address, 'ian', 'cisco')
    iosv.open()
    bgp_neighbors = iosv.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent = 4))
    iosv.close()
