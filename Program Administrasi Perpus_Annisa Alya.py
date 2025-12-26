
## ~ PROGRAM ADMINISTRASI PERPUSTAKAAN BAHAGIA ~ ##

from tabulate import tabulate
from datetime import datetime

#--- TABEL DAFTAR BUKU ---#
tabel_buku = [{"index_buku":0, "judul_buku":"bumi manusia", "penulis_buku":"Pramoedya Ananta Toer", "kategori_buku":"Fiksi Sejarah", "tahun_terbit": "1980", "status_buku":"Tersedia"},
              {"index_buku":1, "judul_buku":"laskar pelangi", "penulis_buku":"Andrea Hirata", "kategori_buku":"Fiksi", "tahun_terbit": "2005", "status_buku":"Tersedia"},
              {"index_buku":2, "judul_buku":"cantik itu luka", "penulis_buku":"Eka Kurniawan", "kategori_buku":"Sastra", "tahun_terbit": "2002", "status_buku":"Tidak tersedia"},
              {"index_buku":3, "judul_buku":"statistik deskriptif & inferensial (dengan SPSS)", "penulis_buku":"Sugiono", "kategori_buku":"Pendidikan", "tahun_terbit": "2019", "status_buku":"Tidak tersedia"},
              {"index_buku":4, "judul_buku":"negeri 5 menara", "penulis_buku":"Ahmad Fuadi", "kategori_buku":"Inspiratif","tahun_terbit": "2009", "status_buku":"Tersedia"},
              {"index_buku":5, "judul_buku":"saman", "penulis_buku":"Ayu Utami", "kategori_buku":"Sastra", "tahun_terbit":"1998", "status_buku":"Tersedia"},
              {"index_buku":6, "judul_buku":"dasar-dasar aljabar Linear", "penulis_buku":"Howard Anton", "kategori_buku":"Pendidikan", "tahun_terbit": "2000", "status_buku":"Tidak tersedia"},
              {"index_buku":7, "judul_buku":"daun yang jatuh tak pernah membenci angin", "penulis_buku":"Tere Liye", "kategori_buku":"Roman", "tahun_terbit":"2012", "status_buku":"Tersedia"},
              {"index_buku":8, "judul_buku":"gadis kretek", "penulis_buku":"Ratih Kumala", "kategori_buku":"Sejarah","tahun_terbit":"2012", "status_buku":"Tersedia"},
              {"index_buku":9, "judul_buku":"kalkulus: edisi kesembilan jilid 1", "penulis_buku":"Edwin J. Purcell", "kategori_buku":"Pendidikan", "tahun_terbit":"2010", "status_buku":"Tidak tersedia"},
              {"index_buku":10, "judul_buku":"laut bercerita", "penulis_buku":"Leila S. Chudori", "kategori_buku":"Fiksi Sejarah", "tahun_terbit":"2017", "status_buku":"Tersedia"}]

nama_kolom = {"index_buku":"indeks buku", "judul_buku":"judul", "penulis_buku":"penulis", "kategori_buku":"kategori","tahun_terbit":"tahun terbit", "status_buku":"status"}

def print_tabel_buku(data_tabel_buku, nama_kolom_tabel):
    print(tabulate(data_tabel_buku, headers='keys', tablefmt= "pretty"))



