# Mengimpor modul yang dibutuhkan


import os
import random
#Menginstall CSV
os.system("pip install python-csv")
#Menginstall time
import csv
#Menginstall time
os.system("pip install python-time")
import time
#Menginstall pwinput
os.system("pip install pwinput")
import pwinput
#Menginstall library prettytable
os.system("pip install PrettyTable")
from prettytable import PrettyTable, from_csv

#akun admin
adminakun = ("admin", "admin")

# Fungsi untuk membersihkan layar konsol
def clear():
    os.system("cls")

# Fungsi untuk memberi jeda
def delay(seconds):
    time.sleep(seconds)

# Fungsi untuk menunggu pengguna menekan ENTER
def enter():
    input("Tekan ENTER Untuk Lanjut.....")

# Fungsi untuk menampilkan logo
def logo1():
    print("""

    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
          """)


# Fungsi untuk menampilkan logo
def logo2():
    print("""

    ████████╗░█████╗░
    ╚══██╔══╝██╔══██╗
    ░░░██║░░░██║░░██║
    ░░░██║░░░██║░░██║
    ░░░██║░░░╚█████╔╝
    ░░░╚═╝░░░░╚════╝░
          """)


# Fungsi untuk menampilkan logo
def logo():
    print("""
    ░██████╗██╗██╗░░██╗██╗██╗░░░░░░█████╗░████████╗
    ██╔════╝██║██║░██╔╝██║██║░░░░░██╔══██╗╚══██╔══╝
    ╚█████╗░██║█████═╝░██║██║░░░░░███████║░░░██║░░░
    ░╚═══██╗██║██╔═██╗░██║██║░░░░░██╔══██║░░░██║░░░
    ██████╔╝██║██║░╚██╗██║███████╗██║░░██║░░░██║░░░
    ╚═════╝░╚═╝╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
    """)

# Fungsi untuk memastikan file CSV ada dan membuat jika belum ada
def ensure_csv_file(file_name, fieldnames):
    # Memeriksa apakah file CSV sudah ada
    if not os.path.isfile(file_name):
        # Jika belum ada, buat file baru
        with open(file_name, 'w', newline='') as csvfile:
            # Membuat objek writer untuk menulis header menggunakan fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Menulis header ke file CSV
            writer.writeheader()

# Menjalankan kode untuk memastikan file CSV ada

# Mendapatkan direktori skrip saat ini
script_directory = os.path.dirname(os.path.abspath(__file__))

# Menggabungkan direktori skrip dengan nama folder "Database"
DBPath = os.path.join(script_directory, "Database")

# Menggabungkan direktori "Database" dengan nama file "akun.csv"
dataakun = os.path.join(DBPath, "akun.csv")

# Menggabungkan direktori "Database" dengan nama file "alamat.csv"
databarang = os.path.join(DBPath, "alamat.csv")

# Membuat folder "Database" jika belum ada
if not os.path.exists(DBPath):
    os.makedirs(DBPath)

# Memastikan file "akun.csv" ada dengan header fieldnames yang sesuai
ensure_csv_file(dataakun, ['Username', 'Password', 'Role', 'Resi Dan Barang'])

# Memastikan file "alamat.csv" ada dengan header fieldnames yang sesuai
ensure_csv_file(databarang, ['Resi', 'Barang', 'Alamat Pengirim', 'Alamat Penerima', 'Status Konfirmasi', 'Lokasi Terkini'])


# Fungsi untuk membaca data akun CSV
def load_users(file_name):
    # Mendapatkan path lengkap ke file CSV
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    users = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
        # Membaca data dari setiap baris CSV dan memasukkannya ke dalam struktur data users
            user_data = {
                'Password': row['Password'],
                'Role': row['Role'],
            }
            if 'Resi Dan Barang' in row and row['Resi Dan Barang']:
                user_data['Resi Dan Barang'] = {item.split(': ')[0]: str(item.split(': ')[1]) for item in row['Resi Dan Barang'].split(', ')}
            else:
                user_data['Resi Dan Barang'] = {}
            users[row['Username']] = user_data
    return users


# Fungsi untuk menulis data akun ke file CSV
def write_users(users, file_name):
    # Mendapatkan path lengkap ke file CSV
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'w', newline='') as file:
        fieldnames = ['Username', 'Password', 'Role', 'Resi Dan Barang']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for username, data in users.items():
            resi_data = data.get('Resi Dan Barang', {})
            # Menulis data akun ke dalam file CSV
            writer.writerow({
                'Username': username,
                'Password': data['Password'],
                'Role': data['Role'],
                'Resi Dan Barang': ', '.join(f"{key}: {value}" for key, value in resi_data.items())
            })

