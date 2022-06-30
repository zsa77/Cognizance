with open("onelinefile.txt","r") as f:
    s=str(f.read())
    fi=len(s)
    temp=""
    c=0
    for i in range(fi):
        if s[i].isalpha()==True:
            temp+=s[i]
            
            if i+1<fi:
                if s[i+1].isalpha()!=True:
                    if c!=3:
                        temp+=","
                    c+=1
        elif s[i].isdigit()==True:
            temp+=s[i]
            
            if s[i+1]==".":
                temp+="."
            elif s[i+1].isdigit()!=True and s[i+1]!=".":
                if c!=3:
                    temp+=","
                c+=1
        if c%4==0:
            temp+="\n"
            c=0

with open("Filename2.csv","w") as f2:
    f2.writelines(temp)
    print("Contents of the file:\n"+temp)
