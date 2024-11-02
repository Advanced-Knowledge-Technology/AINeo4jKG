import json

# # Dữ liệu gốc
# input_data = {
#     "isSymptomOf": [
#         "có triệu chứng", 
#         "triệu chứng của", 
#         "biểu hiện của", 
#         "dấu hiệu của", 
#         "triệu chứng"
#     ],
#     "causedBy": [
#         "gây ra bởi", 
#         "do", 
#         "nguyên nhân là", 
#         "được gây ra bởi"
#     ]
#     # Thêm các mối quan hệ khác nếu cần
# }
file_path = "./relation_text.json"
with open(file_path, 'r', encoding='utf-8') as f:
    input_data = json.load(f)
print(input_data)

# Khởi tạo dictionary kết quả
output_data = {}

# Lặp qua từng mối quan hệ và từ tương ứng để tạo key-value mới
for relation, phrases in input_data.items():
    for phrase in phrases:
        key = phrase.replace(" ", "_")  # Chuyển khoảng trắng thành dấu gạch dưới
        output_data[key] = relation

# Xuất kết quả
output_json = json.dumps(output_data, ensure_ascii=False, indent=4)
print(output_json)

# Nếu bạn muốn lưu lại thành file JSON
with open("output_relationships.json", "w", encoding="utf-8") as f:
    f.write(output_json)
