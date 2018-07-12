import requests
import re
import time

url='https://tieba.baidu.com/p/2256306796?pn=6'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}


response=requests.get(url,headers=headers)
html_doc = response.content.decode('utf-8')

reg = r'src="(http.+?\.jpg)"'
pattern = re.compile(reg)
get_img = re.findall(pattern, html_doc)

n=0
for i in get_img:
    print(i)
    try:
        ir=requests.get(i,headers=headers,timeout=2) #设置连接时间为2s，以防止连接过久出错中断
        print(ir)
        n += 1
        with open('box/' + str(n) + '.jpg', 'wb')as file:
            file.write(ir.content)
    except Exception:  #如果出现错误，空过继续(Exception 捕捉所有错误)(requests.exceptions.ConnectTimeout超时连接错误)
        print('Error')
        pass
