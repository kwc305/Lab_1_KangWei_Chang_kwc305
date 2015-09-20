import random

def insertionSort(listarray):
   for each in range(1,len(listarray)):

     currentvalue = listarray[each]
     position = each

     while position>0 and listarray[position-1]>currentvalue:
         listarray[position]=listarray[position-1]
         position = position-1
         print listarray

     listarray[position]=currentvalue



listarray=[]

for each in range(10):
	listarray.append(random.randrange(1,100))
	# print each
print 'original array:'
print listarray

insertionSort(listarray)
print listarray