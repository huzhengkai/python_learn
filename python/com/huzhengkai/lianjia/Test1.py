import psutil
pids = psutil.pids()
for pid in pids:
    p = psutil.Process(pid)
    print("pid-%d,pname-%s" %(pid,p.name()))
    # if str(p.name()).find("python")!=-1:
    #     print("pid-%d,pname-%s" %(pid,p.name()))
