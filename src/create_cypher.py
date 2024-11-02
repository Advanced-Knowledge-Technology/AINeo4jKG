import pandas as pd
import json
import os

structure_folder_path = r".\structure_data_old"
full_data_structure = []
# file_structure_path = r".\structure_data\ung-thu-vom-hong-giai-doan-1.json"
for file_name in os.listdir(structure_folder_path):
    file_structure_path = os.path.join(structure_folder_path, file_name)

    with open(file_structure_path, 'r', encoding='utf-8') as f:
        data_structure = json.load(f)
    
    full_data_structure.extend(data_structure)

df = pd.DataFrame(full_data_structure)

unique_entities = set()
for item in full_data_structure:
    try:
        if 'head' not in item:
            item['head'] = item['text']
        unique_entities.add((item['head'].replace(" ","_").replace("-","").replace("'","").lower(), item['head_type']))
        unique_entities.add((item['tail'].replace(" ","_").replace("-","").replace("'","").lower(), item['tail_type']))
    except Exception as e:
        print("Error", e)
        print("Item", item)
        continue
unique_entities_list = list(unique_entities)
# print(unique_entities_list)

import os

# Đảm bảo thư mục tồn tại
output_dir = r"./cypher_query_old"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_count = 1  # Đếm số file
line_count = 0  # Đếm số dòng đã ghi trong file hiện tại
max_lines_per_file = 500  # Số dòng tối đa trong mỗi file

# Tạo tên file đầu tiên
file_path = os.path.join(output_dir, f"cypher_query_{file_count}.txt")
file = open(file_path, "a", encoding='utf-8')

for item in unique_entities_list:
    label, entity = item
    id = label.replace(" ","_").replace("-","").replace("'","").lower()
    merge_statement = f"""MERGE (`{id}_{entity}`:{entity} {{id: "{label}"}})\n"""
    
    # Kiểm tra xem có cần tạo file mới không
    if line_count >= max_lines_per_file:
        file.close()  # Đóng file hiện tại
        file_count += 1  # Tăng số file
        file_path = os.path.join(output_dir, f"cypher_query_{file_count}.txt")  # Tạo file mới
        file = open(file_path, "a", encoding='utf-8')  # Mở file mới
        line_count = 0  # Reset số dòng trong file mới
    
    file.write(merge_statement)
    line_count += 1  # Tăng số dòng đã ghi

for index, item in enumerate(full_data_structure):
    head = item['head'].replace(" ","_").replace("-","").replace("'","").lower()
    tail = item['tail'].replace(" ","_").replace("-","").replace("'","").lower()
    cypher = f"""MERGE (`{head}_{item['head_type']}`)-[r{index}:{item['relation']}]->(`{tail}_{item['tail_type']}`)\nSET r{index}.text = '{item['text']}'\n"""
    
    # Kiểm tra xem có cần tạo file mới không
    if line_count >= max_lines_per_file:
        file.close()  # Đóng file hiện tại
        file_count += 1  # Tăng số file
        file_path = os.path.join(output_dir, f"cypher_query_{file_count}.txt")  # Tạo file mới
        file = open(file_path, "a", encoding='utf-8')  # Mở file mới
        line_count = 0  # Reset số dòng trong file mới
    
    file.write(cypher)
    line_count += 2  # Tăng số dòng đã ghi

# Đóng file cuối cùng
file.close()
