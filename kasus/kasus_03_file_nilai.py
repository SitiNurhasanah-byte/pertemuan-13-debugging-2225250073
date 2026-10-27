try:
    with open("nilai.txt", "r", encoding="utf-8") as file:
        for baris in file:
            print(baris.strip())
except FileNotFoundError:
    print("File tidak ditemukan.")