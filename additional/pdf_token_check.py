import fitz  # PyMuPDF
import tiktoken
import sys
import os

PDF_ROOT = "../datalake"  # folder where PDFs are stored

def main(pdf_name):
    pdf_path = os.path.join(PDF_ROOT, pdf_name)

    if not os.path.exists(pdf_path):
        print(f"PDF not found: {pdf_path}")
        return

    enc = tiktoken.get_encoding("cl100k_base")

    # Open PDF
    doc = fitz.open(pdf_path)
    total_words = 0
    total_tokens = 0
    paragraph_count = 0

    print(f"Checking PDF: {pdf_path}\n")

    for page_num, page in enumerate(doc, start=1):
        text_blocks = page.get_text("blocks")
        print(f"Page {page_num}: {len(text_blocks)} blocks found")

        for b in text_blocks:
            paragraph = b[4].strip()
            if len(paragraph) > 50:
                words = len(paragraph.split())
                tokens = len(enc.encode(paragraph))
                total_words += words
                total_tokens += tokens
                paragraph_count += 1
                print(f"Words: {words}, Tokens: {tokens} | {paragraph[:80]}...")

    print("\n=== PDF SUMMARY ===")
    print(f"Total paragraphs counted: {paragraph_count}")
    print(f"Total words: {total_words}")
    print(f"Total tokens (cl100k_base): {total_tokens}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_token_check.py <pdf_name_in_datalake>")
        sys.exit(1)

    pdf_name = sys.argv[1]
    main(pdf_name)
