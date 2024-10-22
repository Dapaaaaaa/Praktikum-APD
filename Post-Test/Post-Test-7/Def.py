# Disini adalah file fungsi
import os
from time import sleep

width = 50
# Data list makanan
daftarmenu = {
    "menumakanan" : ["Nasi Goreng", "Mie Goreng", "Telor Orak-arik", "Chicken Katsu"],
    "menuminuman" : ["Es Teh", "Teh Hangat", "Cappucino", "Americano",],
    "menusnack" : ["Kentang Goreng", "Lumpia", "Risoles", "Ote-Ote"]
}

def dekor():
    print("="*width)

def clear():
    os.system("cls")

def lihatmenu():
    dekor()
    print("Menu Makanan, Minuman, dan Snack".center(width))    
    dekor()

    print("Menu Makanan".center(width))
    dekor()
    for i, item in enumerate(daftarmenu["menumakanan"]):
        print(f"{i+1}. {item}")
    dekor()

    print("Menu Minuman".center(width))
    dekor()
    for i, item in enumerate(daftarmenu["menuminuman"]):
        print(f"{i+1}. {item}")
    dekor()

    print("Menu Snack".center(width))
    dekor()
    for i, item in enumerate(daftarmenu["menusnack"]):
        print(f"{i+1}. {item}")
    dekor()

    print("Tekan ENTER untuk keluar")
    input("Enter...")
    

def tambahdata (tipemenu, item):
    if tipemenu not in daftarmenu:
        print(f"Tipe menu '{tipemenu}' tidak ditemukan. Harus salah satu dari: {list(daftarmenu.keys())}")
        return
    
    if not item.strip():
        dekor()
        print("Menu tidak boleh kosong atau hanya berisi spasi!".center(width))
        dekor()
        sleep(2)
        clear()
        return
    
    item = item.title()
    
    if item in daftarmenu[tipemenu]:
        dekor()
        print(f"Menu '{item}' sudah ada di dalam menu .".center(width))
        dekor()
        sleep(2)
        clear()
        return
    
    daftarmenu[tipemenu].append(item)
    dekor()
    print(f"Menu '{item}' berhasil ditambahkan kedalam menu!")
    dekor()
    sleep(2)
    clear()

def ubahdata(tipemenu):
    dekor()
    print(f"Menu {tipemenu}".center(width))
    dekor()

    for i, item in enumerate(daftarmenu[tipemenu]):
        print(f"{i + 1}. {item}")

    dekor()
    item_update = int(input(f"Masukkan nomor {tipemenu} yang ingin diupdate: ")) - 1
    clear()

    if 0 <= item_update < len(daftarmenu[tipemenu]):
        dekor()
        print("Masukan Nama!".center(width))
        dekor()
        itembaru = input(f"Masukkan nama baru untuk {daftarmenu[tipemenu][item_update]}: ")
        daftarmenu[tipemenu][item_update] = itembaru.title()
        dekor()
        print(f"Data berhasil diperbarui menjadi: {daftarmenu[tipemenu][item_update]}".center(width))
        dekor()
        sleep(2)
        clear()
    else:
        dekor()
        print("Nomor yang Anda masukkan tidak valid!".center(width))
        dekor()
        sleep(1)
        clear()
        
def hapusdata(tipemenu):
    dekor()
    print(f"Menu {tipemenu}".center(width))
    dekor()

    for i, item in enumerate(daftarmenu[tipemenu]):
        print(f"{i + 1}. {item}")

    dekor()
    item_hapus = int(input(f"Masukkan nomor {tipemenu} yang ingin dihapus: ")) - 1
    clear()

    if 0 <= item_hapus < len(daftarmenu[tipemenu]):
        dekor()
        print(f"Menu {daftarmenu[tipemenu][item_hapus]} telah dihapus!".center(width))
        dekor()
        daftarmenu[tipemenu].pop(item_hapus)
        sleep(2)
        clear()
    else:
        dekor()
        print("Nomor yang Anda masukkan tidak valid!".center(width))
        dekor()
        sleep(1)
        clear()
        
def daftaruser(user):
    clear()
        
    while True:
        dekor()
        print("Registrasi".center(width))
        dekor()
        
        username = input("Masukan username : ").strip()
        password = input("Masukan password : ").strip()
        
        if not username or not password:
            clear()
            dekor()
            print("Username dan password tidak boleh kosong!".center(width))
            dekor()
            sleep(2)
            clear()
            
        elif username in [akun["username"] for akun in user]:
            clear()
            dekor()
            print("Username sudah terdaftar!".center(width))
            dekor()
            sleep(2)
            clear()
            
        else:
            user.append({"username" : username , "password" : password, "user" : "user"})
            dekor()
            print("Registrasi berhasil!")
            dekor()
            sleep(2)
            
            clear()
            break
        
def tambahdatalagi(tipemenu):
    dekor()
    item = input("Masukan menu baru : ")

    tambahdata(tipemenu, item)

    lagi = input("Apakah Anda ingin menambah data lagi? (y/n): ").strip().lower()
    if lagi == "y":
        tambahdatalagi(tipemenu)