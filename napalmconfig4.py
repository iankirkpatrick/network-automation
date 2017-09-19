import json
from napalm import get_network_driver

device_list = ['192.168.122.2',
               '192.168.122.226',
               ]

for device in device_list:
    driver = get_network_driver('ios')
    iosvl2 = driver(device, 'ian', 'cisco')
    iosvl2.open()
    print ('Accessing device ' + str(device))
    print ('Checking ACLs')
    iosvl2.load_merge_candidate(filename='ACL1.cfg')

    diffs = iosvl2.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosvl2.commit_config()
    else:
        print('No ACL changes required')
        iosvl2.discard_config()

    print ('Checking OSPF')
    iosvl2.load_merge_candidate(filename='ospf1.cfg')

    diffs = iosvl2.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosvl2.commit_config()
    else:
        print('No OSPF changes required')
        iosvl2.discard_config()

    iosvl2.close()
