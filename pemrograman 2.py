class Hewan:
    def __init__(self, nama, spesies):
        self.nama = nama
        self.spesies = spesies
    
    def suara(self, suara):
        print(f"{self.nama} adalah {self.spesies} memiliki suara {suara}")
        
kucing = Hewan("caty", "Kucing")
anjing = Hewan("heryy", "Anjing")

kucing.suara("Miawww")  # Caca adalah Kucing memiliki suara Meoww
anjing.suara("gukguk")  # Chiko adalah Anjing memiliki suara Woogg
