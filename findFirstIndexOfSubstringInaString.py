
def findIndex(str1, str2):
  for i in range(0, len(str1) - len(str2)+1):
    if str1[i:i+len(str2)] == str2:
      return i
  return '-1'

if __name__ == "__main__":
  str1 = "sadpeopletalksadideasinsadmoods"
  str2 = "mun"
  print(findIndex(str1, str2))
