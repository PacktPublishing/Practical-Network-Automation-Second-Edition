from netmiko import ConnectHandler

username = 'test'
password="test"
for n in range(1, 5):
    ip="192.168.20.{0}".format(n)
    device = ConnectHandler(device_type='cisco_ios', ip=ip, username='test', password='test')
    output = device.send_command("show version | in uptime")
    print (output)
