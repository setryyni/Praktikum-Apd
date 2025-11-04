data_user = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    }
}

def register():
    """Fungsi untuk daftar akun baru"""
    print("\n=== DAFTAR AKUN BARU ===")
    
    username = input("Username baru: ")
    
    if username == "" or username.isspace():
        return False, "Username tidak boleh kosong!"
    
    if username in data_user:
        return False, "Username sudah dipakai!"
    
    password = input("Password baru: ")
    
    if password == "" or password.isspace():
        return False, "Password tidak boleh kosong!"
    
    if len(password) < 8:
        return False, "Password minimal 8 karakter!"
    
    ada_angka = False
    for huruf in password:
        if huruf.isdigit():
            ada_angka = True
            break
    
    if ada_angka == False:
        return False, "Password harus ada angkanya!"
    
    data_user[username] = {
        "password": password,
        "role": "penyewa"
    }
    
    return True, "Daftar berhasil! Silakan login."

def login(username, password):
    """Fungsi untuk login"""
    
    if username not in data_user:
        return False, "Username tidak ditemukan!", None
    
    if data_user[username]["password"] != password:
        return False, "Password salah!", None
    
    role = data_user[username]["role"]
    
    return True, "Login berhasil!", role