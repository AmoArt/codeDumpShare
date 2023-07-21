import os
import json
import re

def is_valid_message(message_text):
    return bool(re.search(r':\w+:', message_text))

def process_json_files(input_folder):
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)

                with open(file_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)

                # Process the JSON data to merge messages with the same 'username'
                processed_data = []
                current_msg = None
                for msg in json_data:
                    if 'msg' in msg:
                        message_text = msg['msg'].strip()  # Remove leading/trailing whitespace
                        if message_text and is_valid_message(message_text):
                            processed_data.append(msg)

                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(processed_data, f, indent=2, ensure_ascii=False)

                print(f"Processed '{file_path}'")

if __name__ == '__main__':
    input_folder = 'processed_json_v02'  # Replace with the path to your input folder
    process_json_files(input_folder)
