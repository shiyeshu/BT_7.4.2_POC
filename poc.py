import requests
def go(url):
        
        if 'http' not in url:
            url = 'http://'+url
            pass
        else:
            
            if ':888/pma' not in url:
                url =url+ ':888/pma'
        geturl = requests.get(url)
        status=geturl.status_code
        if status == 200:
            print ("存在漏洞，请及时升级面板")
            pass
        else:
            print ("这个站点没有漏洞")       
            pass
if __name__ == '__main__':
	t=input('请输入url\n')
	go(t)
