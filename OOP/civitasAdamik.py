from mahasiswa1 import *
from Dosen import *

mhs1 = Mahasiswa("Muhammad Raditya Anwar", "Laki - Laki", 19, "TI13", "1")
dsn1 = Dosen("Muhammad Raditya Anwar", "Laki - Laki", 19, "M.Kom", "Kepala Sekolah")

dsn1.setGaji(1200000)
mhs1.cetak()
dsn1.cetak()