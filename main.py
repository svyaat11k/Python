class Sprawdzanie:
    def __init__(self, ip):
        self.ip = ip
        self.message = ""
    def sprawdz(self):
        if self.ip.count(".") != 3:
            self.message = "Nie poprawny format"
        self.lista = self.ip.split('.')
        if len(self.lista) != 4:
            self.message = "Nie poprawny format"
        for i in self.lista:
            if int(i) < 0 or int(i) > 255:
                niedziala = True
        if niedziala:
            self.message = "Taki adres nie istnieje"
        else:
            self.message = "Adres jest poprawny"
    def __str__(self):
        return self.message
adres = input("Podaj adres IPv4: ")
print(Sprawdzanie(adres))