import os
import zipfile

def create_folders_if_not_exist():
    folders_to_check = ['json_raw', 'json_raw_zip']
    for folder in folders_to_check:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Folder '{folder}' created.")

def extract_zip_files():
    zip_folder = 'json_raw_zip'
    extract_folder = 'json_raw'

    if not os.path.exists(zip_folder):
        print(f"Folder '{zip_folder}' does not exist.")
        return

    for filename in os.listdir(zip_folder):
        if filename.endswith('.zip'):
            zip_file_path = os.path.join(zip_folder, filename)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
            print(f"Extracted '{filename}' to '{extract_folder}'.")

if __name__ == "__main__":
    create_folders_if_not_exist()
    extract_zip_files()
