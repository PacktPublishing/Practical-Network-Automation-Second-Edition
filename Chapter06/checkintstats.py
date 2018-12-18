# cocurrent threads executed at a time - 25
# each thread connect to the router . fetch show interfaces output
# invoke fetch_interface_summary and get the interface names in a list format
# network device ips are input in allips variable
# this takes around 30 secs to execute
# data is written on c:\splunklogs\network_device_stats_details.txt

import re
import netmiko
import time
import datetime
import math
from threading import Thread
import logging
import threading
from random import randrange
import itertools
import itertools
import sys
import base64

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

lck = threading.Lock()
splitlist = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

absolute_path = "c:\\splunklogs\\"
filename1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
full_filename = "network_device_stats_details.txt"
abs_filename = absolute_path+full_filename

with open(abs_filename, "w") as text_file:
    text_file.close()

def get_interface_name(interface_details):
    ''' fetch interface name from the interface description'''
    m = re.search('(^[a-zA-Z0-9/-]*) is ',interface_details)
    if m:
        interface_name_fetched = m.group(1).strip(",")
    else:
        interface_name_fetched = 'NULL'
    return interface_name_fetched

def fetch_router_interface_stats(device_type,routerip,username,password,timestamp,enable_passwd = ''):
    '''fetch the interface stats from a network'''
    router = {
    'device_type' : device_type,
    'ip' : routerip,
    'username' : username,
    'password' : password,
    'secret' : enable_passwd
    }
    global lck
    try:
        net_connect = netmiko.ConnectHandler(**router)
        print("connect to router {} is successful ".format(routerip))
    except Exception as ex:
        print("connect to router {} is not successful ".format(routerip))
        print (ex)
        return
    # this is the list of dictionaries filled with all stats
    router_stats = []
    router_hostname = net_connect.find_prompt()
    router_hostname = router_hostname.strip('#')
    output = net_connect.send_command("term length 0")
    time.sleep(1)
    print("router name is {}".format(router_hostname))
    interface_details = net_connect.send_command("show interfaces")
    time.sleep(4)
    interface_list = fetch_interface_summary(interface_details)
    #print("List of interfaces : {}".format(interface_list))
    parsedconfig=parseconfig(interface_details)
    #print("parsedconfig is {}".format(parsedconfig))
    i = 0
    for item in parsedconfig:
        if len(parsedconfig[i]) > 3:
            parsedconfig[i] = '\n'.join(parsedconfig[i])
        i = i+1
    #print("parsedconfig is {}".format(parsedconfig))
    for item in parsedconfig:
        #print("the interface desc is {}".format(item))
        interface_name = get_interface_name(item)
        if interface_name.strip() in interface_list:
            router_stats.append(fetch_interface_stats(item,interface_name))
    #print("router_stats is {}".format(router_stats))
    net_connect.disconnect()
    lck.acquire()
    with open(abs_filename, "a+") as text_file:
        for interface_stats in router_stats:
            text_file.write("{},router_name={},interface_name={},interface_description={},interface_status={},line_protocol={},ip_address={},input_errors={},CRC={},output_errors={},interface_resets={},reliability={},txload={},rxload={},bandwidth={},input_queue_drops={},output_queue_drops={}".format(timestamp,router_hostname,interface_stats['interface_name'],interface_stats['interface_description'],interface_stats['interface_status'],interface_stats['line_protocol'],interface_stats['ip_address'],interface_stats['input_errors'],interface_stats['CRC'],interface_stats['output_errors'],interface_stats['interface_resets'],interface_stats['reliability'],interface_stats['txload'],interface_stats['rxload'],interface_stats['bandwidth'],interface_stats['input_queue_drops'],interface_stats['output_queue_drops']))
            text_file.write('\n')
    lck.release()
    return

def fetch_interface_summary(ip_interface_brief):
    '''this func will  extract interfaces from show interfaces CLI output. returns the list of interface names'''
    interface_list = []
    tmplist=ip_interface_brief.split("\n")
    for item in tmplist:
        if 'line protocol' in item:
            item = item.strip()
            if item.split()[0].lower() != 'interface'.lower() and 'deleted' not in item:
                interface_list.append(item.split()[0].strip())
    return interface_list

