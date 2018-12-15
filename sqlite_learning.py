import sqlite3

conn=sqlite3.connect('test.db')
cursor=conn.cursor()
def insert():
    #cursor.execute('create table 小麦(part varchar(20),val varchar(20),unit varchar(20))')
    # cursor.execute('''create table 大米
    # (part char(20),
    # val float,
    # unit char(20))
    # ''')
    cursor.execute('insert into 大米 (part,val,unit) values (\'卡路里\',25,\'千焦\')')
    cursor.rowcount

def show():
    cursor.execute('select * from 大米 where part=?',('卡路里',))    #制定表格单项数据查找
    values=cursor.fetchall()    #赋值
    print(values)
    c=cursor.execute('select part,val,unit from 大米')    #遍历表格
    for i in c:     #遍历后输出
        print(i)
def all_tab():
    cursor.execute("select name from sqlite_master where type='table' order by name")   #所有的table
    print(cursor.fetchall())
    
all_tab()
cursor.close()
conn.commit()
conn.close()
