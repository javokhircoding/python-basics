class Avto():
    def __init__(self,model,rang,korobka,narh):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = 0
    def get_info(self):
        return f"Avtomobil haqida, Modeli: {self.model} Rangi: {self.rang} Korobkasi: {self.korobka} Narhi: {self.narh} Yurgani: {self.kilometr}"

    def update_km(self):
        a = int(input("Qancha yurganini kiriting: "))
        self.kilometr.update(a)


avto1 = Avto("Tesla", "Qizil", "Avtomat", "25000")

print(avto1.get_info())
