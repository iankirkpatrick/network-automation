import json
from pyntc import ntc_device as NTC

device_list = ['192.168.122.2',
               '192.168.122.226',
               ]

for device in device_list:
    iosvl2 = NTC(host=device, username='ian', password='cisco', device_type='cisco_ios_ssh')

    print ('Accessing device ' + str(device))
    iosvl2.open()
    ios_run = iosvl2.running_config

    print ('Running configuration from device ' + str(device))
    print (ios_run)

    print ('Saving device configuration to file')
    saveoutput = open('device' + str(device), 'w')
    saveoutput.write(ios_run)
    saveoutput.close

    iosvl2.close()
