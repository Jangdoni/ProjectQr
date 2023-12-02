import os

def merge_files(source_folder, destination_folder, files_per_merge=5):
    # Membuat folder destinasi jika belum ada
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Mendapatkan daftar file di folder sumber dan mengurutkannya berdasarkan nilai numerik
    source_files = sorted(os.listdir(source_folder), key=lambda x: int(x.split('.')[0]))

    # Iterasi melalui file-file di folder sumber
    for i in range(0, len(source_files), files_per_merge):
        # Mengambil 5 file dengan urutan yang diinginkan
        files_to_merge = source_files[i:i+files_per_merge]

        # Membaca isi dari 5 file tersebut
        file_contents = []
        for file_name in files_to_merge:
            file_path = os.path.join(source_folder, file_name)
            with open(file_path, 'r') as file:
                file_contents.append(file.read().splitlines())

        # Membuat nama file baru
        merged_file_name = f"merged_file_{i//files_per_merge + 1}.txt"
        merged_file_path = os.path.join(destination_folder, merged_file_name)

        # Menyimpan hasil gabungan ke dalam file baru dengan format 5 kolom
        with open(merged_file_path, 'w') as merged_file:
            for line in zip(*file_contents):
                merged_line = '\t'.join(line)
                merged_file.write(merged_line + '\n')

if __name__ == "__main__":
    source_folder = "End-PO"
    destination_folder = "dest-file"
    merge_files(source_folder, destination_folder)
