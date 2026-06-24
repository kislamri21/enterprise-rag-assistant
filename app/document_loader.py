def load_document(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def chunk_text(text: str, chunk_size: int = 500) -> list[str]:
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks
