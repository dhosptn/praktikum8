class DaftarNilaiMahasiswa:
    def __init__(self):
        self.daftar_nilai = []

    def tambah(self, nama, nilai):
        mahasiswa = {'nama': nama, 'nilai': nilai}
        self.daftar_nilai.append(mahasiswa)
        print(f"Data mahasiswa {nama} berhasil ditambahkan.")

    def tampilkan(self):
        print("\nDaftar Nilai Mahasiswa:")
        print("="*23)
        for mahasiswa in self.daftar_nilai:
            print(f"Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")

    def hapus(self, nama):
        for mahasiswa in self.daftar_nilai:
            if mahasiswa['nama'] == nama:
                self.daftar_nilai.remove(mahasiswa)
                print(f"Data mahasiswa {nama} berhasil dihapus.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        for mahasiswa in self.daftar_nilai:
            if mahasiswa['nama'] == nama:
                mahasiswa['nilai'] = nilai_baru
                print(f"Data mahasiswa {nama} berhasil diubah menjadi nilai {nilai_baru}.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

# Contoh penggunaan program
daftar_nilai_mahasiswa = DaftarNilaiMahasiswa()

daftar_nilai_mahasiswa.tambah("Ahmad", 100)
daftar_nilai_mahasiswa.tambah("Ridho", 100)
daftar_nilai_mahasiswa.tambah("Ardho", 100)


daftar_nilai_mahasiswa.tampilkan()

daftar_nilai_mahasiswa.hapus("Ridho")
daftar_nilai_mahasiswa.tampilkan()

daftar_nilai_mahasiswa.ubah("Ardho", 100)
daftar_nilai_mahasiswa.tampilkan()
