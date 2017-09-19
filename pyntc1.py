import json
from pyntc import ntc_device as NTC

#Define parameters to establish SSH session
iosvl2 = NTC(host='192.168.122.2', username='ian', password='cisco', device_type='cisco_ios_ssh')

#Open SSH session
iosvl2.open()

#Gather uptime, interfaces etc. from device
ios_output = iosvl2.facts
#Utilise json to format output to more readable format
print (json.dumps(ios_output, indent=4))

#Apply configuration commands in list
iosvl2.config_list(['hostname s1_python'])
iosvl2.close()
