import time
def insertion_sort(data, drawData, timeTick): 
# Traverse through 1 to len(data)
    for i in range(1, len(data)):
 
        key = data[i]
 
        # Move elements of data[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < data[j] :
                data[j + 1] = data[j]
                drawData(data, ['yellow' if x == j+1 or x<j+1 else 'red' for x in range(len(data))] )
                time.sleep(timeTick)
                j -= 1
        data[j + 1] = key
    drawData(data, ['green' for x in range(len(data))])
	