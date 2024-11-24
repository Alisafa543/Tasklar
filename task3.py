reqem1 = int(input("1-ci rəqəmi daxil edin: "))
reqem2 = int(input("2-ci rəqəmi daxil edin: "))
reqem3 = int(input("3-cü rəqəmi daxil edin: "))
if reqem1 > reqem2 and reqem1 > reqem3:
    print(reqem1)
elif reqem2 > reqem1 and reqem2 > reqem3:
    print(reqem2)
elif reqem3 > reqem1 and reqem3 > reqem2:
    print(reqem3)