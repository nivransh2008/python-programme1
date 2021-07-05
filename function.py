def countWords():
    fileName = input("enter your file name ")
    openFile = open(fileName, "r")
    numberOfWords = 0
    for i in openFile:
        words = i.split()
        numberOfWords= numberOfWords+len(words)
        print(words)
    print(numberOfWords)
countWords()
