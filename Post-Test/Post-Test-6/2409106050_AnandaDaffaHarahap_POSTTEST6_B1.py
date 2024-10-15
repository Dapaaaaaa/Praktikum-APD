import os
from time import sleep

width = 50

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


# Data list makanan
daftarmenu = {
    "menumakanan" : ["Nasi Goreng", "Mie Goreng", "Telor Orak-arik", "Chicken Katsu"],
    "menuminuman" : ["Es Teh", "Teh Hangat", "Cappucino", "Americano",],
    "menusnack" : ["Kentang Goreng", "Lumpia", "Risoles", "Ote-Ote"]
}



login = "y"
while login == "y":
    os.system("cls")
    print("="*width)
    print("Selamat Datang".center(width))
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
        print("="*width)
        
        loginuser = "y"
        while kesempatan > 0 and loginuser == "y":

            # Menu admin
            username = input("Masukan username : ").strip()
            password = input("Masukan password : ").strip()
            print("="*width)
        
            if not username or not password:
                os.system("cls")
                print("="*width)
                print("Username dan Password tidak boleh kosong atau spasi!")
                print("="*width)
                sleep(2)
                continue
                
            for akun in user:
                if username == akun["username"] and password == akun["password"]:
                    
                    
                    if akun["user"] == "admin":
                        os.system("cls")
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

                                print("="*width)
                                print("Menu Makanan, Minuman, dan Snack".center(width))    
                                print("="*width)

                                print("Menu Makanan".center(width))
                                print("="*width)
                                for i, item in enumerate(daftarmenu["menumakanan"]):
                                    print(f"{i+1}. {item}")
                                print("="*width)

                                print("Menu Minuman".center(width))
                                print("="*width)
                                for i, item in enumerate(daftarmenu["menuminuman"]):
                                    print(f"{i+1}. {item}")
                                print("="*width)

                                print("Menu Snack".center(width))
                                print("="*width)
                                for i, item in enumerate(daftarmenu["menusnack"]):
                                    print(f"{i+1}. {item}")
                                print("="*width)

                                print("Tekan ENTER untuk keluar")
                                input("Enter...")
                                os.system("cls")
                                
                            elif menu == "2":

                                while cobapilihan == "y":

                                    print("="*width)
                                    print("Tambah Data".center(width))
                                    print("="*width)
                                    print("1. Menu makanan \n2. Menu minuman \n3. Menu Snack \n4. Balik ke menu utama")
                                    print("="*width)
                                    pilihan = input("Masukan menu : ")
                                    os.system("cls")

                                    if pilihan == "1":
                                        print("="*width)
                                        print("Masukan menu makanan baru".center(width))
                                        print("="*width)
                                        
                                        menubaru = ""
                                        while not menubaru.strip():
                                            menubaru = input("Masukan nama menu makanan baru : ")
                                            if not menubaru.strip():
                                                os.system("cls")
                                                print("="*width)
                                                print("Menu makanan tidak boleh kosong!")
                                                print("="*width)
                                                
                                            else: 
                                                menubaru = menubaru.title()
                                                if menubaru in daftarmenu["menumakanan"]:
                                                    os.system("cls")
                                                    print("="*width)
                                                    print("Menu makanan sudah ada!")
                                                    print("="*width)
                                                    menubaru = ""
                                                    
                                                else:
                                                    daftarmenu["menumakanan"].append(menubaru)
                                                    os.system("cls")
                                                    print("="*width)
                                                    print("Berhasil tambah menu!".center(width))
                                                    print("="*width)
                                                    sleep(2)
                                                    os.system("cls")

                                    elif pilihan == "2":
                                        print("="*width)
                                        print("Masukan menu minuman baru".center(width))
                                        print("="*width)

                                        menubaru = ""
                                        while not menubaru.strip():
                                            menubaru = input("Masukan nama menu minuman baru : ")
                                            if not menubaru.strip():
                                                os.system("cls")
                                                print("="*width)
                                                print("Menu minuman tidak boleh kosong!")
                                                print("="*width)
                                                
                                            else: 
                                                menubaru = menubaru.title()
                                                if menubaru in daftarmenu["menuminuman"]:
                                                    os.system("cls")
                                                    print("="*width)
                                                    print("Menu minuman sudah ada!")
                                                    print("="*width)
                                                    menubaru = ""
                                                    
                                                else:
                                                    daftarmenu["menuminuman"].append(menubaru)
                                                    os.system("cls")
                                                    print("="*width)
                                                    print("Berhasil tambah menu!".center(width))
                                                    print("="*width)
                                                    sleep(2)
                                                    os.system("cls")

                                    elif pilihan == "3":
                                        print("="*width)
                                        print("Masukan menu snack baru".center(width))
                                        print("="*width)

                                        menubaru = ""
                                        while not menubaru.strip():
                                            menubaru = input("Masukan nama menu snack baru : ")
                                            if not menubaru.strip():
                                                os.system("cls")
                                                print("="*width)
                                                print("Menu snack tidak boleh kosong!")
                                                print("="*width)
                                                
                                            else: 
                                                menubaru = menubaru.title()
                                                if menubaru in daftarmenu["menusnack"]:
                                                    os.system("cls")
                                                    print("="*width)
                                                    print("Menu snack sudah ada!")
                                                    print("="*width)
                                                    menubaru = ""
                                                    
                                                else:
                                                    daftarmenu["menusnack"].append(menubaru)
                                                    os.system("cls")
                                                    print("="*width)
                                                    print("Berhasil tambah menu!".center(width))
                                                    print("="*width)
                                                    sleep(2)
                                                    os.system("cls")

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

                                        for i, item in enumerate(daftarmenu["menumakanan"]):
                                            print(f"{i+1}. {item}")

                                        print("="*width)
                                        item_update = int(input("Masukkan nomor makanan yang ingin diupdate: ")) - 1
                                        os.system("cls")

                                        if 0 <= item_update < len(daftarmenu["menumakanan"]):
                                            print("="*width)
                                            print("Masukan Nama!".center(width))
                                            print("="*width)
                                            itembaru = input(f"Masukkan nama baru untuk {daftarmenu['menumakanan'][item_update]}: ")
                                            print("="*width)
                                            daftarmenu["menumakanan"][item_update] = itembaru.title()
                                            print(f"Data berhasil diperbarui menjadi: {daftarmenu['menumakanan'][item_update]}".center(width))
                                            print("="*width)
                                            sleep(2)
                                            os.system("cls")
                                        else:
                                            print("Nomor yang Anda masukkan tidak valid!")
                                            sleep(1)
                                            os.system("cls")

                                    elif pilihan == "2": 
                                        print("="*width)
                                        print("Menu minuman".center(width))
                                        print("="*width)

                                        for i, item in enumerate(daftarmenu["menuminuman"]):
                                            print(f"{i+1}. {item}")

                                        print("="*width)
                                        item_update = int(input("Masukkan nomor minuman yang ingin diupdate: ")) - 1
                                        os.system("cls")

                                        if 0 <= item_update < len(daftarmenu["menuminuman"]):
                                            print("="*width)
                                            print("Masukan Nama!".center(width))
                                            print("="*width)
                                            itembaru = input(f"Masukkan nama baru untuk {daftarmenu['menuminuman'][item_update]}: ")
                                            daftarmenu["menuminuman"][item_update] = itembaru.title()
                                            print("="*width)
                                            print(f"Data berhasil diperbarui menjadi: {daftarmenu['menuminuman'][item_update]}".center(width))
                                            print("="*width)
                                            sleep(2)
                                            os.system("cls")
                                        else:
                                            print("Nomor yang Anda masukkan tidak valid!")
                                            sleep(1)
                                            os.system("cls")

                                    elif pilihan == "3":  
                                        print("="*width)
                                        print("Menu snack".center(width))
                                        print("="*width)

                                        for i, item in enumerate(daftarmenu["menusnack"]):
                                            print(f"{i+1}. {item}")

                                        print("="*width)
                                        item_update = int(input("Masukkan nomor snack yang ingin diupdate: ")) - 1
                                        os.system("cls")

                                        if 0 <= item_update < len(daftarmenu["menusnack"]):
                                            print("="*width)
                                            print("Masukan Nama!".center(width))
                                            print("="*width)
                                            itembaru = input(f"Masukkan nama baru untuk {daftarmenu['menusnack'][item_update]}: ")
                                            daftarmenu["menusnack"][item_update] = itembaru.title()
                                            print("="*width)
                                            print(f"Data berhasil diperbarui menjadi: {daftarmenu['menusnack'][item_update]}".center(width))
                                            print("="*width)
                                            sleep(2)
                                            os.system("cls")
                                        else:
                                            print("Nomor yang Anda masukkan tidak valid!")
                                            sleep(1)
                                            os.system("cls")

                                    elif pilihan == "4":
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

                                    for i, item in enumerate(daftarmenu["menumakanan"]):
                                        print(f"{i+1}. {item}")

                                    print("="*width)
                                    item_hapus = int(input("Masukkan nomor makanan yang ingin dihapus: ")) - 1
                                    os.system("cls")

                                    if 0 <= item_hapus < len(daftarmenu["menumakanan"]):
                                        print("="*width)
                                        print(f"Menu {daftarmenu['menumakanan'][item_hapus]} telah dihapus!".center(width))
                                        print("="*width)
                                        daftarmenu["menumakanan"].pop(item_hapus)
                                        sleep(2)
                                        os.system("cls")
                                    else:
                                        print("Nomor yang Anda masukkan tidak valid!")
                                        sleep(1)
                                        os.system("cls")

                                elif pilihan == "2":
                                    print("="*width)
                                    print("Menu minuman".center(width))
                                    print("="*width)

                                    for i, item in enumerate(daftarmenu["menuminuman"]):
                                        print(f"{i+1}. {item}")

                                    print("="*width)
                                    item_hapus = int(input("Masukkan nomor minuman yang ingin dihapus: ")) - 1
                                    os.system("cls")

                                    if 0 <= item_hapus < len(daftarmenu["menuminuman"]):
                                        print("="*width)
                                        print(f"Menu {daftarmenu['menuminuman'][item_hapus]} telah dihapus!".center(width))
                                        print("="*width)
                                        daftarmenu["menuminuman"].pop(item_hapus)
                                        sleep(2)
                                        os.system("cls")
                                    else:
                                        print("Nomor yang Anda masukkan tidak valid!")
                                        sleep(1)
                                        os.system("cls")

                                elif pilihan == "3":
                                    print("="*width)
                                    print("Menu snack".center(width))
                                    print("="*width)

                                    for i, item in enumerate(daftarmenu["menusnack"]):
                                        print(f"{i+1}. {item}")

                                    print("="*width)
                                    item_hapus = int(input("Masukkan nomor snack yang ingin dihapus: ")) - 1
                                    os.system("cls")

                                    if 0 <= item_hapus < len(daftarmenu["menusnack"]):
                                        print("="*width)
                                        print(f"Menu {daftarmenu['menusnack'][item_hapus]} telah dihapus!".center(width))
                                        print("="*width)
                                        daftarmenu["menusnack"].pop(item_hapus)
                                        sleep(2)
                                        os.system("cls")
                                    else:
                                        print("Nomor yang Anda masukkan tidak valid!")
                                        sleep(1)
                                        os.system("cls")

                                elif pilihan == "4":
                                    cobapilihan = "n"
                                    balikmenu = "y"

                            elif menu == "5":
                                balikmenu = "n"
                                loginuser = "n"
                                print("="*width)
                                print("Anda berhasil keluar!".center(width))
                                print("="*width)

                                sleep(2)
                                break

                    elif akun["user"] == "user":
                        
                        os.system("cls")
                        print("="*width)
                        print("MENU".center(width))
                        print("="*width)
                        
                        print("Menu makanan".center(width))
                        print("="*width)
                        for i, item in enumerate(daftarmenu["menumakanan"]):
                            print(f"{i+1}. {item}")
                            
                        print("="*width)
                        print("Menu minuman".center(width))
                        print("="*width)
                        
                        for i, item in enumerate(daftarmenu["menuminuman"]):
                            print(f"{i+1}. {item}")
                            
                        print("="*width)
                        print("Menu snack".center(width))
                        print("="*width)    
                        
                        for i, item in enumerate(daftarmenu["menusnack"]):
                            print(f"{i+1}. {item}")
                        
                        print("="*width)
                        input("tekan Enter untuk keluar!")
                        print("="*width)
                        os.system("cls")
                        
                    loginuser = "n"
                    break

            else:
                os.system("cls")
                kesempatan -= 1
                print("="*width)
                print("Username atau Password yang anda masukan salah!".center(width))
                print(f"kesempatan anda tersisa {kesempatan}".center(width))
                print("="*width)

        if kesempatan == 0:
            print("="*width)
            print("Anda telah mencapai batas kesempatan!".center(width))
            print("="*width)

            sleep(2)

            os.system("cls")
            login = "n"
            break
            

    elif kebutuhan == "2":
        os.system("cls")
        
        while True:
            print("="*width)
            print("Registrasi".center(width))
            print("="*width)
            
            username = input("Masukan username : ").strip()
            password = input("Masukan password : ").strip()
            
            if not username or not password:
                os.system("cls")
                print("="*width)
                print("Username dan password tidak boleh kosong!".center(width))
                print("="*width)
                sleep(2)
                os.system("cls")
                
            elif username in [akun["username"] for akun in user]:
                os.system("cls")
                print("="*width)
                print("Username sudah terdaftar!".center(width))
                print("="*width)
                sleep(2)
                os.system("cls")
                
            else:
                user.append({"username" : username , "password" : password, "user" : "user"})
                print("="*width)
                print("Registrasi berhasil!")
                print("="*width)
                sleep(2)
                
                os.system("cls")
                break
    
    elif kebutuhan == "3":
        login = "n"
        loginuser = "n"
        kesempatan = 0
        os.system("cls")
        print("="*width)
        print("Anda berhasil keluar!".center(width))
        print("="*width)
        sleep(2)
        os.system("cls")
        break