#! Python3
# Programming Tutorial
# Threading module

print('''

    #####################
    #                   #
    #  Starting Python3 #
    #      Scripts.     #
    #  It's an exciting #
    # time to be alive  #
    #                   # 
    #####################

	''')

import threading
from queue import Queue
import time

print_lock = threading.Lock()



def exampleJob(worker):
	time.sleep(0.5)

	with print_lock:
		print(threading.current_thread().name, worker)

def threader():
	while True:
		worker = q.get()
		exampleJob(worker)
		q.task_done()


# Workers = threads = q
q = Queue()

# Workers
for x in range(10):
	t = threading.Thread(target = threader)
	t.daemon = True
	t.start()

start = time.time()

# Jobs
for worker in range(20):
	q.put(worker)

# Wait for the for terminate
q.join()

print('Entire job took:',time.time()-start)
