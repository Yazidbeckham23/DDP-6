# Buat class animaal sebagai parent class. class animal mempunyai properti 4 properti (nama, makanan, hidup, berkembang biak)

class Animal:
    def __init__(self, name, makanannya, habitatnya, berkembang_biak):
        self.name = name
        self.makanannya = makanannya
        self.habitatnya = habitatnya 
        self.berkembang_biak = berkembang_biak

    def info_animal (self):
        print("nama hewan \t\t\t : ", self.name, 
        "\nmakanannya \t\t\t : ", self.makanannya, 
        "\nhabitatnya \t\t\t : ", self.habitatnya,
        "\nberkembang_biak \t\t : ", self.berkembang_biak,) 

#hewan = Animal("Kucing oyen", "tulang", "darat", "beranak")
#hewan.info_animal()