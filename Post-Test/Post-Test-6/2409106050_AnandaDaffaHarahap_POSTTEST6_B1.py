import os
from time import sleep

width = 50

# Data Pengguna
user = [["admin", "admin123", "admin"]]


# Data list makanan
menumakanan = ["Nasi goreng", "Mie goreng", "Telor orak-arik", "Chicken katsu"]
menuminuman = ["Es teh", "Teh hangat", "Cappucino", "Americano"]
menusnack = ["Kentang goreng", "Lumpia", "Risoles", "Ote-ote"]


login = "y"
while login == "y":
    print("="*width)
    print("Pilih kebutuhan : \n1. Login \n2. Registrasi \n3. Keluar")
    print("="*width)
    kebutuhan = input("Pilihan : ")
    if kebutuhan == "1":
        
        os.system("cls")
        print("="*width)
        print("Sistem Daftar Antri Makanan".center(width))

        kesempatan = 3
        print("="*width)
        print("Anda punya 3 kali kesempatan!".center(width))
        
        while kesempatan > 0:
            print("="*width)

            # Menu admin
            username = input("Masukan username : ").strip()
            password = input("Masukan password : ").strip()
            print("="*width)
        
            if not username or not password:
                print("="*width)
                print("Username dan Password tidak boleh kosong atau spasi!")
                continue
                
            if username == user[0][0] and password == user[0][1] and user[0][2] == "admin":
                print("="*width)
                print("Selamat datang admin!".center(width))
                print("="*width)

                sleep(2)
                os.system("cls")

                balikmenu = "y"
                while balikmenu == "y":
                    print("="*width)
                    print("Menu".center(width))
                    print("="*width)
                    print("1. Lihat data \n2. Tambah data \n3. Ubah data \n4. Hapus data \n5. Keluar")
                    print("="*width)

                    menu = input("Masukan pilihan : ")
                    os.system("cls")

                    cobapilihan = "y"
                    if menu == "1":

                        
                        while cobapilihan == "y":

                            print("="*width)
                            print("Pilih data yang mau ditampilkan".center(width))
                            print("="*width)    

                            print("="*width)
                            print("1. Menu makanan \n2. Menu minuman \n3. Menu snack \n4. Balik ke menu utama")
                            print("="*width)
                            
                            pilihan = input("Masukan pilihan : ")
                            print("="*width)
                            os.system("cls")

                            if pilihan == "1":
                                print("="*width)
                                print("Menu".center(width))
                                print("="*width)

                                for i, item in enumerate(menumakanan):
                                    print(f"{i+1}. {item}")

                                print("="*width)
                                print("Tekan ENTER untuk keluar")
                                print("="*width)
                                input("Enter...")

                            elif pilihan == "2":
                                print("="*width)
                                print("Menu".center(width))
                                print("="*width)

                                for i, item in enumerate(menuminuman):
                                    print(f"{i+1}. {item}")
                                
                                print("="*width)
                                print("Tekan ENTER untuk keluar")
                                print("="*width)
                                input("Enter...")

                            elif pilihan == "3":
                                print("="*width)
                                print("Menu".center(width))
                                print("="*width)

                                for i, item in enumerate(menusnack):
                                    print(f"{i+1}. {item}")

                                print("="*width)
                                print("Tekan ENTER untuk keluar")
                                print("="*width)
                                input("Enter...")
                            
                            elif pilihan == "4":
                                cobapilihan = "n"
                                balikmenu = "y"
                        
                    elif menu == "2":

                        while cobapilihan == "y":

                            print("="*width)
                            print("Tambah Data".center(width))
                            print("="*width)
                            print("1. Menu makanan \n2. Menu minuman \n3. Snack \n4. Balik ke menu utama")
                            print("="*width)
                            pilihan = input("Masukan menu : ")
                            os.system("cls")

                            if pilihan == "1":
                                print("="*width)
                                print("Masukan menu baru".center(width))
                                print("="*width)

                                menubaru = input("Masukan nama menu baru : ")
                                menumakanan.append(menubaru)

                            elif pilihan == "2":
                                print("="*width)
                                print("Masukan menu baru".center(width))
                                print("="*width)

                                menubaru = input("Masukan nama menu baru : ")
                                menuminuman.append(menubaru)

                            elif pilihan == "3":
                                print("="*width)
                                print("Masukan menu baru".center(width))
                                print("="*width)

                                menubaru = input("Masukan nama menu baru : ")
                                menusnack.append(menubaru)

                            elif pilihan == "4":
                                cobapilihan = "n"
                                balikmenu = "y"

                    elif menu == "3":

                        while cobapilihan == "y":

                            print("="*width)
                            print("Ubah Data".center(width))
                            print("="*width)
                            print("1. Menu makanan \n2. Menu minuman \n3. Snack \n4. Balik ke menu utama")
                            print("="*width)
                            pilihan = input("Masukan menu : ")
                            os.system("cls")

                            if pilihan == "1": 
                                print("="*width)
                                print("Menu makanan".center(width))
                                print("="*width)

                                for i, item in enumerate(menumakanan):
                                    print(f"{i+1}. {item}")

                                print("="*width)
                                item_update = int(input("Masukkan nomor makanan yang ingin diupdate: ")) - 1

                                if 0 <= item_update < len(menumakanan):
                                    itembaru = input(f"Masukkan nama baru untuk {menumakanan[item_update]}: ")
                                    menumakanan[item_update] = itembaru
                                    print(f"Data berhasil diperbarui menjadi: {menumakanan[item_update]}")
                                else:
                                    print("Nomor yang Anda masukkan tidak valid!")

                            elif pilihan == "2": 
                                print("="*width)
                                print("Menu minuman".center(width))
                                print("="*width)

                                for i, item in enumerate(menuminuman):
                                    print(f"{i+1}. {item}")

                                print("="*width)
                                item_update = int(input("Masukkan nomor minuman yang ingin diupdate: ")) - 1

                                if 0 <= item_update < len(menuminuman):
                                    itembaru = input(f"Masukkan nama baru untuk {menuminuman[item_update]}: ")
                                    menuminuman[item_update] = itembaru
                                    print(f"Data berhasil diperbarui menjadi: {menuminuman[item_update]}")
                                else:
                                    print("Nomor yang Anda masukkan tidak valid!")

                            elif pilihan == "3":  
                                print("="*width)
                                print("Menu snack".center(width))
                                print("="*width)

                                for i, item in enumerate(menusnack):
                                    print(f"{i+1}. {item}")

                                print("="*width)
                                item_update = int(input("Masukkan nomor snack yang ingin diupdate: ")) - 1

                                if 0 <= item_update < len(menusnack):
                                    itembaru = input(f"Masukkan nama baru untuk {menusnack[item_update]}: ")
                                    menusnack[item_update] = itembaru
                                    print(f"Data berhasil diperbarui menjadi: {menusnack[item_update]}")
                                else:
                                    print("Nomor yang Anda masukkan tidak valid!")

                            elif pilihan == "4":  # Kembali ke menu utama
                                cobapilihan = "n"
                                balikmenu = "y"

                    if menu == "4":

                        print("="*width)
                        print("Hapus Data".center(width))
                        print("="*width)
                        print("1. Menu makanan \n2. Menu minuman \n3. Snack \n4. Balik ke menu utama")
                        print("="*width)
                        pilihan = input("Masukan menu : ")
                        os.system("cls")

                        if pilihan == "1":

                            print("="*width)
                            print("Menu makanan".center(width))
                            print("="*width)

                            menumakanan.pop()

                            print("Menu makanan telah diperbarui!")

                            sleep(3)

                            os.system("cls")

                        elif pilihan == "2":

                            print("="*width)
                            print("Menu minuman".center(width))
                            print("="*width)

                            menuminuman.pop()

                            print("Menu minuman telah diperbarui!")

                            sleep(3)

                            os.system("cls")

                        elif pilihan == "3":

                            print("="*width)
                            print("Menu snack".center(width))
                            print("="*width)

                            menusnack.pop()

                            print("Menu makanan telah diperbarui!")

                            sleep(3)

                            os.system("cls")
                        
                        elif pilihan == "4":
                            cobapilihan = "n"
                            balikmenu = "y"

                    elif menu == "5":
                        balikmenu = "n"
                        kesempatan = 0
                        print("="*width)
                        print("Anda berhasil keluar!".center(width))
                        print("="*width)

                        sleep(3)
                        
                        break

        
            if username == user[1][0] and password == user[1][1] and user[1][2] == "user":
                os.system("cls")
                print("="*width)
                print("MENU".center(width))
                print("="*width)
                
                print("Menu makanan".center(width))
                print("="*width)
                for i, item in enumerate(menumakanan):
                    print(f"{i+1}. {item}")
                    
                print("="*width)
                print("Menu minuman".center(width))
                print("="*width)
                
                for i, item in enumerate(menuminuman):
                    print(f"{i+1}. {item}")
                    
                print("="*width)
                print("Menu snack".center(width))
                print("="*width)    
                
                for i, item in enumerate(menusnack):
                    print(f"{i+1}. {item}")
                
                print("="*width)
                print("Tekan ENTER untuk keluar")
                print("="*width)
                input("Enter...")   
                login = "n"
                break

            else:
                os.system("cls")
                kesempatan -= 1
                print("="*width)
                print("Username atau Password yang anda masukan salah!".center(width))
                print(f"kesempatan anda tersisa {kesempatan}".center(width))

        if kesempatan == 0:
            print("="*width)
            print("Anda telah mencapai batas kesempatan!".center(width))
            print("="*width)

            sleep(2)

            os.system("cls")

            break
            

    elif kebutuhan == "2":
        print("="*width)
        username = input("Masukan username : ").strip()
        password = input("Masukan password : ").strip()
        
        if not username or not password:
            print("Username dan password tidak boleh kosong!")
        else:
            user.append([username, password, "user"])
            print("Registrasi berhasil!")
            sleep(2)
            
            os.system("cls")
    
    elif kebutuhan == "3":
        print("="*width)
        print("Keluar")
        print("="*width)
        break