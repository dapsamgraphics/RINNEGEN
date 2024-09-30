import random
import string
from rich.console import Console
from rich.text import Text
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

console = Console()

# Fungsi untuk menampilkan ASCII Art dengan warna
def display_ascii_art():
    # ASCII art dengan karakter @ yang akan diwarnai putih
    ascii_art = """                    
                    ......-*%@@@@@@@@@@@@%*-......                    
               ......*@@@@%%%%%%%%%@@%%%%%%%@@@@*......               
               ..=@@@%%%%%%%%%%%#@@@%%%%%%%%%%%%%@@@=..               
            ..-@@%%%%%%%%%##%%%@@@@@@@@%%%%%%%%%%%%%%@@-..            
          ..*@@%%%%%%%%%@%%##%%%%@@@@%%%#%%%%@%#%%%%%%%@@*..          
       ...+@%%%%%%%%@%%%#####%%%%%##%%%%#####%%%%@%%%%%%%%@*..        
       .-@@%%%%%%%%%#%###%%%%%%%%%%%%%%%%%%%%#####%%%%%%%%%@@=.       
     ..#@%%%%%%%%%###%%%%%%%%%%%%%%%%%%%%%%%%%%%####%%%%%%%%%@#..     
  ...:@@%%%%%%%%###%%%%%%%%%@%%%%%%%%%%%%@%%%%%%%%%####%%%%%%%@@-..   
  ..-@%%%%%%%%###%%%%%%%@%%%%%%#########%%%%%@%%%%%%%###%%%%%%%%@=..  
  .:@%%%%%%%####%%%%%%%%%#######%%%%@%%#####%%%%%%%%%%###%%%%%%%%@-.  
..:@%%%%%%%###%%%%%%%%%%###%%%%%%@@@%%%%%%%###%#%%%%%%%%###%%%%%%%@-..
..#@%%%%%%###%@%%@@%%%##%%%%%%%%%@@@@%%%%%%%%%##%%%@@@@@%%#%%%%%%%@%..
.+@%%%%%@%##%%%@@@@@%#%%%%%%%%%%#@@@@%%%%%%%%%%##%@@@@@%%%###@%%%%%@+.
.@@%%%#@####%%%%@@@@%%%%%%%%%###########%%%%%%%%%%@@@@%%%%%#%#@%%%%%@:
-@%%%%%%###%%%%%%%##%%#%%@%###%%%%%%%%%%####%%%%%%##%%@%%%%##%%%%%%%@=
*@%%%%%%##%%%%%%%###%%%@@@@%%%%%%%%%%%%%%%%@@@@%%%###%%%%%%%##%%%%%%@*
%@%%%%@###%%%%%%####%%%%%%#%%%%%%@@@@%%%%%%##%%%%%%##%%@%%%%###@%%%%@%
@%%%%%@###%%%%@%%##%%%%%###%%%%%@@@@@@%%%%%##%%%%%%##%%@%%%%##%@%%%%%@ 
@%%%%%@###%%%%@%%##%%%%%%##%%%%%@@@@@@%%%%%##%%%%%%##%%@%%%%##%@%%%%%@ 
%@%%%%@%##%%%%%%%##%%%%%%##%%%%%%@@@@%%%%%%#%%%%%%###%%%%%%%###@%%%%@%
*@%%%%%%##%%%%%%%###%%%@@@@%%%%%%%%%%%%%%%%@@@@%%%###%%%%%%%##%%%%%%@*
-@%%%%%%%##%%%%@%%##%@%@@@@%##%%%%%%%%%%##%@@@@@%###%%@%%%%##%%#%%%%@=
:@@%%%%@%###%%%%@%%###%%@%%%%%%%#########%%%%%#@%##%%@%%%%%##%@%%%%%@:
.+@%%%%%@##%%%%%%@%%%##%%%%%%@%%###%#%%%%%%%%%%%#%#%@%%%%####@%%%%%@+.
..#@%%%%%@@%%%%%%%@%%%###%%%%%%%%%@@%%%%%%%%%####%%@%%%%%#%%%%%%%%@%..
..:@%%%%@@@@@##%%%%%%%%%##%%%%%%%%%%%%%%%%%%##%%%%%%%%%%%@@@@@%%%%@-..
  .-@%@@@@@@%%#%%%%%%%%%%%####%%%%%%%%%#######%%%%%%%%%##%@@@@@%%@-.
  ..-@%%%%%%@%###%%%%%%%@%%%%%##%%@@%###%%%%%@%%%%%%%###%@%%%%@%@=..
  ...-@@%%%%%%%%%##%%%%%%%%%@%%%%@@@@%%%%@%%%%%%%%%####%%%%%%%%@-..
     ..#@%%%%%%%%%###%%%%%%%%%%%%@@@@%%%%%%%%%%%%####%@%%%%%%@#..
       .-@@%%%%%%%%%%####%%%%%%%%%%@%%%%%%%%%#####%%%%%%%%%@@=.
        ..*@%%%%%%%%@%%%######%%#%##%%%######%%%%@%%%%%%%%@*...
          ..*@@%%%%%%%#%@%%%%%##########%%%%%@%##%%%%%%%@*..
            ..-@@%%%%%%%%%%%%%%@@@@@@@@%%%%%%%%%%%%%%@@-..
               ..=@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@=..
                .....*@@@%%%%%%%%%%%%%%%%%%%%@@@*......
    """
    
    # Mencetak ASCII art dengan karakter @ berwarna putih
    for char in ascii_art:
        if char == '@':
            print(Fore.LIGHTBLACK_EX + char, end='')  # Karakter @ berwarna putih
        else:
            print(Fore.MAGENTA + char, end='')      # Karakter lainnya berwarna merah
    print()  # Untuk pindah ke baris baru setelah selesai

