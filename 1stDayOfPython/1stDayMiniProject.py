# 1stDayMiniProject Is Data Type Converter
guiofMini = input("Enter Anything You Want To Convert Into Other Data Types>")
datatypeofMini = input("In Which Data Type You Want To Convert The Data? Int = I,Float = F,Str = S,List = L,Dict = D,Set - SE,Tuple = T")
datatypeofMini1lower = datatypeofMini.lower()
if datatypeofMini1lower == 'i' and datatypeofMini1lower == float :
    intdata = int(guiofMini)
    print(f"The Data Converted is{intdata} ")
elif datatypeofMini1lower == 'f' and datatypeofMini1lower == int:
    floatdata = float(guiofMini)
    print(f"The Data Converted is{floatdata} ")
elif datatypeofMini1lower == 's':
    stringdata = str(guiofMini)
    print(f"The Data Converted is{stringdata} ")
elif datatypeofMini1lower == 'l':
    listdata = list(guiofMini)
    print(f"The Data Converted is{listdata} ")
elif datatypeofMini1lower == 'd':
    dictdata = dict(guiofMini)
    print(f"The Data Converted is{dictdata} ")
elif datatypeofMini1lower == 'se':
    setdata = set(guiofMini)
    print(f"The Data Converted is{setdata} ")
elif datatypeofMini1lower == 't':
    tupledata = tuple(guiofMini)
    print(f"The Data Converted is{tupledata} ")
else:
    print("Plz Try Again:")







































