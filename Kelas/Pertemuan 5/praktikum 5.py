# # contoh

# # data = [1, 2, 3, 4, True, [2, 3], "Adi"]
# # data_2 = list((1, 2, 3, 4, 5))


# # ini untuk list
# # print(data[1])

# # # Ini untuk list dalam list
# # print(data[5][-1])
# # print(type(data_2))

# data = ["Apel", "Durian", "Jeruk"]
# # print(data)
# print()

# # # Untuk nambah data di akhir
# # data.append("Semangka")
# # data.append("Semangka")
# # data.append(True)

# # print(data)
# # print()

# # # Untuk menambah data
# # data.extend(["Rambutan", "Semangka"])

# # # Masukan data di awal
# # data.insert(0, "Rambutan")
# # print(data)

# # print(len(data))


# # Untuk mengubah data
# # data[0] = "Anggur"
# print(data)

# # bisa memakai slicing
# # data [0:2]= ["Anggur", "Mangga"]
# # print(data)

# # Metode delete
# # del data[1]
# print(data)

# # DEL itu ngehapus sampai kedata
# # POP itu cumman tidak menampilkan

# # Method pop
# data.pop(1)
# print()
# print(data)

# # Bisa munculkan pop
# nilai_hapus = data.pop(1)
# print(nilai_hapus)

# # Untuk method REMOVE hanya bisa didalam list kurang disarankan karena hanya bisa 1 data awal saja apabila sama
# data.remove("Apel")
# print(data)

# # Output agar banyak atau berkali kali
# data = ["Apel", "Durian", "Jeruk"]
# print(data*3)

# Untuk nested list
# data_mahasiswa = [
#     ["060", "Ifnu", ["APD", "Arsikom"]],
    
#     ["065", "Adi"]
# ]

# print(data_mahasiswa[0][2][0])

# Untuk user
# data_mahasiswa = [
#     ["Admin", "Admin1234", "Admin"],
#     ["User", "User1234", "User"]
# ]

# # print(data_mahasiswa[0][1])

# # Perulangan
# buah = ["Apel", "Durian", "Jeruk"]
# index = 1

# Cara mencari ke 1
# for data in buah:
#     print(f"Data ke {index}")
#     print(data)
#     print("="*5)
#     index += 1

# Ini cara mencari ke 2
# for index in range(len(buah)):
#     print(f"Data ke {index+1}")
#     print(buah[index])
#     print("="*5)

# Cara mencari ke 3
# for index, item in enumerate(buah):
#     print(f"Data ke {index+1}")
#     print(item)

# for index, item in enumerate(data_mahasiswa):
#     print(f"Data ke {index+1}")
#     print(f"Username anda : {item[0]}")
#     print(f"password anda : {item[1]}")
#     print(f"status anda   : {item[2]}")

# buah = ["Apel", "Durian", "Jeruk"]
# buah1, buah2, buah3 = buah

# print(buah1)
# print(buah2)
# print(buah3)

# buah1, * banyak_buah = buah
# # mengambil banyak data sekaligus
# print(buah1)
# print(banyak_buah)