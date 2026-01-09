import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

def chunk_paragraphs(paragraphs, max_tokens=250):
    chunks = []
    current = []

    for p in paragraphs:
        tokens = len(enc.encode(p))
        if tokens > max_tokens:
            continue

        current.append(p)
        if sum(len(enc.encode(x)) for x in current) > max_tokens:
            chunks.append(" ".join(current))
            current = []

    if current:
        chunks.append(" ".join(current))

    return chunks
