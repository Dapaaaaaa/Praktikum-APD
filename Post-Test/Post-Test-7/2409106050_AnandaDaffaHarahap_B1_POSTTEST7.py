# import os
from time import sleep
from Def import *


login = "y"
Kesempatan = 3

# Data Pengguna
user = [{
    "username": "admin",
    "password": "admin123",
    "user": "admin"
    },
    
    {
    "username": "daffa",
    "password": "daffa",
    "user": "user"       
    }
]  

while login == "y":
    clear()
    dekor()
    print("Selamat Datang".center(width))
    dekor()
    print("Pilih kebutuhan : \n1. Login \n2. Registrasi \n3. Keluar")
    dekor()
    
    kebutuhan = input("Pilihan : ")
    if kebutuhan == "1":
        
        clear()
        dekor()
        print("Sistem Daftar Antri Makanan".center(width))

        kesempatan = 3
        dekor()
        print("Anda punya 3 kali kesempatan!".center(width))
        dekor()
        
        loginuser = "y"
        while kesempatan > 0 and loginuser == "y":

            # Menu admin
            username = input("Masukan username : ").strip()
            password = input("Masukan password : ").strip()
            dekor()
        
            if not username or not password:
                clear()
                dekor()
                print("Username dan Password tidak boleh kosong atau spasi!")
                dekor()
                sleep(2)
                continue
                
            for akun in user:
                if username == akun["username"] and password == akun["password"]:
                    
                    
                    if akun["user"] == "admin":
                        clear()
                        dekor()
                        print("Selamat datang admin!".center(width))
                        dekor()

                        sleep(2)
                        clear()

                        balikmenu = "y"
                        while balikmenu == "y":
                            dekor()
                            print("Menu".center(width))
                            dekor()
                            print("1. Lihat data \n2. Tambah data \n3. Ubah data \n4. Hapus data \n5. Keluar")
                            dekor()

                            menu = input("Masukan pilihan : ")
                            clear()

                            cobapilihan = "y"
                            if menu == "1":
                                lihatmenu()

                                
                            elif menu == "2":

                                while cobapilihan == "y":

                                    dekor()
                                    print("Tambah Data".center(width))
                                    dekor()
                                    print("1. Menu makanan \n2. Menu minuman \n3. Menu Snack \n4. Balik ke menu utama")
                                    dekor()
                                    pilihan = input("Masukan menu : ")

                                    if pilihan == "1":
                                        tipemenu = "menumakanan"
                                        
                                    elif pilihan == "2":
                                        tipemenu = "menuminuman"
                                        
                                    elif pilihan == "3":
                                        tipemenu = "menusnack"

                                    elif pilihan == "4":
                                        cobapilihan = "n"
                                        balikmenu = "y"
                                        continue
                                    
                                    tambahdatalagi(tipemenu)

                            elif menu == "3":

                                while cobapilihan == "y":

                                    dekor()
                                    print("Ubah Data".center(width))
                                    dekor()
                                    print("1. Menu makanan \n2. Menu minuman \n3. Snack \n4. Balik ke menu utama")
                                    dekor()
                                    pilihan = input("Masukan menu : ")
                                    clear()

                                    if pilihan == "1": 
                                        ubahdata("menumakanan")

                                    elif pilihan == "2": 
                                        ubahdata("menuminuman")

                                    elif pilihan == "3":  
                                        ubahdata("menusnack")

                                    elif pilihan == "4":
                                        cobapilihan = "n"
                                        balikmenu = "y"

                            if menu == "4":

                                dekor()
                                print("Hapus Data".center(width))
                                dekor()
                                print("1. Menu makanan \n2. Menu minuman \n3. Snack \n4. Balik ke menu utama")
                                dekor()
                                pilihan = input("Masukan menu : ")
                                clear()

                                if pilihan == "1":
                                    hapusdata("menumakanan")

                                elif pilihan == "2":
                                    hapusdata("menuminuman")

                                elif pilihan == "3":
                                    hapusdata("menusnack")

                                elif pilihan == "4":
                                    cobapilihan = "n"
                                    balikmenu = "y"

                            elif menu == "5":
                                balikmenu = "n"
                                loginuser = "n"
                                dekor()
                                print("Anda berhasil keluar!".center(width))
                                dekor()

                                sleep(2)
                                break

                    elif akun["user"] == "user":
                        
                        lihatmenu()
                        
                    loginuser = "n"
                    break

            else:
                clear()
                kesempatan -= 1
                dekor()
                print("Username atau Password yang anda masukan salah!".center(width))
                print(f"kesempatan anda tersisa {kesempatan}".center(width))
                dekor()

        if kesempatan == 0:
            dekor()
            print("Anda telah mencapai batas kesempatan!".center(width))
            dekor()

            sleep(2)

            clear()
            login = "n"
            break
            

    elif kebutuhan == "2":
        daftaruser(user)
    
    elif kebutuhan == "3":
        login = "n"
        loginuser = "n"
        kesempatan = 0
        clear()
        dekor()
        print("Anda berhasil keluar!".center(width))
        dekor()
        sleep(2)
        clear()
        break