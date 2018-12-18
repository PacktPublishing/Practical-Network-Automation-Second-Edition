#create a dictionary:
config={
    "IOS":"exec-timeout 15 0",
    "NXOS":"exec-timeout 15"
    }

getchoice=input("Enter IOS type (IOS/NXOS) : ")

if (getchoice == "IOS"):
 print (config.get("IOS"))

if (getchoice == "NXOS"):
 print (config.get("NXOS"))


