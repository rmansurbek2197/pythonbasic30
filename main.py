class Inventory:
    def __init__(self):
        self.mahsulotlar = {}

    def qoshish(self, nomi, soni, narxi):
        if nomi in self.mahsulotlar:
            self.mahsulotlar[nomi]['soni'] += soni
        else:
            self.mahsulotlar[nomi] = {'soni': soni, 'narxi': narxi}

    def ochirish(self, nomi, soni):
        if nomi in self.mahsulotlar:
            if self.mahsulotlar[nomi]['soni'] >= soni:
                self.mahsulotlar[nomi]['soni'] -= soni
            else:
                print("Mahsulot yetarli emas")
        else:
            print("Mahsulot topilmadi")

    def boshqarish(self):
        for mahsulot, info in self.mahsulotlar.items():
            print(f"Mahsulot: {mahsulot}, Soni: {info['soni']}, Narxi: {info['narxi']}")

    def jami_soni(self):
        jami = sum(info['soni'] for info in self.mahsulotlar.values())
        return jami

    def jami_narxi(self):
        jami = sum(info['soni'] * info['narxi'] for info in self.mahsulotlar.values())
        return jami

    def mahsulot_narxi(self, nomi):
        if nomi in self.mahsulotlar:
            return self.mahsulotlar[nomi]['narxi']
        else:
            return "Mahsulot topilmadi"

    def mahsulot_soni(self, nomi):
        if nomi in self.mahsulotlar:
            return self.mahsulotlar[nomi]['soni']
        else:
            return "Mahsulot topilmadi"

inventory = Inventory()
inventory.qoshish("Apple", 10, 10000)
inventory.qoshish("Banana", 20, 5000)
inventory.boshqarish()
inventory.ochirish("Apple", 5)
inventory.boshqarish()
print(inventory.jami_soni())
print(inventory.jami_narxi())
print(inventory.mahsulot_narxi("Banana"))
print(inventory.mahsulot_soni("Apple"))