import os

def rename_files(directory, prefix):
    for filename in os.listdir(directory):
        if filename.startswith(prefix):
            continue  # Skip files that already have the desired prefix
        old_path = os.path.join(directory, filename)
        new_filename = f"{prefix}_{filename}"
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    directory_path = "/path/to/your/directory"  # Replace with the actual directory path
    new_prefix = "new_prefix"  # Replace with the desired prefix
    rename_files(directory_path, new_prefix)
