def create_files(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    chunk_size = 1000
    num_chunks = len(lines) // chunk_size + 1

    for i in range(num_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, len(lines))
        chunk = lines[start:end]

        output_file = f'file{i + 1}.txt'

        with open(output_file, 'w') as f_out:
            f_out.writelines(chunk)

if __name__ == "__main__":
    input_file = "All-DataQr1Jt.txt"
    create_files(input_file)