def fetch_interface_stats(interface_details,interface_name) :
    ''' returns interface_description,interface_status,line_protocol,ip_address,input_errors,CRC,output_error,interface_resets'''
    stats = {}
    m = re.search('([\d]+) interface resets',interface_details)
    if m:
        interface_resets = int(m.group(1))
    else:
        interface_resets = -1
    m = re.search('([\d]+) output errors',interface_details)
    if m:
        output_error = int(m.group(1))
    else:
        output_error = -1
    m = re.search('([\d]+) CRC',interface_details)
    if m:
        CRC = int(m.group(1))
    else:
        CRC = -1
    m = re.search('([\d]+) input errors',interface_details)
    if m:
        input_errors = int(m.group(1))
    else:
        input_errors = -1   
    m = re.search('Internet address is (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d{1,2}|))',interface_details)
    if m:
        ip_address = m.group(1)
    else:
        ip_address = 'NULL'   
    m = re.search('line protocol is ([a-zA-Z]+)',interface_details)
    if m:
        line_protocol = m.group(1)
    else:
        line_protocol = 'NULL'
    m = re.search(interface_name+' is ([a-zA-Z ]+,)',interface_details)
    if m:
        interface_status = m.group(1).strip(",")
    else:
        interface_status = 'NULL'
    m = re.search('Description: ([a-zA-Z0-9_ -:]*)',interface_details)
    if m:
        interface_description = m.group(1).strip()
    else:
        interface_description = 'NULL'
    m = re.search('reliability ([0-9]*)',interface_details)
    if m:
        reliability = m.group(1).strip()
    else:
        reliability = -1
    m = re.search('txload ([0-9]*)',interface_details)
    if m:
        txload = m.group(1).strip()
    else:
        txload = -1
    m = re.search('rxload ([0-9]*)',interface_details)
    if m:
        rxload = m.group(1).strip()
    else:
        rxload = -1
    m = re.search('BW ([0-9]*)',interface_details)
    if m:
        bandwidth = m.group(1).strip()
    else:
        bandwidth = -1
    m = re.search('Input queue: \d{1,4}\/\d{1,4}\/(\d{1,4})\/\d{1,4}',interface_details)
    if m:
        input_queue_drops = m.group(1).strip()
    else:
        input_queue_drops = -1
    m = re.search('Total output drops: ([0-9]*)',interface_details)
    if m:
        output_queue_drops = m.group(1).strip()
    else:
        output_queue_drops = -1
    stats['interface_name'] = interface_name
    stats['interface_description'] = interface_description
    stats['interface_status'] = interface_status
    stats['line_protocol'] = line_protocol
    stats['ip_address'] = ip_address
    stats['input_errors'] = input_errors
    stats['CRC'] = CRC
    stats['output_errors'] = output_error
    stats['interface_resets'] = interface_resets
    stats['reliability'] = reliability
    stats['txload'] = txload
    stats['rxload'] = rxload
    stats['bandwidth'] = bandwidth
    stats['input_queue_drops'] = input_queue_drops
    stats['output_queue_drops'] = output_queue_drops
    return stats

def fetch_stats_multithread(allips,device_type,username,password,timestamp):
    ''' fetch stats of network devices using multi threading '''
    splitsublist=splitlist(allips,25)
    for subiplist_iteration in splitsublist:
        threads_imagex= []
        for deviceip in subiplist_iteration:
            t = Thread(target=fetch_router_interface_stats, args=(device_type,deviceip,username,password,timestamp))
            t.start()
            time.sleep(randrange(1,2,1)/20)
            threads_imagex.append(t)

        for t in threads_imagex:
            t.join()

username = 'test'
#password = 'XXXXXXX'
# encrypted password
content = 'dGVzdA=='
passwd = base64.b64decode(content)
password = passwd.decode("utf-8")
device_type = 'cisco_ios'
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

### All out routers for the stats to be fetched
allips = ['192.168.20.1','192.168.20.2','192.168.20.3','192.168.20.4']

fetch_stats_multithread(allips,device_type,username,password,timestamp)


