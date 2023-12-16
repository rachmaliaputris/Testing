import mysql.connector


# Fungsi untuk membuat koneksi ke database dan tabel
def create_table():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="latihan",
    )
    cursor = connection.cursor()

    # Membuat tabel jika belum ada
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS data (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
    )

    connection.commit()
    connection.close()


# Fungsi untuk menambahkan data ke tabel
def insert_data(name, age):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="latihan",
    )
    cursor = connection.cursor()

    # Menambahkan data ke tabel
    cursor.execute("INSERT INTO data (name, age) VALUES (%s, %s)", (name, age))

    connection.commit()
    connection.close()


# Fungsi untuk membaca data dari tabel
def read_data():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="latihan",
    )
    cursor = connection.cursor()

    # Membaca data dari tabel
    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()
    for row in data:
        print(row)

    connection.close()


# Fungsi untuk memperbarui data dalam tabel
def update_data(id, name, age):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="latihan",
    )
    cursor = connection.cursor()

    # Memperbarui data dalam tabel
    cursor.execute("UPDATE data SET name=%s, age=%s WHERE id=%s", (name, age, id))

    connection.commit()
    connection.close()


# Fungsi untuk menghapus data dari tabel
def delete_data(id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="latihan",
    )
    cursor = connection.cursor()

    # Menghapus data dari tabel
    cursor.execute("DELETE FROM data WHERE id=%s", (id,))

    connection.commit()
    connection.close()


# Main program
create_table()

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Perbarui Data")
    print("4. Hapus Data")
    print("5. Keluar")

    choice = input("Pilih operasi (1/2/3/4/5): ")

    if choice == "1":
        name = input("Masukkan nama: ")
        age = int(input("Masukkan umur: "))
        insert_data(name, age)

    elif choice == "2":
        print("\nData saat ini:")
        read_data()

    elif choice == "3":
        id = int(input("Masukkan ID data yang akan diperbarui: "))
        name = input("Masukkan nama baru: ")
        age = int(input("Masukkan umur baru: "))
        update_data(id, name, age)

    elif choice == "4":
        id = int(input("Masukkan ID data yang akan dihapus: "))
        delete_data(id)

    elif choice == "5":
        print("Program berhenti.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")

#try:
 #   connection = mysql.connector.connect(**con)
  #  if conn.is_connected():
   #     print("berhasil connect")
#except mysql.connector.Error as apa_yang_error:
 #   print(f"error connectinng to mysql : {apa_yang_error}")
#finally:
 #   if "connection" in locals() and connection.is_connected():
  #      connection.close()
   #     print("connection closed")
