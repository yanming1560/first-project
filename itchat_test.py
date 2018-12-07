import itchat,time,random,requests
from itchat.content import TEXT
from bs4 import BeautifulSoup as bs

def weather():      #回复天气预报
    url = 'https://www.tianqi.com/shanghai/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    }

    aa = requests.get(url, headers=headers)
    bb = bs(aa.content, 'lxml')
    cc = bb.find(class_='weather_info')
    dd = cc.find_all('dd')
    out=''    
    for i in dd:
        out+=i.text
    return out

@itchat.msg_register(TEXT)      #获取msg
def simple(msg):                #子函数竟然是自动运行的。。。
    time.sleep(random.uniform(0,0.5))
    if msg['Type'] == TEXT:     #如果是文本类型的消息输入
        # print(msg['User'])      #消息里面User相关的内容
        # all='你的昵称：'+msg['User']['NickName']+'\n'
        # if msg['User']['Sex']==0:
        #     all += '性别:未知\n'
        # elif msg['User']['Sex']==1:
        #     all += '性别:男\n'
        # elif msg['User']['Sex']==2:
        #     all+='性别:女\n'
        # all+='地址：'+msg['User']['Province']+msg['User']['City']
        # print(all)
        # itchat.send_msg(all,toUserName=msg['FromUserName'])     #消息回复
        if '天气' in msg['Content']:
            out=weather()            
            itchat.send_msg(out, toUserName=msg['FromUserName'])  # 消息回复

itchat.auto_login()     #二维码登录
itchat.run()            #维持登录状态

