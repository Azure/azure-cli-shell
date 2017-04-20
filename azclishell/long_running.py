#!/usr/bin/env python
""" This is a Troy snippet for progress """

import time 
import sys
import os
 
total = 32212255232
 
try:
    while True:
        size = os.path.getsize('large30.vhd')
        percent = size / total
        bar_len = 100
        completed = int(bar_len*percent)
 
        message = '\r['
        for i in range(bar_len):
            if i < completed:
                message += '#'
            else:
                message += ' '
        message += ']  {:.4%}'.format(percent)
 
        sys.stdout.write(message)
        sys.stdout.flush()
        time.sleep(0.2)
except KeyboardInterrupt:
    sys.stdout.write("Bye\n")
    sys.exit(0)


"""
In terms of notes:
- there are calls to the SDK that get information, the get_long_running_operations in places like:
https://github.com/Azure/azure-sdk-for-python/blob/master/azure-mgmt-network/azure/mgmt/network/v2017_03_01/operations/network_watchers_operations.py
and there are the client side stuff here:
https://github.com/Azure/msrest-for-python/blob/master/msrest/paging.py 
https://github.com/Azure/msrest-for-python/blob/master/msrest/pipeline.py 

In the CLI:
- there is a LongRunning Operation class that poles the server to get some information
    - exactly what information I can abstract I still don't know

Long Running:
- If all I can get is that it's not done:
    - I would have to do something like a spinning wheel equilavent, maybe a note in the side bar saying in progress
- If I can get a percentage of work done:
    - I can do a ====>++++++ kind of thing or something with color gradient (super cool)
    - I can place the number and do some combination of both

"""