#--- TABEL PEMINJAMAN BUKU ---#
tabel_pinjam = [{"ID_pinjam":0, "ID_mahasiswa":0, "nama":"doni", "index_buku":2, "tanggal_pinjam":"2025-05-29"},
              {"ID_pinjam":1, "ID_mahasiswa":1,"nama":"indah", "index_buku":10, "tanggal_pinjam":"2025-05-29"},
              {"ID_pinjam":2, "ID_mahasiswa":2,"nama":"kiki", "index_buku":8, "tanggal_pinjam":"2025-06-17"},
              {"ID_pinjam":3, "ID_mahasiswa":3,"nama":"budi", "index_buku":1, "tanggal_pinjam":"2025-06-20"},
              {"ID_pinjam":4, "ID_mahasiswa":4,"nama":"caca", "index_buku":3, "tanggal_pinjam":"2025-06-29"},
              {"ID_pinjam":5, "ID_mahasiswa":5,"nama":"ikis", "index_buku":4, "tanggal_pinjam":"2025-07-02"},
              {"ID_pinjam":6, "ID_mahasiswa":0,"nama":"doni", "index_buku":7, "tanggal_pinjam":"2025-07-19"},
              {"ID_pinjam":7, "ID_mahasiswa":6,"nama":"mawar", "index_buku":6, "tanggal_pinjam":"2025-08-29"},
              {"ID_pinjam":8, "ID_mahasiswa":7,"nama":"adit", "index_buku":9, "tanggal_pinjam":"2025-08-15"},
              {"ID_pinjam":9, "ID_mahasiswa":4,"nama":"caca", "index_buku":0, "tanggal_pinjam":"2025-08-15"}]

nama_pinjam = {"ID_pinjam":"index pinjam", "ID_mahasiswa":"ID mahasiswa","nama":"nama mahasiswa", "index_buku":"kode buku", "tanggal_pinjam":"tanggal pinjam"}

def print_tabel_pinjam(data_tabel_pinjam, nama_pinjam):
    print(tabulate(data_tabel_pinjam, headers= 'keys', tablefmt= "pretty"))



#--- TABEL PENGEMBALIAN BUKU ---#
tabel_pengembalian = [{"ID_pengembalian":0, "ID_mahasiswa":1,"nama":"indah", "index_buku":10, "tanggal_pinjam":"2025-05-29", "tanggal_pengembalian":"2025-05-30", "keterlambatan hari":"0"},
                        {"ID_pengembalian":1, "ID_mahasiswa":2,"nama":"kiki", "index_buku":8, "tanggal_pinjam":"2025-06-17", "tanggal_pengembalian":"2025-06-23", "keterlambatan hari":"3"},
                        {"ID_pengembalian":2, "ID_mahasiswa":3,"nama":"budi", "index_buku":1, "tanggal_pinjam":"2025-06-20", "tanggal_pengembalian":"2025-06-30", "keterlambatan hari":"7"},
                        {"ID_pengembalian":3, "ID_mahasiswa":5,"nama":"ikis", "index_buku":4, "tanggal_pinjam":"2025-07-02", "tanggal_pengembalian":"2025-07-05", "keterlambatan hari":"0"},
                        {"ID_pengembalian":4, "ID_mahasiswa":0,"nama":"doni", "index_buku":7, "tanggal_pinjam":"2025-07-19", "tanggal_pengembalian":"2025-07-25", "keterlambatan hari":"3"},
                        {"ID_pengembalian":5, "ID_mahasiswa":4,"nama":"caca", "index_buku":0, "tanggal_pinjam":"2025-08-15", "tanggal_pengembalian":"2025-08-16", "keterlambatan hari":"0"}]

nama_pengembalian = {"ID_pengembalian":"index pengembalian", "ID_mahasiswa":"ID mahasiswa","nama":"nama mahasiswa", "index_buku":"kode buku","tanggal_pinjam":"tanggal pinjam",
                      "tanggal_pengembalian":"tanggal pengembalian", "keterlambatan hari":"keterlambatan hari"}

def print_tabel_pengembalian(data_tabel_pengembalian, nama_pengembalian):
    print(tabulate(data_tabel_pengembalian, headers= 'keys', tablefmt= "pretty")) 



