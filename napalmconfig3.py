import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.2', 'ian', 'cisco')
iosvl2.open()

print ('Accessing 192.168.122.2 - Checking ACLs')
iosvl2.load_merge_candidate(filename='ACL1.cfg')

diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No ACL changes required')
    iosvl2.discard_config()

print ('Accessing 192.168.122.2 - Checking OSPF')
iosvl2.load_merge_candidate(filename='ospf1.cfg')

diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No OSPF changes required')
    iosvl2.discard_config()

iosvl2.close()
