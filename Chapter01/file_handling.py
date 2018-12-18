getinput=input("Do you want to store a new record (Y/N) ")

getinput=getinput.strip()
getinput=getinput.lower()
if ("y" in getinput):
    readvaluename=input("Enter the Name: ")
    readvalueage=input("Enter the Age: ")
    readvaluelocation=input("Current location: ")
    tmpvariable=readvaluename+","+readvalueage+","+readvaluelocation+"\n"
    fopen=open("myrecord.csv","w")
    fopen.write(tmpvariable)
    fopen.close()


