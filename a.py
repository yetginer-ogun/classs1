class Ev:

    oda_sayısı = 4
    banyo_sayısı = 1
    kapı_sifresi = "1234"
    boyut = 100
    ısınma_tipi = "Doğalgaz"
    tv_sayısı = 3
    modem_sayısı = 1

    def enter(self):
        x = input("Şifreyi girin")
        if x == self.kapı_sifresi:
            print("Eve girildi")
        else:
            print("Hatalı şifre")

    def exit(self):
        print("Evden çık")

    def kilitle(self):
        print("Kapı kitlendi")
    
    def kod(self):
        print(f"Şifre: {self.kapı_sifresi}")

    def degis(self):
        self.kapı_sifresi = input("Yeni şifreyi girin")
        print(f"Şifre değiştirildi. Yeni şifre: {self.kapı_sifresi}" )
    

benim_evim = Ev()

benim_evim.exit()
benim_evim.kilitle()
benim_evim.enter()
benim_evim.kod()
benim_evim.enter()
benim_evim.degis()
