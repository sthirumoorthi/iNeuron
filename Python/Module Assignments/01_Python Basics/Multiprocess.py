import multiprocessing
from datetime import datetime
from time import sleep
import random

def printsec(seconds):
    """
    This function waits for some random seconds and prints the date time.
    """
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.now())
    
if __name__ == '__main__':    
    for n in range(3):
        seconds = random.randint(1,5)
        proc = multiprocessing.Process(target=printsec, args=(seconds,))
        proc.start()
        proc.join()