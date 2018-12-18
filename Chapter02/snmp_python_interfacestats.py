from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

for n in range(1, 3):
    server_ip="192.168.20.{0}".format(n)
    print ("\nFetching stats for...", server_ip)
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
        cmdgen.CommunityData('mytest'),
        cmdgen.UdpTransportTarget((server_ip, 161)),
        0,25,
        '1.3.6.1.2.1.2.2.1.2'
    )

    for varBindTableRow in varBindTable:
        for name, val in varBindTableRow:
            print('%s = Interface Name: %s' % (name.prettyPrint(), val.prettyPrint()))


