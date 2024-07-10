import hashlib
def calculate_sha256(file_path):
    # Initialize the SHA-256 hash object
    sha256 = hashlib.sha256()    
    try:
        # Open the file in binary mode for reading
        with open(file_path , "rb") as f:
            # Read the file in chunks to handle large files efficiently
            chunk = f.read(4096)  # 4KB chunk size
            while chunk:
                sha256.update(chunk)  # Update hash with the read chunk
                chunk = f.read(4096)  # Read next chunk
    
        # Calculate the hexadecimal digest of the hash
        sha256_digest = sha256.hexdigest()
        return sha256_digest
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except IsADirectoryError:
        print(f"Error: '{file_path}' is a directory, not a file.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def main():
    # Prompt user to enter the file path
    file_path = input("Enter the path of the file: ").strip()
    
    # Calculate SHA-256 hash of the file
    hash_value = calculate_sha256(file_path)
    
    if hash_value:
        print(f"SHA-256 Hash of the file '{file_path}': {hash_value}")

if __name__ == "__main__":
    main()
