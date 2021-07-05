intro = input("Tell me about your self ")
charcount = 0
wordcount = 1 
 
for i in intro:
     charcount+=1
     if(i==" "):
         wordcount+=1
print("number of words in the string"+ str(wordcount))
print("number of characters in the string"+ str(charcount)) 


