from neo4j import GraphDatabase

# Thông tin kết nối Neo4j
uri = "neo4j+s://ffdfad2c.databases.neo4j.io"                   # Địa chỉ database
username = "neo4j"                                              # Username
password = "niQisz0U5weBUMit5DuSDTxMXmDsU91qykqIEOJTA4o"        # Password

# Tạo driver kết nối
driver = GraphDatabase.driver(uri, auth=(username, password))

def query_graph_1_hop_with_text(tx):
    query = """
    MATCH (n)-[r]-(related)
    WHERE n.id CONTAINS "tuyến_thượng_thận"
    RETURN n, r.text AS relationship_text, related
    """
    result = tx.run(query)
    return [(record["n"], record["relationship_text"], record["related"]) for record in result]

# Mở session và thực hiện truy vấn
with driver.session() as session:
    graph_data = session.execute_read(query_graph_1_hop_with_text)
    
    set_text = set()
    # In ra kết quả các node và thuộc tính 'text' của mối quan hệ
    for node, relationship_text, related_node in graph_data:
        # print(f"Node: {node}")
        # print(f"Relationship Text: {relationship_text}")
        # print(f"Related Node: {related_node}\n")
        set_text.add(relationship_text)

    for text in set_text:
        print(f"Text: {text}")

# Đóng kết nối
driver.close()
