from animal1 import Animal

class Mamalia(Animal):
    def __init__(self, name, makanannya, habitatnya, berkembang_biak, ukuran_tubuh, jenis_kulit):
        super().__init__(name, makanannya, habitatnya, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit

    def info_mamalia(self):
        super().info_animal()
        print("ukuran_tubuh \t\t\t : ", self.ukuran_tubuh,
        "\njenis_kulit \t\t\t : ", self.jenis_kulit)

beruang = Mamalia("beruang", "daging dan ikan", "kutub utara", "beranak", "sangat besar", "berbulu lebat")
beruang.info_mamalia()
print("=========================")
kucing = Mamalia("kucing", "ikan", "darat", "beranak", "sedang", "berlbulu")
kucing.info_mamalia()
print("==========================")
lumba_lumba = Mamalia("lumba_lumba", "ikan", "laut luas", "beranak", "besar", "halus dan licin")
lumba_lumba.info_mamalia()


        