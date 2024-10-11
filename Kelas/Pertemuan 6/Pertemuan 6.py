# Buah = ["apel", "mangga"]

# Buah = {
#     "buah1" : "apel",
#     "buah2" : "mangga"
# }

# print(Buah["buah1"])

# data_mhs = {
#     "nama" : "ucup",
#     "NIM"  : 1,
#     "Matkul" : ["Algoritma", "Pemrograman", "APD"],
#     # "nama" : "daffa"
# }

# # Cek value
# for value in data_mhs.values():
#     print(value)
    
# # Cek key 
# for key in data_mhs.keys():
#     print(key)

# Nambah data
# data_mhs["alamat"] = "Samarinda"
# data_mhs["alamat"] = "Tenggarong"

# Nambah data (update)
# data_mhs.update({"alamat" : "Samarinda"})
# data_mhs.update({"alamat" : "Tenggarong"})

# data_mhs["nama"] = "daffa"

# # del data_mhs["NIM"]
# cache = data_mhs.pop("NIM")

# # Ini kalau mau ubah key nya yaitu NIM
# print(data_mhs, "Dictionary")
# print(cache, "Cache")
# data_mhs["id"] = cache

# print(data_mhs)

# Menghitung panjang data
# print("Jumlah data =", len(data_mhs))

# Cara clear



# print(data_mhs.get("mapel", "Tidak ada mapel"))

# Tanpa menggunakan items
# for data in data_mhs:
#     print(data)

# Menggunakan items
# for i, j in data_mhs.items():
#     print(i,":", j)
    
# for key_data, items_data in data_mhs.items():
#     print(f"Key : {key_data} \nValue : {items_data}")

# print(data_mhs["nama"])
# print(data_mhs["NIM"])

# print(data_mhs)

# print(data_mhs)

# Kalau value lebih dari 1 akan menjadi tuple = (1, 5, 9)
# key = "apel", "jeruk", "mangga", "Semangka", "Anggur"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 20
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# data_mhs = {
#     "nama" : "ucup",
#     "nim"  : 1,
#     "matkul" : ["APD", "Kalkulus", "Jarkom"],
#     "Dosen" : {
#         "nama" : "Pak Awang",
#         "matkul" : "APD"
#     }
# }

# print(data_mhs["Dosen"]["nama"])

data_mhs = [
    {
    "Nama" : "ucup",
    "Role" : "User"
    },
    
    {
    "Nama" : "daffa",
    "Role" : "Admin"
    }
]

data_mhs2 = [
    ["Ucup", "Admin"],
    ["Daffa", "User"]
]

# Ini untuk data mahasiswa 1 
# print(data_mhs[0]["Nama"])
# print(data_mhs[1])

# Ini data mahasiswa 2
print(data_mhs2[0][1])