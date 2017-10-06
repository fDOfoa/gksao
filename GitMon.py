import os
import sched, time
import datetime

s = sched.scheduler(time.time, time.sleep)



def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

previousSize = get_size()

def do_something(sc, previousSize): 
    if(previousSize != get_size()):
        os.system('git add .')
        os.system('git commit -m ' + "'" + str(datetime.datetime.now()) + "'") 
        os.system('git push')
        
    previousSize = get_size();

    # do your stuff
    s.enter(2, 1, do_something, (sc,previousSize))
s.enter(2, 1, do_something, (s,previousSize))
s.run()

