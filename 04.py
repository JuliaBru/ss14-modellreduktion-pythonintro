#!/usr/bin/python

def mylist_thingy(letter):
  #! change this so it directly returns via list comprehension
  retvalue = []
#  for x in range(ord('A'), ord(letter)):
#    retvalue.append(chr(x))

  retvalue=[chr(x) for x in range(ord('A'),ord(letter))]
  return retvalue

#! make this a proper generator function
def mygenerator_thingy(letter):
  current = ord('A')
  while current < ord(letter):
    yield chr(current)
    current += 1
    
real_list = mylist_thingy('Z')
iterable = mygenerator_thingy('Z')
iterable_list = list(iterable)

print(real_list)
print(iterable)
print(iterable_list)
#! lengths are supposed to be equal
print(len(set(iterable_list).intersection(real_list))==len(real_list))