# Fungsi untuk membaca data barang CSV
def load_pengiriman(files):
    # Mendapatkan path lengkap ke file CSV
    file_path = os.path.join(os.path.dirname(__file__), files)
    pengiriman = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Membaca data dari setiap baris CSV dan memasukkannya ke dalam struktur data pengiriman
            pengiriman[row['Resi']] = {
                'Barang': row['Barang'],
                'Alamat Pengirim': row['Alamat Pengirim'],
                'Alamat Penerima': row['Alamat Penerima'],
                'Status Konfirmasi': row['Status Konfirmasi'],
                'Lokasi Terkini': row['Lokasi Terkini']
            }
    return pengiriman

# Fungsi untuk menulis data barang ke file CSV
def write_pengiriman(pengiriman, files):
    # Mendapatkan path lengkap ke file CSV
    file_path = os.path.join(os.path.dirname(__file__), files)
    with open(file_path, 'w', newline='') as file:
        fieldnames = ['Resi', 'Barang', 'Alamat Pengirim', 'Alamat Penerima', 'Status Konfirmasi', 'Lokasi Terkini']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for resi, dataa in pengiriman.items():
            # Menulis data barang ke dalam file CSV
            writer.writerow({
                'Resi': resi,
                'Barang': dataa['Barang'],
                'Alamat Pengirim': dataa['Alamat Pengirim'],
                'Alamat Penerima': dataa['Alamat Penerima'],
                'Status Konfirmasi': dataa['Status Konfirmasi'],
                'Lokasi Terkini': dataa['Lokasi Terkini']
            })
