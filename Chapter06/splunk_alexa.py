from splunkquery import run
def alexa(data,resp):
    try:
        string=data.split(' ')
    except:
        string=data
    search=' '.join(string[0:-1])
    param=string[-1]
    print("param"+param)
    match_dict={0:"routers management interface",1:"routers management loopback"}
    for no in range(2):
        print(match_dict[no].split(' '))
        print(search.split(' '))
        test=list(map(lambda x:x in search.split(' '),match_dict[no].split(' ')))
        print(test)
        print(no)
        if False in test:
            pass
        else:
            if no in [0,1]:
                if param.lower()=="up":
                    query="search%20index%3D%22main%22%20earliest%3D0%20%7C%20dedup%20interface_name%2Crouter_name%20%7C%20where%20interface_name%3D%22Loopback45%22%20%20and%20interface_status%3D%22up%22%20%7C%20table%20router_name"
                elif param.lower()=="down":
                    query="search%20index%3D%22main%22%20earliest%3D0%20%7C%20dedup%20interface_name%2Crouter_name%20%7C%20where%20interface_name%3D%22Loopback45%22%20%20and%20interface_status%21%3D%22up%22%20%7C%20table%20router_name"
                else:
                    return "None"
                result=run(query,resp)
                return result
