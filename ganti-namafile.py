import os

folder_path = "src-file-1000"

# Mendapatkan daftar file dalam folder
file_list = os.listdir(folder_path)

# Memfilter file dengan kriteria "file-"
filtered_files = [file for file in file_list if file.startswith("file")]

# Mengganti nama setiap file yang memenuhi kriteria
for file_name in filtered_files:
    old_path = os.path.join(folder_path, file_name)
    
    # Menghasilkan nama baru tanpa "file-"
    new_name = file_name.replace("file", "")
    new_path = os.path.join(folder_path, new_name)
    
    # Mengganti nama file
    os.rename(old_path, new_path)
    print(f"File {file_name} telah diubah namanya menjadi {new_name}.")

print("Pengubahan nama selesai.")
