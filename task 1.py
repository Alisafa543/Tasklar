list = ["Aslan" , "Imran" , "Afaq" , "Uzeyir" , "Shahin"]
secim = input("Kim haqqinda melumat almaq isteyirdiniz: ")
if secim == "Aslan":
    print("Aslan emi ogludur.")
elif secim == "Imran":
    print("Imran dayi ogludur.")    
elif secim == "Afaq":
    print("Afaq bibi qizidir.")    
elif secim == "Uzeyir":
    print("Uzeyir xala ogludur.")
elif secim == "Shahin":
    print("Shahin yaxin dostdur.")
elif secim == "":
    print("Siz ad daxil etmediniz")
else :
    print(secim , "kimdir? Men onu tanimadim")
