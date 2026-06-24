import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="enterprise_docs"
)


def add_documents(chunks):
    for index, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            ids=[f"doc_{index}"]
        )


def search_documents(question, n_results=3):
    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    return results["documents"][0]