#--- TABEL DAFTAR ANGGOTA PERPUSTAKAAN ---#
tabel_anggota = [{"ID_mahasiswa":0, "nama":"doni", "tahun_bergabung": 2015,"jumlah_pinjaman_buku":2},
                  {"ID_mahasiswa":1, "nama":"indah","tahun_bergabung": 2018, "jumlah_pinjaman_buku":1},
                  {"ID_mahasiswa":2, "nama":"kiki", "tahun_bergabung": 2020, "jumlah_pinjaman_buku":1},
                  {"ID_mahasiswa":3, "nama":"budi", "tahun_bergabung": 2020, "jumlah_pinjaman_buku":1},
                  {"ID_mahasiswa":4, "nama":"caca", "tahun_bergabung": 2021, "jumlah_pinjaman_buku":2},
                  {"ID_mahasiswa":5, "nama":"ikis", "tahun_bergabung": 2024, "jumlah_pinjaman_buku":1},
                  {"ID_mahasiswa":6, "nama":"mawar", "tahun_bergabung": 2025, "jumlah_pinjaman_buku":1},
                  {"ID_mahasiswa":7, "nama":"adit", "tahun_bergabung": 2025, "jumlah_pinjaman_buku":1}]

nama_anggota = {"ID_mahasiswa":"ID mahasiswa", "nama_mahasiswa":"nama mahasiswa", "tahun_bergabung": "tahun bergabung","jumlah_pinjaman_buku":"total peminjaman buku"}

def print_tabel_anggota(tabel_anggota):
    print(tabulate(tabel_anggota, headers= 'keys', tablefmt= "pretty")) 



#--- 2. MENAMBAHKAN BUKU ---#
def tambah_buku(data_tabel_buku):

    ## Meminta input untuk buku baru ditambahkan ke database
    while True:
        judul = input("Masukkan judul buku: ").lower()
        # Validasi agar tidak ada buku yang sama
        if judul in {buku["judul_buku"] for buku in data_tabel_buku}:
            print(f" Error. Buku {judul} sudah ada dalam database")
            continue
        else:
            break
    
    # Validasi input adalah string
    while True:
        penulis = input("Masukkan penulis buku: ")
        kategori = input("Masukkan kategori buku: ")
        status = input("Masukkan status buku (Tersedia/Tidak tersedia): ")
        if penulis.isalpha() and kategori.isalpha() and status.isalpha:
            break
        else:
            print("input tidak valid! hanya boleh huruf tanpa spasi/angka.")
    
    # Validasi tahun terbit hanya berupa angka
    while True:
        tahun_terbit = input("Masukkan tahun terbit buku: ")
        if len(tahun_terbit)== 4 and tahun_terbit.isnumeric():
            int(tahun_terbit)
            break
        else:
            print("Input tidak valid! Harap masukkan 4 angka saja.")
     
    ## menambah buku baru ke tabel daftar buku
    indeks_buku_baru = max([buku["index_buku"] for buku in data_tabel_buku])+1

    item_baru = {"index_buku": indeks_buku_baru, "judul_buku": judul, "penulis_buku":penulis, 
                 "kategori_buku":kategori, "tahun_terbit":tahun_terbit, "status_buku":status}
    data_tabel_buku.append(item_baru)
    return



#--- 3. HAPUS BUKU DIDALAM DAFTAR BUKU---#
def hapus_buku(data_tabel_buku):
    index_buku = input_index_buku(data_tabel_buku, "Masukkan index buku yang ingin dihapus: ")
    print(tabulate([{"index_buku": index_buku,
                     "judul_buku": data_tabel_buku[index_buku]["judul_buku"], 
                     "penulis_buku":data_tabel_buku[index_buku]["penulis_buku"], 
                     "kategori_buku":data_tabel_buku[index_buku]["kategori_buku"], 
                     "tahun_terbit":data_tabel_buku[index_buku]["tahun_terbit"], 
                     "status_buku":data_tabel_buku[index_buku]["status_buku"]}], headers= 'keys', tablefmt= "pretty")) 
    
    # meminta konfirmasi sebelum menghapus buku
    konfirmasi = input_konfirmasi ("Apakah anda ingin menghapus item di atas? (ya/tidak) = ")
    if konfirmasi == "ya":
        data_tabel_buku.pop(index_buku)
        return
    else:
        return


