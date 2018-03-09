# append the file in sample.txt as print the table of 2
# till 12 and it should be printed as follow

myList = []
for i in range(1, 13):
    myList.append("{0} times 2 is {1}".format(i, i*2))
# print(myList)
with open("sample.txt", 'a') as myFile:
    print("", file=myFile)
    for listApp in myList:
        print(listApp, file=myFile)
    print("="*20, file=myFile)
