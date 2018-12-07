import itchat,time,random
from itchat.content import TEXT


@itchat.msg_register(TEXT)      #获取msg
def simple(msg):                #子函数竟然是自动运行的。。。
    time.sleep(0.5+random.uniform(0,0.5))
    if msg['Type'] == TEXT:     #如果是文本类型的消息输入
        print(msg['User'])      #消息里面User相关的内容
        all='你的昵称：'+msg['User']['NickName']+'\n'
        all+='性别:'+'男' if msg['User']['Sex']==1 else '女'
        all+='\n'
        all+='地址：'+msg['User']['Province']+msg['User']['City']
        print(all)
        itchat.send_msg(all,toUserName=msg['FromUserName'])     #消息回复

itchat.auto_login()     #二维码登录
itchat.run()            #维持登录状态