## Mengulang permintaan input hingga pengguna memasukkan 'ya' atau 'tidak'
def input_konfirmasi(pesan):
    konfirmasi = ""
    while konfirmasi not in {"ya","tidak"}:
        konfirmasi = input(pesan).lower()
    return konfirmasi


def input_index_buku(data_tabel_buku,pesan):
    while True:
        index_buku = input(pesan)
        if not index_buku.isnumeric():
            print(f"Error. indeks{index_buku} tidak ada dalam database")
            continue
        
        index_buku = int(index_buku)

        if index_buku not in {buku["index_buku"] for buku in data_tabel_buku}:
            print(f"Error. indeks{index_buku} tidak ada dalam database")
            continue
        
        return index_buku
    


#--- 4. PEMINJAMAN BUKU---#
def pinjam_buku(data_tabel_pinjam):

    # Validasi input adalah huruf
    while True:
        nama_peminjam = input("Masukkan nama anda: ").strip()
        nama_peminjam = nama_peminjam.replace(" ","")
        if nama_peminjam.isalpha():
            break
        else:
            print("Input tidak valid! Hanya boleh huruf tanpa ")

    # validasi ID 
    while True:
        peminjam = input("Masukkan ID mahasiswa: ")
        if peminjam.isnumeric():
            break 
        else:
            print("Input tidak valid! Pastikan ID mahasiswa berupa angka.")
    
    peminjam = int(peminjam)
    daftar_buku_tersedia = filter_buku_tersedia(tabel_buku)
    list_index_tersedia = [buku["index_buku"] for buku in daftar_buku_tersedia]

    # Validasi index_buku di tabel_buku_tersedia
    while True:
        kode_buku = input("Masukkan index buku: ")
        if not kode_buku.isnumeric():
            print("index harus berupa angka!")
            continue

        kode_buku = int(kode_buku)
        
        if kode_buku in list_index_tersedia:
            break
        else:
            print("index buku tidak valid! Silahkan Masukkan kembali index buku")

    tanggal_pinjam= input("Masukkan tanggal pinjam buku (tahun-bulan-tanggal): ")
    indeks_pinjam = max([buku["ID_pinjam"] for buku in data_tabel_pinjam]) +1
    pinjam_baru = {"ID_pinjam": indeks_pinjam,"ID_mahasiswa": peminjam,"nama":nama_peminjam, "index_buku":kode_buku, "tanggal_pinjam":tanggal_pinjam}
    data_tabel_pinjam.append(pinjam_baru)

    # Update status_buku pada tabel_buku
    tabel_buku[kode_buku]["status_buku"] = "Tidak tersedia"

    # Update jumlah_pinjaman_buku pada tabel_anggota
    total_pinjam = None
    for anggota in tabel_anggota:
        if peminjam == anggota["ID_mahasiswa"] :
            total_pinjam = anggota
            break
    
    total_pinjam["jumlah_pinjaman_buku"] =+1
    
    return print(tabulate(data_tabel_pinjam, headers= 'keys', tablefmt= "pretty")) 



