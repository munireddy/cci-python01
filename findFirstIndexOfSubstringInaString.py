
def findIndex(str1, str2):
  len_str1 = len(str1)
  len_str2 = len(str2)
  if len_str2 > len_str1:
    return -1
  for i in range(0, len_str1 - len_str2+1):
    if str1[i:i+len_str2] == str2:
      return i
  return -1

if __name__ == "__main__":
  str1 = "sadpeopletalksadideasinsadmoods"
  str2 = "sad"
  print(findIndex(str1, str2))