# Fungsi untuk menampilkan menu pengguna
def user(username):
    while True:
        userTable = PrettyTable(["HALO SELAMAT DATANG DI SIKILAT"])
        userTable.add_row(["[1] Kirim Barang"])
        userTable.add_row(["[2] Cek Resi Barang"])
        userTable.add_row(["[3] Lokasi Terkini Barang"])
        userTable.add_row(["[4] Membatalkan pesanan"])
        userTable.add_row(["[5] Mengubah Alamat"])
        userTable.add_row(["[6] Logout"])
        userTable.align["HALO SELAMAT DATANG DI SIKILAT"] = "l"
        print(userTable)
        choice = input("Pilih Menu: ")
        # Definisi path file CSV untuk data pengguna
        file_name = '.\Database\\akun.csv'

        # Memanggil fungsi load_users untuk memuat data dari file CSV ke dalam variabel users
        users = load_users(file_name)

        # Definisi path file CSV untuk data pengiriman
        files = '.\Database\\alamat.csv'

        # Memanggil fungsi load_pengiriman untuk memuat data dari file CSV ke dalam variabel pengiriman
        pengiriman = load_pengiriman(files)

        clear()
        if choice == "1":
            barang = input("Barang Apa Yang Ingin Di Kirim: ")
            if not barang:
                print("Mohon masukkan nama barang yang ingin Anda kirim.")
                continue
            kode_resi = random.randint(9999, 999999)#Memberi angka random sebagai kode resi
            alamat_pengirim = input("Masukkan Alamat Lengkap Pengantar: ")
            alamat_penerima = input("Masukkan Alamat Lengkap Penerima: ")
            if username not in users:
                users[username] = {'Password': users[username]['Password'], 'Role': users[username]['Role'], 'Resi Dan Barang': {}}
            if 'Resi Dan Barang' not in users[username]:
                users[username]['Resi Dan Barang'] = {}
            pengiriman[kode_resi] = {'Barang': barang, 'Alamat Pengirim': alamat_pengirim, 'Alamat Penerima': alamat_penerima, 'Status Konfirmasi': 'Sedang Di Proses', 'Lokasi Terkini': '-'}
            users[username]['Resi Dan Barang'][kode_resi] = barang
            write_users(users, file_name)
            write_pengiriman(pengiriman, files)

            print(f"Barang {barang} telah ditambahkan ke akun Anda.")
            print(f"Kode Pengiriman Anda untuk barang {barang}: {kode_resi}")
        elif choice == "2":
                if not users[username]["Resi Dan Barang"]:
                    print("Anda Belum Mengirim Apapun")
                else:
                    tableresi = PrettyTable(["List Resi Anda", "List Barang Anda"])
                    for resi, barang in users[username]['Resi Dan Barang'].items():
                        tableresi.add_row([resi, barang])
                    print(tableresi)
                    enter()
                    clear()
        elif choice == "3":
            masukresi = input("Masukkan Resi Yang Ingin Di Lacak: ")
            if masukresi in pengiriman:
                table = PrettyTable(["Info", "Data"])
                for key, value in pengiriman[masukresi].items():
                    table.add_row([key, value])
                print(table)
                enter()
                clear()
            else:
                print(f"Resi {masukresi} Tidak Di Temukan")

        elif choice == "4":
            hapus_resi = input("Masukkan kode resi yang ingin dihapus: ")
            if hapus_resi in users[username]['Resi Dan Barang']:
                if pengiriman[hapus_resi]['Status Konfirmasi'] == "Sedang Di Proses":
                    deleted_barang = users[username]['Resi Dan Barang'][hapus_resi]
                    del users[username]['Resi Dan Barang'][hapus_resi]
                    if hapus_resi in pengiriman:
                        del pengiriman[hapus_resi]
                    write_users(users, file_name)
                    write_pengiriman(pengiriman, files)
                    print(f"Barang dengan kode resi {hapus_resi} ({deleted_barang}) telah di batalkan.")
                else:
                    print("Pesenan Sudah Di Konfirmaasi Tidak Dapat Di Batalkan")
            else:
                print(f"Kode resi {hapus_resi} tidak ditemukan.")
        elif choice == "5":
            input_resi = input("Masukkan Resi Yang Ingin Di ubah: ")
            if input_resi in pengiriman:
                if pengiriman[input_resi]['Status Konfirmasi'] == "Sedang Di Proses":
                    while True:
                        MENUUBAHTable = PrettyTable(["SILAHKAN PILIH"])
                        MENUUBAHTable.add_row(["[1] Mengubah Alamat Pengirim"])
                        MENUUBAHTable.add_row(["[2] Mengubah Alamat Penerima"])
                        MENUUBAHTable.add_row(["[3] Mengubah Keduanya"])
                        MENUUBAHTable.add_row(["[4] Kembali Kemenu Awal"])
                        MENUUBAHTable.align["SILAHKAN PILIH"] = "l"
                        print(MENUUBAHTable)
                        choic  = input("Masukkan PIlihan Anda: ")
                        clear()
                        if choic == "1":
                            ubah_alamat = input("Masukkan Alamat Baru: ")
                            pengiriman[input_resi]['Alamat Pengirim'] = ubah_alamat
                            print("Berhasil Di Ubah")
                            write_pengiriman(pengiriman, files)
                        elif choic == "2":
                            ubah_alamat = input("Masukkan Alamat Baru: ")
                            pengiriman[input_resi]['Alamat Penerima'] = ubah_alamat
                            print("Berhasil Di Ubah")
                            write_pengiriman(pengiriman, files)
                        elif choic == "3":
                            alamat_barup = input("Masukkan Alamat Baru Pengirim: ")
                            alamat_barut = input("Masukkan Alamat Baru Penerima: ")
                            pengiriman[input_resi]['Alamat Pengirim'] = alamat_barup
                            pengiriman[input_resi]['Alamat Penerima'] = alamat_barut
                            print("Berhasil Di Ubah")
                            write_pengiriman(pengiriman, files)
                        elif choic == "4":
                            break
                        else:
                            print("Pilihan Tidak Valid")          
                else:
                    print("Pesenan Sudah Di Konfirmaasi Tidak Dapat Di Ubah")
            else:
                print(f"Resi {input_resi} Tidak Di Temukan")
        elif choice == "6":
            break
        else:
            print("Pilihan Tidak Valid")
