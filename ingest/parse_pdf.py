import fitz  # PyMuPDF

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    blocks = []

    for page in doc:
        text = page.get_text("blocks")
        for b in text:
            blocks.append(b[4].strip())

    # return [b for b in blocks if len(b) > 50]
    return [b for b in blocks if len(b) > 30]
