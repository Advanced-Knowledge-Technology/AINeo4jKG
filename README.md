# Step by Step

# Module 1: Từ text sang dư liệu và push lên neo4j

## Step 1: Từ file html (bị lỗi) sang file summary (done)
Sử dụng code trong file thucong.py 
Chuyển từ file trong thư mục corpus sang file trong thư mục corpus_clean

## Step 2: Sinh dữ liệu có cấu trúc từ file summary
Sử dụng code trong drive (Module 1)
Từ corpus_clean sang thư mục structure_data

## Step 3: Xử lý dữ liệu có cấu trúc thành câu lệnh cipher
Sử dụng code trong file create_cipher.py
Từ structure_data sang thư mục cypher_query

## Step 4: Thực hiện chạy các lệnh cypher để tạo đồ thị trên neo4j
Sử dụng code connect_neo4j.py
Từ thư mục cypher_query trở thành đồ thị trên neo4j

# Module 2: Trả lời câu hỏi query

## Step 1: Từ câu query split thành 2 phần chứa chủ ngữ và vị ngữ và tách object và relation và chuyển thành câu lệnh cypher
Sử dụng file query_to_cypher.py
Nhận vào một câu query và trả về câu lệnh cypher

## Step 2: Từ câu lệnh cypher thực hiện truy vấn trên neo4j lấy ra được full text trong các relationship
Sử dụng file node_from_cypher.py
Nhận vào một câu lệnh cypher thực hiện kết nối đồ thị và lấy các mối quan hệ trả về

## Step 3: Từ các text trong các mối quan hệ trả về thực hiện sắp xếp theo top 10 độ liên quan để làm passage cho LLM
Sử dụng file full_ques_answer.py
Nhận vào full text và query, trả về câu answer cho câu query dựa trên thông tin trong full text

# Conclusions
Module 1 có tất cả trong file class_text2neo4j.py
Module 2 có tất cả trong file class_QA_Neo4j.py
Các file tests của các module nằm trong thư mục tests