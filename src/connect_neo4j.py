from neo4j import GraphDatabase
import os
import time

# Thông tin kết nối Neo4j
uri = "neo4j+s://ffdfad2c.databases.neo4j.io"  # Địa chỉ database
username = "neo4j"             # Username
password = "niQisz0U5weBUMit5DuSDTxMXmDsU91qykqIEOJTA4o"     # Password

# Hàm để xóa toàn bộ đồ thị
def delete_old_graph(tx):
    query = """
    MATCH (n)
    DETACH DELETE n
    """
    tx.run(query)

# Hàm để tạo đồ thị từ file Cypher
def create_graph(tx, file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        query = f.read()
    tx.run(query)

# Đường dẫn tới thư mục chứa các tệp Cypher
folder_path = r".\cypher_query_new"
file_list = os.listdir(folder_path)
print(len(file_list))

# Vòng lặp để xử lý các tệp Cypher
for index in range(22, len(file_list)):
    file_path = os.path.join(folder_path, f"cypher_query_{index+1}.txt")
    print(f"Processing file: {file_path}")

    driver = GraphDatabase.driver(uri, auth=(username, password), max_connection_lifetime=600)

    # Cố gắng kết nối và thực thi lệnh, nếu lỗi thì thử lại tối đa 3 lần
    retry_count = 0
    max_retries = 3
    success = False

    print("Processing...")
    while retry_count < max_retries and not success:
        try:
            with driver.session() as session:
                # session.execute_write(delete_old_graph)  # Nếu cần xóa đồ thị cũ
                session.execute_write(create_graph, file_path)
            success = True  # Nếu thực thi thành công, thoát vòng lặp
            print(f"Successfully processed file: {file_path}")
        except Exception as e:
            retry_count += 1
            print(f"Error processing file {file_path}, attempt {retry_count}/{max_retries}: {e}")
            if retry_count < max_retries:
                print(f"Retrying in 60 seconds...")
                time.sleep(60)  # Chờ 60 giây trước khi thử lại
            else:
                print(f"Failed to process file {file_path} after {max_retries} attempts. Skipping...")

    # Đóng kết nối sau khi hoàn tất (hoặc sau khi gặp lỗi quá nhiều lần)
    driver.close()
    time.sleep(240)  # Nghỉ 240 giây trước khi chuyển sang tệp tiếp theo
