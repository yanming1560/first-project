import multiprocessing,time,random

def run_test(i):
    one_list=[]
    time_start=time.time()
    print('test ',i,'is working....')
    one_list.append(i)
    #one_list.append(time_start)
    for t in range(10):
        time.sleep(random.uniform(0,1))
        print('test ',i,'work ',t,'times')
        one_list.append(time.time()-time_start)
    return one_list

def process(n):
    all_list=[]
    for i in range(n):
        p=multiprocessing.Process(target=run_test,args=(i,))
        all_list.append(p)
        p.start()
    p.join()
    return all_list


def process_pool(n):
    time1=time.time()
    p = multiprocessing.Pool(processes=10)
    for i in range(n):
       res=p.apply_async(run_test,args=(i,))
    p.close()
    p.join()
    time2 = time.time()
    print(n, ' processing cost ', time2 - time1, ' seconds!')
    print(res.get())

if __name__=='__main__':
    print(process_pool(3))
