from ingest.parse_pdf import extract_text
from chunking.chunker import chunk_paragraphs
from embedding.embedder import Embedder
from storage.weaviate_store import VectorStore
from retrieval.retriever import Retriever
from generation.answer import answer, answer_flexibly
import sys, os

PDF_ROOT = "datalake"

pdf_name = os.path.basename(sys.argv[1]).lower()
question = sys.argv[2]
pdf_path = os.path.join(PDF_ROOT, pdf_name)

store = VectorStore()

if store.has_paper(pdf_name):
    print(f"Document '{pdf_name}' already exists in the database. Skipping embedding.")
else:
    paras = extract_text(pdf_path)
    chunks = chunk_paragraphs(paras)

    embedder = Embedder()
    vectors = embedder.embed(chunks)

    store.add(chunks, vectors, paper_id=pdf_name)
    


retriever = Retriever(store, Embedder())
ctx = retriever.retrieve(question)

# print(answer(question, ctx))
print(answer_flexibly(question, ctx))
