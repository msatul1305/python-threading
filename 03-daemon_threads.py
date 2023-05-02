# Example of a multi-threaded application using daemon threads
# line 11 - daemon =True. Main thraed will not wait for threads to complete.

from training import WEBSITES, visit_website
import threading


if __name__ == '__main__':
    print('Main thread starting')
    for website in WEBSITES:
        # Create a Thread object with target and args
        t = threading.Thread(target=visit_website, args=[website], daemon=True)
        # Start the thread
        t.start()
    print('Main thread ending')
