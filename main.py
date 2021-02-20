def bubble_sort(data):
  length = len(data) - 1
  is_sorted = False
  
  while not sorted:
    is_sorted = True
    for i in range(length):
      if data[i] > data[i+1]:
        data[i+1],data[i] = data[i],data[i+1]
        is_sorted = False
  return data
#====================
def binary_search(structure,query):
  start = 0
  end = len(structure) - 1
  
  while start <= end:
    midpoint = (start + end) // 2
    if structure[midpoint] == query:
      return midpoint
    else:
      if structure[midpoint] < query:
        start = midpoint + 1
      else:
        end = midpoint - 1
    
  return False
#====================
# MAIN PROGRAM
arr = [1,5,2,4,3]
print(f"Found at index [{binary_search(bubble_sort(arr),2)}]")