# Fungsi menu untuk admin
def admin():
    while True:
        file_name = '.\Database\\akun.csv'
        users = load_users(file_name)
        files = '.\Database\\alamat.csv'
        pengiriman = load_pengiriman(files)
        adminTable = PrettyTable(["Welcome to SIKILAT Admin Menu"])
        adminTable.add_row(["[1] Cek Data Barang"])
        adminTable.add_row(["[2] Cek Data Akun"])
        adminTable.add_row(["[3] Ubah Status Konfirmasi"])
        adminTable.add_row(["[4] Perbarui Lokasi Terkini Barang"])
        adminTable.add_row(["[5] Logout"])
        adminTable.align["Welcome to SIKILAT Admin Menu"] = "l"
        print(adminTable)
        choice = input("Pilih Menu: ")
        clear()
        if choice == "1":
            if not pengiriman:
                print("Tidak ada data pengiriman yang tersedia.")
                continue
            else:
                file_path = os.path.join(os.path.dirname(__file__), files)
                with open(file_path) as data:
                    databarang = from_csv(data)
                    print(databarang)
                    enter()
                    clear()
        elif choice == "2":
            if not users:
                print("Tidak ada data akun user yang tersedia.")
                continue
            else:
                file_path = os.path.join(os.path.dirname(__file__), file_name)
                with open(file_path) as data:
                    dataakun = from_csv(data)
                    print(dataakun)
                    enter()
                    clear()
        elif choice == "3":
            resi = input("Masukkan Resi Yang Ingin Di Ubah: ")
            if resi in pengiriman:
                while True:
                    statustable = PrettyTable(["Silahkan Pilih"])
                    statustable.add_row(["[1] Konfirmasi"])
                    statustable.add_row(["[2] Sedang Di Proses"])
                    statustable.add_row(["[3] Ke menu awal "])
                    statustable.align["Silahkan Pilih"] = "l"
                    print(statustable)  
                    status = input("Masukkan Pilhan Anda: ")
                    if status =="1":
                        pengiriman[resi]['Status Konfirmasi'] = 'Konfirmasi'
                        clear()
                        write_pengiriman(pengiriman, files)
                        print("Satatus Telah Di Perbarui")
                        break

                    elif status == "2":
                        pengiriman[resi]['Status Konfirmasi'] = 'Sedang Di Proses'
                        write_pengiriman(pengiriman, files)
                        clear()
                        print("Satatus Telah Di Perbarui")
                        break
                    elif status == "3":
                        break
                    else:
                        print("Pilihan Tidak Valid")
            else:
                print(f"Resi {resi} Tidak Di Temukan")
        elif choice == "4":
            resi = input("Masukkan Resi Yang Ingin Di Perbarui: ")
            if resi in pengiriman:
                ubah = input("Masukkan Lokasi Barang Sekarang: ")
                pengiriman[resi]['Lokasi Terkini'] = ubah
                write_pengiriman(pengiriman, files)
                print("Berhasil Memperbarui Lokasi Terkini")
            else:
                print(f"Resi {resi} Tidak Di Temukan")

        elif choice == "5":
            break
        else:
            print("Pilihan Tidak Valid")

# Menampilkan logo dan membuat folder dan file CSV yang diperlukan
logo1()
delay(1)
clear()
logo2()
delay(1)
clear()
logo()
delay(1)
clear()
file_name = os.path.join('Database', 'akun.csv')
users = load_users(file_name)
files = os.path.join('Database', 'alamat.csv')
pengiriman = load_pengiriman(files)

# Menu utama untuk login/registrasi
def menulogin():
    while True:
        table = PrettyTable(["WELCOME TO SIKILAT"])
        table.add_row(["[1] LOGIN"])
        table.add_row(["[2] REGISTRASI"])
        table.add_row(["[3] EXIT"])
        table.align["WELCOME TO SIKILAT"] = "l"

        print(table)
        choices = input("Masukkan pilihan anda: ")
        clear()
        if choices == "1":
            username = input("Masukkan username: ")
            password = pwinput.pwinput("Masukkan password: ")
            if username in users and users[username]['Password'] == password:
                user(username)
            elif adminakun[0] == username and adminakun[1]== password:
                admin()
            else:
                print("Login gagal.")
        elif choices == "2":
            username = input("Masukkan username: ")
            if username in users:
                print("Username sudah digunakan. Coba lagi.")
            else:
                password = pwinput.pwinput("Masukkan password: ")
                if len(password) < 8:
                    print("Password tidak boleh kurang dari 8 karakter")
                else:
                    users[username] = {'Password': password, 'Role': 'user', 'Barang': {}}
                    write_users(users, file_name) 
                    print("Registrasi berhasil.")
        elif choices == "3":
            exit("Terimakasih Sudah Memakai Aplikasi Kami")
        else:
            print("Masukkan Pilihan Dengan Benar")

menulogin()
