boy = float(input("Boyunuzu daxil edin: "))
kutle = float(input("Kutlenizi daxil edin: "))
bki = kutle / (boy * boy)
if (bki < 18.5):
    print ("Zəif")
elif (18.5 <= bki < 25):
    print("Normal")
elif (25 <= bki < 30):
    print ("Kilolu")
elif (bki >= 30):
    print ("Obez")


