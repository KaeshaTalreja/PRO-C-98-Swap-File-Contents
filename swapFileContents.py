def swapContents():
    fileName1=input("Enter the name of file 1: ")
    fileName2=input("Enter the name of file 2: ")

    file1=open(fileName1,'r')
    file2=open(fileName2,'r')

    contents1=file1.read()
    contents2=file2.read()

    file1=open(fileName1,'w')
    file1.write(contents2)

    file2=open(fileName2,'w')
    file2.write(contents1)

swapContents()

    