#--- 5. PENGEMBALIAN BUKU---#
def pengembalian_buku(data_pengembalian_buku):
    while True:
        pengembali = int(input("Masukkan ID mahasiswa: "))
        for peminjam in tabel_pinjam:
            if peminjam["ID_mahasiswa"] == pengembali:
                peminjam_ditemukan = peminjam
                break
    
        if peminjam_ditemukan:
            print("\n Data Peminjam Ditemukan")
            print(tabulate([peminjam_ditemukan], headers='keys', tablefmt='pretty'))
            break
        else:
            print("Maaf Data Peminjaman dengan ID tersebut tidak ada. Silahkan masukkan ID mahasiswa kembali.")


    t_pinjam = tabel_pinjam[pengembali]["tanggal_pinjam"]
    k_buku = tabel_pinjam[pengembali]["index_buku"]
    nama = tabel_pinjam[pengembali]["nama"]
    tanggal_pengembalian = input("Masukkan tanggal pengembalian buku (tanggal-bulan-tanggal):  ")
    keterlambatan_hari = hitung_keterlambatan_hari(t_pinjam,tanggal_pengembalian)
    
    ## menambah data pengembalian baru ke tabel pengembalian buku
    indeks_pengembalian = max([buku["ID_pengembalian"] for buku in data_pengembalian_buku]) +1
    pengembalian_baru = {"ID_pengembalian": indeks_pengembalian,"ID_mahasiswa": pengembali,"nama":nama, "index_buku":k_buku, 
                        "tanggal_pinjam":t_pinjam, "tanggal_pengembalian": tanggal_pengembalian, "keterlambatan hari": keterlambatan_hari}
    data_pengembalian_buku.append(pengembalian_baru)

    # Update status_buku pada tabel_buku
    kode_buku = int(k_buku)
    tabel_buku[kode_buku]["status_buku"] = "Tersedia"
    
    # Print jumlah keterlambatan
    print(hitung_denda(keterlambatan_hari))
    print("\n Tabel Pengembalian")
    print(tabulate(data_pengembalian_buku, headers = 'keys', tablefmt= "pretty"))
    
    return


# cara menghitung keterlambatan hari & denda
def hitung_keterlambatan_hari(t_pinjam,tanggal_pengembalian):
    t_pinjam = datetime.strptime(t_pinjam,"%Y-%m-%d")   
    tanggal_pengembalian = datetime.strptime(tanggal_pengembalian,"%Y-%m-%d")
    selisih_hari =(tanggal_pengembalian) - (t_pinjam)
    batas_waktu = 3
    waktu = selisih_hari.days
    hari_terlambat = waktu - batas_waktu
    return hari_terlambat

def hitung_denda(keterlambatan_hari):
    while True:
        if keterlambatan_hari > 3 :
            denda = keterlambatan_hari * 1000
            print(f" Anda terlambat {keterlambatan_hari} hari, dan terkena denda sebesar {denda} rupiah")
            break
        if keterlambatan_hari <= 3:
            print("tidak ada denda")
            break
    return



#--- 6. PENDAFTARAN ANGGOTA BARU PERPUSTAKAAN ---#
def pendaftaran_anggota(data_tabel_anggota):
    nama = input("Masukkan Nama Anda: ")
    tahun_bergabung = input("Masukkan Tahun Angkatan Anda: ")
    indeks_mahasiswa = max([mahasiswa["ID_mahasiswa"] for mahasiswa in data_tabel_anggota]) +1
    anggota_baru = {"ID_mahasiswa": indeks_mahasiswa, "nama": nama, "tahun_bergabung": tahun_bergabung,"jumlah_pinjaman_buku": 0 }
    data_tabel_anggota.append(anggota_baru)

    return print(tabulate(data_tabel_anggota, headers = 'keys', tablefmt= "pretty"))
    


#--- FILTER BUKU TERSEDIA ---#
def filter_buku_tersedia(tabel_buku):
    buku_tersedia = []
    for buku in tabel_buku:
        if buku["status_buku"].lower() == "tersedia":
            buku_tersedia.append(buku)

    print("Daftar Buku Tersedia:")
    if buku_tersedia:
        print(tabulate(buku_tersedia, headers= 'keys', tablefmt= "pretty"))
    else:
        print("Tidak ada buku yang tersedia.")
    
    return buku_tersedia



#--- SANDI ADMIN ---#
def sandi():
    while True:
        sandi = 98765
        input_sandi = int(input("Masukkan sandi admin: "))
        if input_sandi == sandi:
            break
        else:
            print("Input tidak valid! Silahkan masukkan kembali sandi admin.")
    
    return



