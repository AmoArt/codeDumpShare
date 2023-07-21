import os
import json

def remove_username(json_data):
    return [{k: v for k, v in msg.items() if k != 'username'} for msg in json_data]

def process_json_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith('.json'):
                input_file_path = os.path.join(root, filename)
                output_file_path = os.path.join(output_folder, filename)

                with open(input_file_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)

                json_data = remove_username(json_data)

                with open(output_file_path, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, indent=2, ensure_ascii=False)

                print(f"Processed '{input_file_path}' -> '{output_file_path}'")

if __name__ == '__main__':
    input_folder = 'processed_json'  # Replace with the path to your input folder
    output_folder = 'processed_json_v02'  # Replace with the desired output folder path
    process_json_files(input_folder, output_folder)
