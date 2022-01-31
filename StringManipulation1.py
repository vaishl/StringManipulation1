string1=""
def joinlist(string1):
  Alist=str(input("Please enter seperated by a comma the items you would like in a string"))
  Alist = Alist.split(",")
  Astring=str(input("Please enter the string you would like between them"))
  for i in range(len(Alist)):
    string1=string1+Astring+Alist[i]
  print(string1)

joinlist(string1)

def joinList(aList,separator):
    stringup = str(aList[0])
    for i in range (1, len(aList)):
        stringup=stringup + separator + str(aList[i])
    return stringup