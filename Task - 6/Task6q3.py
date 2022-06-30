import re

with open("about.txt", "r")  as file:
    text=file.read()
    lis=re.findall(r"\b\w{6,}\b", text)
    print(*lis,sep='\n')

count = 0  
word = ""  
maxCount = 0  
words = [] 
file = open("about.txt", "r")
for line in file:    
    string = line.lower().replace(',','').replace('.','').split(" ");    
    for s in string:  
        words.append(s);  
for i in range(0, len(words)):  
    count = 1;   
    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1;   
    if(count > maxCount):  
        maxCount = count;  
        word = words[i];            
print("\nMost repeated word over 6 letters long: " + word);  
file.close();
