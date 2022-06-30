with open("onelinefile.txt","r") as f:
    string=str(f.read())
    file=len(string)
    temp=""
    comma=0
    for i in range(file):
        if string[i].isalpha()==True:
            temp+=string[i]
            
            if i+1<file:
                if string[i+1].isalpha()!=True:
                    if comma!=3:
                        temp+=","
                    comma+=1
        elif string[i].isdigit()==True:
            temp+=string[i]
            
            if string[i+1]==".":
                temp+="."
            elif string[i+1].isdigit()!=True and string[i+1]!=".":
                if comma!=3:
                    temp+=","
                comma+=1
        if comma%4==0:
            temp+="\n"
            comma=0

with open("Filename2.csv","w") as f2:
    f2.writelines(temp)
    print("Contents of the file:\n"+temp)
