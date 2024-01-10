class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        return self.ism

    def get_age(self,yil):
        return yil - self.tyil

    def get_lastname(self):
        return self.familiya


    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya}, tug'ilgan yilim {self.tyil}-yil"


talaba1 = Talaba("Olim","Olimov", 2000)
talaba2 = Talaba("Hasan","Husanov", 1995)
talaba3 = Talaba("Akrom","Aliyev", 2004)