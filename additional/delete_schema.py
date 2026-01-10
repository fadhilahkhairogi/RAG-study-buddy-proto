import weaviate

client = weaviate.Client("http://localhost:8080")

# Delete the old class (this removes all old vectors)
if client.schema.exists("Chunk"):
    client.schema.delete_class("Chunk")
    print("Old Chunk class deleted")
