import os,datetime,shutil,time

target='IND_FAN_DATA_25T'
backup=r'\\服务器\ind_fan_testdata'

# target='target'
# backup='backup'

log_file=backup+'\\'+'备份日志.txt'
if not(os.path.exists(log_file)):
    with open(log_file,'a') as f:
        f.write("%s         创建日志文件。\n"%str(datetime.datetime.now())[5:16])


t1=datetime.datetime.now()
all_file=[]
all_dir=[]
for root, dirs, files in os.walk(target):
    for i in files:
        all_file.append(root+'\\'+i)
    for i in dirs:
        all_dir.append(root+'\\'+i)

#备份所有的文件夹和目录树，如果不存在，整个粘贴，如果存在不做处理。
for i in all_dir:
    back_i = i.replace(target, backup)
    if not(os.path.exists(back_i)):
        shutil.copytree(i, back_i)
        with open(log_file, 'a') as f:
            f.write("%s         备份文件夹:%s。\n" % (str(datetime.datetime.now())[5:16],back_i))
        print('备份文件夹:%s' % back_i)

#备份所有的文件，如果不存在，整个粘贴，如果存在，如果日期一致，不处理，如果日期不一致，粘贴。
for i in all_file:
    if '~$' in i:
        print('文件：%s正在修改中，无法准确备份。。。'%i.replace('~$',''))
    else:
        back_i=i.replace(target,backup)
        # print(back_i)
        # print(os.path.exists(back_i))
        if os.path.exists(back_i):
            if os.stat(i).st_mtime!=os.stat(back_i).st_mtime:
                shutil.copy2(i, back_i)
                shutil.copystat(i,back_i)
                with open(log_file, 'a') as f:
                    f.write("%s         修改文件:%s。\n" % (str(datetime.datetime.now())[5:16], i))
                print("修改文件:%s"%i)
        else:
            shutil.copy2(i,back_i)
            shutil.copystat(i, back_i)
            with open(log_file, 'a') as f:
                f.write("%s         备份文件:%s。\n" % (str(datetime.datetime.now())[5:16], i))
            print("备份文件:%s" % i)

t2=datetime.datetime.now()
print(t2-t1)
