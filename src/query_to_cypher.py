from neo4j import GraphDatabase

query = "Bệnh ung thư gan có triệu chứng và cách điều trị là gì?"

# Thông tin kết nối Neo4j
uri = "neo4j+s://ffdfad2c.databases.neo4j.io"                   # Địa chỉ database
username = "neo4j"                                              # Username
password = "niQisz0U5weBUMit5DuSDTxMXmDsU91qykqIEOJTA4o"        # Password

# Tạo driver kết nối
driver = GraphDatabase.driver(uri, auth=(username, password))

def query_subgraph(tx, objs, relations):
    # Trích xuất id từ objs
    ids = [obj['n']['id'] for obj in objs]
    
    # Tạo query động để match các relations
    query = """
    MATCH (n)-[r]-(related)
    WHERE n.id IN $ids AND type(r) IN $relations
    RETURN n.id AS node_id, r.text AS relationship_text, related.id AS related_id
    """
    result = tx.run(query, ids=ids, relations=relations)
    return [(record["node_id"], record["relationship_text"], record["related_id"]) for record in result]

# Đối tượng và mối quan hệ được cung cấp
objs = [{'n': {'id': 'ung_thư_gan_disease'}}]
relations = ['isSymptomOf', 'treatedBy']

# Mở session và thực hiện truy vấn
with driver.session() as session:
    subgraph_data = session.execute_read(query_subgraph, objs, relations)
    
    full_text = []
    set_text = set()
    # In ra kết quả các node và thuộc tính 'text' của mối quan hệ
    for node, relationship_text, related_node in subgraph_data:
        print(f"Node: {node}")
        print(f"Relationship: {relationship_text}")
        print(f"Related Node: {related_node}\n")
        if relationship_text not in set_text:
            set_text.add(relationship_text)
            full_text.append(f"Head: {node}\tTail: {related_node}\tText: {relationship_text}")
        
    for text in full_text:
        print("Text:", text)

    print(full_text)

# Đóng kết nối
driver.close()
