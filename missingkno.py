def missingNO(array):
#The array is missing one number no we must +1 to the length iterate over all values
  for idx in range(len(array)+1):
    #Index must start at 1 so idx+1
    if (idx+1) not in array:
      return idx+1

#Intermediate
def missingNOs(array):
  #create array to hold multiple values
  temp = []
  #Missing two values so +2 to the length
  for idx in range(len(array)+2):
    #Again, +1 to correctly index
    if (idx+1) not in array:
      temp.append(idx+1)
  return temp

#Hard
def missingNOKetsuban(array, n):

    temp = []
    for idx in range(n):
        if (idx+1) not in array:
            temp.append(idx+1)
    return temp

#Test for Basic
n = int(input("size:"))
array1 =[x+1 for x in range(n)]
print(array1)
array1.remove(6)
print(array1)
print(missingNO(array1))

#Test for Intermediate
array1.pop(13)
print(missingNOs(array1))

#Test for Hard
array1.pop(12)
print(missingNOKetsuban(array1,30))
