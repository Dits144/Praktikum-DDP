class Mahasiswa:
    nim = ""
    nama = ""
    rombel = ""

    def __init__(self, nim, nama, rombel):
        self.nim = nim
        self.nama = nama
        self.rombel = rombel

    def welcome(self):
        print("Hallo", self.nama, "Di STT Terpadu NurulFikri")

    def lulus(self, nilai):
        if(nilai > 90):
            print("lulus")
        else:
            print("Tidak lulus")

mhs1 = Mahasiswa("0110222301", "Muhammad Raditya Anwar", "TI13")
# mhs1.nama = "Radit"
# mhs1.nim = "0110222301"
# mhs1.rombel = "TI-13"

print("nama Mahasiswa : ",mhs1.nama)
print("NIM : ", mhs1.nim)
print("rombel : ", mhs1.rombel)
mhs1.lulus(91)
print(mhs1.welcome)