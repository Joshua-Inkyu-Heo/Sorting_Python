import random

def insertion_sort(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index - 1
        while i>=0 and (value < list[i]):
            list[i+1], list[i] = list[i], value
            i = i - 1

def bubble_sort(list):
    for index in range(1,len(list)):
        i = 0
        while i<=(len(list)-1-index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
            i = i + 1

def selection_sort(list):
    for index in range(1,len(list)):
        i = index-1
        min_val = list[index-1]
        min_add = index-1
        while i <= (len(list)-2):
            if list[i+1] <= min_val:
                min_val = list[i+1]
                min_add = i+1
            i = i + 1
        list[index-1], list[min_add] = list[min_add], list[index-1]

def quick_sort(list, start, end):
    if start < end:
        # partition the list
        pivot = partition(list, start, end)
        # sort both halves
        quick_sort(list, start, pivot-1)
        quick_sort(list, pivot+1, end)
    return list

def partition(list, start, end):
    pivot = list[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and list[left] <= pivot:
            left = left + 1
        while list[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=list[left]
            list[left]=list[right]
            list[right]=temp
    # swap start with list[right]
    temp=list[start]
    list[start]=list[right]
    list[right]=temp
    return right


print '------------------------------------------------'

a = [random.randint(0,100) for n in xrange(10)]
print 'Unordered array = ', a
insertion_sort(a)
print 'result in Insertion sort = ' , a

print '------------------------------------------------'

a = [random.randint(0,100) for n in xrange(10)]
print 'Unordered array = ', a
bubble_sort(a)
print 'result in Bubble sort = ' , a

print '------------------------------------------------'

a = [random.randint(0,100) for n in xrange(10)]
print 'Unordered array = ', a
selection_sort(a)
print 'result in Selectione sort = ' , a

print '------------------------------------------------'

a = [random.randint(0,100) for n in xrange(10)]
print 'Unordered array = ', a
quick_sort(a, 0, len(a)-1)
print 'result in Quick sort = ' , a

print '------------------------------------------------'
