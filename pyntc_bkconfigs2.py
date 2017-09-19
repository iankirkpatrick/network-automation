from pyntc import ntc_device as NTC

#Define device list
device_list = ['192.168.122.2',
               '192.168.122.226',
               ]
#Loop for each device
for device in device_list:
    iosvl2 = NTC(host=device, username='ian', password='cisco', device_type='cisco_ios_ssh')
    print ('Accessing device ' + str(device))
    #Open SSH session to device and backup config to file
    iosvl2.open()
    ios_run = iosvl2.backup_running_config(str(device) + '.cfg')

    iosvl2.close()
