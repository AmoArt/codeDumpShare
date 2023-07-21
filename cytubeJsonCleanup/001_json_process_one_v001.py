import os
import json

def extract_tagged_messages(json_data):
    tagged_messages = []
    for event in json_data['eventsLog']:
        if event['type'] == 'chatMsg':
            tagged_messages.append({
                'username': event['data'][0]['username'],
                'msg': event['data'][0]['msg']
            })
    return tagged_messages

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

                tagged_messages = extract_tagged_messages(json_data)

                with open(output_file_path, 'w', encoding='utf-8') as f:
                    json.dump(tagged_messages, f, indent=2, ensure_ascii=False)

                print(f"Processed '{input_file_path}' -> '{output_file_path}'")

if __name__ == '__main__':
    input_folder = 'json_raw'  # Replace with the path to your input folder
    output_folder = 'processed_json'  # Replace with the desired output folder path
    process_json_files(input_folder, output_folder)