# Fungsi untuk menampilkan judul dan deskripsi menggunakan rich
def display_title():
    title = Text(
        """\
.%%%%%...%%%%%%..%%..%%..%%..%%..%%%%%%...%%%%...%%%%%%..%%..%%.
.%%..%%....%%....%%%.%%..%%%.%%..%%......%%......%%......%%%.%%.
.%%%%%.....%%....%%.%%%..%%.%%%..%%%%....%%.%%%..%%%%....%%.%%%.
.%%..%%....%%....%%..%%..%%..%%..%%......%%..%%..%%......%%..%%.
.%%..%%..%%%%%%..%%..%%..%%..%%..%%%%%%...%%%%...%%%%%%..%%..%%.
................................................................
""",
        style="bold white"
    )
    subtitle = Text("INI BUKAN SCRIPT AUTO CREATE TELE BG KERIPTOOHH, TAPI CINI CUMAN GENERATE USERNAME TELE & EMAIL. JADI KALO ENTE BUAT AKUN TELEGRAM YA..TETEP MANUAL, INI BIAR AGA MEMPERMUDAH AJA BIAR TINGGAL COPY PASTE", style="bold yellow")
    description = Text("kalo pas buat gmail kena req otp yaudah bg sabar aja:v", style="white")
    
    # Menampilkan title dan subtitle tanpa border
    console.print(title)
    console.print(subtitle)
    console.print("-" * 50, style="white")
    console.print(description)
    console.print("-" * 50, style="white")

# Fungsi untuk menghasilkan username secara acak dengan huruf besar dan kecil
def generate_random_username(base_username):
    # Menambahkan variasi huruf besar dan kecil
    username_variation = ''.join(random.choice([char.upper(), char.lower()]) for char in base_username)
    
    # Menambahkan beberapa karakter atau angka secara acak
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits + "_", k=random.randint(3, 10)))
    
    return f"@{username_variation}{random_suffix}"

# Fungsi untuk menghasilkan email secara acak dengan variasi huruf besar-kecil dan angka
def generate_random_email(base_email, count):
    base_name, domain = base_email.split("@")
    
    # Menambahkan variasi huruf besar dan kecil
    email_variation = ''.join(random.choice([char.upper(), char.lower()]) for char in base_name)
    
    # Menambahkan angka atau karakter acak di akhir email
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits + "_", k=random.randint(1, 5)))
    
    return f"{email_variation}{count}{random_suffix}@{domain}"

# Fungsi untuk validasi input
def validate_input(prompt, error_message="Input nya yang bener bang keripetohhh :)"):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "":
            console.print(f"[bold red]{error_message}[/bold red]")  # Notifikasi error berwarna merah
        else:
            return user_input

# Fungsi untuk validasi email
def validate_email(prompt, error_message="Input Email nya harus ada '@' bang keripetohhh"):
    while True:
        email = input(prompt)
        if "@" not in email or email.count('@') != 1:
            console.print(f"[bold red]{error_message}[/bold red]")  # Notifikasi error berwarna merah
        else:
            return email

# Fungsi untuk validasi jumlah input
def validate_int_input(prompt, error_message="Input jumlah nya yang bener bang keripetohhh :)"):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            console.print(f"[bold red]{error_message}[/bold red]")  # Notifikasi error berwarna merah

# Fungsi utama
def main():
    display_ascii_art()  # Menampilkan ASCII art tanpa border
    display_title()  # Menampilkan judul dan deskripsi setelah ASCII art

    base_username = validate_input("Silahkan masukkan username yang ingin kamu buat. " + Fore.WHITE + "contoh: madarauchiha" + Style.RESET_ALL + ": ")
    base_email = validate_email("Silahkan masukkan email yang ingin kamu buat. " + Fore.WHITE + "contoh: madarauchiha@gmail.com/madarauchiha@uchiha.com" + Style.RESET_ALL + ": ")
    gmail_password = validate_input("Silahkan masukkan password gmail yang ingin kamu buat. " + Fore.WHITE + "contoh: madarauchihalo" + Style.RESET_ALL + ": ")
    telegram_password = validate_input("Silahkan masukkan password telegram yang ingin kamu buat. " + Fore.WHITE + "contoh: madarauchihalo" + Style.RESET_ALL + ": ")
    file_name = validate_input("Silahkan kasih nama untuk file.txt nya. " + Fore.WHITE + "contoh: madarauchiha.txt" + Style.RESET_ALL + ": ")

    jumlah_akun = validate_int_input("Masukkan jumlah akun yang ingin dibuat: ")

    # Menghasilkan dan menyimpan akun
    with open(file_name, "w") as f:
        for i in range(jumlah_akun):
            username = generate_random_username(base_username)
            email = generate_random_email(base_email, i)
            f.write(f"=======================================\n")
            f.write(f"[AKUN {i}]\n")
            f.write(f"No HP:\n")
            f.write(f"Username: {username}\n")
            f.write(f"Gmail: {email}\n")
            f.write(f"Password Gmail: {gmail_password}\n")
            f.write(f"Password Telegram: {telegram_password}\n")
            f.write(f"=======================================\n\n")
    
    console.print(f"[bold green]Akun berhasil dibuat dan disimpan di {file_name}[/bold green]")

if __name__ == "__main__":
    main()
