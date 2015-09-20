import random

print 'HW1 kwc305'

listarray=[]

for each in range(10):
	listarray.append(random.randrange(1,100))
	# print each
print 'original array:'
print listarray



def bubblesort(listarray):
	print 'bubble sort'
	for outsite in range(9):
		for inside in range(9):
			if listarray[inside]>listarray[inside+1]:
				listarray[inside],listarray[inside+1]=listarray[inside+1],listarray[inside]
		print listarray
	print listarray


bubblesort(listarray)