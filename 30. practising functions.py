

# 1. GST calc return for buisness and workers
# 2. math and random mod 




def business_gst(gst):
  gst = gst + (gst * 0.10)
  return gst 


def workingclass_gst(gst):
  gst = gst + (gst * 0.18)
  return gst 


print("business gst of 100 is ", business_gst(100))

print("salaried class gst of 100 is " , workingclass_gst(100))




from math import log2, sqrt

print("the square of 25 is", sqrt(25))



import random 

print(random.random())



import math 

print(math.sqrt(64))



print(dir(math))