#--- MENU UTAMA ---#
def main_menu():
    while True:
        pilihan_menu = input(''' 
        ===================================================================
         ~ SELAMAT DATANG DI PERPUSTAKAAN BAHAGIA ~
        
        List Menu
        Masuk sebagai:
            1. Pengunjung
            2. Admin Perpustakaan
            3. Exit Program
        
        Masukkan angka Menu yang ingin dijalankan :
        ===================================================================
        ''' ).strip()

        if pilihan_menu == "1":
            menu_pengunjung()
        
        elif pilihan_menu == "2":
            sandi()
            menu_admin()
        
        elif pilihan_menu == "3":
            print("\n Program ditutup. Terima kasih!")
            break

        else:
            print("\n Invalid input. Silahkan masukkan 1,2, atau 3.")
            continue
    return


#--- MENU PENGUNJUNG---#
def menu_pengunjung():
    while True:
        pilihan_daftar = input(''' 
        ===================================================================
         ~ SELAMAT DATANG DI PERPUSTAKAAN BAHAGIA ~
        
        List Menu Pengunjung Perpustakaan:
        1. Menampilkan Daftar Buku
        2. Peminjaman Buku
        3. Pendaftaran Anggota Baru Perpustakaan
        4. Kembali Ke Menu Utama
        
        Masukkan angka Menu yang ingin dijalankan :
        ===================================================================
        ''' ).strip()

        if pilihan_daftar == "1" :
            print("\n DAFTAR BUKU")
            print_tabel_buku(tabel_buku, nama_kolom)
        
        elif pilihan_daftar == "2" :
            pinjam_buku(tabel_pinjam)
            print_tabel_pinjam(tabel_pinjam, nama_pinjam)
        
        elif pilihan_daftar == "3" :
            pendaftaran_anggota(tabel_anggota)
        
        elif pilihan_daftar == "4" :
            break

        else:
            print("\n Invalid input.")
            continue
    
    return


#--- MENU ADMIN---#
def menu_admin():
    while True:
        pilihan_daftar = input(''' 
        ===================================================================
         ~ SELAMAT DATANG DI PERPUSTAKAAN BAHAGIA `
        
        List Menu Admin Perpustakaan:
        1. Menampilkan Daftar Buku
        2. Menambahkan Buku di Daftar Buku
        3. Menghapus Buku di Daftar Buku
        4. Peminjaman Buku
        5. Pengembalian Buku
        6. Pendaftaran Anggota Baru Perpustakaan
        7. Kembali Ke Menu Utama
        
        Masukkan angka Menu yang ingin dijalankan : 
        ===================================================================
        ''' ).strip()

        if pilihan_daftar == "1" :
            print("DAFTAR BUKU \n")
            print_tabel_buku(tabel_buku, nama_kolom)
        
        elif pilihan_daftar == "2" :
            print_tabel_buku(tabel_buku, nama_kolom)
            tambah_buku(tabel_buku)
            print_tabel_buku(tabel_buku, nama_kolom)
        
        elif pilihan_daftar == "3" :
            print_tabel_buku(tabel_buku, nama_kolom)
            hapus_buku(tabel_buku)
            print_tabel_buku(tabel_buku, nama_kolom)
        
        elif pilihan_daftar == "4" :
            pinjam_buku(tabel_pinjam)
            print_tabel_pinjam(tabel_pinjam, nama_pinjam)
        
        elif pilihan_daftar == "5":
            pengembalian_buku(tabel_pengembalian)
            print("\n Daftar Buku di Perpustakaan Bahagia")
            print_tabel_buku(tabel_buku, nama_kolom)
        
        elif pilihan_daftar == "6" :
            pendaftaran_anggota(tabel_anggota)

        elif pilihan_daftar == "7" :
            break

        else:
            print("\n Invalid input.")
            continue
    return

if __name__ == '__main__':
    main_menu()



