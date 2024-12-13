from animal1 import Animal

class Amphibi(Animal): 
    def __init__(self, name, makanannya, habitatnya, berkembang_biak, jenis_air, bernapas_dengan):
        super().__init__(name, makanannya, habitatnya, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas_dengan = bernapas_dengan

    def info_amphibi(self):
        super().info_animal()
        print("jenis_air \t\t\t : ", self.jenis_air,
            "\nbernapas_dengan \t\t : ", self.bernapas_dengan)
        
katak = Amphibi("katak", "serangga", "dua alam", "bertelur", "air tawar", "kulit dan paru-paru")
katak.info_amphibi()
print("=======================")
salamander = Amphibi("salamander", "cacing tanah", "dua alam", "bertelur", "air tawar", "kulit dan paru-paru")
salamander.info_amphibi()
print("========================")
sesilia = Amphibi("sesilia", "rayap dan kepompong", "dua alam", "bertelur", "air tawar", "kulit dan paru-paru")
sesilia.info_amphibi()
        


