import os
import json
import re

def process_text_and_tags(message_text):
    # Remove everything that is a :tag:
    text_only = re.sub(r':\w+:', '', message_text)
    # Remove everything except :tags:
    tags_only = re.findall(r':\w+:', message_text)
    return text_only.strip(), " ".join(tags_only)

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

                # Process the JSON data to extract 'msg', 'text_', and 'tags_' events
                processed_data = []
                for msg in json_data:
                    if 'msg' in msg:
                        message_text = msg['msg']
                        text_only, tags_only = process_text_and_tags(message_text)
                        msg['text_'] = text_only
                        msg['tags_'] = tags_only
                        processed_data.append(msg)

                with open(output_file_path, 'w', encoding='utf-8') as f:
                    json.dump(processed_data, f, indent=2, ensure_ascii=False)

                print(f"Processed '{input_file_path}' -> '{output_file_path}'")

if __name__ == '__main__':
    input_folder = 'processed_json_v03'  # Replace with the path to your input folder
    output_folder = 'processed_json_v04'  # Replace with the desired output folder path
    process_json_files(input_folder, output_folder)
