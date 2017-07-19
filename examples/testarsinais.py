#!/usr/bin/env python3

# I used this script to check what happens when I stop a process
# and how this is handled by python

import sys, signal, time

def handler(signum = None, frame = None):
    print('Signal handler called with signal', signum)
    time.sleep(1)  #here check if process is done
    print ('Wait done')
    sys.exit(0)

for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
    signal.signal(sig, handler)

while True:
    time.sleep(6)

