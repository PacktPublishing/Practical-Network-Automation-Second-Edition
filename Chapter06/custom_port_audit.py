from lxml import etree
from netmiko import ConnectHandler
import itertools

class linecheck:
    def __init__(self):
        self.state = 0
    def __call__(self, line):
        if line and not line[0].isspace():
            self.state += 1
        return self.state

def parseconfig(config):
    rlist=[]
    for _, group in itertools.groupby(config.splitlines(), key=linecheck()):
        templist=list(group)
        if (len(templist) == 1):
            if "!" in str(templist):
                continue
        rlist.append(templist)
    return rlist



def read_xml_metadata(link_profiles="LinkDescriptionProfiles.xml"):
    """
    """
    LP_MetaData = dict()

    try:
        lp_hnd = open(link_profiles, "r")
    except IOError as io_error:
        print(io_error)
        sys.exit()

    lp_data = lp_hnd.read()
    lp_hnd.close()
    lp_xml_tree = etree.fromstring(lp_data)

    lp_check_id = lp_xml_tree.xpath("/DescriptionProfiles/description/@id")
    lp_check_config = lp_xml_tree.xpath("/DescriptionProfiles/description/configuration")

    lp_lam = lambda config, name, LP_MetaData : LP_MetaData.update({name:config.split(";")})
    [lp_lam(config.text, name, LP_MetaData) for name, config in zip(lp_check_id, lp_check_config)]

    return LP_MetaData



LP_MetaData = read_xml_metadata()

ignorecommandlist=['ip address','shut']

def validateconfig(config1,config2,typeconfig):
    tmpval=""
    #del config2[0]
    ignore=False
    config2=",".join(config2)
    for line in config1:
        line=line.strip()
        if ("interface " in line):
            continue
        if (line in config2):
            continue
        else:
            if (typeconfig=="baseconfig"):
                tmpval=tmpval+"  + [{}]\n".format(line)
            else:
                for ignorecommand in ignorecommandlist:
                    if (ignorecommand in line):
                        ignore=True
                if (ignore):
                    ignore=False
                    tmpval=tmpval+"  *ignore [{}]\n".format(line)
                else:
                    tmpval=tmpval+"  - [{}]\n".format(line)
    return tmpval
    
    
    

ip="192.168.20.{0}".format(1)
print ("\nValidating for IP address ",ip)
device = ConnectHandler(device_type='cisco_ios', ip=ip, username='test', password='test')
deviceconfig = device.send_command("show run")

parsedconfig=parseconfig(deviceconfig)
tmpval=""
for interfaceconfig in parsedconfig:
    if ("interface " in interfaceconfig[0]):
        interfacename=interfaceconfig[0].split(' ')
        interface_name=None
        interface_name = [x for x in LP_MetaData.keys() if x.strip() == interfacename[1]]
        
        #### validate base config from fetched config
        if (len(interface_name) > 0 ):
            print (interface_name)
            getbaseconfig=LP_MetaData[interface_name[0]]
            #### validate fetched config from base config
            returnval=validateconfig(getbaseconfig,interfaceconfig,"baseconfig")
            print (returnval)
            #### validate base config from fetched config
            returnval=validateconfig(interfaceconfig,getbaseconfig,"fetchedconfig")
            print (returnval)
        else:
            tmpval="  *ignore [{}]\n".format(interfacename[1])
            #print (tmpval)
        #print (interfaceconfig)

