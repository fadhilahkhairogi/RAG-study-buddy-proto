import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

def chunk_paragraphs(paragraphs, max_tokens=250, overlap=50):
    
    chunks = []

    for p in paragraphs:
        tokens = enc.encode(p)

        if len(tokens) <= max_tokens:
            chunks.append(p)
        else:
            start = 0
            while start < len(tokens):
                end = min(start + max_tokens, len(tokens))
                chunk_tokens = tokens[start:end]
                chunks.append(enc.decode(chunk_tokens))
                start += max_tokens - overlap  # slide window

    return chunks
