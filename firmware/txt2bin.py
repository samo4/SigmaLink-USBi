import hashlib

def calculate_sha1(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):  # Read the file in chunks
            sha1.update(chunk)
    return sha1.hexdigest()

def convert_txt_to_bin(input_file, output_file):
    with open(input_file, 'r') as txt_file, open(output_file, 'wb') as bin_file:
        for line in txt_file:
            line = line.strip()
            if line:
                byte_value = int(line, 16)
                bin_file.write(byte_value.to_bytes(1, byteorder='big'))

if __name__ == "__main__":
    input_path = "24aa256.txt"
    output_path = "24aa256.bin"
    convert_txt_to_bin(input_path, output_path)
    print(f"Conversion complete. Binary file saved to {output_path}")
    sha1_hash = calculate_sha1(output_path)
    print(f"SHA-1 hash of {output_path}: {sha1_hash}")