from DISClib.ADT import list as lt

a = [4,8,1,17,6,2,3,0,9,8,2,11,16]

listibiris = lt.newList(datastructure="ARRAY_LIST")

for b in a:
    lt.addLast(listibiris,b)

def heapify(array,size,root):
    largest = root
    left = (largest*2)+1
    right = (largest*2)+2

    if left < size and lt.getElement(array,largest) < lt.getElement(array,left):
        largest = left
    
    if right < size and lt.getElement(array,largest) < lt.getElement(array,right):
        largest = right

    if largest != root:
        oldroot = lt.getElement(array, root)
        newroot = lt.getElement(array, largest)
        lt.changeInfo(array,largest,oldroot)
        lt.changeInfo(array,root,newroot)

    heapify(array,size,largest)

def heapsort(array):
    size = lt.size(array)

    for root in range(size//2 -1,0,-1):
        heapify(array,size,root)
    
    for subsize in range(size,1,-1):
        oldlast = lt.getElement(array, subsize)
        newlast = lt.getElement(array, 1)
        lt.changeInfo(array,1,oldlast)
        lt.changeInfo(array,subsize,newlast)
        heapify(array,subsize,1)

print(listibiris)
heapsort(listibiris)
print(listibiris)

    

