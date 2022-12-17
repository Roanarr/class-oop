class mahasiswa:
    def _init_(self, nama,nim,nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def tambah(self,nama,nim,nilai):
        data.nama.append(nama)
        data.nim.append(nim)
        data.nilai.append(nilai)

    def lihat(self):
        for i in range(len(data.nama)):
            print("|", i+1, "|", end="")
            print('{0:^20}'.format(self.nama[i]), end="")
            print("|", '{0:^8}'.format(self.nim[i]), end=" ")
            print("|", '{0:^8}'.format(self.nilai[i]), end="\n")

    def ubah(self,nama,nim,nilai):
        self.nama[no] = nama
        self.nim[no] = nim
        self.nilai[no] = nilai

    def hapus(self):
        del self.nama[no]
        del self.nim[no]
        del self.nilai[no]


data = mahasiswa([],[],[])

while True:
    menu = input("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]:")
    if menu == "t" or menu == "T":
       print("\nTambah Data")
       data.tambah(
           input("Nama : "),
           input("NIM : "),
           int(input("Nilai  : "))
           )
       print("\nData ditambahkan")

    elif menu == "l" or menu == "L":
        print("\nDaftar Nilai")
        print("="*50)
        print("|No|\t\tNAMA\t\t|\tNIM\t|\tNilai\t|")
        print("="*50)
        if len(data.nama) != 0:
            data.lihat()
        else:
            print("                   TIDAK ADA DATA                               ")
        print("="*50)
    elif menu == "u" or menu == "U":
        print("\nUbah Data")
        ubah = input("Masukkan Nama : ")
        if ubah in data.nama:
           no = data.nama.index(ubah)
           print("Masukkan Data Baru : ")
           data.ubah(
               input("Nama : "),
               input("NIM : "),
               int(input("Nilai Tugas : ")),)
        else:
            print(ubah, "tidak ada di dalam data")

    elif menu == "h" or menu == "H":
        print("\nHapus Data")
        hapus = input("Masukkan Nama : ")
        if hapus in data.nama:
            no = data.nama.index(hapus)
            data.hapus()
            print("Data", hapus, "dihapus")
        else:
            print(hapus, "tidak ada data")

    elif menu == "k" or menu == "K":
        print("\nProgram Keluar")
        print("Terimakasih\n")
        break

    else:
        print("\nsalah!\n")