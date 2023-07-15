
def findIndex(str1, str2):
  len_str1 = len(str1)
  len_str2 = len(str2)
  if len_str2 > len_str1:
    return -1
  for i in range(0, len_str1 - len_str2+1):
    if str1[i:i+len_str2] == str2:
      return i
  return -1

def isDuplicateElementPresentInArray(arr1):
  for i in range(0, len(arr1) -1 ):
    if arr1.count(arr1[i]) >1 :
      return 1
  return -1

def arrayIndeciesMatchingTargetValue(arr1, target):
  l1 = []
  for i in range(0, len(arr1) + 1):
    for j in range( i+1, len(arr1)):
      if arr1[i] + arr1[j] == target:
        l1.append((i,j))
  return l1      

if __name__ == "__main__":
  str1 = "sadpeopletalksadideasinsadmoods"
  str2 = "sad"
  print(findIndex(str1, str2))
 
  # Second function
  a = [1,2,3,4,5,6,7,8,9]
  print(isDuplicateElementPresentInArray(a))

  # Third function
  l1 = arrayIndeciesMatchingTargetValue(arr1, 9)
  if len(l1) >= 1:
    print(l1)
  else:
    print("No Matchi for the target value")
