import requests
for line in open("ip.txt"):#ip列表文件位置
    url=line.strip('\n')
    if 'http' not in url:
            url = 'http://'+url                       
    if ':888/pma' not in url:
            url =url+ ':888/pma'
    try:
        geturl = requests.get(url,timeout=1)#超时参数
        status=geturl.status_code
        if status == 200:
            print (url+" 存在漏洞，请及时升级面板")
            pass
        else:
            print (url+" 路径不存在，不存在漏洞")       
            pass
    except :
        print (url+" 访问超时，端口未打开或拒绝访问")
        pass

