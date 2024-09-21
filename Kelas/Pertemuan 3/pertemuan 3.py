# cuaca = "cerah"
# if cuaca == "cerah":
#     print("Kamu pergi keluar rumah")


# Variabel akan bernilai false jika string kosong, nol, [], (), {}, false
# uang = 1

# # Ini pemborosan
# # if uang == True:

# if uang :
#     print("Kamu pergi ke pasar!")
# else :
#     print("Pergi kerumah teman!")

# nilai = 70

# if nilai < 70:
#     print("Tidak lulus")
# else:
#     print("lulus")

# Ini dari saya
# angka = 63

# if angka % 2 == 0:
#     print("Genap")
# else:
#     print("Ganjil")

# Ini untuk punya gusni
# nilai = -0

# if nilai >0:
#     print("Nilai positif")
# else:
#     print("Nilai negatif")

# contoh dari modul 

# Umur = int(input("Masukkan umur Anda : "))
# if Umur <= 10:
#     print("Umur Anda termasuk kategori anak-anak")
# elif Umur <= 18:
#     print("Umur Anda termasuk kategori remaja")
# elif Umur <= 35:
#     print("Umur Anda termasuk kategori dewasa")
# elif Umur <= 65:
#     print("Umur Anda termasuk kategori paruh baya")
# else:
#     print("Umur Anda termasuk kategori tua")

# Wajib indentasi untuk memasukan agar kodenya berjalan dengan sesuai yang diinginkan

# nilai = 84

# if nilai >= 80:

#     if nilai >= 85:
#         print("A+")
    
#     else:
#         print("A-")

# else:
#     print("Tidak Lulus")    

# Test dari abang vito dan bang adi
# print("Menu :")
# print("1. Nonton film")
# print("2. Ngoding")
# print("3. Keluar")

# nilai = int(input("Masukan pilihan : "))
# if nilai == 1 :
#     print("Sedang nonton film")

# elif nilai == 2 :
#     print("Sedang ngoding")

# elif nilai == 3 :
#     print("Keluar")

# else:
#     print("Tidak tersedia")

# error ji
# if nilai == "1" :
    
#     if nilai == "2" :
        
#         if nilai == "3" :
#             print("Sedang nonton film")
#     else:
#         print("Sedang ngoding")
# else:
#     print("keluar")

# Perbedaan if if dan if elif

# Kondisi pertama
# angka = 10
# if angka % 2 == 0:
#     print("Genap")
# if angka > 0:
#     print("Ganjil")

# # Kondisi kedua
# angka = 10
# if angka % 2 == 0:
#     print("Genap")
# elif angka > 0 :
#     print("Ganjil")

# Review
jumlah = int(input("Masukan jumlah buku yang anda beli : "))
harga = int(input("Masukan harga yang anda beli : "))
totalharga = jumlah*harga
diskon = totalharga/20*100

if jumlah >= 5 :
    print(f"Harga sebelum diskon {totalharga} anda mendapat diskon sebesar 20% untuk pembelian item diatas 5, total belanja anda menjadi {diskon}")
else:
    print(f"Total belanja anda {totalharga}, mohon maaf anda tidak mendapat diskon")