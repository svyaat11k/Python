ip = input("Podaj")

def sprawdz(ip):
    if ip.count('.') != 3:
        return False
    lista = ip.split('.')
    if len(lista) != 4:
        return False
    for i in lista:
        if int(i) < 0 or int(i) > 255:
            return False
    else:
        return True

if sprawdz(ip) == True:
    print("Poprawny")
else:
    print("Nie poprawny")
