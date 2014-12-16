#!/usr/bin/env python


import hubo_ach as ha
import ach
import sys
import time
from ctypes import *

# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
#s.flush()
#r.flush()

# feed-forward will now be refered to as "state"
state = ha.HUBO_STATE()

# feed-back will now be refered to as "ref"
ref = ha.HUBO_REF()

# Get the current feed-forward (state) 
[statuss, framesizes] = s.get(state, wait=False, last=False)
elbow=1
#left elbow
ref.ref[ha.LEB] = -1
#left shoulder rotation
ref.ref[ha.LSR] = 1
#left shoulder yaw
ref.ref[ha.LSY] = 1
#left wrist roll
ref.ref[ha.LWR] = -1
#forward feed
ref.ref[ha.LEB] = elbow
r.put(ref)
time.sleep(0.5)	

for j in range(0,3):
	for i in range(0,5):
				#left elbow
		ref.ref[ha.LEB] = -1
		r.put(ref)
		time.sleep(0.3)	

		ref.ref[ha.RHP] = -0 - (0.1*i)
		ref.ref[ha.RKN] = 0 + (0.2*i)
		ref.ref[ha.RAP] = -0 - (0.1*i)
		ref.ref[ha.LHP] = -0 - (0.1*i)
		ref.ref[ha.LKN] = 0 + (0.2*i)
		ref.ref[ha.LAP] = -0 - (0.1*i)
		r.put(ref)
		time.sleep(.3)
		ref.ref[ha.LEB] = -2
		r.put(ref)
		time.sleep(0.3)	
	for i in range(0,5):
				#left elbow
		ref.ref[ha.LEB] = -1
		r.put(ref)
		time.sleep(0.3)	

		ref.ref[ha.RHP] = -0.5 + (0.1*i)
		ref.ref[ha.RKN] = 1- (0.2*i)
		ref.ref[ha.RAP] = -0.5 + (0.1*i)
		ref.ref[ha.LHP] = -0.5 + (0.1*i)
		ref.ref[ha.LKN] = 1- (0.2*i)
		ref.ref[ha.LAP] = -0.5 + (0.1*i)
		r.put(ref)
		time.sleep(.3)
		ref.ref[ha.LEB] = -2
		r.put(ref)
		time.sleep(0.3)	
	time.sleep(.5)
	
	
timecount=0	
while timecount<10:
	#left elbow
	ref.ref[ha.LEB] = -1
	#left shoulder rotation
	ref.ref[ha.LSR] = 1
	#left shoulder yaw
	ref.ref[ha.LSY] = 1
	#left wrist roll
	ref.ref[ha.LWR] = -1
	#forward feed
	r.put(ref)
	#sleep for 1 secound
	time.sleep(0.5)	
	
	ref.ref[ha.LEB] = -2.5
	
	r.put(ref)
	time.sleep(0.5)
	timecount=timecount+1	
	
ref.ref[ha.LEB] = 0
#left shoulder rotation
ref.ref[ha.LSR] = 0
#left shoulder yaw
ref.ref[ha.LSY] = 0
#left wrist roll
ref.ref[ha.LWR] = 0
#forward feed
r.put(ref)
time.sleep(0.5)	





r.close()
s.close()


