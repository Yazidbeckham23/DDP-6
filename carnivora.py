from animal1 import Animal

class carnivora(Animal):
    def __init__(self, name, makanannya, habitatnya, berkembang_biak, sistem_pencernaan, jenis_gigi):
        super().__init__(name, makanannya, habitatnya, berkembang_biak)
        self.sistem_pencernaan = sistem_pencernaan
        self.jenis_gigi = jenis_gigi

    def info_carnivora(self):
        super().info_animal()
        print("sistem_pencernaan \t\t : ", self.sistem_pencernaan,
        "\njenis_gigi \t\t\t : ", self.jenis_gigi)

trex = carnivora("trex", "daging", "alam liar", "beranak", "sederhana", "bertaring tajam")
trex.info_carnivora()
print("=========================")
harimau = carnivora("harimau", "daging", "alam liar", "beranak", "sederhana", "bertaring tajam")
harimau.info_carnivora()
print("=========================")
anjing = carnivora("anjing", "daging", "darat", "beranak", "sederhana", "bertaring tajam")
anjing.info_carnivora()


        