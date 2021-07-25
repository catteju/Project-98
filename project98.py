def swappingData():
    file1 = input("Enter The File A")
    file2 = input("Enter the File To Be Swapped With File A")
    with open(file1,'r') as a:
        dataA = a.read()
    with open(file2, 'r') as b:
        dataB = b.read()
    
    with open(file1, 'w') as a:
        a.write(dataB)
    with open(file2, 'w') as b:
        b.write(dataA)

swappingData()
