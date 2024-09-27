# print("Perulangan ke-0")
# print("Perulangan ke-1")
# print("Perulangan ke-2")
# print("Perulangan ke-3")
# print("Perulangan ke-4")
# print("Perulangan ke-5")I
# print("Perulangan ke-6")
# print("Perulangan ke-7")
# print("Perulangan ke-8")
# print("Perulangan ke-9")

# batas = 20

# for i in range(10, batas, 2):
#     print(f"Perulangan ke-{i}")

# buah_banyak = ["Apple", "Mangga", "Anggur", "Semangka"]
# for buah in buah_banyak:
#     print(buah)

# for baris in range(1, 4):
#     print("Baris ke ", baris)
#     for kolom in range(1, 4):
#         print(kolom, "Kolom", end=" ")
#     print()

#     print()

# Jangan pernah sampai perulangan tak terbatas
# while True:
    # print("Hello")

# lagi = "ya"
# ulang = 0
# while lagi == "ya":
#     ulang += 1
#     print("Mabar")
#     lagi = input("Mabar lagi ga?")
# print(f"Selesai mabar!")
# print(f"Perulangan sebanyak {ulang} kali")

# for i in range(1, 10):
#     if i == 4:
#         break
#     else:
#         print(f"perulangan ke {i} kali")

# buah_banyak = ["Apple", "Mangga", "Anggur", "Semangka"]
# for buah in buah_banyak:
#     if buah == "Anggur":
#         print("Buah anggur ketemu")
#         break
#     else:
#         print("Belum ditemukan")

# while True:
#     ulang = input("Mabar lagi: ")
#     if ulang.lower() == "gak":
#         break
#     print(f"Mabar sebanyak {ulang} kali")

# for i in range(1, 10):
#     if i % 2 == 1:
#         continue
#     print(f"perulangan ke {i} kali")

# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#     print(f"perulangan ke {i} kali")
    
    # Break itu untuk mengstop pada variabel itu
    # Continue sebaliknya untuk mengskip atau meloncati variabel itu

# Matrix
# for i in range(0, 5):
#     for j in range(0, 5):
#         print("*", end=" ")
#     print()

# # Segitiga sama kaki
# for i in range(0, 5):
#     if i == +1:
#         print("*", end=" ")

kesempatan = 3
while kesempatan > 0:
    if kesempatan:
        username = input("Masukan username anda : ")
        password = input("Masukan password anda : ")

    if username == "Admin" and password == "Admin1234":
            print("Anda berhasil login")
            break
    
    else:
        print("Username atau password anda salah")
        kesempatan -= 1
    
print("Kesempatan Anda Sudah Habis")