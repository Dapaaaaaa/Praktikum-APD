import os
data_mahasiswa =["Ifnu","Adi","ucup","michael"]

def clear_screen():
    os.system('cls || clear')

def tampilkan_mahasiswa():
    for i in range(len(data_mahasiswa)):
        print(f"data ke {i+1}")
        print(f"Nama : {data_mahasiswa[i]}")
        print("="*10)

def tambah_data():
    print("MENU TAMBAH DATA")
    print("=" * 10)
    inputUser = input("Data yang mau ditambahkan : ")
    data_mahasiswa.append(inputUser)
    print(f"{inputUser} telah ditambahkan")

def ubah_data():
    print("Menu ubah data")
    tampilkan_mahasiswa()
    index= int(input("masukkan index yang mau diedit : "))
    data_baru =input("masukkan nama anda :")
    data_mahasiswa[index-1]=data_baru
    print("data berhasil diubah")
    input("Enter.....")
    
def hapus_data():
    print("Menu Hapus Data")
    tampilkan_mahasiswa()
    index_user = int(input("masukkan index yang ingin dihapus: "))
    del_user = data_mahasiswa.pop(index_user-1)
    
    return del_user
        
def menu():
        print("""
    Menu
Lihat Data  >> 1
Tambah Data >> 2
Edit Data   >> 3
Hapus Data  >> 4
Keluar      >> 5
""")  

while True:
    menu()
    pilih = input("Masukan Pilihan menu >> ")  
    
    match(pilih):
        case "1":
            print("===Lihat Data===")
            tampilkan_mahasiswa()
            input("Enter.....")
            clear_screen()
            
        case "2":
            tambah_data()
            
            input("Enter....")
            clear_screen()
            
        case "3":
            ubah_data()
            clear_screen()
            
        case "4":
            hapus = hapus_data()
            print(f"{hapus} telah dihapus")
            input("Enter......")
            clear_screen()
            
        case "5":
            print("Anda memilih menu 5")
            exit()
            clear_screen()
        case _:
            print(f"Menu {pilih} tidak tersedia")
            input("Enter.....")
            clear_screen()