import random
import copy
def bubblesort(listarray):
	print 'bubble sort'
	print 'original:', listarray
	for outsite in range(9):
		for inside in range(9):
			if listarray[inside]>listarray[inside+1]:
				listarray[inside],listarray[inside+1]=listarray[inside+1],listarray[inside]
		print listarray
	print listarray

def insertionSort(newarray):
	print 'insertion sort'
	print 'original:',newarray
	for each in range(1,len(newarray)):

		currentvalue = newarray[each]
		position = each
		while position>0 and newarray[position-1]>currentvalue:
			newarray[position]=newarray[position-1]
			position = position-1
			print newarray
			newarray[position]=currentvalue


listarray=[]
newarray=[]
for each in range(10):
	listarray.append(random.randrange(1,100))
	newarray.append(random.randrange(1,100))


print 'original array:'
print listarray
print newarray

bubblesort(listarray)
print '--------------------------------'
insertionSort(newarray)
