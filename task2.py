secim1 = input ("Login: ")
secim2 = input ("Parol: ")
if secim1 == "Alisafa" and secim2 == "12345":
    print("Xos geldiniz")
elif secim1 == "" and secim2 == "":
    print("Login ve Parol daxil etmediniz")
elif secim1 == "":
    print("Login daxil etmediniz")
elif secim2 == "":
    print("Parol daxil etmediniz")
elif secim1 != "Alisafa" and secim2 == "12345" :
    print("Login yanlisdir")
elif secim1 == "Alisafa" and secim2 != "12345":
    print("Parol yanlisdir")
elif secim1 != "Alisafa" and secim2 != "12345":
    print("Login ve Parol yanlisdir")
